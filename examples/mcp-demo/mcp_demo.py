#!/usr/bin/env python3
"""
MCP Demo — examples/mcp-demo/mcp_demo.py

Demonstrates a minimal Model Context Protocol (MCP) style tool server:
  - Declarative JSON-Schema tool definitions
  - Request/response envelope (mcp_call / mcp_result)
  - Input validation against declared schema
  - Read-only tools only (no filesystem writes, no shell exec)
  - Structured error passback

No external dependencies. Runs on Python 3.10+.

Usage:
    python examples/mcp-demo/mcp_demo.py
"""
from __future__ import annotations

import json
import math
import sys
from typing import Any

# ---------------------------------------------------------------------------
# Schema types
# ---------------------------------------------------------------------------

_PRIMITIVE_MAP: dict[str, type] = {
    "string": str,
    "number": float,
    "integer": int,
    "boolean": bool,
    "array": list,
    "object": dict,
}


def _coerce(value: Any, schema_type: str) -> Any:
    """Best-effort coercion of *value* to *schema_type*."""
    if schema_type == "number":
        return float(value)
    if schema_type == "integer":
        return int(value)
    if schema_type == "string":
        return str(value)
    if schema_type == "boolean":
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in {"true", "1", "yes"}
        return bool(value)
    return value


def validate_input(params_schema: dict[str, Any], raw: dict[str, Any]) -> dict[str, Any]:
    """
    Validate *raw* against a simplified JSON-Schema-style *params_schema*.

    params_schema format::

        {
            "properties": {
                "city": {"type": "string", "description": "..."},
                "units": {"type": "string", "description": "...", "default": "celsius"},
            },
            "required": ["city"],
        }

    Returns a validated and coerced copy, with defaults applied.
    Raises ValueError with a descriptive message on validation failure.
    """
    properties: dict[str, Any] = params_schema.get("properties", {})
    required: list[str] = params_schema.get("required", [])
    result: dict[str, Any] = {}

    # Check required
    for key in required:
        if key not in raw:
            raise ValueError(f"missing required parameter: {key!r}")

    for key, prop in properties.items():
        if key in raw:
            expected_type = prop.get("type", "string")
            py_type = _PRIMITIVE_MAP.get(expected_type)
            value = raw[key]
            if py_type and not isinstance(value, py_type):
                value = _coerce(value, expected_type)
            result[key] = value
        elif "default" in prop:
            result[key] = prop["default"]

    # Pass through any extra keys not in schema (permissive mode)
    for key in raw:
        if key not in result:
            result[key] = raw[key]

    return result


# ---------------------------------------------------------------------------
# Tool definitions
# ---------------------------------------------------------------------------

class Tool:
    def __init__(
        self,
        name: str,
        description: str,
        params_schema: dict[str, Any],
        fn: Any,
        *,
        read_only: bool = True,
    ) -> None:
        self.name = name
        self.description = description
        self.params_schema = params_schema
        self.fn = fn
        self.read_only = read_only

    def to_schema(self) -> dict[str, Any]:
        """Return the MCP-style tool definition dict."""
        return {
            "name": self.name,
            "description": self.description,
            "inputSchema": {
                "type": "object",
                **self.params_schema,
            },
        }


# ---------------------------------------------------------------------------
# Built-in read-only tools
# ---------------------------------------------------------------------------

_MOCK_WEATHER: dict[str, dict[str, Any]] = {
    "beijing": {"condition": "sunny", "temp_c": 28, "humidity_pct": 45},
    "shanghai": {"condition": "cloudy", "temp_c": 26, "humidity_pct": 72},
    "tokyo": {"condition": "rainy", "temp_c": 22, "humidity_pct": 88},
    "london": {"condition": "foggy", "temp_c": 15, "humidity_pct": 82},
    "new york": {"condition": "partly cloudy", "temp_c": 24, "humidity_pct": 60},
}


def _get_weather(city: str, units: str = "celsius") -> dict[str, Any]:
    key = city.lower().strip()
    data = _MOCK_WEATHER.get(key)
    if data is None:
        raise ValueError(f"no weather data for city: {city!r}")
    temp = data["temp_c"]
    if units == "fahrenheit":
        temp = round(temp * 9 / 5 + 32, 1)
    return {
        "city": city,
        "condition": data["condition"],
        "temperature": temp,
        "units": units,
        "humidity_pct": data["humidity_pct"],
    }


def _calculate(expression: str) -> dict[str, Any]:
    """
    Evaluate a safe arithmetic expression.

    Allowed: digits, +, -, *, /, **, (, ), ., spaces, sqrt, pi, e.
    Everything else raises ValueError.
    """
    import re

    cleaned = expression.strip()
    if not re.match(r"^[\d\s\+\-\*\/\(\)\.\*\*sqrtpie]+$", cleaned):
        raise ValueError(f"unsafe characters in expression: {expression!r}")
    ns: dict[str, Any] = {
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        "__builtins__": {},
    }
    try:
        result = eval(cleaned, ns)  # noqa: S307 — controlled allowlist above
    except Exception as exc:
        raise ValueError(f"invalid expression: {exc}") from exc
    return {"expression": expression, "result": result}


def _list_topics(category: str = "all") -> dict[str, Any]:
    """Return a static list of AI Agent learning topics."""
    all_topics = {
        "core": ["agent-loop", "tool-calling", "planning", "memory"],
        "protocols": ["mcp", "function-calling", "rag"],
        "patterns": ["react", "reflection", "multi-agent"],
    }
    if category == "all":
        return {"category": "all", "topics": all_topics}
    if category not in all_topics:
        raise ValueError(f"unknown category: {category!r}; valid: {sorted(all_topics)}")
    return {"category": category, "topics": {category: all_topics[category]}}


_TOOLS: dict[str, Tool] = {}


def _register_defaults() -> None:
    _TOOLS["get_weather"] = Tool(
        name="get_weather",
        description="Get current weather (mock data) for a city.",
        params_schema={
            "properties": {
                "city": {"type": "string", "description": "City name"},
                "units": {
                    "type": "string",
                    "description": "Temperature units: celsius or fahrenheit",
                    "default": "celsius",
                },
            },
            "required": ["city"],
        },
        fn=_get_weather,
    )
    _TOOLS["calculate"] = Tool(
        name="calculate",
        description="Evaluate a safe arithmetic expression (no code execution beyond math).",
        params_schema={
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Arithmetic expression, e.g. '2 * (3 + 4)'",
                },
            },
            "required": ["expression"],
        },
        fn=_calculate,
    )
    _TOOLS["list_topics"] = Tool(
        name="list_topics",
        description="List AI Agent learning topics by category.",
        params_schema={
            "properties": {
                "category": {
                    "type": "string",
                    "description": "core | protocols | patterns | all",
                    "default": "all",
                },
            },
            "required": [],
        },
        fn=_list_topics,
    )


_register_defaults()


# ---------------------------------------------------------------------------
# MCP protocol envelope
# ---------------------------------------------------------------------------

def mcp_call(tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    """
    Execute a tool call using MCP-style request/response format.

    Returns::

        {
            "tool": str,
            "arguments": dict,
            "ok": bool,
            "content": [{"type": "text", "text": str}],  # on success
            "isError": bool,                              # on failure
            "error": {"message": str, "type": str},       # on failure
        }
    """
    tool = _TOOLS.get(tool_name)
    if tool is None:
        known = sorted(_TOOLS)
        return {
            "tool": tool_name,
            "arguments": arguments,
            "ok": False,
            "isError": True,
            "error": {
                "message": f"unknown tool {tool_name!r}; available: {known}",
                "type": "UnknownToolError",
            },
        }

    try:
        validated = validate_input(tool.params_schema, arguments)
        result = tool.fn(**validated)
        text = json.dumps(result, ensure_ascii=False, indent=2)
        return {
            "tool": tool_name,
            "arguments": arguments,
            "ok": True,
            "isError": False,
            "content": [{"type": "text", "text": text}],
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "tool": tool_name,
            "arguments": arguments,
            "ok": False,
            "isError": True,
            "error": {"message": str(exc), "type": type(exc).__name__},
        }


def list_tools() -> list[dict[str, Any]]:
    """Return MCP-style tool list."""
    return [t.to_schema() for t in sorted(_TOOLS.values(), key=lambda t: t.name)]


# ---------------------------------------------------------------------------
# Main demo
# ---------------------------------------------------------------------------

def main() -> None:
    print("=== MCP Demo ===\n")

    # 1. List available tools
    print("Available tools:")
    for spec in list_tools():
        print(f"  {spec['name']:20s} — {spec['description']}")
    print()

    # 2. Demo calls
    demo_calls: list[tuple[str, dict[str, Any]]] = [
        ("get_weather", {"city": "Tokyo"}),
        ("get_weather", {"city": "London", "units": "fahrenheit"}),
        ("calculate", {"expression": "sqrt(16) + 2 ** 3"}),
        ("list_topics", {"category": "protocols"}),
        ("list_topics", {}),
        # Error cases
        ("get_weather", {"city": "Atlantis"}),
        ("calculate", {"expression": "import os"}),
        ("unknown_tool", {}),
    ]

    for tool_name, args in demo_calls:
        resp = mcp_call(tool_name, args)
        if resp["ok"]:
            print(f"[OK]    {tool_name}({args})")
            print(f"        {resp['content'][0]['text'][:120]}")
        else:
            print(f"[ERROR] {tool_name}({args})")
            print(f"        {resp['error']['type']}: {resp['error']['message'][:100]}")
        print()


if __name__ == "__main__":
    main()

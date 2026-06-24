#!/usr/bin/env python3
"""
Tool-Calling Demo — examples/tool-calling-demo/demo.py

Demonstrates: ToolRegistry, JSON-schema-style param validation,
              tool execution, structured error passback, and call logging.

No external dependencies. Runs on Python 3.10+.

Usage:
    python examples/tool-calling-demo/demo.py
"""
from __future__ import annotations

import sys
import time
from dataclasses import dataclass, field
from typing import Any, Callable


# ---------------------------------------------------------------------------
# Param and ToolSpec
# ---------------------------------------------------------------------------

@dataclass
class Param:
    name: str
    type_: type
    required: bool = True
    description: str = ""


@dataclass
class ToolSpec:
    name: str
    description: str
    params: list[Param]
    fn: Callable[..., Any]
    safe: bool = True  # read-only / non-destructive


# ---------------------------------------------------------------------------
# ToolRegistry
# ---------------------------------------------------------------------------

class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ToolSpec] = {}
        self._log: list[dict[str, Any]] = []

    def register(self, spec: ToolSpec) -> None:
        self._tools[spec.name] = spec

    def names(self) -> list[str]:
        """Return all registered tool names, sorted."""
        return sorted(self._tools)

    def execute(self, name: str, args: dict[str, Any]) -> dict[str, Any]:
        """
        Execute a tool by name with the given args dict.

        Always returns a record dict with keys:
          tool, args, ok (bool), result (value or error dict), latency_ms
        The call is appended to the internal log regardless of outcome.
        """
        t0 = time.monotonic()
        record: dict[str, Any] = {"tool": name, "args": args}
        try:
            spec = self._tools.get(name)
            if spec is None:
                raise KeyError(f"unknown tool {name!r}")
            validated = _validate_args(spec, args)
            record["result"] = spec.fn(**validated)
            record["ok"] = True
        except Exception as exc:  # noqa: BLE001
            record["ok"] = False
            record["result"] = {"error": str(exc), "type": type(exc).__name__}
        record["latency_ms"] = round((time.monotonic() - t0) * 1000, 2)
        self._log.append(record)
        return record

    def log(self) -> list[dict[str, Any]]:
        """Return a copy of all recorded call entries."""
        return list(self._log)


def _validate_args(spec: ToolSpec, args: dict[str, Any]) -> dict[str, Any]:
    """
    Validate and coerce args against the spec's param definitions.

    Raises TypeError for missing required params or type-coercion failures.
    """
    out: dict[str, Any] = {}
    for p in spec.params:
        if p.name not in args:
            if p.required:
                raise TypeError(f"missing required param {p.name!r}")
            continue
        try:
            out[p.name] = p.type_(args[p.name])
        except (ValueError, TypeError) as exc:
            raise TypeError(
                f"param {p.name!r}: expected {p.type_.__name__}, "
                f"got {args[p.name]!r}: {exc}"
            ) from exc
    return out


# ---------------------------------------------------------------------------
# Built-in tools
# ---------------------------------------------------------------------------

def _add(a: float, b: float) -> float:
    return a + b


def _multiply(a: float, b: float) -> float:
    return a * b


def _word_count(text: str) -> int:
    return len(text.split())


def _truncate(text: str, max_chars: int) -> str:
    n = int(max_chars)
    return text[:n] + ("..." if len(text) > n else "")


def build_registry() -> ToolRegistry:
    """Return a ToolRegistry pre-loaded with the built-in tools."""
    registry = ToolRegistry()
    registry.register(ToolSpec(
        name="add",
        description="Return the sum of two numbers.",
        params=[Param("a", float), Param("b", float)],
        fn=_add,
    ))
    registry.register(ToolSpec(
        name="multiply",
        description="Return the product of two numbers.",
        params=[Param("a", float), Param("b", float)],
        fn=_multiply,
    ))
    registry.register(ToolSpec(
        name="word_count",
        description="Return the number of words in a string.",
        params=[Param("text", str)],
        fn=_word_count,
    ))
    registry.register(ToolSpec(
        name="truncate",
        description="Truncate a string to at most max_chars characters.",
        params=[Param("text", str), Param("max_chars", int)],
        fn=_truncate,
    ))
    return registry


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    registry = build_registry()

    calls: list[tuple[str, dict[str, Any]]] = [
        ("add",        {"a": 3, "b": 4}),
        ("multiply",   {"a": 6, "b": 7}),
        ("word_count", {"text": "the quick brown fox"}),
        ("truncate",   {"text": "Hello, world!", "max_chars": 5}),
        ("truncate",   {"text": "Hi", "max_chars": 10}),
        ("add",        {"a": "not_a_number", "b": 1}),  # type error -> error passback
        ("unknown",    {}),                              # unknown tool -> error passback
    ]

    print(f"Registered tools: {registry.names()}\n")
    for name, args in calls:
        record = registry.execute(name, args)
        status = "ok " if record["ok"] else "err"
        print(f"[{status}] {name}({args}) -> {record['result']}  ({record['latency_ms']} ms)")

    print(f"\n{len(registry.log())} calls logged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

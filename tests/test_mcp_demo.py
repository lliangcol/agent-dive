"""Tests for examples/mcp-demo/mcp_demo.py"""
from __future__ import annotations

import math
import runpy
import sys
from pathlib import Path
from typing import Any

import pytest

# Make the example importable without installing
sys.path.insert(0, str(Path(__file__).parent.parent / "examples" / "mcp-demo"))
import mcp_demo as mcp  # noqa: E402


# ---------------------------------------------------------------------------
# validate_input
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# _coerce (direct)
# ---------------------------------------------------------------------------

class TestCoerce:
    def test_number_from_string(self):
        assert mcp._coerce("3.14", "number") == 3.14

    def test_integer_from_string(self):
        assert mcp._coerce("7", "integer") == 7

    def test_string_from_int(self):
        assert mcp._coerce(42, "string") == "42"

    def test_bool_passthrough_true(self):
        assert mcp._coerce(True, "boolean") is True

    def test_bool_passthrough_false(self):
        assert mcp._coerce(False, "boolean") is False

    def test_bool_from_int(self):
        assert mcp._coerce(1, "boolean") is True
        assert mcp._coerce(0, "boolean") is False

    def test_bool_from_string_true(self):
        assert mcp._coerce("yes", "boolean") is True

    def test_bool_from_string_false(self):
        assert mcp._coerce("false", "boolean") is False

    def test_unknown_type_passthrough(self):
        obj = {"x": 1}
        assert mcp._coerce(obj, "array") is obj


class TestValidateInput:
    _SCHEMA: dict[str, Any] = {
        "properties": {
            "city": {"type": "string"},
            "units": {"type": "string", "default": "celsius"},
        },
        "required": ["city"],
    }

    def test_valid_full(self):
        r = mcp.validate_input(self._SCHEMA, {"city": "Tokyo", "units": "fahrenheit"})
        assert r == {"city": "Tokyo", "units": "fahrenheit"}

    def test_default_applied(self):
        r = mcp.validate_input(self._SCHEMA, {"city": "Tokyo"})
        assert r["units"] == "celsius"

    def test_missing_required_raises(self):
        with pytest.raises(ValueError, match="missing required parameter"):
            mcp.validate_input(self._SCHEMA, {})

    def test_extra_keys_passed_through(self):
        r = mcp.validate_input(self._SCHEMA, {"city": "Tokyo", "extra": 42})
        assert r["extra"] == 42

    def test_type_coercion_string_to_int(self):
        schema = {"properties": {"count": {"type": "integer"}}, "required": ["count"]}
        r = mcp.validate_input(schema, {"count": "5"})
        assert r["count"] == 5

    def test_type_coercion_string_to_float(self):
        schema = {"properties": {"val": {"type": "number"}}, "required": ["val"]}
        r = mcp.validate_input(schema, {"val": "3.14"})
        assert abs(r["val"] - 3.14) < 1e-9

    def test_type_coercion_bool_from_string_true(self):
        schema = {"properties": {"flag": {"type": "boolean"}}, "required": ["flag"]}
        r = mcp.validate_input(schema, {"flag": "true"})
        assert r["flag"] is True

    def test_type_coercion_bool_from_string_false(self):
        schema = {"properties": {"flag": {"type": "boolean"}}, "required": ["flag"]}
        r = mcp.validate_input(schema, {"flag": "false"})
        assert r["flag"] is False

    def test_bool_passthrough(self):
        schema = {"properties": {"flag": {"type": "boolean"}}, "required": ["flag"]}
        r = mcp.validate_input(schema, {"flag": True})
        assert r["flag"] is True

    def test_empty_schema(self):
        r = mcp.validate_input({}, {"x": 1})
        assert r == {"x": 1}

    def test_no_required_key(self):
        schema = {"properties": {"opt": {"type": "string", "default": "hi"}}, "required": []}
        r = mcp.validate_input(schema, {})
        assert r["opt"] == "hi"


# ---------------------------------------------------------------------------
# _get_weather
# ---------------------------------------------------------------------------

class TestGetWeather:
    def test_celsius_default(self):
        r = mcp._get_weather("Tokyo")
        assert r["city"] == "Tokyo"
        assert r["temperature"] == 22
        assert r["units"] == "celsius"

    def test_fahrenheit(self):
        r = mcp._get_weather("London", units="fahrenheit")
        assert r["units"] == "fahrenheit"
        assert abs(r["temperature"] - (15 * 9 / 5 + 32)) < 0.1

    def test_case_insensitive(self):
        r = mcp._get_weather("BEIJING")
        assert r["condition"] == "sunny"

    def test_unknown_city_raises(self):
        with pytest.raises(ValueError, match="no weather data"):
            mcp._get_weather("Atlantis")

    def test_all_cities_present(self):
        for city in ["beijing", "shanghai", "tokyo", "london", "new york"]:
            r = mcp._get_weather(city)
            assert "condition" in r


# ---------------------------------------------------------------------------
# _calculate
# ---------------------------------------------------------------------------

class TestCalculate:
    def test_simple_addition(self):
        r = mcp._calculate("2 + 3")
        assert r["result"] == 5

    def test_multiplication(self):
        r = mcp._calculate("4 * 5")
        assert r["result"] == 20

    def test_power(self):
        r = mcp._calculate("2 ** 10")
        assert r["result"] == 1024

    def test_sqrt(self):
        r = mcp._calculate("sqrt(16)")
        assert abs(r["result"] - 4.0) < 1e-9

    def test_pi(self):
        r = mcp._calculate("pi")
        assert abs(r["result"] - math.pi) < 1e-9

    def test_expression_key_returned(self):
        r = mcp._calculate("1 + 1")
        assert r["expression"] == "1 + 1"

    def test_import_blocked(self):
        with pytest.raises(ValueError, match="unsafe characters"):
            mcp._calculate("import os")

    def test_semicolon_blocked(self):
        with pytest.raises(ValueError, match="unsafe characters"):
            mcp._calculate("1; 2")

    def test_invalid_expression_raises(self):
        with pytest.raises(ValueError, match="invalid expression"):
            mcp._calculate("(((")

    def test_combined_expression(self):
        r = mcp._calculate("sqrt(16) + 2 ** 3")
        assert abs(r["result"] - 12.0) < 1e-9


# ---------------------------------------------------------------------------
# _list_topics
# ---------------------------------------------------------------------------

class TestListTopics:
    def test_all_categories(self):
        r = mcp._list_topics()
        assert r["category"] == "all"
        assert "core" in r["topics"]
        assert "protocols" in r["topics"]
        assert "patterns" in r["topics"]

    def test_specific_category(self):
        r = mcp._list_topics("protocols")
        assert "mcp" in r["topics"]["protocols"]

    def test_unknown_category_raises(self):
        with pytest.raises(ValueError, match="unknown category"):
            mcp._list_topics("nonexistent")

    def test_core_category(self):
        r = mcp._list_topics("core")
        assert "agent-loop" in r["topics"]["core"]


# ---------------------------------------------------------------------------
# Tool.to_schema
# ---------------------------------------------------------------------------

class TestToolSchema:
    def test_to_schema_structure(self):
        tool = mcp._TOOLS["get_weather"]
        schema = tool.to_schema()
        assert schema["name"] == "get_weather"
        assert "description" in schema
        assert schema["inputSchema"]["type"] == "object"
        assert "properties" in schema["inputSchema"]

    def test_read_only_flag(self):
        for tool in mcp._TOOLS.values():
            assert tool.read_only is True


# ---------------------------------------------------------------------------
# list_tools
# ---------------------------------------------------------------------------

class TestListTools:
    def test_returns_list(self):
        tools = mcp.list_tools()
        assert isinstance(tools, list)

    def test_all_tools_included(self):
        names = {t["name"] for t in mcp.list_tools()}
        assert "get_weather" in names
        assert "calculate" in names
        assert "list_topics" in names

    def test_sorted_by_name(self):
        names = [t["name"] for t in mcp.list_tools()]
        assert names == sorted(names)


# ---------------------------------------------------------------------------
# mcp_call
# ---------------------------------------------------------------------------

class TestMcpCall:
    def test_success_weather(self):
        r = mcp.mcp_call("get_weather", {"city": "Tokyo"})
        assert r["ok"] is True
        assert r["isError"] is False
        assert r["content"][0]["type"] == "text"
        assert "Tokyo" in r["content"][0]["text"]

    def test_success_calculate(self):
        r = mcp.mcp_call("calculate", {"expression": "2 + 2"})
        assert r["ok"] is True
        assert "4" in r["content"][0]["text"]

    def test_success_list_topics_default(self):
        r = mcp.mcp_call("list_topics", {})
        assert r["ok"] is True
        assert "mcp" in r["content"][0]["text"]

    def test_unknown_tool(self):
        r = mcp.mcp_call("does_not_exist", {})
        assert r["ok"] is False
        assert r["isError"] is True
        assert r["error"]["type"] == "UnknownToolError"
        assert "available" in r["error"]["message"]

    def test_missing_required_param(self):
        r = mcp.mcp_call("get_weather", {})
        assert r["ok"] is False
        assert "city" in r["error"]["message"]

    def test_tool_raises_value_error(self):
        r = mcp.mcp_call("get_weather", {"city": "Nowhere"})
        assert r["ok"] is False
        assert r["error"]["type"] == "ValueError"

    def test_calculate_unsafe_expression(self):
        r = mcp.mcp_call("calculate", {"expression": "os.system('x')"})
        assert r["ok"] is False

    def test_arguments_echoed_on_success(self):
        args = {"city": "Tokyo"}
        r = mcp.mcp_call("get_weather", args)
        assert r["arguments"] == args

    def test_arguments_echoed_on_failure(self):
        args = {"city": "Nowhere"}
        r = mcp.mcp_call("get_weather", args)
        assert r["arguments"] == args

    def test_tool_name_in_response(self):
        r = mcp.mcp_call("calculate", {"expression": "1"})
        assert r["tool"] == "calculate"

    def test_units_fahrenheit_via_mcp(self):
        r = mcp.mcp_call("get_weather", {"city": "Beijing", "units": "fahrenheit"})
        assert r["ok"] is True
        import json as _json
        data = _json.loads(r["content"][0]["text"])
        assert data["units"] == "fahrenheit"


# ---------------------------------------------------------------------------
# main()
# ---------------------------------------------------------------------------

class TestMain:
    def test_main_runs(self, capsys):
        mcp.main()
        out = capsys.readouterr().out
        assert "MCP Demo" in out
        assert "Available tools" in out
        assert "[OK]" in out
        assert "[ERROR]" in out

    def test_main_shows_all_tools(self, capsys):
        mcp.main()
        out = capsys.readouterr().out
        assert "get_weather" in out
        assert "calculate" in out
        assert "list_topics" in out

    def test_main_shows_error_cases(self, capsys):
        mcp.main()
        out = capsys.readouterr().out
        assert "UnknownToolError" in out
        assert "ValueError" in out


# ---------------------------------------------------------------------------
# __main__ via runpy
# ---------------------------------------------------------------------------

_SCRIPT = Path(__file__).parent.parent / "examples" / "mcp-demo" / "mcp_demo.py"


def test_dunder_main_via_runpy(capsys):
    runpy.run_path(str(_SCRIPT), run_name="__main__")
    out = capsys.readouterr().out
    assert "MCP Demo" in out

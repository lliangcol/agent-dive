"""Unit tests for examples/tool-calling-demo/demo.py"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

_DEMO = Path(__file__).resolve().parents[1] / "examples" / "tool-calling-demo" / "demo.py"
_spec = importlib.util.spec_from_file_location("tool_calling_demo", _DEMO)
_mod = importlib.util.module_from_spec(_spec)
sys.modules["tool_calling_demo"] = _mod  # required for dataclasses to resolve __module__
_spec.loader.exec_module(_mod)

Param = _mod.Param
ToolSpec = _mod.ToolSpec
ToolRegistry = _mod.ToolRegistry
build_registry = _mod.build_registry
_validate_args = _mod._validate_args


# ---------------------------------------------------------------------------
# Registration and listing
# ---------------------------------------------------------------------------

def test_build_registry_has_expected_tools():
    reg = build_registry()
    assert set(reg.names()) == {"add", "multiply", "word_count", "truncate"}


def test_names_are_sorted():
    reg = build_registry()
    assert reg.names() == sorted(reg.names())


def test_register_custom_tool():
    reg = ToolRegistry()
    reg.register(ToolSpec(
        name="noop",
        description="Does nothing.",
        params=[],
        fn=lambda: None,
    ))
    assert "noop" in reg.names()


# ---------------------------------------------------------------------------
# Successful execution
# ---------------------------------------------------------------------------

def test_execute_add():
    reg = build_registry()
    r = reg.execute("add", {"a": 3, "b": 4})
    assert r["ok"] is True
    assert r["result"] == 7.0


def test_execute_multiply():
    reg = build_registry()
    r = reg.execute("multiply", {"a": 6, "b": 7})
    assert r["ok"] is True
    assert r["result"] == 42.0


def test_execute_word_count():
    reg = build_registry()
    r = reg.execute("word_count", {"text": "the quick brown fox"})
    assert r["ok"] is True
    assert r["result"] == 4


def test_execute_truncate_long():
    reg = build_registry()
    r = reg.execute("truncate", {"text": "Hello, world!", "max_chars": 5})
    assert r["ok"] is True
    assert r["result"] == "Hello..."


def test_execute_truncate_short():
    reg = build_registry()
    r = reg.execute("truncate", {"text": "Hi", "max_chars": 10})
    assert r["ok"] is True
    assert r["result"] == "Hi"


# ---------------------------------------------------------------------------
# Type coercion
# ---------------------------------------------------------------------------

def test_execute_coerces_string_to_float():
    reg = build_registry()
    r = reg.execute("add", {"a": "3", "b": "4"})
    assert r["ok"] is True
    assert r["result"] == 7.0


def test_execute_coerces_float_string_to_int_for_truncate():
    reg = build_registry()
    r = reg.execute("truncate", {"text": "Hello!", "max_chars": "3"})
    assert r["ok"] is True
    assert r["result"] == "Hel..."


# ---------------------------------------------------------------------------
# Error passback
# ---------------------------------------------------------------------------

def test_execute_unknown_tool_returns_error_passback():
    reg = build_registry()
    r = reg.execute("no_such_tool", {})
    assert r["ok"] is False
    assert "error" in r["result"]
    assert "unknown tool" in r["result"]["error"]


def test_execute_bad_type_returns_error_passback():
    reg = build_registry()
    r = reg.execute("add", {"a": "not_a_number", "b": 1})
    assert r["ok"] is False
    assert r["result"]["type"] == "TypeError"
    assert "param" in r["result"]["error"]


def test_execute_missing_required_param_returns_error_passback():
    reg = build_registry()
    r = reg.execute("add", {"a": 3})  # b missing
    assert r["ok"] is False
    assert "missing required param" in r["result"]["error"]


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

def test_log_accumulates_entries():
    reg = build_registry()
    reg.execute("add", {"a": 1, "b": 2})
    reg.execute("multiply", {"a": 2, "b": 3})
    assert len(reg.log()) == 2


def test_log_entry_has_latency():
    reg = build_registry()
    reg.execute("add", {"a": 1, "b": 2})
    entry = reg.log()[0]
    assert "latency_ms" in entry
    assert entry["latency_ms"] >= 0


def test_log_entry_contains_tool_name_and_args():
    reg = build_registry()
    reg.execute("word_count", {"text": "hello world"})
    entry = reg.log()[0]
    assert entry["tool"] == "word_count"
    assert entry["args"] == {"text": "hello world"}


def test_log_returns_copy_not_reference():
    reg = build_registry()
    reg.execute("add", {"a": 1, "b": 2})
    snapshot = reg.log()
    snapshot.append({"dummy": True})
    assert len(reg.log()) == 1  # internal log not modified


def test_failed_call_still_logged():
    reg = build_registry()
    reg.execute("no_such_tool", {})
    assert len(reg.log()) == 1
    assert reg.log()[0]["ok"] is False


# ---------------------------------------------------------------------------
# _validate_args
# ---------------------------------------------------------------------------

def test_validate_optional_param_absent_is_allowed():
    spec = ToolSpec(
        name="test",
        description="",
        params=[Param("a", int), Param("b", int, required=False)],
        fn=lambda a: a,
    )
    validated = _validate_args(spec, {"a": 5})
    assert validated == {"a": 5}
    assert "b" not in validated


def test_validate_required_param_missing_raises():
    spec = ToolSpec(
        name="test",
        description="",
        params=[Param("x", str)],
        fn=lambda x: x,
    )
    with pytest.raises(TypeError, match="missing required param"):
        _validate_args(spec, {})


# ---------------------------------------------------------------------------
# __main__ subprocess
# ---------------------------------------------------------------------------

def test_runs_as_script():
    result = subprocess.run(
        [sys.executable, str(_DEMO)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Registered tools:" in result.stdout
    assert "calls logged" in result.stdout
    assert "[ok ]" in result.stdout
    assert "[err]" in result.stdout

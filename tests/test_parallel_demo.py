"""Unit tests for examples/tool-calling-demo/parallel_demo.py"""

from __future__ import annotations

import importlib.util
import runpy
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

_PARALLEL = (
    Path(__file__).resolve().parents[1]
    / "examples"
    / "tool-calling-demo"
    / "parallel_demo.py"
)

_spec = importlib.util.spec_from_file_location("parallel_demo", _PARALLEL)
_mod = importlib.util.module_from_spec(_spec)  # type: ignore[arg-type]
sys.modules["parallel_demo"] = _mod
_spec.loader.exec_module(_mod)  # type: ignore[union-attr]

build_registry = _mod.build_registry
dispatch_parallel = _mod.dispatch_parallel
ToolRegistry = _mod.ToolRegistry


# ---------------------------------------------------------------------------
# dispatch_parallel — happy path
# ---------------------------------------------------------------------------

def test_dispatch_returns_correct_count():
    reg = build_registry()
    calls = [("add", {"a": 1, "b": 2}), ("multiply", {"a": 3, "b": 4})]
    results = dispatch_parallel(reg, calls)
    assert len(results) == 2


def test_dispatch_preserves_order():
    reg = build_registry()
    calls = [
        ("add",      {"a": 10, "b": 20}),
        ("multiply", {"a": 6,  "b": 7}),
        ("add",      {"a": 1,  "b": 1}),
    ]
    results = dispatch_parallel(reg, calls)
    assert results[0]["result"] == 30.0
    assert results[1]["result"] == 42.0
    assert results[2]["result"] == 2.0


def test_dispatch_all_ok():
    reg = build_registry()
    calls = [
        ("add",        {"a": 5,   "b": 5}),
        ("word_count", {"text":   "hello world"}),
    ]
    results = dispatch_parallel(reg, calls)
    assert all(r["ok"] for r in results)


def test_dispatch_word_count_value():
    reg = build_registry()
    results = dispatch_parallel(reg, [("word_count", {"text": "a b c d"})])
    assert results[0]["result"] == 4


def test_dispatch_add_value():
    reg = build_registry()
    results = dispatch_parallel(reg, [("add", {"a": 100, "b": 200})])
    assert results[0]["result"] == 300.0


def test_dispatch_multiply_value():
    reg = build_registry()
    results = dispatch_parallel(reg, [("multiply", {"a": 6, "b": 7})])
    assert results[0]["result"] == 42.0


# ---------------------------------------------------------------------------
# dispatch_parallel — error passback
# ---------------------------------------------------------------------------

def test_dispatch_unknown_tool_returns_error_record():
    reg = build_registry()
    results = dispatch_parallel(reg, [("no_such_tool", {})])
    assert results[0]["ok"] is False
    assert "error" in results[0]["result"]


def test_dispatch_bad_args_returns_error_record():
    reg = build_registry()
    results = dispatch_parallel(reg, [("add", {"a": "not_a_number", "b": 1})])
    assert results[0]["ok"] is False
    assert results[0]["result"]["type"] == "TypeError"


def test_dispatch_mixed_ok_and_error():
    reg = build_registry()
    calls = [
        ("add",      {"a": 1, "b": 2}),
        ("unknown",  {}),
    ]
    results = dispatch_parallel(reg, calls)
    assert results[0]["ok"] is True
    assert results[1]["ok"] is False


# ---------------------------------------------------------------------------
# dispatch_parallel — registry log integration
# ---------------------------------------------------------------------------

def test_dispatch_logs_all_calls():
    reg = build_registry()
    calls = [("add", {"a": i, "b": i}) for i in range(5)]
    dispatch_parallel(reg, calls)
    assert len(reg.log()) == 5


def test_dispatch_failed_call_still_logged():
    reg = build_registry()
    dispatch_parallel(reg, [("unknown_tool", {})])
    assert len(reg.log()) == 1
    assert reg.log()[0]["ok"] is False


# ---------------------------------------------------------------------------
# dispatch_parallel — edge cases
# ---------------------------------------------------------------------------

def test_dispatch_empty_batch_returns_empty_list():
    reg = build_registry()
    results = dispatch_parallel(reg, [])
    assert results == []


def test_dispatch_single_call():
    reg = build_registry()
    results = dispatch_parallel(reg, [("add", {"a": 7, "b": 8})])
    assert len(results) == 1
    assert results[0]["result"] == 15.0


def test_dispatch_max_workers_one_still_works():
    reg = build_registry()
    calls = [("add", {"a": i, "b": i}) for i in range(3)]
    results = dispatch_parallel(reg, calls, max_workers=1)
    assert len(results) == 3
    assert all(r["ok"] for r in results)


def test_dispatch_large_batch_preserves_order():
    reg = build_registry()
    n = 20
    calls = [("add", {"a": float(i), "b": 0.0}) for i in range(n)]
    results = dispatch_parallel(reg, calls)
    for i, r in enumerate(results):
        assert r["result"] == float(i), f"index {i}: expected {float(i)}, got {r['result']}"


# ---------------------------------------------------------------------------
# main() entry point
# ---------------------------------------------------------------------------

def test_main_returns_zero():
    assert _mod.main() == 0


# ---------------------------------------------------------------------------
# __main__ subprocess
# ---------------------------------------------------------------------------

def test_runs_as_script():
    result = subprocess.run(
        [sys.executable, str(_PARALLEL)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Dispatching" in result.stdout
    assert "calls completed" in result.stdout
    assert "[ok ]" in result.stdout


def test_main_block_via_runpy():
    """Cover sys.exit(main()) on line 101 using runpy in-process."""
    with pytest.raises(SystemExit) as exc:
        runpy.run_path(str(_PARALLEL), run_name="__main__")
    assert exc.value.code == 0

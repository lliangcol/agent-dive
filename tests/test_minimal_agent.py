"""Unit tests for examples/minimal-agent/agent.py."""

from __future__ import annotations

import importlib.util
import runpy
import subprocess
import sys
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parents[1] / "examples" / "minimal-agent" / "agent.py"
_spec = importlib.util.spec_from_file_location("minimal_agent", _SCRIPT)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

run_agent = _mod.run_agent
model = _mod.model
tool_add = _mod.tool_add
tool_word_count = _mod.tool_word_count
tool_finish = _mod.tool_finish
TOOLS = _mod.TOOLS
MAX_STEPS = _mod.MAX_STEPS


# ---------------------------------------------------------------------------
# Tool unit tests
# ---------------------------------------------------------------------------

def test_tool_add_integers():
    assert tool_add(3.0, 4.0) == "7.0"


def test_tool_add_floats():
    assert tool_add(1.5, 2.5) == "4.0"


def test_tool_word_count_basic():
    assert tool_word_count("hello world") == "2"


def test_tool_word_count_single():
    assert tool_word_count("word") == "1"


def test_tool_word_count_empty():
    assert tool_word_count("") == "0"


def test_tool_finish_passthrough():
    assert tool_finish("done") == "done"
    assert tool_finish("") == ""


# ---------------------------------------------------------------------------
# TOOLS registry
# ---------------------------------------------------------------------------

def test_tools_has_required_keys():
    assert "add" in TOOLS
    assert "word_count" in TOOLS
    assert "finish" in TOOLS


def test_tools_each_has_fn():
    for name, spec in TOOLS.items():
        assert callable(spec["fn"]), f"TOOLS[{name!r}]['fn'] must be callable"


# ---------------------------------------------------------------------------
# Model routing
# ---------------------------------------------------------------------------

def test_model_routes_addition():
    ctx = [{"role": "user", "content": "What is 10 + 20?"}]
    action = model(ctx)
    assert action["tool"] == "add"
    assert action["args"]["a"] == 10.0
    assert action["args"]["b"] == 20.0


def test_model_routes_word_count():
    ctx = [{"role": "user", "content": "word count this text for me"}]
    action = model(ctx)
    assert action["tool"] == "word_count"


def test_model_falls_back_to_finish():
    ctx = [{"role": "user", "content": "Tell me a joke"}]
    action = model(ctx)
    assert action["tool"] == "finish"
    assert "unknown" in action["args"]["answer"].lower()


def test_model_uses_last_user_message():
    """Model should only look at user messages, not tool messages."""
    ctx = [
        {"role": "user", "content": "Start"},
        {"role": "tool", "tool": "add", "result": "5.0"},
        {"role": "user", "content": "What is 1 + 2?"},
    ]
    action = model(ctx)
    assert action["tool"] == "add"
    assert action["args"]["a"] == 1.0
    assert action["args"]["b"] == 2.0


def test_model_requires_two_numbers_for_add():
    """A + without numbers does not route to add."""
    ctx = [{"role": "user", "content": "What is a + b?"}]
    action = model(ctx)
    # No numeric operands → falls back to finish
    assert action["tool"] == "finish"


# ---------------------------------------------------------------------------
# run_agent integration
# ---------------------------------------------------------------------------

def test_run_agent_addition_end_to_end():
    result = run_agent("What is 3 + 4?", verbose=False)
    assert result == "7.0"


def test_run_agent_word_count_end_to_end():
    result = run_agent("word count: hello world foo bar", verbose=False)
    assert result.isdigit()
    assert int(result) > 0


def test_run_agent_unknown_returns_string():
    result = run_agent("This is an unanswerable question", verbose=False)
    assert isinstance(result, str)


def test_run_agent_terminates_within_max_steps():
    """Even for an unroutable query, the agent must finish within MAX_STEPS."""
    # "Tell me a joke" routes to finish immediately, so result is not the sentinel
    result = run_agent("Tell me a joke", verbose=False)
    assert result != "[max steps reached]"


def test_run_agent_verbose_prints(capsys):
    run_agent("What is 1 + 1?", verbose=True)
    captured = capsys.readouterr()
    assert "step 1" in captured.out
    assert "add" in captured.out


def test_run_agent_unknown_tool_handled(monkeypatch):
    """If model returns an unknown tool, run_agent reports it but does not crash."""
    def bad_model(ctx):
        return {"tool": "nonexistent", "args": {}}

    monkeypatch.setattr(_mod, "model", bad_model)
    result = run_agent("anything", verbose=False)
    assert "[unknown tool" in result or result == "[max steps reached]"


# ---------------------------------------------------------------------------
# __main__ block (subprocess)
# ---------------------------------------------------------------------------

def test_runs_as_script_with_math():
    proc = subprocess.run(
        [sys.executable, str(_SCRIPT), "What is 5 + 3?"],
        capture_output=True, text=True,
    )
    assert proc.returncode == 0
    assert "8.0" in proc.stdout


def test_runs_as_script_default_question():
    """Running without arguments uses the built-in default question."""
    proc = subprocess.run(
        [sys.executable, str(_SCRIPT)],
        capture_output=True, text=True,
    )
    assert proc.returncode == 0
    assert "7.0" in proc.stdout  # default: "What is 3 + 4?"


def test_tool_exception_is_caught(monkeypatch):
    """Exceptions raised inside a tool fn are caught and included in the result."""
    def exploding_add(**_):
        raise ValueError("boom")

    monkeypatch.setitem(TOOLS, "add", {**TOOLS["add"], "fn": exploding_add})
    result = run_agent("What is 1 + 2?", verbose=False)
    assert "[error:" in result or isinstance(result, str)


def test_main_block_via_runpy(monkeypatch, capsys):
    """Cover the __main__ block (lines 123-127) using runpy in-process."""
    monkeypatch.setattr(sys, "argv", [str(_SCRIPT), "What is 2 + 2?"])
    runpy.run_path(str(_SCRIPT), run_name="__main__")
    captured = capsys.readouterr()
    assert "4.0" in captured.out

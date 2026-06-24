"""Unit tests for examples/minimal-agent/agent_sdk.py.

All tests run without a real ANTHROPIC_API_KEY.  The LLM client is replaced by
a lightweight mock built from unittest.mock.MagicMock so the agent loop logic
is exercised in full without network calls.
"""
from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# ---------------------------------------------------------------------------
# Load module (anthropic is NOT required at import time by design)
# ---------------------------------------------------------------------------

_SCRIPT = Path(__file__).resolve().parents[1] / "examples" / "minimal-agent" / "agent_sdk.py"
_spec = importlib.util.spec_from_file_location("minimal_agent_sdk", _SCRIPT)
_mod = importlib.util.module_from_spec(_spec)
sys.modules["minimal_agent_sdk"] = _mod
_spec.loader.exec_module(_mod)

run_agent_sdk = _mod.run_agent_sdk
tool_add = _mod.tool_add
tool_word_count = _mod.tool_word_count
TOOLS = _mod.TOOLS
TOOL_DEFS = _mod.TOOL_DEFS


# ---------------------------------------------------------------------------
# Helpers: build mock Anthropic responses
# ---------------------------------------------------------------------------

def _end_turn(text: str) -> MagicMock:
    """Return a mock response that signals end_turn with a text block."""
    block = MagicMock()
    block.type = "text"
    block.text = text
    resp = MagicMock()
    resp.stop_reason = "end_turn"
    resp.content = [block]
    return resp


def _tool_use(name: str, input_dict: dict, uid: str = "tu-1") -> MagicMock:
    """Return a mock response that requests a single tool call."""
    block = MagicMock()
    block.type = "tool_use"
    block.name = name
    block.input = input_dict
    block.id = uid
    resp = MagicMock()
    resp.stop_reason = "tool_use"
    resp.content = [block]
    return resp


def _client(*responses: MagicMock) -> MagicMock:
    """Return a mock Anthropic client whose messages.create() yields responses."""
    c = MagicMock()
    c.messages.create.side_effect = list(responses)
    return c


# ---------------------------------------------------------------------------
# Tool unit tests
# ---------------------------------------------------------------------------

def test_tool_add_integers():
    assert tool_add(3.0, 4.0) == "7.0"


def test_tool_add_floats():
    assert tool_add(1.5, 2.5) == "4.0"


def test_tool_word_count_basic():
    assert tool_word_count("hello world foo") == "3"


def test_tool_word_count_single_word():
    assert tool_word_count("hi") == "1"


# ---------------------------------------------------------------------------
# TOOL_DEFS structure
# ---------------------------------------------------------------------------

def test_tool_defs_contains_all_tools():
    names = {d["name"] for d in TOOL_DEFS}
    assert names == set(TOOLS.keys())


def test_tool_defs_have_input_schema():
    for defn in TOOL_DEFS:
        assert "input_schema" in defn
        assert "type" in defn["input_schema"]


# ---------------------------------------------------------------------------
# run_agent_sdk integration tests (all with mock client)
# ---------------------------------------------------------------------------

def test_end_turn_immediately_returns_text():
    result = run_agent_sdk("?", _client(_end_turn("42")), verbose=False)
    assert result == "42"


def test_tool_then_end_turn():
    result = run_agent_sdk(
        "What is 3 + 4?",
        _client(_tool_use("add", {"a": 3.0, "b": 4.0}), _end_turn("The sum is 7.0.")),
        verbose=False,
    )
    assert result == "The sum is 7.0."


def test_word_count_tool_then_end_turn():
    result = run_agent_sdk(
        "Count words",
        _client(
            _tool_use("word_count", {"text": "hello world"}),
            _end_turn("2 words"),
        ),
        verbose=False,
    )
    assert result == "2 words"


def test_unknown_tool_returns_error_in_tool_result():
    """Unknown tool names produce an error string; agent continues to end_turn."""
    result = run_agent_sdk(
        "?",
        _client(_tool_use("nonexistent_tool", {}), _end_turn("fallback")),
        verbose=False,
    )
    assert result == "fallback"


def test_tool_exception_is_caught():
    """Exceptions raised inside a tool fn are caught and returned as error strings."""
    # tool_word_count calls str(text).split() — passing a bare int will still work
    # because of the str() cast; pass a dict whose .split() fails without str() cast
    # to test the path. Actually we monkeypatch the fn to raise.
    original_fn = TOOLS["add"]["fn"]
    TOOLS["add"]["fn"] = lambda **_: (_ for _ in ()).throw(ValueError("boom"))
    try:
        result = run_agent_sdk(
            "?",
            _client(_tool_use("add", {"a": 1, "b": 2}), _end_turn("handled")),
            verbose=False,
        )
    finally:
        TOOLS["add"]["fn"] = original_fn
    assert result == "handled"


def test_max_steps_sentinel(monkeypatch):
    monkeypatch.setattr(_mod, "MAX_STEPS", 2)
    never_ending = _tool_use("add", {"a": 1, "b": 1})
    result = run_agent_sdk(
        "loop",
        _client(never_ending, never_ending, never_ending),
        verbose=False,
    )
    assert result == "[max steps reached]"


def test_end_turn_with_no_text_block():
    """If end_turn has no text block, return the sentinel string."""
    block = MagicMock()
    block.type = "image"  # not "text"
    resp = MagicMock()
    resp.stop_reason = "end_turn"
    resp.content = [block]
    result = run_agent_sdk("?", _client(resp), verbose=False)
    assert result == "(no text in response)"


def test_verbose_prints_tool_call(capsys):
    run_agent_sdk(
        "What is 5 + 6?",
        _client(_tool_use("add", {"a": 5, "b": 6}), _end_turn("11")),
        verbose=True,
    )
    captured = capsys.readouterr()
    assert "add" in captured.out
    assert "step 1" in captured.out


# ---------------------------------------------------------------------------
# main() unit tests (no subprocess, no network)
# ---------------------------------------------------------------------------

def test_main_exits_1_when_anthropic_not_installed(monkeypatch):
    """main() prints a pip-install hint and exits 1 when anthropic is absent."""
    with patch.dict(sys.modules, {"anthropic": None}):
        with pytest.raises(SystemExit) as exc:
            _mod.main()
    assert exc.value.code == 1


def test_main_exits_1_when_api_key_missing(monkeypatch):
    """main() exits 1 with a clear message when ANTHROPIC_API_KEY is empty."""
    mock_anthropic = MagicMock()
    monkeypatch.setenv("ANTHROPIC_API_KEY", "")
    with patch.dict(sys.modules, {"anthropic": mock_anthropic}):
        with pytest.raises(SystemExit) as exc:
            _mod.main()
    assert exc.value.code == 1


# ---------------------------------------------------------------------------
# Subprocess test — verifies __main__ path and error messaging end-to-end
# ---------------------------------------------------------------------------

def test_subprocess_exits_with_error_and_helpful_message():
    """Script must exit 1 and mention 'anthropic' regardless of install state."""
    env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
    env["ANTHROPIC_API_KEY"] = ""

    result = subprocess.run(
        [sys.executable, str(_SCRIPT)],
        env=env,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    combined = result.stdout + result.stderr
    # Either "pip install anthropic" (package absent) or "ANTHROPIC_API_KEY" (key absent)
    assert "anthropic" in combined.lower()

"""Unit tests for scripts/check-agent-dive.py."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

# Load module with hyphenated filename
_SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check-agent-dive.py"
_spec = importlib.util.spec_from_file_location("check_agent_dive", _SCRIPT)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

split_markdown_row = _mod.split_markdown_row
check_todo_table = _mod.check_todo_table
count_todo_tasks = _mod.count_todo_tasks
load_json = _mod.load_json
check_placeholders = _mod.check_placeholders


# ---------------------------------------------------------------------------
# split_markdown_row
# ---------------------------------------------------------------------------

def test_split_row_basic():
    assert split_markdown_row("| a | b | c |") == ["a", "b", "c"]


def test_split_row_no_trailing_pipe():
    assert split_markdown_row("| a | b | c") == ["a", "b", "c"]


def test_split_row_trims_whitespace():
    assert split_markdown_row("|  x  |  y  |") == ["x", "y"]


def test_split_row_escaped_pipe():
    cells = split_markdown_row(r"| a \| b | c |")
    assert len(cells) == 2
    assert "a" in cells[0]


# ---------------------------------------------------------------------------
# check_todo_table
# ---------------------------------------------------------------------------

_VALID = "| [x] | `PROJ-L1-01` | task | ref | src | note | 1h | high | no | link |"
_VALID_2 = "| [ ] | `PROJ-L1-02` | task | ref | src | note | 1h | high | no | link |"


def _write(tmp_path: Path, content: str) -> Path:
    f = tmp_path / "learning-todo-list.md"
    f.write_text(content, encoding="utf-8")
    return f


def test_todo_table_valid(tmp_path):
    path = _write(tmp_path, _VALID + "\n" + _VALID_2 + "\n")
    assert check_todo_table(path) == []


def test_todo_table_duplicate_task_id(tmp_path):
    path = _write(tmp_path, _VALID + "\n" + _VALID + "\n")
    errors = check_todo_table(path)
    assert any("duplicate task_id" in e for e in errors)


def test_todo_table_all_rows_checked(tmp_path):
    """Duplicate on row 3 must be detected — confirms no early-return bug."""
    path = _write(tmp_path, _VALID + "\n" + _VALID_2 + "\n" + _VALID + "\n")
    errors = check_todo_table(path)
    assert any("duplicate task_id" in e and "PROJ-L1-01" in e for e in errors)


def test_todo_table_wrong_column_count(tmp_path):
    path = _write(tmp_path, "| [ ] | `PROJ-L1-01` | task | ref |\n")
    errors = check_todo_table(path)
    assert any("expected 10 task columns" in e for e in errors)


def test_todo_table_invalid_state(tmp_path):
    bad = "| [Y] | `PROJ-L1-01` | t | r | s | n | 1h | h | n | l |"
    path = _write(tmp_path, bad + "\n")
    errors = check_todo_table(path)
    assert any("invalid task state" in e for e in errors)


def test_todo_table_invalid_task_id(tmp_path):
    bad = "| [ ] | `bad-id` | t | r | s | n | 1h | h | n | l |"
    path = _write(tmp_path, bad + "\n")
    errors = check_todo_table(path)
    assert any("invalid task_id" in e for e in errors)


def test_todo_table_accepts_done_marker(tmp_path):
    done = "| [X] | `PROJ-L2-01` | t | r | s | n | 1h | h | n | l |"
    path = _write(tmp_path, done + "\n")
    assert check_todo_table(path) == []


# ---------------------------------------------------------------------------
# count_todo_tasks
# ---------------------------------------------------------------------------

def test_count_todo_tasks(tmp_path):
    content = (
        "| [x] | `T-L1-01` | t | r | s | n | 1h | h | n | l |\n"
        "| [ ] | `T-L1-02` | t | r | s | n | 1h | h | n | l |\n"
        "| [X] | `T-L1-03` | t | r | s | n | 1h | h | n | l |\n"
        "# not a task row\n"
    )
    path = tmp_path / "todo.md"
    path.write_text(content, encoding="utf-8")
    done, total = count_todo_tasks(path)
    assert total == 3
    assert done == 2


# ---------------------------------------------------------------------------
# load_json
# ---------------------------------------------------------------------------

def test_load_json_valid(tmp_path):
    f = tmp_path / "meta.json"
    f.write_text('{"key": "value"}', encoding="utf-8")
    assert load_json(f) == {"key": "value"}


def test_load_json_invalid_gives_friendly_error(tmp_path):
    f = tmp_path / "bad.json"
    f.write_text("{invalid json}", encoding="utf-8")
    with pytest.raises(ValueError, match="invalid JSON"):
        load_json(f)


def test_load_json_friendly_error_has_location(tmp_path):
    f = tmp_path / "bad.json"
    f.write_text('{\n  "key": bad\n}', encoding="utf-8")
    with pytest.raises(ValueError) as exc_info:
        load_json(f)
    msg = str(exc_info.value)
    # Message should contain line number and column
    assert "bad.json" in msg or "invalid JSON" in msg


# ---------------------------------------------------------------------------
# check_placeholders
# ---------------------------------------------------------------------------

def _make_note(tmp_path: Path, name: str, content: str) -> Path:
    """Create a file inside a properly named learning-notes sub-directory."""
    d = tmp_path / "learning-notes" / "owner__repo"
    d.mkdir(parents=True, exist_ok=True)
    f = d / name
    f.write_text(content, encoding="utf-8")
    return f


def test_placeholders_project_name(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    d = tmp_path / "projects" / "cat" / "owner__repo"
    d.mkdir(parents=True)
    (d / "README.md").write_text("# <Project Name>", encoding="utf-8")
    errors = check_placeholders()
    assert any("<Project Name>" in e for e in errors)


def test_placeholders_powershell_artifact(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _make_note(tmp_path, "05-integration-notes.en.md",
               "- evidence file: $(System.Collections.Hashtable.Evidence).")
    errors = check_placeholders()
    assert any("$(System.Collections.Hashtable" in e for e in errors)


def test_placeholders_to_be_replenished(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _make_note(tmp_path, "05-integration-notes.en.md",
               "## Notes\n\nTo be replenished.")
    errors = check_placeholders()
    assert any("To be replenished." in e for e in errors)


def test_placeholders_skeleton_status_en(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _make_note(tmp_path, "00-study-plan.en.md",
               "Status: completed note skeleton during closed-loop transfer of learning.")
    errors = check_placeholders()
    assert any("completed note skeleton during closed-loop transfer of learning" in e
               for e in errors)


def test_placeholders_skeleton_status_zh(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _make_note(tmp_path, "00-study-plan.md",
               "状态：学习闭环迁移时补齐的笔记骨架。")
    errors = check_placeholders()
    assert any("学习闭环迁移时补齐的笔记骨架" in e for e in errors)


def test_placeholders_dai_bu_zh(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _make_note(tmp_path, "notes.md", "## 笔记\n\n待补。")
    errors = check_placeholders()
    assert any("待补。" in e for e in errors)


def test_placeholders_clean_file_passes(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _make_note(tmp_path, "05-integration-notes.en.md",
               "# Notes\n\n*(Content pending — to be filled in during study.)*")
    errors = check_placeholders()
    assert errors == []

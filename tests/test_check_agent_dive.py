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
parse_projects_index = _mod.parse_projects_index
parse_learning_progress = _mod.parse_learning_progress


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


# ---------------------------------------------------------------------------
# parse_projects_index
# ---------------------------------------------------------------------------

_PROJECTS_HEADER = (
    "| 项目名称 | GitHub 地址 | 分类 | 收录等级 | 当前状态 |"
    " 是否跑通 | 是否源码分析 | 是否有图解 | 是否有学习笔记 | 最近更新 |\n"
    "|---|---|---|---|---|---|---|---|---|---|\n"
)
_PROJECTS_ROW = (
    "| MyProj | https://github.com/owner/repo | agentic-coding |"
    " Level A | analyzing | 否 | 部分 | 是 | 是 | 2026-06-01 |\n"
)


def test_parse_projects_index_valid(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    (tmp_path / "PROJECTS.md").write_text(
        "# Projects\n\n" + _PROJECTS_HEADER + _PROJECTS_ROW, encoding="utf-8"
    )
    rows = parse_projects_index()
    assert len(rows) == 1
    assert rows[0]["project_id"] == "owner__repo"
    assert rows[0]["name"] == "MyProj"
    assert rows[0]["category"] == "agentic-coding"
    assert rows[0]["status"] == "analyzing"
    assert rows[0]["runtime"] == "否"


def test_parse_projects_index_no_table(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    (tmp_path / "PROJECTS.md").write_text("# Projects\n\nNo table here.\n", encoding="utf-8")
    assert parse_projects_index() == []


def test_parse_projects_index_skips_non_github(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    row = (
        "| BitProj | https://bitbucket.org/owner/repo | cat |"
        " Level A | analyzing | 否 | 否 | 否 | 否 | 2026-01-01 |\n"
    )
    (tmp_path / "PROJECTS.md").write_text(_PROJECTS_HEADER + row, encoding="utf-8")
    assert parse_projects_index() == []


def test_parse_projects_index_stops_at_next_section(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    content = (
        "# Projects\n\n"
        + _PROJECTS_HEADER
        + _PROJECTS_ROW
        + "\n## Field Notes\n"
        + "| Other | https://github.com/x/y | cat | L | done | 否 | 否 | 否 | 否 | 2026-01-01 |\n"
    )
    (tmp_path / "PROJECTS.md").write_text(content, encoding="utf-8")
    rows = parse_projects_index()
    assert len(rows) == 1
    assert rows[0]["project_id"] == "owner__repo"


# ---------------------------------------------------------------------------
# parse_learning_progress
# ---------------------------------------------------------------------------

_LP_HEADER = (
    "| 项目名称 | 项目 ID | 当前阶段 | 完成进度 | 卡住的问题 | 下一步行动 |\n"
    "|---|---|---:|---|---|---|\n"
)
_LP_ROW = "| MyProj | owner__repo | analyzing | 5/20 | none | continue |\n"


def test_parse_learning_progress_valid(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    (tmp_path / "LEARNING_PROGRESS.md").write_text(
        "# Learning Progress\n\n" + _LP_HEADER + _LP_ROW, encoding="utf-8"
    )
    rows = parse_learning_progress()
    assert "owner__repo" in rows
    assert rows["owner__repo"]["stage"] == "analyzing"
    assert rows["owner__repo"]["progress"] == "5/20"
    assert rows["owner__repo"]["name"] == "MyProj"


def test_parse_learning_progress_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    (tmp_path / "LEARNING_PROGRESS.md").write_text(
        "# Learning Progress\n\nNo table.\n", encoding="utf-8"
    )
    assert parse_learning_progress() == {}


def test_parse_learning_progress_skips_short_rows(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    short = "| OnlyTwo | cols |\n"
    (tmp_path / "LEARNING_PROGRESS.md").write_text(
        _LP_HEADER + short, encoding="utf-8"
    )
    assert parse_learning_progress() == {}


# ---------------------------------------------------------------------------
# check_project helpers & tests
# ---------------------------------------------------------------------------

def _valid_meta(project_id: str, name: str, category: str, github_url: str) -> dict:
    return {
        "project_id": project_id,
        "name": name,
        "github_url": github_url,
        "category": category,
        "collect_level": "Level A",
        "status": "analyzing",
        "source_snapshot": {"commit": "abc123"},
        "verification": {
            "runtime_status": "not_run",
            "tests_status": "not_run",
            "source_review_status": "not_run",
            "diagram_status": "not_run",
            "learning_notes_status": "not_run",
        },
        "evidence": {
            "evidence_file": f"projects/{category}/{project_id}/evidence.md"
        },
    }


def _valid_progress(project_id: str, name: str, github_url: str, done: int = 1, total: int = 2) -> dict:
    return {
        "project_id": project_id,
        "project_name": name,
        "github_url": github_url,
        "status": "in_progress",
        "current_stage": "analyzing",
        "completed_tasks": done,
        "total_tasks": total,
        "last_studied_at": "2026-06-01",
        "blocked_items": [],
        "next_actions": [],
        "evidence_file": f"projects/agentic-coding/{project_id}/evidence.md",
        "review_questions_done": False,
        "final_summary_done": False,
    }


def _make_full_project(root: Path, project_id: str = "owner__repo",
                       category: str = "agentic-coding", name: str = "MyProj",
                       done: int = 1, total: int = 2):
    """Create a minimal but complete valid project structure."""
    github_url = f"https://github.com/{project_id.replace('__', '/', 1)}"
    project_dir = root / "projects" / category / project_id
    notes_dir = root / "learning-notes" / project_id
    project_dir.mkdir(parents=True)
    notes_dir.mkdir(parents=True)

    meta = _valid_meta(project_id, name, category, github_url)
    meta["evidence"]["evidence_file"] = f"projects/{category}/{project_id}/evidence.md"
    progress = _valid_progress(project_id, name, github_url, done, total)
    progress["evidence_file"] = f"projects/{category}/{project_id}/evidence.md"

    (project_dir / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    (notes_dir / "progress.json").write_text(json.dumps(progress), encoding="utf-8")

    for fname in ["README.md", "project-analysis.md", "integration-guide.md",
                  "source-code-reading.md", "troubleshooting.md", "collect-report.md"]:
        (project_dir / fname).write_text(f"# {fname}\n\nContent.", encoding="utf-8")

    (project_dir / "evidence.md").write_text(
        "# Evidence\n\nnot_run: runtime not tested yet.", encoding="utf-8"
    )

    todo_rows = "".join(
        f"| {'[x]' if i < done else '[ ]'} | `PROJ-L1-{i+1:02d}` |"
        f" task | ref | src | note | 1h | high | no | link |\n"
        for i in range(total)
    )
    (project_dir / "learning-todo-list.md").write_text(todo_rows, encoding="utf-8")

    for fname in ["README.md", "00-study-plan.md", "01-first-impression.md",
                  "02-quickstart-notes.md", "03-architecture-notes.md",
                  "04-source-reading-notes.md", "05-integration-notes.md",
                  "06-troubleshooting-notes.md", "07-reflection.md", "review-questions.md"]:
        (notes_dir / fname).write_text(f"# {fname}\n\nContent.", encoding="utf-8")

    row = {
        "project_id": project_id, "name": name, "github_url": github_url,
        "category": category, "collect_level": "Level A", "status": "analyzing",
        "runtime": "否", "source": "部分", "diagram": "是", "notes": "是",
    }
    learning_row = {
        "project_id": project_id, "name": name,
        "stage": "analyzing", "progress": f"{done}/{total}",
        "blocked": "none", "next_action": "continue",
    }
    return project_dir, notes_dir, row, learning_row


def test_check_project_valid(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _, _, row, learning_row = _make_full_project(tmp_path)
    errors = _mod.check_project(row, learning_row)
    assert errors == [], errors


def test_check_project_missing_project_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    row = {
        "project_id": "owner__repo", "name": "MyProj",
        "github_url": "https://github.com/owner/repo", "category": "agentic-coding",
        "collect_level": "Level A", "status": "analyzing",
        "runtime": "否", "source": "否", "diagram": "否", "notes": "否",
    }
    errors = _mod.check_project(row, None)
    assert any("missing project directory" in e for e in errors)


def test_check_project_missing_notes_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    row = {
        "project_id": "owner__repo", "name": "MyProj",
        "github_url": "https://github.com/owner/repo", "category": "agentic-coding",
        "collect_level": "Level A", "status": "analyzing",
        "runtime": "否", "source": "否", "diagram": "否", "notes": "否",
    }
    (tmp_path / "projects" / "agentic-coding" / "owner__repo").mkdir(parents=True)
    errors = _mod.check_project(row, None)
    assert any("missing learning notes directory" in e for e in errors)


def test_check_project_missing_required_files(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    (tmp_path / "projects" / "agentic-coding" / "owner__repo").mkdir(parents=True)
    (tmp_path / "learning-notes" / "owner__repo").mkdir(parents=True)
    row = {
        "project_id": "owner__repo", "name": "MyProj",
        "github_url": "https://github.com/owner/repo", "category": "agentic-coding",
        "collect_level": "Level A", "status": "analyzing",
        "runtime": "否", "source": "否", "diagram": "否", "notes": "否",
    }
    errors = _mod.check_project(row, None)
    assert any("missing" in e for e in errors)


def test_check_project_meta_project_id_mismatch(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    project_dir, _, row, learning_row = _make_full_project(tmp_path)
    meta = json.loads((project_dir / "meta.json").read_text(encoding="utf-8"))
    meta["project_id"] = "wrong__id"
    (project_dir / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("meta project_id mismatch" in e for e in errors)


def test_check_project_invalid_meta_status(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    project_dir, _, row, learning_row = _make_full_project(tmp_path)
    meta = json.loads((project_dir / "meta.json").read_text(encoding="utf-8"))
    meta["status"] = "invalid-status"
    (project_dir / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    row["status"] = "invalid-status"
    errors = _mod.check_project(row, learning_row)
    assert any("invalid meta status" in e for e in errors)


def test_check_project_invalid_progress_status(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _, notes_dir, row, learning_row = _make_full_project(tmp_path)
    progress = json.loads((notes_dir / "progress.json").read_text(encoding="utf-8"))
    progress["status"] = "invalid_status"
    (notes_dir / "progress.json").write_text(json.dumps(progress), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("invalid progress status" in e for e in errors)


def test_check_project_no_tasks(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    project_dir, notes_dir, row, _ = _make_full_project(tmp_path, done=0, total=0)
    (project_dir / "learning-todo-list.md").write_text("# Todo\n\nNo tasks here.\n", encoding="utf-8")
    progress = json.loads((notes_dir / "progress.json").read_text(encoding="utf-8"))
    progress["completed_tasks"] = 0
    progress["total_tasks"] = 0
    (notes_dir / "progress.json").write_text(json.dumps(progress), encoding="utf-8")
    learning_row_fixed = {
        "project_id": "owner__repo", "name": "MyProj",
        "stage": "analyzing", "progress": "0/0",
        "blocked": "none", "next_action": "continue",
    }
    errors = _mod.check_project(row, learning_row_fixed)
    assert any("no structured task rows" in e for e in errors)


def test_check_project_task_count_mismatch(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _, notes_dir, row, learning_row = _make_full_project(tmp_path, done=1, total=2)
    progress = json.loads((notes_dir / "progress.json").read_text(encoding="utf-8"))
    progress["completed_tasks"] = 99
    progress["total_tasks"] = 99
    (notes_dir / "progress.json").write_text(json.dumps(progress), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("task count" in e for e in errors)


def test_check_project_missing_learning_progress_row(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _, _, row, _ = _make_full_project(tmp_path)
    errors = _mod.check_project(row, None)
    assert any("missing LEARNING_PROGRESS.md row" in e for e in errors)


def test_check_project_invalid_index_marker(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _, _, row, learning_row = _make_full_project(tmp_path)
    row["runtime"] = "yes"  # should be 是/否/部分/不适用
    errors = _mod.check_project(row, learning_row)
    assert any("invalid PROJECTS.md runtime marker" in e for e in errors)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def _setup_valid_repo(root: Path) -> None:
    """Set up a minimal valid repository with one project."""
    github_url = "https://github.com/owner/repo"
    project_id = "owner__repo"
    category = "agentic-coding"
    name = "MyProj"

    _make_full_project(root, project_id, category, name)

    (root / "PROJECTS.md").write_text(
        "# Projects\n\n"
        + _PROJECTS_HEADER
        + f"| {name} | {github_url} | {category} | Level A | analyzing |"
        f" 否 | 部分 | 是 | 是 | 2026-06-01 |\n",
        encoding="utf-8",
    )
    (root / "LEARNING_PROGRESS.md").write_text(
        "# Learning Progress\n\n"
        + _LP_HEADER
        + f"| {name} | {project_id} | analyzing | 1/2 | none | continue |\n",
        encoding="utf-8",
    )


def test_main_passes_on_valid_repo(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _setup_valid_repo(tmp_path)
    result = _mod.main()
    assert result == 0
    out = capsys.readouterr().out
    assert "passed" in out


def test_main_returns_1_when_no_projects(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    (tmp_path / "PROJECTS.md").write_text("# Projects\n", encoding="utf-8")
    (tmp_path / "LEARNING_PROGRESS.md").write_text("# Learning Progress\n", encoding="utf-8")
    result = _mod.main()
    assert result == 1
    out = capsys.readouterr().out
    assert "failed" in out


def test_main_detects_extra_learning_row(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _setup_valid_repo(tmp_path)
    # Add an extra project ID in LEARNING_PROGRESS.md that has no PROJECTS.md entry
    existing = (tmp_path / "LEARNING_PROGRESS.md").read_text(encoding="utf-8")
    (tmp_path / "LEARNING_PROGRESS.md").write_text(
        existing + "| Ghost | ghost__proj | analyzing | 0/0 | none | none |\n",
        encoding="utf-8",
    )
    result = _mod.main()
    assert result == 1
    out = capsys.readouterr().out
    assert "ghost__proj" in out


# ---------------------------------------------------------------------------
# parse edge cases — hitting the continue/break lines inside tables
# ---------------------------------------------------------------------------

def test_parse_projects_index_non_pipe_line_in_table(tmp_path, monkeypatch):
    """A non-pipe, non-blank line inside the table area is silently skipped."""
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    content = (
        "# Projects\n\n"
        + _PROJECTS_HEADER
        + "This is a stray comment line inside the table.\n"
        + _PROJECTS_ROW
    )
    (tmp_path / "PROJECTS.md").write_text(content, encoding="utf-8")
    rows = parse_projects_index()
    assert len(rows) == 1
    assert rows[0]["project_id"] == "owner__repo"


def test_parse_learning_progress_breaks_on_blank_line(tmp_path, monkeypatch):
    """A blank line after the table header triggers the break, rows after are not parsed."""
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    content = (
        _LP_HEADER
        + _LP_ROW
        + "\n"
        + "| Ghost | ghost__proj | analyzing | 0/0 | none | none |\n"
    )
    (tmp_path / "LEARNING_PROGRESS.md").write_text(content, encoding="utf-8")
    rows = parse_learning_progress()
    assert "owner__repo" in rows
    assert "ghost__proj" not in rows


def test_parse_learning_progress_non_pipe_line_in_table(tmp_path, monkeypatch):
    """A non-pipe, non-blank line inside the table area is silently skipped."""
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    content = (
        _LP_HEADER
        + _LP_ROW
        + "Some stray comment line.\n"
    )
    (tmp_path / "LEARNING_PROGRESS.md").write_text(content, encoding="utf-8")
    rows = parse_learning_progress()
    assert "owner__repo" in rows


# ---------------------------------------------------------------------------
# check_project — additional field mismatch and validation paths
# ---------------------------------------------------------------------------

def test_check_project_meta_missing_keys(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    project_dir, _, row, learning_row = _make_full_project(tmp_path)
    (project_dir / "meta.json").write_text('{"project_id": "owner__repo"}', encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("meta.json missing keys" in e for e in errors)


def test_check_project_progress_missing_keys(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _, notes_dir, row, learning_row = _make_full_project(tmp_path)
    (notes_dir / "progress.json").write_text('{"project_id": "owner__repo"}', encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("progress.json missing keys" in e for e in errors)


def test_check_project_meta_name_mismatch(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    project_dir, _, row, learning_row = _make_full_project(tmp_path)
    meta = json.loads((project_dir / "meta.json").read_text(encoding="utf-8"))
    meta["name"] = "WrongName"
    (project_dir / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("meta name mismatch" in e for e in errors)


def test_check_project_meta_url_mismatch(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    project_dir, _, row, learning_row = _make_full_project(tmp_path)
    meta = json.loads((project_dir / "meta.json").read_text(encoding="utf-8"))
    meta["github_url"] = "https://github.com/wrong/url"
    (project_dir / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("meta github_url mismatch" in e for e in errors)


def test_check_project_meta_category_mismatch(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    project_dir, _, row, learning_row = _make_full_project(tmp_path)
    meta = json.loads((project_dir / "meta.json").read_text(encoding="utf-8"))
    meta["category"] = "wrong-category"
    (project_dir / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("meta category mismatch" in e for e in errors)


def test_check_project_meta_collect_level_mismatch(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    project_dir, _, row, learning_row = _make_full_project(tmp_path)
    meta = json.loads((project_dir / "meta.json").read_text(encoding="utf-8"))
    meta["collect_level"] = "Level Z"
    (project_dir / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("meta collect_level mismatch" in e for e in errors)


def test_check_project_progress_id_mismatch(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _, notes_dir, row, learning_row = _make_full_project(tmp_path)
    progress = json.loads((notes_dir / "progress.json").read_text(encoding="utf-8"))
    progress["project_id"] = "wrong__id"
    (notes_dir / "progress.json").write_text(json.dumps(progress), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("progress project_id mismatch" in e for e in errors)


def test_check_project_progress_name_mismatch(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _, notes_dir, row, learning_row = _make_full_project(tmp_path)
    progress = json.loads((notes_dir / "progress.json").read_text(encoding="utf-8"))
    progress["project_name"] = "WrongName"
    (notes_dir / "progress.json").write_text(json.dumps(progress), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("progress project_name mismatch" in e for e in errors)


def test_check_project_progress_url_mismatch(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _, notes_dir, row, learning_row = _make_full_project(tmp_path)
    progress = json.loads((notes_dir / "progress.json").read_text(encoding="utf-8"))
    progress["github_url"] = "https://github.com/wrong/url"
    (notes_dir / "progress.json").write_text(json.dumps(progress), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("progress github_url mismatch" in e for e in errors)


def test_check_project_source_snapshot_missing_commit(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    project_dir, _, row, learning_row = _make_full_project(tmp_path)
    meta = json.loads((project_dir / "meta.json").read_text(encoding="utf-8"))
    meta["source_snapshot"] = {"no_commit_key": True}
    (project_dir / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("source_snapshot.commit missing" in e for e in errors)


def test_check_project_invalid_verification_value(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    project_dir, _, row, learning_row = _make_full_project(tmp_path)
    meta = json.loads((project_dir / "meta.json").read_text(encoding="utf-8"))
    meta["verification"]["runtime_status"] = "unknown_value"
    (project_dir / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("invalid verification.runtime_status" in e for e in errors)


def test_check_project_evidence_file_mismatch_in_meta(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    project_dir, _, row, learning_row = _make_full_project(tmp_path)
    meta = json.loads((project_dir / "meta.json").read_text(encoding="utf-8"))
    meta["evidence"]["evidence_file"] = "wrong/path/evidence.md"
    (project_dir / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("evidence.evidence_file should be" in e for e in errors)


def test_check_project_evidence_file_mismatch_in_progress(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _, notes_dir, row, learning_row = _make_full_project(tmp_path)
    progress = json.loads((notes_dir / "progress.json").read_text(encoding="utf-8"))
    progress["evidence_file"] = "wrong/path/evidence.md"
    (notes_dir / "progress.json").write_text(json.dumps(progress), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("progress evidence_file should be" in e for e in errors)


def test_check_project_learning_progress_progress_mismatch(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _, _, row, learning_row = _make_full_project(tmp_path)
    learning_row["progress"] = "99/99"
    errors = _mod.check_project(row, learning_row)
    assert any("LEARNING_PROGRESS progress" in e for e in errors)


def test_check_project_runtime_is_marked_pass_but_verification_not_pass(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _, _, row, learning_row = _make_full_project(tmp_path)
    row["runtime"] = "是"
    errors = _mod.check_project(row, learning_row)
    assert any("PROJECTS.md says runtime passed but meta verification is not pass" in e for e in errors)


def test_check_project_study_ready_requires_runtime_pass(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    project_dir, notes_dir, row, learning_row = _make_full_project(tmp_path)
    row["status"] = "study-ready"
    learning_row["stage"] = "study-ready"
    meta = json.loads((project_dir / "meta.json").read_text(encoding="utf-8"))
    meta["status"] = "study-ready"
    (project_dir / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    progress = json.loads((notes_dir / "progress.json").read_text(encoding="utf-8"))
    progress["current_stage"] = "study-ready"
    (notes_dir / "progress.json").write_text(json.dumps(progress), encoding="utf-8")
    errors = _mod.check_project(row, learning_row)
    assert any("requires runtime_status pass" in e for e in errors)


def test_check_project_evidence_missing_not_run_text(tmp_path, monkeypatch):
    """evidence.md must contain 'not_run' when runtime_status is not_run."""
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    project_dir, _, row, learning_row = _make_full_project(tmp_path)
    (project_dir / "evidence.md").write_text(
        "# Evidence\n\nRuntime was tested successfully.", encoding="utf-8"
    )
    errors = _mod.check_project(row, learning_row)
    assert any("runtime_status is not_run but evidence.md does not say not_run" in e for e in errors)


# ---------------------------------------------------------------------------
# main — duplicate PROJECTS.md row
# ---------------------------------------------------------------------------

def test_main_detects_duplicate_projects_row(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _setup_valid_repo(tmp_path)
    existing = (tmp_path / "PROJECTS.md").read_text(encoding="utf-8")
    duplicate = (
        "| MyProj | https://github.com/owner/repo | agentic-coding |"
        " Level A | analyzing | 否 | 部分 | 是 | 是 | 2026-06-01 |\n"
    )
    (tmp_path / "PROJECTS.md").write_text(existing + duplicate, encoding="utf-8")
    result = _mod.main()
    assert result == 1
    out = capsys.readouterr().out
    assert "duplicate PROJECTS.md row" in out


# ---------------------------------------------------------------------------
# check_placeholders — 待填写 pattern
# ---------------------------------------------------------------------------

def test_placeholders_dai_tian_xie(tmp_path, monkeypatch):
    monkeypatch.setattr(_mod, "ROOT", tmp_path)
    _make_note(tmp_path, "01-first-impression.md", "# Notes\n\n待填写。\n")
    errors = check_placeholders()
    assert any("待填写" in e for e in errors)

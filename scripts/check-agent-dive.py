#!/usr/bin/env python3
"""Validate AgentDive project metadata, learning progress, and evidence files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PROJECT_REQUIRED_FILES = [
    "README.md",
    "project-analysis.md",
    "learning-todo-list.md",
    "integration-guide.md",
    "source-code-reading.md",
    "troubleshooting.md",
    "collect-report.md",
    "meta.json",
    "evidence.md",
]

NOTE_REQUIRED_FILES = [
    "README.md",
    "00-study-plan.md",
    "01-first-impression.md",
    "02-quickstart-notes.md",
    "03-architecture-notes.md",
    "04-source-reading-notes.md",
    "05-integration-notes.md",
    "06-troubleshooting-notes.md",
    "07-reflection.md",
    "progress.json",
    "review-questions.md",
]

META_REQUIRED_KEYS = {
    "project_id",
    "name",
    "github_url",
    "category",
    "collect_level",
    "status",
    "source_snapshot",
    "verification",
    "evidence",
}

PROGRESS_REQUIRED_KEYS = {
    "project_id",
    "project_name",
    "github_url",
    "status",
    "current_stage",
    "completed_tasks",
    "total_tasks",
    "last_studied_at",
    "blocked_items",
    "next_actions",
    "evidence_file",
    "review_questions_done",
    "final_summary_done",
}

VALID_PROJECT_STATUSES = {
    "candidate",
    "triaging",
    "accepted",
    "analyzing",
    "documented",
    "diagrammed",
    "study-ready",
    "in-study",
    "completed",
    "archived",
}

VALID_PROGRESS_STATUSES = {
    "not_started",
    "in_progress",
    "blocked",
    "completed",
    "archived",
}

VALID_INDEX_MARKERS = {"是", "否", "部分", "不适用"}

VERIFICATION_ALLOWED_BY_FIELD = {
    "runtime_status": {"not_run", "pending", "pass", "fail", "partial", "blocked"},
    "tests_status": {"not_run", "pending", "pass", "fail", "partial", "blocked"},
    "source_review_status": {"not_run", "pending", "pass", "fail", "partial", "blocked"},
    "diagram_status": {"not_run", "pending", "pass", "fail", "partial", "blocked", "draft"},
    "learning_notes_status": {"not_run", "pending", "pass", "fail", "partial", "blocked", "created"},
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def parse_projects_index() -> list[dict]:
    rows: list[dict] = []
    in_table = False
    for raw_line in (ROOT / "PROJECTS.md").read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("| 项目名称 | GitHub 地址 |"):
            in_table = True
            continue
        if in_table and (not line or line.startswith("## ")):
            break
        if not in_table or line.startswith("|---"):
            continue
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 9 or not cells[1].startswith("https://github.com/"):
            continue
        owner, repo = cells[1].removeprefix("https://github.com/").split("/", 1)
        rows.append(
            {
                "name": cells[0],
                "github_url": cells[1],
                "category": cells[2],
                "collect_level": cells[3],
                "status": cells[4],
                "runtime": cells[5],
                "source": cells[6],
                "diagram": cells[7],
                "notes": cells[8],
                "updated_at": cells[9] if len(cells) > 9 else "",
                "project_id": f"{owner}__{repo}",
            }
        )
    return rows


def parse_learning_progress() -> dict[str, dict]:
    rows: dict[str, dict] = {}
    in_table = False
    for raw_line in (ROOT / "LEARNING_PROGRESS.md").read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("| 项目名称 | 项目 ID | 当前阶段 |"):
            in_table = True
            continue
        if in_table and (not line or line.startswith("## ")):
            break
        if not in_table or line.startswith("|---"):
            continue
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 6:
            continue
        rows[cells[1]] = {
            "name": cells[0],
            "project_id": cells[1],
            "stage": cells[2],
            "progress": cells[3],
            "blocked": cells[4],
            "next_action": cells[5],
        }
    return rows


def count_todo_tasks(path: Path) -> tuple[int, int]:
    done = 0
    total = 0
    task_row = re.compile(r"^\|\s*\[(?P<mark>[ xX])\]\s*\|")
    for line in path.read_text(encoding="utf-8").splitlines():
        match = task_row.match(line)
        if not match:
            continue
        total += 1
        if match.group("mark").lower() == "x":
            done += 1
    return done, total


def split_markdown_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]

    cells: list[str] = []
    current: list[str] = []
    backslash_count = 0
    for char in stripped:
        if char == "|" and backslash_count % 2 == 0:
            cells.append("".join(current).strip())
            current = []
            backslash_count = 0
            continue
        current.append(char)
        if char == "\\":
            backslash_count += 1
        else:
            backslash_count = 0
    cells.append("".join(current).strip())
    return cells


def check_todo_table(path: Path) -> list[str]:
    errors: list[str] = []
    seen_task_ids: set[str] = set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("| ["):
            continue
        cells = split_markdown_row(line)
        if len(cells) != 10:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: expected 10 task columns, got {len(cells)}"
            )
            continue
        if cells[0] not in {"[ ]", "[x]", "[X]"}:
            errors.append(f"{path.relative_to(ROOT)}:{line_number}: invalid task state {cells[0]!r}")
        task_id = cells[1].strip("`")
        if not re.match(r"^[A-Z0-9]+-L[1-6]-\d{2}$", task_id):
            errors.append(f"{path.relative_to(ROOT)}:{line_number}: invalid task_id {task_id!r}")
        if task_id in seen_task_ids:
            errors.append(f"{path.relative_to(ROOT)}:{line_number}: duplicate task_id {task_id!r}")
        seen_task_ids.add(task_id)
    return errors


def check_project(row: dict, learning_row: dict | None) -> list[str]:
    errors: list[str] = []
    project_id = row["project_id"]
    project_dir = ROOT / "projects" / row["category"] / project_id
    notes_dir = ROOT / "learning-notes" / project_id

    if not project_dir.is_dir():
        return [f"{project_id}: missing project directory {project_dir.relative_to(ROOT)}"]
    if not notes_dir.is_dir():
        return [f"{project_id}: missing learning notes directory {notes_dir.relative_to(ROOT)}"]

    for filename in PROJECT_REQUIRED_FILES:
        if not (project_dir / filename).is_file():
            errors.append(f"{project_id}: missing {project_dir.relative_to(ROOT)}/{filename}")
    for filename in NOTE_REQUIRED_FILES:
        if not (notes_dir / filename).is_file():
            errors.append(f"{project_id}: missing {notes_dir.relative_to(ROOT)}/{filename}")
    if errors:
        return errors

    meta = load_json(project_dir / "meta.json")
    progress = load_json(notes_dir / "progress.json")
    evidence_path = project_dir / "evidence.md"
    todo_path = project_dir / "learning-todo-list.md"

    missing_meta = META_REQUIRED_KEYS - set(meta)
    if missing_meta:
        errors.append(f"{project_id}: meta.json missing keys {sorted(missing_meta)}")
    missing_progress = PROGRESS_REQUIRED_KEYS - set(progress)
    if missing_progress:
        errors.append(f"{project_id}: progress.json missing keys {sorted(missing_progress)}")

    if meta.get("project_id") != project_id:
        errors.append(f"{project_id}: meta project_id mismatch")
    if meta.get("name") != row["name"]:
        errors.append(f"{project_id}: meta name mismatch")
    if meta.get("github_url") != row["github_url"]:
        errors.append(f"{project_id}: meta github_url mismatch")
    if meta.get("category") != row["category"]:
        errors.append(f"{project_id}: meta category mismatch")
    if meta.get("collect_level") != row["collect_level"]:
        errors.append(f"{project_id}: meta collect_level mismatch")
    if meta.get("status") != row["status"]:
        errors.append(f"{project_id}: meta status does not match PROJECTS.md")
    if meta.get("status") not in VALID_PROJECT_STATUSES:
        errors.append(f"{project_id}: invalid meta status {meta.get('status')!r}")
    if progress.get("project_id") != project_id:
        errors.append(f"{project_id}: progress project_id mismatch")
    if progress.get("project_name") != row["name"]:
        errors.append(f"{project_id}: progress project_name mismatch")
    if progress.get("github_url") != row["github_url"]:
        errors.append(f"{project_id}: progress github_url mismatch")
    if progress.get("current_stage") != row["status"]:
        errors.append(f"{project_id}: progress current_stage does not match PROJECTS.md")
    if progress.get("status") not in VALID_PROGRESS_STATUSES:
        errors.append(f"{project_id}: invalid progress status {progress.get('status')!r}")
    for field in ("runtime", "source", "diagram", "notes"):
        if row[field] not in VALID_INDEX_MARKERS:
            errors.append(f"{project_id}: invalid PROJECTS.md {field} marker {row[field]!r}")
    if learning_row is None:
        errors.append(f"{project_id}: missing LEARNING_PROGRESS.md row")
    else:
        if learning_row.get("stage") != row["status"]:
            errors.append(f"{project_id}: LEARNING_PROGRESS stage does not match PROJECTS.md")

    source_snapshot = meta.get("source_snapshot", {})
    verification = meta.get("verification", {})
    evidence = meta.get("evidence", {})
    if not isinstance(source_snapshot, dict) or "commit" not in source_snapshot:
        errors.append(f"{project_id}: source_snapshot.commit missing")
    for key, allowed_values in VERIFICATION_ALLOWED_BY_FIELD.items():
        value = verification.get(key)
        if value not in allowed_values:
            errors.append(f"{project_id}: invalid verification.{key} {value!r}")
    expected_evidence = str(evidence_path.relative_to(ROOT)).replace("\\", "/")
    if evidence.get("evidence_file") != expected_evidence:
        errors.append(f"{project_id}: evidence.evidence_file should be {expected_evidence}")
    if progress.get("evidence_file") != expected_evidence:
        errors.append(f"{project_id}: progress evidence_file should be {expected_evidence}")

    done, total = count_todo_tasks(todo_path)
    errors.extend(check_todo_table(todo_path))
    if total == 0:
        errors.append(f"{project_id}: learning-todo-list.md has no structured task rows")
    if progress.get("completed_tasks") != done or progress.get("total_tasks") != total:
        errors.append(
            f"{project_id}: progress task count {progress.get('completed_tasks')}/{progress.get('total_tasks')} "
            f"does not match TODO {done}/{total}"
        )
    if learning_row is not None:
        expected_progress = f"{done}/{total}"
        if learning_row.get("progress") != expected_progress:
            errors.append(
                f"{project_id}: LEARNING_PROGRESS progress {learning_row.get('progress')!r} "
                f"does not match TODO {expected_progress}"
            )

    if row["runtime"] == "是" and verification.get("runtime_status") != "pass":
        errors.append(f"{project_id}: PROJECTS.md says runtime passed but meta verification is not pass")
    if row["status"] in {"study-ready", "in-study", "completed"}:
        if verification.get("runtime_status") != "pass":
            errors.append(f"{project_id}: {row['status']} requires runtime_status pass")
        if verification.get("source_review_status") not in {"pass", "partial"}:
            errors.append(f"{project_id}: {row['status']} requires source review evidence")
    if "not_run" not in evidence_path.read_text(encoding="utf-8") and verification.get("runtime_status") == "not_run":
        errors.append(f"{project_id}: runtime_status is not_run but evidence.md does not say not_run")

    return errors


def check_placeholders() -> list[str]:
    errors: list[str] = []
    patterns = [
        "<Project Name>",
        "<owner__repo>",
        "TODO: fill",
        "initial skeleton created during learning-loop migration",
        "Status: initial skeleton",
        "Evidence file:",
        "Next step: follow the first open task",
        "Pending.",
    ]
    project_docs = [
        path
        for path in (ROOT / "projects").rglob("*.md")
        if path.parent.name.count("__") == 1
    ]
    note_docs = [
        path
        for path in (ROOT / "learning-notes").rglob("*.md")
        if path.parent.name.count("__") == 1
    ]
    for path in project_docs + note_docs:
        text = path.read_text(encoding="utf-8")
        for pattern in patterns:
            if pattern in text:
                errors.append(f"{path.relative_to(ROOT)} contains placeholder {pattern!r}")
    return errors


def main() -> int:
    errors: list[str] = []
    rows = parse_projects_index()
    learning_rows = parse_learning_progress()
    if not rows:
        errors.append("PROJECTS.md has no project rows")
    seen = set()
    for row in rows:
        project_id = row["project_id"]
        if project_id in seen:
            errors.append(f"{project_id}: duplicate PROJECTS.md row")
            continue
        seen.add(project_id)
        errors.extend(check_project(row, learning_rows.get(project_id)))
    extra_learning_rows = set(learning_rows) - seen
    for project_id in sorted(extra_learning_rows):
        errors.append(f"{project_id}: LEARNING_PROGRESS.md row has no PROJECTS.md entry")
    errors.extend(check_placeholders())

    if errors:
        print("AgentDive check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"AgentDive check passed: {len(rows)} projects validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

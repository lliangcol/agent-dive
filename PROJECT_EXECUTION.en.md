# Project execution instructions

This document describes how the AgentDive version 1 repository skeleton is implemented and maintained.

## Current stage

The current repository is in the construction stage of the first batch of samples and quality management. The core delivery is documents, templates, directory structure, learning routes, collection process instructions, first-round project deep dive samples, evidence files and lightweight consistency checks. Does not include complex web systems, backend services, or real GitHub API automated collect programs.

## Execution Principles

- Retain original requirements and deliverables under `docs/`.
- Do not write the local absolute path, account number, key or private information when adding a public document.
- Does not generate false project collection results.
- Don't mark projects lacking evidence as completed, `study-ready` or `completed`.
- Use `owner__repo` as the quarantine ID for each project.
- The analysis materials, learning notes and diagrams of a single project must be placed in the respective project directory.
- Each project must have `meta.json`, `evidence.md` and `learning-notes/<owner__repo>/progress.json`.

## Recommended maintenance process

1. Determine whether the project is suitable for collect based on `scripts/collect-project.md`.
2. Determine the classification, collection level and directory ID for the project.
3. Generate project analysis data under `projects/<category>/<owner__repo>/`.
4. Generate learning notes under `learning-notes/<owner__repo>/`.
5. Update `PROJECTS.md` and `LEARNING_PROGRESS.md`.
6. Update projects `meta.json`, `evidence.md` and study `progress.json`.
7. Run `python scripts/check-agent-dive.py`.
8. Use the quality check items in the template to do self-checks.

## Relationship with requirements document

`docs/` is the demand source and original data area and is not used as a daily editing area. If there is a conflict between requirements and repository implementation in the future, priority should be given to updating the public specifications of the repository root directory, and the reasons should be recorded in the change description.

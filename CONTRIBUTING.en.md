# Contributing

Welcome to contribute project deep dives, templates, diagrams, learning routes and bug fixes to AgentDive.

## Before you begin

- Read [README.md](README.en.md), [USAGE.md](USAGE.en.md) and [START_HERE.md](START_HERE.en.md) to confirm repository location and current status.
- Get to know [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.en.md), [SECURITY.md](SECURITY.en.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.en.md).
- Create a topic branch from `main` and do not submit work directly on the master branch.

## Basic principles

- Use Simplified Chinese.
- Markdown style remains clear and restrained, suitable for reading on GitHub.
- Do not submit accounts, keys, local absolute paths or private configurations.
- Do not falsify running results, source code conclusions, project status or collection results.
- The conclusion should be traceable to the project README, official documentation, source code, operating results or clear human judgment.
- The main branch name should be `main`.

## Local check

This repository currently does not require the installation of third-party dependencies. Run after modifying project materials, learning notes, templates or indexes:

```bash
python scripts/check-agent-dive.py
```

If you have changed the Python script, it is also recommended to run:

```bash
python -m compileall scripts
```

## project collection specifications

When adding a new project, use the stable project ID: `owner__repo`.

Recommended path:

```text
projects/<category>/<owner__repo>/
learning-notes/<owner__repo>/
```

A single collect is only allowed to modify the current project directory, the corresponding learning notes directory, `PROJECTS.md` and `LEARNING_PROGRESS.md`. Do not change other project directories, and do not modify the `docs/` original data.

## Contribution type

- project collection: Added project deep dive, diagrams, Learning Todo List and collection reports.
- Template improvements: Optimize the general template under `templates/`.
- Knowledge completion: Supplement the AI Agent engineering topic under `knowledge/`.
- Learning route: Improve `learning-roadmap/`’s stage tasks and check questions.
- diagrams bugfix: Fix errors in Mermaid source files or exported diagrams.
- Comparative analysis: Improve cross-project comparison under `comparisons/`.

## Issue specification

- For content or process issues please use the "Content or Process Issues" template.
- Please use the "Suggested project collection" template to recommend new projects, and explain the learning value and preliminary evidence.
- For documentation clarification please use the "Documentation Improvement" template.
- Security issues are handled as [SECURITY.md](SECURITY.en.md), and do not paste sensitive information in public issues.

## Check before submission

- [ ] No modifications to `docs/` original information.
- [ ] No account, key, local absolute path or private information is written.
- [ ] Add new items using `owner__repo` as the directory ID.
- [ ] `PROJECTS.md` is consistent with the project directory status.
- [ ] `LEARNING_PROGRESS.md` Only records an overview and does not carry complete project analysis.
- [ ] The conclusions of diagrams are consistent with the text, and the speculated content has been marked.
- [ ] There are no false claims of operational validation or automation capabilities in the documentation.
- [ ] Running `python scripts/check-agent-dive.py`.

## Branches and Pull Requests

- Create a topic branch from `main`.
- The PR title describes the type of change and scope of impact.
- The PR description lists new files, modified files, verification methods and unfinished items.
- If it is declared to run, test or source code verification, the PR must point to the evidence in the corresponding `evidence.md`.
- If the project status is upgraded to `study-ready`, `in-study` or `completed`, the project directory, learning notes, `PROJECTS.md` and `LEARNING_PROGRESS.md` must be updated simultaneously.

By submitting a PR, you agree that your contribution is authorized by this repository [LICENSE](LICENSE) and confirm that no unauthorized third-party content has been introduced.

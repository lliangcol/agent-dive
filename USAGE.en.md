# AgentDive User Guide

This document is the unified entrance to AgentDive. Start here when using it for the first time, continuing to learn, collecting new projects, maintaining materials, or letting the AI Agent take over tasks.

## Confirm the current boundary first

AgentDive is currently an AI Agent open source project deep dive and learning material repository, not Awesome List, nor a collection platform that has been automated.

The current repository has collected the first batch of projects and generated project analysis, diagrams, Learning Todo List and learning notes skeleton; however, most projects are still in `analyzing` status. Unless the `evidence.md` in the project directory clearly records actual operation, testing or source code verification evidence, do not understand "existing documentation" as "already run" or `study-ready`.

There is currently no truly automated collect program. `scripts/collect-project.md` and `scripts/collect-project-usage.md` are process specifications for manual or AI Agent-assisted collection.

## What kind of user are you?

### Learner

Goal: Learn AI Agent engineering capabilities based on projects, from being able to use it to being able to break down, integrate, and troubleshoot.

Suggested process:

1. Open [PROJECTS.md](PROJECTS.en.md) and select a project.
2. Prioritize `CodeGraph` as the starting point; it has minimum running evidence, but it still needs to continue to complete the source code and learn the closed loop.
3. Open the project directory: `projects/<category>/<owner__repo>/`.
4. Read projects `README.md` and `project-analysis.md` first.
5. Open `learning-todo-list.md` and start from the first unfinished task.
6. After executing the task, write the running command, source code basis, test results or failure reasons into the project `evidence.md`.
7. Synchronously update the notes under `learning-notes/<owner__repo>/` and `progress.json`.

Don't mark a task as completed just because you've read a README, copied an example, or generated an analysis document.

### Maintainer

Goal: Maintain the quality of repository data, add or update project collection, and keep index, evidence, and progress consistent.

Suggested process:

1. Read [scripts/collect-project.md](scripts/collect-project.en.md) before starting a new project collection.
2. For complete instructions and examples, read [scripts/collect-project-usage.md](scripts/collect-project-usage.en.md).
3. Confirm whether the project is clearly related to AI Agent and whether it has README, source code, documentation, license and learning value.
4. Determine the classification, collection level and directory ID: `owner__repo`.
5. Only write the current project directory, the corresponding learning notes directory, [PROJECTS.md](PROJECTS.en.md) and [LEARNING_PROGRESS.md](LEARNING_PROGRESS.en.md).
6. Run a quality check after every new addition or update.

```bash
python scripts/check-agent-dive.py
```

Before the verification is passed, do not upgrade the project status to `study-ready`, `in-study` or `completed`.

### AI Agent

Goal: Let the AI Agent continuously advance learning or collection according to a fixed protocol without overstepping authority or falsifying results.

Recommended prompt words for learning tasks:

```text
Continue learning <project_id>, starting with the next unfinished and non-blocked task in learning-todo-list.md. Read progress.json and evidence.md before execution; update Learning notes, evidence.md and progress.json after execution. Stop and report on encounters requiring keys, global configuration writes, paid APIs, destructive commands, or 3 consecutive failures for the same block.
```

Recommended prompt words to check whether the project can improve its status:

```text
Check if <project_id> can be promoted from analyzing to study-ready. Meta.json, evidence.md, learning-todo-list.md and progress.json must be read. Only real running or source code verification evidence is accepted, speculation is not accepted.
```

See [LEARN_WITH_AGENT.md](LEARN_WITH_AGENT.en.md) for the complete agreement.

## collect a new project

Input format:

```text
Collect: https://github.com/<owner>/<repo>
```

Summary of standard procedures:

1. Parse the GitHub URL and confirm `owner`, `repo` and the default branch.
2. Obtain README, License, main language, document entry and source code structure.
3. Determine whether it is clearly related to the AI Agent.
4. Determine classification and collection level.
5. Check whether collect is repeated.
6. Create `projects/<category>/<owner__repo>/`.
7. Generate project analysis, source reading, integration, troubleshooting, learning tasks and collection reports.
8. Create `learning-notes/<owner__repo>/`.
9. Update `PROJECTS.md` and `LEARNING_PROGRESS.md`.
10. Run `python scripts/check-agent-dive.py`.
11. Output the collection conclusion, verified content, unverified content and risks.

Write boundaries:

- Allow writing: `projects/<category>/<owner__repo>/`
- Allow writing: `learning-notes/<owner__repo>/`
- Allow writing: `PROJECTS.md`
- Allow writing: `LEARNING_PROGRESS.md`
- Do not modify: `docs/` original information
- Do not write: account, key, token, local private path or global configuration

## How to read directory

| Path | Purpose |
|---|---|
| [README.md](README.en.md) | Project introduction and simplified entrance |
| [START_HERE.md](START_HERE.en.md) | A quick first step for learners, maintainers, and AI agents |
| [PROJECTS.md](PROJECTS.en.md) | collected project index and status |
| [LEARNING_PROGRESS.md](LEARNING_PROGRESS.en.md) | Global learning progress, blocking items and next steps |
| [LEARN_WITH_AGENT.md](LEARN_WITH_AGENT.en.md) | AI Agent continuous assisted learning protocol |
| [PROJECT_EXECUTION.md](PROJECT_EXECUTION.en.md) | repository execution and maintenance principles |
| [CONTRIBUTING.md](CONTRIBUTING.en.md) | Contribution Specifications |
| [scripts/collect-project.md](scripts/collect-project.en.md) | project collection process specification |
| [scripts/collect-project-usage.md](scripts/collect-project-usage.en.md) | Detailed instructions for using project collection |
| `projects/` | Store project deep dive data by category |
| `learning-notes/` | Store learning process and progress by project |
| `learning-roadmap/` | AI Agent Engineering Learning Route |
| `knowledge/` | General Knowledge Topics |
| `templates/` | Project analysis, source reading, integration, troubleshooting and collection templates |
| `comparisons/` | Cross-project and ecological comparison |
| `examples/` | Sample project planning |
| `assets/` | Public diagrams and materials |
| `docs/` | Original requirement information and deliverables, unchanged by default |

## Status and evidence rules

Project status:

| Status | Meaning |
|---|---|
| `candidate` | Candidate Projects |
| `triaging` | Under evaluation |
| `accepted` | Passed collection evaluation |
| `analyzing` | Analyzing |
| `documented` | Document has been generated |
| `diagrammed` | diagrams have been generated |
| `study-ready` | Study materials are ready |
| `in-study` | Studying |
| `completed` | Study completed |
| `archived` | Archive or stop maintenance |

evidence rules:

- Run verification, test results, source code call chain and failure reasons are written into the project `evidence.md`.
- For tasks that are not_run, write `not_run`.
- For tasks blocked by environment, permissions, accounts, keys or paid services, write `blocked`.
- Only when `evidence.md` has a real pass record, the project can be marked as passed.
- Speculated content must be marked as pending verification or human judgment.

## Common commands

Quality check:

```bash
python scripts/check-agent-dive.py
```

View the collection process:

```text
Read scripts/collect-project.md
Read scripts/collect-project-usage.md
```

Start learning:

```text
Read PROJECTS.md
Choose a project
Open projects/<category>/<owner__repo>/learning-todo-list.md
Start from the first incomplete task
```

## Self-check before completion

Before submitting or claiming that information is available, at least confirm:

- The status of `PROJECTS.md` is consistent with the contents of the project directory.
- `LEARNING_PROGRESS.md` Only records an overview and does not carry complete project analysis.
- Project directories exist for `meta.json`, `evidence.md` and `learning-todo-list.md`.
- The learning notes directory exists `progress.json`.
- The conclusions of diagrams are based on sources and the boundaries of speculation are clear.
- There are no accounts, keys, tokens, local private paths or false running results.
- `python scripts/check-agent-dive.py` Passed.

## Next entry

First time learning: Select items from [PROJECTS.md](PROJECTS.en.md).

Maintenance collection: starting from [scripts/collect-project-usage.md](scripts/collect-project-usage.en.md).

Let the AI Agent take over: Read [LEARN_WITH_AGENT.md](LEARN_WITH_AGENT.en.md) first, then use the recommended prompts in this document.
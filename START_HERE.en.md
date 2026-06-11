# Start Here

This is the quick start page for AgentDive. For the complete usage path, collection process, evidence rules and AI Agent takeover method, see [USAGE.md](USAGE.en.md).

AgentDive has currently collected 8 high-star AI Agent-related projects, but these materials are still in the first round of deep dive and quality management stages. Do not consider a project to be fully run or `study-ready` unless the project evidence file is explicitly marked as run-verified.

## Learner’s first step

1. First look at [PROJECTS.md](PROJECTS.en.md) and select a project.
2. Open the corresponding `projects/<category>/<owner__repo>/README.md` and `project-analysis.md` to understand the project positioning.
3. Open `learning-todo-list.md` and start from the first unfinished task in Level 1.
4. Every time a task is completed, the notes under `learning-notes/<owner__repo>/` and `progress.json` are updated simultaneously.
5. runtime verification, source code verification, and test results must be written to `evidence.md` in the project directory.

It is recommended to start with CodeGraph because it is the current default golden sample candidate, has a clear learning scope, and is suitable for verifying MCP, code indexing, and Agent-assisted code understanding closed loops.

## Maintainer’s first step

1. Read [scripts/collect-project.md](scripts/collect-project.en.md) before starting a new project collection.
2. After adding or modifying project information, run:

```bash
python scripts/check-agent-dive.py
```

3. Do not upgrade the project status to `study-ready`, `in-study` or `completed` before the verification is passed.
4. Don’t continue to pile up the number of items. Priority is given to turning one Level A project into a complete sample supported by evidence.

## AI Agent first command

Recommended prompt words:

```text
Continue learning <project_id>, starting with the next unfinished and non-blocked task in learning-todo-list.md. Read progress.json and evidence.md before execution; update Learning notes, evidence.md and progress.json after execution. Stop and report on encounters requiring keys, global configuration writes, paid APIs, destructive commands, or 3 consecutive failures for the same block.
```

See [LEARN_WITH_AGENT.md](LEARN_WITH_AGENT.en.md) for the complete agreement.

## Status explanation

- `analyzing`: The data has been generated, but the operation, source code or integration evidence is still insufficient.
- `study-ready`: Learning tasks, note skeleton, running evidence and key source code verification are all available.
- `in-study`: The learner or Agent is executing according to TODO.
- `completed`: All Level learning outputs, review questions and final evaluation have been completed.

Current default judgment: CodeGraph already has the minimum running evidence in the cache, but it is still not `study-ready` or `completed`; the remaining projects have not yet been fully run through and cannot be referenced as completed samples.
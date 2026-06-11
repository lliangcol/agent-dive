# Learn With Agent

This document defines the continuous execution protocol for AI Agent-assisted learning in AgentDive. The goal is to enable the Agent to advance learning tasks without interruption, without falsifying results, or crossing permission boundaries.

## Input

The user gives the project ID, for example:

```text
Continue studying colbymchenry__codegraph until the current Level is complete or a blocker is encountered.
```

Agent must read:

- `PROJECTS.md`
- `LEARNING_PROGRESS.md`
- `projects/<category>/<owner__repo>/learning-todo-list.md`
- `projects/<category>/<owner__repo>/evidence.md`
- `learning-notes/<owner__repo>/progress.json`

## Execute loop

1. Confirm the project ID, category, and current status.
2. Find the first unfinished task in `learning-todo-list.md`.
3. Determine whether the task can be executed automatically.
4. Perform minimum safety steps.
5. Write the command, environment, output summary, failure reason, and unverified items to `evidence.md`.
6. Write your understanding, conclusions and questions into corresponding learning notes.
7. Update the completion number, blocking items, next action and time of `progress.json`.
8. Continue to the next task until the current Level is completed or a stop condition is triggered.

## Stop condition

You must stop and report any of the following situations:

- Requires real API Key, account, paid model or private service.
- The command writes to the user's global Agent configuration, shell profile, system directory, or home configuration directory.
- Commands may delete, overwrite, migrate or batch overwrite non-cached directories.
- The task requires the installation of a browser extension, IDE plug-in, or real Claude Code plug-in, and there is no temporary configuration directory.
- The same blocking failed 3 times in a row.
- The project documentation is clearly inconsistent with the actual commands, and continuing to execute would pollute the evidence.

## evidence requirements

Each execution must be logged:

- Date and native environment summary.
- A command or action.
- Execution scope, for example `.cache/sources/<owner__repo>/`.
- Result: `pass`, `fail`, `partial`, `not_run` or `blocked`.
- Output a summary without copying large sections of third-party content.
- Impact on learning TODO and progress.

Tasks that are not_run must remain unfinished and cannot be marked as run just because the README has been read.

## Automatic execution level

- `yes`: Read-only reading, source code location, document organization, and side-effect-free verification.
- `guarded`: Run in `.cache/`, temporary directory or temporary configuration. Check whether the command will write the global status before execution.
- `manual-confirm`: Requires explicit confirmation from the user, usually involving real installation, plug-in activation, global configuration, external account or paid API.

## Recommended prompt words

```text
Continue to learn <project_id> and execute LEARN_WITH_AGENT.md. Only process the next unfinished task; if the task can be executed automatically, execute it, record evidence, update notes and progress, and then continue with the next task at the same level. Stop immediately when encountering stopping conditions, and explain the cause of the obstruction and the recommended next step.
```

```text
Check if <project_id> can be promoted from analyzing to study-ready. Meta.json, evidence.md, learning-todo-list.md and progress.json must be read. Only real running or source code verification evidence is accepted, speculation is not accepted.
```

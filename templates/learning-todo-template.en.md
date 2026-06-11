# <Project Name> Learning Todo List

## Usage scenarios

Used to generate learning tasks for a single project from understanding, running through, source code understanding, integration, transformation to summary evaluation.

## Fill in the instructions

- Each task must be able to be performed or checked, and have clear completion criteria.
- Each task must indicate the evidence placement point, usually learning notes and `evidence.md`.
- Synchronously update `learning-notes/<owner__repo>/progress.json` after the task is completed.
- For tasks involving installation, global configuration, paid APIs, keys, or destructive commands, `Agent Automation` must write `manual-confirm`.

## Standard structure

## Level 1: Understand the project

| Status | task_id | Level | Goal | Preconditions | Operation/Command | Expected evidence | Completion criteria | Failure handling | Agent automatic execution |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `<ID>-L1-01` | Level 1 | Read README and official documents | Project links are accessible | Read-only | `01-first-impression.md`, `evidence.md` Source records | Can describe the project positioning, problems and applicable scenarios in one sentence | Record missing documents or access failures | yes |
| [ ] | `<ID>-L1-02` | Level 1 | Record first impressions and issues to be verified | completed L1-01 | Write notes on first impressions | `01-first-impression.md` | Notes distinguish between known facts, speculations, and items to be verified | Mark blocked and write down gaps | yes |

Output: `01-first-impression.md`.

## Level 2: Run-through project

| Status | task_id | Level | Goal | Preconditions | Operation/Command | Expected evidence | Completion criteria | Failure handling | Agent automatic execution |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `<ID>-L2-01` | Level 2 | Install or prepare an isolated running environment | Use `.cache/` or temporary directory | Perform official minimal installation or dry-run | `02-quickstart-notes.md`, `evidence.md` command record | Record version, environment, write range and output summary | Log exit code, stderr summary and next step on failure | guarded |
| [ ] | `<ID>-L2-02` | Level 2 | Run through the minimum Demo or read-only equivalent command | L2-01 completed | Execute the minimum command | `02-quickstart-notes.md`, `evidence.md` | Explicitly pass/fail/blocked, do not exaggerate the results | Stop when a key or paid API is required | guarded |

Output: `02-quickstart-notes.md`.

## Level 3: Understand the source code

| Status | task_id | Level | Goal | Preconditions | Operation/Command | Expected evidence | Completion criteria | Failure handling | Agent automatic execution |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `<ID>-L3-01` | Level 3 | Fixed source code commit and find the entry file | Source code is accessible | Read-only source code location | `04-source-reading-notes.md`, `evidence.md` commit record | Can point to the entry file and main call chain | Record the replacement basis when the source code is missing | yes |
| [ ] | `<ID>-L3-02` | Level 3 | Found Agent Loop, tool, Memory/RAG/MCP or context management module | L3-01 completed | Read-only source code analysis | `04-source-reading-notes.md` and call chain diagram | Key conclusions have source code paths or speculation boundaries | Leave as pending if it cannot be verified | yes |

Output: `04-source-reading-notes.md` and call chain graph.

## Level 4: Complete integration

| Status | task_id | Level | Goal | Preconditions | Operation/Command | Expected evidence | Completion criteria | Failure handling | Agent automatic execution |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `<ID>-L4-01` | Level 4 | Complete minimal integration in temporary project | Level 2 with running evidence | Perform integration using temporary configuration | `05-integration-notes.md`, `evidence.md` | Record write scope, permissions, rollback path and results | Stop before writing global configuration | manual-confirm |
| [ ] | `<ID>-L4-02` | Level 4 | Record integration problems and solutions | L4-01 Complete or clear blocked | Organize problem list | `05-integration-notes.md`, `06-troubleshooting-notes.md` | Each problem has recurrence, cause, and treatment method | Mark pending when it cannot be reproduced | yes |

Output: `05-integration-notes.md`.

## Level 5: Transformation Extension

| Status | task_id | Level | Goal | Preconditions | Operation/Command | Expected evidence | Completion criteria | Failure handling | Agent automatic execution |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `<ID>-L5-01` | Level 5 | Complete a low-risk extension or retrofit design | Level 4 Complete or have alternative validation scope | Design/validate in a staging branch or sandbox | `07-reflection.md` or retrofit summary, `evidence.md` | Explain retrofit costs, risks, and rollback paths | Stop when keys or production configurations are involved | manual-confirm |
| [ ] | `<ID>-L5-02` | Level 5 | Add evaluation, regression or quality inspection ideas | L5-01 completed | Design minimum inspection | Transformation summary | Check items are reusable and have clear boundaries | State the reason when it cannot run | guarded |

Output: transformation summary and reusable experience.

## Level 6: Summary evaluation

| Status | task_id | Level | Goal | Preconditions | Operation/Command | Expected evidence | Completion criteria | Failure handling | Agent automatic execution |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `<ID>-L6-01` | Level 6 | Write down the project's advantages and disadvantages, applicable scenarios and not applicable scenarios | Preface notes have been updated | Summarize evidence and notes | `07-reflection.md` | The evaluation is supported by evidence, do not regard pending as a fact | Clear restrictions when running evidence is missing | yes |
| [ ] | `<ID>-L6-02` | Level 6 | Generate review questions and compare similar products | L6-01 completed | Write review questions | `review-questions.md` | Questions cover usage, source code, integration, risks | Mark the missing comparison samples to be filled | yes |

Output: `07-reflection.md` and `review-questions.md`.

## To-do check items

- [ ] Each Level has tasks and outputs.
- [ ] learning tasks cover usage, source code, integration, transformation and summary.
- [ ] The current completion status has been synchronized to the learning progress.

## Quality check items

- [ ] Tasks from shallow to deep.
- [ ] Tasks are executable and checkable.
- [ ] does not make "read more information" the only task.
- [ ] The learning output path is clear.
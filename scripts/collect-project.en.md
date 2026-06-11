# project collection process specification

This document defines the standard processing flow when the AI Agent receives the following instructions:

```text
Collect: https://github.com/<owner>/<repo>
```

The current file is a process specification, not a runnable script.

## Core Agreement

- Project Directory ID: `owner__repo`.
- Project information directory: `projects/<category>/<owner__repo>/`.
- Learning notes directory: `learning-notes/<owner__repo>/`.
- Third-party source code cache: `.cache/sources/<owner__repo>/`.
- Run cache: `.cache/runs/<owner__repo>/`.
- Project metadata: `projects/<category>/<owner__repo>/meta.json`.
- Project evidence file: `projects/<category>/<owner__repo>/evidence.md`.
- Learning progress file: `learning-notes/<owner__repo>/progress.json`.

## Write to whitelist

A single collect only allows writing:

- `projects/<category>/<owner__repo>/`
- `learning-notes/<owner__repo>/`
- `PROJECTS.md`
- `LEARNING_PROGRESS.md`

Not to be modified:

- `docs/` Original information
- Other project directories
- Other project learning notes
- Local private configuration and key files

## Standard process

1. Parse the GitHub URL.
2. Get project information.
3. Determine whether it is related to AI Agent.
4. Determine the collection level.
5. Create a project directory.
6. Generate project analysis documents.
7. Generate diagrams files.
8. Generate Learning Todo List.
9. Generate `learning-notes/<owner__repo>/`.
10. Generate or update `meta.json`.
11. Generate or update `evidence.md`.
12. Update `PROJECTS.md`.
13. Update `LEARNING_PROGRESS.md`.
14. Run `python scripts/check-agent-dive.py`.
15. Output the collection report.

## collect pre-judgment

- [ ] Whether it is explicitly related to the AI Agent.
- [ ] Is there a README or official documentation.
- [ ] Whether there is analyzable source code.
- [ ] Are there examples, docs or usage instructions?
- [ ] License whether to allow learning organization and citation.
- [ ] Whether this is a duplicate collection.
- [ ] Whether it has learning value.
- [ ] Whether it has engineering reference value.
- [ ] Whether it is possible to generate Learning Todo List.
- [ ] Whether it is possible to generate at least one valid diagram.
- [ ] Whether it is possible to record clear evidence distinguishing `pass`, `fail`, `partial`, `not_run` and `blocked`.

## Collection level

| grade | name | Applicable objects | Output requirements |
|---|---|---|---|
| Level A | In-depth collection | Core focus projects | Complete documentation, source code breakdown, diagrams, integration, troubleshooting, learning notes, evaluation |
| Level B | Standard collection | Strong general projects | Overview, quick start, core principles, basic diagrams, learning tasks, brief evaluation |
| Level C | Lightweight collection | Projects to watch | Project introduction, recommendation reasons, classification tags, follow-up analysis suggestions |
| Level D | Not collecting yet | Projects that do not meet the requirements | Reasons for not collecting, risk description, alternative project suggestions |

## Project status

| state | meaning |
|---|---|
| `candidate` | Candidate projects |
| `triaging` | Evaluating |
| `accepted` | Passed collection evaluation |
| `analyzing` | Analyzing |
| `documented` | Document has been generated |
| `diagrammed` | diagrams have been generated |
| `study-ready` | Study materials are ready |
| `in-study` | learning |
| `completed` | Study completed |
| `archived` | Archive or stop maintenance |

## Output requirements

After collect is completed, it must output:

- collection conclusion.
- collection levels and categories.
- Generate file list.
- Content verified.
- Content not verified.
- Risks and matters to be manually confirmed.
- Result of `python scripts/check-agent-dive.py`.

## evidence requirements

- GitHub metadata, source code commit, running command, test command, output summary and failure reason are all written to `evidence.md`.
- Unexecuted commands are written as `not_run`, and tasks blocked by environment or permissions are written as `blocked`.
- A project can be marked as run-through only if there is a real pass record in `evidence.md`.
- Do not copy large sections of third-party README, source code or logs.

## Quality Access Control

- [ ] No false project run results are generated.
- [ ] Failure to write unverified conclusions as facts.
- [ ] No keys, accounts, local absolute paths or private information are written.
- [ ] `PROJECTS.md` is consistent with the project directory status.
- [ ] `LEARNING_PROGRESS.md` Only log overview.
- [ ] diagrams have provenance or clearly marked speculative boundaries.
- [ ] `meta.json`, `evidence.md`, `progress.json` are consistent with the index status.
- [ ] `python scripts/check-agent-dive.py` Passed.

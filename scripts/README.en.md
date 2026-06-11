# Scripts

This directory stores lightweight process descriptions and subsequent automation entries.

At the current stage, no real automated collection program has been implemented. `collect-project.md` is the collection process specification, used to guide manual or AI Agent-assisted execution.

A lightweight consistency check script has been provided:

```bash
python scripts/check-agent-dive.py
```

This script only checks the consistency of repository documents, metadata, learning progress, and evidence files. It does not connect to the Internet, execute third-party project commands, or modify files.

For detailed usage instructions and Hermes Agent examples, see [collect-project-usage.md](collect-project-usage.en.md).

## Follow-up script principles

- No complex dependencies are introduced.
- `docs/` is not modified by default.
- The writing range must be limited to the current project directory, the corresponding learning notes directory, `PROJECTS.md` and `LEARNING_PROGRESS.md`.
- `meta.json`, `evidence.md` and `learning-notes/<owner__repo>/progress.json` must be maintained for each collect or update.
- The project status must be supported by evidence before it can be upgraded to `study-ready`, `in-study` or `completed`.
- The third-party source code cache is placed in `.cache/sources/<owner__repo>/`, and the running cache is placed in `.cache/runs/<owner__repo>/`.
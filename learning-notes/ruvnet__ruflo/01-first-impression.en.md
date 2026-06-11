# Ruflo First impressions

## Initial impressions

- Ruflo is a large and comprehensive multi-agent harness, not a single Agent SDK.
- It puts Claude Code plugin, CLI full install, MCP server, Codex `.agents`, Web UI and plugin marketplace in the same ecosystem.
- The repository still retains the Claude Flow naming, and you must distinguish between `ruflo`, `claude-flow`, `@claude-flow/cli` and `@claude-flow/codex` when reading.

## Points worth learning

- Production details of MCP stdio: stdout filtering, JSON-RPC parser, buffer cap.
- SwarmCoordinator's agent lifecycle, task distribution, metrics and topology management.
- WorkflowEngine's task dependencies, pause/resume, rollback and debug info.
- SQLite + AgentDB layering of Hybrid memory.
- Boundary description between Plugin lite and CLI full install.
- Verification witness uses signed manifest to prevent regression.

## First batch of questions

- `ruflo@latest` Will heavy model or embedding dependencies be downloaded during startup?
- What files are actually written by CLI full init?
- Are the number of MCP tool list and README consistent?
- Does the Codex read `.agents/config.toml` and `.agents/skills/`?
- Claude hooks of ` |  | What does true` mean for security access control?

## Current conclusion

Ruflo is suitable for Level A in-depth collection, but it cannot just recite the README. The next step must be to fix the real behavior with the read-only CLI and MCP tool list.

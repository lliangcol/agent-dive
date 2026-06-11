# Ruflo

Ruflo is a multi-agent orchestration harness for Claude Code and Codex. It puts CLI, MCP server, swarm coordination, agent memory, Claude Code plugin, Codex `.agents` configuration, hooks, plug-in market and Web UI in the same warehouse to coordinate multi-Agent workflow.

## collect information

| Field | value |
|---|---|
| Project name | Ruflo |
| Project ID | `ruvnet__ruflo` |
| GitHub | https://github.com/ruvnet/ruflo |
| Project home page | https://flo.ruv.io/ |
| Main category | `multi-agent` |
| Auxiliary tags | `agentic-coding`、`mcp-tools`、`claude-code`、`codex`、`swarm`、`memory`、`plugin-system` |
| collectlevel | Level A depth collect |
| Current status | `analyzing` |
| Default branch | `main` |
| collect snapshot | 2026-06-11 |
| Analysis Commit | `6a2964ac94e10ca9916da030302686c725638adb` |
| Whether to run verification locally | no |

## Why collect

- Explicitly related to AI Agent: README positions Ruflo as a multi-agent AI harness for Claude Code and Codex. The core concepts include swarm, agents, memory, MCP, hooks and federation.
- High learning value: can disassemble multi-Agent topology, task distribution, MCP tool surface, memory backend, plugin lifecycle, hook behavior and Codex / Claude Code integration differences.
- High engineering reference value: The warehouse contains npm packages, CLI, MCP server, Web UI, plug-in directory, verification witness, Claude plugin, `.agents` configuration and a large number of test/verification materials.
- Suitable for deep collection: the project scope is large, there are many modules, and it highly overlaps with AgentDive’s multi-agent / MCP / agentic coding learning objectives.

## Data generated

- [project deep dive](project-analysis.en.md)
- [source reading record](source-code-reading.en.md)
- [integration guide](integration-guide.en.md)
- [Problem troubleshooting records](troubleshooting.en.md)
- [Learning Todo List](learning-todo-list.md)
- [collectreport](collect-report.en.md)
- [diagrams directory](assets/diagrams/)

## Current validation boundaries

Verified:

- The GitHub page is accessible and the repository is a public repository.
- `git ls-remote --symref` displays HEAD pointing to `refs/heads/main`, and the current HEAD is `6a2964ac94e10ca9916da030302686c725638adb`.
- npm metadata shows `ruflo@3.10.41`, `claude-flow@3.10.41`, `@claude-flow/cli@3.10.41`, and the Node engine is `>=20.0.0`.
- README description Claude Code plugin is a lite path, CLI install only registers MCP server and hooks.
- Currently there is no `.codex-plugin/plugin.json` in HEAD; on the Codex side there are mainly `.agents/config.toml` and `.agents/skills/`.
- `.claude-plugin/plugin.json` exists and declares that Claude Flow is compatible with MCP servers, including `claude-flow`, `ruv-swarm` and `flow-nexus`.
- `.claude-plugin/hooks/hooks.json` Configures for POSIX hooks and explains that Windows is written by init to the node-based equivalent.
- There are `SwarmCoordinator`, `WorkflowEngine`, `HybridBackend`, `PluginManager`, `MCPServer` and MCP tools in the source code.

Not verified:

- `npx ruflo@latest init`, `npx ruflo@latest mcp start` or `npm test` is not executed.
- The Claude Code plugin or the individual `ruflo-*` marketplace plugin is not installed.
- The true loading behavior of Codex `.agents/config.toml`, `.agents/skills/` and `@claude-flow/codex` is not verified.
- The web UI, mcp-bridge, daemon, worker, federation, or AgentDB/RuVector backend is not started.
- It has not been verified whether the number of capabilities, plug-ins and MCP tools in the README are completely consistent with the current build.

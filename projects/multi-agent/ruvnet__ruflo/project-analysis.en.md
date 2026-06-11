# Ruflo project deep dive

## 1. Basic project information

- Project name: Ruflo
- Project ID: `ruvnet__ruflo`
- GitHub：https://github.com/ruvnet/ruflo
- Official Documentation/Web UI: https://flo.ruv.io/
- Category: `multi-agent`
-Collect level: Level A deep collect
- Current status: `analyzing`
- Main language: TypeScript/JavaScript
- License：MIT
- Analysis date: 2026-06-11
- Analysis version/Commit:`6a2964ac94e10ca9916da030302686c725638adb`
- Whether to run verification: No
- Analysis basis: GitHub page, `git ls-remote`, README, `package.json`, `ruflo/package.json`, `ruflo/bin/ruflo.js`, `.claude-plugin/plugin.json`, `.claude-plugin/hooks/hooks.json`, `.agents/config.toml`, `v3/src/*`, `v3/@claude-flow/cli/src/*`, `verification/README.md`, `npm view`

## 2. Positioning in one sentence

Ruflo is an agent orchestration platform that combines multi-Agent swarm, MCP tools, memory backends, hooks, plug-ins and Codex / Claude Code integration.

## 3. Problems solved by the project

Common problems with a single AI coding assistant in complex tasks include: weak division of roles, thin cross-session memory, scattered tool surfaces, difficulty in uniform configuration of MCP servers and hooks, lack of status and observation for long tasks, and lack of security boundaries in team/cross-machine Agent collaboration. Ruflo attempts to make these capabilities into an installable harness: users introduce agent, swarm, memory, MCP, hooks and plug-in capabilities through the CLI or Claude Code plugin.

Learning value is mainly concentrated in six categories:

- Multi-agent coordination: How to define agents, swarm topology, task assignment, consensus and metrics.
- MCP-first tool surface: How CLI exposes tools such as agent, swarm, memory, task, session, and workflow in stdio/HTTP mode.
- Memory and learning: Engineering organization of SQLite/AgentDB/hybrid search, SONA, ReasoningBank, and trajectory learning.
- Plugin / hook system: How to combine Claude Code plugin, independent `ruflo-*` plugin, hooks and witness verification.
- Codex boundary: The current HEAD is dominated by `.agents/config.toml` and `.agents/skills/`, and the existence of `.codex-plugin/plugin.json` cannot be assumed.
- Product surface: CLI, Web UI, mcp-bridge, daemon, workers and marketplace together form the productization entrance.

## 4. Project main line

Ruflo's main line can be split into two paths:

1. Claude Code plugin path: User adds `ruvnet/ruflo` marketplace and installs a single `ruflo-*` plugin. The README makes it clear that this path is biased towards lite and mainly provides slash commands, skills and agent definitions, and does not register the complete Ruflo MCP server.
2. CLI install path: User executes `npx ruflo@latest init` or `npx ruflo@latest init wizard`. This path will be written to `.claude/`, `.claude-flow/`, `CLAUDE.md`, helpers, settings, etc., register MCP server and hooks, and enter the complete Ruflo loop.

At the source code level, the npm `ruflo` package is a thin wrapper, delegated to `@claude-flow/cli`. `@claude-flow/cli` also provides `init`, `agent`, `swarm`, `memory`, `mcp`, `task`, `session`, `workflow`, `hooks` and other commands and MCP tools. The core runtime types are in `v3/src/`: Agent represents the execution unit, SwarmCoordinator is responsible for agent management and task allocation, WorkflowEngine handles task dependencies and workflow, Memory backend is responsible for storage and retrieval, and PluginManager manages extension points.

## 5. Quick Start

### Environmental requirements

- Node.js: `>=20.0.0`, based on `ruflo/package.json`, root `package.json` and npm metadata.
- npm / npx。
- Optional: Claude Code, Codex, Docker, Git, MCP client.

### Installation path

```bash
# Claude Code plugin lite path, based on README
/plugin marketplace add ruvnet/ruflo
/plugin install ruflo-core@ruflo
/plugin install ruflo-swarm@ruflo
```

```bash
# CLI full path, based on README and npm metadata
npx ruflo@latest init wizard
npx ruflo@latest init
npm install -g ruflo@latest
```

```bash
# MCP server path, based on README
claude mcp add ruflo -- npx ruflo@latest mcp start
```

### Minimal verification recommendations

The Ruflo CLI is not executed this time. Subsequent real-life verification is recommended to start with a read-only or low-write command:

```bash
npx --yes ruflo@latest --version
npx --yes ruflo@latest --help
npx --yes ruflo@latest mcp start --help
npx --yes ruflo@latest init --help
```

Only after confirming the command loading cost, Node version and writing range, execute `init` in the temporary project.

### Known limitations

- The number of capabilities, plug-ins, and MCP tools in the README may drift with the version. The collect data only regards them as indicators to be reviewed.
- Claude Code plugin path and CLI install path have different capabilities. The result of plugin lite cannot be regarded as full loop.
- Codex support requires actual measurement of `.agents/config.toml`, `.agents/skills/`, `@claude-flow/codex`; currently HEAD does not find `.codex-plugin/plugin.json`.

## 6. Core architecture

Ruflo can be broken down into nine layers:

- npm packaging layer: `ruflo/package.json`, `ruflo/bin/ruflo.js`, exposed `ruflo` bin, delegated to `@claude-flow/cli`.
- CLI layer: `v3/@claude-flow/cli/src/commands/`, including init, agent, swarm, memory, mcp, workflow, hooks, daemon, doctor and other commands.
- MCP layer: `v3/@claude-flow/cli/bin/cli.js`, `v3/@claude-flow/cli/src/mcp-client.ts`, `v3/@claude-flow/cli/src/mcp-server.ts`, `v3/@claude-flow/cli/src/mcp-tools/`, responsible for stdio/HTTP MCP tool surface.
- Domain runtime layer: `v3/src/agent-lifecycle/`, `coordination/`, `task-execution/`, `memory/`.
- Memory layer: SQLite, AgentDB, HybridBackend, RAG / vector / graph / retrieval related modules.
- Plugin layer: `v3/src/infrastructure/plugins/`, `plugins/ruflo-*`, `.claude-plugin/`.
- Hook layer: `.claude-plugin/hooks/hooks.json`, plugin scripts, CLI `hooks` command.
- Codex configuration layer: `.agents/config.toml`, `.agents/skills/`, npm `@claude-flow/codex`.
- Verification layer: `verification/` witness manifests, smoke tests and signed regression protection.

diagrams see:

- `assets/diagrams/architecture.mmd`
- `assets/diagrams/install-surface.mmd`
- `assets/diagrams/mcp-memory-flow.mmd`
- `assets/diagrams/plugin-boundary.mmd`

## 7. Core Principles

### 7.1 Swarm coordination

`SwarmCoordinator` Maintain agent map, metrics, connections and topology. It supports spawn / terminate / list agents, distribute tasks by capacity and load, execute tasks concurrently, send agent messages, obtain hierarchy / mesh connection, scale agents and reach consensus. Current source code level reading shows that consensus still has simulated voting logic, and real production behavior needs to continue to track how the CLI/MCP layer connects to LLM or external workers.

### 7.2 Agent and workflow

`Agent` is a runtime entity that saves id, type, status, capabilities, role and metadata. `executeTask()` Responsible for state switching, callback execution, failure packaging and result return. `WorkflowEngine` Handles workflow execution, pause/resume, parallel execution, distributed workflow, rollback, metrics and debug info, and executes tasks through the coordinator.

### 7.3 MCP tool surface

`@claude-flow/cli/bin/cli.js` Enters MCP stdio mode on stdin pipe without normal parameters or explicit `mcp start` and processes JSON-RPC. There is a 10MB stdin buffer upper limit and stdout/stderr noise isolation in the source code, indicating that the stability of MCP stdio is the focus. `src/mcp-tools/index.ts` Aggregates agent, swarm, memory, config, hooks, task, session, workflow, analyze, security, embeddings, claims, wasm, guidance, autopilot and other tool groups.

### 7.4 Memory backend

`HybridBackend` Use SQLite as the main path for structured queries and write it to AgentDB when the memory is embedding for vector search and hybrid search. The CLI layer also has deeper modules such as BGE embedder, hybrid retrieval, graph edge writer, ReasoningBank/intelligence, etc., which require subsequent special reading.

### 7.5 Plugin and hook boundary

`.claude-plugin/plugin.json` declares Claude Code plugin metadata and MCP servers. `.claude-plugin/hooks/hooks.json` Configure PreToolUse, PostToolUse, PreCompact, and Stop, but comment clearly that the file is POSIX-only and pass ` |  | true` prevents hook script failure from blocking Claude Code turn. Windows is written by init to the node-based equivalent configuration. This boundary is important for security evaluation: the collect phase cannot equate the presence of hooks with mandatory security access.

### 7.6 Codex boundary

The README has a Codex badge and exists on npm `@claude-flow/codex@3.0.0-alpha.12`. But currently HEAD does not find `.codex-plugin/plugin.json`; the more specific materials on the Codex side in the warehouse are `.agents/config.toml` and `.agents/skills/`, in which MCP server `npx -y @claude-flow/cli@latest` and swarm/memory/sparc/security skills are configured. The loading behavior needs to be verified separately in Codex later.

## 8. Source code structure

- Ruflo npm wrapper：`ruflo/package.json`、`ruflo/bin/ruflo.js`
- Root package：`package.json`
- CLI bin：`bin/cli.js`、`v3/@claude-flow/cli/bin/cli.js`
- CLI commands：`v3/@claude-flow/cli/src/commands/`
- MCP tools：`v3/@claude-flow/cli/src/mcp-tools/`
- MCP server/client：`v3/@claude-flow/cli/src/mcp-server.ts`、`v3/@claude-flow/cli/src/mcp-client.ts`
- Domain exports：`v3/src/index.ts`
- Agent entity：`v3/src/agent-lifecycle/domain/Agent.ts`
- Swarm coordinator：`v3/src/coordination/application/SwarmCoordinator.ts`
- Workflow engine：`v3/src/task-execution/application/WorkflowEngine.ts`
- Memory backend：`v3/src/memory/infrastructure/*`
- Plugin runtime：`v3/src/infrastructure/plugins/*`
- Claude plugin：`.claude-plugin/`
- Codex-style config：`.agents/config.toml`、`.agents/skills/`
- Plugin marketplace：`plugins/ruflo-*`
- Web UI / bridge：`ruflo/src/`
- Verification：`verification/`

## 9. Key call chain

### Call chain 1: `ruflo` bin to CLI runtime

- Trigger condition: User execution `npx ruflo@latest <command>` or global `ruflo <command>`.
- Starting point: `ruflo/bin/ruflo.js`.
- Key steps: Find `@claude-flow/cli` -> MCP mode delegate `bin/cli.js`, normal CLI mode import `dist/src/index.js` and set `name: 'ruflo'`.
- Output: Ruflo CLI commands or MCP server behavior.
- Based on: `ruflo/bin/ruflo.js`, `ruflo/package.json`, npm metadata.

### Call chain 2: CLI command registry

- Trigger condition: CLI parses `init`, `agent`, `swarm`, `memory`, `mcp` and other commands.
- Starting point: `v3/@claude-flow/cli/src/commands/index.ts`.
- Key steps: Core commands are loaded synchronously, and advanced/management/analysis commands are imported on demand through lazy loader.
- Output: Corresponds to command handler execution.
- Basis: `commands/index.ts`.

### Call chain 3: MCP stdio server

- Trigger condition: stdin is piped and has no ordinary parameters, or explicit `mcp start` and no non-stdio transport is required.
- Starting point: `v3/@claude-flow/cli/bin/cli.js`.
- Key steps: Import `listMCPTools`, `callMCPTool`, `hasTool` -> read JSON-RPC line -> call MCP tool -> output JSON-RPC response.
- Output: Agent / swarm / memory / workflow and other MCP tool responses.
- Risk control: 10MB buffer upper limit, parse error / internal error response, stdout noise filtering.

### Call chain 4: Swarm task execution

- Trigger condition: MCP tool, CLI command or runtime call to create agent and execute tasks.
- Starting point: `SwarmCoordinator.spawnAgent()` / `distributeTasks()` / `executeTask()`.
- Key steps: Create Agent -> Maintain metrics/connections -> Allocate by task type and capability -> Call `Agent.executeTask()` -> Write to memory backend.
- Output: TaskResult, metrics, memory event.
- Basis: `SwarmCoordinator.ts`, `Agent.ts`.

### Call chain 5: Workflow execution

- Trigger condition: user or tool submits workflow definition.
- Starting point: `WorkflowEngine.executeWorkflow()`.
- Key steps: Create execution state -> Call plugin extension point -> Execute tasks in dependency order -> Optional nested workflow / rollback -> Record event log and metrics.
- Output: WorkflowResult, debug info, memory snapshots.
- Basis: `WorkflowEngine.ts`.

## 10. integration method

### Claude Code

Lightweight paths use plugin marketplace. The full path uses CLI init to have Ruflo write Claude settings, MCP server and hooks. The collect phase should first verify whether plugin lite only provides commands/agents/skills, and then verify the writing range of full init.

### Codex

Prioritize research on `.agents/config.toml` and `.agents/skills/`. Do not think of Claude Code hooks as Codex enabled controls. Later, you can individually test whether `@claude-flow/codex` generates or installs the Codex configuration.

### MCP client

README recommends:

```bash
claude mcp add ruflo -- npx ruflo@latest mcp start
```

When authenticating the local machine, first execute `mcp start --help`, and then use the isolated MCP client to check the tool list.

### Web UI / self-host

`ruflo/` contains Docker, mcp-bridge, Svelte-derived UI, nginx and ruvocal related directories. It is an independent product surface and the collect phase has not been started. The Web UI and CLI/MCP runtime should be verified separately later.

## 11. Problemshooting

See [troubleshooting.md](troubleshooting.en.md) for details. The first round focuses on Node version, plugin lite vs CLI full path, Codex boundary, non-blocking on hook failure, Windows hook override, MCP stdout pollution, capability number drift and init write range.

## 12. Objective evaluation

### advantage

- The learning surface is complete, covering multi-agent, MCP, memory, hooks, plugin, CLI, Web UI and verification.
- There are clear source code entities that are readable: Agent, SwarmCoordinator, WorkflowEngine, MemoryBackend, PluginManager, MCPServer.
- The README clearly explains the differences between plugin lite and CLI full path, which facilitates security boundary analysis.
- npm package, plug-in directory, verification witness and security policy reflect productization awareness.
- MIT License, public warehouse, suitable for learning and organization.

### shortcoming

- The scale of the project is large and it is easy to be biased by the number of READMEs. It must be verified based on the source code and operation results.
- The old name Claude Flow, the current name Ruflo, the root package name `claude-flow`, and the npm package `ruflo` coexist, and the naming boundaries are complicated.
- Hooks have ` by default |  | true`, is more like assisted automation and should not be treated as a strong blocking security access control.
- Codex support currently requires actual testing, and conclusions cannot be drawn based solely on the existence of badges or npm packages.
- Depends on external environments such as Node >=20, MCP, AgentDB/RuVector, Claude Code, etc., and the cost of complete verification is high.

### Applicable scenarios

- Learn multi-Agent swarm orchestration.
- Research the productization of MCP server and agent tool surface.
- Compare the capability boundaries between Claude Code plugin, CLI init, and Codex `.agents` configurations.
- Design team-level AI coding agent workflow, memory, hook and verification system.

### not applicable scenario

- Just want to learn the smallest Agent Loop.
- Environments that require low intrusion, zero global configuration writes.
- The isolation test project and rollback plan have not been prepared yet.
- Want to copy complete hooks/skills/plugins directly to the production repository without auditing.

## 13. Learning Todo List

See [learning-todo-list.md](learning-todo-list.en.md) for details.

## 14. Summary

Ruflo deserves to be considered as a Level A deep collection item. Its most valuable aspect is not a single command, but the merging of multi-agent, MCP, memory, plugin, hooks, verification and multi-harness integration into a complex but disassembled system. In the next round of learning, you should first run the read-only CLI help/version, then verify the MCP tool list, and finally test the write range of `init` in a temporary project.

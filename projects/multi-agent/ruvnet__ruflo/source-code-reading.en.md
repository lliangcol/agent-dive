# Ruflo source reading record

## 1. Reading objectives

- Questions to understand in this round: How Ruflo organizes CLI, MCP, swarm, memory, plugins, hooks and Codex / Claude Code integration into a multi-agent harness.
- Related functions: npm wrapper, CLI command registry, MCP stdio server, SwarmCoordinator, WorkflowEngine, HybridBackend, PluginManager, Claude plugin, Codex `.agents` config.
- Expected output: first-round module map, recommended reading order, key call chains and subsequent source code digging issues.

## 2. Source code entry

| Entrance | path | effect | in accordance with |
|---|---|---|---|
| Ruflo wrapper | `ruflo/bin/ruflo.js` | External `ruflo` bin, entrusted `@claude-flow/cli` | Source code / npm metadata |
| Root CLI wrapper | `bin/cli.js` | `claude-flow` bin, import V3 CLI | Source code |
| CLI entry | `v3/@claude-flow/cli/bin/cli.js` | CLI/MCP stdio automatic offloading, JSON-RPC processing, log filtering | Source code |
| Command registry | `v3/@claude-flow/cli/src/commands/index.ts` | Register init, agent, swarm, memory, mcp, hooks and other commands | Source code |
| MCP tools | `v3/@claude-flow/cli/src/mcp-tools/index.ts` | Aggregate tool groups such as agent, swarm, memory, workflow, and security | Source code |
| Domain exports | `v3/src/index.ts` | Export Agent, Task, SwarmCoordinator, WorkflowEngine, MemoryBackend, PluginManager, MCPServer | Source code |
| Swarm coordinator | `v3/src/coordination/application/SwarmCoordinator.ts` | Management agent, topology, task distribution, metrics, consensus | Source code |
| Workflow engine | `v3/src/task-execution/application/WorkflowEngine.ts` | Execute workflow, pause/resume, rollback, debug info | Source code |
| Hybrid memory | `v3/src/memory/infrastructure/HybridBackend.ts` | SQLite + AgentDB hybrid search | Source code |
| Claude plugin | `.claude-plugin/plugin.json`、`.claude-plugin/hooks/hooks.json` | Claude Code plugin metadata、MCP servers、hooks | Source code |
| Codex config | `.agents/config.toml`、`.agents/skills/` | Codex-style MCP/skills configuration | Source code |
| Verification | `verification/README.md` | signed witness regression protection | Source code |

## 3. Module map

| module | path | Responsibilities | Dependencies |
|---|---|---|---|
| npm wrapper | `ruflo/` | Publish `ruflo` package, delegate `@claude-flow/cli` | Depends on `@claude-flow/cli` |
| CLI command layer | `v3/@claude-flow/cli/src/commands/` | User command entry | Call runtime, MCP tools, init generators |
| MCP runtime | `v3/@claude-flow/cli/bin/cli.js`、`v3/@claude-flow/cli/src/mcp-*` | stdio/HTTP MCP server and tool dispatch | Depends on MCP tool registry |
| MCP tools | `v3/@claude-flow/cli/src/mcp-tools/` | Tool groups such as agent, swarm, memory, workflow, security, and embeddings | Call CLI services/runtime |
| Agent domain | `v3/src/agent-lifecycle/` | Agent status, capabilities and task execution | Called by coordinator |
| Swarm coordination | `v3/src/coordination/` | Topology, agent map, task assignment, metrics | writable memory backend |
| Task workflow | `v3/src/task-execution/` | workflow state, dependency sorting, rollback, distributed execution | Depend on coordinator |
| Memory | `v3/src/memory/`、`v3/@claude-flow/cli/src/memory/` | SQLite/AgentDB/embedding/hybrid retrieval | Depends on AgentDB/RuVector |
| Plugin system | `v3/src/infrastructure/plugins/`、`plugins/ruflo-*` | plugin lifecycle and extension points | Extended by workflow and CLI |
| Claude plugin | `.claude-plugin/`、`plugin/`、`plugins/ruflo-*` | marketplace plugin、hooks、commands、skills | Depends on Claude Code plugin loader |
| Codex integration | `.agents/`、`@claude-flow/codex` | Codex MCP/skills configuration | Actual loading to be verified |
| Web UI | `ruflo/src/` | chat UI、mcp-bridge、Docker self-host | Independent product side |
| Verification | `verification/` | witness manifest and regression protection | CI / scripts |

## 4. Recommended reading order

1. README, `ruflo/package.json`, root `package.json`, first clarify the relationship between Ruflo / Claude Flow / npm package names.
2. `ruflo/bin/ruflo.js`, `v3/@claude-flow/cli/bin/cli.js`, confirm the CLI and MCP mode switching.
3. `v3/@claude-flow/cli/src/commands/index.ts`, confirm the commands registry and lazy loading.
4. `v3/@claude-flow/cli/src/mcp-tools/index.ts`, lists MCP tool groups.
5. `v3/src/index.ts`、`Agent.ts`、`SwarmCoordinator.ts`、`WorkflowEngine.ts`。
6. `HybridBackend.ts`, `SQLiteBackend.ts`, `AgentDBBackend.ts` and CLI memory modules.
7. `.claude-plugin/plugin.json`、`.claude-plugin/hooks/hooks.json`、`plugins/ruflo-core/`。
8. `.agents/config.toml`、`.agents/skills/`、npm `@claude-flow/codex`。
9. `verification/README.md` and witness scripts.
10. `ruflo/src/` Web UI / mcp-bridge as an independent topic.

## 5. Key call chain

### Call chain 1: Ruflo CLI wrapper

- Trigger condition: `ruflo <command>` or `npx ruflo@latest <command>`.
- Starting point: `ruflo/bin/ruflo.js`.
- Key steps: Quick processing `--version` -> Find `node_modules/@claude-flow/cli` -> MCP mode import `bin/cli.js` -> Normal mode import `dist/src/index.js` and construct `CLI({ name: 'ruflo' })`.
- End point: command handler or MCP server.
- Basis: `ruflo/bin/ruflo.js`.

### Call chain 2: MCP stdio JSON-RPC

- Trigger condition: stdin pipe + no args, or explicit `mcp start` and no non-stdio transport.
- Starting point: `v3/@claude-flow/cli/bin/cli.js`.
- Key steps: Load `mcp-client.js` -> Create session id -> newline-based stdin parser -> `handleMessage()` -> tool list / call / hasTool.
- Endpoint: stdout output JSON-RPC response.
- Key risk control: stdout noise filtering, 10MB buffer upper limit, parse error / internal error clear return.
- Basis: `bin/cli.js`.

### Call chain 3: Agent spawn / execute

- Trigger condition: CLI/MCP/runtime creates agent and submits task.
- Starting point: `SwarmCoordinator.spawnAgent()`.
- Key steps: new `Agent(config)` -> metrics initialization -> topology connections -> eventBus emit -> optional write memory -> `distributeTasks()` -> `executeTask()`.
- End point: `TaskResult`, metrics, memory record.
- Basis: `SwarmCoordinator.ts`, `Agent.ts`.

### Call chain 4: Workflow engine

- Trigger condition: call `WorkflowEngine.executeWorkflow(workflow)`.
- Starting point: `WorkflowEngine.createExecution()`.
- Key steps: plugin `workflow.beforeExecute` -> event log -> dependency order -> nested workflow or task execution -> optional rollback -> `workflow.afterExecute`.
- End point: `WorkflowResult`, debug info, event log, memory snapshots.
- Basis: `WorkflowEngine.ts`.

### Call chain 5: Claude plugin hooks

- Trigger condition: Claude Code triggers PreToolUse / PostToolUse / PreCompact / Stop.
- Starting point: `.claude-plugin/hooks/hooks.json`.
- Key steps: matcher hits Bash / Write / Edit / MultiEdit -> Call `${CLAUDE_PLUGIN_ROOT}/scripts/ruflo-hook.sh` -> pass in modify-bash / modify-file / post-command / post-edit / session-end.
- Endpoint: hook output or no-op.
- Boundary: command strip ` |  | true`, failure will not block turn; the hooks.json is POSIX-only, Windows is written by init to the node-based equivalent configuration.

## 6. Read notes

- Important findings: The Claude Flow compatibility layer is still retained under the Ruflo name, and the root package `claude-flow` and the `ruflo` package exist at the same time.
- Important findings: README clearly distinguishes Claude Code plugin lite and CLI full install, and subsequent verification must separate the paths.
- Important findings: `.codex-plugin/plugin.json` is not currently found by HEAD, and the Codex path should be independently verified as `.agents/config.toml` / `.agents/skills/` / `@claude-flow/codex`.
- Important findings: MCP stdio's stdout pollution and large buffer DoS are explicitly handled by the source code, which are MCP productization details worth learning.
- Important findings: The Agent/Swarm/Workflow code in the runtime domain is relatively clear, but it still needs to be traced between it and the actual CLI/MCP tool.
- Uncertainty: The number of 100+ agents, 60+ commands, 30 skills, and MCP tools in the README needs to be verified with the build script or running results.
- Uncertainty: Claude plugin hooks default no-op on failure, and the true strength of the security access control needs to be verified.
- Uncertainty: The operating boundaries between Web UI/mcp-bridge and CLI MCP server need to be disassembled and verified.

## 7. To-do check items

- [x] Found Ruflo npm wrapper.
- [x] CLI/MCP entry found.
- [x] Found SwarmCoordinator/Agent/WorkflowEngine/HybridBackend.
- [x] Find Claude plugin and hooks manifest.
- [x] Found Codex-style `.agents` configuration.
- [ ] Run `ruflo --help` and `ruflo mcp start --help`.
- [ ] List actual MCP tools.
- [ ] Trace `agent-tools.ts` to specific CLI/runtime service.
- [ ] Trace `memory-tools.ts` to AgentDB/RuVector.
- [ ] Verify CLI init write range.

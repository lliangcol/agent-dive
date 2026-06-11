# Ruflo source reading notes

## Read entry

- `ruflo/bin/ruflo.js`
- `v3/@claude-flow/cli/bin/cli.js`
- `v3/@claude-flow/cli/src/commands/index.ts`
- `v3/@claude-flow/cli/src/mcp-tools/index.ts`
- `v3/src/index.ts`
- `v3/src/agent-lifecycle/domain/Agent.ts`
- `v3/src/coordination/application/SwarmCoordinator.ts`
- `v3/src/task-execution/application/WorkflowEngine.ts`
- `v3/src/memory/infrastructure/HybridBackend.ts`
- `v3/src/infrastructure/plugins/PluginManager.ts`
- `.claude-plugin/plugin.json`
- `.claude-plugin/hooks/hooks.json`
- `.agents/config.toml`

## Key records

- `ruflo/bin/ruflo.js` is a thin wrapper, normal CLI mode imports `@claude-flow/cli/dist/src/index.js`, MCP mode delegates to `@claude-flow/cli/bin/cli.js`.
- `@claude-flow/cli/bin/cli.js` has a fast path to `--version` to avoid heavy imports.
- MCP stdio parser has 10MB buffer cap and returns protocol level errors for JSON parse error and internal error.
- The command registry loads core commands synchronously, and other commands are lazy loaded.
- MCP tool registry aggregates agent, swarm, memory, config, hooks, task, session, workflow, security, embeddings, claims, wasm, guidance, autopilot and other groups.
- `SwarmCoordinator` Contains agent spawn/terminate/list, task distribution, concurrent execution, message, metrics, consensus, and scale.
- `WorkflowEngine` Contains execute/pause/resume/rollback/metrics/debug.
- `HybridBackend` Use SQLite for structured query, and write AgentDB with embedding memory.
- `.claude-plugin/hooks/hooks.json` Explicitly POSIX-only and pass ` |  | true` avoids hook failure blocking.

## To be continued tracking

- `mcp-tools/agent-tools.ts`, `swarm-tools.ts`, `memory-tools.ts` to the actual runtime service.
- `commands/init.ts` Go to settings/hooks/MCP file generator.
- `@claude-flow/codex` The source code and generation path of the package.
- hook scripts, witness scripts and smoke tests for `plugins/ruflo-core`.
- `ruflo/src/mcp-bridge` Boundary to Web UI.

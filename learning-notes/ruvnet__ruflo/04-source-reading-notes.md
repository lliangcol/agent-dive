# Ruflo 源码阅读笔记

## 已读入口

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

## 关键记录

- `ruflo/bin/ruflo.js` 是 thin wrapper，普通 CLI 模式导入 `@claude-flow/cli/dist/src/index.js`，MCP 模式委托到 `@claude-flow/cli/bin/cli.js`。
- `@claude-flow/cli/bin/cli.js` 对 `--version` 有 fast path，避免 heavy imports。
- MCP stdio parser 有 10MB buffer cap，并对 JSON parse error 和 internal error 返回协议级错误。
- command registry 同步加载核心命令，其他命令 lazy load。
- MCP tool registry 聚合 agent、swarm、memory、config、hooks、task、session、workflow、security、embeddings、claims、wasm、guidance、autopilot 等组。
- `SwarmCoordinator` 包含 agent spawn/terminate/list、task distribution、concurrent execution、message、metrics、consensus、scale。
- `WorkflowEngine` 包含 execute/pause/resume/rollback/metrics/debug。
- `HybridBackend` 结构化查询走 SQLite，带 embedding 的记忆写 AgentDB。
- `.claude-plugin/hooks/hooks.json` 明确 POSIX-only，并通过 `|| true` 避免 hook 失败阻断。

## 待继续追踪

- `mcp-tools/agent-tools.ts`、`swarm-tools.ts`、`memory-tools.ts` 到实际 runtime service。
- `commands/init.ts` 到 settings/hooks/MCP 文件生成器。
- `@claude-flow/codex` 包的源码和生成路径。
- `plugins/ruflo-core` 的 hook scripts、witness scripts 和 smoke tests。
- `ruflo/src/mcp-bridge` 与 Web UI 的边界。

# Ruflo 源码阅读记录

## 1. 阅读目标

- 本轮要理解的问题：Ruflo 如何把 CLI、MCP、swarm、memory、plugin、hooks 和 Codex / Claude Code 集成组织成 multi-agent harness。
- 关联功能：npm wrapper、CLI command registry、MCP stdio server、SwarmCoordinator、WorkflowEngine、HybridBackend、PluginManager、Claude plugin、Codex `.agents` config。
- 预期产出：首轮模块地图、推荐阅读顺序、关键调用链和后续源码深挖问题。

## 2. 源码入口

| 入口 | 路径 | 作用 | 依据 |
|---|---|---|---|
| Ruflo wrapper | `ruflo/bin/ruflo.js` | 对外 `ruflo` bin，委托 `@claude-flow/cli` | 源码 / npm metadata |
| Root CLI wrapper | `bin/cli.js` | `claude-flow` bin，导入 V3 CLI | 源码 |
| CLI entry | `v3/@claude-flow/cli/bin/cli.js` | CLI / MCP stdio 自动分流、JSON-RPC 处理、日志过滤 | 源码 |
| Command registry | `v3/@claude-flow/cli/src/commands/index.ts` | 注册 init、agent、swarm、memory、mcp、hooks 等命令 | 源码 |
| MCP tools | `v3/@claude-flow/cli/src/mcp-tools/index.ts` | 聚合 agent、swarm、memory、workflow、security 等工具组 | 源码 |
| Domain exports | `v3/src/index.ts` | 导出 Agent、Task、SwarmCoordinator、WorkflowEngine、MemoryBackend、PluginManager、MCPServer | 源码 |
| Swarm coordinator | `v3/src/coordination/application/SwarmCoordinator.ts` | 管理 agent、拓扑、任务分发、metrics、consensus | 源码 |
| Workflow engine | `v3/src/task-execution/application/WorkflowEngine.ts` | 执行 workflow、pause/resume、rollback、debug info | 源码 |
| Hybrid memory | `v3/src/memory/infrastructure/HybridBackend.ts` | SQLite + AgentDB hybrid search | 源码 |
| Claude plugin | `.claude-plugin/plugin.json`、`.claude-plugin/hooks/hooks.json` | Claude Code plugin metadata、MCP servers、hooks | 源码 |
| Codex config | `.agents/config.toml`、`.agents/skills/` | Codex-style MCP/skills 配置 | 源码 |
| Verification | `verification/README.md` | signed witness regression protection | 源码 |

## 3. 模块地图

| 模块 | 路径 | 职责 | 依赖关系 |
|---|---|---|---|
| npm wrapper | `ruflo/` | 发布 `ruflo` 包，委托 `@claude-flow/cli` | 依赖 `@claude-flow/cli` |
| CLI command layer | `v3/@claude-flow/cli/src/commands/` | 用户命令入口 | 调用 runtime、MCP tools、init generators |
| MCP runtime | `v3/@claude-flow/cli/bin/cli.js`、`v3/@claude-flow/cli/src/mcp-*` | stdio/HTTP MCP server 与 tool dispatch | 依赖 MCP tool registry |
| MCP tools | `v3/@claude-flow/cli/src/mcp-tools/` | agent、swarm、memory、workflow、security、embeddings 等工具组 | 调用 CLI services / runtime |
| Agent domain | `v3/src/agent-lifecycle/` | Agent 状态、能力和 task 执行 | 被 coordinator 调用 |
| Swarm coordination | `v3/src/coordination/` | 拓扑、agent map、task assignment、metrics | 可写入 memory backend |
| Task workflow | `v3/src/task-execution/` | workflow state、依赖排序、rollback、distributed execution | 依赖 coordinator |
| Memory | `v3/src/memory/`、`v3/@claude-flow/cli/src/memory/` | SQLite/AgentDB/embedding/hybrid retrieval | 依赖 AgentDB/RuVector |
| Plugin system | `v3/src/infrastructure/plugins/`、`plugins/ruflo-*` | plugin lifecycle 和 extension points | 被 workflow 和 CLI 扩展 |
| Claude plugin | `.claude-plugin/`、`plugin/`、`plugins/ruflo-*` | marketplace plugin、hooks、commands、skills | 依赖 Claude Code plugin loader |
| Codex integration | `.agents/`、`@claude-flow/codex` | Codex MCP/skills 配置 | 实际加载待验证 |
| Web UI | `ruflo/src/` | chat UI、mcp-bridge、Docker self-host | 独立产品面 |
| Verification | `verification/` | witness manifest 和回归保护 | CI / scripts |

## 4. 推荐阅读顺序

1. README、`ruflo/package.json`、root `package.json`，先理清 Ruflo / Claude Flow / npm 包名关系。
2. `ruflo/bin/ruflo.js`、`v3/@claude-flow/cli/bin/cli.js`，确认 CLI 与 MCP 模式切换。
3. `v3/@claude-flow/cli/src/commands/index.ts`，确认命令 registry 和 lazy loading。
4. `v3/@claude-flow/cli/src/mcp-tools/index.ts`，列出 MCP tool groups。
5. `v3/src/index.ts`、`Agent.ts`、`SwarmCoordinator.ts`、`WorkflowEngine.ts`。
6. `HybridBackend.ts`、`SQLiteBackend.ts`、`AgentDBBackend.ts` 和 CLI memory 模块。
7. `.claude-plugin/plugin.json`、`.claude-plugin/hooks/hooks.json`、`plugins/ruflo-core/`。
8. `.agents/config.toml`、`.agents/skills/`、npm `@claude-flow/codex`。
9. `verification/README.md` 与 witness scripts。
10. `ruflo/src/` Web UI / mcp-bridge 作为独立专题。

## 5. 关键调用链

### 调用链 1：Ruflo CLI 包装器

- 触发条件：`ruflo <command>` 或 `npx ruflo@latest <command>`。
- 起点：`ruflo/bin/ruflo.js`。
- 关键步骤：快速处理 `--version` -> 查找 `node_modules/@claude-flow/cli` -> MCP 模式导入 `bin/cli.js` -> 普通模式导入 `dist/src/index.js` 并构造 `CLI({ name: 'ruflo' })`。
- 终点：命令 handler 或 MCP server。
- 依据：`ruflo/bin/ruflo.js`。

### 调用链 2：MCP stdio JSON-RPC

- 触发条件：stdin pipe + no args，或显式 `mcp start` 且没有非 stdio transport。
- 起点：`v3/@claude-flow/cli/bin/cli.js`。
- 关键步骤：加载 `mcp-client.js` -> 建立 session id -> newline-based stdin parser -> `handleMessage()` -> tool list / call / hasTool。
- 终点：stdout 输出 JSON-RPC response。
- 关键风险控制：stdout 噪声过滤、10MB buffer 上限、parse error / internal error 明确返回。
- 依据：`bin/cli.js`。

### 调用链 3：Agent spawn / execute

- 触发条件：CLI/MCP/runtime 创建 agent 并提交 task。
- 起点：`SwarmCoordinator.spawnAgent()`。
- 关键步骤：new `Agent(config)` -> metrics 初始化 -> topology connections -> eventBus emit -> 可选写入 memory -> `distributeTasks()` -> `executeTask()`。
- 终点：`TaskResult`、metrics、memory record。
- 依据：`SwarmCoordinator.ts`、`Agent.ts`。

### 调用链 4：Workflow engine

- 触发条件：调用 `WorkflowEngine.executeWorkflow(workflow)`。
- 起点：`WorkflowEngine.createExecution()`。
- 关键步骤：plugin `workflow.beforeExecute` -> event log -> dependency order -> nested workflow 或 task execution -> 可选 rollback -> `workflow.afterExecute`。
- 终点：`WorkflowResult`、debug info、event log、memory snapshots。
- 依据：`WorkflowEngine.ts`。

### 调用链 5：Claude plugin hooks

- 触发条件：Claude Code 触发 PreToolUse / PostToolUse / PreCompact / Stop。
- 起点：`.claude-plugin/hooks/hooks.json`。
- 关键步骤：matcher 命中 Bash / Write / Edit / MultiEdit -> 调用 `${CLAUDE_PLUGIN_ROOT}/scripts/ruflo-hook.sh` -> 传入 modify-bash / modify-file / post-command / post-edit / session-end。
- 终点：hook 输出或 no-op。
- 边界：命令带 `|| true`，失败不会阻断 turn；该 hooks.json 为 POSIX-only，Windows 由 init 写入 node-based 等价配置。

## 6. 阅读笔记

- 重要发现：Ruflo 名称下仍保留 Claude Flow 兼容层，root 包 `claude-flow` 与 `ruflo` 包同时存在。
- 重要发现：README 明确区分 Claude Code plugin lite 和 CLI full install，后续验证必须分路径。
- 重要发现：当前 HEAD 未发现 `.codex-plugin/plugin.json`，Codex 路径应按 `.agents/config.toml` / `.agents/skills/` / `@claude-flow/codex` 单独验证。
- 重要发现：MCP stdio 的 stdout 污染和大 buffer DoS 被源码显式处理，是值得学习的 MCP 产品化细节。
- 重要发现：runtime domain 中的 Agent / Swarm / Workflow 代码相对清晰，但和实际 CLI/MCP 工具之间仍需继续追踪。
- 不确定点：README 中 100+ agents、60+ commands、30 skills、MCP tool 数量需要用构建脚本或运行结果复核。
- 不确定点：Claude plugin hooks 默认 no-op on failure，对安全门禁的真实强度需要运行验证。
- 不确定点：Web UI / mcp-bridge 与 CLI MCP server 的运行边界需要拆开验证。

## 7. 待办检查项

- [x] 找到 Ruflo npm wrapper。
- [x] 找到 CLI / MCP entry。
- [x] 找到 SwarmCoordinator / Agent / WorkflowEngine / HybridBackend。
- [x] 找到 Claude plugin 和 hooks manifest。
- [x] 找到 Codex-style `.agents` 配置。
- [ ] 运行 `ruflo --help` 和 `ruflo mcp start --help`。
- [ ] 列出实际 MCP tools。
- [ ] 追踪 `agent-tools.ts` 到具体 CLI/runtime service。
- [ ] 追踪 `memory-tools.ts` 到 AgentDB/RuVector。
- [ ] 验证 CLI init 写入范围。

# Ruflo 项目精读

## 1. 项目基本信息

- 项目名称：Ruflo
- 项目 ID：`ruvnet__ruflo`
- GitHub：https://github.com/ruvnet/ruflo
- 官方文档 / Web UI：https://flo.ruv.io/
- 分类：`multi-agent`
- 收录等级：Level A 深度收录
- 当前状态：`analyzing`
- 主要语言：TypeScript / JavaScript
- License：MIT
- 分析日期：2026-06-11
- 分析版本 / Commit：`6a2964ac94e10ca9916da030302686c725638adb`
- 是否运行验证：否
- 分析依据：GitHub 页面、`git ls-remote`、README、`package.json`、`ruflo/package.json`、`ruflo/bin/ruflo.js`、`.claude-plugin/plugin.json`、`.claude-plugin/hooks/hooks.json`、`.agents/config.toml`、`v3/src/*`、`v3/@claude-flow/cli/src/*`、`verification/README.md`、`npm view`

## 2. 一句话定位

Ruflo 是一个把多 Agent swarm、MCP 工具、记忆后端、hooks、插件和 Codex / Claude Code 集成组合起来的 agent orchestration 平台。

## 3. 项目解决的问题

单个 AI coding assistant 在复杂任务中常见问题包括：角色分工弱、跨会话记忆薄、工具表面分散、MCP server 和 hooks 难以统一配置、长任务缺少状态和观测、团队/跨机器 Agent 协作缺少安全边界。Ruflo 试图把这些能力做成一个可安装的 harness：用户通过 CLI 或 Claude Code plugin 引入 agent、swarm、memory、MCP、hooks 和插件能力。

学习价值主要集中在六类：

- Multi-agent coordination：如何定义 agent、swarm topology、task assignment、consensus 和 metrics。
- MCP-first tool surface：CLI 如何在 stdio / HTTP 模式下暴露 agent、swarm、memory、task、session、workflow 等工具。
- Memory and learning：SQLite / AgentDB / hybrid search、SONA、ReasoningBank、trajectory learning 的工程组织方式。
- Plugin / hook system：Claude Code plugin、独立 `ruflo-*` 插件、hooks 和 witness 验证如何组合。
- Codex boundary：当前 HEAD 以 `.agents/config.toml` 和 `.agents/skills/` 为主，不能假设存在 `.codex-plugin/plugin.json`。
- Product surface：CLI、Web UI、mcp-bridge、daemon、workers 和 marketplace 共同组成产品化入口。

## 4. 项目主线

Ruflo 的主线可以拆成两条路径：

1. Claude Code plugin 路径：用户添加 `ruvnet/ruflo` marketplace 并安装单个 `ruflo-*` plugin。README 明确该路径偏 lite，主要提供 slash commands、skills 和 agent definitions，不注册完整 Ruflo MCP server。
2. CLI install 路径：用户执行 `npx ruflo@latest init` 或 `npx ruflo@latest init wizard`。该路径会写入 `.claude/`、`.claude-flow/`、`CLAUDE.md`、helpers、settings 等，注册 MCP server 和 hooks，进入完整 Ruflo loop。

源码层面，npm `ruflo` 包是一个 thin wrapper，委托给 `@claude-flow/cli`。`@claude-flow/cli` 再提供 `init`、`agent`、`swarm`、`memory`、`mcp`、`task`、`session`、`workflow`、`hooks` 等命令和 MCP 工具。核心 runtime 类型在 `v3/src/`：Agent 表示执行单元，SwarmCoordinator 负责 agent 管理和任务分配，WorkflowEngine 处理任务依赖与工作流，Memory backend 负责存储和检索，PluginManager 管理扩展点。

## 5. 快速开始

### 环境要求

- Node.js：`>=20.0.0`，依据 `ruflo/package.json`、root `package.json` 和 npm metadata。
- npm / npx。
- 可选：Claude Code、Codex、Docker、Git、MCP client。

### 安装路径

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

### 最小验证建议

本次没有执行 Ruflo CLI。后续真实验证建议从只读或低写入命令开始：

```bash
npx --yes ruflo@latest --version
npx --yes ruflo@latest --help
npx --yes ruflo@latest mcp start --help
npx --yes ruflo@latest init --help
```

只有确认命令加载成本、Node 版本和写入范围后，再在临时项目执行 `init`。

### 已知限制

- README 中的能力数量、插件数量、MCP tool 数量可能随版本漂移，收录资料只把它们当作待复核指标。
- Claude Code plugin 路径和 CLI install 路径能力面不同，不能把 plugin lite 结果当作 full loop。
- Codex support 需要实测 `.agents/config.toml`、`.agents/skills/`、`@claude-flow/codex`；当前 HEAD 未发现 `.codex-plugin/plugin.json`。

## 6. 核心架构

Ruflo 可拆成九层：

- npm 包装层：`ruflo/package.json`、`ruflo/bin/ruflo.js`，对外暴露 `ruflo` bin，委托到 `@claude-flow/cli`。
- CLI 层：`v3/@claude-flow/cli/src/commands/`，包含 init、agent、swarm、memory、mcp、workflow、hooks、daemon、doctor 等命令。
- MCP 层：`v3/@claude-flow/cli/bin/cli.js`、`v3/@claude-flow/cli/src/mcp-client.ts`、`v3/@claude-flow/cli/src/mcp-server.ts`、`v3/@claude-flow/cli/src/mcp-tools/`，负责 stdio/HTTP MCP tool surface。
- Domain runtime 层：`v3/src/agent-lifecycle/`、`coordination/`、`task-execution/`、`memory/`。
- Memory 层：SQLite、AgentDB、HybridBackend、RAG / vector / graph / retrieval 相关模块。
- Plugin 层：`v3/src/infrastructure/plugins/`、`plugins/ruflo-*`、`.claude-plugin/`。
- Hook 层：`.claude-plugin/hooks/hooks.json`、plugin scripts、CLI `hooks` command。
- Codex 配置层：`.agents/config.toml`、`.agents/skills/`、npm `@claude-flow/codex`。
- Verification 层：`verification/` witness manifests、smoke tests 和 signed regression protection。

图解见：

- `assets/diagrams/architecture.mmd`
- `assets/diagrams/install-surface.mmd`
- `assets/diagrams/mcp-memory-flow.mmd`
- `assets/diagrams/plugin-boundary.mmd`

## 7. 核心原理

### 7.1 Swarm coordination

`SwarmCoordinator` 维护 agent map、metrics、connections 和 topology。它支持 spawn / terminate / list agents、按能力和负载分发 task、并发执行任务、发送 agent message、获取 hierarchy / mesh connection、scale agents 和 reach consensus。当前源码级阅读显示 consensus 仍有模拟投票逻辑，真实生产行为需要继续追踪 CLI / MCP 层如何接入 LLM 或外部 worker。

### 7.2 Agent and workflow

`Agent` 是运行时实体，保存 id、type、status、capabilities、role 和 metadata。`executeTask()` 负责状态切换、执行回调、失败包装和结果返回。`WorkflowEngine` 处理 workflow execution、pause/resume、parallel execution、distributed workflow、rollback、metrics 和 debug info，并通过 coordinator 执行 task。

### 7.3 MCP tool surface

`@claude-flow/cli/bin/cli.js` 在 stdin pipe 且无普通参数或显式 `mcp start` 时进入 MCP stdio 模式，并处理 JSON-RPC。源码中有 10MB stdin buffer 上限和 stdout/stderr 噪声隔离，说明 MCP stdio 稳定性是重点。`src/mcp-tools/index.ts` 聚合 agent、swarm、memory、config、hooks、task、session、workflow、analyze、security、embeddings、claims、wasm、guidance、autopilot 等工具组。

### 7.4 Memory backend

`HybridBackend` 将 SQLite 作为结构化查询主路径，并在 memory 带 embedding 时写入 AgentDB，用于 vector search 和 hybrid search。CLI 层还有 BGE embedder、hybrid retrieval、graph edge writer、ReasoningBank / intelligence 等更深模块，需后续专题阅读。

### 7.5 Plugin and hook boundary

`.claude-plugin/plugin.json` 声明 Claude Code plugin metadata 和 MCP servers。`.claude-plugin/hooks/hooks.json` 配置 PreToolUse、PostToolUse、PreCompact 和 Stop，但注释明确该文件为 POSIX-only，并通过 `|| true` 避免 hook 脚本失败阻断 Claude Code turn。Windows 由 init 写入 node-based 等价配置。这个边界对安全评价很重要：收录阶段不能把 hook 存在等同于强制安全门禁。

### 7.6 Codex boundary

README 有 Codex badge，并且 npm 上存在 `@claude-flow/codex@3.0.0-alpha.12`。但当前 HEAD 未发现 `.codex-plugin/plugin.json`；仓库中 Codex 侧更明确的材料是 `.agents/config.toml` 和 `.agents/skills/`，其中配置了 MCP server `npx -y @claude-flow/cli@latest` 与 swarm/memory/sparc/security skills。后续需要在 Codex 中单独验证加载行为。

## 8. 源码结构

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

## 9. 关键调用链

### 调用链 1：`ruflo` bin 到 CLI runtime

- 触发条件：用户执行 `npx ruflo@latest <command>` 或全局 `ruflo <command>`。
- 起点：`ruflo/bin/ruflo.js`。
- 关键步骤：查找 `@claude-flow/cli` -> MCP 模式委托 `bin/cli.js`，普通 CLI 模式导入 `dist/src/index.js` 并设置 `name: 'ruflo'`。
- 输出：Ruflo CLI 命令或 MCP server 行为。
- 依据：`ruflo/bin/ruflo.js`、`ruflo/package.json`、npm metadata。

### 调用链 2：CLI command registry

- 触发条件：CLI 解析 `init`、`agent`、`swarm`、`memory`、`mcp` 等命令。
- 起点：`v3/@claude-flow/cli/src/commands/index.ts`。
- 关键步骤：核心命令同步加载，advanced/management/analysis 命令通过 lazy loader 按需导入。
- 输出：对应 command handler 执行。
- 依据：`commands/index.ts`。

### 调用链 3：MCP stdio server

- 触发条件：stdin 被 pipe 且无普通参数，或显式 `mcp start` 且未要求非 stdio transport。
- 起点：`v3/@claude-flow/cli/bin/cli.js`。
- 关键步骤：导入 `listMCPTools`、`callMCPTool`、`hasTool` -> 读取 JSON-RPC line -> 调用 MCP tool -> 输出 JSON-RPC response。
- 输出：Agent / swarm / memory / workflow 等 MCP tool response。
- 风险控制：10MB buffer 上限、parse error / internal error 响应、stdout 噪声过滤。

### 调用链 4：Swarm task execution

- 触发条件：MCP tool、CLI command 或 runtime 调用创建 agent 并执行任务。
- 起点：`SwarmCoordinator.spawnAgent()` / `distributeTasks()` / `executeTask()`。
- 关键步骤：创建 Agent -> 维护 metrics/connections -> 按 task type 和 capability 分配 -> 调用 `Agent.executeTask()` -> 写入 memory backend。
- 输出：TaskResult、metrics、memory event。
- 依据：`SwarmCoordinator.ts`、`Agent.ts`。

### 调用链 5：Workflow execution

- 触发条件：用户或工具提交 workflow definition。
- 起点：`WorkflowEngine.executeWorkflow()`。
- 关键步骤：创建 execution state -> 调用 plugin extension point -> 按依赖顺序执行 task -> 可选 nested workflow / rollback -> 记录 event log 和 metrics。
- 输出：WorkflowResult、debug info、memory snapshots。
- 依据：`WorkflowEngine.ts`。

## 10. 集成方式

### Claude Code

轻量路径使用 plugin marketplace。完整路径使用 CLI init，让 Ruflo 写入 Claude settings、MCP server 和 hooks。收录阶段应先验证 plugin lite 是否只提供 commands/agents/skills，再验证 full init 的写入范围。

### Codex

优先研究 `.agents/config.toml` 与 `.agents/skills/`。不要把 Claude Code hooks 当成 Codex 已启用控制。后续可以单独测试 `@claude-flow/codex` 是否生成或安装 Codex 配置。

### MCP client

README 推荐：

```bash
claude mcp add ruflo -- npx ruflo@latest mcp start
```

本机验证时先执行 `mcp start --help`，再用隔离 MCP client 检查 tool list。

### Web UI / self-host

`ruflo/` 下包含 Docker、mcp-bridge、Svelte-derived UI、nginx 和 ruvocal 相关目录。它是独立产品面，收录阶段未启动。后续应将 Web UI 与 CLI/MCP runtime 分开验证。

## 11. 问题排查

详见 [troubleshooting.md](troubleshooting.md)。首轮重点是 Node 版本、plugin lite vs CLI full path、Codex 边界、hook 失败不阻断、Windows hook override、MCP stdout 污染、能力数量漂移和 init 写入范围。

## 12. 客观评价

### 优点

- 学习面完整，覆盖 multi-agent、MCP、memory、hooks、plugin、CLI、Web UI 和 verification。
- 有明确的源码实体可读：Agent、SwarmCoordinator、WorkflowEngine、MemoryBackend、PluginManager、MCPServer。
- README 对 plugin lite 和 CLI full path 的差异有清楚说明，便于做安全边界分析。
- npm 包、插件目录、验证 witness 和 security policy 体现产品化意识。
- MIT License，公开仓库，适合学习整理。

### 缺点

- 项目规模很大，容易被 README 数量宣传带偏，必须按源码和运行结果分层核验。
- 旧名 Claude Flow、现名 Ruflo、root 包名 `claude-flow`、npm 包 `ruflo` 并存，命名边界复杂。
- hooks 默认有 `|| true`，更像辅助自动化，不应当当作强阻断安全门禁。
- Codex support 当前需要实测，不能只凭 badge 或 npm 包存在下结论。
- 依赖 Node >=20、MCP、AgentDB/RuVector、Claude Code 等外部环境，完整验证成本高。

### 适用场景

- 学习多 Agent swarm orchestration。
- 研究 MCP server 和 agent tool surface 的产品化。
- 对比 Claude Code plugin、CLI init、Codex `.agents` 配置之间的能力边界。
- 设计团队级 AI coding agent workflow、记忆、hook 和验证体系。

### 不适用场景

- 只想学习最小 Agent Loop。
- 需要低侵入、零全局配置写入的环境。
- 尚未准备隔离测试项目和回滚方案。
- 想直接复制完整 hooks/skills/plugins 到生产仓库而不审计。

## 13. Learning Todo List

详见 [learning-todo-list.md](learning-todo-list.md)。

## 14. 总结

Ruflo 值得作为 Level A 深度收录项目。它最有价值的地方不是单个命令，而是把 multi-agent、MCP、memory、plugin、hooks、verification 和多 harness 集成合并成一个复杂但可拆解的系统。下一轮学习应优先跑只读 CLI help/version，再验证 MCP tool list，最后在临时项目中测试 `init` 的写入范围。

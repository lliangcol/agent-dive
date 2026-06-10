# Ruflo

Ruflo 是一个面向 Claude Code 和 Codex 的 multi-agent orchestration harness。它把 CLI、MCP server、swarm coordination、agent memory、Claude Code plugin、Codex `.agents` 配置、hooks、插件市场和 Web UI 放在同一仓库中，用来协调多 Agent 工作流。

## 收录信息

| 字段 | 值 |
|---|---|
| 项目名称 | Ruflo |
| 项目 ID | `ruvnet__ruflo` |
| GitHub | https://github.com/ruvnet/ruflo |
| 项目主页 | https://flo.ruv.io/ |
| 主分类 | `multi-agent` |
| 辅助标签 | `agentic-coding`、`mcp-tools`、`claude-code`、`codex`、`swarm`、`memory`、`plugin-system` |
| 收录等级 | Level A 深度收录 |
| 当前状态 | `analyzing` |
| 默认分支 | `main` |
| 收录快照 | 2026-06-11 |
| 分析 Commit | `6a2964ac94e10ca9916da030302686c725638adb` |
| 是否本机运行验证 | 否 |

## 为什么收录

- 与 AI Agent 明确相关：README 把 Ruflo 定位为 Claude Code 和 Codex 的 multi-agent AI harness，核心概念包括 swarm、agents、memory、MCP、hooks 和 federation。
- 学习价值高：可以拆解多 Agent 拓扑、任务分发、MCP tool surface、记忆后端、plugin lifecycle、hook 行为和 Codex / Claude Code 集成差异。
- 工程参考价值高：仓库包含 npm 包、CLI、MCP server、Web UI、插件目录、验证 witness、Claude plugin、`.agents` 配置和大量测试/验证资料。
- 适合做深度收录：项目范围大、模块多、和 AgentDive 的 multi-agent / MCP / agentic coding 学习目标高度重合。

## 已生成资料

- [项目精读](project-analysis.md)
- [源码阅读记录](source-code-reading.md)
- [集成指南](integration-guide.md)
- [问题排查记录](troubleshooting.md)
- [Learning Todo List](learning-todo-list.md)
- [收录报告](collect-report.md)
- [图解目录](assets/diagrams/)

## 当前验证边界

已验证：

- GitHub 页面可访问，仓库为公开仓库。
- `git ls-remote --symref` 显示 HEAD 指向 `refs/heads/main`，当前 HEAD 为 `6a2964ac94e10ca9916da030302686c725638adb`。
- npm metadata 显示 `ruflo@3.10.41`、`claude-flow@3.10.41`、`@claude-flow/cli@3.10.41`，Node engine 为 `>=20.0.0`。
- README 说明 Claude Code plugin 是 lite 路径，CLI install 才注册 MCP server 和 hooks。
- 当前 HEAD 没有 `.codex-plugin/plugin.json`；Codex 侧主要是 `.agents/config.toml` 与 `.agents/skills/`。
- `.claude-plugin/plugin.json` 存在，并声明 Claude Flow 兼容 MCP servers，包括 `claude-flow`、`ruv-swarm` 和 `flow-nexus`。
- `.claude-plugin/hooks/hooks.json` 为 POSIX hook 配置，并说明 Windows 由 init 写入 node-based 等价项。
- 源码中存在 `SwarmCoordinator`、`WorkflowEngine`、`HybridBackend`、`PluginManager`、`MCPServer` 和 MCP tools。

未验证：

- 未执行 `npx ruflo@latest init`、`npx ruflo@latest mcp start` 或 `npm test`。
- 未安装 Claude Code plugin 或单个 `ruflo-*` marketplace plugin。
- 未验证 Codex `.agents/config.toml`、`.agents/skills/` 和 `@claude-flow/codex` 的真实加载行为。
- 未启动 Web UI、mcp-bridge、daemon、worker、federation 或 AgentDB/RuVector 后端。
- 未验证 README 中能力数量、插件数量和 MCP tool 数量是否与当前构建完全一致。

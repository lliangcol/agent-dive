# Ruflo 架构笔记

## 当前理解

Ruflo 的架构可以看成四个同心层：

1. 用户入口：Ruflo CLI、Claude Code plugin、Codex `.agents`、Web UI。
2. 工具表面：CLI commands 和 MCP tools。
3. Runtime domain：Agent、SwarmCoordinator、WorkflowEngine、MemoryBackend、PluginManager。
4. 外部系统：Claude Code、Codex、AgentDB/RuVector、provider APIs、Docker/Web UI、verification CI。

## 关键边界

- Claude Code plugin lite 不等于 CLI full install。
- Codex `.agents` 不等于 Claude Code hooks。
- MCP stdio server 要保证 stdout 只承载 JSON-RPC。
- Hook 文件存在不等于强制门禁启用。
- Web UI / mcp-bridge 是产品面，和 CLI/MCP runtime 要分开验证。

## 图解

项目资料中已生成：

- `projects/multi-agent/ruvnet__ruflo/assets/diagrams/architecture.mmd`
- `projects/multi-agent/ruvnet__ruflo/assets/diagrams/install-surface.mmd`
- `projects/multi-agent/ruvnet__ruflo/assets/diagrams/mcp-memory-flow.mmd`
- `projects/multi-agent/ruvnet__ruflo/assets/diagrams/plugin-boundary.mmd`

## 待补充

- 实际 MCP tool list。
- CLI init 生成文件图。
- Codex `.agents` 加载流程。
- Web UI / mcp-bridge 请求链路。

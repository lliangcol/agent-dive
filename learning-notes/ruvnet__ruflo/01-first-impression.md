# Ruflo 第一印象

## 初步印象

- Ruflo 是一个大而全的 multi-agent harness，不是单一 Agent SDK。
- 它把 Claude Code plugin、CLI full install、MCP server、Codex `.agents`、Web UI 和 plugin marketplace 放在同一个生态中。
- 仓库仍保留 Claude Flow 命名，阅读时必须区分 `ruflo`、`claude-flow`、`@claude-flow/cli` 和 `@claude-flow/codex`。

## 值得学习的点

- MCP stdio 的产品化细节：stdout 过滤、JSON-RPC parser、buffer 上限。
- SwarmCoordinator 的 agent lifecycle、task distribution、metrics 和 topology 管理。
- WorkflowEngine 的任务依赖、pause/resume、rollback 和 debug info。
- Hybrid memory 的 SQLite + AgentDB 分层。
- Plugin lite 与 CLI full install 的边界说明。
- Verification witness 用 signed manifest 防回归的思路。

## 第一批问题

- `ruflo@latest` 启动是否会下载 heavy model 或 embedding 依赖？
- CLI full init 真实写入哪些文件？
- MCP tool list 与 README 数量是否一致？
- Codex 是否读取 `.agents/config.toml` 和 `.agents/skills/`？
- Claude hooks 的 `|| true` 对安全门禁意味着什么？

## 当前结论

Ruflo 适合 Level A 深度收录，但不能只复述 README。下一步必须用只读 CLI 和 MCP tool list 固定真实行为。

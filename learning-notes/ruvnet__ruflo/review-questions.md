# Ruflo 复习问题

1. Ruflo、Claude Flow、`@claude-flow/cli`、`@claude-flow/codex` 分别是什么关系？
2. Claude Code plugin lite 和 CLI full install 的能力差异是什么？
3. 为什么不能把 Claude Code hooks 推断为 Codex hooks？
4. `ruflo/bin/ruflo.js` 如何区分普通 CLI 模式和 MCP 模式？
5. `@claude-flow/cli/bin/cli.js` 为 MCP stdio 做了哪些稳定性处理？
6. `SwarmCoordinator` 如何选择 agent 执行 task？
7. `Agent.executeTask()` 如何处理失败？
8. `WorkflowEngine` 的 rollback 条件是什么？
9. `HybridBackend` 为什么同时使用 SQLite 和 AgentDB？
10. `.claude-plugin/hooks/hooks.json` 中 `|| true` 对安全门禁意味着什么？
11. `.agents/config.toml` 中配置了哪些 Codex 相关能力？
12. README 中的能力数量为什么需要运行复核？

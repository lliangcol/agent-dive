# RTK 复习问题

1. RTK 和普通 shell alias 的核心区别是什么？
2. 为什么 hook scripts 要做 thin delegate，而不是把 rewrite 逻辑复制到每个 Agent？
3. Codex 集成为什么不能等同于 Claude Code transparent hook？
4. `Deny > Ask > Allow > Default` 的权限优先级解决什么风险？
5. 什么情况下应该回读 raw output，而不是只看 RTK filtered output？
6. `RTK_TEE_DIR` 和 `RTK_TELEMETRY_DISABLED` 分别解决什么问题？
7. 如何验证 README 中的 token savings 结论？
8. 如果要新增一个 command filter，应该先读哪些模块和测试？

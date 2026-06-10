# RTK 第一印象

## 一句话印象

RTK 是给 AI 编码助手使用的命令输出压缩层，不是 Agent 框架，而是让 Agent 少读冗长 shell 输出的工具链基础设施。

## 值得关注

- Rust single binary，跨生态命令过滤覆盖面广。
- Hook 文档把 deployed hook、hook lifecycle、rewrite registry 和 command filters 分得比较清楚。
- Codex 路径是 prompt-level guidance，这一点需要和 Claude / Cursor 透明 hook 区分。
- 有 tracking、tee recovery 和 telemetry opt-in 文档，说明项目不只是简单 alias。

## 待验证问题

- README 的 60-90% savings 是否能在真实工作流复现。
- README 版本示例和 `Cargo.toml` 版本为何不一致。
- `rtk init --codex` 实际写入什么文件，是否易回滚。
- hook 权限模型在 compound command 上是否和文档一致。

# ECC 学习计划

## 学习目标

- 理解 ECC 如何把 agent workflow 从单一工具配置提升到跨 harness 操作系统。
- 找到 Codex、Claude Code、OpenCode、Cursor 的适配边界。
- 验证 selective install、hook lifecycle、MCP config、operator state 的实际行为。
- 总结可借鉴和不可照搬的设计。

## 阶段安排

1. 文档阅读：README、README.zh-CN、cross-harness architecture、release notes。
2. 只读验证：`ecc plan`、`ecc consult`、catalog 检查。
3. 源码阅读：CLI、installer、manifest、hook、control pane。
4. 最小集成：Codex minimal profile dry-run，Claude plugin hook 验证。
5. 对比复盘：与现有 AGENTS、skills、governance tooling 对比。

## 当前边界

本笔记尚未包含任何本机运行结果。所有命令都需要后续单独记录输出。

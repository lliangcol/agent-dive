# ECC 问题排查笔记

## 当前问题清单

| 问题 | 状态 | 下一步 |
|---|---|---|
| 重复安装造成重复 hooks/skills | 待验证 | 先 dry-run，记录 install-state |
| Codex hook parity 误解 | 文档级确认 | 按 instruction-backed 验证 |
| 写入范围不明 | 待验证 | 运行 `ecc plan --json` |
| 能力数量漂移 | 待验证 | 跑 catalog check |
| Windows installer 行为 | 待验证 | 在隔离环境测试 |

## 排查原则

- 每个问题保留原始命令和退出码。
- 不记录 token、账号、私有路径。
- 区分 README 说明、源码判断和本机运行结果。

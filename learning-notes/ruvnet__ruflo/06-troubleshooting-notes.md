# Ruflo 问题排查笔记

## 已识别问题

| 问题 | 当前状态 | 下一步 |
|---|---|---|
| Plugin lite 与 full install 混淆 | README 级确认 | 分路径验证 |
| Codex 支持边界不清 | 源码级初步确认 | 测 `.agents` 和 `@claude-flow/codex` |
| hooks 失败不阻断 | 源码级确认 | 触发 hook smoke |
| Windows hook 与 POSIX hook 不同 | 源码级确认 | Windows 临时项目验证 |
| MCP stdout 污染 | 源码有防护 | MCP client smoke |
| 能力数量漂移 | 待验证 | 跑 inventory / tool list |
| CLI init 写入范围大 | README 级确认 | 临时项目验证 |

## 记录要求

- 每个问题都要记录命令、环境、输出、写入文件和回滚方式。
- 与安全相关的问题必须区分“提示/辅助”与“硬阻断”。
- Windows 和 POSIX 行为分开记录。

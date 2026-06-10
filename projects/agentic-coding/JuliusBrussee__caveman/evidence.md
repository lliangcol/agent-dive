# Caveman Evidence

## Snapshot

- Project ID: `JuliusBrussee__caveman`
- GitHub: https://github.com/JuliusBrussee/caveman
- Category: `agentic-coding`
- Collect level: Level B
- Current status: `analyzing`
- Source snapshot commit: `655b7d9c5431f822264b7732e9901c5578ac84cf`
- Source cache path: `.cache/sources/JuliusBrussee__caveman`
- TODO progress at migration: 0/35

## Verification Status

| Area | Status | Notes |
|---|---|---|
| Runtime / CLI | `not_run` | 除非下方命令证据记录为 `pass`，否则不把本地运行计为已验证。 |
| Test suite | `not_run` | 尚未运行。 |
| Source review | `partial` | 已有首轮源码或文档分析，但函数级验证尚未完成。 |
| Diagrams | `draft` | 已有 Mermaid 图解；渲染产物和源码级准确性仍需复核。 |
| Learning notes | `created` | 学习笔记骨架已存在，后续必须随任务逐项更新。 |

## Command Evidence

| Date | Environment | Command / Operation | Scope | Result | Output summary | Follow-up |
|---|---|---|---|---|---|---|
| 2026-06-11 | AgentDive 文档分析 | 已查看 GitHub 元数据、README/docs 和部分源码路径 | 公开仓库和已生成的 AgentDive 文件 | `partial` | 已记录元数据和首轮分析；不声明本地运行通过。 | 继续推进 Level 2 和 Level 3 任务。 |
| pending | `.cache/sources/JuliusBrussee__caveman` | 运行 smoke 命令 | 隔离克隆或临时配置 | `not_run` | 尚未执行。 | 标记运行任务完成前，先记录命令、退出码、输出摘要和写入范围。 |

## 已知缺口

- Unified installer dry-run is not verified
- Local agent installation and uninstall behavior are not verified
- Source-level call chains for installer, hooks, MCP shrink, and memory compression are not verified
- Benchmarks and token statistics are not reproduced

## 下一步行动

- Run installer --list in a temporary clone
- Run installer dry-run and record write scope
- Trace installer, hooks, MCP shrink, and memory compression scripts

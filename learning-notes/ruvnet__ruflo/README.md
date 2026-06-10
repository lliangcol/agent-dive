# Ruflo 学习笔记

项目 ID：`ruvnet__ruflo`

对应资料目录：`projects/multi-agent/ruvnet__ruflo/`

## 当前阶段

- 当前状态：未开始正式学习
- 当前重点：先完成 README / package / CLI / MCP / `.agents` 边界理解和只读命令验证
- 最近更新：2026-06-11

## 笔记索引

- [学习计划](00-study-plan.md)
- [第一印象](01-first-impression.md)
- [快速开始笔记](02-quickstart-notes.md)
- [架构笔记](03-architecture-notes.md)
- [源码阅读笔记](04-source-reading-notes.md)
- [集成笔记](05-integration-notes.md)
- [问题排查笔记](06-troubleshooting-notes.md)
- [复盘总结](07-reflection.md)
- [复习问题](review-questions.md)

## 下一步

1. 阅读 README、`ruflo/package.json`、`.claude-plugin/plugin.json`、`.agents/config.toml`。
2. 执行只读命令 `npx --yes ruflo@latest --version` 和 `npx --yes ruflo@latest --help`。
3. 记录是否发生下载、耗时、stdout/stderr 和是否写入文件。
4. 沿 `ruflo/bin/ruflo.js`、`v3/@claude-flow/cli/bin/cli.js`、`mcp-tools/index.ts` 做源码阅读。

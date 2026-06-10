# CodeGraph

## 项目定位

CodeGraph 是一个面向 Claude Code、Codex CLI、Cursor、opencode、Hermes Agent、Gemini CLI、Antigravity IDE 和 Kiro 的本地代码知识图谱工具。它通过 CLI 建立 `.codegraph/codegraph.db`，再通过 MCP Server 向 Agent 暴露结构化代码搜索、源码探索、调用方、被调用方和影响面分析能力。

## 收录信息

| 字段 | 值 |
|---|---|
| 项目名称 | CodeGraph |
| GitHub | https://github.com/colbymchenry/codegraph |
| 官方文档 | https://colbymchenry.github.io/codegraph/ |
| 项目 ID | `colbymchenry__codegraph` |
| 分类 | `mcp-tools` |
| 收录等级 | Level A 深度收录 |
| 当前状态 | `analyzing` |
| 主要语言 | TypeScript |
| License | MIT |
| 分析日期 | 2026-06-10 |
| 分析版本 | `16c73e2b0e027411e22039baeb32fbe60ab42b4c` |
| 是否运行验证 | 否 |

## 资料索引

- [项目精读](project-analysis.md)
- [源码阅读记录](source-code-reading.md)
- [集成指南](integration-guide.md)
- [问题排查记录](troubleshooting.md)
- [Learning Todo List](learning-todo-list.md)
- [收录报告](collect-report.md)

## 图解

- [architecture.mmd](assets/diagrams/architecture.mmd)
- [indexing-pipeline.mmd](assets/diagrams/indexing-pipeline.mmd)
- [mcp-tool-flow.mmd](assets/diagrams/mcp-tool-flow.mmd)

## 验证边界

本次收录已读取 GitHub API、README、官方文档源码、`package.json` 和核心 TypeScript 源码结构；未安装 CLI、未运行 `codegraph init -i`、未跑测试套件，也未验证 README 中的 benchmark 数字。

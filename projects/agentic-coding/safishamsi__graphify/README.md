# Graphify

Graphify 是面向 AI 编码助手的知识图谱工具。它把代码、文档、SQL schema、脚本、论文、图片、视频等项目材料转成可查询的知识图谱，用于减少编码 Agent 对全文读取和临时 grep 的依赖。

## 收录信息

| 字段 | 值 |
|---|---|
| 项目名称 | Graphify |
| 项目 ID | `safishamsi__graphify` |
| GitHub | https://github.com/safishamsi/graphify |
| 项目主页 | https://graphifylabs.ai/ |
| 主分类 | `agentic-coding` |
| 辅助标签 | `knowledge-graph`、`rag-agents`、`mcp-tools`、`tree-sitter`、`context-engineering` |
| 收录等级 | Level B 标准收录 |
| 当前状态 | `analyzing` |
| 默认分支 | `v8` |
| 收录快照 | 2026-06-10 |
| 最近复核 | 2026-06-11 |
| 分析 Commit | `5504c84324fc9249eb4c9d0cca86da7140250032` |
| 是否本机运行验证 | 否 |

## 为什么收录

- 与 AI Agent 明确相关：README 明确面向 Claude Code、Codex、OpenCode、Cursor、Gemini CLI 等 AI 编码助手。
- 学习价值高：可用于理解代码库知识图谱、静态分析、语义抽取、上下文压缩、Agent 工具集成和 MCP server 输出。
- 工程参考价值明确：仓库包含 CLI、skill 安装、hook、图谱导出、MCP、Tree-sitter 解析、多模态输入等工程主题。
- 适合生成图解和学习任务：可以拆成架构图、构建流程图、助手集成图、MCP 查询图和排查图。

## 已生成资料

- [项目精读](project-analysis.md)
- [源码阅读记录](source-code-reading.md)
- [集成指南](integration-guide.md)
- [问题排查记录](troubleshooting.md)
- [Learning Todo List](learning-todo-list.md)
- [收录报告](collect-report.md)
- [图解目录](assets/diagrams/)

## 当前验证边界

已验证：

- GitHub 仓库公开存在。
- GitHub API 显示默认分支为 `v8`、主要语言为 Python、License 为 MIT，homepage 为 `https://graphifylabs.ai/`。
- 2026-06-11 复核时，GitHub API 显示 stars `64743`、forks `6578`、open_issues_count `328`。
- `git ls-remote --symref` 显示 HEAD 指向 `refs/heads/v8`，当前 HEAD 为 `5504c84324fc9249eb4c9d0cca86da7140250032`。
- README 描述了 `graphify` CLI、AI assistant skill 安装、输出 `graph.html`、`GRAPH_REPORT.md`、`graph.json`，以及 Codex / MCP / Neo4j / Tree-sitter / 多模态 extras 等能力。
- README 的隐私说明区分了数据路径：代码文件通过 Tree-sitter 本地 AST 处理；视频 / 音频使用 faster-whisper 本地转写；docs、PDF、图片会经由用户配置的 AI assistant / backend 做语义抽取。

未验证：

- 未在本机安装 `graphifyy` 或执行 `graphify .`。
- 未验证生成的 `graphify-out/` 内容。
- 未源码级确认 CLI、hook、MCP server、Tree-sitter parser、semantic extraction 的完整调用链。
- 未验证所有平台 skill 安装路径和 hook 行为。

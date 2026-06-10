# CodeGraph 学习笔记

## 学习状态

| 字段 | 值 |
|---|---|
| 项目 | CodeGraph |
| 项目 ID | `colbymchenry__codegraph` |
| 当前阶段 | source-reading |
| 完成进度 | 10/33 |
| 最近更新 | 2026-06-10 |

进度按 `learning-todo-list.md` 的任务项统计：已完成 Level 1 的 5 项和 Level 3 的 5 项。

## 第一印象

CodeGraph 是一个很适合用来学习 MCP 工具产品化的项目。它不是传统 Agent 框架，而是给 Agent 提供代码理解底座：先把仓库转成本地 SQLite 图谱，再把探索、搜索、调用关系和影响面分析暴露成 MCP tools。

## 已完成

- [x] 阅读 README 和官方文档入口。
- [x] 确认 GitHub 元数据、License、默认分支和最新 commit。
- [x] 浅读 CLI、MCP、installer、extraction、resolution、graph、sync 目录。
- [x] 生成项目精读、源码阅读记录、集成指南、排查记录、图解和学习任务。

## 待验证

- [ ] 安装 CLI 并记录版本。
- [ ] 在样例仓库运行 `codegraph init -i`。
- [ ] 启动或通过 Agent 调用 MCP tools。
- [ ] 跑 `npm test` 或关键测试子集。
- [ ] 复核 README benchmark 是否能在本地复现。

## 卡住的问题

当前没有硬阻塞；开放缺口是尚未进行 CLI/MCP 运行验证，也尚未运行测试套件。

## 下一步

选择一个公开中型 TypeScript 仓库，执行最小验证闭环：`codegraph init -i` -> `codegraph status` -> `codegraph query` -> Agent 中 `codegraph_explore`。

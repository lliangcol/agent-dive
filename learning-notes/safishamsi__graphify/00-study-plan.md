# Graphify 学习计划

## 学习目标

- 理解 Graphify 如何把项目材料转成知识图谱。
- 跑通一次最小图谱构建。
- 理解 Codex / Claude Code 集成方式和写入边界。
- 源码确认 CLI、抽取、图构建、导出、MCP server 的关键调用链。
- 总结它对 Agentic Coding 和上下文工程的借鉴价值。

## 阶段安排

1. 了解项目：阅读 README、docs 和安全说明。
2. 跑通使用：安装 `graphifyy`，对公开小仓库执行 `graphify .`。
3. 源码阅读：从 `graphify.__main__:main` 和 `graphify.serve:_main` 进入。
4. 集成验证：测试 Codex project install 和 MCP server。
5. 总结评价：对比 codebase-memory-mcp、普通 RAG 和 grep 工作流。

## 验证边界

- 未完成本机运行前，不把“可用”写成事实。
- 未读源码前，不把 README 流程写成真实调用链。
- 未检查 `SECURITY.md` 和 README Privacy 前，不对私有仓库中的 docs、PDF、图片等非代码材料执行 semantic extraction。

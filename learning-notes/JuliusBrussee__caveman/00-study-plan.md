# Caveman 学习计划

## 学习目标

- 理解 Caveman 如何把输出压缩规则分发到多个 AI 编码助手。
- 跑通一次无写入 dry-run，并记录 provider matrix。
- 理解 Claude Code hooks、statusline、mode flag 和自动激活路径。
- 源码确认 installer、MCP shrink、memory compression 的关键调用链。
- 总结它对 Agentic Coding、token governance 和技能分发的借鉴价值。

## 阶段安排

1. 了解项目：阅读 README、INSTALL.md、CLAUDE.md 和 hooks / MCP 文档。
2. 跑通使用：先 dry-run，再在隔离环境只安装一个 Agent 路径。
3. 源码阅读：从 `bin/install.js`、`src/hooks/`、`src/mcp-servers/caveman-shrink/` 进入。
4. 集成验证：测试 Codex 单路径、MCP shrink 和无敏感 memory compression。
5. 总结评价：对比普通 concise prompt、editor rule files、Codex skill 和 MCP metadata 优化。

## 验证边界

- 未完成 dry-run 前，不把安装写入范围写成事实。
- 未读源码前，不把 README / INSTALL.md 流程写成真实调用链。
- 未确认 API / CLI fallback 前，不对敏感记忆文件执行 `caveman-compress`。
- 未复现 benchmark 前，不把 README token savings 当作本地工作流收益。

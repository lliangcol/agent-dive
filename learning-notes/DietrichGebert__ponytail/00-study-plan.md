# Ponytail 学习计划

## 学习目标

1. 理解 Ponytail 的核心规则：为什么它能约束 AI 编码 Agent 少写代码，但仍要求保留安全、边界验证和必要测试。
2. 理解跨宿主分发方式：Codex、Claude Code、Copilot CLI、OpenCode、Gemini、Pi、OpenClaw 和 instruction-only 规则文件分别怎么接入。
3. 验证 lifecycle hook 的真实行为：SessionStart 注入、UserPromptSubmit 模式切换、SubagentStart 子代理注入、状态文件和宿主 payload。
4. 复核 benchmark 方法：区分 LOC、成本、延迟和 correctness gate，避免把 Claude 单轮结果泛化。

## 阶段安排

| 阶段 | 重点 | 完成标准 |
|---|---|---|
| L1 | 元数据、README、LICENSE、文件树 | 能准确说明项目定位和收录边界 |
| L2 | skill、commands、adapter 文档 | 能画出宿主到文件的映射 |
| L3 | hooks、config、runtime、OpenCode、Pi | 能解释模式注入和状态持久化 |
| L4 | 本地测试和真实宿主 smoke | 有可复现命令和 evidence |
| L5 | benchmark 和横向对比 | 能说明成本结论的适用范围 |
| L6 | 学习闭环 | 完成复习题、反思和状态更新 |

## 本轮之后的第一步

本轮已创建临时 Python venv，安装 pandas，并通过 venv-local `python3.exe` 让完整 `npm test` 通过。下一步进入 Codex / Claude 隔离 profile 的 plugin smoke，重点验证 hook 信任、mode 切换和 SubagentStart。

# ECC

ECC 是一个面向 AI 编码工具和 agent harness 的工作流操作系统。它把 skills、agents、commands、hooks、rules、MCP 配置、安装清单、会话/编排工具和安全门禁组织成可在 Claude Code、Codex、OpenCode、Cursor、Gemini、Zed 等工具间迁移的工程资产。

## 收录信息

| 字段 | 值 |
|---|---|
| 项目名称 | ECC |
| 项目 ID | `affaan-m__ECC` |
| GitHub | https://github.com/affaan-m/ECC |
| 项目主页 | https://ecc.tools |
| 主分类 | `agentic-coding` |
| 辅助标签 | `agent-harness`、`claude-code`、`codex`、`opencode`、`mcp-tools`、`security`、`workflow-automation` |
| 收录等级 | Level A 深度收录 |
| 当前状态 | `analyzing` |
| 默认分支 | `main` |
| 收录快照 | 2026-06-11 |
| 分析 Commit | `c888d2b73f26d605ff6c172b433d4cad2200206f` |
| 是否本机运行验证 | 否 |

## 为什么收录

- 与 AI Agent 明确相关：README 和 `package.json` 都将项目定位为面向 Codex、Claude Code、OpenCode、Cursor、Gemini 等 harness 的 agent workflow / operator system。
- 学习价值高：可以拆解 skills 格式、cross-harness 适配、hook 生命周期、安全门禁、MCP 配置、安装清单、会话记录、worktree 编排和 operator dashboard。
- 工程参考价值高：仓库包含 `scripts/`、`skills/`、`agents/`、`commands/`、`hooks/`、`rules/`、`.codex-plugin/`、`.claude-plugin/`、`.opencode/`、`ecc2/`、`tests/` 等完整产品化表面。
- 适合做深度收录：项目规模大、能力面广、和 AgentDive 的 agentic coding / governance / validation 学习目标高度重合。

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

- GitHub 仓库公开存在，GitHub API 显示默认分支为 `main`，主要语言为 JavaScript，License 为 MIT。
- `git ls-remote --symref` 显示 HEAD 指向 `refs/heads/main`，当前 HEAD 为 `c888d2b73f26d605ff6c172b433d4cad2200206f`。
- GitHub API 显示 topics 包含 `ai-agents`、`claude-code`、`developer-tools`、`llm`、`mcp`、`productivity`。
- README 描述了跨 Codex、Claude Code、Cursor、OpenCode、Gemini、Zed、GitHub Copilot 的 agent workflow 表面。
- `package.json` 显示 npm 包名 `ecc-universal`，版本 `2.0.0`，bin 包含 `ecc`、`ecc-control-pane`、`ecc-install`，Node engine 为 `>=18`。
- npm 元数据复核显示 `ecc-universal@2.0.0` 暴露 `ecc` bin，同时 npm 上存在独立的 `ecc@0.0.2` 包；后续验证应使用显式 package selector 或本地源码脚本，避免 `npx ecc` 解析到错误包。
- `docs/architecture/cross-harness.md` 说明 durable workflow 放在 `skills/`、`rules/`、`hooks/`、`scripts/`、`mcp-configs/`，各 harness 只做薄适配。
- `hooks/hooks.json` 包含 PreToolUse、PreCompact、SessionStart、PostToolUse、Stop、SessionEnd 等 hook 生命周期配置。

未验证：

- 未在本机安装 Claude plugin、Codex plugin 或 npm 包。
- 未运行 `npx --package ecc-universal ecc ...`、本地 `node scripts/ecc.js ...`、`ecc install`、`ecc plan`、`ecc doctor`、`npm test`。
- 未验证 hook 在 Claude Code、OpenCode、Cursor 中的真实触发行为。
- 未验证 Codex 的 skill、plugin、MCP 配置加载效果。
- 未源码级完整追踪 install、hook、control-pane、session、worktree lifecycle 的所有调用链。
- 未核验 README / release notes / plugin manifest 中能力数量是否完全一致。

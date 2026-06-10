# Claude HUD

Claude HUD is a Claude Code plugin that renders a live statusline below the input area. It surfaces model/project identity, context usage, subscriber usage windows, git state, tool activity, subagent activity, MCP/skill activity, todos, session metadata, and optional local system information.

## 收录信息

| 字段 | 值 |
|---|---|
| 项目名称 | Claude HUD |
| 项目 ID | `jarrodwatts__claude-hud` |
| GitHub | https://github.com/jarrodwatts/claude-hud |
| 项目主页 | https://github.com/jarrodwatts/claude-hud |
| 主分类 | `agentic-coding` |
| 辅助标签 | `claude-code`、`statusline`、`context-observability`、`usage-limits`、`transcript-jsonl`、`tool-activity`、`developer-tooling` |
| 收录等级 | Level B 标准收录 |
| 当前状态 | `analyzing` |
| 默认分支 | `main` |
| 收录快照 | 2026-06-11 |
| 分析 Commit | `9650a43600e9bcc94057fbd693a7f05aba4ee1ff` |
| 包版本 | `0.1.1` |
| 是否本机运行验证 | 否 |

## 为什么收录

- 与 AI 编码 Agent 明确相关：它直接接入 Claude Code plugin / statusLine 机制，用来观察 Claude Code 会话状态。
- 学习价值明确：适合学习 Claude Code statusline stdin、transcript JSONL、工具调用活动解析、上下文用量展示、rate limit 展示和配置迁移。
- 工程参考价值高：源码包含 TypeScript statusline 主程序、跨平台 setup 指令、配置验证、git 状态读取、transcript cache、外部 usage snapshot、渲染宽度处理和 Node test suite。
- 与现有 AgentDive 样例互补：它不是新的 Agent loop，而是 Agent 运行期可观测性和 Claude Code 用户体验增强工具。

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
- GitHub 页面显示仓库为 `jarrodwatts/claude-hud`，README 定位为 Claude Code plugin。
- GitHub 页面快照显示约 24.9k stars、约 1.1k forks、1 个 open issue 和 1 个 PR。
- `git clone --depth 1` 取得默认分支 `main`，HEAD 为 `9650a43600e9bcc94057fbd693a7f05aba4ee1ff`。
- `package.json` 显示项目名 `claude-hud`、版本 `0.1.1`、TypeScript/ESM、Node `>=18.0.0`、License `MIT`。
- 已读取 `.claude-plugin/plugin.json`、`commands/setup.md`、`commands/configure.md`、`src/index.ts`、`src/stdin.ts`、`src/transcript.ts`、`src/config.ts`、`src/render/index.ts` 和若干 render / usage / git 模块。
- 在 Windows 临时浅克隆中执行了 `npm ci` 和 `npm test`。依赖安装成功，`npm run build` 在测试流程中完成，但 `npm test` 退出码为 1，输出中采样到 31 个唯一失败测试名，主要集中在 config count、external usage、extra command、git、entrypoint 和 integration 渲染断言。

未验证：

- 未在真实 Claude Code 中执行 `/plugin marketplace add jarrodwatts/claude-hud`、`/plugin install claude-hud` 或 `/claude-hud:setup`。
- 未跑通真实插件安装、statusline 写入或 HUD 展示；因此本项目在 `PROJECTS.md` 中的“是否跑通”仍记为“否”。
- 未验证真实 `statusLine` 配置写入、已有 statusline 备份、Windows `statusline.mjs` wrapper 和 Claude Code 重启后的 HUD 展示。
- 未验证真实 Claude Code stdin `rate_limits`、transcript_path、background agent、TodoWrite、MCP tool name 等运行期 payload。
- 未复现 README 中约 300ms 刷新体验。
- 未确认 Windows 测试失败是否来自当前本机环境差异、依赖版本、Git Bash / PowerShell 差异或项目当前回归。

# Ponytail

Ponytail 是一个面向 AI 编码 Agent 的“懒惰资深开发者模式”规则集和多宿主插件分发包。它把 YAGNI、stdlib first、native platform first、最小正确实现和过度工程审查封装成可移植 skill、插件命令和生命周期 hook。

## 收录信息

| 字段 | 值 |
|---|---|
| 项目名称 | Ponytail |
| 项目 ID | `DietrichGebert__ponytail` |
| GitHub | https://github.com/DietrichGebert/ponytail |
| 项目主页 | https://github.com/DietrichGebert/ponytail |
| 主分类 | `agentic-coding` |
| 辅助标签 | `codex-plugin`、`claude-code-plugin`、`agent-portability`、`lifecycle-hooks`、`yagni`、`prompt-benchmarks` |
| 收录等级 | Level B 标准收录 |
| 当前状态 | `analyzing` |
| 默认分支 | `main` |
| 收录快照 | 2026-06-25 |
| 分析 Commit | `a945778b4a73b0b78c3c781a594b62cd3a324637` |
| 收录时最新 release | `v4.8.3` |
| `package.json` 版本 | `4.8.3` |
| 插件 manifest 版本 | `4.8.3` |
| 是否真实宿主运行验证 | 否 |

## 为什么收录

- 与 AI 编码 Agent 明确相关：README、`AGENTS.md`、`skills/`、`.codex-plugin/`、`.claude-plugin/` 和 `.github/plugin/` 都围绕编码 Agent 行为约束展开。
- 学习价值明确：适合研究“规则集如何跨 Codex、Claude Code、Copilot CLI、OpenCode、Gemini CLI、Pi、OpenClaw 等宿主分发”。
- 工程参考价值高：仓库包含共享 instruction builder、配置解析、SessionStart / UserPromptSubmit / SubagentStart hook、Windows PowerShell hook 回归测试、OpenCode server plugin、Pi extension、promptfoo benchmark 和同步校验脚本。
- 与现有 AgentDive 样例互补：它不是代码图谱或完整 Agent 框架，而是“Agent 输出治理和过度工程压缩”的轻量工具层样例。

## 已生成资料

- [项目精读](project-analysis.md)
- [源码阅读记录](source-code-reading.md)
- [集成指南](integration-guide.md)
- [问题排查记录](troubleshooting.md)
- [Learning Todo List](learning-todo-list.md)
- [收录报告](collect-report.md)
- [证据记录](evidence.md)
- [图解目录](assets/diagrams/)

## 当前验证边界

已验证：

- GitHub 仓库公开存在，默认分支为 `main`。
- 2026-06-25 GitHub API 快照显示主语言 JavaScript、MIT License、56052 stars、2833 forks、71 个 open issues，当时最近 push 时间为 `2026-06-24T13:37:06Z`。
- 2026-06-25 `git ls-remote` 与临时浅克隆确认当时 HEAD 为 `a945778b4a73b0b78c3c781a594b62cd3a324637`。
- `README.md`、`AGENTS.md`、`docs/agent-portability.md`、`package.json`、`.codex-plugin/plugin.json`、`.claude-plugin/plugin.json`、`.github/plugin/plugin.json`、`gemini-extension.json`、`hooks/`、`skills/`、`commands/`、`pi-extension/`、`.opencode/plugins/ponytail.mjs` 已抽样阅读。
- `node scripts/check-rule-copies.js` 通过。
- 临时 venv 中安装 `pandas 3.0.3`，并添加 venv-local `python3.exe` shim 后，`npm test` 全量通过：主仓库 61 个测试通过，并链式运行 Pi extension 15 个测试通过。

未验证：

- 未在真实 Claude Code、Codex、Codex desktop、Copilot CLI、OpenCode、Gemini CLI、Pi 或 OpenClaw 中安装并交互验证。
- 未信任或执行真实 Codex / Claude Code 插件生命周期 hook。
- 未在真实 Codex / Claude Code 宿主中验证 `SubagentStart` 规则注入。
- 未运行 promptfoo API benchmark；README 中的成本、延迟和代码行数结论只记录为 upstream 自述和 benchmark 文档结论。
- 未验证 `PONYTAIL_DEFAULT_MODE` 和用户级 config 在真实宿主中的持久化交互。

## 下一步

1. 用临时插件数据目录和临时 Claude / Codex 配置目录验证 hook 输出 JSON、flag 文件和 mode 切换。
2. 在测试用 Codex profile 中安装插件，打开 `/hooks` 审核并信任两个生命周期 hook。
3. 在真实宿主中验证 `SubagentStart` 是否给子代理注入同一规则集。
4. 使用最小 API key 预算复现一轮 `benchmarks/promptfooconfig.yaml`，只把可复现结果写入 evidence。

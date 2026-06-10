# Caveman

Caveman 是面向 AI 编码助手的输出压缩 skill / plugin。它通过一组提示词规则、安装器、hooks、状态栏和辅助工具，让 Claude Code、Codex、Gemini CLI、Cursor、Windsurf、Cline、Copilot 等 Agent 以更短的回复表达同等技术信息。

## 收录信息

| 字段 | 值 |
|---|---|
| 项目名称 | Caveman |
| 项目 ID | `JuliusBrussee__caveman` |
| GitHub | https://github.com/JuliusBrussee/caveman |
| 项目主页 | https://getcaveman.dev/ |
| 主分类 | `agentic-coding` |
| 辅助标签 | `prompt-engineering`、`skills`、`claude-code`、`codex`、`mcp-tools`、`token-optimization` |
| 收录等级 | Level B 标准收录 |
| 当前状态 | `analyzing` |
| 默认分支 | `main` |
| 收录快照 | 2026-06-11 |
| 分析 Commit | `655b7d9c5431f822264b7732e9901c5578ac84cf` |
| 是否本机运行验证 | 否 |

## 为什么收录

- 与 AI Agent 明确相关：README 把项目定位为 Claude Code skill/plugin，并列出 Codex、Gemini、Cursor、Windsurf、Cline、Copilot 等多 Agent 接入方式。
- 学习价值明确：可用于理解 Agent 回复风格约束、skill 分发、插件安装、hooks、状态栏、token 统计、记忆压缩和 MCP tool description 压缩。
- 工程参考价值明确：仓库包含统一 Node 安装器、shell / PowerShell shim、Claude Code hooks、Codex / Gemini command stubs、OpenCode plugin、MCP proxy、测试和 benchmark / eval 目录。
- 适合生成图解和学习任务：可以拆成安装路径图、hook 激活图、skill 规则图、MCP shrink 图和压缩验证流程图。

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
- GitHub API 显示默认分支为 `main`、主要语言为 JavaScript、License 为 MIT，homepage 为 `https://getcaveman.dev/`。
- `git ls-remote --symref` 显示 HEAD 指向 `refs/heads/main`，当前 HEAD 为 `655b7d9c5431f822264b7732e9901c5578ac84cf`。
- README / INSTALL.md 描述了统一安装器、per-agent 安装、`/caveman` 模式、`caveman-compress`、`caveman-stats`、`caveman-shrink` 和 cavecrew 子 Agent。
- GitHub tree 显示仓库包含 `bin/install.js`、`skills/`、`src/hooks/`、`src/mcp-servers/caveman-shrink/`、`plugins/caveman/`、`tests/`、`benchmarks/` 和 `evals/`。

未验证：

- 未执行 `install.sh`、`install.ps1` 或 `node bin/install.js`，因此未验证本机安装写入范围。
- 未执行 `npx skills add JuliusBrussee/caveman -a codex`。
- 未源码级确认 installer、Claude Code hooks、OpenCode plugin、MCP shrink、token stats 和 compress scripts 的完整调用链。
- 未运行 Node / Python 测试和 benchmark / eval。

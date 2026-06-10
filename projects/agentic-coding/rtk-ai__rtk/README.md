# RTK

RTK, or Rust Token Killer, is a Rust CLI proxy for AI coding workflows. It rewrites common development commands to `rtk` equivalents and filters command output before it enters an LLM context.

## 收录信息

| 字段 | 值 |
|---|---|
| 项目名称 | RTK |
| 项目 ID | `rtk-ai__rtk` |
| GitHub | https://github.com/rtk-ai/rtk |
| 项目主页 | https://www.rtk-ai.app |
| 主分类 | `agentic-coding` |
| 辅助标签 | `token-optimization`、`cli-proxy`、`command-output-filtering`、`hooks`、`codex`、`claude-code` |
| 收录等级 | Level B 标准收录 |
| 当前状态 | `analyzing` |
| 默认分支 | `develop` |
| 收录快照 | 2026-06-11 |
| 分析 Commit | `6785a6c7695d7273e722214a295249a84819b6f0` |
| 是否本机运行验证 | 否 |

## 为什么收录

- 与 AI 编码 Agent 明确相关：README 和 hooks 文档说明它支持 Claude Code、Codex、Cursor、Gemini CLI、OpenCode、Hermes、Copilot 等 AI coding tools。
- 学习价值明确：适合学习命令输出压缩、hook 命令重写、Agent 权限边界、上下文成本观测和开发工具链集成。
- 工程参考价值高：源码包含 Rust CLI、命令路由、生态级过滤模块、rewrite registry、hook installer、tracking SQLite、tee raw-output recovery 和 telemetry consent 文档。
- 与现有 AgentDive 样例互补：它更偏“上下文输入成本治理”和“命令输出压缩”，可与 Caveman 的输出风格压缩、Graphify 的代码图谱上下文治理对比学习。

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
- GitHub API 显示默认分支为 `develop`、主要语言为 Rust、License 为 Apache-2.0，homepage 为 `https://www.rtk-ai.app`。
- `git ls-remote --symref` 显示 HEAD 指向 `refs/heads/develop`，当前 HEAD 为 `6785a6c7695d7273e722214a295249a84819b6f0`。
- README 描述了 CLI proxy、command filtering、auto-rewrite hook、analytics、tee raw-output recovery、telemetry opt-in 和多 Agent 支持。
- 临时浅克隆读取了 `Cargo.toml`、`src/main.rs`、`src/hooks/`、`src/discover/registry.rs`、`src/core/`、`hooks/`、`docs/contributing/ARCHITECTURE.md` 和相关 README。

未验证：

- 未在本机安装 `rtk`。
- 未运行 `rtk init`、`rtk rewrite`、`rtk gain` 或任何真实过滤命令。
- 未验证 hook 对 Claude Code / Codex / Gemini / Cursor 等目标 Agent 的真实写入和运行效果。
- 未复现 README 中 60-90% token savings 统计。
- 未执行 Rust 测试套件、安装脚本或 release binary。

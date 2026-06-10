# Caveman 收录报告

## 1. 基本信息

- GitHub 地址：https://github.com/JuliusBrussee/caveman
- 收录时间：2026-06-11
- 项目名称：Caveman
- 项目 ID：`JuliusBrussee__caveman`
- 项目分类：`agentic-coding`
- 收录等级：Level B 标准收录
- 当前状态：`analyzing`
- 是否建议收录：是
- 收录人 / Agent：Codex

## 2. 收录依据

- 与 AI Agent 的相关性：README 明确定位为 Claude Code skill/plugin，并列出 Codex、Gemini、Cursor、Windsurf、Cline、Copilot 等 Agent 支持。
- 项目学习价值：覆盖 prompt compression、AI coding assistant skill、插件分发、Claude Code hooks、statusline、token stats、memory compression、MCP metadata compression 和 subagents。
- 工程参考价值：可作为“如何把一套 Agent 行为规则跨平台分发并保持安装 / 卸载 / dry-run 边界”的工程样例。
- 文档和源码可分析性：仓库包含 README、INSTALL.md、CLAUDE.md、`bin/`、`skills/`、`src/hooks/`、`src/mcp-servers/`、`plugins/`、`tests/`、`benchmarks/` 和 `evals/`。
- License 初步判断：GitHub API 显示 MIT License。
- 是否重复收录：收录前重复检查未发现 `JuliusBrussee__caveman` 或 Caveman 既有条目。

## 3. 风险

- 运行风险：尚未本机执行安装器；one-liner 或 `--all` 可能写多个用户级 Agent 配置。
- 维护风险：支持的 Agent 平台和安装命令较多，INSTALL.md 与源码 provider matrix 需要同步验证。
- 安全风险：`caveman-compress` 会处理用户指定记忆文件，并可能通过 Anthropic SDK 或 Claude CLI 处理内容；安装器和 hooks 涉及用户配置写入。
- 文档过期风险：当前资料基于 2026-06-11 快照和 commit `655b7d9c5431f822264b7732e9901c5578ac84cf`。
- 结论待验证项：installer provider detection、dry-run 无写入保证、Codex 安装路径、Claude hooks、MCP shrink 透传语义、stats 统计口径、benchmark 复现。

## 4. 生成文件清单

- [x] `projects/agentic-coding/JuliusBrussee__caveman/README.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/meta.json`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/project-analysis.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/source-code-reading.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/integration-guide.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/troubleshooting.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/learning-todo-list.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/collect-report.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/assets/diagrams/`
- [x] `learning-notes/JuliusBrussee__caveman/`
- [x] `PROJECTS.md` 更新
- [x] `LEARNING_PROGRESS.md` 更新

## 5. 待人工确认事项

- [ ] License 是否满足目标发布和引用方式。
- [ ] `node bin/install.js --dry-run --all` 是否完全无写入。
- [ ] Codex 单 Agent 安装是否只影响预期配置。
- [ ] Claude Code hooks、statusline 和 mode flag 是否按文档工作。
- [ ] `caveman-shrink` 是否只压缩预期 metadata 字段。
- [ ] `caveman-compress` 的备份、路径、大小和 API / CLI fallback 是否符合安全预期。
- [ ] benchmark / eval 是否可复现，统计口径是否适合本仓库学习。

## 6. 下一步建议

1. 在临时克隆中执行 `node bin/install.js --list` 和 `node bin/install.js --dry-run --all`。
2. 阅读 `bin/install.js`、`src/hooks/*.js`、`src/mcp-servers/caveman-shrink/*.js` 和 `skills/caveman-compress/scripts/*.py`。
3. 用测试 Agent 或隔离配置目录做单路径安装和卸载验证。
4. 用测试 MCP server 与无敏感 memory file 验证 `caveman-shrink` 和 `caveman-compress`。
5. 复现一组 benchmark / eval 后，再决定是否提升为 Level A 深度收录。

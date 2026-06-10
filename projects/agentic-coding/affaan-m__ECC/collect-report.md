# ECC 收录报告

## 1. 基本信息

- GitHub 地址：https://github.com/affaan-m/ECC
- 收录时间：2026-06-11
- 项目名称：ECC
- 项目 ID：`affaan-m__ECC`
- 项目分类：`agentic-coding`
- 收录等级：Level A 深度收录
- 当前状态：`analyzing`
- 是否建议收录：是
- 收录人 / Agent：Codex

## 2. 收录依据

- 与 AI Agent 的相关性：明确相关。项目描述、README、`package.json` 和 plugin manifest 都围绕 Claude Code、Codex、OpenCode、Cursor、Gemini 等 AI coding harness。
- 项目学习价值：高。覆盖 skills、agents、commands、hooks、rules、MCP、install manifests、session adapters、worktree lifecycle、operator dashboard、security gates 等主题。
- 工程参考价值：高。包含 CLI、selective installer、hook runtime、plugin manifests、OpenCode adapter、Codex config、tests 和 CI validators。
- 文档和源码可分析性：高。README、中文 README、多语言 docs、architecture docs、release notes、源码和测试目录齐全。
- License 初步判断：MIT。
- 是否重复收录：收录前未发现 `PROJECTS.md` 或仓库内已有 `affaan-m/ECC`。

## 3. 风险

- 运行风险：未安装、未执行 CLI、未验证 plugin 和 hook 行为。
- 维护风险：项目能力面很广，manifest、plugin、catalog、README 的数量和术语可能漂移。
- 安全风险：hooks、MCP 配置、installer 和 operator tools 涉及本机文件、命令、配置和可能的全局写入，需要严格审计。
- 文档过期风险：README、release notes、plugin manifest 可能不在同一生成点。
- 结论待验证项：Codex plugin 加载、Claude hook 触发、OpenCode event adapter、Windows installer、Node 版本兼容、catalog/test 状态。

## 4. 生成文件清单

- [x] `projects/agentic-coding/affaan-m__ECC/README.md`
- [x] `projects/agentic-coding/affaan-m__ECC/meta.json`
- [x] `projects/agentic-coding/affaan-m__ECC/project-analysis.md`
- [x] `projects/agentic-coding/affaan-m__ECC/source-code-reading.md`
- [x] `projects/agentic-coding/affaan-m__ECC/integration-guide.md`
- [x] `projects/agentic-coding/affaan-m__ECC/troubleshooting.md`
- [x] `projects/agentic-coding/affaan-m__ECC/learning-todo-list.md`
- [x] `projects/agentic-coding/affaan-m__ECC/collect-report.md`
- [x] `projects/agentic-coding/affaan-m__ECC/assets/diagrams/`
- [x] `learning-notes/affaan-m__ECC/`
- [x] `PROJECTS.md` 更新
- [x] `LEARNING_PROGRESS.md` 更新

## 5. 已验证内容

- GitHub API 显示仓库公开、默认分支 `main`、主要语言 JavaScript、License MIT。
- GitHub API 显示 Star 212486、Fork 32632、`open_issues_count` 为 60；GitHub Search API 拆分为 open issues 20、open PRs 40。topics 包含 `ai-agents`、`claude-code`、`developer-tools`、`llm`、`mcp`、`productivity`。
- `git ls-remote --symref` 显示 HEAD 指向 `refs/heads/main`，commit 为 `c888d2b73f26d605ff6c172b433d4cad2200206f`。
- GitHub languages API 显示 JavaScript、Rust、Python、Shell、TypeScript、Swift、CSS、PowerShell。
- README 描述 ECC v2.0.0 为 cross-harness agent workflow / operator system，覆盖 Codex、Claude Code、Cursor、OpenCode、Gemini、Zed、GitHub Copilot 等。
- `package.json` 显示 npm 包 `ecc-universal`、版本 `2.0.0`、bin `ecc` / `ecc-control-pane` / `ecc-install`、Node `>=18`。
- npm 元数据复核显示 `ecc-universal@2.0.0` 暴露 `ecc` bin，同时存在独立 `ecc@0.0.2` 包；后续验证命令应避免直接写 `npx ecc ...`。
- `docs/architecture/cross-harness.md` 说明共享 workflow source 和 harness adapter 的边界。
- `hooks/hooks.json` 包含 PreToolUse、PreCompact、SessionStart、PostToolUse、Stop、SessionEnd。
- 首轮源码检查确认 `scripts/ecc.js`、`scripts/install-plan.js`、`scripts/install-apply.js`、`scripts/lib/install-manifests.js`、`scripts/lib/install-executor.js`、`scripts/control-pane.js` 等入口存在。

## 6. 未验证内容

- 未 clone 完整源码到本仓库缓存。
- 未执行 `npx --package ecc-universal ecc ...`、本地 `node scripts/ecc.js ...`、`ecc plan`、`ecc install`、`ecc doctor`。
- 未执行 `npm test` 或 catalog/hook/manifest validators。
- 未安装 Claude plugin、Codex plugin、OpenCode package 或 Cursor adapter。
- 未验证 hook 实际触发、阻断和 timeout 行为。
- 未验证 Codex MCP/skills/plugin 是否真实加载。
- 未验证 control pane、session adapters、state store、worktree lifecycle。

## 7. 待人工确认事项

- [ ] License 是否满足 AgentDive 引用和学习整理策略。
- [ ] Level A 深度收录是否符合当前学习优先级。
- [ ] 是否允许在隔离环境真实安装 ECC minimal profile。
- [ ] 是否把 Codex 路径作为优先验证对象。
- [ ] 是否需要和现有本地 AGENTS / skills / governance 工具做专项对比。

## 8. 下一步建议

后续行动：先做只读验证。执行 `npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json` 和 `npx --yes --package ecc-universal ecc consult "tdd code review security" --target codex`，记录输出和写入范围。只有 dry-run 结果可接受后，再在临时环境验证 Codex minimal profile 和 Claude plugin hook 行为。

## 9. 信息快照

- 快照日期：2026-06-11
- GitHub API：https://api.github.com/repos/affaan-m/ECC
- README：https://raw.githubusercontent.com/affaan-m/ECC/main/README.md
- GitHub 页面：https://github.com/affaan-m/ECC
- Cross-harness architecture：https://raw.githubusercontent.com/affaan-m/ECC/main/docs/architecture/cross-harness.md
- Release notes：https://raw.githubusercontent.com/affaan-m/ECC/main/docs/releases/2.0.0/release-notes.md

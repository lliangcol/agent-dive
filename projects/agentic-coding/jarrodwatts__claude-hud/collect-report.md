# Claude HUD 收录报告

## 1. 基本信息

- GitHub 地址：https://github.com/jarrodwatts/claude-hud
- 收录时间：2026-06-11
- 项目名称：Claude HUD
- 项目 ID：`jarrodwatts__claude-hud`
- 项目分类：`agentic-coding`
- 收录等级：Level B 标准收录
- 当前状态：`analyzing`
- 是否建议收录：是
- 收录人 / Agent：Codex

## 2. 收录依据

- 与 AI Agent 的相关性：README 明确描述为 Claude Code plugin，服务 Claude Code 会话状态展示。
- 项目学习价值：覆盖 statusline API、context usage、rate limits、transcript JSONL、tool/agent/todo activity、MCP/Skill 活动和配置治理。
- 工程参考价值：TypeScript ESM、跨平台 setup、配置校验、终端宽度处理、缓存、外部 usage snapshot、Node test suite。
- 文档和源码可分析性：仓库包含 README、中文 README、setup/configure commands、src、dist、tests、plugin manifest 和 package 配置。
- License 初步判断：`package.json` 和 plugin manifest 显示 MIT。
- 是否重复收录：收录前重复检查未发现 `jarrodwatts__claude-hud` 或 `jarrodwatts/claude-hud` 既有条目。

## 3. 风险

- 运行风险：未在真实 Claude Code 中安装 plugin 或执行 setup。
- 配置风险：setup 会修改用户级 `settings.json` 的 `statusLine.command`，可能替换其他 statusline。
- 平台风险：Windows PowerShell、Git Bash/MSYS2、WSL、macOS/Linux 的 command format 差异明显。
- API 风险：GitHub REST API 在收录时被限流，精确 stars/forks 元数据采用 GitHub 页面近似值。
- 测试风险：临时 Windows 浅克隆 `npm test` 失败，不能声明测试通过。
- 漂移风险：Claude Code statusline stdin 和 transcript JSONL schema 可能随 Claude Code 版本变化。

## 4. 生成文件清单

- [x] `projects/agentic-coding/jarrodwatts__claude-hud/README.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/meta.json`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/project-analysis.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/source-code-reading.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/integration-guide.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/troubleshooting.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/learning-todo-list.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/collect-report.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/assets/diagrams/`
- [x] `learning-notes/jarrodwatts__claude-hud/`
- [x] `PROJECTS.md` 更新
- [x] `LEARNING_PROGRESS.md` 更新

## 5. 已验证内容

- GitHub 仓库公开存在。
- GitHub 页面显示 README 定位、stars/forks/issues/PRs 概览。
- raw README 显示安装命令、功能定位、配置选项、usage limits、troubleshooting、requirements 和 development 命令。
- raw `package.json` 显示项目名、版本、Node engine、scripts、license 和 TypeScript 依赖。
- 浅克隆 HEAD：`9650a43600e9bcc94057fbd693a7f05aba4ee1ff`。
- 源码抽样：`.claude-plugin/plugin.json`、`commands/setup.md`、`commands/configure.md`、`src/index.ts`、`src/stdin.ts`、`src/transcript.ts`、`src/config.ts`、`src/render/index.ts`、`src/git.ts`、`src/external-usage.ts`。
- 本地临时测试：`npm ci` 成功；`npm test` 退出码 1。

## 6. 待人工确认事项

- [ ] 使用认证 GitHub API 或后续刷新补齐精确 stars/forks/issues 元数据。
- [ ] 在真实 Claude Code 中执行 marketplace add、install、reload 和 setup。
- [ ] 验证 setup 对已有 statusline 的备份、询问和恢复路径。
- [ ] 验证 Windows PowerShell、Windows Git Bash、WSL、macOS/Linux 的 command format。
- [ ] 采样真实 statusline stdin 和 transcript JSONL。
- [ ] 定位 `npm test` Windows 失败项是否为环境差异或上游回归。
- [ ] 验证 usage/cost 在 subscriber、API-key-only、Bedrock、Vertex 场景下的显示边界。

## 7. 下一步建议

1. 先用临时 `CLAUDE_CONFIG_DIR` 验证 setup 写入和备份逻辑。
2. 在真实 Claude Code 测试 profile 中安装 plugin 并完成一次重启验证。
3. 针对 Windows 测试失败，先单独跑 `tests/core.test.js`、`tests/external-usage.test.js`、`tests/extra-cmd.test.js`、`tests/git.test.js` 和 `tests/integration.test.js`。
4. 采集真实 transcript 后更新 `source-code-reading.md` 的调用链证据。
5. 与 RTK、Caveman、CodeGraph 做一次 agentic-coding 工具层对比：输出压缩、输入压缩、代码图谱、运行期 HUD 分别解决什么问题。


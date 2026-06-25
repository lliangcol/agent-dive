# Ponytail 收录报告

## 1. 基本信息

- GitHub 地址：https://github.com/DietrichGebert/ponytail
- 收录时间：2026-06-25
- 项目名称：Ponytail
- 项目 ID：`DietrichGebert__ponytail`
- 项目分类：`agentic-coding`
- 收录等级：Level B 标准收录
- 当前状态：`analyzing`
- 是否建议收录：是
- 收录人 / Agent：Codex

## 2. 收录依据

- 与 AI Agent 的相关性：项目直接提供 Codex、Claude Code、Copilot CLI、OpenCode、Gemini、Pi、OpenClaw 等宿主的 ruleset、skill、plugin 或 instruction adapter。
- 项目学习价值：适合研究 AI 编码 Agent 的输出约束、过度工程审查、生命周期 hook、模式持久化和跨宿主分发。
- 工程参考价值：仓库包含共享 instruction builder、配置解析、hook runtime、SubagentStart 注入、Windows hook 回归测试、OpenCode plugin、Pi extension、promptfoo benchmark 和 rule-copy 检查。
- 文档和源码可分析性：README、agent portability 文档、examples、benchmarks、tests、skills、hooks、plugin manifests 都可分析。
- License 初步判断：GitHub API、LICENSE 和 manifests 均显示 MIT。
- 是否重复收录：收录前检查未发现 `DietrichGebert__ponytail` 或 `DietrichGebert/ponytail` 既有条目。

## 3. 风险

- 运行风险：未在真实宿主安装或信任 hooks。
- 配置风险：默认模式可由环境变量和用户级 config 控制，团队环境中可能产生隐性行为差异。
- 安全风险：lifecycle hooks 会读取 prompt payload 并写状态文件，接入前必须审查源码和权限。
- 质量风险：Ponytail 的“少写”偏好不能覆盖安全、合规、支付、数据迁移和明确需求中的必要验证。
- benchmark 风险：README 主结论主要是 Claude API 单轮 generation benchmark，不应推广为跨模型或真实多轮 session 成本承诺。
- 版本观察：本轮 `package.json`、Codex / Claude / Copilot plugin manifest 与 release 均为 `4.8.3`；后续仍需留意 release 流程是否持续保持一致。

## 4. 生成文件清单

- [x] `projects/agentic-coding/DietrichGebert__ponytail/README.md`
- [x] `projects/agentic-coding/DietrichGebert__ponytail/meta.json`
- [x] `projects/agentic-coding/DietrichGebert__ponytail/project-analysis.md`
- [x] `projects/agentic-coding/DietrichGebert__ponytail/source-code-reading.md`
- [x] `projects/agentic-coding/DietrichGebert__ponytail/integration-guide.md`
- [x] `projects/agentic-coding/DietrichGebert__ponytail/troubleshooting.md`
- [x] `projects/agentic-coding/DietrichGebert__ponytail/learning-todo-list.md`
- [x] `projects/agentic-coding/DietrichGebert__ponytail/evidence.md`
- [x] `projects/agentic-coding/DietrichGebert__ponytail/collect-report.md`
- [x] `projects/agentic-coding/DietrichGebert__ponytail/assets/diagrams/`
- [x] `learning-notes/DietrichGebert__ponytail/`
- [x] `PROJECTS.md` 更新
- [x] `LEARNING_PROGRESS.md` 更新

## 5. 已验证内容

- GitHub 仓库公开存在。
- 2026-06-25 GitHub API 元数据、默认分支、当时 latest release 和语言统计已获取。
- `git ls-remote` 与临时浅克隆确认收录时 HEAD。
- 已读取 README、AGENTS、agent portability 文档、plugin manifests、hooks、skills、commands、OpenCode plugin、Pi extension、benchmark 和测试文件。
- `node scripts/check-rule-copies.js` 通过。
- 未装 pandas 时 `npm test` 为 60/61，失败项仍是 CSV pandas correctness。
- 临时 venv 安装 `pandas 3.0.3` 并提供 venv-local `python3.exe` shim 后，`npm test` 全量通过：主仓库 61/61，Pi extension 15/15。

## 6. 待人工确认事项

- [ ] 在测试 Codex profile 中安装 Ponytail 并审核 `/hooks`。
- [ ] 在临时 `CLAUDE_CONFIG_DIR` 下验证 Claude Code hook 和 statusline 提示。
- [ ] 复现至少一轮小样本 promptfoo benchmark，并把原始配置与结果链接写入 evidence。
- [ ] 在真实 Codex / Claude Code 宿主中验证 `SubagentStart` 规则注入。
- [ ] 与 Caveman、RTK、Claude HUD 做一次 agentic-coding 工具层对比。

## 7. 下一步建议

1. 先做隔离 hook smoke：不安装到主力 profile，只验证 hook stdout 和 `.ponytail-active`。
2. 选择 Codex 或 Claude Code 做一次真实 plugin install 记录，验证 mode 切换、关闭和 SubagentStart 注入。
3. 复核 benchmark 结论时单独标注 Claude、OpenAI、Gemini 和多轮 session 边界。

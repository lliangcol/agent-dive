# Ruflo 收录报告

## 1. 基本信息

- GitHub 地址：https://github.com/ruvnet/ruflo
- 收录时间：2026-06-11
- 项目名称：Ruflo
- 项目 ID：`ruvnet__ruflo`
- 项目分类：`multi-agent`
- 收录等级：Level A 深度收录
- 当前状态：`analyzing`
- 是否建议收录：是
- 收录人 / Agent：Codex

## 2. 收录依据

- 与 AI Agent 的相关性：明确相关。README 定位为 Claude Code 和 Codex 的 multi-agent AI harness，覆盖 agents、swarm、memory、MCP、hooks、federation 和 Web UI。
- 项目学习价值：高。适合学习多 Agent 协调、MCP stdio、记忆后端、plugin lifecycle、hook 边界、Codex / Claude Code 集成差异。
- 工程参考价值：高。仓库包含 npm packages、CLI、MCP server、domain runtime、plugin marketplace、Web UI、security policy 和 signed witness verification。
- 文档和源码可分析性：较高。README、package metadata、plugin manifests、runtime source、verification docs 均可读取；但完整运行路径仍需后续实测。
- License 初步判断：MIT。
- 是否重复收录：收录前未发现 `PROJECTS.md` 或仓库内已有 `ruvnet/ruflo`。

## 3. 风险

- 运行风险：CLI init 会写入项目 / harness 配置；MCP server 可能拉取 npm 包和 heavy dependencies。
- 维护风险：Ruflo / Claude Flow 命名共存，README、npm 包、plugin manifest 和源码数量可能漂移。
- 安全风险：hooks、MCP tools、memory、Web UI、federation 和 provider config 都涉及本地文件、命令、网络和数据边界。
- 文档过期风险：README 中 agents、commands、plugins、MCP tools 数量需要用实际 tool list / inventory 复核。
- 结论待验证项：CLI help/version、MCP tool list、Claude Code plugin、CLI full init、Codex `.agents` config、hooks、Web UI、witness scripts。

## 4. 生成文件清单

- [x] `projects/multi-agent/ruvnet__ruflo/README.md`
- [x] `projects/multi-agent/ruvnet__ruflo/meta.json`
- [x] `projects/multi-agent/ruvnet__ruflo/project-analysis.md`
- [x] `projects/multi-agent/ruvnet__ruflo/source-code-reading.md`
- [x] `projects/multi-agent/ruvnet__ruflo/integration-guide.md`
- [x] `projects/multi-agent/ruvnet__ruflo/troubleshooting.md`
- [x] `projects/multi-agent/ruvnet__ruflo/learning-todo-list.md`
- [x] `projects/multi-agent/ruvnet__ruflo/collect-report.md`
- [x] `projects/multi-agent/ruvnet__ruflo/assets/diagrams/`
- [x] `learning-notes/ruvnet__ruflo/`
- [x] `PROJECTS.md` 更新
- [x] `LEARNING_PROGRESS.md` 更新

## 5. 待人工确认事项

- [ ] Level A 深度收录是否符合当前学习优先级。
- [ ] 是否优先验证 Codex `.agents` 路径还是 Claude Code plugin 路径。
- [ ] README 中具体数量是否需要跑 inventory / tool list 后再固化。
- [ ] 是否允许在临时项目执行 Ruflo full init。
- [ ] Web UI / mcp-bridge 是否纳入当前阶段学习范围。

## 6. 下一步建议

后续行动：先做只读验证。执行 `npx --yes ruflo@latest --version`、`npx --yes ruflo@latest --help`、`npx --yes ruflo@latest mcp start --help`。如果输出和环境可接受，再在临时项目执行 `init wizard` 并记录写入范围。最后用 MCP client 验证 tool list，并将实际结果回填到集成笔记。

## 7. 本次验证依据

- GitHub 页面：https://github.com/ruvnet/ruflo
- GitHub raw / 临时浅克隆 HEAD：`6a2964ac94e10ca9916da030302686c725638adb`
- npm metadata：`ruflo@3.10.41`、`claude-flow@3.10.41`、`@claude-flow/cli@3.10.41`、`@claude-flow/codex@3.0.0-alpha.12`
- 关键源码：`ruflo/bin/ruflo.js`、`v3/@claude-flow/cli/bin/cli.js`、`v3/@claude-flow/cli/src/commands/index.ts`、`v3/@claude-flow/cli/src/mcp-tools/index.ts`、`v3/src/*`

## 质量检查项

- [x] 没有生成虚假运行结果。
- [x] 没有把 README 复述写成已验证运行结论。
- [x] 收录等级与输出要求匹配。
- [x] 目录 ID 使用 `ruvnet__ruflo`。

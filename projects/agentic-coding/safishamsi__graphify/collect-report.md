# Graphify 收录报告

## 1. 基本信息

- GitHub 地址：https://github.com/safishamsi/graphify
- 收录时间：2026-06-10
- 本次复核时间：2026-06-11
- 项目名称：Graphify
- 项目 ID：`safishamsi__graphify`
- 项目分类：`agentic-coding`
- 收录等级：Level B 标准收录
- 当前状态：`analyzing`
- 是否建议收录：是
- 收录人 / Agent：Codex

## 2. 收录依据

- 与 AI Agent 的相关性：README 明确面向 Claude Code、Codex、OpenCode、Cursor、Gemini CLI 等 AI 编码助手。
- 项目学习价值：覆盖知识图谱、上下文工程、Tree-sitter 静态分析、非代码 semantic extraction、skill 安装、hook、MCP server 等主题。
- 工程参考价值：可作为“编码 Agent 如何查询项目知识图谱”的工程样例。
- 文档和源码可分析性：仓库包含 README、docs、`ARCHITECTURE.md`、`SECURITY.md`、`graphify/`、`tests/` 和 `pyproject.toml`。
- License 初步判断：GitHub API 显示 MIT License。
- 是否重复收录：已存在 `safishamsi__graphify` 条目；本次按已有收录复核和元数据刷新处理，不重复创建目录。
- 2026-06-11 复核：GitHub API 显示默认分支 `v8`、主要语言 Python、License MIT、stars `64743`、forks `6578`、open_issues_count `328`；`git ls-remote --symref` 显示 HEAD 仍为 `5504c84324fc9249eb4c9d0cca86da7140250032`。

## 3. 风险

- 运行风险：尚未本机安装 `graphifyy`，未验证 CLI、extras 和平台安装器。
- 维护风险：项目更新频繁，README、平台列表和参数可能快速变化。
- 安全风险：README 称代码 AST 抽取本地执行，但 docs、PDF、图片 semantic extraction 可能涉及外部模型 / assistant backend；对私有仓库使用前必须确认数据外发边界。
- 文档过期风险：当前正文资料基于 2026-06-10 快照和 commit `5504c84324fc9249eb4c9d0cca86da7140250032`；2026-06-11 仅刷新公开 GitHub 元数据，未重新做源码级分析。
- 结论待验证项：CLI 调用链、Codex hook 写入行为、MCP server 工具协议、Tree-sitter 抽取细节、缓存和 ignore 规则。

## 4. 生成文件清单

- [x] `projects/agentic-coding/safishamsi__graphify/README.md`
- [x] `projects/agentic-coding/safishamsi__graphify/meta.json`
- [x] `projects/agentic-coding/safishamsi__graphify/project-analysis.md`
- [x] `projects/agentic-coding/safishamsi__graphify/source-code-reading.md`
- [x] `projects/agentic-coding/safishamsi__graphify/integration-guide.md`
- [x] `projects/agentic-coding/safishamsi__graphify/troubleshooting.md`
- [x] `projects/agentic-coding/safishamsi__graphify/learning-todo-list.md`
- [x] `projects/agentic-coding/safishamsi__graphify/collect-report.md`
- [x] `projects/agentic-coding/safishamsi__graphify/assets/diagrams/`
- [x] `learning-notes/safishamsi__graphify/`
- [x] `PROJECTS.md` 更新
- [x] `LEARNING_PROGRESS.md` 更新

## 5. 待人工确认事项

- [ ] License 是否满足目标发布和引用方式。
- [ ] `graphify .` 是否能在本机测试仓库跑通。
- [ ] `graphify install --project --platform codex` 的写入范围是否符合预期。
- [ ] 核心调用链是否与源码一致。
- [ ] 图解是否与源码和运行结果一致。
- [ ] 是否应在后续提升为 Level A 深度收录。

## 6. 下一步建议

1. 用公开小仓库完成 `graphify .` 最小运行验证。
2. 阅读 `ARCHITECTURE.md`、`SECURITY.md` 和 `docs/how-it-works.md`，补齐安全和架构边界。
3. 沿 `graphify.__main__:main` 和 `graphify.serve:_main` 做源码级调用链验证。
4. 验证 Codex project install 的实际写入文件，再决定是否把状态推进到 `study-ready`。

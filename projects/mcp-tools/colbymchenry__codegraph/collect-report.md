# CodeGraph 收录报告

## 1. 基本信息

- GitHub 地址：https://github.com/colbymchenry/codegraph
- 收录时间：2026-06-10
- 项目名称：CodeGraph
- 项目 ID：`colbymchenry__codegraph`
- 项目分类：`mcp-tools`
- 收录等级：Level A 深度收录
- 当前状态：`analyzing`
- 是否建议收录：是
- 收录人 / Agent：Codex

## 2. 收录依据

- 与 AI Agent 的相关性：明确相关。项目通过 MCP Server 服务 Claude Code、Codex CLI、Cursor、opencode、Hermes Agent、Gemini CLI、Antigravity IDE 和 Kiro。
- 项目学习价值：高。覆盖 MCP tools、代码知识图谱、tree-sitter、SQLite FTS5、引用解析、影响面分析和 Agent tool guidance。
- 工程参考价值：高。源码有 CLI、installer、MCP、extraction、resolution、graph、sync、tests 等完整工程模块。
- 文档和源码可分析性：高。README、docs site、tests 和 TypeScript 源码齐全。
- License 初步判断：MIT。
- 是否重复收录：收录前未发现 `PROJECTS.md` 中已有该项目。

## 3. 风险

- 运行风险：未安装、未跑通 CLI、未验证 MCP server。
- 维护风险：语言/框架覆盖面很广，后续精度和兼容性维护成本高。
- 安全风险：MCP tools 可返回源码片段，企业使用时需要权限和审计。
- 文档过期风险：site docs 的 MCP Server 页和当前 README/源码在 instructions 写入方式上存在表述差异。
- 结论待验证项：README benchmark、本机索引耗时、Windows 安装器、Agent 实际调用体验、测试套件状态。

## 4. 生成文件清单

- [x] `projects/mcp-tools/colbymchenry__codegraph/README.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/project-analysis.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/source-code-reading.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/integration-guide.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/troubleshooting.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/learning-todo-list.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/collect-report.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/assets/diagrams/`
- [x] `learning-notes/colbymchenry__codegraph/`
- [x] `PROJECTS.md` 更新
- [x] `LEARNING_PROGRESS.md` 更新

## 5. 已验证内容

- GitHub API 显示默认分支为 `main`，主要语言 TypeScript，License 为 MIT。
- GitHub API 和浅克隆 commit 一致：`16c73e2b0e027411e22039baeb32fbe60ab42b4c`。
- `package.json` 显示 npm 包名 `@colbymchenry/codegraph`、CLI bin `codegraph`、测试命令 `vitest run`。
- 源码包含 CLI、MCP、installer、extraction、resolution、graph、sync、db、tests 等模块。
- README 与源码均显示新版工具指导由 MCP initialize response 提供，不再依赖写入 `CLAUDE.md` / `AGENTS.md`。

## 6. 未验证内容

- 未执行安装器。
- 未执行 `codegraph init -i`。
- 未运行 `npm test`。
- 未实际启动 `codegraph serve --mcp`。
- 未验证 README benchmark。
- 未确认每种语言和框架 resolver 的准确率。

## 7. 待人工确认事项

- [ ] License 是否满足本仓库引用和学习整理策略。
- [ ] Level A 收录是否符合维护优先级。
- [ ] 是否要补充和 `codebase-memory-mcp` 的对比分析。
- [ ] 是否在本机真实安装并用于一个样例仓库。
- [ ] 是否把 README benchmark 作为后续复现实验。

## 8. 下一步建议

后续行动：优先跑通最小闭环。选择一个公开中型 TypeScript 仓库，执行 `codegraph init -i`、`codegraph status`、`codegraph query`、`codegraph impact`，再在 Codex 或 Claude Code 中验证 MCP tools 返回是否符合 README 描述。

## 9. 信息快照

- 快照日期：2026-06-10
- GitHub API：https://api.github.com/repos/colbymchenry/codegraph
- README：https://raw.githubusercontent.com/colbymchenry/codegraph/main/README.md
- GitHub 页面：https://github.com/colbymchenry/codegraph
- 官方文档：https://colbymchenry.github.io/codegraph/

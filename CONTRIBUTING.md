# Contributing

欢迎为 AgentDive 贡献项目精读、模板、图解、学习路线和问题修正。

## 开始之前

- 阅读 [README.md](README.md)、[USAGE.md](USAGE.md) 和 [START_HERE.md](START_HERE.md)，确认仓库定位和当前状态。
- 了解 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)、[SECURITY.md](SECURITY.md) 和 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
- 从 `main` 创建主题分支，不直接在主分支提交工作。

## 基本原则

- 使用简体中文。
- Markdown 风格保持清晰、克制，适合 GitHub 阅读。
- 不提交账号、密钥、本机绝对路径或私有配置。
- 不伪造运行结果、源码结论、项目状态或收录结果。
- 结论应可追溯到项目 README、官方文档、源码、运行结果或明确的人工判断。
- 主分支名称统一使用 `main`。

## 本地检查

本仓库当前不需要安装第三方依赖。修改项目资料、学习笔记、模板或索引后运行：

```bash
python scripts/check-agent-dive.py
```

如果改动了 Python 脚本，也建议运行：

```bash
python -m compileall scripts
```

## 项目收录规范

新增项目时使用稳定项目 ID：`owner__repo`。

推荐路径：

```text
projects/<category>/<owner__repo>/
learning-notes/<owner__repo>/
```

单次收录只允许修改当前项目目录、对应学习笔记目录、`PROJECTS.md` 和 `LEARNING_PROGRESS.md`。不要改动其他项目目录，不要修改 `docs/` 原始资料。

## 贡献类型

- 项目收录：新增项目精读、图解、Learning Todo List 和收录报告。
- 模板改进：优化 `templates/` 下的通用模板。
- 知识补全：补充 `knowledge/` 下的 AI Agent 工程主题。
- 学习路线：完善 `learning-roadmap/` 的阶段任务和检查问题。
- 图解修正：修正 Mermaid 源文件或导出图中的错误。
- 对比分析：完善 `comparisons/` 下的跨项目对比。

## Issue 规范

- 内容或流程问题请使用 “内容或流程问题” 模板。
- 推荐新项目请使用 “建议收录项目” 模板，并说明学习价值和初步证据。
- 文档澄清请使用 “文档改进” 模板。
- 安全问题按 [SECURITY.md](SECURITY.md) 处理，不要在公开 Issue 中粘贴敏感信息。

## 提交前检查

- [ ] 没有修改 `docs/` 原始资料。
- [ ] 没有写入账号、密钥、本机绝对路径或私有信息。
- [ ] 新增项目使用 `owner__repo` 作为目录 ID。
- [ ] `PROJECTS.md` 与项目目录状态一致。
- [ ] `LEARNING_PROGRESS.md` 只记录总览，不承载完整项目分析。
- [ ] 图解结论与正文一致，推测内容已经标注。
- [ ] 文档中没有虚假的运行验证或自动化能力声明。
- [ ] 已运行 `python scripts/check-agent-dive.py`。

## 分支与 Pull Request

- 从 `main` 创建主题分支。
- PR 标题说明变更类型和影响范围。
- PR 描述中列出新增文件、修改文件、验证方式和未完成事项。
- 如声明运行、测试或源码验证，PR 必须指向对应 `evidence.md` 中的证据。
- 如提升项目状态到 `study-ready`、`in-study` 或 `completed`，必须同步更新项目目录、学习笔记、`PROJECTS.md` 和 `LEARNING_PROGRESS.md`。

提交 PR 即表示你同意自己的贡献按本仓库 [LICENSE](LICENSE) 授权，并确认没有引入未授权第三方内容。

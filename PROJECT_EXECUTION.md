# 项目执行说明

本文档说明 AgentDive 第一版仓库骨架的执行和维护方式。

## 当前阶段

当前仓库处于首批样例和质量治理建设阶段。核心交付是文档、模板、目录结构、学习路线、收录流程说明、首轮项目精读样例、证据文件和轻量一致性检查。不包含复杂 Web 系统、后端服务或真实 GitHub API 自动收录程序。

## 执行原则

- 保留 `docs/` 下的原始需求资料和交付物。
- 新增公开文档时不写入本机绝对路径、账号、密钥或私有信息。
- 不生成虚假的项目收录结果。
- 不把缺少证据的项目标记为已跑通、`study-ready` 或 `completed`。
- 每个项目使用 `owner__repo` 作为隔离 ID。
- 单个项目的分析资料、学习笔记和图解必须放在各自项目目录下。
- 每个项目必须有 `meta.json`、`evidence.md` 和 `learning-notes/<owner__repo>/progress.json`。

## 推荐维护流程

1. 根据 `scripts/collect-project.md` 判断项目是否适合收录。
2. 为项目确定分类、收录等级和目录 ID。
3. 在 `projects/<category>/<owner__repo>/` 下生成项目分析资料。
4. 在 `learning-notes/<owner__repo>/` 下生成学习笔记。
5. 更新 `PROJECTS.md` 和 `LEARNING_PROGRESS.md`。
6. 更新项目 `meta.json`、`evidence.md` 和学习 `progress.json`。
7. 运行 `python scripts/check-agent-dive.py`。
8. 使用模板中的质量检查项做自检。

## 与需求文档的关系

`docs/` 是需求来源和原始资料区，不作为日常编辑区。后续若需求和仓库实现出现冲突，应优先更新仓库根目录的公开规范，并在变更说明中记录原因。

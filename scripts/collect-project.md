# 项目收录流程规范

本文档定义 AI Agent 收到以下指令时的标准处理流程：

```text
收录：https://github.com/<owner>/<repo>
```

当前文件是流程规范，不是可运行脚本。

## 核心约定

- 项目目录 ID：`owner__repo`。
- 项目资料目录：`projects/<category>/<owner__repo>/`。
- 学习笔记目录：`learning-notes/<owner__repo>/`。
- 第三方源码缓存：`.cache/sources/<owner__repo>/`。
- 运行缓存：`.cache/runs/<owner__repo>/`。
- 项目元数据：`projects/<category>/<owner__repo>/meta.json`。
- 项目证据文件：`projects/<category>/<owner__repo>/evidence.md`。
- 学习进度文件：`learning-notes/<owner__repo>/progress.json`。

## 写入白名单

单次收录只允许写入：

- `projects/<category>/<owner__repo>/`
- `learning-notes/<owner__repo>/`
- `PROJECTS.md`
- `LEARNING_PROGRESS.md`

不得修改：

- `docs/` 原始资料
- 其他项目目录
- 其他项目学习笔记
- 本地私有配置和密钥文件

## 标准流程

1. 解析 GitHub URL。
2. 获取项目信息。
3. 判断是否 AI Agent 相关。
4. 判断收录等级。
5. 创建项目目录。
6. 生成项目分析文档。
7. 生成图解文件。
8. 生成 Learning Todo List。
9. 生成 `learning-notes/<owner__repo>/`。
10. 生成或更新 `meta.json`。
11. 生成或更新 `evidence.md`。
12. 更新 `PROJECTS.md`。
13. 更新 `LEARNING_PROGRESS.md`。
14. 运行 `python scripts/check-agent-dive.py`。
15. 输出收录报告。

## 收录前置判断

- [ ] 是否与 AI Agent 明确相关。
- [ ] 是否有 README 或官方文档。
- [ ] 是否有可分析源码。
- [ ] 是否有 examples、docs 或使用说明。
- [ ] License 是否允许学习整理和引用。
- [ ] 是否已经重复收录。
- [ ] 是否具备学习价值。
- [ ] 是否具备工程参考价值。
- [ ] 是否可以生成 Learning Todo List。
- [ ] 是否可以生成至少一张有效图解。
- [ ] 是否可以记录明确 evidence，区分 `pass`、`fail`、`partial`、`not_run` 和 `blocked`。

## 收录等级

| 等级 | 名称 | 适用对象 | 输出要求 |
|---|---|---|---|
| Level A | 深度收录 | 核心重点项目 | 完整文档、源码拆解、图解、集成、排查、学习笔记、评价 |
| Level B | 标准收录 | 普通优秀项目 | 概览、快速开始、核心原理、基础图解、学习任务、简要评价 |
| Level C | 轻量收录 | 观察项目 | 项目简介、推荐理由、分类标签、后续分析建议 |
| Level D | 暂不收录 | 不符合要求项目 | 不收录原因、风险说明、替代项目建议 |

## 项目状态

| 状态 | 含义 |
|---|---|
| `candidate` | 候选项目 |
| `triaging` | 正在评估 |
| `accepted` | 已通过收录评估 |
| `analyzing` | 正在分析 |
| `documented` | 文档已生成 |
| `diagrammed` | 图解已生成 |
| `study-ready` | 学习资料已就绪 |
| `in-study` | 正在学习 |
| `completed` | 学习完成 |
| `archived` | 归档或停止维护 |

## 输出要求

收录完成后必须输出：

- 收录结论。
- 收录等级和分类。
- 生成文件清单。
- 已验证内容。
- 未验证内容。
- 风险和待人工确认事项。
- `python scripts/check-agent-dive.py` 的结果。

## 证据要求

- GitHub 元数据、源码 commit、运行命令、测试命令、输出摘要和失败原因都写入 `evidence.md`。
- 未执行的命令写 `not_run`，被环境或权限挡住的任务写 `blocked`。
- 只有 `evidence.md` 中存在真实通过记录时，才能把项目标记为已跑通。
- 不复制大段第三方 README、源码或日志。

## 质量门禁

- [ ] 没有生成虚假的项目运行结果。
- [ ] 没有把未验证结论写成事实。
- [ ] 没有写入密钥、账号、本机绝对路径或私有信息。
- [ ] `PROJECTS.md` 与项目目录状态一致。
- [ ] `LEARNING_PROGRESS.md` 只记录总览。
- [ ] 图解有来源依据或明确标注推测边界。
- [ ] `meta.json`、`evidence.md`、`progress.json` 与索引状态一致。
- [ ] `python scripts/check-agent-dive.py` 通过。

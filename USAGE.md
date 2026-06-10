# AgentDive 使用指南

本文档是 AgentDive 的统一入口。首次使用、继续学习、收录新项目、维护资料或让 AI Agent 接手任务时，先从这里开始。

## 先确认当前边界

AgentDive 当前是 AI Agent 开源项目精读与学习资料仓库，不是 Awesome List，也不是已经自动化完成的收录平台。

当前仓库已经收录首批项目，并生成了项目分析、图解、Learning Todo List 和学习笔记骨架；但多数项目仍处于 `analyzing` 状态。除非项目目录下的 `evidence.md` 明确记录真实运行、测试或源码验证证据，否则不要把“已有文档”理解为“已经跑通”或 `study-ready`。

当前没有真实自动化收录程序。`scripts/collect-project.md` 和 `scripts/collect-project-usage.md` 是人工或 AI Agent 辅助收录的流程规范。

## 你是哪类使用者

### 学习者

目标：按项目学习 AI Agent 工程能力，从会用走向能拆解、能集成、能排查。

建议流程：

1. 打开 [PROJECTS.md](PROJECTS.md)，选择一个项目。
2. 优先选择 `CodeGraph` 作为起点；它已有最小运行证据，但仍需继续补齐源码和学习闭环。
3. 打开项目目录：`projects/<category>/<owner__repo>/`。
4. 先读项目 `README.md` 和 `project-analysis.md`。
5. 打开 `learning-todo-list.md`，从第一个未完成任务开始。
6. 执行任务后，把运行命令、源码依据、测试结果或失败原因写入项目 `evidence.md`。
7. 同步更新 `learning-notes/<owner__repo>/` 下的笔记和 `progress.json`。

不要因为读过 README、复制过示例或生成过分析文档，就把任务标记为已跑通。

### 维护者

目标：维护仓库资料质量，新增或更新项目收录，保持索引、证据和进度一致。

建议流程：

1. 新收录项目前先读 [scripts/collect-project.md](scripts/collect-project.md)。
2. 如需完整说明和示例，读 [scripts/collect-project-usage.md](scripts/collect-project-usage.md)。
3. 确认项目是否与 AI Agent 明确相关，是否有 README、源码、文档、License 和学习价值。
4. 确定分类、收录等级和目录 ID：`owner__repo`。
5. 只写入当前项目目录、对应学习笔记目录、[PROJECTS.md](PROJECTS.md) 和 [LEARNING_PROGRESS.md](LEARNING_PROGRESS.md)。
6. 每次新增或更新后运行质量检查。

```bash
python scripts/check-agent-dive.py
```

校验通过前，不要把项目状态提升为 `study-ready`、`in-study` 或 `completed`。

### AI Agent

目标：让 AI Agent 按固定协议连续推进学习或收录，同时不越权、不伪造结果。

学习任务推荐提示词：

```text
继续学习 <project_id>，从 learning-todo-list.md 中下一个未完成且未阻塞的任务开始。执行前读取 progress.json 和 evidence.md；执行后更新学习笔记、evidence.md 和 progress.json。遇到需要密钥、全局配置写入、付费 API、破坏性命令或同一阻塞连续失败 3 次时停止并报告。
```

检查项目能否提升状态的推荐提示词：

```text
检查 <project_id> 是否可以从 analyzing 提升为 study-ready。必须读取 meta.json、evidence.md、learning-todo-list.md 和 progress.json，只接受真实运行或源码验证证据，不接受推测。
```

完整协议见 [LEARN_WITH_AGENT.md](LEARN_WITH_AGENT.md)。

## 收录一个新项目

输入格式：

```text
收录：https://github.com/<owner>/<repo>
```

标准流程摘要：

1. 解析 GitHub URL，确认 `owner`、`repo` 和默认分支。
2. 获取 README、License、主要语言、文档入口和源码结构。
3. 判断是否与 AI Agent 明确相关。
4. 判断分类和收录等级。
5. 检查是否重复收录。
6. 创建 `projects/<category>/<owner__repo>/`。
7. 生成项目分析、源码阅读、集成、排查、学习任务和收录报告。
8. 创建 `learning-notes/<owner__repo>/`。
9. 更新 `PROJECTS.md` 和 `LEARNING_PROGRESS.md`。
10. 运行 `python scripts/check-agent-dive.py`。
11. 输出收录结论、已验证内容、未验证内容和风险。

写入边界：

- 允许写入：`projects/<category>/<owner__repo>/`
- 允许写入：`learning-notes/<owner__repo>/`
- 允许写入：`PROJECTS.md`
- 允许写入：`LEARNING_PROGRESS.md`
- 不要修改：`docs/` 原始资料
- 不要写入：账号、密钥、token、本机私有路径或全局配置

## 目录怎么读

| 路径 | 用途 |
|---|---|
| [README.md](README.md) | 项目简介和简版入口 |
| [START_HERE.md](START_HERE.md) | 学习者、维护者、AI Agent 的快速第一步 |
| [PROJECTS.md](PROJECTS.md) | 已收录项目索引和状态 |
| [LEARNING_PROGRESS.md](LEARNING_PROGRESS.md) | 全局学习进度、阻塞项和下一步 |
| [LEARN_WITH_AGENT.md](LEARN_WITH_AGENT.md) | AI Agent 连续辅助学习协议 |
| [PROJECT_EXECUTION.md](PROJECT_EXECUTION.md) | 仓库执行和维护原则 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 贡献规范 |
| [scripts/collect-project.md](scripts/collect-project.md) | 项目收录流程规范 |
| [scripts/collect-project-usage.md](scripts/collect-project-usage.md) | 项目收录详细使用说明 |
| `projects/` | 按分类存放项目精读资料 |
| `learning-notes/` | 按项目存放学习过程和进度 |
| `learning-roadmap/` | AI Agent 工程学习路线 |
| `knowledge/` | 通用知识主题 |
| `templates/` | 项目分析、源码阅读、集成、排查和收录模板 |
| `comparisons/` | 跨项目和生态对比 |
| `examples/` | 示例工程规划 |
| `assets/` | 公共图解和素材 |
| `docs/` | 原始需求资料和交付物，默认不改动 |

## 状态和证据规则

项目状态：

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

证据规则：

- 运行验证、测试结果、源码调用链和失败原因写入项目 `evidence.md`。
- 未运行的任务写 `not_run`。
- 被环境、权限、账号、密钥或付费服务挡住的任务写 `blocked`。
- 只有 `evidence.md` 有真实通过记录时，才能把项目标记为已跑通。
- 推测内容必须标注为待验证或人工判断。

## 常用命令

质量检查：

```bash
python scripts/check-agent-dive.py
```

查看收录流程：

```text
阅读 scripts/collect-project.md
阅读 scripts/collect-project-usage.md
```

开始学习：

```text
阅读 PROJECTS.md
选择项目
打开 projects/<category>/<owner__repo>/learning-todo-list.md
从第一个未完成任务开始
```

## 完成前自检

提交或宣称资料可用前，至少确认：

- `PROJECTS.md` 的状态和项目目录内容一致。
- `LEARNING_PROGRESS.md` 只记录总览，不承载完整项目分析。
- 项目目录存在 `meta.json`、`evidence.md` 和 `learning-todo-list.md`。
- 学习笔记目录存在 `progress.json`。
- 图解结论有来源依据，推测边界清楚。
- 没有账号、密钥、token、本机私有路径或虚假运行结果。
- `python scripts/check-agent-dive.py` 通过。

## 下一步入口

首次学习：从 [PROJECTS.md](PROJECTS.md) 选择项目。

维护收录：从 [scripts/collect-project-usage.md](scripts/collect-project-usage.md) 开始。

让 AI Agent 接手：先读 [LEARN_WITH_AGENT.md](LEARN_WITH_AGENT.md)，再使用本文档中的推荐提示词。

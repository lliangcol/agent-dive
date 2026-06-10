# Start Here

这是 AgentDive 的快速开始页。完整使用路径、收录流程、证据规则和 AI Agent 接手方式见 [USAGE.md](USAGE.md)。

AgentDive 当前已经收录 8 个高星 AI Agent 相关项目，但这些资料仍处在首轮精读和质量治理阶段。除非项目证据文件明确标记为已通过运行验证，否则不要把项目视为已经完整跑通或 `study-ready`。

## 学习者第一步

1. 先看 [PROJECTS.md](PROJECTS.md)，选择一个项目。
2. 打开对应的 `projects/<category>/<owner__repo>/README.md` 和 `project-analysis.md`，了解项目定位。
3. 打开 `learning-todo-list.md`，从 Level 1 的第一个未完成任务开始。
4. 每完成一个任务，同步更新 `learning-notes/<owner__repo>/` 下的笔记和 `progress.json`。
5. 运行验证、源码验证、测试结果必须写入项目目录下的 `evidence.md`。

推荐从 CodeGraph 开始，因为它是当前默认金样本候选，学习范围较清晰，且适合验证 MCP、代码索引和 Agent 辅助代码理解闭环。

## 维护者第一步

1. 新收录项目前先阅读 [scripts/collect-project.md](scripts/collect-project.md)。
2. 新增或修改项目资料后运行：

```bash
python scripts/check-agent-dive.py
```

3. 校验通过前不要把项目状态提升为 `study-ready`、`in-study` 或 `completed`。
4. 不要继续堆项目数量。优先把 1 个 Level A 项目做成有证据支撑的完整样例。

## AI Agent 第一条指令

推荐提示词：

```text
继续学习 <project_id>，从 learning-todo-list.md 中下一个未完成且未阻塞的任务开始。执行前读取 progress.json 和 evidence.md；执行后更新学习笔记、evidence.md 和 progress.json。遇到需要密钥、全局配置写入、付费 API、破坏性命令或同一阻塞连续失败 3 次时停止并报告。
```

完整协议见 [LEARN_WITH_AGENT.md](LEARN_WITH_AGENT.md)。

## 状态解释

- `analyzing`：资料已生成，但运行、源码或集成证据仍不足。
- `study-ready`：学习任务、笔记骨架、运行证据和关键源码验证都已齐备。
- `in-study`：学习者或 Agent 正在按 TODO 执行。
- `completed`：所有 Level 的学习产出、复习问题和最终评价已完成。

当前默认判断：CodeGraph 已有缓存内最小运行证据，但仍不是 `study-ready` 或 `completed`；其余项目尚未完整跑通，不能作为完成样例引用。

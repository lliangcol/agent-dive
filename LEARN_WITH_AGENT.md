# Learn With Agent

本文档定义 AgentDive 中 AI Agent 辅助学习的连续执行协议。目标是让 Agent 能在不中断的情况下推进学习任务，同时不伪造结果、不越过权限边界。

## 输入

用户给出项目 ID，例如：

```text
继续学习 colbymchenry__codegraph，直到当前 Level 完成或遇到阻塞。
```

Agent 必须读取：

- `PROJECTS.md`
- `LEARNING_PROGRESS.md`
- `projects/<category>/<owner__repo>/learning-todo-list.md`
- `projects/<category>/<owner__repo>/evidence.md`
- `learning-notes/<owner__repo>/progress.json`

## 执行循环

1. 确认项目 ID、分类目录和当前状态。
2. 找到 `learning-todo-list.md` 中第一个未完成任务。
3. 判断任务是否可自动执行。
4. 执行最小安全步骤。
5. 把命令、环境、输出摘要、失败原因和未验证项写入 `evidence.md`。
6. 把理解、结论和疑问写入对应学习笔记。
7. 更新 `progress.json` 的完成数、阻塞项、下一步行动和时间。
8. 继续下一个任务，直到当前 Level 完成或触发停止条件。

## 停止条件

遇到以下任一情况必须停止并报告：

- 需要真实 API Key、账号、付费模型或私有服务。
- 命令会写入用户全局 Agent 配置、shell profile、系统目录或主配置目录。
- 命令可能删除、覆盖、迁移或批量改写非缓存目录。
- 任务要求安装浏览器扩展、IDE 插件或真实 Claude Code plugin，且没有临时配置目录。
- 同一阻塞连续失败 3 次。
- 项目文档与实际命令明显不一致，继续执行会污染证据。

## 证据要求

每次执行都必须记录：

- 日期和本机环境摘要。
- 命令或操作。
- 执行范围，例如 `.cache/sources/<owner__repo>/`。
- 结果：`pass`、`fail`、`partial`、`not_run` 或 `blocked`。
- 输出摘要，不复制大段第三方内容。
- 对学习 TODO 和 progress 的影响。

未运行的任务必须保持未完成，不能因为读过 README 就标记为已跑通。

## 自动执行等级

- `yes`：只读阅读、源码定位、文档整理、无副作用校验。
- `guarded`：在 `.cache/`、临时目录或临时配置中运行，执行前检查命令是否会写入全局状态。
- `manual-confirm`：需要用户明确确认，通常涉及真实安装、插件启用、全局配置、外部账号或付费 API。

## 推荐提示词

```text
继续学习 <project_id>，按 LEARN_WITH_AGENT.md 执行。只处理下一个未完成任务；如果任务可自动执行，就执行、记录 evidence、更新笔记和 progress，然后继续同一 Level 的下一个任务。遇到停止条件立即停下，并说明阻塞原因和建议的下一步。
```

```text
检查 <project_id> 是否可以从 analyzing 提升为 study-ready。必须读取 meta.json、evidence.md、learning-todo-list.md 和 progress.json，只接受真实运行或源码验证证据，不接受推测。
```

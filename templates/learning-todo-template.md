# <Project Name> Learning Todo List

## 使用场景

用于为单个项目生成从了解、跑通、源码理解、集成、改造到总结评价的学习任务。

## 填写说明

- 每个任务必须能被执行或检查，并有明确完成标准。
- 每个任务必须说明证据落点，通常是学习笔记和 `evidence.md`。
- 任务完成后同步更新 `learning-notes/<owner__repo>/progress.json`。
- 涉及安装、全局配置、付费 API、密钥或破坏性命令的任务，`Agent 自动执行` 必须写 `manual-confirm`。

## 标准结构

## Level 1：了解项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `<ID>-L1-01` | Level 1 | 阅读 README 和官方文档 | 项目链接可访问 | 只读阅读 | `01-first-impression.md`、`evidence.md` 来源记录 | 能用一句话说明项目定位、问题和适用场景 | 记录缺失文档或访问失败 | yes |
| [ ] | `<ID>-L1-02` | Level 1 | 记录第一印象和待验证问题 | 已完成 L1-01 | 写入第一印象笔记 | `01-first-impression.md` | 笔记区分已知事实、推测和待验证项 | 标记 blocked 并写明缺口 | yes |

产出：`01-first-impression.md`。

## Level 2：跑通项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `<ID>-L2-01` | Level 2 | 安装或准备隔离运行环境 | 使用 `.cache/` 或临时目录 | 执行官方最小安装或 dry-run | `02-quickstart-notes.md`、`evidence.md` 命令记录 | 记录版本、环境、写入范围和输出摘要 | 失败则记录 exit code、stderr 摘要和下一步 | guarded |
| [ ] | `<ID>-L2-02` | Level 2 | 跑通最小 Demo 或只读等价命令 | L2-01 完成 | 执行最小命令 | `02-quickstart-notes.md`、`evidence.md` | 明确 pass/fail/blocked，不夸大结果 | 需要密钥或付费 API 时停止 | guarded |

产出：`02-quickstart-notes.md`。

## Level 3：理解源码

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `<ID>-L3-01` | Level 3 | 固定源码 commit 并找到入口文件 | 源码可访问 | 只读源码定位 | `04-source-reading-notes.md`、`evidence.md` commit 记录 | 能指向入口文件和主调用链 | 源码缺失时记录替代依据 | yes |
| [ ] | `<ID>-L3-02` | Level 3 | 找到 Agent Loop、工具、Memory/RAG/MCP 或上下文管理模块 | L3-01 完成 | 只读源码分析 | `04-source-reading-notes.md` 和调用链图 | 关键结论有源码路径或推测边界 | 无法验证时保留为 pending | yes |

产出：`04-source-reading-notes.md` 和调用链图。

## Level 4：完成集成

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `<ID>-L4-01` | Level 4 | 在临时项目完成最小集成 | Level 2 有运行证据 | 使用临时配置执行集成 | `05-integration-notes.md`、`evidence.md` | 记录写入范围、权限、回滚路径和结果 | 写入全局配置前停止 | manual-confirm |
| [ ] | `<ID>-L4-02` | Level 4 | 记录集成问题和解决方案 | L4-01 完成或明确 blocked | 整理问题清单 | `05-integration-notes.md`、`06-troubleshooting-notes.md` | 每个问题有复现、原因、处理方式 | 无法复现时标注 pending | yes |

产出：`05-integration-notes.md`。

## Level 5：改造扩展

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `<ID>-L5-01` | Level 5 | 完成一个低风险扩展或改造设计 | Level 4 完成或有替代验证范围 | 在临时分支或沙箱中设计/验证 | `07-reflection.md` 或改造总结、`evidence.md` | 说明改造成本、风险和回滚路径 | 涉及密钥或生产配置时停止 | manual-confirm |
| [ ] | `<ID>-L5-02` | Level 5 | 增加评测、回归或质量检查思路 | L5-01 完成 | 设计最小检查 | 改造总结 | 检查项可复用且边界清楚 | 无法运行时写明原因 | guarded |

产出：改造总结和可复用经验。

## Level 6：总结评价

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `<ID>-L6-01` | Level 6 | 写出项目优缺点、适用场景和不适用场景 | 前序笔记已更新 | 汇总证据和笔记 | `07-reflection.md` | 评价有证据支撑，不把 pending 当事实 | 缺运行证据时明确限制 | yes |
| [ ] | `<ID>-L6-02` | Level 6 | 生成复习问题和同类对比 | L6-01 完成 | 写复习问题 | `review-questions.md` | 问题覆盖使用、源码、集成、风险 | 缺对比样本时标注待补 | yes |

产出：`07-reflection.md` 和 `review-questions.md`。

## 待办检查项

- [ ] 每个 Level 都有任务和产出。
- [ ] 学习任务覆盖使用、源码、集成、改造和总结。
- [ ] 当前完成状态已经同步到学习进度。

## 质量检查项

- [ ] 任务从浅到深。
- [ ] 任务可执行、可检查。
- [ ] 没有把“阅读更多资料”作为唯一任务。
- [ ] 学习产出路径明确。

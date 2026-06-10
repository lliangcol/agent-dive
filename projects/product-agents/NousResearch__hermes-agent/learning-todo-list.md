# Hermes Agent Learning Todo List

本清单已经迁移为可执行任务表。每个任务必须同步更新学习笔记、`evidence.md` 和 `learning-notes/NousResearch__hermes-agent/progress.json`；未验证内容保持未完成。

## Level 1：了解项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [x] | `HERMES-L1-01` | Level 1 | 阅读 README 和官方文档首页。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/01-first-impression.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [x] | `HERMES-L1-02` | Level 1 | 用一句话说明 Hermes Agent 的定位。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/01-first-impression.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [x] | `HERMES-L1-03` | Level 1 | 区分 CLI、gateway、skills、memory、tools、MCP、cron、terminal backends 的职责。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/01-first-impression.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [x] | `HERMES-L1-04` | Level 1 | 记录项目适合学习的主题。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/01-first-impression.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `HERMES-L1-05` | Level 1 | 写一页第一印象笔记。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/01-first-impression.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |

产出：`learning-notes/NousResearch__hermes-agent/01-first-impression.md`。

## Level 2：跑通项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `HERMES-L2-01` | Level 2 | 在隔离环境中按官方说明安装 Hermes。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/02-quickstart-notes.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `HERMES-L2-02` | Level 2 | 执行 `hermes doctor`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `hermes doctor`。 | `learning-notes/NousResearch__hermes-agent/02-quickstart-notes.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `HERMES-L2-03` | Level 2 | 执行 `hermes model` 并选择测试 provider。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `hermes model` 并选择测试 provider。 | `learning-notes/NousResearch__hermes-agent/02-quickstart-notes.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `HERMES-L2-04` | Level 2 | 执行 `hermes tools` 查看默认工具配置。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `hermes tools` 查看默认工具配置。 | `learning-notes/NousResearch__hermes-agent/02-quickstart-notes.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `HERMES-L2-05` | Level 2 | 启动 `hermes` 完成一次普通文本对话。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 启动 `hermes` 完成一次普通文本对话。 | `learning-notes/NousResearch__hermes-agent/02-quickstart-notes.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `HERMES-L2-06` | Level 2 | 记录安装、模型配置、工具权限和 CLI 输出。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/02-quickstart-notes.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |

产出：`learning-notes/NousResearch__hermes-agent/02-quickstart-notes.md`。

## Level 3：理解源码

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `HERMES-L3-01` | Level 3 | 克隆源码并固定 commit。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/04-source-reading-notes.md` 和源码级调用链图; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HERMES-L3-02` | Level 3 | 找到 `AIAgent` 主循环。 | 已固定源码 commit 或公开源码视图日期 | 找到 `AIAgent` 主循环。 | `learning-notes/NousResearch__hermes-agent/04-source-reading-notes.md` 和源码级调用链图; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HERMES-L3-03` | Level 3 | 找到 prompt builder、context compression 和 prompt caching。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/04-source-reading-notes.md` 和源码级调用链图; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HERMES-L3-04` | Level 3 | 找到 provider runtime resolution 和模型 API mode 分支。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/04-source-reading-notes.md` 和源码级调用链图; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HERMES-L3-05` | Level 3 | 找到 `tools/registry.py`、`model_tools.py` 和 toolsets 的协作方式。 | 已固定源码 commit 或公开源码视图日期 | 找到 `tools/registry.py`、`model_tools.py` 和 toolsets 的协作方式。 | `learning-notes/NousResearch__hermes-agent/04-source-reading-notes.md` 和源码级调用链图; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HERMES-L3-06` | Level 3 | 找到 memory 文件、session storage 和 FTS5 搜索实现。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/04-source-reading-notes.md` 和源码级调用链图; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HERMES-L3-07` | Level 3 | 找到 gateway message dispatch、authorization 和 delivery。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/04-source-reading-notes.md` 和源码级调用链图; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HERMES-L3-08` | Level 3 | 找到 cron scheduler 和 job state 更新。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/04-source-reading-notes.md` 和源码级调用链图; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HERMES-L3-09` | Level 3 | 画出经过源码验证的 3 条调用链。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/04-source-reading-notes.md` 和源码级调用链图; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |

产出：`learning-notes/NousResearch__hermes-agent/04-source-reading-notes.md` 和源码级调用链图。

## Level 4：完成集成

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `HERMES-L4-01` | Level 4 | 配置一个最小 provider。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/05-integration-notes.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `HERMES-L4-02` | Level 4 | 启用一个安全的只读工具集。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/05-integration-notes.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `HERMES-L4-03` | Level 4 | 配置一个只读 MCP server。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/05-integration-notes.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `HERMES-L4-04` | Level 4 | 选择一个测试消息平台验证 gateway。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/05-integration-notes.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `HERMES-L4-05` | Level 4 | 创建一个低风险 cron job。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/05-integration-notes.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `HERMES-L4-06` | Level 4 | 记录权限、日志、失败路径和恢复方式。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/05-integration-notes.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |

产出：`learning-notes/NousResearch__hermes-agent/05-integration-notes.md`。

## Level 5：改造扩展

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `HERMES-L5-01` | Level 5 | 增加一个自定义只读 tool。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和安全边界记录; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `HERMES-L5-02` | Level 5 | 增加一个自定义 skill。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和安全边界记录; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `HERMES-L5-03` | Level 5 | 尝试切换 provider 或模型配置。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和安全边界记录; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `HERMES-L5-04` | Level 5 | 为关键调用链补一个最小回归测试或手工验证脚本。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和安全边界记录; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `HERMES-L5-05` | Level 5 | 对 terminal backend 的审批和隔离策略做一次安全复盘。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和安全边界记录; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |

产出：改造总结和安全边界记录。

## Level 6：总结评价

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `HERMES-L6-01` | Level 6 | 写出 Hermes Agent 的优势和限制。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/07-reflection.md` 和 `review-questions.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `HERMES-L6-02` | Level 6 | 写出适用场景和不适用场景。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/07-reflection.md` 和 `review-questions.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `HERMES-L6-03` | Level 6 | 与 Claude Code、OpenAI Codex、OpenHands、LangGraph 中至少两个项目对比。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/07-reflection.md` 和 `review-questions.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `HERMES-L6-04` | Level 6 | 总结可借鉴的工程设计。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/07-reflection.md` 和 `review-questions.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `HERMES-L6-05` | Level 6 | 生成复习问题。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/NousResearch__hermes-agent/07-reflection.md` 和 `review-questions.md`; projects/product-agents/NousResearch__hermes-agent/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |

产出：`learning-notes/NousResearch__hermes-agent/07-reflection.md` 和 `review-questions.md`。


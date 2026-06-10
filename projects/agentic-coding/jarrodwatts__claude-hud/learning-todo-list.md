# Claude HUD Learning Todo List

本清单已经迁移为可执行任务表。每个任务必须同步更新学习笔记、`evidence.md` 和 `learning-notes/jarrodwatts__claude-hud/progress.json`；未验证内容保持未完成。

## Level 1：了解项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `HUD-L1-01` | Level 1 | 阅读 README 和 README.zh.md。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/01-first-impression.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `HUD-L1-02` | Level 1 | 用一句话说明 Claude HUD 和 Claude Code statusline 的关系。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/01-first-impression.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `HUD-L1-03` | Level 1 | 区分 context usage、subscriber usage、tool activity、agent activity、todo progress。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/01-first-impression.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `HUD-L1-04` | Level 1 | 记录默认显示内容和可选显示内容。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/01-first-impression.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `HUD-L1-05` | Level 1 | 阅读 `.claude-plugin/plugin.json`，理解 plugin command 分发。 | 项目 README 或官方文档可访问 | 阅读 `.claude-plugin/plugin.json`，理解 plugin command 分发。 | `learning-notes/jarrodwatts__claude-hud/01-first-impression.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |

产出：`learning-notes/jarrodwatts__claude-hud/01-first-impression.md`。

## Level 2：跑通使用

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `HUD-L2-01` | Level 2 | 在临时 Claude 配置或测试机器中安装 plugin。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/02-quickstart-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `HUD-L2-02` | Level 2 | 执行 `/plugin marketplace add jarrodwatts/claude-hud`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `/plugin marketplace add jarrodwatts/claude-hud`。 | `learning-notes/jarrodwatts__claude-hud/02-quickstart-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `HUD-L2-03` | Level 2 | 执行 `/plugin install claude-hud` 和 `/reload-plugins`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `/plugin install claude-hud` 和 `/reload-plugins`。 | `learning-notes/jarrodwatts__claude-hud/02-quickstart-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `HUD-L2-04` | Level 2 | 执行 `/claude-hud:setup`，记录写入的 statusLine command。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `/claude-hud:setup`，记录写入的 statusLine command。 | `learning-notes/jarrodwatts__claude-hud/02-quickstart-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `HUD-L2-05` | Level 2 | 完全重启 Claude Code，确认 HUD 是否出现。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/02-quickstart-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `HUD-L2-06` | Level 2 | 执行 `/claude-hud:configure`，开启 tools、agents、todos 和中文 labels。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `/claude-hud:configure`，开启 tools、agents、todos 和中文 labels。 | `learning-notes/jarrodwatts__claude-hud/02-quickstart-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |

产出：`learning-notes/jarrodwatts__claude-hud/02-quickstart-notes.md`。

## Level 3：理解源码

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `HUD-L3-01` | Level 3 | 阅读 `src/index.ts` 主链路。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `src/index.ts` 主链路。 | `learning-notes/jarrodwatts__claude-hud/04-source-reading-notes.md` 和源码图解; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HUD-L3-02` | Level 3 | 阅读 `src/stdin.ts`，理解 stdin timeout、max bytes、context percent 和 rate limits。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `src/stdin.ts`，理解 stdin timeout、max bytes、context percent 和 rate limits。 | `learning-notes/jarrodwatts__claude-hud/04-source-reading-notes.md` 和源码图解; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HUD-L3-03` | Level 3 | 阅读 `src/transcript.ts`，确认 tool、Skill、MCP、Agent、Todo 的解析方式。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `src/transcript.ts`，确认 tool、Skill、MCP、Agent、Todo 的解析方式。 | `learning-notes/jarrodwatts__claude-hud/04-source-reading-notes.md` 和源码图解; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HUD-L3-04` | Level 3 | 阅读 `src/config.ts`，理解 defaults、migration 和 validation。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `src/config.ts`，理解 defaults、migration 和 validation。 | `learning-notes/jarrodwatts__claude-hud/04-source-reading-notes.md` 和源码图解; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HUD-L3-05` | Level 3 | 阅读 `src/render/index.ts`，理解 compact / expanded layout 和宽度处理。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `src/render/index.ts`，理解 compact / expanded layout 和宽度处理。 | `learning-notes/jarrodwatts__claude-hud/04-source-reading-notes.md` 和源码图解; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HUD-L3-06` | Level 3 | 阅读 `src/git.ts`，理解 git status 和 file stats。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `src/git.ts`，理解 git status 和 file stats。 | `learning-notes/jarrodwatts__claude-hud/04-source-reading-notes.md` 和源码图解; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `HUD-L3-07` | Level 3 | 阅读 `src/external-usage.ts`，理解 usage snapshot 读写边界。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `src/external-usage.ts`，理解 usage snapshot 读写边界。 | `learning-notes/jarrodwatts__claude-hud/04-source-reading-notes.md` 和源码图解; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |

产出：`learning-notes/jarrodwatts__claude-hud/04-source-reading-notes.md` 和源码图解。

## Level 4：完成集成验证

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `HUD-L4-01` | Level 4 | 用临时 `CLAUDE_CONFIG_DIR` 验证 setup 不误改主配置。 | 已有运行证据，或已明确集成验证边界 | 用临时 `CLAUDE_CONFIG_DIR` 验证 setup 不误改主配置。 | `learning-notes/jarrodwatts__claude-hud/05-integration-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `HUD-L4-02` | Level 4 | 验证已有 statusline 时的备份和询问逻辑。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/05-integration-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `HUD-L4-03` | Level 4 | 采集真实 statusline stdin JSON 样例。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/05-integration-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `HUD-L4-04` | Level 4 | 采集真实 transcript JSONL 样例。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/05-integration-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `HUD-L4-05` | Level 4 | 触发 Read/Edit/Grep/Bash，确认 tools line。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/05-integration-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `HUD-L4-06` | Level 4 | 触发 TodoWrite 或任务计划，确认 todo progress。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/05-integration-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `HUD-L4-07` | Level 4 | 触发一个 subagent，确认 agents line。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/05-integration-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `HUD-L4-08` | Level 4 | 配置一个 MCP server，确认 MCP activity line。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/05-integration-notes.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |

产出：`learning-notes/jarrodwatts__claude-hud/05-integration-notes.md`。

## Level 5：二次改造

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `HUD-L5-01` | Level 5 | 增加一个新的 display element 并接入 `elementOrder`。 | 已理解最小集成路径；使用沙箱或只输出设计 | 增加一个新的 display element 并接入 `elementOrder`。 | extension summary in `learning-notes/jarrodwatts__claude-hud/07-reflection.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `HUD-L5-02` | Level 5 | 增加一个新的 config validation case。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | extension summary in `learning-notes/jarrodwatts__claude-hud/07-reflection.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `HUD-L5-03` | Level 5 | 增加一个 transcript fixture，覆盖新的 Claude Code payload。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | extension summary in `learning-notes/jarrodwatts__claude-hud/07-reflection.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `HUD-L5-04` | Level 5 | 改造 render 截断或 CJK 宽度处理，并补测试。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | extension summary in `learning-notes/jarrodwatts__claude-hud/07-reflection.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `HUD-L5-05` | Level 5 | 分析并修复当前 Windows 测试失败中的一个模块。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | extension summary in `learning-notes/jarrodwatts__claude-hud/07-reflection.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |

产出：extension summary in `learning-notes/jarrodwatts__claude-hud/07-reflection.md`。

## Level 6：总结评价

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `HUD-L6-01` | Level 6 | 写出 Claude HUD 的优势和限制。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `HUD-L6-02` | Level 6 | 写出 statusline 方案相比独立 TUI / dashboard 的取舍。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `HUD-L6-03` | Level 6 | 与 Claude Code 原生 `/context`、自定义 statusline、其他 HUD 工具做对比。 | 前序笔记和证据已更新 | 与 Claude Code 原生 `/context`、自定义 statusline、其他 HUD 工具做对比。 | `learning-notes/jarrodwatts__claude-hud/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `HUD-L6-04` | Level 6 | 总结可借鉴的工程设计：stdin schema、防御式解析、缓存、配置迁移、跨平台 setup。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/jarrodwatts__claude-hud/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/jarrodwatts__claude-hud/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |

产出：`learning-notes/jarrodwatts__claude-hud/07-reflection.md` 和 `review-questions.md`。


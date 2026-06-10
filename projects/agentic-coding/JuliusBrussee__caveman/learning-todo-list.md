# Caveman Learning Todo List

本清单已经迁移为可执行任务表。每个任务必须同步更新学习笔记、`evidence.md` 和 `learning-notes/JuliusBrussee__caveman/progress.json`；未验证内容保持未完成。

## Level 1：了解项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `CAVEMAN-L1-01` | Level 1 | 阅读 README、INSTALL.md、CLAUDE.md 和 `src/hooks/README.md`。 | 项目 README 或官方文档可访问 | 阅读 README、INSTALL.md、CLAUDE.md 和 `src/hooks/README.md`。 | `learning-notes/JuliusBrussee__caveman/01-first-impression.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `CAVEMAN-L1-02` | Level 1 | 用一句话说明 Caveman 与普通“回答简短点”提示词的区别。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/01-first-impression.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `CAVEMAN-L1-03` | Level 1 | 列出 `caveman`、`caveman-compress`、`caveman-stats`、`caveman-shrink`、`cavecrew` 的职责。 | 项目 README 或官方文档可访问 | 列出 `caveman`、`caveman-compress`、`caveman-stats`、`caveman-shrink`、`cavecrew` 的职责。 | `learning-notes/JuliusBrussee__caveman/01-first-impression.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `CAVEMAN-L1-04` | Level 1 | 标注自己最关心的 Agent 路径：Codex、Claude Code、Gemini CLI、OpenCode 或 Cursor。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/01-first-impression.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `CAVEMAN-L1-05` | Level 1 | 记录第一印象和待验证问题。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/01-first-impression.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |

产出：`learning-notes/JuliusBrussee__caveman/01-first-impression.md`。

## Level 2：跑通项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `CAVEMAN-L2-01` | Level 2 | 准备 Node 18+。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/02-quickstart-notes.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `CAVEMAN-L2-02` | Level 2 | 在临时目录克隆仓库并固定 commit。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/02-quickstart-notes.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `CAVEMAN-L2-03` | Level 2 | 执行 `node bin/install.js --list`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `node bin/install.js --list`。 | `learning-notes/JuliusBrussee__caveman/02-quickstart-notes.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `CAVEMAN-L2-04` | Level 2 | 执行 `node bin/install.js --dry-run --all`，记录写入计划。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `node bin/install.js --dry-run --all`，记录写入计划。 | `learning-notes/JuliusBrussee__caveman/02-quickstart-notes.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `CAVEMAN-L2-05` | Level 2 | 只选择一个非关键 Agent 做安装验证。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/02-quickstart-notes.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `CAVEMAN-L2-06` | Level 2 | 记录安装、激活、关闭和卸载命令。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/02-quickstart-notes.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |

产出：`learning-notes/JuliusBrussee__caveman/02-quickstart-notes.md`。

## Level 3：理解源码

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `CAVEMAN-L3-01` | Level 3 | 找到 `bin/install.js` 的 provider matrix。 | 已固定源码 commit 或公开源码视图日期 | 找到 `bin/install.js` 的 provider matrix。 | `learning-notes/JuliusBrussee__caveman/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `CAVEMAN-L3-02` | Level 3 | 确认参数解析、dry-run、`--only`、`--all`、`--uninstall` 行为。 | 已固定源码 commit 或公开源码视图日期 | 确认参数解析、dry-run、`--only`、`--all`、`--uninstall` 行为。 | `learning-notes/JuliusBrussee__caveman/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `CAVEMAN-L3-03` | Level 3 | 确认 `bin/lib/settings.js` 如何读写 JSON / JSONC 配置。 | 已固定源码 commit 或公开源码视图日期 | 确认 `bin/lib/settings.js` 如何读写 JSON / JSONC 配置。 | `learning-notes/JuliusBrussee__caveman/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `CAVEMAN-L3-04` | Level 3 | 确认 `src/hooks/caveman-activate.js` 的 SessionStart 行为。 | 已固定源码 commit 或公开源码视图日期 | 确认 `src/hooks/caveman-activate.js` 的 SessionStart 行为。 | `learning-notes/JuliusBrussee__caveman/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `CAVEMAN-L3-05` | Level 3 | 确认 `src/hooks/caveman-mode-tracker.js` 的模式解析和关闭逻辑。 | 已固定源码 commit 或公开源码视图日期 | 确认 `src/hooks/caveman-mode-tracker.js` 的模式解析和关闭逻辑。 | `learning-notes/JuliusBrussee__caveman/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `CAVEMAN-L3-06` | Level 3 | 确认 `src/mcp-servers/caveman-shrink/` 的 JSON-RPC 透传和字段压缩。 | 已固定源码 commit 或公开源码视图日期 | 确认 `src/mcp-servers/caveman-shrink/` 的 JSON-RPC 透传和字段压缩。 | `learning-notes/JuliusBrussee__caveman/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `CAVEMAN-L3-07` | Level 3 | 确认 `skills/caveman-compress/scripts/` 的路径、安全和备份逻辑。 | 已固定源码 commit 或公开源码视图日期 | 确认 `skills/caveman-compress/scripts/` 的路径、安全和备份逻辑。 | `learning-notes/JuliusBrussee__caveman/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `CAVEMAN-L3-08` | Level 3 | 画出安装器、hook 和 MCP shrink 的关键调用链。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |

产出：`learning-notes/JuliusBrussee__caveman/04-source-reading-notes.md` 和调用链图。

## Level 4：完成集成

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `CAVEMAN-L4-01` | Level 4 | 在测试环境执行 Codex 单路径安装。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/05-integration-notes.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `CAVEMAN-L4-02` | Level 4 | 新开会话分别执行 `/caveman lite`、`/caveman full`、`/caveman ultra`，记录输出差异。 | 已有运行证据，或已明确集成验证边界 | 新开会话分别执行 `/caveman lite`、`/caveman full`、`/caveman ultra`，记录输出差异。 | `learning-notes/JuliusBrussee__caveman/05-integration-notes.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `CAVEMAN-L4-03` | Level 4 | 对一个真实代码 review 问题比较普通输出和 caveman 输出。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/05-integration-notes.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `CAVEMAN-L4-04` | Level 4 | 在测试 MCP server 上验证 `caveman-shrink`。 | 已有运行证据，或已明确集成验证边界 | 在测试 MCP server 上验证 `caveman-shrink`。 | `learning-notes/JuliusBrussee__caveman/05-integration-notes.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `CAVEMAN-L4-05` | Level 4 | 用无敏感测试文件验证 `caveman-compress` 备份和写回行为。 | 已有运行证据，或已明确集成验证边界 | 用无敏感测试文件验证 `caveman-compress` 备份和写回行为。 | `learning-notes/JuliusBrussee__caveman/05-integration-notes.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `CAVEMAN-L4-06` | Level 4 | 记录回滚或卸载流程。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/05-integration-notes.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |

产出：`learning-notes/JuliusBrussee__caveman/05-integration-notes.md`。

## Level 5：改造扩展

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `CAVEMAN-L5-01` | Level 5 | 为团队定义“何时可以压缩、何时必须完整表达”的规则。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `CAVEMAN-L5-02` | Level 5 | 给一个测试 MCP server 设计 shrink 前后对比脚本。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `CAVEMAN-L5-03` | Level 5 | 给安装器写入范围做一份 checklist。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `CAVEMAN-L5-04` | Level 5 | 对 `caveman-compress` 设计敏感内容预检步骤。 | 已理解最小集成路径；使用沙箱或只输出设计 | 对 `caveman-compress` 设计敏感内容预检步骤。 | 改造总结和可复用经验; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `CAVEMAN-L5-05` | Level 5 | 比较 Caveman 与普通 concise system prompt 的差异。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |

产出：改造总结和可复用经验。

## Level 6：总结评价

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `CAVEMAN-L6-01` | Level 6 | 写出 Caveman 的优势和限制。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `CAVEMAN-L6-02` | Level 6 | 写出适用和不适用场景。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `CAVEMAN-L6-03` | Level 6 | 与 Graphify、codebase-memory-mcp、普通 prompt snippet 和 editor rule files 对比。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `CAVEMAN-L6-04` | Level 6 | 总结可借鉴设计：跨 Agent 分发、hook 状态、MCP metadata 压缩、benchmark 口径。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `CAVEMAN-L6-05` | Level 6 | 生成复习问题。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/JuliusBrussee__caveman/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/JuliusBrussee__caveman/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |

产出：`learning-notes/JuliusBrussee__caveman/07-reflection.md` 和 `review-questions.md`。


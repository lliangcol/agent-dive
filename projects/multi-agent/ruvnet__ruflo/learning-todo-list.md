# Ruflo Learning Todo List

本清单已经迁移为可执行任务表。每个任务必须同步更新学习笔记、`evidence.md` 和 `learning-notes/ruvnet__ruflo/progress.json`；未验证内容保持未完成。

## Level 1：了解项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `RUFLO-L1-01` | Level 1 | 阅读 README、`ruflo/package.json`、root `package.json`、`.claude-plugin/plugin.json`。 | 项目 README 或官方文档可访问 | 阅读 README、`ruflo/package.json`、root `package.json`、`.claude-plugin/plugin.json`。 | `learning-notes/ruvnet__ruflo/01-first-impression.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `RUFLO-L1-02` | Level 1 | 用一句话说明 Ruflo 与 Claude Flow、`@claude-flow/cli`、`@claude-flow/codex` 的关系。 | 项目 README 或官方文档可访问 | 用一句话说明 Ruflo 与 Claude Flow、`@claude-flow/cli`、`@claude-flow/codex` 的关系。 | `learning-notes/ruvnet__ruflo/01-first-impression.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `RUFLO-L1-03` | Level 1 | 区分 Claude Code plugin lite、CLI full install、MCP server、Codex `.agents` config 四条路径。 | 项目 README 或官方文档可访问 | 区分 Claude Code plugin lite、CLI full install、MCP server、Codex `.agents` config 四条路径。 | `learning-notes/ruvnet__ruflo/01-first-impression.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `RUFLO-L1-04` | Level 1 | 列出 README 中提到的 agents、commands、MCP tools、plugins，并标注“待复核”。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/ruvnet__ruflo/01-first-impression.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `RUFLO-L1-05` | Level 1 | 写出第一印象和待验证问题。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/ruvnet__ruflo/01-first-impression.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |

产出：`learning-notes/ruvnet__ruflo/01-first-impression.md`。

## Level 2：跑通只读评估

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `RUFLO-L2-01` | Level 2 | 准备 Node.js `>=20`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 准备 Node.js `>=20`。 | `learning-notes/ruvnet__ruflo/02-quickstart-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `RUFLO-L2-02` | Level 2 | 执行 `npx --yes ruflo@latest --version`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `npx --yes ruflo@latest --version`。 | `learning-notes/ruvnet__ruflo/02-quickstart-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `RUFLO-L2-03` | Level 2 | 执行 `npx --yes ruflo@latest --help`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `npx --yes ruflo@latest --help`。 | `learning-notes/ruvnet__ruflo/02-quickstart-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `RUFLO-L2-04` | Level 2 | 执行 `npx --yes ruflo@latest mcp start --help`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `npx --yes ruflo@latest mcp start --help`。 | `learning-notes/ruvnet__ruflo/02-quickstart-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `RUFLO-L2-05` | Level 2 | 执行 `npx --yes ruflo@latest init --help`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `npx --yes ruflo@latest init --help`。 | `learning-notes/ruvnet__ruflo/02-quickstart-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `RUFLO-L2-06` | Level 2 | 记录输出、耗时、是否下载额外模型/包、是否发生写入。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/ruvnet__ruflo/02-quickstart-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `RUFLO-L2-07` | Level 2 | 与 `npx --yes --package @claude-flow/cli@latest claude-flow --version` 对比。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 与 `npx --yes --package @claude-flow/cli@latest claude-flow --version` 对比。 | `learning-notes/ruvnet__ruflo/02-quickstart-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |

产出：`learning-notes/ruvnet__ruflo/02-quickstart-notes.md`。

## Level 3：理解源码

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `RUFLO-L3-01` | Level 3 | 阅读 `ruflo/bin/ruflo.js`，理解 wrapper 和 MCP 模式分流。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `ruflo/bin/ruflo.js`，理解 wrapper 和 MCP 模式分流。 | `learning-notes/ruvnet__ruflo/04-source-reading-notes.md` 和调用链图; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RUFLO-L3-02` | Level 3 | 阅读 `v3/@claude-flow/cli/bin/cli.js`，关注 stdout 过滤、MCP parser、buffer cap。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `v3/@claude-flow/cli/bin/cli.js`，关注 stdout 过滤、MCP parser、buffer cap。 | `learning-notes/ruvnet__ruflo/04-source-reading-notes.md` 和调用链图; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RUFLO-L3-03` | Level 3 | 阅读 `v3/@claude-flow/cli/src/commands/index.ts`，整理命令分类。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `v3/@claude-flow/cli/src/commands/index.ts`，整理命令分类。 | `learning-notes/ruvnet__ruflo/04-source-reading-notes.md` 和调用链图; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RUFLO-L3-04` | Level 3 | 阅读 `v3/@claude-flow/cli/src/mcp-tools/index.ts`，整理 tool groups。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `v3/@claude-flow/cli/src/mcp-tools/index.ts`，整理 tool groups。 | `learning-notes/ruvnet__ruflo/04-source-reading-notes.md` 和调用链图; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RUFLO-L3-05` | Level 3 | 阅读 `v3/src/agent-lifecycle/domain/Agent.ts`。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `v3/src/agent-lifecycle/domain/Agent.ts`。 | `learning-notes/ruvnet__ruflo/04-source-reading-notes.md` 和调用链图; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RUFLO-L3-06` | Level 3 | 阅读 `v3/src/coordination/application/SwarmCoordinator.ts`。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `v3/src/coordination/application/SwarmCoordinator.ts`。 | `learning-notes/ruvnet__ruflo/04-source-reading-notes.md` 和调用链图; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RUFLO-L3-07` | Level 3 | 阅读 `v3/src/task-execution/application/WorkflowEngine.ts`。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `v3/src/task-execution/application/WorkflowEngine.ts`。 | `learning-notes/ruvnet__ruflo/04-source-reading-notes.md` 和调用链图; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RUFLO-L3-08` | Level 3 | 阅读 `v3/src/memory/infrastructure/HybridBackend.ts`、`SQLiteBackend.ts`、`AgentDBBackend.ts`。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `v3/src/memory/infrastructure/HybridBackend.ts`、`SQLiteBackend.ts`、`AgentDBBackend.ts`。 | `learning-notes/ruvnet__ruflo/04-source-reading-notes.md` 和调用链图; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RUFLO-L3-09` | Level 3 | 阅读 `v3/src/infrastructure/plugins/PluginManager.ts`。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `v3/src/infrastructure/plugins/PluginManager.ts`。 | `learning-notes/ruvnet__ruflo/04-source-reading-notes.md` 和调用链图; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RUFLO-L3-10` | Level 3 | 阅读 `.claude-plugin/hooks/hooks.json` 和 `plugins/ruflo-core/scripts/`。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `.claude-plugin/hooks/hooks.json` 和 `plugins/ruflo-core/scripts/`。 | `learning-notes/ruvnet__ruflo/04-source-reading-notes.md` 和调用链图; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |

产出：`learning-notes/ruvnet__ruflo/04-source-reading-notes.md` 和调用链图。

## Level 4：完成最小集成

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `RUFLO-L4-01` | Level 4 | 在临时项目中安装 Claude Code plugin lite，记录可见 commands/agents/skills。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/ruvnet__ruflo/05-integration-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `RUFLO-L4-02` | Level 4 | 在临时项目中执行 Ruflo CLI full init，记录新增/修改文件。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/ruvnet__ruflo/05-integration-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `RUFLO-L4-03` | Level 4 | 验证 MCP server tool list。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/ruvnet__ruflo/05-integration-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `RUFLO-L4-04` | Level 4 | 触发一个低风险 agent / swarm / memory tool。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/ruvnet__ruflo/05-integration-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `RUFLO-L4-05` | Level 4 | 验证 `.agents/config.toml` 是否能被 Codex 读取。 | 已有运行证据，或已明确集成验证边界 | 验证 `.agents/config.toml` 是否能被 Codex 读取。 | `learning-notes/ruvnet__ruflo/05-integration-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `RUFLO-L4-06` | Level 4 | 验证 `.agents/skills/` 是否能被 Codex 暴露。 | 已有运行证据，或已明确集成验证边界 | 验证 `.agents/skills/` 是否能被 Codex 暴露。 | `learning-notes/ruvnet__ruflo/05-integration-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `RUFLO-L4-07` | Level 4 | 测试卸载或手动回滚路径。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/ruvnet__ruflo/05-integration-notes.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |

产出：`learning-notes/ruvnet__ruflo/05-integration-notes.md`。

## Level 5：改造扩展

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `RUFLO-L5-01` | Level 5 | 设计一个最小团队级 Ruflo profile：只启用 swarm、memory、review/security skills。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `RUFLO-L5-02` | Level 5 | 禁用高风险 hooks 和外部 provider，记录上下文和权限变化。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `RUFLO-L5-03` | Level 5 | 为一个小型代码仓库设计 Ruflo MCP tool allowlist。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `RUFLO-L5-04` | Level 5 | 用 CI 复现 witness / verification 思路，防止关键 hook 或 MCP tool drift。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `RUFLO-L5-05` | Level 5 | 对比 Ruflo 与 ECC、CodeGraph、Graphify、Caveman 的集成边界。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |

产出：改造总结和可复用经验。

## Level 6：总结评价

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `RUFLO-L6-01` | Level 6 | 写出 Ruflo 的优势和限制。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/ruvnet__ruflo/07-reflection.md` 和 `review-questions.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `RUFLO-L6-02` | Level 6 | 写出适用和不适用场景。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/ruvnet__ruflo/07-reflection.md` 和 `review-questions.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `RUFLO-L6-03` | Level 6 | 总结可借鉴设计：MCP stdio hardening、plugin lite/full install 分层、swarm runtime、hybrid memory、verification witness。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/ruvnet__ruflo/07-reflection.md` 和 `review-questions.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `RUFLO-L6-04` | Level 6 | 总结必须避免的风险：写入范围不清、hook 误判、Codex 边界误判、数量漂移、Web UI 数据边界。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/ruvnet__ruflo/07-reflection.md` 和 `review-questions.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `RUFLO-L6-05` | Level 6 | 生成复习问题。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/ruvnet__ruflo/07-reflection.md` 和 `review-questions.md`; projects/multi-agent/ruvnet__ruflo/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |

产出：`learning-notes/ruvnet__ruflo/07-reflection.md` 和 `review-questions.md`。


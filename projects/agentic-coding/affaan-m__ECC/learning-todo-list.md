# ECC Learning Todo List

本清单已经迁移为可执行任务表。每个任务必须同步更新学习笔记、`evidence.md` 和 `learning-notes/affaan-m__ECC/progress.json`；未验证内容保持未完成。

## Level 1：了解项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `ECC-L1-01` | Level 1 | 阅读 README、README.zh-CN、`docs/architecture/cross-harness.md` 和 `docs/releases/2.0.0/release-notes.md`。 | 项目 README 或官方文档可访问 | 阅读 README、README.zh-CN、`docs/architecture/cross-harness.md` 和 `docs/releases/2.0.0/release-notes.md`。 | `learning-notes/affaan-m__ECC/01-first-impression.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `ECC-L1-02` | Level 1 | 用一句话说明 ECC 和普通 dotfiles / prompt library / plugin 的区别。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/01-first-impression.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `ECC-L1-03` | Level 1 | 区分 shared source、harness adapter、hook-backed、instruction-backed 四个概念。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/01-first-impression.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `ECC-L1-04` | Level 1 | 列出 Claude Code、Codex、OpenCode、Cursor、Gemini、Zed 的支持边界。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/01-first-impression.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `ECC-L1-05` | Level 1 | 记录 README、release notes、plugin manifest 中能力数量和术语差异。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/01-first-impression.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `ECC-L1-06` | Level 1 | 写出第一印象和待验证问题。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/01-first-impression.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |

产出：`learning-notes/affaan-m__ECC/01-first-impression.md`。

## Level 2：跑通只读评估

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `ECC-L2-01` | Level 2 | 准备 Node.js `>=18`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 准备 Node.js `>=18`。 | `learning-notes/affaan-m__ECC/02-quickstart-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `ECC-L2-02` | Level 2 | 执行 `npx --yes --package ecc-universal ecc --help` 或本地 clone 后执行 `node scripts/ecc.js --help`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `npx --yes --package ecc-universal ecc --help` 或本地 clone 后执行 `node scripts/ecc.js --help`。 | `learning-notes/affaan-m__ECC/02-quickstart-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `ECC-L2-03` | Level 2 | 执行 `npx --yes --package ecc-universal ecc plan --list-profiles`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `npx --yes --package ecc-universal ecc plan --list-profiles`。 | `learning-notes/affaan-m__ECC/02-quickstart-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `ECC-L2-04` | Level 2 | 执行 `npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json`。 | `learning-notes/affaan-m__ECC/02-quickstart-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `ECC-L2-05` | Level 2 | 执行 `npx --yes --package ecc-universal ecc consult "tdd code review security" --target codex`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `npx --yes --package ecc-universal ecc consult "tdd code review security" --target codex`。 | `learning-notes/affaan-m__ECC/02-quickstart-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `ECC-L2-06` | Level 2 | 记录命令、输出、耗时和是否有网络依赖。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/02-quickstart-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `ECC-L2-07` | Level 2 | 确认只读命令没有修改用户目录或项目目录。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/02-quickstart-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |

产出：`learning-notes/affaan-m__ECC/02-quickstart-notes.md`。

## Level 3：理解源码

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `ECC-L3-01` | Level 3 | 阅读 `package.json` 的 bin、scripts、files、engines。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `package.json` 的 bin、scripts、files、engines。 | `learning-notes/affaan-m__ECC/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `ECC-L3-02` | Level 3 | 追踪 `scripts/ecc.js` 的命令分发。 | 已固定源码 commit 或公开源码视图日期 | 追踪 `scripts/ecc.js` 的命令分发。 | `learning-notes/affaan-m__ECC/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `ECC-L3-03` | Level 3 | 追踪 `scripts/install-plan.js` 的参数解析和 plan 输出。 | 已固定源码 commit 或公开源码视图日期 | 追踪 `scripts/install-plan.js` 的参数解析和 plan 输出。 | `learning-notes/affaan-m__ECC/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `ECC-L3-04` | Level 3 | 追踪 `scripts/install-apply.js` 到 install runtime / executor。 | 已固定源码 commit 或公开源码视图日期 | 追踪 `scripts/install-apply.js` 到 install runtime / executor。 | `learning-notes/affaan-m__ECC/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `ECC-L3-05` | Level 3 | 阅读 `scripts/lib/install-manifests.js`，整理 profile、module、component、target 的数据结构。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `scripts/lib/install-manifests.js`，整理 profile、module、component、target 的数据结构。 | `learning-notes/affaan-m__ECC/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `ECC-L3-06` | Level 3 | 阅读 `.codex-plugin/plugin.json`、`.claude-plugin/plugin.json`、`.opencode/README.md`，对比 adapter。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `.codex-plugin/plugin.json`、`.claude-plugin/plugin.json`、`.opencode/README.md`，对比 adapter。 | `learning-notes/affaan-m__ECC/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `ECC-L3-07` | Level 3 | 阅读 `hooks/hooks.json`，按 lifecycle 分组 hook。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `hooks/hooks.json`，按 lifecycle 分组 hook。 | `learning-notes/affaan-m__ECC/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `ECC-L3-08` | Level 3 | 选 3 个 hook script 深读：配置保护、quality gate、session-end。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `ECC-L3-09` | Level 3 | 阅读 `scripts/control-pane.js` 和 `scripts/lib/control-pane/`。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `scripts/control-pane.js` 和 `scripts/lib/control-pane/`。 | `learning-notes/affaan-m__ECC/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `ECC-L3-10` | Level 3 | 阅读 `tests/` 和 `scripts/ci/`，列出 catalog / manifest / hook / skill 校验项。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `tests/` 和 `scripts/ci/`，列出 catalog / manifest / hook / skill 校验项。 | `learning-notes/affaan-m__ECC/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |

产出：`learning-notes/affaan-m__ECC/04-source-reading-notes.md` 和调用链图。

## Level 4：完成最小集成

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `ECC-L4-01` | Level 4 | 在临时测试环境执行 Codex target 的 dry-run install。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/05-integration-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `ECC-L4-02` | Level 4 | 检查 planned file operations，确认写入范围。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/05-integration-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `ECC-L4-03` | Level 4 | 真实安装 minimal Codex profile，并记录变更文件。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/05-integration-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `ECC-L4-04` | Level 4 | 在 Codex 中确认 `AGENTS.md` / skills / MCP 配置是否可见。 | 已有运行证据，或已明确集成验证边界 | 在 Codex 中确认 `AGENTS.md` / skills / MCP 配置是否可见。 | `learning-notes/affaan-m__ECC/05-integration-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `ECC-L4-05` | Level 4 | 在 Claude Code 测试环境安装 plugin，并确认 hooks 是否加载。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/05-integration-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `ECC-L4-06` | Level 4 | 触发一个低风险 hook，记录 stdout/stderr/exit code。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/05-integration-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `ECC-L4-07` | Level 4 | 尝试 OpenCode plugin 或 Cursor adapter 的最小路径。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/05-integration-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `ECC-L4-08` | Level 4 | 执行卸载或回滚，确认 install-state 是否足够。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/05-integration-notes.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |

产出：`learning-notes/affaan-m__ECC/05-integration-notes.md`。

## Level 5：改造扩展

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `ECC-L5-01` | Level 5 | 为一个本地项目设计最小 ECC profile：只保留 TDD、review、security、verification。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `ECC-L5-02` | Level 5 | 删除或禁用不需要的 MCP、hooks、rules，记录上下文节省。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `ECC-L5-03` | Level 5 | 自定义一个团队 skill，并验证是否能跨 Codex / Claude Code 复用。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `ECC-L5-04` | Level 5 | 增加一条团队级安全门禁，避免写入密钥或私有路径。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `ECC-L5-05` | Level 5 | 设计一个 CI 校验，防止 ECC config drift。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `ECC-L5-06` | Level 5 | 比较 ECC 和本仓库现有 AGENTS / skills / governance 的差异。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |

产出：改造总结和可复用经验。

## Level 6：总结评价

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `ECC-L6-01` | Level 6 | 写出 ECC 的优势和限制。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `ECC-L6-02` | Level 6 | 写出适用和不适用场景。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `ECC-L6-03` | Level 6 | 与 CodeGraph、Graphify、onm-agent-pack / governance tooling 做对比。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `ECC-L6-04` | Level 6 | 总结可借鉴设计：薄适配、manifest install、hook lifecycle、session state、MCP inventory。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `ECC-L6-05` | Level 6 | 总结必须避免的风险：重复安装、全局污染、hook 误判、数量漂移、私有信息泄露。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `ECC-L6-06` | Level 6 | 生成复习问题。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/affaan-m__ECC/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/affaan-m__ECC/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |

产出：`learning-notes/affaan-m__ECC/07-reflection.md` 和 `review-questions.md`。


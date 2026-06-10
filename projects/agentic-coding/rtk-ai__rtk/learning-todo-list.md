# RTK Learning Todo List

本清单已经迁移为可执行任务表。每个任务必须同步更新学习笔记、`evidence.md` 和 `learning-notes/rtk-ai__rtk/progress.json`；未验证内容保持未完成。

## Level 1：了解项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `RTK-L1-01` | Level 1 | 阅读 README、INSTALL.md、`docs/contributing/ARCHITECTURE.md`、`hooks/README.md` 和 `docs/TELEMETRY.md`。 | 项目 README 或官方文档可访问 | 阅读 README、INSTALL.md、`docs/contributing/ARCHITECTURE.md`、`hooks/README.md` 和 `docs/TELEMETRY.md`。 | `learning-notes/rtk-ai__rtk/01-first-impression.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `RTK-L1-02` | Level 1 | 用一句话说明 RTK 与普通 shell alias、日志截断工具、Agent 框架的区别。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/01-first-impression.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `RTK-L1-03` | Level 1 | 列出 RTK 支持的命令类别：git、tests、build、files、cloud、containers、package managers。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/01-first-impression.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `RTK-L1-04` | Level 1 | 区分 transparent hook、plugin mutation、deny-with-suggestion 和 prompt-level guidance。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/01-first-impression.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `RTK-L1-05` | Level 1 | 记录第一印象和待验证问题。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/01-first-impression.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |

产出：`learning-notes/rtk-ai__rtk/01-first-impression.md`。

## Level 2：跑通项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `RTK-L2-01` | Level 2 | 在临时环境安装 RTK，确认 `rtk --version`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 在临时环境安装 RTK，确认 `rtk --version`。 | `learning-notes/rtk-ai__rtk/02-quickstart-notes.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `RTK-L2-02` | Level 2 | 确认没有安装到 crates.io 同名 Rust Type Kit。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/02-quickstart-notes.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `RTK-L2-03` | Level 2 | 执行 `rtk rewrite "git status"`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `rtk rewrite "git status"`。 | `learning-notes/rtk-ai__rtk/02-quickstart-notes.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `RTK-L2-04` | Level 2 | 在小仓库对比 `git status` 与 `rtk git status`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 在小仓库对比 `git status` 与 `rtk git status`。 | `learning-notes/rtk-ai__rtk/02-quickstart-notes.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `RTK-L2-05` | Level 2 | 对比 `git diff`、`git diff --stat` 与 `rtk git diff` 的输出差异。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 对比 `git diff`、`git diff --stat` 与 `rtk git diff` 的输出差异。 | `learning-notes/rtk-ai__rtk/02-quickstart-notes.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `RTK-L2-06` | Level 2 | 构造失败命令并验证 tee raw-output recovery。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/02-quickstart-notes.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `RTK-L2-07` | Level 2 | 执行 `rtk gain`，记录 tracking 行为。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `rtk gain`，记录 tracking 行为。 | `learning-notes/rtk-ai__rtk/02-quickstart-notes.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |

产出：`learning-notes/rtk-ai__rtk/02-quickstart-notes.md`。

## Level 3：理解源码

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `RTK-L3-01` | Level 3 | 阅读 `src/main.rs` 的 Clap command 和 `run_cli` 路由。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `src/main.rs` 的 Clap command 和 `run_cli` 路由。 | `learning-notes/rtk-ai__rtk/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RTK-L3-02` | Level 3 | 阅读 `src/discover/rules.rs` 和 `src/discover/registry.rs` 的 rewrite rule。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `src/discover/rules.rs` 和 `src/discover/registry.rs` 的 rewrite rule。 | `learning-notes/rtk-ai__rtk/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RTK-L3-03` | Level 3 | 阅读 `src/hooks/rewrite_cmd.rs` 的 exit code contract。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `src/hooks/rewrite_cmd.rs` 的 exit code contract。 | `learning-notes/rtk-ai__rtk/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RTK-L3-04` | Level 3 | 阅读 `src/hooks/permissions.rs` 的 Deny / Ask / Allow 优先级。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `src/hooks/permissions.rs` 的 Deny / Ask / Allow 优先级。 | `learning-notes/rtk-ai__rtk/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RTK-L3-05` | Level 3 | 阅读 `src/core/runner.rs` 的 captured / streamed / passthrough 执行模式。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `src/core/runner.rs` 的 captured / streamed / passthrough 执行模式。 | `learning-notes/rtk-ai__rtk/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RTK-L3-06` | Level 3 | 选择 `src/cmds/git/git.rs`、`src/cmds/rust/cargo_cmd.rs`、`src/cmds/python/pytest_cmd.rs` 各做一条调用链。 | 已固定源码 commit 或公开源码视图日期 | 选择 `src/cmds/git/git.rs`、`src/cmds/rust/cargo_cmd.rs`、`src/cmds/python/pytest_cmd.rs` 各做一条调用链。 | `learning-notes/rtk-ai__rtk/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RTK-L3-07` | Level 3 | 阅读 `src/core/tracking.rs`、`src/core/tee.rs` 和 `src/core/telemetry.rs`。 | 已固定源码 commit 或公开源码视图日期 | 阅读 `src/core/tracking.rs`、`src/core/tee.rs` 和 `src/core/telemetry.rs`。 | `learning-notes/rtk-ai__rtk/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `RTK-L3-08` | Level 3 | 画出 hook rewrite、command filter 和 tracking / telemetry 三张图。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |

产出：`learning-notes/rtk-ai__rtk/04-source-reading-notes.md` 和调用链图。

## Level 4：完成集成

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `RTK-L4-01` | Level 4 | 在隔离配置目录验证 `rtk init --codex` 或目标 Agent 等价路径。 | 已有运行证据，或已明确集成验证边界 | 在隔离配置目录验证 `rtk init --codex` 或目标 Agent 等价路径。 | `learning-notes/rtk-ai__rtk/05-integration-notes.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `RTK-L4-02` | Level 4 | 记录实际写入文件、备份文件和回滚命令。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/05-integration-notes.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `RTK-L4-03` | Level 4 | 对 Claude Code 或 Cursor 单独验证 transparent hook。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/05-integration-notes.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `RTK-L4-04` | Level 4 | 对 Codex 验证 prompt-level guidance 是否被读取，以及是否需要显式 `rtk`。 | 已有运行证据，或已明确集成验证边界 | 对 Codex 验证 prompt-level guidance 是否被读取，以及是否需要显式 `rtk`。 | `learning-notes/rtk-ai__rtk/05-integration-notes.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `RTK-L4-05` | Level 4 | 为团队常用命令写一份“何时用 RTK，何时读 raw output”的规则。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/05-integration-notes.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `RTK-L4-06` | Level 4 | 验证 `exclude_commands` 和 `transparent_prefixes` 配置。 | 已有运行证据，或已明确集成验证边界 | 验证 `exclude_commands` 和 `transparent_prefixes` 配置。 | `learning-notes/rtk-ai__rtk/05-integration-notes.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |

产出：`learning-notes/rtk-ai__rtk/05-integration-notes.md`。

## Level 5：改造扩展

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `RTK-L5-01` | Level 5 | 新增一个自定义 TOML filter，并验证 trust / config 行为。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `RTK-L5-02` | Level 5 | 为一个团队 CI 命令设计 filtered output 与 raw output 双路径。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `RTK-L5-03` | Level 5 | 对一个真实失败测试比较 raw output、RTK output 和人工摘要。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `RTK-L5-04` | Level 5 | 编写一个小脚本统计 RTK 前后的 token 估算差异。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `RTK-L5-05` | Level 5 | 评估 telemetry 默认关闭、opt-in 和本地 tracking 的团队合规要求。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |

产出：改造总结和可复用经验。

## Level 6：总结评价

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `RTK-L6-01` | Level 6 | 写出 RTK 的优势和限制。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `RTK-L6-02` | Level 6 | 写出适用和不适用场景。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `RTK-L6-03` | Level 6 | 与 Caveman、Graphify、CodeGraph、普通 shell alias 和 CI log folding 对比。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `RTK-L6-04` | Level 6 | 总结可借鉴设计：thin hook delegate、central registry、fail-open、tee recovery、permission precedence。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `RTK-L6-05` | Level 6 | 生成复习问题。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/rtk-ai__rtk/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/rtk-ai__rtk/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |

产出：`learning-notes/rtk-ai__rtk/07-reflection.md` 和 `review-questions.md`。


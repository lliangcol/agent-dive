# CodeGraph Learning Todo List

本清单已经迁移为可执行任务表。每个任务必须同步更新学习笔记、`evidence.md` 和 `learning-notes/colbymchenry__codegraph/progress.json`；未验证内容保持未完成。

## Level 1：了解项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [x] | `CODEGRAPH-L1-01` | Level 1 | 阅读 README 和官方文档。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/README.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [x] | `CODEGRAPH-L1-02` | Level 1 | 用一句话说明项目定位。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/README.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [x] | `CODEGRAPH-L1-03` | Level 1 | 说明项目解决的问题。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/README.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [x] | `CODEGRAPH-L1-04` | Level 1 | 判断项目适合什么场景。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/README.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [x] | `CODEGRAPH-L1-05` | Level 1 | 记录第一印象和待验证问题。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/README.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |

产出：`learning-notes/colbymchenry__codegraph/README.md`。

## Level 2：跑通项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [x] | `CODEGRAPH-L2-01` | Level 2 | 安装 CLI，记录安装方式和版本。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/02-quickstart-notes.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [x] | `CODEGRAPH-L2-02` | Level 2 | 在一个可公开测试仓库执行 `codegraph init -i`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 在一个可公开测试仓库执行 `codegraph init -i`。 | `learning-notes/colbymchenry__codegraph/02-quickstart-notes.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [x] | `CODEGRAPH-L2-03` | Level 2 | 执行 `codegraph status`，记录文件数、节点数、边数。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `codegraph status`，记录文件数、节点数、边数。 | `learning-notes/colbymchenry__codegraph/02-quickstart-notes.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [x] | `CODEGRAPH-L2-04` | Level 2 | 执行 `codegraph query`、`codegraph callers`、`codegraph impact`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `codegraph query`、`codegraph callers`、`codegraph impact`。 | `learning-notes/colbymchenry__codegraph/02-quickstart-notes.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [x] | `CODEGRAPH-L2-05` | Level 2 | 在 Agent 中确认 MCP tools 可用。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/02-quickstart-notes.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |

产出：`learning-notes/colbymchenry__codegraph/02-quickstart-notes.md`。

## Level 3：理解源码

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [x] | `CODEGRAPH-L3-01` | Level 3 | 找到 CLI 入口 `src/bin/codegraph.ts`。 | 已固定源码 commit 或公开源码视图日期 | 找到 CLI 入口 `src/bin/codegraph.ts`。 | `learning-notes/colbymchenry__codegraph/04-source-reading-notes.md` 和调用链图; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [x] | `CODEGRAPH-L3-02` | Level 3 | 找到核心 facade `src/index.ts`。 | 已固定源码 commit 或公开源码视图日期 | 找到核心 facade `src/index.ts`。 | `learning-notes/colbymchenry__codegraph/04-source-reading-notes.md` 和调用链图; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [x] | `CODEGRAPH-L3-03` | Level 3 | 找到 MCP 工具定义 `src/mcp/tools.ts`。 | 已固定源码 commit 或公开源码视图日期 | 找到 MCP 工具定义 `src/mcp/tools.ts`。 | `learning-notes/colbymchenry__codegraph/04-source-reading-notes.md` 和调用链图; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [x] | `CODEGRAPH-L3-04` | Level 3 | 找到索引提取逻辑 `src/extraction/`。 | 已固定源码 commit 或公开源码视图日期 | 找到索引提取逻辑 `src/extraction/`。 | `learning-notes/colbymchenry__codegraph/04-source-reading-notes.md` 和调用链图; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [x] | `CODEGRAPH-L3-05` | Level 3 | 找到图存储 schema `src/db/schema.sql`。 | 已固定源码 commit 或公开源码视图日期 | 找到图存储 schema `src/db/schema.sql`。 | `learning-notes/colbymchenry__codegraph/04-source-reading-notes.md` 和调用链图; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `CODEGRAPH-L3-06` | Level 3 | 深读 `findRelevantContext()` 和 `buildContext()` 的排序/预算策略。 | 已固定源码 commit 或公开源码视图日期 | 深读 `findRelevantContext()` 和 `buildContext()` 的排序/预算策略。 | `learning-notes/colbymchenry__codegraph/04-source-reading-notes.md` 和调用链图; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `CODEGRAPH-L3-07` | Level 3 | 深读一个语言 extractor，例如 TypeScript 或 Python。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/04-source-reading-notes.md` 和调用链图; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `CODEGRAPH-L3-08` | Level 3 | 深读一个 framework resolver，例如 Express、Django 或 Spring。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/04-source-reading-notes.md` 和调用链图; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |

产出：`learning-notes/colbymchenry__codegraph/04-source-reading-notes.md` 和调用链图。

## Level 4：完成集成

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `CODEGRAPH-L4-01` | Level 4 | 选择一个本地中型仓库作为测试项目。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/05-integration-notes.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `CODEGRAPH-L4-02` | Level 4 | 运行 `codegraph init -i` 并记录索引耗时。 | 已有运行证据，或已明确集成验证边界 | 运行 `codegraph init -i` 并记录索引耗时。 | `learning-notes/colbymchenry__codegraph/05-integration-notes.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `CODEGRAPH-L4-03` | Level 4 | 在 Codex 或 Claude Code 中通过 MCP 查询同一问题。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/05-integration-notes.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `CODEGRAPH-L4-04` | Level 4 | 对比 CodeGraph 查询与普通 `rg` / 文件读取的上下文质量。 | 已有运行证据，或已明确集成验证边界 | 对比 CodeGraph 查询与普通 `rg` / 文件读取的上下文质量。 | `learning-notes/colbymchenry__codegraph/05-integration-notes.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `CODEGRAPH-L4-05` | Level 4 | 记录权限配置、PATH、watcher、sync 的问题。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/05-integration-notes.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |

产出：`learning-notes/colbymchenry__codegraph/05-integration-notes.md`。

## Level 5：改造扩展

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `CODEGRAPH-L5-01` | Level 5 | 增加一个小型 fixtures 项目，观察新增语言/框架测试方式。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `CODEGRAPH-L5-02` | Level 5 | 阅读 `__tests__/frameworks.test.ts` 和 MCP 相关测试。 | 已理解最小集成路径；使用沙箱或只输出设计 | 阅读 `__tests__/frameworks.test.ts` 和 MCP 相关测试。 | 改造总结和可复用经验; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `CODEGRAPH-L5-03` | Level 5 | 分析如何新增一个 Agent target。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `CODEGRAPH-L5-04` | Level 5 | 分析如何新增一个 MCP tool 或调整 tool guidance。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `CODEGRAPH-L5-05` | Level 5 | 评估 `.codegraph/` 是否适合 CI 缓存。 | 已理解最小集成路径；使用沙箱或只输出设计 | 评估 `.codegraph/` 是否适合 CI 缓存。 | 改造总结和可复用经验; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |

产出：改造总结和可复用经验。

## Level 6：总结评价

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `CODEGRAPH-L6-01` | Level 6 | 写出项目优点和缺点。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/07-reflection.md` 和 `review-questions.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `CODEGRAPH-L6-02` | Level 6 | 写出适用和不适用场景。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/07-reflection.md` 和 `review-questions.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `CODEGRAPH-L6-03` | Level 6 | 与 `codebase-memory-mcp`、Sourcegraph Cody 或其他代码索引工具对比。 | 前序笔记和证据已更新 | 与 `codebase-memory-mcp`、Sourcegraph Cody 或其他代码索引工具对比。 | `learning-notes/colbymchenry__codegraph/07-reflection.md` 和 `review-questions.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `CODEGRAPH-L6-04` | Level 6 | 总结 MCP 工具设计经验。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/07-reflection.md` 和 `review-questions.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `CODEGRAPH-L6-05` | Level 6 | 生成复习问题。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/colbymchenry__codegraph/07-reflection.md` 和 `review-questions.md`; projects/mcp-tools/colbymchenry__codegraph/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |

产出：`learning-notes/colbymchenry__codegraph/07-reflection.md` 和 `review-questions.md`。

## 复习问题

1. CodeGraph 为什么要先索引再给 Agent 查询，而不是让 Agent 每次 grep/read？
2. `nodes`、`edges`、`files`、`unresolved_refs` 分别解决什么问题？
3. `codegraph_explore` 和 `codegraph_search` 的适用场景有什么区别？
4. watcher、catch-up sync、manual sync 分别覆盖哪些 freshness 场景？
5. 安装器为什么要区分 Claude、Codex、Cursor 等 target？
6. 静态知识图谱在动态语言和运行时框架中有哪些天然限制？


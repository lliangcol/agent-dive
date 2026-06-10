# Graphify Learning Todo List

本清单已经迁移为可执行任务表。每个任务必须同步更新学习笔记、`evidence.md` 和 `learning-notes/safishamsi__graphify/progress.json`；未验证内容保持未完成。

## Level 1：了解项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `GRAPHIFY-L1-01` | Level 1 | 阅读 README、`ARCHITECTURE.md`、`SECURITY.md` 和 `docs/how-it-works.md`。 | 项目 README 或官方文档可访问 | 阅读 README、`ARCHITECTURE.md`、`SECURITY.md` 和 `docs/how-it-works.md`。 | `learning-notes/safishamsi__graphify/01-first-impression.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `GRAPHIFY-L1-02` | Level 1 | 用一句话说明 Graphify 与普通 grep、RAG、静态分析工具的区别。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/01-first-impression.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `GRAPHIFY-L1-03` | Level 1 | 说明 `graph.html`、`GRAPH_REPORT.md`、`graph.json` 分别服务谁。 | 项目 README 或官方文档可访问 | 说明 `graph.html`、`GRAPH_REPORT.md`、`graph.json` 分别服务谁。 | `learning-notes/safishamsi__graphify/01-first-impression.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `GRAPHIFY-L1-04` | Level 1 | 列出支持的助手平台，并标注自己最关心的 Codex / Claude Code 路径。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/01-first-impression.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |
| [ ] | `GRAPHIFY-L1-05` | Level 1 | 记录第一印象和待验证问题。 | 项目 README 或官方文档可访问 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/01-first-impression.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录文档缺失或访问失败，保持任务未完成 | yes |

产出：`learning-notes/safishamsi__graphify/01-first-impression.md`。

## Level 2：跑通项目

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `GRAPHIFY-L2-01` | Level 2 | 准备 Python 3.10+ 和 `uv`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 准备 Python 3.10+ 和 `uv`。 | `learning-notes/safishamsi__graphify/02-quickstart-notes.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `GRAPHIFY-L2-02` | Level 2 | 执行 `uv tool install graphifyy`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 执行 `uv tool install graphifyy`。 | `learning-notes/safishamsi__graphify/02-quickstart-notes.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `GRAPHIFY-L2-03` | Level 2 | 在一个公开小仓库执行 `graphify .`。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 在一个公开小仓库执行 `graphify .`。 | `learning-notes/safishamsi__graphify/02-quickstart-notes.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `GRAPHIFY-L2-04` | Level 2 | 打开 `graphify-out/graph.html`，检查图谱是否非空。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 打开 `graphify-out/graph.html`，检查图谱是否非空。 | `learning-notes/safishamsi__graphify/02-quickstart-notes.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `GRAPHIFY-L2-05` | Level 2 | 阅读 `graphify-out/GRAPH_REPORT.md`，记录报告是否能帮助定位模块。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 阅读 `graphify-out/GRAPH_REPORT.md`，记录报告是否能帮助定位模块。 | `learning-notes/safishamsi__graphify/02-quickstart-notes.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `GRAPHIFY-L2-06` | Level 2 | 查询或检查 `graphify-out/graph.json`，确认节点和边的大致结构。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 查询或检查 `graphify-out/graph.json`，确认节点和边的大致结构。 | `learning-notes/safishamsi__graphify/02-quickstart-notes.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |
| [ ] | `GRAPHIFY-L2-07` | Level 2 | 记录命令、耗时、输出和错误。 | 使用 `.cache/` 或临时环境；避免写入全局配置 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/02-quickstart-notes.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录命令、退出码和 stderr 摘要；如需密钥或全局写入则停止 | guarded |

产出：`learning-notes/safishamsi__graphify/02-quickstart-notes.md`。

## Level 3：理解源码

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `GRAPHIFY-L3-01` | Level 3 | 找到 `graphify` CLI 入口和命令分发。 | 已固定源码 commit 或公开源码视图日期 | 找到 `graphify` CLI 入口和命令分发。 | `learning-notes/safishamsi__graphify/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `GRAPHIFY-L3-02` | Level 3 | 找到文件扫描与 ignore 规则。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `GRAPHIFY-L3-03` | Level 3 | 找到 Tree-sitter parser 注册和代码结构抽取逻辑。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `GRAPHIFY-L3-04` | Level 3 | 找到 semantic extraction 与 backend 配置逻辑。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `GRAPHIFY-L3-05` | Level 3 | 找到图构建、社区发现、查询和导出逻辑。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `GRAPHIFY-L3-06` | Level 3 | 找到 `graphify-mcp` server 入口和工具定义。 | 已固定源码 commit 或公开源码视图日期 | 找到 `graphify-mcp` server 入口和工具定义。 | `learning-notes/safishamsi__graphify/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `GRAPHIFY-L3-07` | Level 3 | 找到 Codex / Claude Code install 写入逻辑。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |
| [ ] | `GRAPHIFY-L3-08` | Level 3 | 画出 CLI 构建图谱的关键调用链。 | 已固定源码 commit 或公开源码视图日期 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/04-source-reading-notes.md` 和调用链图; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 记录未解析路径或推测边界，保持任务 pending | yes |

产出：`learning-notes/safishamsi__graphify/04-source-reading-notes.md` 和调用链图。

## Level 4：完成集成

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `GRAPHIFY-L4-01` | Level 4 | 在测试仓库执行 `graphify install --project --platform codex`。 | 已有运行证据，或已明确集成验证边界 | 在测试仓库执行 `graphify install --project --platform codex`。 | `learning-notes/safishamsi__graphify/05-integration-notes.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `GRAPHIFY-L4-02` | Level 4 | 检查写入文件，确认是否只影响预期路径。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/05-integration-notes.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `GRAPHIFY-L4-03` | Level 4 | 在 Codex 中提出一个代码定位问题，记录是否能走图谱查询。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/05-integration-notes.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `GRAPHIFY-L4-04` | Level 4 | 安装 `graphifyy[mcp]` 并尝试 MCP server。 | 已有运行证据，或已明确集成验证边界 | 安装 `graphifyy[mcp]` 并尝试 MCP server。 | `learning-notes/safishamsi__graphify/05-integration-notes.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `GRAPHIFY-L4-05` | Level 4 | 对比“直接 grep / 读文件”和“图谱查询”的上下文大小与准确性。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/05-integration-notes.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |
| [ ] | `GRAPHIFY-L4-06` | Level 4 | 记录回滚或卸载命令。 | 已有运行证据，或已明确集成验证边界 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/05-integration-notes.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 在写入全局配置前停止，记录回滚缺口和阻塞原因 | manual-confirm |

产出：`learning-notes/safishamsi__graphify/05-integration-notes.md`。

## Level 5：改造扩展

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `GRAPHIFY-L5-01` | Level 5 | 为一个小型仓库设计自定义 Graphify 使用规范。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `GRAPHIFY-L5-02` | Level 5 | 增加一条安全规则：禁止对敏感 docs、PDF、图片等非代码材料做 semantic extraction，或强制使用本地 backend。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `GRAPHIFY-L5-03` | Level 5 | 尝试只使用本地 backend 或无外发路径。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `GRAPHIFY-L5-04` | Level 5 | 对 Graphify 输出补一条质量检查脚本或手工 checklist。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |
| [ ] | `GRAPHIFY-L5-05` | Level 5 | 比较 JSON 输出和 MCP 查询结果，评估是否适合接入本地知识库。 | 已理解最小集成路径；使用沙箱或只输出设计 | 按任务描述执行并记录结果 | 改造总结和可复用经验; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 不修改生产配置；记录仅设计结论或阻塞原因 | manual-confirm |

产出：改造总结和可复用经验。

## Level 6：总结评价

| 状态 | task_id | Level | 目标 | 前置条件 | 操作 / 命令 | 预期证据 | 完成标准 | 失败处理 | Agent 自动执行 |
|---|---|---|---|---|---|---|---|---|---|
| [ ] | `GRAPHIFY-L6-01` | Level 6 | 写出 Graphify 的优势和限制。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `GRAPHIFY-L6-02` | Level 6 | 写出适用和不适用场景。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `GRAPHIFY-L6-03` | Level 6 | 与 codebase-memory-mcp、RepoWiki、普通 RAG 和传统静态分析工具对比。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `GRAPHIFY-L6-04` | Level 6 | 总结可借鉴设计：图谱输出、助手集成、hook 提醒、MCP 查询、数据边界。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |
| [ ] | `GRAPHIFY-L6-05` | Level 6 | 生成复习问题。 | 前序笔记和证据已更新 | 按任务描述执行并记录结果 | `learning-notes/safishamsi__graphify/07-reflection.md` 和 `review-questions.md`; projects/agentic-coding/safishamsi__graphify/evidence.md | 学习笔记包含结论、依据和未解决问题，且 progress.json 与任务状态一致 | 明确说明证据缺口，不声明学习已完成 | yes |

产出：`learning-notes/safishamsi__graphify/07-reflection.md` 和 `review-questions.md`。


# Ponytail Learning Todo List

## 任务说明

本 TODO 面向后续学习和验证，不把未执行的安装、benchmark 或宿主行为写成事实。当前项目状态为 `analyzing`，已完成收录资料但未进入 `study-ready`。

| 状态 | Task ID | 等级 | 主题 | 任务 | 验证方式 | 产出 | 依赖 | 风险 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| [x] | `PTL-L1-01` | L1 | 元数据 | 复核 GitHub API 元数据和 latest release | GitHub API 与 `git ls-remote` | 更新 `meta.json` | 网络 | 数字漂移 | 已复核 2026-06-25 |
| [ ] | `PTL-L1-02` | L1 | 定位 | 阅读 README 和 AGENTS 规则 | 源码快照 | 一页摘要 | 无 | 只看营销文案 | 标注 benchmark 边界 |
| [ ] | `PTL-L1-03` | L1 | License | 复核 LICENSE 与 manifest license | 文件阅读 | license 结论 | 无 | manifest 漂移 | MIT |
| [ ] | `PTL-L1-04` | L1 | 文件树 | 生成隐藏目录完整文件树 | `rg --files --hidden` | 模块地图 | 无 | 漏掉 dot dir | 已知核心在隐藏目录 |
| [ ] | `PTL-L2-01` | L2 | Skill | 阅读 `skills/ponytail/SKILL.md` | 文件阅读 | 规则拆解 | 无 | 误读强度模式 | 关注边界 |
| [ ] | `PTL-L2-02` | L2 | Commands | 阅读 review、audit、debt、help skills | 文件阅读 | 命令能力表 | L2-01 | 误把 review 当修复 | commands 只报告 |
| [ ] | `PTL-L2-03` | L2 | Adapter | 阅读 `docs/agent-portability.md` | 文件阅读 | 宿主映射表 | L1-04 | 适配状态漂移 | 关注 thin adapter |
| [x] | `PTL-L2-04` | L2 | Manifest | 比较 Codex、Claude、Copilot manifests | 文件阅读 | manifest 对比 | L1-04 | 版本差异 | 2026-06-25 确认为 4.8.3 一致 |
| [ ] | `PTL-L2-05` | L2 | Hook | 阅读 `hooks/claude-codex-hooks.json` 与 `hooks/copilot-hooks.json` | 文件阅读 | hook 事件表 | L1-04 | 宿主协议误判 | 区分 SessionStart、UserPromptSubmit 和 SubagentStart |
| [ ] | `PTL-L2-06` | L2 | Benchmark | 阅读 `benchmarks/README.md` | 文件阅读 | benchmark 方法摘要 | 无 | 泛化结论 | 标注 Claude scope |
| [ ] | `PTL-L3-01` | L3 | Config | 追踪 `getDefaultMode` 调用链 | 源码阅读 | 配置优先级图 | L2-05 | 用户级路径风险 | 覆盖 Windows |
| [ ] | `PTL-L3-02` | L3 | Instructions | 追踪 `getPonytailInstructions` 调用链 | 源码阅读 | 注入流程图 | L2-01 | fallback 误判 | 区分模式过滤 |
| [ ] | `PTL-L3-03` | L3 | Runtime | 追踪 Codex、Copilot、Claude 输出分支 | 源码阅读 | payload 对比 | L2-05 | 环境变量冲突 | Copilot 优先 |
| [ ] | `PTL-L3-04` | L3 | Mode | 追踪 `/ponytail` prompt 解析 | 源码阅读和单测 | mode 状态表 | L3-03 | 同轮切换差异 | 覆盖 off |
| [ ] | `PTL-L3-05` | L3 | OpenCode | 阅读 OpenCode plugin transform | 源码阅读 | OpenCode 集成笔记 | L2-03 | 路径解析风险 | 注意 ESM bridge |
| [ ] | `PTL-L3-06` | L3 | Pi | 阅读 Pi extension lifecycle | 源码阅读 | Pi 集成笔记 | L2-03 | 未跑真实 harness | 已有单测 |
| [ ] | `PTL-L3-07` | L3 | Tests | 阅读 Windows hook regression | 源码阅读和测试 | Windows 风险说明 | L2-05 | PowerShell 语法 | 已有聚焦测试 |
| [x] | `PTL-L4-01` | L4 | Static Gate | 运行 rule-copy 检查 | `node scripts/check-rule-copies.js` | evidence 更新 | Node | 上游新增规则 | 2026-06-25 通过 |
| [x] | `PTL-L4-02` | L4 | Focus Tests | 跑 hook、adapter、OpenCode、OpenClaw 聚焦测试 | `node --test ...` | evidence 更新 | Node | 测试集合漏项 | full `npm test` 覆盖并通过 |
| [x] | `PTL-L4-03` | L4 | Pi Tests | 跑 Pi extension 测试 | `npm test --prefix pi-extension` | evidence 更新 | Node | 真实 harness 未覆盖 | 2026-06-25 15/15 通过 |
| [x] | `PTL-L4-04` | L4 | Full Tests | 用临时 venv 安装 pandas 后跑 `npm test` | npm test | tests_status 判断 | pandas | 依赖污染 | 2026-06-25 61/61 + 15/15 通过 |
| [ ] | `PTL-L4-05` | L4 | Codex Smoke | 在测试 profile 安装 Codex plugin | 手动安装和 hook 审核 | Codex smoke 记录 | Codex | 写用户配置 | 不碰主力 profile |
| [ ] | `PTL-L4-06` | L4 | Claude Smoke | 用临时 `CLAUDE_CONFIG_DIR` 验证 hook | hook 输出和状态文件 | Claude smoke 记录 | Claude Code | statusline 修改 | 不写真实 settings |
| [ ] | `PTL-L4-07` | L4 | OpenCode Smoke | 加载 `.opencode/plugins/ponytail.mjs` | OpenCode session | OpenCode smoke 记录 | OpenCode | 插件 API 漂移 | 可选 |
| [ ] | `PTL-L5-01` | L5 | Benchmark | 复现 Claude 小样本 promptfoo | promptfoo repeat | 结果表 | API key | 成本 | 明确模型和日期 |
| [ ] | `PTL-L5-02` | L5 | Correctness | 单独检查 correctness gate 覆盖 | Node/Python | gate 风险说明 | pandas | 结构性检查不足 | React 和 FastAPI 不是完整运行 |
| [ ] | `PTL-L5-03` | L5 | Cost Claim | 对比 Claude 与 OpenAI 文档结论 | benchmark 文档和复现 | 成本边界说明 | L5-01 | 泛化错误 | 不写绝对承诺 |
| [ ] | `PTL-L5-04` | L5 | Comparison | 与 Caveman、RTK、Claude HUD 对比 | AgentDive 资料 | 对比表 | 既有项目 | 概念混淆 | 区分输出压缩和运行观测 |
| [ ] | `PTL-L5-05` | L5 | Security | 评估 hooks 的读取和写入范围 | 源码和 smoke | 安全边界 | L4-05 | prompt payload 敏感 | 写治理建议 |
| [ ] | `PTL-L6-01` | L6 | Study Ready | 根据证据更新项目状态 | check 脚本 | 状态调整 PR | L4 全部 | 过早升级 | runtime pass 才能 study-ready |
| [ ] | `PTL-L6-02` | L6 | Docs Polish | 回填英文镜像或对比文章 | 文档审阅 | 后续资料 | L5-04 | 范围扩大 | 非本次必须 |
| [ ] | `PTL-L6-03` | L6 | Final Review | 完成复习题和反思 | 学习笔记 | 学习闭环 | L6-01 | 证据不足 | 不伪造成 completed |

## 进度统计

- 已完成：6
- 总任务：32
- 当前阶段：最新快照本地测试已通过，等待隔离宿主验证。

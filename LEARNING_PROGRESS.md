# Learning Progress

本文件记录全局学习进度总览。单个项目的详细学习笔记和进度应放在 `learning-notes/<owner__repo>/`。

## 总体学习状态

- 当前阶段：首批项目质量治理和学习闭环验证阶段
- 当前重点：统一 Hermes Agent、ECC、Ruflo、Graphify、Caveman、RTK、Claude HUD、Ponytail 和 CodeGraph 的元数据、证据文件、学习 TODO 和进度记录
- 最近更新：2026-06-25
- 质量门禁：项目提升到 `study-ready`、`in-study` 或 `completed` 前必须通过 `python scripts/check-agent-dive.py`，并在 `evidence.md` 中有真实运行或源码验证记录

## 当前正在学习的项目

| 项目名称 | 项目 ID | 当前阶段 | 完成进度 | 卡住的问题 | 下一步行动 |
|---|---|---|---:|---|---|
| Hermes Agent | NousResearch__hermes-agent | analyzing | 4/36 | 尚未克隆源码，尚未本机运行安装和 `hermes doctor` | 固定 commit 后验证源码调用链和最小运行 |
| ECC | affaan-m__ECC | analyzing | 0/43 | 未运行本机 CLI；未验证 Codex plugin / Claude hooks / install 写入范围 | 先执行只读 `npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json`，再追踪 install 和 hook 调用链 |
| Ruflo | ruvnet__ruflo | analyzing | 0/39 | 未运行 CLI/init/MCP；未验证 Claude hooks、Codex `.agents` 配置和插件 marketplace 行为 | 先执行只读 `npx --yes ruflo@latest --version`、`npx --yes ruflo@latest --help`，再追踪 CLI/MCP/Swarm/Memory 调用链 |
| Graphify | safishamsi__graphify | analyzing | 0/36 | 未运行本机 CLI；未验证源码调用链；未验证 Codex install 写入范围 | 阅读官方架构和安全文档，并用公开小仓库跑 `graphify .` |
| Caveman | JuliusBrussee__caveman | analyzing | 0/35 | 未运行统一安装器 dry-run；未验证 installer、hooks、MCP shrink 和 memory compression 调用链 | 在临时克隆中执行 `node bin/install.js --list` 和 `node bin/install.js --dry-run --all` |
| RTK | rtk-ai__rtk | analyzing | 0/36 | 未安装本机 binary；未验证 `rtk rewrite`、过滤输出、hook 写入和 token savings 统计 | 在临时环境执行 `rtk rewrite "git status"`，再验证 `rtk git status`、tee recovery 和目标 Agent 集成 |
| Claude HUD | jarrodwatts__claude-hud | analyzing | 0/35 | 未在真实 Claude Code 中安装 plugin / setup；Windows 临时 `npm test` 当前失败 | 先用临时 `CLAUDE_CONFIG_DIR` 验证 setup 写入，再定位 Windows 测试失败组 |
| Ponytail | DietrichGebert__ponytail | analyzing | 6/32 | 未在真实 Codex / Claude Code 中安装 plugin；promptfoo benchmark 未复现；真实 SubagentStart 注入未做宿主验证 | 先做隔离 Codex / Claude plugin smoke，并验证 SubagentStart hook 注入 |
| CodeGraph | colbymchenry__codegraph | analyzing | 15/33 | 已完成缓存克隆、构建、CLI version/help、`init -i`、`status`、query/callers/impact、MCP initialize/tools-list 和一个聚焦测试；完整测试仍未验证 | 继续 Level 3 源码阅读，并确认完整测试或聚焦测试子集标准 |

## 已完成项目

| 项目名称 | 项目 ID | 完成时间 | 总结链接 |
|---|---|---|---|
| - | - | - | - |

## 卡住的问题

- Hermes Agent：未完成源码函数级验证，未完成本机安装和运行验证。
- ECC：未完成 CLI dry-run、Codex plugin 加载、Claude/OpenCode hook 执行和 install 写入范围验证。
- Ruflo：未完成 CLI/init/MCP 本机运行验证，未验证 Claude Code plugin、Codex `.agents` 配置、hooks 和 Web UI。
- Graphify：未完成本机 CLI 运行、源码调用链验证和 Codex project install 写入范围验证。
- Caveman：未完成统一安装器 dry-run、单 Agent 安装 / 卸载、Claude hooks、MCP shrink、memory compression 和 benchmark 复现验证。
- RTK：未完成本机安装、`rtk rewrite` smoke、命令过滤对比、hook 写入范围、raw-output recovery 和 token savings 复现验证。
- Claude HUD：未完成真实 Claude Code plugin install、`/claude-hud:setup` 写入验证、HUD 展示验证和 Windows 测试失败定位。
- Ponytail：已在临时 venv 中补齐 pandas 并通过最新快照 `npm test`；未完成真实 Codex / Claude Code plugin install、hook 信任验证、SubagentStart 宿主验证和 promptfoo benchmark 复现。
- CodeGraph：CLI 构建、`init -i`、`status`、query/callers/impact、MCP initialize/tools-list 和一个聚焦测试已通过；未完成完整测试套件、MCP tools/call 采样和 npm audit 风险复核。

## 下一步学习建议

- [x] 至少选择 1 个 Level A 项目做深度收录样例。
- [x] 为收录项目生成项目精读、图解和 Learning Todo List。
- [x] 补齐统一 `meta.json`、`evidence.md`、`progress.json` 和结构化 Learning Todo List。
- [x] 增加 AI Agent 连续学习协议。
- [x] 增加 `python scripts/check-agent-dive.py` 一致性检查。
- [x] 对 CodeGraph 执行一次真实 CLI/MCP 最小运行验证。
- [ ] 对 CodeGraph 补充 MCP `tools/call` 采样、完整测试或认可的聚焦测试子集。
- [ ] 对 Ponytail 执行隔离 Codex / Claude plugin smoke，并验证 SubagentStart hook 注入。
- [ ] 对 RTK 执行一次隔离环境 rewrite / filter / tee smoke。
- [ ] 按学习路线补齐 Agent Loop、Tool Calling、RAG、MCP 等基础主题。

## 复习计划

| 复习主题 | 关联项目 | 计划时间 | 状态 |
|---|---|---|---|
| Agent Loop 与 Tool Calling 的边界 | - | 未安排 | 未开始 |
| RAG Agent 的检索与生成链路 | - | 未安排 | 未开始 |
| MCP 工具接入流程 | colbymchenry__codegraph | 未安排 | 已开始 |

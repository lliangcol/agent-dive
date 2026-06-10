# ECC 项目精读

## 1. 项目基本信息

- 项目名称：ECC
- 项目 ID：`affaan-m__ECC`
- GitHub：https://github.com/affaan-m/ECC
- 官方文档：https://ecc.tools
- 分类：`agentic-coding`
- 收录等级：Level A 深度收录
- 当前状态：`analyzing`
- 主要语言：JavaScript
- License：MIT
- 分析日期：2026-06-11
- 分析版本 / Commit：`c888d2b73f26d605ff6c172b433d4cad2200206f`
- 是否运行验证：否
- 分析依据：GitHub API、README、`package.json`、`docs/architecture/cross-harness.md`、`docs/releases/2.0.0/release-notes.md`、`.codex-plugin/plugin.json`、`.claude-plugin/plugin.json`、`hooks/hooks.json`、`scripts/ecc.js`、`scripts/install-plan.js`、`scripts/install-apply.js`、`scripts/lib/install-*` 首轮检查

## 2. 一句话定位

ECC 是一个跨 AI 编码 harness 的工程工作流层，把可复用的 skills、rules、hooks、commands、MCP 配置、安装器和 operator 工具打包成可在 Claude Code、Codex、OpenCode、Cursor、Gemini 等环境中迁移的 agentic coding 操作系统。

## 3. 项目解决的问题

AI 编码工具的痛点不是只有模型能力，还包括工作流资产难复用、hook 能力不一致、MCP 配置分散、skills 和 rules 在不同工具间格式不同、上下文/记忆/安全门禁缺少统一治理、多人或多 worktree agent 运行难以观测。ECC 的核心思路是把 durable workflow 放在共享源码目录中，再通过各 harness adapter 薄适配到不同运行环境。

学习价值主要在五类：

- 跨 harness 资产设计：同一套 skills、rules、commands、MCP conventions 如何映射到 Claude Code、Codex、OpenCode、Cursor 等工具。
- Agent safety gates：通过 hooks、quality gate、secret/config protection、MCP health check、session persistence 等约束 agent 行为。
- Selective install：用 manifest、profile、component、target 和 install-state 管理大规模 workflow 包。
- Operator workflows：用 sessions、status、work-items、control-pane、worktree lifecycle 支撑长期 agent 工作。
- Codex / Claude / OpenCode 对比：哪些能力是 native hook，哪些只能 instruction-backed。

## 4. 项目主线

ECC 的主线不是一个单一 Agent Loop，而是一个 harness workflow package：

1. 维护者在 `skills/`、`agents/`、`commands/`、`rules/`、`hooks/`、`mcp-configs/`、`manifests/` 中维护可复用能力。
2. 用户通过 Claude plugin、Codex plugin、OpenCode package、npm CLI 或手动安装路径选择目标 harness。
3. `ecc` CLI 根据命令分发到 `install-apply.js`、`install-plan.js`、`catalog.js`、`consult.js`、`doctor.js`、`status.js`、`control-pane.js` 等脚本。
4. 安装器解析 profile / modules / components / target，生成文件操作计划，写入对应 harness 的配置、skills、rules、commands 或 MCP 配置。
5. 支持 hook 的 harness 在工具调用、会话开始、响应停止、会话结束等阶段触发安全、质量、记忆和观测脚本；不支持 hook 的 harness 用 `AGENTS.md`、plugin manifest 和配置约定承载指令。
6. Operator 工具读取 session、state、work items、MCP inventory、worktree lifecycle 等信息，帮助长期 agent 工作可观测、可恢复、可复盘。

依据：README、cross-harness architecture 文档、`package.json` bin/scripts、`scripts/ecc.js`、`hooks/hooks.json`。

## 5. 快速开始

### 环境要求

- Node.js：`package.json` 标注 `>=18`。
- 可选：Claude Code、Codex、OpenCode、Cursor、Gemini、Zed 等目标 harness。
- 可选：Python，用于 `ecc_dashboard.py` 或其他辅助工具。

### 安装路径

README 给出多条路径，不能叠加安装：

```bash
# Claude Code plugin path, based on README
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

```bash
# npm package / selective installer path, based on package.json and README
npx --yes --package ecc-universal ecc consult "security reviews" --target claude
npx --yes --package ecc-universal ecc install --profile minimal --target claude
```

注意：README 示例使用 `npx ecc ...`，但本次复核 npm 元数据时发现 npm 上存在独立的 `ecc@0.0.2` 包。后续验证应使用 `npx --package ecc-universal ecc ...`，或在 clone 后使用 `node scripts/ecc.js ...`。

```powershell
# Windows manual installer path, based on README
.\install.ps1 --profile minimal --target claude
```

### 最小验证建议

本次没有执行安装。后续真实验证应先跑只读或 dry-run 路径：

```bash
npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json
npx --yes --package ecc-universal ecc consult "code review and security" --target codex
npx --yes --package ecc-universal ecc doctor
```

### 已知限制

- Codex 当前没有 Claude-style hook parity。ECC README 和 cross-harness 文档都把 Codex 路径描述为 instruction-backed。
- Full profile 可能向用户目录或项目目录写入大量文件，验证前应先 dry-run 并准备回滚。
- README、release notes、plugin manifest 中的公开技能数量存在可能漂移，需要用仓库脚本复核 catalog。

## 6. 核心架构

ECC 可拆成八层：

- 共享资产层：`skills/`、`agents/`、`commands/`、`rules/`、`hooks/`、`mcp-configs/`。
- Harness 适配层：`.claude-plugin/`、`.codex-plugin/`、`.codex/`、`.opencode/`、`.cursor/`、`.gemini/`、`.zed/`、`.qwen/` 等。
- CLI 分发层：`scripts/ecc.js` 把 `ecc install`、`ecc plan`、`ecc consult`、`ecc doctor`、`ecc status`、`ecc control-pane` 等命令路由到具体脚本。
- Selective install 层：`scripts/install-plan.js`、`scripts/install-apply.js`、`scripts/lib/install-manifests.js`、`scripts/lib/install-executor.js`、`scripts/lib/install/`。
- Hook runtime 层：`hooks/hooks.json`、`scripts/hooks/`、hook bootstrap 和 run-with-flags 机制。
- Operator state 层：`scripts/status.js`、`scripts/sessions-cli.js`、`scripts/work-items.js`、`scripts/worktree-lifecycle.js`、`scripts/mcp-inventory.js`。
- Control pane 层：`scripts/control-pane.js` 和 `scripts/lib/control-pane/`。
- Alpha control plane：`ecc2/`，README 和 release notes 将其描述为 2.0 alpha，不应当当作稳定公共运行时。

图解见：

- `assets/diagrams/architecture.mmd`
- `assets/diagrams/cross-harness-flow.mmd`
- `assets/diagrams/install-flow.mmd`
- `assets/diagrams/hook-lifecycle.mmd`
- `assets/diagrams/control-pane-flow.mmd`

## 7. 核心原理

### 7.1 Durable workflow 与薄适配

`docs/architecture/cross-harness.md` 明确把 `skills/` 视为最可迁移的单元，把 rules、hooks、MCP、commands、sessions 等能力放在共享层，再让各 harness 只适配加载方式、事件形状和命令映射。

### 7.2 Selective install

`package.json` 暴露 `ecc` 和 `ecc-install` bin。`scripts/install-plan.js` 负责解析 profile、modules、components、skills、target 和 config；`scripts/install-apply.js` 在解析请求后创建 install plan 并应用。首轮源码检查显示安装器有 manifest、target adapter、install-state、dry-run/json 输出等概念，但完整写入策略尚未逐项验证。

### 7.3 Hook lifecycle

`hooks/hooks.json` 覆盖 PreToolUse、PreCompact、SessionStart、PostToolUse、Stop、SessionEnd。典型用途包括 Bash preflight、配置保护、MCP health check、quality gate、frontend design warning、format/typecheck batching、session persistence、cost tracking 等。Claude/OpenCode/Cursor 等支持 hook 或 event 的 harness 可以执行；Codex 目前主要通过指令和配置约束表达。

### 7.4 Skills / agents / commands

README 和 plugin manifest 显示 ECC 将 agents、skills、commands 作为核心表面。`AGENTS.md` 提供 agent-first、TDD、security-first、plan-before-execute 等全局工作流要求；`commands/` 主要承载 legacy slash entry；`skills/` 是更长期的可迁移 workflow source。

### 7.5 Operator observability

2.0 release notes 提到 session adapters、MCP inventory、worktree lifecycle、`orch-*` orchestrator family。`package.json` 中也有 `status`、`sessions`、`work-items`、`control-pane`、`platform-audit`、`observability:ready` 等脚本入口。当前只做了文件级确认，未启动 SQLite state store 或 control pane。

## 8. 源码结构

- CLI 入口：`scripts/ecc.js`
- 安装预览：`scripts/install-plan.js`
- 安装执行：`scripts/install-apply.js`
- manifest 和 profile 解析：`scripts/lib/install-manifests.js`
- install executor：`scripts/lib/install-executor.js`
- install runtime：`scripts/lib/install/`
- hook 配置：`hooks/hooks.json`
- hook 脚本：`scripts/hooks/`
- Control pane：`scripts/control-pane.js`、`scripts/lib/control-pane/`
- 状态/会话/work item：`scripts/status.js`、`scripts/sessions-cli.js`、`scripts/work-items.js`
- MCP inventory：`scripts/mcp-inventory.js`
- Worktree lifecycle：`scripts/worktree-lifecycle.js`
- Codex 表面：`.codex-plugin/`、`.codex/`
- Claude 表面：`.claude-plugin/`、`.claude/`
- OpenCode 表面：`.opencode/`
- Cursor 表面：`.cursor/`
- 技能、agent、命令、规则：`skills/`、`agents/`、`commands/`、`rules/`
- Rust alpha control plane：`ecc2/`
- 测试目录：`tests/`
- 文档目录：`docs/`

## 9. 关键调用链

### 调用链 1：CLI 命令分发

- 触发条件：用户执行环境中已有的 `ecc <command>`、显式 npm package 形式 `npx --package ecc-universal ecc <command>`，或 clone 后执行 `node scripts/ecc.js <command>`
- 起点：`scripts/ecc.js`
- 关键步骤：解析命令 -> 查表选择脚本 -> 通过 Node 子进程执行 `install-apply.js`、`install-plan.js`、`consult.js`、`doctor.js`、`status.js` 等
- 输出：安装结果、plan、catalog、诊断、状态等
- 错误处理：首轮只确认了命令表和帮助文本，未执行错误路径
- 依据：`scripts/ecc.js`、`package.json`

### 调用链 2：Selective install plan 到 apply

- 触发条件：用户执行 `ecc plan` 或 `ecc install`
- 起点：`scripts/install-plan.js` / `scripts/install-apply.js`
- 关键步骤：解析参数 -> normalize install request -> 读取 config -> create install plan -> 解析 modules/components/target -> dry-run 或 apply
- 输出：文件操作计划、install-state、目标 harness 配置
- 错误处理：源码中有 unknown argument、unknown module、unsupported target、warnings 等概念；完整策略待运行验证
- 依据：`scripts/install-plan.js`、`scripts/install-apply.js`、`scripts/lib/install/runtime.js`、`scripts/lib/install-manifests.js`、`scripts/lib/install-executor.js`

### 调用链 3：Hook 生命周期

- 触发条件：harness 触发 PreToolUse、SessionStart、PostToolUse、Stop 等事件
- 起点：`hooks/hooks.json`
- 关键步骤：匹配 tool/event -> 调用 plugin bootstrap / run-with-flags -> 执行具体 `scripts/hooks/*.js` -> 返回阻断、警告、异步记录或 session 输出
- 输出：质量门禁、配置保护、MCP 健康检查、格式化/类型检查、会话状态保存等结果
- 错误处理：hook JSON 中为部分脚本配置 timeout、async 和 dispatcher；真实行为依赖 harness
- 依据：`hooks/hooks.json`

### 调用链 4：Control pane

- 触发条件：用户执行 `ecc control-pane` 或 `ecc-control-pane`
- 起点：`scripts/control-pane.js`
- 关键步骤：解析 host/port/db/action 参数 -> `createControlPaneServer()` -> 读取 state snapshot -> 暴露本地 HTTP UI / API -> 可选执行 allowlist action
- 输出：本地 control pane URL、state db 路径、只读或 action-enabled 状态
- 错误处理：首轮只检查了入口和 server 文件摘要，未启动服务
- 依据：`scripts/control-pane.js`、`scripts/lib/control-pane/server.js`

## 10. 集成方式

### Codex 集成

Codex 方向优先研究 `.codex-plugin/plugin.json`、`.codex/AGENTS.md`、`.codex/config.toml`、`.mcp.json`、`skills/` 和 `.agents/skills/` 的关系。已验证 `.codex-plugin/plugin.json` 的 `skills` 指向 `./skills/`；README 的 Codex 支持说明还提到 `.agents/skills/`，两者的实际加载边界需要后续在 Codex 中验证。由于 Codex 没有 Claude-style hooks，研究重点应该放在 instruction-backed 约束、plugin skill 暴露、MCP 配置和 agent role 文件。

### Claude Code 集成

Claude Code 是 ECC 的一等支持表面。学习重点是 plugin marketplace 安装、`hooks/hooks.json`、`skills/`、`commands/`、`rules/`、`CLAUDE.md` / `AGENTS.md` 的加载关系，以及 hook 对 Bash/Edit/Stop/SessionStart 的影响。

### OpenCode / Cursor 集成

OpenCode 有 plugin/event 体系，Cursor 有自己的 rule/hook layout。两者适合用来对比“共享 workflow source”和“harness adapter”的边界。

### Java / Spring Boot 关系

ECC 不是 Java/Spring Boot 框架。Java 项目中更适合作为 agent workflow package 使用：安装 Java/Spring Boot 相关 skills、rules、reviewer/build-resolver agent，再让 Claude Code、Codex 或 OpenCode 在项目中遵循这些工作流。

## 11. 问题排查

详见 [troubleshooting.md](troubleshooting.md)。首轮重点包括重复安装、full profile 造成重复 skills/hooks、Codex hook parity 误解、Node 版本、Windows PowerShell installer、全局配置写入范围、hook 阻断和 catalog 数量漂移。

## 12. 客观评价

### 优点

- 跨 harness 设计非常贴合 agentic coding 学习主题。
- 不是只给提示词，而是包含 installer、manifest、hooks、MCP、state、sessions、worktree、tests、release gate 等工程化表面。
- 对 Codex / Claude / OpenCode / Cursor 的差异有明确边界描述，适合做横向比较。
- 安全、质量、TDD、review、verification、cost/context、memory 等治理主题丰富。
- MIT License，公开仓库，源码和文档可分析。

### 缺点

- 范围很大，容易只停留在 README 复述，必须分主题拆解。
- 安装会修改用户级或项目级 agent 配置，验证成本和回滚要求高。
- Hook 行为高度依赖具体 harness，不能用一个环境的结果推断所有环境。
- README、release notes、plugin manifest 中数量表述可能存在漂移，需要 catalog 脚本复核。
- 能力与个人工作流绑定较深，学习时需要区分通用设计和作者偏好的 workflow。

### 适用场景

- 学习 AI coding harness 的工程化工作流。
- 研究 skills/rules/hooks/MCP 的跨工具迁移。
- 设计团队级 agent governance、quality gate、安全检查和 session 复盘体系。
- 对比 Claude Code、Codex、OpenCode、Cursor 的加载和执行能力。

### 不适用场景

- 只想学习单个 Agent Loop 或模型调用 SDK。
- 无法接受写入本机 agent 全局配置的受限环境。
- 需要稳定 SDK API 的生产业务依赖。
- 想不经审查地复制完整 hooks/rules/skills 到私有仓库。

## 13. Learning Todo List

详见 [learning-todo-list.md](learning-todo-list.md)。

## 14. 总结

ECC 值得作为 Level A 深度收录项目。它最有价值的不是某个单点工具，而是展示了 AI 编码工作流如何从“提示词集合”演进为跨 harness 的可安装、可诊断、可门禁、可观测的操作系统。下一轮学习应优先执行 dry-run install plan，再分别验证 Codex instruction-backed 路径和 Claude/OpenCode hook-backed 路径。

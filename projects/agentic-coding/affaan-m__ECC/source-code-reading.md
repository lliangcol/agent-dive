# ECC 源码阅读记录

## 1. 阅读目标

- 本轮要理解的问题：ECC 如何把同一套 agent workflow 资产分发到不同 AI coding harness，并通过 hooks、installer、MCP 和 operator tools 管理长期工作。
- 关联功能：CLI、selective install、hook lifecycle、Codex plugin、Claude plugin、OpenCode adapter、control pane、session/worktree 状态。
- 预期产出：首轮模块地图、推荐阅读顺序、待验证调用链和后续源码深挖问题。

## 2. 源码入口

| 入口 | 路径 | 作用 | 依据 |
|---|---|---|---|
| CLI dispatcher | `scripts/ecc.js` | 将 `ecc install/plan/consult/doctor/status/control-pane` 等命令路由到脚本 | `package.json` bin 和源码 |
| Install preview | `scripts/install-plan.js` | 解析 profile、modules、components、target，输出 plan | 源码 |
| Install apply | `scripts/install-apply.js` | 创建并应用 install plan，支持 dry-run/json | 源码 |
| Install manifests | `scripts/lib/install-manifests.js` | 读取 module/profile/component/target 信息 | 源码 |
| Hook manifest | `hooks/hooks.json` | 定义 PreToolUse、PostToolUse、Stop、SessionStart 等生命周期 | 源码 |
| Control pane | `scripts/control-pane.js` | 启动本地 operator control pane | 源码 |
| Codex plugin | `.codex-plugin/plugin.json` | Codex plugin 元数据、skills、MCP servers、默认 prompt | 源码 |
| Claude plugin | `.claude-plugin/plugin.json` | Claude plugin 元数据、hooks、skills、commands/rules 表面 | 源码 |
| OpenCode adapter | `.opencode/` | OpenCode commands、plugins、tools、instructions | GitHub tree |
| Alpha control plane | `ecc2/` | Rust alpha control plane | README / release notes / GitHub tree |

## 3. 模块地图

| 模块 | 路径 | 职责 | 依赖关系 |
|---|---|---|---|
| Shared skills | `skills/`、`.agents/skills/` | 可迁移 workflow 单元 | `.codex-plugin/plugin.json` 指向 `skills/`；README 的 Codex support 还提到 `.agents/skills/`，实际加载边界待验证 |
| Agents | `agents/`、`.codex/agents/`、`.opencode/prompts/agents/` | 专用 reviewer、planner、resolver 等角色 | 受不同 harness 的 agent/role 机制约束 |
| Commands | `commands/`、`.opencode/commands/` | Slash command 或兼容入口 | README 明确 `commands/` 偏 legacy shim |
| Rules | `rules/` | 语言/框架/通用规则 | 安装器按 profile/target 写入 |
| Hooks | `hooks/hooks.json`、`scripts/hooks/` | 安全、质量、记忆、上下文和 session lifecycle | Claude/OpenCode/Cursor 有执行路径；Codex instruction-backed |
| Selective installer | `scripts/install-*.js`、`scripts/lib/install-*`、`manifests/` | 计划、预览、执行、记录 install-state | 依赖 target adapter 和 manifest |
| MCP config | `.mcp.json`、`mcp-configs/`、`scripts/mcp-inventory.js` | 多 harness MCP 配置和 inventory | 依赖各 harness 原生 MCP 支持 |
| Operator tools | `scripts/status.js`、`sessions-cli.js`、`work-items.js`、`worktree-lifecycle.js` | 会话、工作项、状态、worktree 管理 | 依赖本地 state store 和 Git/GitHub 状态 |
| Control pane | `scripts/control-pane.js`、`scripts/lib/control-pane/` | 本地 dashboard / API | 读取 state snapshot，可选 allowlist actions |
| Tests and gates | `tests/`、`scripts/ci/` | 校验 catalog、commands、agents、skills、hooks、install manifests、安全 IOC | `package.json` test scripts |

## 4. 推荐阅读顺序

1. README、`docs/architecture/cross-harness.md`、`docs/releases/2.0.0/release-notes.md`，先理解项目边界。
2. `package.json`、`scripts/ecc.js`，确认 CLI 分发和可执行命令。
3. `manifests/`、`scripts/install-plan.js`、`scripts/install-apply.js`、`scripts/lib/install-manifests.js`、`scripts/lib/install-executor.js`。
4. `.codex-plugin/plugin.json`、`.claude-plugin/plugin.json`、`.opencode/README.md`、`.cursor/`，比较 adapter。
5. `hooks/hooks.json` 和 `scripts/hooks/`，按 PreToolUse -> PostToolUse -> Stop -> SessionStart 追踪。
6. `scripts/status.js`、`scripts/sessions-cli.js`、`scripts/work-items.js`、`scripts/worktree-lifecycle.js`、`scripts/control-pane.js`。
7. `tests/` 和 `scripts/ci/`，检查项目如何防止 catalog、manifest、hook 和 packaging 漂移。

## 5. 关键调用链

### 调用链 1：`ecc install` 选择性安装

- 触发条件：用户执行 `ecc install --profile <name> --target <target>`，或用显式 npm package 运行 `npx --package ecc-universal ecc install ...`。
- 起点：`scripts/ecc.js`。
- 关键步骤：命令表选择 `install-apply.js` -> `parseInstallArgs()` -> 读取可选 config -> `normalizeInstallRequest()` -> `createInstallPlanFromRequest()` -> target adapter 生成操作 -> `applyInstallPlan()`。
- 终点：目标 harness 的配置、skills、rules、commands、MCP 等文件被写入，并记录 install-state。
- 输入：profile/modules/components/skills/target/dry-run/json/config。
- 输出：human plan、JSON plan/result、install-state。
- 错误处理：源码显示有 unknown arguments、unsupported target、unknown module、warnings；真实错误文本待运行验证。
- 依据：`scripts/ecc.js`、`scripts/install-apply.js`、`scripts/lib/install/runtime.js`、`scripts/lib/install-manifests.js`、`scripts/lib/install-executor.js`。

### 调用链 2：`ecc plan` 只读预览

- 触发条件：用户执行 `ecc plan --profile <name> --target <target> --json`。
- 起点：`scripts/install-plan.js`。
- 关键步骤：解析参数 -> list profiles/modules/components 或 resolve install plan -> 输出文本/JSON。
- 终点：不修改目标文件，只返回计划。
- 输入：profile/modules/components/family/target/config/json。
- 输出：可审查的安装计划。
- 错误处理：unknown argument 或 manifest 校验错误会抛出。
- 依据：`scripts/install-plan.js`。

### 调用链 3：Claude-style hook gate

- 触发条件：Claude Code 触发工具调用、会话开始、响应停止或会话结束事件。
- 起点：`hooks/hooks.json`。
- 关键步骤：matcher 命中 Bash/Edit/Write/MultiEdit 等 -> 运行 plugin bootstrap -> `run-with-flags.js` 选择 minimal/standard/strict profile -> 执行具体 hook script。
- 终点：返回警告、阻断、异步观察、质量门禁或 session 状态保存。
- 输入：hook event payload 和当前环境变量。
- 输出：hook stdout/stderr/exit code。
- 错误处理：timeout、async、profile flags 由 hook manifest 配置；真实阻断行为待本机验证。
- 依据：`hooks/hooks.json`。

### 调用链 4：Codex instruction-backed path

- 触发条件：Codex 加载项目/plugin instructions、skills、MCP config。
- 起点：`.codex-plugin/plugin.json`、`.codex/AGENTS.md`、`.codex/config.toml`。
- 关键步骤：Codex 读取 plugin metadata 和 skills/MCP 指向 -> 使用 `AGENTS.md` / skills 约束工作流 -> MCP servers 由配置暴露。
- 终点：Agent 行为受 instructions 和工具配置影响。
- 输入：Codex app/CLI 的 plugin、skills、MCP 支持状态。
- 输出：可用 skills、MCP tools、默认 prompt 行为。
- 错误处理：Codex 无 hook parity；不能假设 `hooks/hooks.json` 会被执行。
- 依据：README、cross-harness architecture、`.codex-plugin/plugin.json`。

### 调用链 5：Control pane 本地服务

- 触发条件：用户执行 `ecc control-pane` 或 `ecc-control-pane`。
- 起点：`scripts/control-pane.js`。
- 关键步骤：parseArgs -> `createControlPaneServer()` -> listen -> 读取 state snapshot -> 可选 allowlist action。
- 终点：本地 HTTP URL 输出到终端。
- 输入：host、port、db path、state db path、allow-actions。
- 输出：本地 dashboard/API。
- 错误处理：server 入口包含 shutdown 处理；action 执行和权限待源码深读。
- 依据：`scripts/control-pane.js`、`scripts/lib/control-pane/server.js`。

## 6. 阅读笔记

- 重要发现：ECC 的核心不是单一 runtime，而是“共享工作流资产 + harness adapter + install/runtime governance”的组合。
- 重要发现：Codex 支持被明确描述为 instruction-backed，不能套用 Claude hook 模型。
- 重要发现：installer 已经不是简单 copy script，而是 manifest/profile/component/target 驱动。
- 重要发现：`package.json` test 命令覆盖 agents、commands、rules、skills、hooks、install manifests、personal path、catalog、command registry 和 tests/run-all。
- 不确定点：manifest 内 profile 和 module 的实际默认组合尚未完整枚举。
- 不确定点：`.codex-plugin/plugin.json` 的 shortDescription 数量和 README/release notes 数量可能不一致，需要跑 catalog 检查。
- 不确定点：README 示例中的 `npx ecc` 与 npm 包名 `ecc-universal` 存在解析歧义；已确认 npm 上有独立 `ecc@0.0.2` 包，验证命令应使用显式 package selector。
- 不确定点：hook bootstrap 在 Windows、Node 21+、Claude plugin cache 路径下的真实行为需要运行验证。
- 待运行验证：`npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json`。
- 待运行验证：`npm test` 或至少 catalog/manifest/hook validators。
- 待运行验证：Claude plugin 安装与卸载、Codex plugin 加载、OpenCode plugin event。

## 7. 待办检查项

- [x] 找到 CLI 入口。
- [ ] 完整追踪 install target adapter。
- [ ] 完整追踪 hook bootstrap 和 run-with-flags。
- [ ] 找到所有 MCP config 读写路径。
- [ ] 找到 state DB schema 和 session adapter 数据模型。
- [ ] 找到 worktree lifecycle 的 conflict prediction 和 cleanup 逻辑。
- [ ] 运行至少一个 dry-run plan 并记录输出。

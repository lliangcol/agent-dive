# ECC 集成指南

## 1. 集成目标

- 目标系统：本地 AI 编码工作环境，包括 Codex、Claude Code、OpenCode、Cursor。
- 目标能力：引入 ECC 的 skills、rules、MCP conventions、review/security/TDD workflow、可选 hooks 和 operator 工具。
- 集成方式：优先 dry-run / plan，确认写入范围后按目标 harness 分别集成。
- 约束条件：不叠加多种安装路径，不在敏感仓库直接 full profile，不写入密钥，不把未支持 hook 的 harness 当成 hook-backed。

## 2. 前置条件

- 运行环境：Node.js `>=18`。
- 依赖：目标 harness；可选 npm/npx；可选 Git。
- 模型或服务配置：ECC 本身不应包含密钥；MCP server 或外部服务需要用户自行配置。
- 权限要求：安装器可能写入用户目录或项目目录。执行前必须确认 target、profile、install root 和 rollback 方案。

## 3. 最小集成路径

### 3.1 Codex 只读评估路径

```bash
npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json
npx --yes --package ecc-universal ecc consult "code review security tdd" --target codex
```

验证重点：

- 输出的 selected modules 是否符合预期。
- 目标路径是否只影响 Codex 相关配置。
- 是否写入 `.codex/config.toml`、`.codex/AGENTS.md`、skills 或 MCP 引用。
- 是否没有声称启用 native hooks。

状态：未执行，本段是基于 README、`package.json`、npm metadata 和安装脚本帮助文本的待验证方案。不要直接使用 `npx ecc ...` 作为验证命令，因为 npm 上存在独立的 `ecc@0.0.2` 包。

### 3.2 Claude Code plugin 路径

```bash
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

验证重点：

- Claude plugin 是否加载 `.claude-plugin/plugin.json`。
- `hooks/hooks.json` 是否被 Claude Code 识别。
- PreToolUse、PostToolUse、Stop、SessionStart 的输出、阻断和 timeout 行为。
- 是否避免在 plugin install 后再次运行 full manual installer。

状态：未执行。

### 3.3 npm selective install 路径

```bash
npx --yes --package ecc-universal ecc consult "security reviews" --target claude
npx --yes --package ecc-universal ecc plan --profile minimal --target claude --json
npx --yes --package ecc-universal ecc install --profile minimal --target claude --dry-run
```

验证重点：

- `--dry-run` 输出是否完整列出 planned file operations。
- `install-state` 路径是否明确。
- `minimal` / `core` / `full` 等 profile 差异是否符合安全预期。
- `--without baseline:hooks` 是否能排除 hook runtime。

状态：未执行。

### 3.4 OpenCode / Cursor 路径

OpenCode 重点看 `.opencode/` 下的 plugin、commands、tools、instructions；Cursor 重点看 `.cursor/` rule 和 hook adapter。建议先在一次性测试项目中安装，不要直接作用于主力仓库。

状态：未执行。

## 4. 接口与数据流

| 输入 | 处理模块 | 输出 | 备注 |
|---|---|---|---|
| `ecc install --profile minimal --target codex` | `scripts/ecc.js` -> `install-apply.js` -> install runtime | Codex 配置、skills、MCP reference、install-state | 待运行验证 |
| `ecc plan --json` | `install-plan.js` -> manifest resolver | JSON plan | 建议作为首个验证命令 |
| Claude tool event | `hooks/hooks.json` -> hook runner -> `scripts/hooks/*.js` | 阻断、警告、异步观察、session 状态 | 仅 hook-backed harness |
| Codex plugin metadata | `.codex-plugin/plugin.json` | skills、MCP servers、default prompt | instruction-backed |
| Operator status query | `scripts/status.js` / `control-pane.js` | state snapshot / local dashboard | 待启动验证 |

## 5. Java / Spring Boot 集成关注点

- Bean 生命周期：ECC 不直接进入 Spring Bean 生命周期，适合作为外部 agent workflow。
- 配置管理：不要把 ECC 全局配置写入业务仓库前置于审查；优先项目级、最小 profile 和 dry-run。
- 权限和审计：hooks、MCP 和 shell command rules 可能影响 agent 行为，企业环境需要审计。
- 日志和链路追踪：可研究 `status`、sessions、work-items、control pane，而不是直接接入应用日志。
- 超时、重试和限流：hook manifest 中有 timeout；MCP 和外部 API 的限流需单独配置。
- 数据库或消息队列：ECC 的 state store 是 operator 层，不应混入业务数据库。

## 6. 集成风险

- 依赖版本：Node 版本、harness 版本、plugin marketplace 支持状态会影响结果。
- 模型成本：skills 和 hooks 可能增加上下文和工具调用，需监控 cost/context。
- 工具权限：hook 和 MCP 可能读取或操作本地文件，必须确认 allowlist 和 sandbox。
- 数据安全：禁止把私有 memory、token、OAuth、个人 workspace state 纳入共享仓库。
- 运行稳定性：多个安装方式叠加可能造成重复 hooks、重复 skills 或冲突配置。
- 回滚风险：必须记录 install-state、变更文件和卸载命令。

## 7. 推荐验证命令

后续建议按从低风险到高风险执行：

```bash
npx --yes --package ecc-universal ecc --help
npx --yes --package ecc-universal ecc plan --list-profiles
npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json
npx --yes --package ecc-universal ecc consult "tdd code review security" --target codex
npx --yes --package ecc-universal ecc install --profile minimal --target codex --dry-run --json
```

只有 dry-run 输出可接受后，再考虑真实 install。

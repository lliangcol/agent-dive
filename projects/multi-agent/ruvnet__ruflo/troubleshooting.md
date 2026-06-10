# Ruflo 问题排查记录

## 问题：Claude Code plugin lite 与 CLI full install 混淆

- 发现时间：2026-06-11
- 当前状态：README 级确认，运行未验证
- 影响范围：Claude Code plugin、Ruflo CLI init、MCP server、hooks

### 现象

README 将安装路径明确分为 Claude Code plugin 和 CLI install。plugin 路径只提供轻量能力，不注册完整 Ruflo MCP server；CLI install 才进入 full loop。

### 初步判断

- 可能原因：两条路径都叫 Ruflo，且仓库包含大量 plugin 和 CLI 文件。
- 风险：用户以为安装单个 plugin 后就有 `memory_store`、`swarm_init`、`agent_spawn` 等完整 MCP tools。

### 后续处理

- 分别记录 plugin lite 和 CLI full install 的文件写入和可用命令。
- 不叠加安装路径；需要叠加时先制定回滚方案。

## 问题：Codex 支持边界不清

- 发现时间：2026-06-11
- 当前状态：源码级初步确认，运行未验证
- 影响范围：Codex、`.agents/config.toml`、`.agents/skills/`、`@claude-flow/codex`

### 现象

README 有 Codex badge，npm 上存在 `@claude-flow/codex`，但当前 HEAD 未发现 `.codex-plugin/plugin.json`。仓库中更明确的 Codex 入口是 `.agents/config.toml` 和 `.agents/skills/`。

### 初步判断

- 可能原因：Codex 集成方式经历过迁移，或由 npm package 生成配置。
- 风险：误把 Claude Code plugin / hooks 当作 Codex 已支持能力。

### 后续处理

- 单独验证 Codex 是否读取 `.agents/config.toml`。
- 单独验证 `@claude-flow/codex` 的实际安装/生成内容。
- 收录资料中只写“待验证”，不写成已验证结论。

## 问题：hooks 失败不阻断

- 发现时间：2026-06-11
- 当前状态：源码级确认，运行未验证
- 影响范围：Claude Code hook-backed 场景

### 现象

`.claude-plugin/hooks/hooks.json` 的 hook command 末尾普遍带 `|| true`。注释说明 shim 会尽量 no-op，不让 CLI/install failure 阻断 Claude Code turn。

### 初步判断

- 这有利于降低 hook 故障对开发的影响。
- 但它也意味着这些 hook 不能直接当作强制阻断安全门禁。

### 后续处理

- 对安全、质量、配置保护类 hook 单独测试 stdout/stderr/exit code。
- 强安全要求应放到 CI 或支持硬阻断的 gate。

## 问题：Windows hook 与 POSIX hook 不同

- 发现时间：2026-06-11
- 当前状态：源码级确认，运行未验证
- 影响范围：Windows、PowerShell、Claude Code hooks

### 现象

`.claude-plugin/hooks/hooks.json` 注释标明该文件 POSIX-only，使用 `/bin/bash`、`jq`、`xargs`、`.sh` scripts。Windows 下由 `ruflo init` 写入 node-based 等价配置。

### 初步判断

- 不能用仓库中的 POSIX hooks.json 直接推断 Windows 行为。
- Windows 需要单独验证 init 生成的 `.claude/settings.json`。

### 后续处理

- 在 Windows 临时项目中运行 init wizard。
- 记录生成的 hook command 和脚本路径。
- 触发一个低风险 hook 做 smoke。

## 问题：MCP stdio stdout 污染

- 发现时间：2026-06-11
- 当前状态：源码级确认，运行未验证
- 影响范围：MCP server、JSON-RPC client

### 现象

`v3/@claude-flow/cli/bin/cli.js` 明确过滤或重定向部分 console 输出，避免 embedding / AgentDB / RuVector 日志污染 MCP stdout。

### 初步判断

- 这是 MCP server 常见失败点。
- 源码已有防护，但仍需真实 `mcp start` smoke。

### 后续处理

- 用 MCP client 请求 `tools/list`，确认 stdout 只有 JSON-RPC。
- 测试 parse error、unknown method 和大 payload 行为。

## 问题：能力数量和命名漂移

- 发现时间：2026-06-11
- 当前状态：待验证
- 影响范围：收录文档、学习任务、对外评价

### 现象

README、package description、plugin manifest、源码常出现 60+ agents、100+ agents、MCP tools、插件数量等表述。不同文件可能来自不同构建时间或统计口径。

### 初步判断

- 数量适合作为线索，不适合作为未经复核的事实。
- 收录资料优先描述能力类型，而不是固化具体数量。

### 后续处理

- 跑官方 inventory / verification / tool list。
- 在 collect-report 中记录“数量待复核”。

## 问题：CLI init 写入范围大

- 发现时间：2026-06-11
- 当前状态：README 级确认，运行未验证
- 影响范围：项目目录、用户 Claude/Codex 配置、MCP config

### 现象

README 明确 CLI install 会写入 `.claude/`、`.claude-flow/`、`CLAUDE.md`、helpers、settings，并注册 MCP server 和 hooks。

### 初步判断

- 直接在主力仓库执行可能污染现有 Agent 配置。
- 需要先在临时空项目验证。

### 后续处理

```bash
npx --yes ruflo@latest init --help
npx --yes ruflo@latest init wizard
```

第二条只能在临时项目中执行，并记录所有新增/修改文件。

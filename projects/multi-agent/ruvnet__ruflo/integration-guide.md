# Ruflo 集成指南

## 1. 集成目标

- 目标系统：Claude Code、Codex、本地 MCP client、临时测试项目。
- 目标能力：引入 Ruflo 的 multi-agent swarm、MCP tools、memory、skills、hooks、plugin marketplace 和可选 Web UI。
- 集成方式：先只读确认版本和 help，再在隔离项目验证 CLI init / MCP / plugin。
- 约束条件：不在主力仓库直接执行 full init；不把 Claude hooks 推断为 Codex hooks；不把 README 数量当作实测结论。

## 2. 前置条件

- Node.js `>=20.0.0`。
- npm / npx。
- 目标 harness：Claude Code 或 Codex。
- 可选：Docker / Docker Compose，用于 Web UI / mcp-bridge。
- 权限要求：CLI init 可能写入 `.claude/`、`.claude-flow/`、`CLAUDE.md`、settings、helpers 和 MCP config。必须在临时项目验证。

## 3. 最小集成路径

### 3.1 只读 CLI 评估

```bash
npx --yes ruflo@latest --version
npx --yes ruflo@latest --help
npx --yes ruflo@latest mcp start --help
npx --yes ruflo@latest init --help
```

验证重点：

- 是否需要 Node >=20。
- 是否触发模型/embedding 下载。
- `--help` 是否走 fast path，是否污染 stdout。
- 命令是否发生写入。

状态：未执行。

### 3.2 Claude Code plugin lite 路径

```bash
/plugin marketplace add ruvnet/ruflo
/plugin install ruflo-core@ruflo
/plugin install ruflo-swarm@ruflo
```

验证重点：

- 是否只暴露 slash commands、agents、skills。
- 是否没有注册完整 Ruflo MCP server。
- 是否没有安装 full hooks。
- 单个 plugin 的卸载和回滚路径。

状态：未执行。

### 3.3 CLI full init 路径

```bash
npx --yes ruflo@latest init wizard
```

验证重点：

- 写入文件清单：`.claude/`、`.claude-flow/`、`CLAUDE.md`、settings、helpers。
- MCP server 是否注册。
- hooks 是否写入，Windows 是否使用 node-based 配置。
- 能否卸载或手动回滚。

状态：未执行。必须在临时项目中验证。

### 3.4 MCP server 路径

```bash
claude mcp add ruflo -- npx ruflo@latest mcp start
```

验证重点：

- MCP tool list 是否符合文档。
- stdio stdout 是否只输出 JSON-RPC。
- 大 payload、parse error 和 unknown method 的错误处理。
- 启动成本和超时。

状态：未执行。

### 3.5 Codex 路径

优先验证 `.agents/config.toml` 中的 MCP server 与 skills：

```toml
[mcp_servers.claude-flow]
command = "npx"
args = ["-y", "@claude-flow/cli@latest"]
enabled = true
```

验证重点：

- Codex 是否读取 `.agents/config.toml`。
- `.agents/skills/swarm-orchestration`、`memory-management`、`sparc-methodology`、`security-audit` 是否被加载。
- `@claude-flow/codex` 与仓库 `.agents` 的关系。
- 不假设 `.claude-plugin/hooks/hooks.json` 会在 Codex 中执行。

状态：未执行。

## 4. 接口与数据流

| 输入 | 处理模块 | 输出 | 备注 |
|---|---|---|---|
| `ruflo --help` | `ruflo/bin/ruflo.js` -> `@claude-flow/cli` | CLI help | 待验证 |
| `ruflo mcp start` | `bin/cli.js` MCP mode -> `mcp-client.js` | JSON-RPC MCP server | 待验证 |
| `agent_spawn` MCP tool | `mcp-tools/agent-tools.ts` -> coordinator | 新 agent / metrics | 待追踪 |
| Workflow definition | `WorkflowEngine` -> `SwarmCoordinator` | `WorkflowResult` | 源码确认，运行待验证 |
| Claude tool event | `.claude-plugin/hooks/hooks.json` -> `ruflo-hook.sh` | hook side effect / no-op | POSIX hook，Windows path 待验证 |
| Codex `.agents` config | Codex loader -> MCP/skills | tools and skills | 待验证 |

## 5. Java / Spring Boot 集成关注点

- Ruflo 不是 Java/Spring Boot SDK，更适合作为外部 Agent harness 使用。
- 不应把 Ruflo state、AgentDB 或 memory 直接混入业务数据库。
- Java 项目中可把 Ruflo 用于代码审查、测试生成、架构任务拆解和文档维护，但需要独立审计 MCP/hook 权限。
- 生产团队应把强制门禁放到 CI、pre-commit 或支持强阻断的工具链中，不要只依赖 Ruflo hook 提示。

## 6. 集成风险

- CLI init 写入范围大，必须先隔离验证。
- Claude plugin lite 和 CLI full install 可能被误混用。
- Codex 支持当前需要实测，不能只看 README badge。
- MCP server 启动可能拉取 npm 包和模型/embedding 依赖，需关注超时和缓存。
- hooks 默认 `|| true`，失败不阻断；不能当作强制安全控制。
- Web UI / mcp-bridge 可能引入认证、网络、模型 provider 和数据边界问题。

## 7. 推荐验证命令

```bash
npx --yes ruflo@latest --version
npx --yes ruflo@latest --help
npx --yes ruflo@latest mcp start --help
npx --yes ruflo@latest init --help
npx --yes --package @claude-flow/cli@latest claude-flow --version
npx --yes --package @claude-flow/cli@latest claude-flow mcp start --help
```

后续在临时项目中再执行 full init，并记录全部文件变更。

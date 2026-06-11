#Ruflo integration guide

## 1. integration goal

- Target system: Claude Code, Codex, local MCP client, temporary test project.
- Target capabilities: Introducing Ruflo's multi-agent swarm, MCP tools, memory, skills, hooks, plugin marketplace and optional web UI.
- Integration method: First read-only to confirm the version and help, and then verify CLI init/MCP/plugin in the isolated project.
- Constraints: Do not directly execute full init in the main warehouse; do not infer Claude hooks as Codex hooks; do not regard the number of READMEs as actual measurement conclusions.

## 2. Preconditions

- Node.js `>=20.0.0`。
- npm / npx。
- Target harness: Claude Code or Codex.
- Optional: Docker/Docker Compose for Web UI/mcp-bridge.
- Permission requirements: CLI init may write to `.claude/`, `.claude-flow/`, `CLAUDE.md`, settings, helpers and MCP config. Must be verified in temporary projects.

## 3. Minimum integration path

### 3.1 Read-only CLI evaluation

```bash
npx --yes ruflo@latest --version
npx --yes ruflo@latest --help
npx --yes ruflo@latest mcp start --help
npx --yes ruflo@latest init --help
```

Verification key points:

- Whether Node >=20 is required.
- Whether to trigger model/embedding download.
- `--help` Whether to use fast path and whether to pollute stdout.
-Whether the command occurred or not.

Status: Not executed.

### 3.2 Claude Code plugin lite path

```bash
/plugin marketplace add ruvnet/ruflo
/plugin install ruflo-core@ruflo
/plugin install ruflo-swarm@ruflo
```

Verification key points:

- Whether to expose only slash commands, agents, skills.
- Whether the Ruflo MCP server is not fully registered.
- Whether full hooks are not installed.
- Uninstall and rollback paths for individual plugins.

Status: Not executed.

### 3.3 CLI full init path

```bash
npx --yes ruflo@latest init wizard
```

Verification key points:

- Write file list: `.claude/`, `.claude-flow/`, `CLAUDE.md`, settings, helpers.
- Whether the MCP server is registered.
- Whether hooks are written and whether Windows uses node-based configuration.
- Can it be uninstalled or rolled back manually.

Status: Not executed. Must be verified in a temporary project.

### 3.4 MCP server path

```bash
claude mcp add ruflo -- npx ruflo@latest mcp start
```

Verification key points:

- Whether the MCP tool list complies with the documentation.
- stdio stdout Whether to output only JSON-RPC.
- Error handling for large payloads, parse errors and unknown methods.
- Startup costs and timeouts.

Status: Not executed.

### 3.5 Codex path

First verify the MCP server and skills in `.agents/config.toml`:

```toml
[mcp_servers.claude-flow]
command = "npx"
args = ["-y", "@claude-flow/cli@latest"]
enabled = true
```

Verification key points:

- Whether the Codex reads `.agents/config.toml`.
- Whether `.agents/skills/swarm-orchestration`, `memory-management`, `sparc-methodology`, `security-audit` are loaded.
- `@claude-flow/codex`’s relationship with warehouse `.agents`.
- Do not assume `.claude-plugin/hooks/hooks.json` will be executed in the Codex.

Status: Not executed.

## 4. Interface and data flow

| enter | processing module | output | Remark |
|---|---|---|---|
| `ruflo --help` | `ruflo/bin/ruflo.js` -> `@claude-flow/cli` | CLI help | To be verified |
| `ruflo mcp start` | `bin/cli.js` MCP mode -> `mcp-client.js` | JSON-RPC MCP server | To be verified |
| `agent_spawn` MCP tool | `mcp-tools/agent-tools.ts` -> coordinator | new agent/metrics | To be tracked |
| Workflow definition | `WorkflowEngine` -> `SwarmCoordinator` | `WorkflowResult` | Source code confirmed, running to be verified |
| Claude tool event | `.claude-plugin/hooks/hooks.json` -> `ruflo-hook.sh` | hook side effect / no-op | POSIX hook, Windows path needs to be verified |
| Codex `.agents` config | Codex loader -> MCP/skills | tools and skills | To be verified |

## 5. Java/Spring Boot integration concerns

- Ruflo is not a Java/Spring Boot SDK and is more suitable for use as an external Agent harness.
- Ruflo state, AgentDB or memory should not be mixed directly into the business database.
- Ruflo can be used for code review, test generation, architecture task disassembly and document maintenance in Java projects, but independent audit MCP/hook permissions are required.
- Production teams should put force-gating into CI, pre-commit, or a toolchain that supports strong blocking, and don't rely solely on Ruflo hook prompts.

## 6. Integration risks

- CLI init has a large writing range and must be isolated and verified first.
- Claude plugin lite and CLI full install may be mistakenly mixed.
- Codex support currently requires actual testing, and you cannot just look at the README badge.
- MCP server startup may pull npm packages and model/embedding dependencies, so attention should be paid to timeout and caching.
- hooks default ` |  | true`, failure will not be blocked; it cannot be used as a mandatory security control.
- Web UI/mcp-bridge may introduce authentication, network, model provider and data boundary issues.

## 7. Recommended verification commands

```bash
npx --yes ruflo@latest --version
npx --yes ruflo@latest --help
npx --yes ruflo@latest mcp start --help
npx --yes ruflo@latest init --help
npx --yes --package @claude-flow/cli@latest claude-flow --version
npx --yes --package @claude-flow/cli@latest claude-flow mcp start --help
```

Subsequently, execute full init in the temporary project and record all file changes.

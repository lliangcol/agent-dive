# CodeGraph integration guide

## 1. integration goal

- Target system: AI coding agent and local code repository.
- Target capability: Let Agent use local pre-indexed code graph for search, source code exploration, call chain and impact surface analysis.
- Integration method: CLI + MCP Server; optional Node SDK embedding.
- Constraints: For this collectnot run verification, the following steps come from README, official documents and source code.

## 2. Preconditions

- Operating systems: Windows, macOS, and Linux are all supported by the README.
- CLI dependency: You can use the self-contained installer; the npm path requires Node, `package.json` is marked `>=20.0.0 <25.0.0`.
- Agent: one of Claude Code, Cursor, Codex CLI, opencode, Hermes Agent, Gemini CLI, Antigravity IDE, Kiro.
- Permission requirements: User-level or project-level Agent MCP configuration needs to be written; `.codegraph/` will be generated in the project directory.
- Security requirements: The index contains source code structures and source code fragments. Although the README is nominally run locally, it is still necessary to avoid treating `.codegraph/` as a publicly releasable asset.

## 3. Minimum integration path

### 3.1 Install CLI

```powershell
irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 | iex
```

or:

```bash
npm i -g @colbymchenry/codegraph
```

verify:

```bash
codegraph --version
```

### 3.2 Configure Agent

```bash
codegraph install
```

Non-interactive example:

```bash
codegraph install --yes
codegraph install --target=codex --yes
codegraph install --target=claude,cursor --location=local
```

Note: The source code shows that the Codex CLI target only supports global configuration.

### 3.3 Initialize project index

```bash
cd your-project
codegraph init -i
codegraph status
```

### 3.4 Agent usage path

After the Agent is started, it is configured to run by the MCP:

```bash
codegraph serve --mcp
```

Commonly used tools:

- `codegraph_explore`: Get context before understanding a region or editing.
- `codegraph_search`: Find symbol location.
- `codegraph_callers` / `codegraph_callees`: Recall the relationship.
- `codegraph_impact`: Evaluate the impact of modifications.
- `codegraph_node`: Read the source code of a single symbol or index file.
- `codegraph_files`: View the index file structure.
- `codegraph_status`: Check index health.

## 4. Interface and data flow

| enter | processing module | output | Remark |
|---|---|---|---|
| Source code files | `src/extraction/` | nodes、edges、files、unresolved refs | tree-sitter WASM and special extractor |
| unresolved refs | `src/resolution/` | calls/imports/extends/references Equilateral | best-effort static analysis |
| Agent query | `src/mcp/tools.ts` | Markdown tool results | With output budget and staleness tips |
| change file | `src/sync/` | Incremental index update | watcher or manually `sync` |
| Agent install target | `src/installer/targets/` | MCP configuration file | target differences are handled by each file |

## 5. Java/Spring Boot integration concerns

CodeGraph is not embedded in Spring Boot as a Java library. It is recommended to use it as a development-side auxiliary tool or CI auxiliary tool:

- Bean life cycle: does not involve business process beans, avoiding putting CodeGraph DB into the production application life cycle.
- Configuration management: Treat `.codegraph/` as a local development index, and decide whether to gitignore according to team policy.
- Permissions and auditing: Agent should confirm the MCP tool permission boundaries before reading source code fragments.
- Log and link tracing: CodeGraph provides static calling relationships and does not replace runtime tracing.
- Timeout, retry and current limit: The first indexing of a large warehouse may be slow, so a timeout must be set when using CI.
- Database or message queue: `.codegraph/codegraph.db` is native SQLite and should not be mixed with business databases.

## 6. Integration risks

- Dependency version: npm path is affected by Node version; README and `package.json` have different contexts for Node requirements of CLI/SDK.
- Model cost: CodeGraph itself does not call the model, but how the Agent consumes the tool results will affect the token.
- Tool permissions: MCP tools can return source code fragments, and the enterprise environment needs to specify the allowlist and audit policy.
- Data security: Index DB may contain sensitive source code symbols and fragments and should not be uploaded.
- Operational stability: watcher may not be available in some sandbox/network file systems, requiring `codegraph sync`.
- Documentation drift: The MCP Server page of site docs still has the statement "installer writes instructions". The current README and source code display instructions are provided from the MCP initialize response.

## 7. Verification Checklist

- [ ] `codegraph --version`
- [ ] `codegraph init -i`
- [ ] `codegraph status`
- See `codegraph_status` in [ ] Agent
- [ ] Run `codegraph_explore` on a symbol
- [ ] Observe the staleness banner or automatically sync after modifying the source code
- [ ] Run the project's own test/lint to confirm that CodeGraph only provides structural context and does not replace real verification

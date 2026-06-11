# CodeGraph source reading record

## 1. Reading objectives

- Issues to be understood in this round: How CodeGraph turns the code base into a local knowledge graph available to the Agent.
- Related functions: CLI initialization, indexing, MCP tools, automatic synchronization, multi-Agent installer.
- Expected output: module map, recommended reading order, key call chains and issues to be verified.

## 2. Source code entry

| Entrance | path | effect | in accordance with |
|---|---|---|---|
| CLI | `src/bin/codegraph.ts` | Define commands such as `init`, `index`, `sync`, `status`, `query`, `serve --mcp`, `install`, etc. | Source code |
| core facade | `src/index.ts` | Expose `CodeGraph` class, organize DB, extraction, parsing, graph query, watcher | Source code |
| MCP tools | `src/mcp/tools.ts` | Define MCP tools and tool processing logic such as `codegraph_explore` | Source code |
| MCP engine | `src/mcp/engine.ts` | Maintain shared CodeGraph instances, watchers, and tool handlers | Source code |
| installer | `src/installer/index.ts` | Multi-Agent detection, configuration writing and project initialization | Source code |

## 3. Module map

| module | path | Responsibilities | Dependencies |
|---|---|---|---|
| CLI | `src/bin/` | User command entry, version and runtime checks | Call `src/index.ts`, `src/installer/`, `src/mcp/` |
| Core | `src/index.ts` | Project life cycle, indexing, synchronization, search, graph query, watch | Combining DB, extraction, resolution, graph, context, sync |
| Extraction | `src/extraction/` | Scan files, language detection, tree-sitter parsing, node/edge extraction | Write QueryBuilder, relying on tree-sitter WASM |
| Resolution | `src/resolution/` | Reference resolution, import/name matching, framework resolver, callback edge | Read nodes/unresolved refs, write edges |
| DB | `src/db/` | SQLite schema, connection, query encapsulation | Shared by Core, Graph, Resolution, MCP |
| Graph | `src/graph/` | BFS/DFS, caller/callee, impact, dependency graph query | Based on QueryBuilder |
| MCP | `src/mcp/` | MCP server、tools、session、daemon、server instructions | Open CodeGraph and return Agent tool results |
| Installer | `src/installer/` | Write configurations such as Claude/Codex/Cursor/Gemini | Target implementation is located at `targets/` |
| Sync | `src/sync/` | file watcher, git hook, worktree detection | Called by Core and MCP engines |
| Tests | `__tests__/` | Unit, integration, MCP, installer, framework, security, etc. testing | Vitest |

## 4. Recommended reading order

1. `README.md`: First understand the product positioning, tool list, installation and indexing process.
2. `package.json`: Confirm the CLI bin, build command, test command, and runtime version.
3. `src/bin/codegraph.ts`: Create a global map from the CLI command entry.
4. `src/index.ts`: Understand how the `CodeGraph` class concatenates indexing, synchronization, parsing, and querying.
5. `src/extraction/grammars.ts` and `src/extraction/index.ts`: See language support, scanning rules and extraction process.
6. `src/db/schema.sql`: Look at the graph data model.
7. `src/resolution/index.ts`: Understand how unresolved refs become cross-file edges.
8. `src/mcp/tools.ts` and `src/mcp/server-instructions.ts`: Understand how the Agent consumes the graph.
9. `src/installer/targets/`: Understand the configuration differences of different Agents.
10. `__tests__/integration/` and MCP related tests: verify implementation assumptions.

## 5. Key call chain

### Call chain 1: `codegraph init -i`

- Trigger condition: User initializes the project and requires immediate indexing.
- Starting point: `init [path]` command of `src/bin/codegraph.ts`.
- Key steps:
1. Parse the project path and check whether it has been initialized.
2. Call `CodeGraph.init(projectPath, { index: false })` to create `.codegraph/` and DB.
3. If there is an index parameter, call `indexAll()`.
4. `ExtractionOrchestrator` Scan the source code, load grammar, and extract nodes/edges/unresolved refs.
5. `ReferenceResolver` Parse references in batches and add calls/imports/extends and other edges.
6. Write index version and extract version metadata.
- Endpoint: local `.codegraph/codegraph.db` can be queried by CLI/MCP.
- Input: project path, indexing options.
- Output: index statistics, SQLite graph.
- Error handling: file lock, anti-concurrency, ignore default dependency directory, parsing timeout, invalid `.gitignore` fault tolerance.
- Based on: `src/bin/codegraph.ts`, `src/index.ts`, `src/extraction/index.ts`.

### Call chain 2: `codegraph_explore`

- Trigger condition: Agent asks "how a certain module works" or requires context before editing.
- Origin: `ToolHandler.execute()` of `src/mcp/tools.ts` distributed to `handleExplore()`.
- Key steps:
1. Verify query, projectPath, maxFiles.
2. Get the `CodeGraph` instance of the default or specified project.
3. Select the output budget based on the number of project files.
4. Call `findRelevantContext()` to find the relevant subgraph.
5. Add seeds to named symbols and aggregate nodes by file.
6. Filter low-value test/icon/i18n files and cut source code fragments.
7. Add relationships, integrity hints, and staleness/worktree notices.
- Endpoint: Return the Markdown tool results that Agent can use directly.
- Input: natural language query or collection of symbols/filenames.
- Output: related source code, relationship diagrams, undisplayed files, and budget tips.
- Error handling: upper limit of input length, upper limit of output length, path verification, pending sync prompt.
- Basis: `src/mcp/tools.ts`.

### Call chain 3: MCP server startup and sharing engine

- Trigger condition: Agent configuration starts `codegraph serve --mcp`.
- Starting point: CLI `serve` command and `src/mcp/engine.ts`.
- Key steps:
1. Create `MCPEngine` after the MCP server is started.
2. `ensureInitialized()` searches upwards from the current directory for `.codegraph/`.
3. Open `CodeGraph` DB and set the default instance.
4. Start watcher and do catch-up sync.
5. Multiple sessions share the same engine and SQLite WAL.
- End point: MCP tools can query the same project index.
- Input: current working directory or explicit projectPath.
- Output: Shared ToolHandler and CodeGraph instances.
- Error handling: retain retry semantics when not initialized; write stderr when opening fails; prompt to run sync when watcher is unavailable.
- Basis: `src/mcp/engine.ts`.

### Call chain 4: Multi-Agent installation

- Trigger condition: User executes `codegraph install`.
- Starting point: `src/installer/index.ts`.
- Key steps:
1. Parse `--target` or select interactively.
2. `detectAll()` detects supported Agents.
3. Select the global/local configuration location.
4. Call `install()` for each target.
5. Write MCP server configuration; Claude can write permissions; old instructions block is cleared.
- Endpoint: The Agent can load CodeGraph MCP the next time it starts.
- Input: target, location, autoAllow, yes and other options.
- Output: Each Agent configuration file changes.
- Error handling: Codex does not support local; unknown target throws an error; writing uses atomic writing.
- Based on: `src/installer/index.ts`, `src/installer/targets/registry.ts`, `src/installer/targets/codex.ts`, `src/installer/targets/claude.ts`.

## 6. Read notes

- Important findings: The current version puts the Agent tool guidance in the MCP initialize response and no longer relies on writing `CLAUDE.md` / `AGENTS.md`. This is critical to avoid duplicate system prompts and for cross-Agent consistency.
- Important findings: `codegraph_explore` is not a simple search, it includes adaptive output budget, named symbol seeding, low-value file filtering, staleness hints and output truncation strategies.
- Important findings: Index freshness is maintained by three layers: watcher, connect-time catch-up, and manual sync.
- Uncertainty: The accuracy of extractors in different languages ​​has not been verified item by item.
- Uncertainty: The README benchmark has not been re-run, and the benefits of this machine or different models cannot be confirmed.
- To-be-run verification: Install CLI, execute `codegraph init -i` on a medium TypeScript project, compare MCP tools output with normal file search results.

## To-do check items

- [x] Entry file found.
- [x] Find the main process or task scheduling main line.
- [x] Clarify the model calling location not applicable: This project is not a model calling framework, the core is MCP tools and code indexes.
- [x] Locate tool registration and execution locations.
- [x] Locate context management and MCP directive locations.
- [ ] Run verification CLI and MCP server.
- [ ] Review the complete test suite.

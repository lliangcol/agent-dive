# CodeGraph project deep dive

## 1. Basic project information

- Project name: CodeGraph
- Project ID: `colbymchenry__codegraph`
- GitHub：https://github.com/colbymchenry/codegraph
- Official documentation: https://colbymchenry.github.io/codegraph/
- Category: `mcp-tools`
-Collect level: Level A deep collect
- Current status: `analyzing`
- Main language: TypeScript
- License：MIT
- Analysis date: 2026-06-10
- Analysis version/Commit:`16c73e2b0e027411e22039baeb32fbe60ab42b4c`
- Whether to run verification: No
- Analysis basis: GitHub API, README, official document source code, `package.json`, `src/` brief reading of source code

## 2. Positioning in one sentence

CodeGraph is a local-first code knowledge graph and MCP tool layer that allows AI coding agents to understand the code base through pre-indexed symbols, calling relationships, file structures and source code snippets, instead of starting from the grep/read file every time.

## 3. Problems solved by the project

AI coding agents usually need to repeatedly list directories, search, read files, and chase call links in unfamiliar warehouses. This consumes a lot of tokens and tool calls, and it is also easy to miss cross-file, cross-language, or dynamic distribution relationships. CodeGraph's approach is to first use tree-sitter and parser to convert the code base into `.codegraph/codegraph.db`, and then provide structured queries through CLI and MCP tools.

Learning value mainly falls into three categories:

- How MCP tools provide agents with retrievable, traceable, and pre-editable code context.
- How static code index goes from file scanning, AST extraction, SQLite storage, reference resolution to call graph and impact surface analysis.
- How multi-Agent installers connect the same MCP server to different hosts such as Claude Code, Codex CLI, Cursor, and Gemini CLI.

## 4. Project main line

The user first installs the `codegraph` CLI, and then executes `codegraph init -i` in the target warehouse to create a local index. The indexing process scans the source code files, loads the tree-sitter WASM grammar by language, extracts nodes and edges, writes them to SQLite, and then runs reference parsing and framework-specific parsing. The Agent side connects to the MCP server through `codegraph serve --mcp` and calls tools such as `codegraph_explore`, `codegraph_search`, `codegraph_callers`, `codegraph_callees`, `codegraph_impact`, `codegraph_node`, `codegraph_files`, `codegraph_status` to obtain the context.

Based on: README's Get Started, How It Works, MCP Tools; source code `src/bin/codegraph.ts`, `src/index.ts`, `src/extraction/index.ts`, `src/mcp/tools.ts`, `src/mcp/engine.ts`.

## 5. Quick Start

- Environmental requirements: README provides a shell/PowerShell installer; npm package's `package.json` annotates Node `>=20.0.0 <25.0.0`, and README's Library Usage also prompts that the embedded API depends on Node 22.5+'s `node:sqlite`.
- Installation steps:

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh

# Windows PowerShell
irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 | iex

# 或 npm
npm i -g @colbymchenry/codegraph
```

- Agent access:

```bash
codegraph install
```

- Project initialization:

```bash
cd your-project
codegraph init -i
```

- Minimal query:

```bash
codegraph status
codegraph query UserService --kind class --limit 10
codegraph callers handleRequest --json
```

- Known limitations: It has not been installed and run this time. The above are README/CLI document-level steps; the actual Windows PATH, effective shell, agent configuration writing and project indexing time need to be verified separately.

## 6. Core architecture

CodeGraph can be split into six layers:

- CLI layer: `src/bin/codegraph.ts` Defines commands such as installation, initialization, indexing, synchronization, status, query, call chain, impact area, MCP server, etc.
- Installer layer: `src/installer/` is responsible for detecting and writing the MCP configuration of different Agents, and the target is registered at `src/installer/targets/registry.ts`.
- Core facade: `src/index.ts`'s `CodeGraph` classes organize database connections, extractors, parsers, graph queries, context building and file watchers.
- Extraction layer: `src/extraction/` Responsible for file scanning, language detection, tree-sitter WASM grammar loading, AST node and edge extraction.
- Graph storage and query layer: `src/db/schema.sql` defines nodes, edges, files, unresolved_refs, FTS5 and other tables; `src/graph/` provides traversal and query manager.
- MCP layer: `src/mcp/engine.ts` manages shared CodeGraph instances and watchers; `src/mcp/tools.ts` defines MCP tools, parameter validation, output budgets, and staleness/worktree hints.

See `assets/diagrams/architecture.mmd` for diagrams.

## 7. Core Principles

### 7.1 Pre-indexed knowledge graph

The core of CodeGraph is not to search online, but to first build a project-level SQLite knowledge graph offline. The `nodes` table in `src/db/schema.sql` stores symbols such as functions, classes, methods, variables, etc. The `edges` table stores relationships such as calls, references, imports, extends, implements, etc. The `files` table stores file hashes and language information. FTS5 is used for full-text symbol search.

### 7.2 AST extraction and language support

`src/extraction/grammars.ts` Mapping languages ​​with file extensions, loading tree-sitter WASM grammar on demand. README nominally supports 20+ languages, and the source code also includes special processing paths such as Vue, Svelte, Liquid, Razor, YAML/properties, etc.

### 7.3 Reference resolution

`src/resolution/index.ts` Aggregates import resolution, name matching, framework resolver, callback synthesizer, path alias, Go module and workspace package and other information, and resolves unresolved references in the extraction phase into cross-file relationships. The source code comments clearly indicate that cross-file resolution is best-effort, and multiple candidates may be returned when encountering ambiguity.

### 7.4 Agent tool layer

The main entrance of MCP tools is `codegraph_explore`, and the goal is to return the source code fragments, relationships and impact information of related symbols at once. The tool layer also provides search, callers, callees, impact, node, files, and status. `src/mcp/server-instructions.ts` Provide the tool usage strategy to the client through the MCP initialize response. The current README and source code indicate that the new version will no longer write this set of instructions `CLAUDE.md` / `AGENTS.md`.

### 7.5 Automatic synchronization

`src/index.ts`'s `watch()` triggers the increment `sync()` through `FileWatcher`, `src/mcp/engine.ts` starts the watcher after the MCP server is initialized, and does catch-up sync before the first tool call. README description watcher uses FSEvents / inotify / ReadDirectoryChangesW, the default debounce is about 2 seconds.

## 8. Source code structure

- Entry file: `src/bin/codegraph.ts`
- Core facade: `src/index.ts`
- MCP server：`src/mcp/`
- Extractor: `src/extraction/`
- Parser: `src/resolution/`
- Picture query: `src/graph/`
- Database: `src/db/`
- Installer: `src/installer/`
- Synchronization mechanism: `src/sync/`
- Test directory: `__tests__/`
- Documentation station: `site/src/content/docs/`
- Build configuration: `package.json`, `tsconfig.json`, `vitest.config.ts`

## 9. Key call chain

### Call chain 1: initialization and full index

- Trigger condition: User executes `codegraph init -i` or `codegraph index`
- Starting point: `src/bin/codegraph.ts`
- Key steps: CLI parsing command -> `CodeGraph.init()` / `CodeGraph.open()` -> `indexAll()` -> `ExtractionOrchestrator.indexAll()` -> `resolveReferencesBatched()` -> write nodes/edges/files metadata
- Output: `.codegraph/codegraph.db` and index statistics
- Error handling: file locks to avoid concurrent indexing; parsing timeout, invalid `.gitignore`, large files and default ignored directories all have protection logic
- Basis: `src/bin/codegraph.ts`, `src/index.ts`, `src/extraction/index.ts`

### Call chain 2: Agent questions to MCP exploration results

- Trigger condition: Agent calls `codegraph_explore`
- Starting point: `src/mcp/tools.ts`
- Key steps: MCP tool parameter verification -> `ToolHandler.handleExplore()` -> Get `CodeGraph` instance -> `findRelevantContext()` -> Aggregate nodes by file -> Budget clipping -> Return source code snippets and relationship tips
- Output: Markdown text results for Agent
- Error handling: input length limit, path verification, output budget, staleness banner, worktree mismatch notice
- Basis: `src/mcp/tools.ts`, `src/mcp/engine.ts`, `src/index.ts`

### Call chain 3: The installer accesses multiple Agents

- Trigger condition: User execution `codegraph install`
- Starting point: `src/installer/index.ts`
- Key steps: Detect available targets -> Parse `--target` -> Select global/local -> Write MCP configuration for each target -> Optional setting Claude auto-allow -> Local mode initialization project
- Output: Claude/Cursor/Codex/opencode/Hermes/Gemini/Antigravity/Kiro corresponding configuration
- Error handling: skip and prompt when the target does not support local; Codex only supports global; old instructions block will be cleaned up
- Basis: `src/installer/index.ts`, `src/installer/targets/registry.ts`, `src/installer/targets/codex.ts`, `src/installer/targets/claude.ts`

## 10. integration method

### CLI / MCP integration

The most direct integration is to use CodeGraph as a standalone CLI and MCP Server: install the CLI, run `codegraph install` to write the agent configuration, and execute `codegraph init -i` in each target project.

### SDK / Embedded integration

README provides Library Usage of `import CodeGraph from '@colbymchenry/codegraph'`, which can call `CodeGraph.init()`, `indexAll()`, `searchNodes()`, `getCallers()`, `buildContext()`, `getImpactRadius()`, `watch()` and other APIs in the Node process. This path is suitable for Electron or self-built development tools, but the Node version and SQLite backend need to be verified separately.

### Java / Spring Boot relationship

CodeGraph is not a Java/Spring Boot library. A more appropriate way in Java projects is to use it as an external CLI/MCP indexer, allowing Agent or CI scripts to assist in determining the impact of changes through `codegraph affected`, `codegraph impact`.

## 11. Problemshooting

See [troubleshooting.md](troubleshooting.en.md) for details. The focus of the first round includes PATH not taking effect, project not initialized, Node version incompatibility, watcher unavailable, index expiration, document and source code representation drift.

## 12. Objective evaluation

### advantage

- Highly compatible with Agent workflow, MCP tools cover search, exploration, calling relationships, influence areas and file structure.
- Native SQLite and local parsing, no external services or API keys required by default.
- TypeScript source code has a clear structure, and the CLI, installer, MCP, extraction, resolution, and graph are clearly layered.
- Multi-language and multi-Agent coverage is wide, suitable for learning MCP tool productization.
- The test directory covers a wide range of topics, including installer, MCP, sync, framework routes, bridge, search, security and other topics.

### shortcoming

- Static parsing can only be best-effort for dynamic calls, runtime reflection, framework magic, and cross-language bridging.
- The benefits of the Agent depend on whether the Agent really prioritizes using CodeGraph tools; if grep/read continues, the benefits will decrease.
- There are many supported languages ​​and frameworks, and the maintenance complexity is high. The accuracy of specific languages ​​needs to be verified item by item.
- The README benchmark has not been rerun in this collection and cannot be used as a conclusion of local actual measurements.

### Applicable scenarios

- Agents for large and medium-sized code bases assist in code reading, impact analysis, and pre-refactoring positioning.
- Want to expose local code indexes to multiple AI coding tools through MCP.
- Learn MCP server, code map, AST extraction, reference resolution and Agent tool design.

### not applicable scenario

- Scenarios that require real runtime call chains, production traces or performance profiling.
- Restricted environment that does not allow generating `.codegraph/` index files in the project directory.
- Repositories that only handle documentation, configuration, binary or non-source assets.

## 13. Learning Todo List

See [learning-todo-list.md](learning-todo-list.en.md) for details.

## 14. Summary

CodeGraph deserves to be used as a Level A deep collection project: it is not only a representative of the MCP tool system, but also shows how static code knowledge graphs can serve Agentic Coding. In the next round of learning, priority should be given to actually running through `codegraph init -i`, checking the generated DB and MCP tools returns, and then reviewing the differences between `codegraph_explore` and ordinary grep/read on a local medium-sized warehouse.

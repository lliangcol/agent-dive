# Graphify source reading record

## 1. Reading objectives

- Questions to understand in this round: How Graphify builds a knowledge graph from the project directory and how to access the AI ​​coding assistant.
- Related functions: CLI, Tree-sitter static analysis, semantic extraction, map output, Codex / Claude Code skill installation, MCP server.
- Expected output: Confirm core module boundaries, key call chains, run verification commands and security boundaries.

## 2. Source code entry

| Entrance | path | effect | in accordance with |
|---|---|---|---|
| CLI | `graphify.__main__:main` | `graphify` Command entry | pyproject.toml, pending source code verification |
| MCP server | `graphify.serve:_main` | `graphify-mcp` Command entry | pyproject.toml, pending source code verification |
| package directory | `graphify/` | Core Python packages | GitHub contents API |
| document | `docs/`、`ARCHITECTURE.md`、`SECURITY.md` | Architecture, safety and usage instructions | GitHub contents API |
| test | `tests/` | Regression testing and behavioral examples | GitHub contents API |

## 3. Module map

| module | path | Responsibilities | Dependencies |
|---|---|---|---|
| CLI layer | `graphify/__main__.py` or adjacent entry file | Parameter parsing, command distribution | pending source code verification |
| installer | `graphify/` Installer/skill related modules | Write skill, AGENTS, and hook configurations for different assistant platforms | pending source code verification |
| File scanning | `graphify/` Scan / ingest related modules | Traverse project files, filter paths, and incremental cache | pending source code verification |
| code extraction | `graphify/` Internal parser / tree-sitter related modules | Extract functions, classes, imports, and calling relationships | pending source code verification |
| Semantic extraction | `graphify/` Internal LLM/extraction related modules | Process semantic nodes such as documents, pictures, and transcriptions | pending source code verification |
| Graph construction | `graphify/` Internal graph related modules | Build node, edge, community or subgraph queries | pending source code verification |
| export layer | `graphify/` Within export / report related modules | Generate output in HTML, Markdown, JSON, GraphML, Neo4j and more | pending source code verification |
| MCP service | `graphify/serve.py` or adjacent module | Expose graph query capabilities | pending source code verification |

## 4. Recommended reading order

1. `README.md`: Confirm the official usage path, output and platform support.
2. `ARCHITECTURE.md`: Let’s first look at the architectural boundaries defined by the author.
3. `SECURITY.md`: Confirm the boundaries of data outgoing, hook, command execution and sensitive file processing.
4. `pyproject.toml`: Confirm entry, extras, dependencies and package data.
5. CLI entry: Follow `graphify.__main__:main` to see command distribution.
6. The main line of map construction: find the serial positions of scanning, analysis, extraction, map construction, and writing files.
7. Platform installer: Check which files are written by Codex / Claude Code / Cursor and other platforms.
8. MCP server: Confirm tool interface, input and output, and map file reading logic.
9. `tests/`: Find regression tests covering CLI, install, graph build, query, and MCP.

## 5. Key call chain

### Call chain 1: Build graph

- Trigger condition: Execute `graphify .`.
- Starting point: `graphify.__main__:main`, pending source code confirmation.
- Key steps: Parse path and backend parameters -> Scan files -> Tree-sitter locally extracts code structure -> Semantic extraction of non-code materials such as docs, PDFs, pictures, etc. -> Build graphs -> Write out `graphify-out/`.
- End point: `graph.html`, `GRAPH_REPORT.md`, `graph.json`.
- Input: project directory, optional backend, optional extras capabilities.
- Output: map files and reports.
- Error handling: pending source code confirmation, including missing dependencies, missing non-code semantic extraction API keys, parsing failures, and cache corruption.
- Based on: README, Privacy description, and pyproject.toml.

### Call chain 2: Install Codex integration

- Trigger condition: Execute `graphify install --platform codex` or `graphify install --project --platform codex`.
- Starting point: Installation command distribution, pending source code confirmation.
- Key steps: Detect platform -> Generate Codex instruction block -> Write `AGENTS.md` or project-level configuration -> Write `.codex/hooks.json`.
- End point: be reminded to query the map first before subsequent Codex search/reading.
- Input: platform parameters, whether project-scoped.
- Output: Assistant configuration file.
- Error handling: To be verified, existing files need to be merged, uninstalled, insufficient permissions, and repeated installation.
-Based on: README Codex installation instructions.

### Call chain 3: MCP query

- Trigger condition: `graphify-mcp` is started and called by an Agent that supports MCP.
- Starting point: `graphify.serve:_main`, pending source code confirmation.
- Key steps: Load graph -> Register tool -> Receive query -> Return relevant nodes, edges or report fragments.
- Endpoint: Agent answers code base questions using smaller context.
- Input: MCP request and graph path.
- Output: query results.
- Error handling: To be confirmed by the source code.
- Based on: pyproject.toml and README extras.

## 6. Read notes

- Important discovery: The key learning point of Graphify is not a single algorithm, but the combination of "static code graph + semantic extraction + Agent workflow injection + query output".
- Uncertainty: There are many platforms mentioned in the README. You need to confirm whether each platform installer shares a set of templates or maintains them separately.
- Verification to be run: Install package, build small warehouse map, open HTML, query JSON, verify Codex project install writing range.

## To-do check items

- [ ] Find the entry file.
- [ ] Find the main process of graph construction.
- [ ] Find the LLM backend configuration and calling location.
- [ ] Find Tree-sitter parser registration and language support tables.
- [ ] Locate the MCP server tool definition.
- [ ] Find the Codex installer write logic.
- [ ] Check security boundaries and sensitive file filtering.

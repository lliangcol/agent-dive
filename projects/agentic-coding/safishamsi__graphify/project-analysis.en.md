# Graphify project deep dive

## 1. Basic project information

- Project name: Graphify
- Project ID: `safishamsi__graphify`
- GitHub：https://github.com/safishamsi/graphify
- Project homepage: https://graphifylabs.ai/（GitHub API homepage / README link)
- Category: `agentic-coding`
-Collect level: Level B standard collect
- Current status: `analyzing`
- Main language: Python
- License：MIT
- Analysis date: 2026-06-10
- Analysis version/Commit:`5504c84324fc9249eb4c9d0cca86da7140250032`
- Default branch: `v8`
- Whether to run verification: No
- Analysis basis: GitHub README, GitHub API, `git ls-remote --symref`, GitHub contents API, pyproject.toml; no local installation and source code call chain verification.

## 2. Positioning in one sentence

Graphify is a project knowledge graph construction and query tool for AI coding assistants. It uses graphed context to replace large-scale full-text reading and temporary search.

## 3. Problems solved by the project

AI coding agents often need to understand module relationships, call relationships, document background, database schema, infrastructure configuration and multimedia materials in real warehouses. Directly inserting a large number of files into the context will waste tokens, and it is also easy for the agent to make judgments based only on local grep results.

The learning value of Graphify is:

- Code base understanding: organize functions, classes, imports, calls, document concepts, etc. into a map.
- Context Engineering: Let the Agent query relevant subgraphs instead of reading the entire warehouse.
- Coding assistant integration: Incorporate graph queries into the workflow through skills, AGENTS.md, hooks or commands.
- Multimodal knowledge organization: In addition to code, it also covers materials such as documents, PDFs, pictures, videos, and audio transcriptions.

Basis: README and GitHub warehouse description; specific implementation boundaries are subject to source code verification.

## 4. Project main line

Based on README, the typical main line of use is as follows:

1. The user installs the PyPI package `graphifyy`, and the CLI command is `graphify`.
2. The user runs `graphify install` or the platform-specific installation command in the project directory to write the Graphify skill/command/hook into the target AI assistant environment.
3. The user asks the assistant to execute `/graphify .` or `$graphify` in the Codex scenario.
4. Graphify scans the target directory and builds a knowledge graph.
5. Generate `graphify-out/graph.html`, `graphify-out/GRAPH_REPORT.md`, `graphify-out/graph.json`.
6. Follow-up code base questions will be answered through graph query, report or MCP server.

Not verified: The above steps have not been executed on this machine, and the specific CLI parameters and output file contents need to be confirmed by running.

## 5. Quick Start

- Environment requirements: Python 3.10+; README recommends `uv`, and also supports `pipx` or `pip`.
- Recommended installation: `uv tool install graphifyy`.
- Register assistant skill: `graphify install`.
- Build the current directory map: README uses `/graphify .` in most assistant scenarios; PowerShell scenarios should use `graphify .` because `/` is the path separator.
- Main output: `graph.html`, `GRAPH_REPORT.md`, `graph.json`.
- Known limitations: This repository has not performed installation and running verification; when it comes to semantic extraction of non-code materials such as docs, PDFs, images, etc., API keys, networks, backends, and sensitive data boundaries need to be checked.

## 6. Core architecture

According to the README, GitHub contents API and pyproject.toml, currently identifiable module clues:

| module | effect | in accordance with | Verification status |
|---|---|---|---|
| CLI `graphify` | Command line entry to perform installation, build, export and query | pyproject `[project.scripts]` Summary | pending source code verification |
| Skill installer | Write instructions or skills to Claude Code, Codex, Cursor, Gemini CLI and other platforms | README Platform Installation Form | pending verification |
| Code extraction | Use static analysis capabilities such as Tree-sitter to extract code structure | README File Handling and Privacy Instructions | pending source code verification |
| Semantic extraction | Semantic extraction of non-code materials such as docs, PDFs, pictures, etc. | README file handling, optional extras and Privacy instructions | pending source code verification |
| Graph outputs | Generate output in HTML, Markdown report, JSON, optional Neo4j/MCP and more | README output description | pending verification |
| MCP server | Expose `graphify-mcp` entrance for tool protocol query | pyproject.toml `[project.scripts]` | pending source code verification |

See `assets/diagrams/architecture.mmd`, `flow.mmd` and `sequence.mmd` for draft diagrams.

## 7. Core Principles

### Knowledge graphing context

The core idea of ​​Graphify is to split project materials into nodes and relationships, and then let the Agent query related subgraphs. This can reduce the cost of full reading and provide a unified search entry for codes, documents, schemas, pictures and transcribed texts.

Basis: README description of `graph.json`, `GRAPH_REPORT.md`, `graph.html` and queryable knowledge graph.

### Static structure extraction

README and pyproject.toml show that code structure analysis relies on Tree-sitter, and the goal is to extract deterministic structures such as classes, functions, imports, calling relationships, and comments. This design is suitable as a source reading entry, but it cannot replace manual verification of key call chains.

Based on: GitHub README and pyproject.toml; pending source code verification.

### Agent tool integration

Graphify is not a simple offline analyzer, it focuses on serving AI coding assistants. The README lists Claude Code, Codex, OpenCode, Cursor, Gemini CLI and other platforms, and explains that Codex reminds you to take the graph path through `AGENTS.md` and hook.

Basis: README platform installation instructions; to be run for verification.

### MCP and Export

pyproject.toml shows that `graphify-mcp = "graphify.serve:_main"` is present, and the README extras also contain `mcp` and `neo4j`. This shows that the project not only generates static graphs, but may also be connected to the Agent tool ecosystem as a queryable service.

Based on: pyproject.toml; pending source code verification.

### Data and Privacy Boundaries

The Privacy chapter of the README clearly distinguishes the processing paths: code files are extracted locally through Tree-sitter, code-only corpus does not require an API key; videos/audio are transcribed locally through faster-whisper; docs, PDFs, and images are sent to the user-configured AI assistant/backend for semantic extraction. Before using a private warehouse, the point is not to ban Graphify in general, but to first confirm whether the input range, backend, environment variables, query logs and non-code materials are allowed to be sent out.

Basis: README Privacy and file handling instructions; to be verified by native configuration.

## 8. Source code structure

The root directory structure shown on the GitHub page:

- `.github/`: CI or automation configuration, to be checked.
- `docs/`: Project documentation, including how-it-works and other instructions.
- `graphify/`: Core Python package, waiting for source reading.
- `tests/`: Test directory, coverage to be checked.
- `tools/`: Auxiliary tool directory, to be checked.
- `worked/`: Sample or working material directory, to be checked.
- `pyproject.toml`: Package metadata, CLI entry, extras and development dependencies.
- `ARCHITECTURE.md`, `SECURITY.md`, `CHANGELOG.md`: Architecture, security and change data entry.

Waiting for source code confirmation:

- CLI main entrance: `graphify.__main__:main`
- MCP server entrance: `graphify.serve:_main`
- Real module boundaries for parsing, extraction, graph building, exporting, and querying.

## 9. Key call chain

### Call chain 1: CLI build graph

- Trigger condition: The user executes `graphify .` in the project directory or the assistant triggers `/graphify .`.
- Starting point: `graphify.__main__:main`, pending source code confirmation.
- Key steps: parse parameters -> scan files -> static structure extraction -> semantic extraction -> build graph -> write out `graphify-out/`.
- Endpoint: Generate `graph.html`, `GRAPH_REPORT.md`, `graph.json`.
- Based on: README and pyproject.toml.
-Status: pending source code and operation verification.

### Call chain 2: Codex integration reminder

- Trigger condition: Execute `graphify install --platform codex` or similar installation.
- Starting point: Installation command, waiting for source code confirmation.
- Key steps: write the AGENTS command -> write the Codex hook configuration -> remind you to query the map first before subsequent search operations.
- End point: Graphify query is given priority in the Codex workflow.
-Based on: README Codex installation instructions.
- Status: pending verification.

### Call chain 3: MCP query

- Trigger condition: Install `mcp` extra and start `graphify-mcp`.
- Starting point: `graphify.serve:_main`, pending source code confirmation.
- Key steps: Read the graph file -> Expose query tool -> Agent calls the tool to obtain relevant nodes, edges or report fragments.
- End point: Agent gets smaller context.
- Based on: pyproject.toml and README extras.
-Status: pending source code and operation verification.

## 10. integration method

It is suitable to do three kinds of integration experiments first:

1. Local warehouse static map: Select a small sample warehouse to execute `graphify .`, and check the output file and query quality.
2. Codex workflow integration: Execute `graphify install --platform codex --project` and confirm the written `AGENTS.md` and hook configuration.
3. MCP query integration: Install `graphifyy[mcp]` and verify whether `graphify-mcp` or the `--mcp` / query command in README can read the map and respond to the query.

The integration focus of the Java/Spring Boot project is not SDK embedding, but using the Java warehouse as input material. After generating the map, it is used for architecture understanding, call chain positioning and knowledge Q&A.

## 11. Problemshooting

Priority troubleshooting direction:

- PowerShell command difference: Do not use `/graphify .` in PowerShell, execute `graphify .` directly.
- The package name is different from the command name: the PyPI package name is `graphifyy`, and the CLI command is still `graphify`.
- PATH issue: Use `uv tool install` or `pipx install` first to avoid the command being invisible after plain `pip`.
- Sensitive data boundaries: Code AST paths are processed locally according to README; before performing semantic extraction on non-code materials such as docs, PDFs, and images, you should confirm which content will be sent to the external model or assistant backend.
- Inaccurate graph generation: first distinguish between static code extraction, document semantic extraction, report summary and query strategy, and do not regard reports as source code facts.

## 12. Objective evaluation

### advantage

- For real AI coding assistant workflow, not just an offline visualization tool.
- Supports unified mapping of code, documents, SQL schema, infrastructure and multi-modal materials.
- Output includes HTML, Markdown report and JSON, taking into account human readability, visualization and machine query.
- There are clear platform integration paths for Codex, Claude Code, Cursor, Gemini CLI, etc.
- MIT License, suitable for learning and secondary research.

### shortcoming

- The range of abilities is very large, and beginners can easily stop at the README level of understanding.
- Involving multi-platform installation, hooks, LLM backend, MCP, Neo4j and multi-modal dependencies, the verification cost is not low.
- The platform and function list of README are updated quickly. There may be version drift in the documentation and source code, which needs to be verified by commit.
- Before using semantic extraction on non-code materials such as docs, PDFs, and images in sensitive warehouses, you must confirm the data outgoing boundary.

### Applicable scenarios

- Learn code base knowledge graph and context compression.
- Establish warehouse-level knowledge portals for coding assistants such as Codex/Claude Code.
- Assist in architecture exploration, module relationship sorting and document generation for large warehouses.
- Study how MCP server serves code understanding tools.

### not applicable scenario

- Need to be a direct replacement for source code review or security audit.
- Sensitive items processed by external models or assistant backends cannot be accepted unless explicitly only processing local AST / local transcribed paths, or a local backend is explicitly selected.
- Just want small tasks like lightweight grep or single file Q&A.
- Hooks and installation write behavior have not yet been verified for production repositories.

## 13. Learning Todo List

See [learning-todo-list.md](learning-todo-list.en.md). It is recommended to complete Level 1 to Level 2 before entering source code level verification.

## 14. Summary

Graphify is worth collecting as a Level B project in the `agentic-coding` direction. It connects code base understanding, knowledge graph, Agent tool integration and contextual engineering, and is suitable as a learning example of "how AI coding assistants can more stably understand large-scale projects".

The next step should be to perform native minimum run verification and source code confirmation of the true boundaries of CLI build, Codex installation, MCP server and semantic extraction.

# Graphify

Graphify is a knowledge graph tool for AI coding assistants. It converts code, documents, SQL schema, scripts, papers, pictures, videos and other project materials into a queryable knowledge graph, which is used to reduce the coding agent's dependence on full-text reading and temporary grep.

## collect information

| Field | value |
|---|---|
| Project name | Graphify |
| Project ID | `safishamsi__graphify` |
| GitHub | https://github.com/safishamsi/graphify |
| Project home page | https://graphifylabs.ai/ |
| Main category | `agentic-coding` |
| Auxiliary tags | `knowledge-graph`、`rag-agents`、`mcp-tools`、`tree-sitter`、`context-engineering` |
| collectlevel | Level B standard collect |
| Current status | `analyzing` |
| Default branch | `v8` |
| collect snapshot | 2026-06-10 |
| latest review | 2026-06-11 |
| Analysis Commit | `5504c84324fc9249eb4c9d0cca86da7140250032` |
| Whether to run verification locally | no |

## Why collect

- Explicitly related to AI Agent: README is explicitly oriented to AI coding assistants such as Claude Code, Codex, OpenCode, Cursor, Gemini CLI, etc.
- High learning value: can be used to understand code base knowledge graph, static analysis, semantic extraction, context compression, Agent tool integration and MCP server output.
- The engineering reference value is clear: the warehouse includes engineering topics such as CLI, skill installation, hooks, map export, MCP, Tree-sitter analysis, multi-modal input, etc.
- Suitable for generating diagrams and learning tasks: it can be split into architecture diagrams, construction flow diagrams, assistant integration diagrams, MCP query diagrams and troubleshooting diagrams.

## Data generated

- [project deep dive](project-analysis.en.md)
- [source reading record](source-code-reading.en.md)
- [integration guide](integration-guide.en.md)
- [Problem troubleshooting records](troubleshooting.en.md)
- [Learning Todo List](learning-todo-list.md)
- [collectreport](collect-report.en.md)
- [diagrams directory](assets/diagrams/)

## Current validation boundaries

Verified:

- GitHub repository exists publicly.
- GitHub API shows that the default branch is `v8`, the main language is Python, the License is MIT, and the homepage is `https://graphifylabs.ai/`.
- When reviewing on 2026-06-11, GitHub API shows stars `64743`, forks `6578`, and open_issues_count `328`.
- `git ls-remote --symref` displays HEAD pointing to `refs/heads/v8`, and the current HEAD is `5504c84324fc9249eb4c9d0cca86da7140250032`.
- README describes `graphify` CLI, AI assistant skill installation, output `graph.html`, `GRAPH_REPORT.md`, `graph.json`, and capabilities such as Codex / MCP / Neo4j / Tree-sitter / multi-modal extras.
- The privacy statement of the README distinguishes the data paths: code files are processed through Tree-sitter local AST; videos/audio are transcribed locally using faster-whisper; docs, PDFs, and images are semantically extracted through the user-configured AI assistant/backend.

Not verified:

- `graphifyy` is not installed or executed on this machine.
- Generated `graphify-out/` content is not verified.
- The complete call chain of CLI, hook, MCP server, Tree-sitter parser, and semantic extraction has not been confirmed at the source code level.
- All platform skill installation paths and hook behaviors are not verified.

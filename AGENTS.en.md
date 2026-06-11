# AGENTS.md

This document is intended for AI coding assistants, automation agents, and maintainers and describes the collaboration boundaries of the AgentDive repository.

## Project positioning

AgentDive is a Chinese AI Agent open source project deep dive and learning material repository. The core products are project analysis, diagrams, learning tasks, learning notes, and verification evidence, not Awesome List, nor third-party project source code images.

## Work rules

- Documents and summaries are written in Simplified Chinese by default.
- Do not modify the original requirements data under `docs/` unless explicitly required by the task.
- Do not submit accounts, keys, tokens, local private paths, private configurations or undesensitized logs.
- Do not falsify running results, source code conclusions, project status, star count, license or upstream capabilities.
- When there is no real operation, test or source code verification evidence, the corresponding `evidence.md`, `meta.json` or `not_run`, `pending`, `partial` or clear inference boundaries must be marked in the text.
- New projects use stable ID: `owner__repo`.
- A single project collection usually only modifies `projects/<category>/<owner__repo>/`, `learning-notes/<owner__repo>/`, `PROJECTS.md` and `LEARNING_PROGRESS.md`.
- Run `python scripts/check-agent-dive.py` after modifying templates, scripts, indexes or project data.

## Code discovery

This project uses codebase-memory-mcp to maintain the code knowledge graph. When doing code discovery, always use the MCP graph tool first, rather than starting with grep, glob, or file searches.

Priority:

1. `search_graph`: Find functions, classes, routes, and variables by name, natural language, or pattern.
2. `trace_path`: Track the caller, callee, data flow or cross-service path.
3. `get_code_snippet`: Read the source code fragment of the located symbol.
4. `query_graph`: Execute complex graph queries.
5. `get_architecture`: Get a summary of the project structure and architecture.

Fallback to `rg`, file list, or read file directly only if:

- Search for string literals, error messages, configuration values, or non-code files.
- The MCP mapping tool is not available, the item is not indexed, or insufficient results are returned.
- The tasks themselves are non-code content such as GitHub configuration, Markdown, license, templates, script instructions, etc.

## Pull Request Expected

- The PR description should list the scope of change, verification orders, and outstanding items.
- PRs that affect the project status must be updated simultaneously in the project directory, learning notes, `PROJECTS.md` and `LEARNING_PROGRESS.md`.
- Do not use `study-ready`, `in-study` or `completed` as promotional status; the status must be supported by evidence.

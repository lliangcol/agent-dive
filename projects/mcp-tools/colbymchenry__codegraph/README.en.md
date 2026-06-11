# CodeGraph

## Project positioning

CodeGraph is a native code knowledge graph tool for Claude Code, Codex CLI, Cursor, opencode, Hermes Agent, Gemini CLI, Antigravity IDE and Kiro. It establishes `.codegraph/codegraph.db` through the CLI, and then exposes structured code search, source code exploration, caller, callee, and impact analysis capabilities to the Agent through the MCP Server.

## collect information

| Field | value |
|---|---|
| Project name | CodeGraph |
| GitHub | https://github.com/colbymchenry/codegraph |
| Official documentation | https://colbymchenry.github.io/codegraph/ |
| Project ID | `colbymchenry__codegraph` |
| Classification | `mcp-tools` |
| collectlevel | Level A depth collect |
| Current status | `analyzing` |
| main language | TypeScript |
| License | MIT |
| Analysis date | 2026-06-10 |
| analysis version | `16c73e2b0e027411e22039baeb32fbe60ab42b4c` |
| Whether to run verification | no |

## Data index

- [project deep dive](project-analysis.en.md)
- [source reading record](source-code-reading.en.md)
- [integration guide](integration-guide.en.md)
- [Problem troubleshooting records](troubleshooting.en.md)
- [Learning Todo List](learning-todo-list.md)
- [collectreport](collect-report.en.md)

## diagrams

- [architecture.mmd](assets/diagrams/architecture.mmd)
- [indexing-pipeline.mmd](assets/diagrams/indexing-pipeline.mmd)
- [mcp-tool-flow.mmd](assets/diagrams/mcp-tool-flow.mmd)

## Validate boundaries

This collect has read the GitHub API, README, official document source code, `package.json` and core TypeScript source code structure; the CLI has not been installed, not_run `codegraph init -i`, the test suite has not been run, and the benchmark number in the README has not been verified.

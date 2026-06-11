# CodeGraph learning notes

## Learning status

| Field | value |
|---|---|
| project | CodeGraph |
| Project ID | `colbymchenry__codegraph` |
| current stage | source-reading |
| Completion progress | 10/33 |
| Latest updates | 2026-06-10 |

Progress statistics are based on `learning-todo-list.md`’s task items: 5 items of Level 1 and 5 items of Level 3 have been completed.

## First impression

CodeGraph is a very suitable project for learning how to productize MCP tools. It is not a traditional Agent framework, but provides a code understanding base for Agents: first convert the repository into a local SQLite graph, and then expose exploration, search, calling relationships and impact surface analysis into MCP tools.

## completed

- [x] Read README and official documentation entry.
- [x] Confirm GitHub metadata, license, default branch and latest commit.
- [x] Briefly read the CLI, MCP, installer, extraction, resolution, graph, and sync directories.
- [x] Generate project deep dive, source reading records, integration guides, troubleshooting records, diagrams and learning tasks.

## To be verified

- [ ] Install CLI and record version.
- [ ] Run `codegraph init -i` in the sample repository.
- [ ] Start or call MCP tools through Agent.
- [ ] Run `npm test` or critical test subset.
- [ ] Review whether the README benchmark can be reproduced locally.

## Stuck problem

There is currently no hard blocking; the open gap is not yet verified to run CLI/MCP, and the test suite has not yet been run.

## Next step

Select a public medium-sized TypeScript repository and perform a minimal verification closed loop: `codegraph init -i` -> `codegraph status` -> `codegraph query` -> `codegraph_explore` in Agent.

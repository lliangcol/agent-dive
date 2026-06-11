# CodeGraph Quick Start Notes

## environment

- Date: 2026-06-11
- Range: `.cache/sources/colbymchenry__codegraph`
- Git: 2.54.0.windows.1
- Node: v24.16.0
- npm: 11.9.0
- Commit:`16c73e2b0e027411e22039baeb32fbe60ab42b4c`

## completed

- `git clone --no-tags --depth 1` succeeded and checked out the expected commit.
- `npm ci --ignore-scripts` succeeded within the cache clone.
- `npm run build` succeeds and generates `dist/bin/codegraph.js`.
- `node dist/bin/codegraph.js --version` returns `0.9.9`.
- `node dist/bin/codegraph.js --help` demonstrates the expected CLI command set.
- `node dist/bin/codegraph.js init -i .` Complete indexing.
- `node dist/bin/codegraph.js status .` reports 216 files, 3,533 nodes, 14,388 edges, DB size 12.55 MB, and indexed up to date.
- `node dist/bin/codegraph.js query buildContext -p . --json` Returns matching methods, interfaces, and import nodes.
- `node dist/bin/codegraph.js callers buildContext -p . --json` returns valid JSON, the symbol caller is empty.
- `node dist/bin/codegraph.js impact buildContext -p . --json` returns the two affected `buildContext` method nodes.
- `node dist/bin/codegraph.js serve --mcp --no-watch -p .` Accepts line-based JSON-RPC initialize and tools/list messages.
- MCP tools/list returns `codegraph_search`, `codegraph_callers`, `codegraph_callees`, `codegraph_impact`, `codegraph_node`, `codegraph_explore`, `codegraph_status`, `codegraph_files`.
- `npx vitest run __tests__/context.test.ts` passed 17 tests.

## To be filled

- If required for subsequent learning tasks, add a controlled MCP `tools/call` sampling.
- Run the full test suite, or an explicitly recognized subset of focused tests.
- Review npm audit risk: `npm ci --ignore-scripts` reported 8 vulnerabilities.

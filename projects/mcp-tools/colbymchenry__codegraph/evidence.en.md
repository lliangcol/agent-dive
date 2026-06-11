# CodeGraph Evidence

## Snapshot

- Project ID: `colbymchenry__codegraph`
- GitHub: https://github.com/colbymchenry/codegraph
- Category: `mcp-tools`
- Collect level: Level A
- Current status: `analyzing`
- Source snapshot commit: `16c73e2b0e027411e22039baeb32fbe60ab42b4c`
- Source cache path: `.cache/sources/colbymchenry__codegraph`
- TODO progress after isolated validation: 15/33

## Verification Status

| Area | Status | Notes |
|---|---|---|
| Runtime / CLI | `pass` | Local build, version/help, init, status, query, callers, impact, and MCP initialize/tools-list passed in `.cache/sources/colbymchenry__codegraph`. |
| Test suite | `partial` | One focused Vitest file passed; the full suite was not run. |
| Source review | `partial` | The first round of source code or document analysis has been completed, but function-level verification has not yet been completed. |
| Diagrams | `draft` | Mermaid diagrams are available; renderings and source code level accuracy still need to be reviewed. |
| Learning notes | `created` | The learning notes skeleton already exists and must be updated one by one along with the tasks. |

## Command Evidence

| Date | Environment | Command / Operation | Scope | Result | Output summary | Follow-up |
|---|---|---|---|---|---|---|
| 2026-06-10 | AgentDive Document Analysis | Viewed GitHub metadata, README/docs and partial source code paths | Public repository and generated AgentDive files | `partial` | Metadata and first round analysis have been recorded; local run pass is not declared. | Continue to advance Level 2 and Level 3 missions. |
| 2026-06-11 | Windows, Node v24.16.0, npm 11.9.0, Git 2.54.0 | `git clone --no-tags --depth 1 https://github.com/colbymchenry/codegraph .cache/sources/colbymchenry__codegraph`; `git rev-parse HEAD` | `.cache/sources/colbymchenry__codegraph` | `pass` | Clone succeeded; HEAD is `16c73e2b0e027411e22039baeb32fbe60ab42b4c`. | Keep docs bound to this commit. |
| 2026-06-11 | Windows, Node v24.16.0, npm 11.9.0 | `npm ci --ignore-scripts` | `.cache/sources/colbymchenry__codegraph` | `pass` | 61 packages installed; npm audit reported 8 vulnerabilities. | Do not auto-fix dependencies; track as risk. |
| 2026-06-11 | Windows, Node v24.16.0, npm 11.9.0 | `npm run build` | `.cache/sources/colbymchenry__codegraph` | `pass` | `tsc`, asset copy, and CLI chmod step completed. | Build artifact available under `dist/`. |
| 2026-06-11 | Windows, Node v24.16.0 | `node dist/bin/codegraph.js --version`; `node dist/bin/codegraph.js --help` | `.cache/sources/colbymchenry__codegraph` | `pass` | Version `0.9.9`; help lists init, index, sync, status, query, serve, callers, callees, impact, affected, install, uninstall, upgrade. | CLI command surface verified; continue deeper runtime checks. |
| 2026-06-11 | Windows, Node v24.16.0 | `node dist/bin/codegraph.js init -i .` | `.cache/sources/colbymchenry__codegraph` | `pass` | Indexed 216 files; 3,533 nodes; 14,388 edges in 1.6s. | Index creation verified; continue status and query checks. |
| 2026-06-11 | Windows, Node v24.16.0 | `node dist/bin/codegraph.js status .` | `.cache/sources/colbymchenry__codegraph` | `pass` | Index is up to date; DB size 12.55 MB; backend `node:sqlite`; files: 216; nodes: 3,533; edges: 14,388. | Status verified; continue MCP and test-suite checks. |
| 2026-06-11 | Windows, Node v24.16.0, npm 11.9.0 | `npx vitest run __tests__/context.test.ts` | `.cache/sources/colbymchenry__codegraph` | `pass` | 1 test file passed; 17 tests passed. Vite CJS API deprecation warning shown. | Full test suite remains pending. |
| 2026-06-11 | Windows, Node v24.16.0 | `node dist/bin/codegraph.js query buildContext -p . --json` | `.cache/sources/colbymchenry__codegraph` | `pass` | Returned `ContextBuilder::buildContext`, `CodeGraph::buildContext`, `BuildContextOptions`, and related imports. | Use results for source-reading follow-up. |
| 2026-06-11 | Windows, Node v24.16.0 | `node dist/bin/codegraph.js callers buildContext -p . --json` | `.cache/sources/colbymchenry__codegraph` | `pass` | Returned valid JSON with empty `callers` array for the queried symbol. | Try additional symbols during source-reading if caller examples are needed. |
| 2026-06-11 | Windows, Node v24.16.0 | `node dist/bin/codegraph.js impact buildContext -p . --json` | `.cache/sources/colbymchenry__codegraph` | `pass` | Returned 2 affected `buildContext` method nodes in `src/context/index.ts` and `src/index.ts`. | Compare with manual source reading. |
| 2026-06-11 | Windows, Node v24.16.0 | `node dist/bin/codegraph.js serve --mcp --no-watch -p .`; line-based JSON-RPC `initialize`, `initialized`, `tools/list` | `.cache/sources/colbymchenry__codegraph` | `pass` | MCP initialize returned server `codegraph` version `0.9.9`; tools/list returned `codegraph_search`, `codegraph_callers`, `codegraph_callees`, `codegraph_impact`, `codegraph_node`, `codegraph_explore`, `codegraph_status`, `codegraph_files`. | Run a controlled `tools/call` only if later learning tasks require it. |

## Known gaps

- Full test suite is not run.
- npm audit reported 8 dependency vulnerabilities after `npm ci --ignore-scripts`.
- MCP `tools/call` behavior is not sampled; only initialize and tools/list are verified.

## Next action

- Compare codegraph_explore output with ordinary file search
- Optionally run one controlled MCP `tools/call` for `codegraph_status`.
- Run the full test suite or define an accepted focused test subset.

## Gold Sample Candidate

CodeGraph is the default gold-sample candidate. It remains `analyzing` until Level 3-6 learning evidence, accepted test-suite evidence, and final review notes are complete.

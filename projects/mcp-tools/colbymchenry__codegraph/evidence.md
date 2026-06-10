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
| Source review | `partial` | 已有首轮源码或文档分析，但函数级验证尚未完成。 |
| Diagrams | `draft` | 已有 Mermaid 图解；渲染产物和源码级准确性仍需复核。 |
| Learning notes | `created` | 学习笔记骨架已存在，后续必须随任务逐项更新。 |

## Command Evidence

| Date | Environment | Command / Operation | Scope | Result | Output summary | Follow-up |
|---|---|---|---|---|---|---|
| 2026-06-10 | AgentDive 文档分析 | 已查看 GitHub 元数据、README/docs 和部分源码路径 | 公开仓库和已生成的 AgentDive 文件 | `partial` | 已记录元数据和首轮分析；不声明本地运行通过。 | 继续推进 Level 2 和 Level 3 任务。 |
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

## 已知缺口

- Full test suite is not run.
- npm audit reported 8 dependency vulnerabilities after `npm ci --ignore-scripts`.
- MCP `tools/call` behavior is not sampled; only initialize and tools/list are verified.

## 下一步行动

- Compare codegraph_explore output with ordinary file search
- Optionally run one controlled MCP `tools/call` for `codegraph_status`.
- Run the full test suite or define an accepted focused test subset.

## Gold Sample Candidate

CodeGraph is the default gold-sample candidate. It remains `analyzing` until Level 3-6 learning evidence, accepted test-suite evidence, and final review notes are complete.


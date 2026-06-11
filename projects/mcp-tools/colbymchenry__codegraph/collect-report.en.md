# CodeGraph collect report

## 1. Basic information

- GitHub address: https://github.com/colbymchenry/codegraph
-Collect time: 2026-06-10
- Project name: CodeGraph
- Project ID: `colbymchenry__codegraph`
- Project Category: `mcp-tools`
-Collect level: Level A deep collect
- Current status: `analyzing`
-Whether collect is recommended: Yes
- collect Person/Agent: Codex

## 2. collect basis

- Relevance to AI Agent: Explicitly relevant. The project serves Claude Code, Codex CLI, Cursor, opencode, Hermes Agent, Gemini CLI, Antigravity IDE and Kiro through MCP Server.
- Project learning value: high. Covers MCP tools, code knowledge graph, tree-sitter, SQLite FTS5, reference resolution, impact surface analysis and Agent tool guidance.
- Engineering reference value: high. The source code includes complete engineering modules such as CLI, installer, MCP, extraction, resolution, graph, sync, and tests.
- Documentation and source code analyzeability: High. README, docs site, tests and TypeScript source code are complete.
- License preliminary judgment: MIT.
- Whether to repeat collect: The project was not found in `PROJECTS.md` before collecting.

## 3. Risk

- Operational risks: not installed, not run the CLI, and not verifying the MCP server.
- Maintenance risk: The language/framework coverage is very wide, and subsequent accuracy and compatibility maintenance costs are high.
- Security risk: MCP tools can return source code fragments, and enterprise use requires permissions and auditing.
- Document expiration risk: There are differences in the way instructions are written between the MCP Server page of site docs and the current README/source code.
- Conclusion Items to be verified: README benchmark, local indexing time, Windows installer, Agent actual calling experience, test suite status.

## 4. Generate file list

- [x] `projects/mcp-tools/colbymchenry__codegraph/README.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/project-analysis.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/source-code-reading.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/integration-guide.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/troubleshooting.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/learning-todo-list.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/collect-report.md`
- [x] `projects/mcp-tools/colbymchenry__codegraph/assets/diagrams/`
- [x] `learning-notes/colbymchenry__codegraph/`
- [x] `PROJECTS.md` Update
- [x] `LEARNING_PROGRESS.md` Update

## 5. Verified content

- GitHub API shows that the default branch is `main`, the main language is TypeScript, and the license is MIT.
- GitHub API is consistent with shallow clone commit: `16c73e2b0e027411e22039baeb32fbe60ab42b4c`.
- `package.json` Display npm package name `@colbymchenry/codegraph`, CLI bin `codegraph`, test command `vitest run`.
- The source code includes CLI, MCP, installer, extraction, resolution, graph, sync, db, tests and other modules.
- Both the README and source code show that the new version of tool guidance is provided by MCP initialize response and no longer relies on writing `CLAUDE.md` / `AGENTS.md`.

## 6. Unverified content

- The installer was not executed.
- `codegraph init -i` is not executed.
- not run `npm test`。
- `codegraph serve --mcp` is not actually started.
- README benchmark not verified.
- The accuracy of each language and framework resolver is not confirmed.

## 7. Matters awaiting manual confirmation

- [ ] Whether the License meets the citation and learning arrangement strategies of this warehouse.
- [ ] Whether Level A collect meets the maintenance priority.
- [ ] Do you want to add a comparative analysis with `codebase-memory-mcp`?
- [ ] Whether to actually install it on this machine and use it for a sample repository.
- [ ] Whether to use the README benchmark as a subsequent replication experiment.

## 8. Next step suggestions

Follow-up actions: Prioritize running through the smallest closed loop. Select a public medium-sized TypeScript repository, execute `codegraph init -i`, `codegraph status`, `codegraph query`, `codegraph impact`, and then verify in Codex or Claude Code whether the MCP tools return conforms to the README description.

## 9. Information snapshot

- Snapshot date: 2026-06-10
- GitHub API：https://api.github.com/repos/colbymchenry/codegraph
- README：https://raw.githubusercontent.com/colbymchenry/codegraph/main/README.md
- GitHub page: https://github.com/colbymchenry/codegraph
- Official documentation: https://colbymchenry.github.io/codegraph/

# Graphify collect report

## 1. Basic information

- GitHub address: https://github.com/safishamsi/graphify
-Collect time: 2026-06-10
- Time of this review: 2026-06-11
- Project name: Graphify
- Project ID: `safishamsi__graphify`
- Project Category: `agentic-coding`
-Collect level: Level B standard collect
- Current status: `analyzing`
-Whether collect is recommended: Yes
- collect Person/Agent: Codex

## 2. collect basis

- Relevance to AI Agent: README is explicitly oriented to AI coding assistants such as Claude Code, Codex, OpenCode, Cursor, Gemini CLI, etc.
- Project learning value: Covers knowledge graph, context engineering, Tree-sitter static analysis, non-code semantic extraction, skill installation, hook, MCP server and other topics.
- Project reference value: It can be used as a project example of "how the coding agent queries the project knowledge graph".
- Documentation and source code analyzeability: The repository contains README, docs, `ARCHITECTURE.md`, `SECURITY.md`, `graphify/`, `tests/` and `pyproject.toml`.
- License preliminary judgment: GitHub API displays MIT License.
- Whether to repeat collect: The `safishamsi__graphify` entry already exists; this time, it will be processed according to the existing collect review and metadata refresh, and the directory will not be created repeatedly.
- 2026-06-11 Review: GitHub API displays default branch `v8`, main language Python, License MIT, stars `64743`, forks `6578`, open_issues_count `328`; `git ls-remote --symref` displays HEAD as still `5504c84324fc9249eb4c9d0cca86da7140250032`.

## 3. Risk

- Operational risk: `graphifyy` has not been installed natively, CLI, extras and platform installers have not been verified.
- Maintenance risk: The project is updated frequently, and the README, platform list and parameters may change rapidly.
- Security risk: README states that code AST extraction is performed locally, but semantic extraction of docs, PDFs, and images may involve external models/assistant backends; data outgoing boundaries must be confirmed before use in private warehouses.
- Document expiration risk: The current text data is based on the 2026-06-10 snapshot and commit `5504c84324fc9249eb4c9d0cca86da7140250032`; on 2026-06-11 only the public GitHub metadata was refreshed, and the source code level analysis was not re-done.
- Conclusion Items to be verified: CLI call chain, Codex hook writing behavior, MCP server tool protocol, Tree-sitter extraction details, cache and ignore rules.

## 4. Generate file list

- [x] `projects/agentic-coding/safishamsi__graphify/README.md`
- [x] `projects/agentic-coding/safishamsi__graphify/meta.json`
- [x] `projects/agentic-coding/safishamsi__graphify/project-analysis.md`
- [x] `projects/agentic-coding/safishamsi__graphify/source-code-reading.md`
- [x] `projects/agentic-coding/safishamsi__graphify/integration-guide.md`
- [x] `projects/agentic-coding/safishamsi__graphify/troubleshooting.md`
- [x] `projects/agentic-coding/safishamsi__graphify/learning-todo-list.md`
- [x] `projects/agentic-coding/safishamsi__graphify/collect-report.md`
- [x] `projects/agentic-coding/safishamsi__graphify/assets/diagrams/`
- [x] `learning-notes/safishamsi__graphify/`
- [x] `PROJECTS.md` Update
- [x] `LEARNING_PROGRESS.md` Update

## 5. Matters awaiting manual confirmation

- [ ] Whether the License meets the target publishing and citation methods.
- [ ] `graphify .` Whether it is possible to test the warehouse on this machine.
- [ ] Whether the writing range of `graphify install --project --platform codex` is as expected.
- [ ] Whether the core call chain is consistent with the source code.
- [ ] Whether the diagrams are consistent with the source code and running results.
- [ ] Whether it should be upgraded to Level A depth collection in the future.

## 6. Next step suggestions

1. Use the public small warehouse to complete `graphify .` minimum operation verification.
2. Read `ARCHITECTURE.md`, `SECURITY.md` and `docs/how-it-works.md` to complete the security and architectural boundaries.
3. Verify the source code level call chain along `graphify.__main__:main` and `graphify.serve:_main`.
4. Verify the actual file written by Codex project install, and then decide whether to advance the status to `study-ready`.

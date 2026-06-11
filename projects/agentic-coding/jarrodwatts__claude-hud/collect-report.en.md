# Claude HUD collect report

## 1. Basic information

- GitHub address: https://github.com/jarrodwatts/claude-hud
-Collect time: 2026-06-11
- Project name: Claude HUD
- Project ID: `jarrodwatts__claude-hud`
- Project Category: `agentic-coding`
-Collect level: Level B standard collect
- Current status: `analyzing`
-Whether collect is recommended: Yes
- collect Person/Agent: Codex

## 2. collect basis

- Relevance to AI Agent: README is clearly described as Claude Code plugin, serving Claude Code session state display.
- Project learning value: Covers statusline API, context usage, rate limits, transcript JSONL, tool/agent/todo activity, MCP/Skill activity and configuration governance.
- Engineering reference value: TypeScript ESM, cross-platform setup, configuration verification, terminal width processing, caching, external usage snapshot, Node test suite.
- Documentation and source code analyzeability: The warehouse contains README, Chinese README, setup/configure commands, src, dist, tests, plugin manifest and package configuration.
- License preliminary judgment: `package.json` and plugin manifest show MIT.
- Whether to repeat collect: Repeat the check before collect and no existing entries of `jarrodwatts__claude-hud` or `jarrodwatts/claude-hud` were found.

## 3. Risk

- Run risk: The plugin is not installed or setup is executed in the real Claude Code.
- Configuration risk: setup will modify `statusLine.command` of user-level `settings.json`, and may replace other statuslines.
- Platform risk: The command formats of Windows PowerShell, Git Bash/MSYS2, WSL, macOS/Linux are significantly different.
- API risk: GitHub REST API is limited during collect, and the accurate stars/forks metadata is approximated by the GitHub page.
- Test risk: Temporary Windows shallow clone `npm test` fails, cannot declare test passed.
- Drift risk: Claude Code statusline stdin and transcript JSONL schema may change with Claude Code version.

## 4. Generate file list

- [x] `projects/agentic-coding/jarrodwatts__claude-hud/README.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/meta.json`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/project-analysis.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/source-code-reading.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/integration-guide.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/troubleshooting.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/learning-todo-list.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/collect-report.md`
- [x] `projects/agentic-coding/jarrodwatts__claude-hud/assets/diagrams/`
- [x] `learning-notes/jarrodwatts__claude-hud/`
- [x] `PROJECTS.md` Update
- [x] `LEARNING_PROGRESS.md` Update

## 5. Verified content

- GitHub repository exists publicly.
- GitHub page displays README positioning, stars/forks/issues/PRs overview.
- raw README shows installation commands, feature targeting, configuration options, usage limits, troubleshooting, requirements, and development commands.
- raw `package.json` displays the project name, version, Node engine, scripts, license and TypeScript dependencies.
- Shallow clone HEAD: `9650a43600e9bcc94057fbd693a7f05aba4ee1ff`.
- Source code sampling: `.claude-plugin/plugin.json`, `commands/setup.md`, `commands/configure.md`, `src/index.ts`, `src/stdin.ts`, `src/transcript.ts`, `src/config.ts`, `src/render/index.ts`, `src/git.ts`, `src/external-usage.ts`.
- Local temporary test: `npm ci` successful; `npm test` exit code 1.

## 6. Matters awaiting manual confirmation

- [ ] Complete stars/forks/issues metadata using the authenticated GitHub API or subsequent refreshes.
- [ ] Execute marketplace add, install, reload and setup in real Claude Code.
- [ ] Verify setup's backup, query, and restore paths for existing statuslines.
- [ ] Verify command format for Windows PowerShell, Windows Git Bash, WSL, macOS/Linux.
- [ ] Sample real statusline stdin and transcript JSONL.
- [ ] Locate `npm test` Whether the Windows failure item is an environment difference or an upstream regression.
- [ ] Verify the display boundary of usage/cost in subscriber, API-key-only, Bedrock, and Vertex scenarios.

## 7. Next step suggestions

1. First use temporary `CLAUDE_CONFIG_DIR` to verify the setup writing and backup logic.
2. Install the plugin in the real Claude Code test profile and complete a restart verification.
3. If the Windows test fails, first run `tests/core.test.js`, `tests/external-usage.test.js`, `tests/extra-cmd.test.js`, `tests/git.test.js` and `tests/integration.test.js` separately.
4. Collect the real transcript and update the calling chain evidence of `source-code-reading.md`.
5. Compare the agentic-coding tool layer with RTK, Caveman, and CodeGraph: what problems do output compression, input compression, code graph, and runtime HUD solve respectively.

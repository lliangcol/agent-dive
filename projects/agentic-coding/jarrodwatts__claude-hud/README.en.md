# Claude HUD

Claude HUD is a Claude Code plugin that renders a live statusline below the input area. It surfaces model/project identity, context usage, subscriber usage windows, git state, tool activity, subagent activity, MCP/skill activity, todos, session metadata, and optional local system information.

## collect information

| Field | value |
|---|---|
| Project name | Claude HUD |
| Project ID | `jarrodwatts__claude-hud` |
| GitHub | https://github.com/jarrodwatts/claude-hud |
| Project home page | https://github.com/jarrodwatts/claude-hud |
| Main category | `agentic-coding` |
| Auxiliary tags | `claude-code`、`statusline`、`context-observability`、`usage-limits`、`transcript-jsonl`、`tool-activity`、`developer-tooling` |
| collectlevel | Level B standard collect |
| Current status | `analyzing` |
| Default branch | `main` |
| collect snapshot | 2026-06-11 |
| Analysis Commit | `9650a43600e9bcc94057fbd693a7f05aba4ee1ff` |
| package version | `0.1.1` |
| Whether to run verification locally | no |

## Why collect

- Explicitly related to the AI ​​Coding Agent: it directly connects to the Claude Code plugin / statusLine mechanism to observe the Claude Code session status.
- Clear learning value: suitable for learning Claude Code statusline stdin, transcript JSONL, tool call activity analysis, context usage display, rate limit display and configuration migration.
- High engineering reference value: The source code includes the TypeScript statusline main program, cross-platform setup instructions, configuration verification, git status reading, transcript cache, external usage snapshot, rendering width processing and Node test suite.
- Complementary to existing AgentDive samples: it is not a new Agent loop, but an Agent runtime observability and Claude Code user experience enhancement tool.

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
- The GitHub page shows that the warehouse is `jarrodwatts/claude-hud`, and the README is located as Claude Code plugin.
- GitHub page snapshot shows about 24.9k stars, about 1.1k forks, 1 open issue and 1 PR.
- `git clone --depth 1` gets the default branch `main`, and the HEAD is `9650a43600e9bcc94057fbd693a7f05aba4ee1ff`.
- `package.json` Displays the project name `claude-hud`, version `0.1.1`, TypeScript/ESM, Node `>=18.0.0`, and License `MIT`.
- Read `.claude-plugin/plugin.json`, `commands/setup.md`, `commands/configure.md`, `src/index.ts`, `src/stdin.ts`, `src/transcript.ts`, `src/config.ts`, `src/render/index.ts` and several render / usage / git modules.
- Executed `npm ci` and `npm test` in a Windows temporary shallow clone. The dependency installation was successful, `npm run build` was completed in the test process, but the exit code of `npm test` was 1, and 31 unique failed test names were sampled in the output, mainly focusing on config count, external usage, extra command, git, entrypoint, and integration rendering assertions.

Not verified:

- `/plugin marketplace add jarrodwatts/claude-hud`, `/plugin install claude-hud` or `/claude-hud:setup` are not executed in real Claude Code.
- The real plug-in installation, statusline writing or HUD display has not been run through; therefore, the "Whether it has been run through" in `PROJECTS.md` for this project is still recorded as "No".
- Unverified real `statusLine` configuration writing, existing statusline backup, HUD display after Windows `statusline.mjs` wrapper and Claude Code restart.
- The real Claude Code stdin `rate_limits`, transcript_path, background agent, TodoWrite, MCP tool name and other runtime payloads have not been verified.
- The approximately 300ms refresh experience in README is not reproduced.
- Unconfirmed whether the Windows test failure comes from current native environment differences, dependency versions, Git Bash/PowerShell differences, or current regressions in the project.

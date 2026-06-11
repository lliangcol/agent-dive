# Claude HUD project deep dive

## 1. Basic project information

- Project name: Claude HUD
- Project ID: `jarrodwatts__claude-hud`
- GitHub：https://github.com/jarrodwatts/claude-hud
- Category: `agentic-coding`
-Collect level: Level B standard collect
- Current status: `analyzing`
- Main language: TypeScript
- License：MIT
- Analysis date: 2026-06-11
- Analysis version/Commit:`9650a43600e9bcc94057fbd693a7f05aba4ee1ff`
- Default branch: `main`
- Package version: `0.1.1`
- Whether to run verification: No. Executed `npm ci` and `npm test` in temporary shallow clones, but tests failed; HUD is not installed or enabled in real Claude Code.
- Analysis basis: GitHub page, raw README, raw `package.json`, shallow clone source code, `.claude-plugin/plugin.json`, `commands/setup.md`, `commands/configure.md`, `src/index.ts`, `src/stdin.ts`, `src/transcript.ts`, `src/config.ts`, `src/render/index.ts`, `src/external-usage.ts`, `src/git.ts`, test output.

## 2. Positioning in one sentence

Claude HUD is a Claude Code statusline plug-in that renders the context window of a Claude Code session, subscription usage, tool activity, sub-agents, Todo, git status, and configuration status into an always-visible terminal HUD.

## 3. Problems solved by the project

The key state of a Claude Code session is scattered across @PH0@@, transcript, settings, git, MCP configuration, hooks, and user memory files. Users often need to actively query to know the current status when performing long tasks, parallel sub-agents, complex tool calls, or approaching the context limit.

The learning value of Claude HUD is:

- Observation layer design: Do not change the Agent loop, but use the statusline API to provide low-invasive runtime observation.
- Context management: Directly read the context window information in Claude Code stdin, give priority to the official used percentage, and then do fallback.
- Activity summary: parse transcript JSONL and convert tool, Skill, MCP, Task/Agent, TodoWrite, TaskCreate/TaskUpdate into short status lines.
- Configuration management: Use `config.json` to support layout, language, threshold, color, git style, usage display, external usage snapshot and other options.
- Cross-platform setup: `/claude-hud:setup` Explicitly handles macOS/Linux, Windows PowerShell, Windows Git Bash/MSYS2, WSL, Bun/Node differences, and existing statusline backups.

## 4. Project main line

Typical main lines are as follows:

1. The user adds marketplace in Claude Code and installs `claude-hud` plugin.
2. The user executes `/claude-hud:setup`.
3. The setup command checks ghost install, platform/shell/runtime, existing statusLine, and generates the appropriate statusLine command.
4. Setup command backs up and updates Claude Code `settings.json`’s `statusLine.command`.
5. Every time Claude Code refreshes statusline, pass stdin JSON to `dist/index.js` or wrapper.
6. `src/index.ts` Read stdin, parse transcript, read configuration, git, usage, memory, version and extra command.
7. The render layer outputs one to multiple rows of HUD according to the compact / expanded layout.

Not verified: Steps 1 to 5 were not executed in a real Claude Code environment. What is confirmed this time is the source code and command document design.

## 5. Quick Start

Installation path given in README:

1. Run `/plugin marketplace add jarrodwatts/claude-hud` in Claude Code.
2. Run `/plugin install claude-hud`.
3. Run `/reload-plugins`.
4. Run `/claude-hud:setup`.
5. Restart Claude Code to make the new `statusLine` configuration take effect.

Environmental requirements:

- Claude Code v1.0.80+。
- macOS/Linux: Node.js 18+ or Bun.
- Windows: Node.js 18+, the setup document clearly requires Windows to use Node instead of Bun.

The current repository does not perform real plugin install or setup writing. Since setup will write user-level Claude Code configuration, only the source code and temporary test verification will be done this time.

## 6. Core architecture

| module | effect | in accordance with | Verification status |
|---|---|---|---|
| `.claude-plugin/plugin.json` | Claude Code plugin manifest, declares setup/configure commands | manifest | Read |
| `commands/setup.md` | Generate and write statusLine command, handle platform, runtime, existing statusline, backup and verification | setup command | Read, not actually executed |
| `commands/configure.md` | guided config flow, modify HUD layout, language, preset and display elements | configure command | Read, not actually executed |
| `src/index.ts` | statusline main entrance, summarizes stdin, transcript, config, git, usage, memory, version and then renders | Source code | Read |
| `src/stdin.ts` | Read Claude Code stdin JSON, calculate context percent, parse rate_limits and provider label | Source code | Read |
| `src/transcript.ts` | Streaming parsing transcript JSONL, extraction tools, Skill, MCP, Agent, Todo, session tokens, advisor, etc. | Source code | Read |
| `src/config.ts` | Default configuration, configuration migration, type checking, color and threshold constraints | Source code | Read |
| `src/render/` | compact / expanded rendering, width calculation, ANSI/OSC8 processing, activity lines | Source code | Read |
| `src/git.ts` | Get branch, dirty, ahead/behind, file stats, line diff and GitHub branch URL | Source code | Read |
| `src/external-usage.ts` | Read or write external usage snapshot, support balance label and freshness verification | Source code | Read |
| `tests/` | Node test suite, covering config, stdin, transcript, render, git, integration, etc. | test output | Run, failed for current Windows environment |

See `assets/diagrams/architecture.mmd`, `statusline-flow.mmd`, `transcript-activity-flow.mmd` and `setup-config-flow.mmd` for draft diagrams.

## 7. Core Principles

### Statusline stdin driver

`src/index.ts` calls `readStdin()`. If there is no stdin, an initialization prompt will be output for setup verification. If there is stdin, read the `transcript_path`, `cwd`, `context_window`, `rate_limits`, `model` and other fields provided by Claude Code.

Basis: `src/index.ts`, `src/stdin.ts`.

### Context and usage display

context percent preferentially uses `context_window.used_percentage` provided by newer versions of Claude Code. If this field is missing or unfilled with 0, the source code then calculates it based on the token and context window size. Subscriber usage is read through `rate_limits`; routed providers such as Bedrock / Vertex have special display boundaries.

Basis: `src/stdin.ts`, README.

### Transcript activity analysis

`src/transcript.ts` Read JSONL line by line and extract:

- tool_use/tool_result: Tool running and completion status.
- `Skill` Tool: active skill.
- `mcp__server__tool` Naming pattern: MCP server activity.
- `Task` / `Agent`: sub-Agent, supports background completion.
- `TodoWrite`、`TaskCreate`、`TaskUpdate`：todo progress。
- assistant usage: session token accumulation.
- `compact_boundary`: Distinguish between compressed real low token and stdin glitch.

Basis: `src/transcript.ts`.

### Configuration and Rendering

`src/config.ts` provides a default expanded layout and allows users to adjust by element order, merge groups, colors, thresholds and switches. The render layer handles ANSI, OSC8 hyperlink, CJK/emoji width, truncation, and line wrapping to try to avoid broken statuslines.

Basis: `src/config.ts`, `src/render/index.ts`.

### Project boundaries of Setup

`commands/setup.md` is one of the heaviest engineering documents of the project. It requires ghost install to be detected first, and then the statusLine command is generated according to the platform; backup is done before writing `settings.json`, and the user is asked when encountering an existing statusline. The Windows PowerShell path also generates a Node launcher to avoid slow startup of PowerShell or cache glob errors every time it is refreshed.

Basis: `commands/setup.md`.

## 8. Key call chain

### Call chain 1: statusline rendering

- Starting point: Claude Code calls `statusLine.command`, and stdin passes in statusline JSON.
- Key steps: `readStdin` -> `parseTranscript` -> `applyContextWindowFallback` -> `countConfigs` -> `loadConfig` -> `getGitStatus` -> `getUsageFromStdin` / external snapshot -> `render`.
- Endpoint: stdout output HUD lines.
- Status: Source code confirmed, not verified in real Claude Code statusline.

### Call chain 2: transcript to active line

- Starting point: `transcript_path` in stdin.
- Key steps: canonicalize path -> stat/cache -> stream JSONL -> process tool_use / tool_result / queue-operation / Todo records -> write transcript cache.
- End point: The render layer gets tools, skills, mcpServers, agents, todos, sessionName and sessionTokens.
- Status: Source code confirmed; real transcript payload has not been sampled for verification.

### Call chain 3: setup writes statusLine

- Starting point: User executes `/claude-hud:setup`.
- Key steps: Detect ghost install -> Detect platform/shell/runtime -> Locate plugin cache version -> Generate statusLine command -> Test command -> Back up `settings.json` -> Process existing statusline -> Write JSON.
- Endpoint: Claude Code calls HUD after restart.
- Status: Command document confirmed; writing not performed.

### Call chain 4: guided configure

- Starting point: User executes `/claude-hud:configure`.
- Key steps: Read `~/.claude/plugins/claude-hud/config.json` -> Select problem flow by new user or existing configuration -> Generate preview -> Write config.
- Endpoint: HUD reads new configuration and changes layout / language / displayed elements.
- Status: Command document confirmed; writing not performed.

## 9. integration method

It is recommended to do three layers of verification first:

1. Temporary source code verification: execute `npm ci`, `npm run build` in shallow clones, and selectively run non-environment sensitive tests.
2. Isolate Claude configuration verification: set up temporary `CLAUDE_CONFIG_DIR`, exercise setup command generation and `settings.json` writing logic.
3. Real Claude Code verification: After confirming that there is a statusline backup, install the plugin, run setup, restart Claude Code, and display it with the minimum transcript scenario verification tool /agent/todo/usage.

It is currently not recommended to directly skip the backup execution setup in the main Claude Code configuration.

## 10. Problemshooting

Priority troubleshooting direction:

- GitHub API rate limit: The REST API has been limited during collect, and GitHub pages, raw files, and shallow clones can be returned.
- Windows runtime: README and setup documents require Node.js LTS for Windows; Bun path only works on macOS/Linux.
- Existing configuration of statusLine: setup will replace `statusLine.command`, you must back it up first and confirm whether it overwrites other statuslines.
- shell mismatch: Windows + Git Bash/MSYS2 should not use the PowerShell command format.
- usage is not displayed: when API-key-only, Bedrock, Vertex or `rate_limits` is missing, usage display is bounded.
- Test failed: The current Windows staging environment `npm test` failed and the test suite cannot be marked as passed.

## 11. Objective evaluation

### advantage

- Use Claude Code's native statusline, stdin payload and transcript JSONL as a lightweight observation layer.
- The setup documentation is very specific on handling cross-platform, existing configuration backup, ghost install, and Windows shell mismatch.
- Configuration validation and render width processing are finer, suitable for learning the boundary conditions of terminal UI.
- Do not rely on private API to capture subscriber usage, preferentially use Claude Code's official stdin information.

### shortcoming

- The function is strongly dependent on the Claude Code statusline API and transcript format, and may drift as the Claude Code version changes.
- The setup process will write user-level configuration, and incorrect operations may overwrite the existing statusline.
- There are currently failed items in the Windows temporary test output, and further determination is needed to determine whether it is a project regression or an environment difference.
- It is an observability HUD, not a full tracing, evaluation or audit system.

### Applicable scenarios

- Learn Claude Code plugin and statusline mechanism.
- Investigate Agent session state visualization and context usage reminders.
- Research transcript JSONL activity parsing.
- Provide low-invasive status prompts for long tasks, parallel Agents, and complex tool calling scenarios.

### not applicable scenario

- The scope of Claude HUD is too local when it is necessary to unify the observability backend across agents/cross-models.
- The HUD status line is not a sufficient replacement for a logging system when compliance auditing or reproducible evaluation is required.
- When there is no backup of the main configuration, it is not suitable to directly overwrite the existing statusline.

## 12. Learning Todo List

See [learning-todo-list.md](learning-todo-list.en.md). It is recommended to first verify the setup write boundary and Windows test failure before doing a real Claude Code installation experience.

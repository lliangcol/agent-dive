# Claude HUD source reading record

## 1. Reading objectives

- Questions to understand in this round: How does Claude HUD generate real-time HUD through Claude Code statusline stdin and transcript JSONL.
- Related functions: plugin manifest, setup/configure command, stdin parsing, context/usage calculation, transcript activity parsing, configuration merging, git status, render width processing, test suite.
- Expected output: Confirm core module boundaries, key call chains, writing scope, test risks and subsequent source reading sequence.

## 2. Source code entry

| Entrance | path | effect | in accordance with |
|---|---|---|---|
| Plugin manifest | `.claude-plugin/plugin.json` | Declare Claude Code plugin metadata and commands | manifest |
| Setup command | `commands/setup.md` | Detect platform and runtime, generate and write statusLine command | command documentation |
| Configure command | `commands/configure.md` | guided flow Modify HUD layout, preset, language and display options | command documentation |
| Statusline main entrance | `src/index.ts` | Read stdin, parse transcript, load configuration and call render | Source code |
| Stdin parsing | `src/stdin.ts` | Read Claude Code statusline JSON, calculate context and usage | Source code |
| Transcript parsing | `src/transcript.ts` | Parse JSONL and extract tools, skills, MCP, agents, todos, tokens | Source code |
| Configuration | `src/config.ts` | Default configuration, migration, verification, path | Source code |
| rendering | `src/render/index.ts` | compact/expanded layout, width, truncation, line wrapping | Source code |
| Tests | `tests/` | Node test suite | Run, failed for current Windows environment |

## 3. Module map

| module | path | Responsibilities | Dependencies |
|---|---|---|---|
| Plug-in distribution | `.claude-plugin/`、`commands/` | Claude Code plugin metadata and slash commands | Claude Code plugin runtime |
| main program | `src/index.ts` | Arrange reading, parsing, configuration, git, usage, render | Call multiple local modules |
| input layer | `src/stdin.ts`、`src/types.ts` | statusline stdin schema and rate limit/context parsing | Claude Code stdin payload |
| transcript layer | `src/transcript.ts` | JSONL stream parse、activity cache、agent/todo/session tokens | transcript file path |
| Configuration layer | `src/config.ts`、`src/config-reader.ts`、`src/claude-config-dir.ts` | HUD config, Claude config/rules/MCP/hook count, path positioning | `CLAUDE_CONFIG_DIR`、home dir、project cwd |
| status source | `src/git.ts`、`src/memory.ts`、`src/version.ts`、`src/external-usage.ts`、`src/extra-cmd.ts` | git, RAM, Claude version, usage snapshot, external command tags | OS, git, file system, child process |
| render layer | `src/render/` | line renderers, colors, widths, activity lines | ANSI terminal |
| internationalization | `src/i18n/` | English and Simplified Chinese labels | config language |
| test | `tests/` | Unit and integration testing | Node test runner |

## 4. Recommended reading order

1. `README.md`: Confirm function positioning, installation path, configuration options and limitations.
2. `.claude-plugin/plugin.json`: Confirm the Claude Code plugin distribution method.
3. `commands/setup.md`: Understand statusLine writing, backup, and cross-platform runtime selection.
4. `src/index.ts`: Read it along the main link.
5. `src/stdin.ts`: Understand context percent, rate limits, provider label.
6. `src/transcript.ts`: Understand activity parse and cache.
7. `src/config.ts`: Understand defaults, migration and validation.
8. `src/render/index.ts` and `src/render/*-line.ts`: Understand the display strategy.
9. `src/config-reader.ts`, `src/external-usage.ts`, `src/git.ts`: locate modules related to the current test failure.
10. `tests/core.test.js`, `tests/integration.test.js`, `tests/git.test.js`: Explanation Windows test failed.

## 5. Key call chain

### Call chain 1: Main rendering link

- Trigger condition: Claude Code calls statusLine command and passes in JSON through stdin.
- Starting point: `main()` of `src/index.ts`.
- Key steps: read stdin -> parse transcript -> context fallback -> count configuration -> read HUD config -> git status -> usage data -> extra command -> version/memory/effort -> render.
- Endpoint: stdout outputs a set of HUD lines.
- Error handling: Output `[claude-hud] Error: ...` after the main entrance catch.

### Call chain 2: stdin and context percent

- Starting point: `readStdin()`.
- Key steps: read only without TTY; set first byte / idle timeout; limit to 256 KB; try JSON parse; calculate context percent.
- Endpoint: Returns `StdinData` or `null`.
- Point of concern: `used_percentage=0` of fresh session will fallback to token calculation to prevent the initial system prompt from being hidden.

### Call chain 3: transcript activity

- Starting point: `parseTranscript(transcriptPath)`.
- Key steps: canonicalize path -> read file state -> return if cache is hit -> stream read JSONL -> process tool blocks -> process queue-operation completion -> update cache.
- Endpoint: `TranscriptData` Contains tools, skills, mcpServers, agents, todos, sessionStart, sessionName, sessionTokens, advisorModel, etc.
- Point of concern: The completion time of background agent comes first from queue-operation, not just tool_result.

### Call chain 4: setup writes configuration

- Starting point: `/claude-hud:setup` command.
- Key steps: Detect ghost install -> Detect platform/shell/runtime -> Generate command -> Test command -> Detect existing statusline -> Back up settings -> Write JSON.
- End point: `settings.json` including `statusLine: { type: "command", command: ... }`.
- Point of concern: The existing statusline may belong to other tools, and the replacement must be explicitly confirmed.

## 6. Key points of read code

- The dependencies of `src/index.ts` can be covered by `MainDeps` for easy testing.
- `src/stdin.ts` Made provider label and usage/cost boundary processing for Bedrock / Vertex / enterprise plan alias.
- `src/transcript.ts` Clean up ANSI and control characters in activity names, and limit the display length.
- The transcript cache path uses the sha256 of transcript path and is written as `plugins/claude-hud/transcript-cache/`.
- `src/config.ts` has migration logic from legacy `layout` to `lineLayout/showSeparators`.
- The render layer turns off OSC8 hyperlink truncation to prevent subsequent text in the terminal from being wrapped in incorrect underlines.
- `src/external-usage.ts` only accepts absolute `.json` write paths and does not create missing parent directories.

## 7. This round of test records

Execute in a temporary shallow clone:

```text
npm ci
npm test
```

result:

- `npm ci` Successful, 62 packages installed, audit shows 0 vulnerabilities.
- `npm test` executes `npm run build && node --test`.
- `npm run build` is done in the `npm test` process and the tests are subsequently run by the Node test runner.
- `npm test` Exit code is 1.
- Failures were sampled to 31 unique test names, concentrated in:
- `countConfigs` and config cache.
- `writeExternalUsageSnapshot` File permission assertion.
  - `runExtraCmd` JSON output。
- `getGitStatus` `mkdir` / file name scenario under Windows.
  - `index` direct entrypoint。
  - integration output newline / added dirs layout。
  - `getClaudeCodeVersion` Windows command resolution。

This result can only show that the test in the current Windows collect environment has failed, and cannot directly conclude that the upstream main must not be available; the next step should be to compare the environment recommended by the maintainer with the CI environment.

## 8. To-do check items

- [ ] Verify in real Claude Code whether the HUD appears after plugin install, setup, and restart.
- [ ] Use temporary `CLAUDE_CONFIG_DIR` to reproduce setup writing without touching the main configuration.
- [ ] Explain `npm test` Windows failure items, distinguishing environmental issues from project regressions.
- [ ] Collect a real statusline stdin JSON sample and confirm that the fields are consistent with `src/types.ts`.
- [ ] Collect a real transcript JSONL and verify the tools / agents / todos / MCP display.
- [ ] Verify differences in permission modes of `display.externalUsageWritePath` on Windows and POSIX.
- [ ] Verify setup command selection for PowerShell, Git Bash, WSL.
- [ ] Verify that statusline backup and restoration paths exist.
- [ ] Verify Chinese labels and CJK width handling.
- [ ] Verify if Bedrock / Vertex / API-key-only scenario usage/cost is hidden or downgraded per doc.

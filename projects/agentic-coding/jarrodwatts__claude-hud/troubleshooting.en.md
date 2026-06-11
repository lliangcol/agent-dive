# Claude HUD problem troubleshooting record

## 1. Current known issues

| question | state | in accordance with | Next step |
|---|---|---|---|
| GitHub API rate limit | Encountered | `Invoke-RestMethod` Return API rate limit exceeded | Use GitHub pages, raw files, and shallow clones; the authentication API can be used later to complete accurate metadata |
| Windows staging environment `npm test` failed | Encountered | `npm test` Exit code 1, sampled 31 unique failed test names | Compare in CI / macOS/Linux / Git Bash / PowerShell 7 |
| True Claude Code install not verified | Not verified | plugin install/setup was not executed this time | Use temporary Claude profile to verify writing first |
| statusLine may override other tools | risk | `commands/setup.md` Explicitly detect existing statusline and ask | Back up settings before execution |
| Windows runtime / shell mismatch | risk | The setup document distinguishes between PowerShell, cmd, Git Bash, MSYS2, and Cygwin | Run shell detection first, do not mix command formats |

## 2. Troubleshooting during installation phase

### The plug-in cannot be installed

Priority confirmation:

- Claude Code plugin marketplace is available.
- Whether `/plugin marketplace add jarrodwatts/claude-hud` has been executed.
- Whether `/plugin install claude-hud` has been executed.
- Whether `/tmp` and home cross file systems on Linux, resulting in `EXDEV: cross-device link not permitted`.
- Whether there is a ghost install: the cache has a directory but the registry has no records, or the registry has records but the cache is missing.

Basis: README, `commands/setup.md`.

### Windows prompts that JavaScript runtime cannot be found

The README and setup documents require Node.js LTS for Windows.

Command to be verified:

```powershell
Get-Command node -ErrorAction SilentlyContinue
```

If it cannot be found, you need to install Node.js LTS and restart the shell, then re-execute `/claude-hud:setup`.

### PowerShell command fails under Git Bash/MSYS2

The setup document clearly states: In a Windows + Git Bash/MSYS2/Cygwin environment, bash will expand PowerShell variables first, causing the PowerShell command format to be unsafe. You should take the Windows + Git Bash branch.

## 3. HUD not displayed

Priority checks:

- Whether to completely restart Claude Code after setup is written.
- `settings.json` Is there `statusLine.command`.
- Is there any output if statusLine command is executed manually?
- Whether the plugin cache can locate the latest `claude-hud` version directory.
- Whether the Windows PowerShell path generated the `statusline.mjs` wrapper.
- Whether stdout only displays initializing, and whether parsing fails due to command path or plugin dir.

## 4. Usage is not displayed

Possible reasons:

- Currently API-key-only usage, no Claude subscriber `rate_limits`.
- Claude Code has not completed the first round of model responses and `rate_limits` has not yet been populated.
- When provider routed sessions such as Bedrock / Vertex are used, the usage/cost display will be hidden or downgraded.
- `display.showUsage` is set to `false`.
- The external usage snapshot path is invalid, expired, JSON schema is invalid, or freshness times out.

Basis: README, `src/stdin.ts`, `src/external-usage.ts`.

## 5. Tools/Agent/Todo line is not displayed

Possible reasons:

- The default or current value of `display.showTools`, `display.showAgents`, `display.showTodos` in config is off.
- There are no records corresponding to tool_use, Task/Agent, TodoWrite/TaskCreate/TaskUpdate in transcript.
- transcript path is missing or cannot be read.
- The transcript cache hits the old state, and you need to confirm whether the file state is updated.
- The activity name is empty after being sanitized.

Basis: `src/transcript.ts`, `src/render/tools-line.ts`, `src/render/agents-line.ts`, `src/render/todos-line.ts`.

## 6. Current test failure summary

Commands for this round:

```text
npm ci
npm test
```

result:

- `npm ci` Success.
- `npm test` Exit code is 1.
- Failure sampling is concentrated in:
- `countConfigs` Configure counting and cache.
- `writeExternalUsageSnapshot` file permissions.
- `runExtraCmd` External command JSON output.
- `getGitStatus` Windows file/directory scenario.
  - `index entrypoint`。
- integration output newlines and added dirs layout.
  - `getClaudeCodeVersion` Windows command resolution。

Judgment boundaries:

- Cannot mark upstream tests as passing.
- You cannot assert that an item is unavailable based on native Windows failure alone.
- Requires comparison in upstream CI equivalent environment, Windows Git Bash, PowerShell 7, macOS/Linux.

## 7. Waiting for manual confirmation

- [ ] True Claude Code plugin install is successful.
- [ ] `/claude-hud:setup` Whether the correct statusLine command is generated.
- [ ] Existing statusline Whether backup and recovery are available.
- [ ] Windows `statusline.mjs` wrapper is written correctly without BOM.
- [ ] HUD whether to display tools / agents / todos under the real transcript.
- [ ] Test whether the failure is a Windows environment difference.

# RTK source reading record

## 1. Reading objectives

- Issues to be understood in this round: How RTK rewrites the original shell command into the `rtk` command, and how to execute, filter, and record the output.
- Related functions: CLI routing, command filters, hook rewrite, permission model, tracking, tee recovery, telemetry boundary.
- Expected output: Confirm source code entry, module map, key call chain and next round of source reading plan.

## 2. Source code entry

| Entrance | path | effect | in accordance with |
|---|---|---|---|
| CLI entry | `src/main.rs` | Clap command definition, `run_cli` distributed to each ecological module | Source code sampling |
| Hook rewrite entry | `src/hooks/rewrite_cmd.rs` | `rtk rewrite` command returns rewriting results based on permissions and registry | Source code sampling |
| Rewrite registry | `src/discover/registry.rs` | Identify supported commands, dismantle compound commands, and process ignored / unsupported | Source code sampling |
| Hook installer | `src/hooks/init.rs` | `rtk init` Install hook/guidance/plugin for different Agents | Source code sampling |
| Universal actuator | `src/core/runner.rs` | Capture native command output, call filter, record tracking | Source code sampling |
| Git filtering example | `src/cmds/git/git.rs` | `git status`, `diff`, `log` and other filtering implementations | Source code sampling |

## 3. Module map

| module | path | Responsibilities | Dependencies |
|---|---|---|---|
| CLI facade | `src/main.rs` | Command definition, parameter parsing, routing | Call `cmds`, `hooks`, `analytics`, `discover` |
| Command filters | `src/cmds/` | Filtering the output of each ecological command | Use `core::runner`, `core::stream`, specific parser |
| Core runtime | `src/core/` | config、runner、stream、filter、tracking、tee、telemetry | Reused by all command modules |
| Rewrite discovery | `src/discover/` | Command identification, rewrite rules, missed savings | Used by hooks and audit |
| Hook lifecycle | `src/hooks/` | init、verify、permission、rewrite、trust、integrity | Read the host configuration and call discover |
| Deployed hooks | `hooks/` | Hook/plugin/rules artifacts of each Agent | Call `rtk rewrite` |
| Parser | `src/parser/` | Structured test/tool ​​output parsing | Used by modules such as Vitest / Playwright |
| Analytics | `src/analytics/`、`src/learn/` | gain, session, discover report, etc. | Read tracking / session data |

## 4. Recommended reading order

1. `src/main.rs`: First understand the CLI surface and `Commands::*` routing.
2. `src/discover/rules.rs` and `src/discover/registry.rs`: Understand which commands will be rewritten.
3. `src/hooks/rewrite_cmd.rs` and `src/hooks/permissions.rs`: Confirm the rewrite exit code and permission boundaries.
4. `hooks/README.md` and the target Agent subdirectory: Confirm how the deployment hook calls binary.
5. `src/core/runner.rs` with a specific command module, such as `src/cmds/git/git.rs`.
6. `src/core/tracking.rs`, `src/core/tee.rs`, `docs/TELEMETRY.md`: Confirm statistics, recovery and privacy boundaries.
7. `tests/` and fixtures: Use test samples to disprove filtering behavior.

## 5. Key call chain

### Call chain 1: hook rewrite

- Trigger condition: Agent hook receives shell command.
- Starting point: `hooks/<agent>/...` calls `rtk rewrite <cmd>`.
- Key steps: `rewrite_cmd::run` -> `permissions::check_command` -> `lexer::contains_unattestable_construct` -> `registry::rewrite_command`.
- End point: stdout output rewritten command, exit code distinguishes allow / passthrough / deny / ask.
- Input: raw shell command string.
- Output: RTK command string or passthrough.
- Error handling: The document requires hooks to fail-open on the exception path and not block the original command.
- Based on: `hooks/README.md`, `src/hooks/rewrite_cmd.rs`, `src/hooks/permissions.rs`.

### Call chain 2: filtered command execution

- Trigger condition: Execute `rtk git diff`, `rtk pytest`, `rtk cargo test`, etc.
- Starting point: `main.rs::run_cli`.
- Key steps: match `Commands::*` -> call the corresponding `cmds` module -> native command execution -> filter output -> tracking.
- Endpoint: The terminal outputs the compression result and retains the exit code.
- Input: RTK command args.
- Output: filtered stdout/stderr.
- Error handling: skip filtering or output stderr when partial module fails, tee can save full output.
- Based on: `src/main.rs`, `src/core/runner.rs`, `src/cmds/git/git.rs`.

### Call chain 3: tracking / gain

- Trigger condition: Command filtering is completed.
- Starting point: `tracking::TimedExecution::start`.
- Key steps: Calculate raw / filtered token estimate -> write to SQLite -> `rtk gain` summary read.
- End point: local savings history.
- Input: original output, filtered output, command label.
- Output: tracking DB records and gain summary.
- Error handling: DB initialization and permission failure path needs to be confirmed.
- Basis: `src/core/tracking.rs`.

## 6. Read notes

- Important discovery: Codex path is prompt-level guidance and cannot be equated with Claude / Cursor transparent hook.
- Important findings: `permissions.rs` requires each segment of the compound command to match the allow rule to automatically allow.
- Important findings: `rewrite_cmd.rs` Select passthrough / ask for unattestable constructs such as command substitution, file redirect, etc. to reduce the risk of rewrite permissions.
- Important discovery: `tee.rs` Let filtered output retain the path back to raw output, suitable for failure troubleshooting.
- Uncertainty: The README version example is inconsistent with the `Cargo.toml` version and requires release/build verification.
- Uncertainty: The actual installation path, backup file, idempotence and uninstall behavior of each Agent hook are not yet run.
- To be run for verification: `rtk rewrite`, `rtk git status`, `rtk err`, `rtk test`, `rtk gain`, `rtk init --codex --dry-run` or equivalent safe path.

## To-do check items

- [x] Entry file found.
- [x] Found command to rewrite mainline.
- [x] Find the main line of command execution and filtering.
- [x] Find tracking and tee recovery.
- [ ] Find test coverage for each type of ecosystem filter.
- [ ] Source code level confirmation of telemetry compile-time switches and sending paths.
- [ ] Perform local builds and tests.

## Quality check items

- [x] Call chain has path or document basis.
- [x] Doesn't claim to have run native verification.
- [x] The difference between Codex prompt guidance and transparent hook has been marked.
- [x] Documented version sample inconsistency risk.

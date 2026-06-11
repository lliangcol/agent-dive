# RTK project deep dive

## 1. Basic project information

- Project name: RTK
- Project ID: `rtk-ai__rtk`
- GitHub：https://github.com/rtk-ai/rtk
- Project homepage: https://www.rtk-ai.app
- Category: `agentic-coding`
-Collect level: Level B standard collect
- Current status: `analyzing`
- Main language: Rust
- License：Apache-2.0
- Analysis date: 2026-06-11
- Analysis version/Commit:`6785a6c7695d7273e722214a295249a84819b6f0`
- Default branch: `develop`
- Whether to run verification: No
- Analysis basis: GitHub API, README, `git ls-remote --symref`, temporary shallow clone, `Cargo.toml`, `src/main.rs`, `src/hooks/README.md`, `hooks/README.md`, `src/discover/registry.rs`, `src/core/runner.rs`, `src/core/tracking.rs`, `src/core/tee.rs`, `docs/contributing/ARCHITECTURE.md`, `docs/TELEMETRY.md`.

## 2. Positioning in one sentence

RTK is a Rust CLI agent for AI coding assistants. Through command rewriting and output filtering, the lengthy output of common development commands is compressed and then handed over to LLM.

## 3. Problems solved by the project

AI coding agent often calls `git status`, `git diff`, `cargo test`, `pytest`, `pnpm`, `docker`, `kubectl` and other commands through the shell. Raw output often contains duplicate logs, full diffs, dependency trees, test pass noise, and build details that quickly consume the context window.

The core value of RTK is to turn these command outputs into digests more suitable for LLM consumption, while preserving exit codes, error highlights, and necessary recovery paths. It is not an Agent framework and is not responsible for model inference; it is a contextual cost governance layer within the AI ​​coding workflow.

Learning value:

- How to design a cross-ecological command filtering CLI.
- How to connect hook/plugin/prompt guidance to different AI coding tools.
- How to handle command security permissions, non-verifiable shell constructs, and rewrite fail-open.
- How to log token savings with SQLite and save the original output for recovery in case of failure.

## 4. Project main line

The typical process is based on README, hooks documents and source code sampling:

1. User installs RTK binary.
2. The user executes `rtk init` and writes hook, plugin or guidance for the target Agent.
3. The Agent subsequently initiates a shell command, such as `git status`.
4. For Agents that support transparent rewriting, hook calls `rtk rewrite "git status"`.
5. `src/discover/registry.rs` matches the rewrite rule and returns `rtk git status`.
6. Agent executes RTK commands.
7. `src/main.rs` is routed to the corresponding `src/cmds/**` module.
8. The command module executes native commands, captures output, filters summaries, and retains exit codes.
9. `src/core/tracking.rs` Record token savings estimates.
10. If the failed output is large, `src/core/tee.rs` can save the original output and give a recovery prompt.

Unverified: RTK is not installed on this machine in this round, and no Agent hook is actually triggered.

## 5. Quick Start

Entrance given by README:

- Homebrew：`brew install rtk`
- Linux / macOS quick install：`curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh`
- Cargo：`cargo install --git https://github.com/rtk-ai/rtk`
- Windows: Download the release zip and put `rtk.exe` into PATH. The hook will not be automatically rewritten under native Windows, and WSL support is more complete.

Verification commands given in README:

- `rtk --version`
- `rtk gain`

Note: The `Cargo.toml` version of this source code snapshot is `0.42.2`, but the verification example of the README still reads `rtk 0.28.2`. This may be because the README example is not synchronized and needs to be confirmed with actual release or local build later.

## 6. Core architecture

| module | effect | in accordance with | Verification status |
|---|---|---|---|
| `src/main.rs` | Clap CLI definition and command routing, connecting `Commands::*` to each ecological module | Source code sampling | Read entries and routes |
| `src/cmds/` | Implement filters according to ecology, such as git, rust, js, python, go, dotnet, cloud, system | tree, README, source code sampling | partial reading |
| `src/core/runner.rs` | Unifiedly execute native commands, capture output, call filters, and record tracking | Source code sampling | Read |
| `src/core/filter.rs` | Language-aware code filtering used by `rtk read` / `smart` | Source code sampling | Read |
| `src/discover/registry.rs` | Recognize original shell commands as RTK equivalents | Source code sampling | Read |
| `src/hooks/` | hook lifecycle：install、uninstall、verify、rewrite、trust、permission | hook README, source code sampling | partial reading |
| `hooks/` | Deployed to the hook/plugin/rules file on the Agent side | hooks README、tree | Read document |
| `src/core/tracking.rs` | SQLite records command, token savings, time consumption and summary | Source code sampling | Read |
| `src/core/tee.rs` | Save original output on failure and return full-output hint | Source code sampling | Read |
| `docs/TELEMETRY.md` | Description Anonymous aggregation telemetry, turned off by default, requires explicit opt-in | document | Read |

See `assets/diagrams/architecture.mmd`, `hook-rewrite-flow.mmd`, `command-filter-flow.mmd` and `tracking-telemetry-flow.mmd` for draft diagrams.

## 7. Core Principles

### Command output filtering

RTK uses different strategies for different commands: statistical extraction, error-only, group by rule, deduplication, structure extraction, code filtering and truncation. `docs/contributing/ARCHITECTURE.md` gives the strategy classification, `src/cmds/**` splits the implementation according to the ecology.

### Hook command rewriting

`hooks/README.md` Description The deployed hook is just a thin delegate: read the JSON sent by the Agent, extract the command string, call `rtk rewrite`, and then use the protocol corresponding to the Agent to return the modified command. The real rewrite judgment is in Rust `discover/registry`.

### Permissions and fail-open boundaries

`src/hooks/permissions.rs` Extract the permission rules of Claude / Cursor / Gemini and other hosts. The priority is Deny > Ask > Allow > Default. The exit code contract of `src/hooks/rewrite_cmd.rs` is used to tell the hook whether to allow, ask, deny or passthrough. The hooks documentation requires that exception paths do not block user commands.

### Original output restoration

Filtering may lose details needed for troubleshooting, so `src/core/tee.rs` supports saving raw output when the failure output is large enough, and outputs `[full output: ...]` prompts. This design is better suited for CI and test failure troubleshooting than simple truncation.

### Tracking and telemetry

`src/core/tracking.rs` Write local command execution statistics to SQLite. `docs/TELEMETRY.md` and README state that telemetry is turned off by default and requires explicit consent from `rtk init` or `rtk telemetry enable`; it can also be overridden by `RTK_TELEMETRY_DISABLED=1`.

## 8. Source code structure

- `src/main.rs`: CLI commands and main route.
- `src/cmds/`: Each ecological filter module.
- `src/core/`: execution, configuration, filtering, tracking, tee, telemetry, stream.
- `src/discover/`: rewrite rules, command lexer, missed savings report.
- `src/hooks/`: hook installation, rewriting, permissions, integrity, trust, audit.
- `hooks/`: Deployment files such as Claude, Codex, Cursor, Copilot, Gemini, OpenCode, Pi, Hermes, etc.
- `docs/guide/`: User Guide.
- `docs/contributing/`: Architecture, technical and contribution documentation.
- `tests/fixtures/`: A large number of command output samples.
- `scripts/benchmark/`: benchmark related scripts.

## 9. Key call chain

### Call chain 1: Agent hook automatically rewrites commands

- Trigger condition: The target Agent executes the shell command.
- Starting point: Agent-specific hooks, such as Claude / Cursor shell hook or OpenCode / Hermes plugin.
- Key steps: read command -> call `rtk rewrite` -> `rewrite_cmd::run` -> `discover::registry::rewrite_command` -> return RTK command or passthrough.
- End point: Agent executes `rtk <command>` or the original command.
- Based on: `hooks/README.md`, `src/hooks/rewrite_cmd.rs`, `src/discover/registry.rs`.
- Status: Source code sampling has been read, and the real Agent behavior has not been verified.

### Call chain 2: RTK execution and filtering commands

- Trigger condition: User or Agent executes `rtk git status`, `rtk cargo test`, etc.
- Starting point: `main.rs::run_cli`.
- Key steps: Clap parse -> `Commands::*` match -> Call `src/cmds/**::run` -> `core::runner` or execute native commands within the module -> Filter stdout/stderr -> Print summary.
- Endpoint: LLM only sees the compressed output.
- Based on: `src/main.rs`, `src/core/runner.rs`, `src/cmds/git/git.rs`.
- Status: Source code sampling has been read, but not_run locally.

### Call chain 3: Failure output recovery and savings statistics

- Trigger condition: The command execution is completed, especially when it fails and the output is long.
- Starting point: `core::runner` or specific command module.
- Key steps: call `TimedExecution::track` after filter -> write to tracking DB; failure output is written to tee file via `tee_and_hint`.
- Endpoint: The user sees the simplified failure summary and the readable full-output hint, and can subsequently query the statistics with `rtk gain`.
- Based on: `src/core/runner.rs`, `src/core/tracking.rs`, `src/core/tee.rs`.
- Status: Source code sampling has been read, verification has not been performed.

## 10. integration method

It is recommended to do isolation verification first:

1. Install binary in a temporary environment or build from source code.
2. Run `rtk --version`, `rtk config --create`, `rtk rewrite "git status"`.
3. Compare the output of `git status` and `rtk git status` for a small warehouse.
4. Use `RTK_TEE_DIR` to point to the temporary directory and verify the failed command raw-output recovery.
5. Execute dry-run or manual installation instructions separately for the target Agent, instead of running global automatic patch directly in the main environment.
6. The Codex path should be carefully confirmed: the README and hooks documents show that the Codex is `AGENTS.md` / `RTK.md` prompt-level guidance, not automatic rewriting of program-level hooks.

## 11. Problemshooting

- Installation source obfuscation: README warns that a Rust Type Kit with the same name exists on crates.io and that Cargo installations should use the GitHub URL.
- Windows hook limitations: native Windows can run filtering commands, but the automatic rewriting hook is incomplete; WSL support is more complete.
- The README version example may be outdated: the source code `Cargo.toml` is `0.42.2`, and the README example is written `0.28.2`.
- Agent support methods are different: transparent hook, plugin mutation, deny-with-suggestion, and prompt guidance are not equivalent.
- Risk of permission misjudgment: Deny/Ask/Allow and compound command behaviors must be verified, and rewrite cannot be allowed to escalate permissions.
- Telemetry boundaries: default off and opt-in declarations need to be confirmed via source/build configuration.

## 12. Objective evaluation

### advantage

- The target problem is specific: reduce context waste when the AI ​​coding agent reads shell output.
- Rust single binary + multi-ecological filter module, clear deployment model.
- Hook documentation clearly differentiates between deployed artifacts, lifecycle manager, rewrite registry and command filters.
- Engineering boundary design such as permission model, hook integrity, tee recovery and telemetry consent.

### shortcoming

- It is not Agent runtime or planner. It cannot be used to replace the Agent Loop / Tool Calling framework when learning.
- README savings figures and version examples require reproduction and should not be quoted directly as verified effects.
- Multi-Agent hook mechanisms vary greatly, and prompt-level guidance such as Codex cannot guarantee automatic rewriting.
- Global installation will write user-level configuration and must be dry-run/backup/single-path verified first.

### Applicable scenarios

- Command output compression for AI coding assistant.
- Long session review, CI debug, test failure troubleshooting and diff reading.
- Learn CLI proxy, hook rewrite, context cost statistics and raw-output recovery.
- Compare context management solutions with Caveman, Graphify, and CodeGraph.

### not applicable scenario

- When you need the full raw log, full diff or audit evidence, don't just look at the filtered output.
- Not suitable for direct global installation when the write range is not audited.
- It is not suitable to use telemetry / token savings statistics as a model quality evaluation.
- Not suitable for relying on prompt-level guidance to enforce security policies.

## 13. Learning Todo List

See [learning-todo-list.md](learning-todo-list.en.md). It is recommended to complete `rtk rewrite` and single command filtering verification first, and then proceed to hook installation and Agent integration verification.

## 14. Summary

RTK is worth collecting as a `agentic-coding` direction Level B project. It represents an important but easily overlooked type of AI coding infrastructure: it does not change the model or agent decision-making, but reduces the cost of tool output entering the context. The next step should be to verify the binary, rewrite, filtered output, tee recovery and single-agent installation paths in the isolation environment, and then decide whether to upgrade to Level A.

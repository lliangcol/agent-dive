# ECC project deep dive

## 1. Basic project information

- Project name: ECC
- Project ID: `affaan-m__ECC`
- GitHub:https://github.com/affaan-m/ECC
- Official documentation: https://ecc.tools
- Category: `agentic-coding`
- Collection level: Level A deep collect
- Current status: `analyzing`
- Main language: JavaScript
- License:MIT
- Analysis date: 2026-06-11
- Analysis version/Commit:`c888d2b73f26d605ff6c172b433d4cad2200206f`
- Whether to run verification: No
- Analysis basis: GitHub API, README, `package.json`, `docs/architecture/cross-harness.md`, `docs/releases/2.0.0/release-notes.md`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, `hooks/hooks.json`, `scripts/ecc.js`, `scripts/install-plan.js`, `scripts/install-apply.js`, `scripts/lib/install-*` first round of inspection

## 2. Positioning in one sentence

ECC is an engineering workflow layer across AI coding harnesses that packages reusable skills, rules, hooks, commands, MCP configurations, installers, and operator tools into an agentic coding operating system that can be migrated in environments such as Claude Code, Codex, OpenCode, Cursor, and Gemini.

## 3. Problems solved by the project

The pain points of AI coding tools are not only model capabilities, but also include difficulty in reusing workflow assets, inconsistent hook capabilities, scattered MCP configurations, different formats of skills and rules between different tools, lack of unified management of context/memory/security access, and difficulty in observing the operation of multiple people or multiple worktree agents. The core idea of ​​ECC is to place the durable workflow in the shared source code directory, and then adapt it to different operating environments through each harness adapter.

Learning value mainly falls into five categories:

- Cross-harness asset design: how the same set of skills, rules, commands, and MCP conventions are mapped to tools such as Claude Code, Codex, OpenCode, and Cursor.
- Agent safety gates: Constrain agent behavior through hooks, quality gate, secret/config protection, MCP health check, session persistence, etc.
- Selective install: Use manifest, profile, component, target and install-state to manage large-scale workflow packages.
- Operator workflows: Use sessions, status, work-items, control-pane, and worktree lifecycle to support long-term agent work.
- Codex / Claude / OpenCode comparison: which capabilities are native hooks and which can only be instruction-backed.

## 4. Project main line

The main line of ECC is not a single Agent Loop, but a harness workflow package:

1. The maintainer maintains reusability in `skills/`, `agents/`, `commands/`, `rules/`, `hooks/`, `mcp-configs/`, `manifests/`.
2. The user selects the target harness through Claude plugin, Codex plugin, OpenCode package, npm CLI or manual installation path.
3. `ecc` CLI distributes to `install-apply.js`, `install-plan.js`, `catalog.js`, `consult.js`, `doctor.js`, `status.js`, `control-pane.js` and other scripts according to the command.
4. The installer parses profile / modules / components / target, generates a file operation plan, and writes the corresponding harness configuration, skills, rules, commands or MCP configuration.
5. Harnesses that support hooks trigger security, quality, memory, and observation scripts in stages such as tool invocation, session start, response stop, and session end; harnesses that do not support hooks use `AGENTS.md`, plugin manifest, and configuration conventions to carry instructions.
6. The Operator tool reads session, state, work items, MCP inventory, worktree lifecycle and other information to help long-term agent work be observable, recoverable and repeatable.

Based on: README, cross-harness architecture documentation, `package.json` bin/scripts, `scripts/ecc.js`, `hooks/hooks.json`.

## 5. Quick Start

### Environmental requirements

- Node.js: `package.json` annotation `>=18`.
- Optional: Claude Code, Codex, OpenCode, Cursor, Gemini, Zed and other target harnesses.
- Optional: Python, for use with `ecc_dashboard.py` or other auxiliary tools.

### Installation path

The README gives multiple paths and cannot be installed overlappingly:

```bash
# Claude Code plugin path, based on README
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

```bash
# npm package / selective installer path, based on package.json and README
npx --yes --package ecc-universal ecc consult "security reviews" --target claude
npx --yes --package ecc-universal ecc install --profile minimal --target claude
```

Note: The README example uses `npx ecc ...`, but when reviewing the npm metadata this time, it was found that there is a separate `ecc@0.0.2` package on npm. Subsequent verification should use `npx --package ecc-universal ecc ...`, or `node scripts/ecc.js ...` after cloning.

```powershell
# Windows manual installer path, based on README
.\install.ps1 --profile minimal --target claude
```

### Minimal verification recommendations

No installation was performed this time. Subsequent real verification should first run the read-only or dry-run path:

```bash
npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json
npx --yes --package ecc-universal ecc consult "code review and security" --target codex
npx --yes --package ecc-universal ecc doctor
```

### Known limitations

- Codex currently has no Claude-style hook parity. Both the ECC README and cross-harness documentation describe Codex paths as instruction-backed.
- Full profile may write a large number of files to the user directory or project directory. You should dry-run and prepare to roll back before verifying.
- The number of public skills in README, release notes, and plugin manifest may drift, so you need to use the repository script to review the catalog.

## 6. Core architecture

ECC can be broken down into eight layers:

- Shared asset layer: `skills/`, `agents/`, `commands/`, `rules/`, `hooks/`, `mcp-configs/`.
- Harness adaptation layer: `.claude-plugin/`, `.codex-plugin/`, `.codex/`, `.opencode/`, `.cursor/`, `.gemini/`, `.zed/`, `.qwen/`, etc.
- CLI distribution layer: `scripts/ecc.js` routes `ecc install`, `ecc plan`, `ecc consult`, `ecc doctor`, `ecc status`, `ecc control-pane`, etc. commands to specific scripts.
- Selective install layers: `scripts/install-plan.js`, `scripts/install-apply.js`, `scripts/lib/install-manifests.js`, `scripts/lib/install-executor.js`, `scripts/lib/install/`.
- Hook runtime layer: `hooks/hooks.json`, `scripts/hooks/`, hook bootstrap and run-with-flags mechanisms.
- Operator state layer: `scripts/status.js`, `scripts/sessions-cli.js`, `scripts/work-items.js`, `scripts/worktree-lifecycle.js`, `scripts/mcp-inventory.js`.
- Control pane layers: `scripts/control-pane.js` and `scripts/lib/control-pane/`.
- Alpha control plane: `ecc2/`, the README and release notes describe this as 2.0 alpha and should not be considered a stable public runtime.

diagrams see:

- `assets/diagrams/architecture.mmd`
- `assets/diagrams/cross-harness-flow.mmd`
- `assets/diagrams/install-flow.mmd`
- `assets/diagrams/hook-lifecycle.mmd`
- `assets/diagrams/control-pane-flow.mmd`

## 7. Core Principles

### 7.1 Durable workflow and thin adaptation

`docs/architecture/cross-harness.md` clearly regards `skills/` as the most migratory unit, puts rules, hooks, MCP, commands, sessions and other capabilities in the shared layer, and then allows each harness to only adapt to the loading method, event shape and command mapping.

### 7.2 Selective install

`package.json` exposes `ecc` and `ecc-install` bins. `scripts/install-plan.js` is responsible for parsing profile, modules, components, skills, target and config; `scripts/install-apply.js` creates the install plan and applies it after parsing the request. The first round of source code inspection shows that the installer has concepts such as manifest, target adapter, install-state, dry-run/json output, etc., but the complete writing strategy has not been verified one by one.

### 7.3 Hook lifecycle

`hooks/hooks.json` Overrides PreToolUse, PreCompact, SessionStart, PostToolUse, Stop, SessionEnd. Typical uses include Bash preflight, configuration protection, MCP health check, quality gate, frontend design warning, format/typecheck batching, session persistence, cost tracking, etc. Harnesses that support hooks or events, such as Claude/OpenCode/Cursor, can be executed; Codex is currently mainly expressed through instructions and configuration constraints.

### 7.4 Skills / agents / commands

The README and plugin manifest show that ECC uses agents, skills, and commands as core surfaces. `AGENTS.md` provides global workflow requirements such as agent-first, TDD, security-first, plan-before-execute, etc.; `commands/` mainly carries legacy slash entries; `skills/` is a longer-term migration source.

### 7.5 Operator observability

2.0 release notes mention session adapters, MCP inventory, worktree lifecycle, `orch-*` orchestrator family. `package.json` also has script entries such as `status`, `sessions`, `work-items`, `control-pane`, `platform-audit`, `observability:ready`. Currently, only file-level confirmation is done, and the SQLite state store or control pane is not started.

## 8. Source code structure

- CLI entrance: `scripts/ecc.js`
- Installation preview: `scripts/install-plan.js`
- Installation execution: `scripts/install-apply.js`
- Manifest and profile parsing: `scripts/lib/install-manifests.js`
- install executor:`scripts/lib/install-executor.js`
- install runtime:`scripts/lib/install/`
- Hook configuration: `hooks/hooks.json`
- hook script: `scripts/hooks/`
- Control pane:`scripts/control-pane.js`, `scripts/lib/control-pane/`
- Status/session/work item: `scripts/status.js`, `scripts/sessions-cli.js`, `scripts/work-items.js`
- MCP inventory:`scripts/mcp-inventory.js`
- Worktree lifecycle:`scripts/worktree-lifecycle.js`
- Codex surface: `.codex-plugin/`, `.codex/`
- Claude Surface: `.claude-plugin/`, `.claude/`
- OpenCode surface: `.opencode/`
- Cursor Surface: `.cursor/`
- Skills, agents, commands, rules: `skills/`, `agents/`, `commands/`, `rules/`
- Rust alpha control plane:`ecc2/`
- Test directory: `tests/`
- Document directory: `docs/`

## 9. Key call chain

### Call chain 1: CLI command distribution

- Trigger condition: `ecc <command>` already exists in the user execution environment, explicit npm package form `npx --package ecc-universal ecc <command>`, or executed after clone `node scripts/ecc.js <command>`
- Starting point: `scripts/ecc.js`
- Key steps: parse command -> look up table and select script -> execute `install-apply.js`, `install-plan.js`, `consult.js`, `doctor.js`, `status.js`, etc. through Node sub-process
- Output: installation results, plan, catalog, diagnosis, status, etc.
- Error handling: In the first round, only the command list and help text were confirmed, and the error path was not executed.
- Basis: `scripts/ecc.js`, `package.json`

### Call chain 2: Selective install plan to apply

- Trigger condition: User executes `ecc plan` or `ecc install`
- Starting point: `scripts/install-plan.js` / `scripts/install-apply.js`
- Key steps: parse parameters -> normalize install request -> read config -> create install plan -> parse modules/components/target -> dry-run or apply
- Output: file operation plan, install-state, target harness configuration
- Error handling: There are concepts such as unknown argument, unknown module, unsupported target, and warnings in the source code; the complete strategy needs to be run for verification
- Basis: `scripts/install-plan.js`, `scripts/install-apply.js`, `scripts/lib/install/runtime.js`, `scripts/lib/install-manifests.js`, `scripts/lib/install-executor.js`

### Call chain 3: Hook life cycle

- Trigger conditions: harness triggers PreToolUse, SessionStart, PostToolUse, Stop and other events
- Starting point: `hooks/hooks.json`
- Key steps: Match tool/event -> Call plugin bootstrap / run-with-flags -> Execute specific `scripts/hooks/*.js` -> Return blocking, warning, asynchronous recording or session output
- Output: Quality gate control, configuration protection, MCP health check, format/type check, session state saving, etc.
- Error handling: Configure timeout, async and dispatcher for partial scripts in hook JSON; the real behavior depends on harness
- Basis: `hooks/hooks.json`

### Call chain 4: Control pane

- Trigger condition: User executes `ecc control-pane` or `ecc-control-pane`
- Starting point: `scripts/control-pane.js`
- Key steps: parse host/port/db/action parameters -> `createControlPaneServer()` -> read state snapshot -> expose local HTTP UI/API -> optionally execute allowlist action
- Output: local control pane URL, state db path, read-only or action-enabled status
- Error handling: In the first round, only the entry and server file summary were checked, and the service was not started.
- Basis: `scripts/control-pane.js`, `scripts/lib/control-pane/server.js`

## 10. integration method

### Codex integration

The Codex direction gives priority to studying the relationship between `.codex-plugin/plugin.json`, `.codex/AGENTS.md`, `.codex/config.toml`, `.mcp.json`, `skills/` and `.agents/skills/`. It has been verified that `skills` of `.codex-plugin/plugin.json` points to `./skills/`; the Codex support description of the README also mentions `.agents/skills/`, and the actual loading boundaries of the two need to be verified in the Codex later. Since Codex does not have Claude-style hooks, the focus of research should be on instruction-backed constraints, plugin skill exposure, MCP configuration and agent role files.

### Claude Code integration

Claude Code is a first-class support surface for ECC. The focus of learning is the plugin marketplace installation, the loading relationship of `hooks/hooks.json`, `skills/`, `commands/`, `rules/`, `CLAUDE.md` / `AGENTS.md`, and the impact of hooks on Bash/Edit/Stop/SessionStart.

### OpenCode / Cursor integration

OpenCode has a plugin/event system, and Cursor has its own rule/hook layout. The two are suitable for comparing the boundaries of "shared workflow source" and "harness adapter".

### Java / Spring Boot relationship

ECC is not a Java/Spring Boot framework. It is more suitable to be used as an agent workflow package in Java projects: install Java/Spring Boot related skills, rules, reviewer/build-resolver agent, and then let Claude Code, Codex or OpenCode follow these workflows in the project.

## 11. Problemshooting

See [troubleshooting.md](troubleshooting.en.md) for details. The focus of the first round includes duplicate installations, full profile causing duplicate skills/hooks, Codex hook parity misunderstanding, Node version, Windows PowerShell installer, global configuration write range, hook blocking and catalog number drift.

## 12. Objective evaluation

### advantage

- The cross-harness design fits the agentic coding learning theme very well.
- Instead of just giving prompt words, it includes engineered surfaces such as installer, manifest, hooks, MCP, state, sessions, worktree, tests, release gate, etc.
- The differences between Codex / Claude / OpenCode / Cursor have clear boundary descriptions, suitable for horizontal comparison.
- Rich governance topics such as security, quality, TDD, review, verification, cost/context, and memory.
- MIT License, public repository, source code and documents can be analyzed.

### shortcoming

- The scope is very large, and it is easy to just stop at the README and must be broken down into topics.
- Installation will modify user-level or project-level agent configurations, requiring high verification costs and rollback requirements.
- Hook behavior is highly dependent on the specific harness, and the results of one environment cannot be used to infer all environments.
- There may be drift in the quantity expressions in README, release notes, and plugin manifest, and the catalog script needs to be reviewed.
- Abilities are deeply bound to personal workflows, and you need to distinguish between universal design and author-preferred workflows when learning.

### Applicable scenarios

- Learn the engineering workflow of AI coding harness.
- Study cross-tool migration of skills/rules/hooks/MCP.
- Design team-level agent governance, quality gate, security inspection and session review system.
- Compare the loading and execution capabilities of Claude Code, Codex, OpenCode, and Cursor.

### not applicable scenario

- Want to learn only a single Agent Loop or Model Call SDK.
- Restricted environments where writing to the native agent global configuration is not acceptable.
- Production business dependencies that require stable SDK API.
- Want to copy complete hooks/rules/skills to a private repository without censorship.

## 13. Learning Todo List

See [learning-todo-list.md](learning-todo-list.en.md) for details.

## 14. Summary

ECC deserves to be used as a Level A deep collection project. Its most valuable thing is not a single point tool, but showing how the AI ​​coding workflow can evolve from a "cue word collection" to an installable, diagnostic, gated, and observable operating system across the harness. In the next round of learning, dry-run install plan should be executed first, and then the Codex instruction-backed path and Claude/OpenCode hook-backed path should be verified separately.

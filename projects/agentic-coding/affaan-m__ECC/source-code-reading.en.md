# ECC source reading record

## 1. Reading objectives

- Issues to be understood in this round: How ECC distributes the same set of agent assets to different AI coding workflow harnesses, and manages long-term work through hooks, installers, MCP and operator tools.
- Related functions: CLI, selective install, hook lifecycle, Codex plugin, Claude plugin, OpenCode adapter, control pane, session/worktree status.
- Expected output: first round module map, recommended reading order, call chain to be verified and subsequent source code digging issues.

## 2. Source code entry

| Entrance | path | effect | in accordance with |
|---|---|---|---|
| CLI dispatcher | `scripts/ecc.js` | Route commands like `ecc install/plan/consult/doctor/status/control-pane` to scripts | `package.json` bin and source code |
| Install preview | `scripts/install-plan.js` | Parse profile, modules, components, target, and output plan | Source code |
| Install apply | `scripts/install-apply.js` | Create and apply install plan, support dry-run/json | Source code |
| Install manifests | `scripts/lib/install-manifests.js` | Read module/profile/component/target information | Source code |
| Hook manifest | `hooks/hooks.json` | Define life cycles such as PreToolUse, PostToolUse, Stop, SessionStart, etc. | Source code |
| Control pane | `scripts/control-pane.js` | Start local operator control pane | Source code |
| Codex plugin | `.codex-plugin/plugin.json` | Codex plugin metadata, skills, MCP servers, default prompt | Source code |
| Claude plugin | `.claude-plugin/plugin.json` | Claude plugin metadata, hooks, skills, commands/rules surface | Source code |
| OpenCode adapter | `.opencode/` | OpenCode commands, plugins, tools, instructions | GitHub tree |
| Alpha control plane | `ecc2/` | Rust alpha control plane | README / release notes / GitHub tree |

## 3. Module map

| module | path | Responsibilities | Dependencies |
|---|---|---|---|
| Shared skills | `skills/`, `.agents/skills/` | Migrating workflow units | `.codex-plugin/plugin.json` points to `skills/`; the Codex support of README also mentions `.agents/skills/`, and the actual loading boundary needs to be verified. |
| Agents | `agents/`, `.codex/agents/`, `.opencode/prompts/agents/` | Dedicated reviewer, planner, resolver and other roles | Constrained by the agent/role mechanisms of different harnesses |
| Commands | `commands/`, `.opencode/commands/` | Slash command or compatible entry | README clearly `commands/` bias towards legacy shim |
| Rules | `rules/` | Language/Framework/Common Rules | The installer writes by profile/target |
| Hooks | `hooks/hooks.json`, `scripts/hooks/` | Security, quality, memory, context and session lifecycle | Claude/OpenCode/Cursor has execution path; Codex instruction-backed |
| Selective installer | `scripts/install-*.js`, `scripts/lib/install-*`, `manifests/` | Plan, preview, execute, record install-state | Depends on target adapter and manifest |
| MCP config | `.mcp.json`, `mcp-configs/`, `scripts/mcp-inventory.js` | Multi-harness MCP configuration and inventory | Rely on native MCP support of each harness |
| Operator tools | `scripts/status.js`, `sessions-cli.js`, `work-items.js`, `worktree-lifecycle.js` | Session, work item, status, worktree management | Rely on local state store and Git/GitHub state |
| Control pane | `scripts/control-pane.js`, `scripts/lib/control-pane/` | Local dashboard/API | Read state snapshot, optional allowlist actions |
| Tests and gates | `tests/`, `scripts/ci/` | Verify catalog, commands, agents, skills, hooks, install manifests, security IOC | `package.json` test scripts |

## 4. Recommended reading order

1. README, `docs/architecture/cross-harness.md`, `docs/releases/2.0.0/release-notes.md`, first understand the project boundaries.
2. `package.json`, `scripts/ecc.js`, confirm CLI distribution and executable commands.
3. `manifests/`, `scripts/install-plan.js`, `scripts/install-apply.js`, `scripts/lib/install-manifests.js`, `scripts/lib/install-executor.js`.
4. `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, `.opencode/README.md`, `.cursor/`, compare adapter.
5. `hooks/hooks.json` and `scripts/hooks/`, press PreToolUse -> PostToolUse -> Stop -> SessionStart to trace.
6. `scripts/status.js`, `scripts/sessions-cli.js`, `scripts/work-items.js`, `scripts/worktree-lifecycle.js`, `scripts/control-pane.js`.
7. `tests/` and `scripts/ci/`, check how the project prevents catalog, manifest, hook and packaging drift.

## 5. Key call chain

### Call chain 1: `ecc install` Selective installation

- Trigger condition: User executes `ecc install --profile <name> --target <target>`, or uses explicit npm package to run `npx --package ecc-universal ecc install ...`.
- Starting point: `scripts/ecc.js`.
- Key steps: command table selection `install-apply.js` -> `parseInstallArgs()` -> read optional config -> `normalizeInstallRequest()` -> `createInstallPlanFromRequest()` -> target adapter generation operation -> `applyInstallPlan()`.
- Endpoint: The configuration, skills, rules, commands, MCP and other files of the target harness are written, and the install-state is recorded.
- Enter: profile/modules/components/skills/target/dry-run/json/config.
- Output: human plan, JSON plan/result, install-state.
- Error handling: The source code shows unknown arguments, unsupported target, unknown module, and warnings; the actual error text needs to be run for verification.
- Based on: `scripts/ecc.js`, `scripts/install-apply.js`, `scripts/lib/install/runtime.js`, `scripts/lib/install-manifests.js`, `scripts/lib/install-executor.js`.

### Call chain 2: `ecc plan` Read-only preview

- Trigger condition: User executes `ecc plan --profile <name> --target <target> --json`.
- Starting point: `scripts/install-plan.js`.
- Key steps: parse parameters -> list profiles/modules/components or resolve install plan -> output text/JSON.
- Endpoint: Do not modify the target file, only return the plan.
- Input: profile/modules/components/family/target/config/json.
- Output: Reviewable installation plan.
- Error handling: unknown argument or manifest validation errors will be thrown.
- Basis: `scripts/install-plan.js`.

### Call chain 3: Claude-style hook gate

- Trigger conditions: Claude Code triggers tool invocation, session start, response stop, or session end event.
- Starting point: `hooks/hooks.json`.
- Key steps: matcher hits Bash/Edit/Write/MultiEdit, etc. -> run plugin bootstrap -> `run-with-flags.js` select minimal/standard/strict profile -> execute specific hook script.
- Endpoint: return warning, blocking, asynchronous observation, quality gate control or session state saving.
- Input: hook event payload and current environment variables.
- Output: hook stdout/stderr/exit code.
- Error handling: timeout, async, and profile flags are configured by the hook manifest; the actual blocking behavior needs to be verified on the machine.
- Basis: `hooks/hooks.json`.

### Call chain 4: Codex instruction-backed path

- Trigger conditions: Codex loading project/plugin instructions, skills, MCP config.
- Starting point: `.codex-plugin/plugin.json`, `.codex/AGENTS.md`, `.codex/config.toml`.
- Key step: Codex reads plugin metadata and skills/MCP points -> constrains workflow using `AGENTS.md`/skills -> MCP servers exposed by configuration.
- End point: Agent behavior is affected by instructions and tool configuration.
- Input: Codex app/CLI plugin, skills, MCP support status.
- Output: available skills, MCP tools, default prompt behavior.
- Error handling: Codex has no hook parity; it cannot be assumed that `hooks/hooks.json` will be executed.
- Based on: README, cross-harness architecture, `.codex-plugin/plugin.json`.

### Call chain 5: Control pane local service

- Trigger condition: The user executes `ecc control-pane` or `ecc-control-pane`.
- Starting point: `scripts/control-pane.js`.
- Key steps: parseArgs -> `createControlPaneServer()` -> listen -> read state snapshot -> optional allowlist action.
- Endpoint: local HTTP URL output to the terminal.
- Input: host, port, db path, state db path, allow-actions.
- Output: local dashboard/API.
- Error handling: The server entry includes shutdown processing; action execution and permissions need to be deeply read in the source code.
- Basis: `scripts/control-pane.js`, `scripts/lib/control-pane/server.js`.

## 6. Read notes

- Important discovery: The core of ECC is not a single runtime, but a combination of "shared workflow assets + harness adapter + install/runtime governance".
- Important findings: Codex support is explicitly described as instruction-backed and cannot be applied to the Claude hook model.
- Important discovery: The installer is no longer a simple copy script, but a manifest/profile/component/target driver.
- Important findings: `package.json` test command covers agents, commands, rules, skills, hooks, install manifests, personal path, catalog, command registry and tests/run-all.
- Uncertainty: The actual default combination of profile and module in the manifest has not yet been fully enumerated.
- Uncertainty: The number of shortDescriptions of `.codex-plugin/plugin.json` and the number of README/release notes may be inconsistent, and a catalog check needs to be run.
- Uncertainty: There is a parsing ambiguity between `npx ecc` in the README example and the npm package name `ecc-universal`; it has been confirmed that there is an independent `ecc@0.0.2` package on npm, and the verification command should use an explicit package selector.
- Uncertainty: The true behavior of hook bootstrap in Windows, Node 21+, and Claude plugin cache paths needs to be verified.
- To be run for verification: `npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json`.
- Validations to run: `npm test` or at least catalog/manifest/hook validators.
- Verification to be run: Claude plugin installation and uninstallation, Codex plugin loading, OpenCode plugin event.

## 7. To-do check items

- [x] Find CLI entry.
- [ ] Full trace install target adapter.
- [ ] Full tracing of hook bootstrap and run-with-flags.
- [ ] Find all MCP config read and write paths.
- [ ] Find the state DB schema and session adapter data model.
- [ ] Find the conflict prediction and cleanup logic of the worktree lifecycle.
- [ ] Run at least one dry-run plan and log the output.

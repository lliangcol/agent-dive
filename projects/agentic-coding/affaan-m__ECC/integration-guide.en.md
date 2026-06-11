# ECC integration guide

## 1. integration goal

- Target system: Local AI coding working environment, including Codex, Claude Code, OpenCode, Cursor.
- Target capabilities: Introduce ECC skills, rules, MCP conventions, review/security/TDD workflow, optional hooks and operator tools.
- Integration method: give priority to dry-run / plan, confirm the writing range and integrate separately according to the target harness.
- Constraints: Do not overlap multiple installation paths, do not directly full profile in sensitive repositories, do not write keys, and do not treat harnesses that do not support hooks as hook-backed.

## 2. Preconditions

- Running environment: Node.js `>=18`.
- Dependencies: target harness; optional npm/npx; optional Git.
- Model or service configuration: ECC itself should not contain keys; MCP server or external services require user configuration.
- Permission requirements: The installer may write to the user directory or the project directory. The target, profile, install root and rollback plans must be confirmed before execution.

## 3. Minimum integration path

### 3.1 Codex read-only evaluation path

```bash
npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json
npx --yes --package ecc-universal ecc consult "code review security tdd" --target codex
```

Verification key points:

- Whether the output selected modules are as expected.
- Whether the target path only affects Codex related configurations.
- Whether to write `.codex/config.toml`, `.codex/AGENTS.md`, skills or MCP references.
- Whether native hooks are not claimed to be enabled.

Status: Not executed. This section is a solution to be verified based on README, `package.json`, npm metadata and installation script help text. Do not use `npx ecc ...` directly as the verification command because there is a separate `ecc@0.0.2` package on npm.

### 3.2 Claude Code plugin path

```bash
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

Verification key points:

- Whether Claude plugin is loaded `.claude-plugin/plugin.json`.
- `hooks/hooks.json` is recognized by Claude Code.
- Output, blocking and timeout behavior for PreToolUse, PostToolUse, Stop, SessionStart.
- Whether to avoid running the full manual installer again after plugin install.

Status: Not executed.

### 3.3 npm selective install path

```bash
npx --yes --package ecc-universal ecc consult "security reviews" --target claude
npx --yes --package ecc-universal ecc plan --profile minimal --target claude --json
npx --yes --package ecc-universal ecc install --profile minimal --target claude --dry-run
```

Verification key points:

- `--dry-run` Whether the output lists planned file operations in full.
- `install-state` Is the path clear?
- `minimal` / `core` / `full` etc. Profile differences are in line with safety expectations.
- `--without baseline:hooks` Is it possible to exclude hook runtime.

Status: Not executed.

### 3.4 OpenCode / Cursor path

For OpenCode, focus on the plugin, commands, tools, and instructions under `.opencode/`; for Cursor, focus on the `.cursor/` rule and hook adapter. It is recommended to install it in a one-time test project first and not directly affect the main repository.

Status: Not executed.

## 4. Interface and data flow

| enter | processing module | output | Remark |
|---|---|---|---|
| `ecc install --profile minimal --target codex` | `scripts/ecc.js` -> `install-apply.js` -> install runtime | Codex configuration, skills, MCP reference, install-state | pending verification |
| `ecc plan --json` | `install-plan.js` -> manifest resolver | JSON plan | Recommended as first verification command |
| Claude tool event | `hooks/hooks.json` -> hook runner -> `scripts/hooks/*.js` | Blocking, warning, asynchronous observation, session status | hook-backed harness only |
| Codex plugin metadata | `.codex-plugin/plugin.json` | skills, MCP servers, default prompt | instruction-backed |
| Operator status query | `scripts/status.js` / `control-pane.js` | state snapshot / local dashboard | Verification to be started |

## 5. Java/Spring Boot integration concerns

- Bean life cycle: ECC does not directly enter the Spring Bean life cycle and is suitable as an external agent workflow.
- Configuration management: Do not write ECC global configuration into the business repository before review; prioritize project level, minimum profile and dry-run.
- Permissions and auditing: Hooks, MCP and shell command rules may affect agent behavior, and enterprise environments require auditing.
- Log and link tracing: You can study `status`, sessions, work-items, and control pane instead of directly accessing application logs.
- Timeout, retry and current limiting: There is a timeout in the hook manifest; the current limiting of MCP and external API needs to be configured separately.
- Database or message queue: ECC's state store is the operator layer and should not be mixed into the business database.

## 6. Integration risks

- Dependency version: Node version, harness version, plugin marketplace support status will affect the results.
- Model cost: skills and hooks may increase context and tool calls, and cost/context needs to be monitored.
- Tool permissions: hooks and MCP may read or operate local files, and must confirm the allowlist and sandbox.
- Data security: It is prohibited to include private memory, token, OAuth, and personal workspace state into shared repositories.
- Operation stability: The superposition of multiple installation methods may cause duplicate hooks, duplicate skills or conflicting configurations.
- Rollback risk: install-state, change files and uninstall commands must be logged.

## 7. Recommended verification commands

Follow-up recommendations are implemented from low risk to high risk:

```bash
npx --yes --package ecc-universal ecc --help
npx --yes --package ecc-universal ecc plan --list-profiles
npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json
npx --yes --package ecc-universal ecc consult "tdd code review security" --target codex
npx --yes --package ecc-universal ecc install --profile minimal --target codex --dry-run --json
```

Only after the dry-run output is acceptable can the real install be considered.

# ECC problem troubleshooting record

## Problem: Repeated installation results in duplicate skills, rules or hooks

- Discovery time: 2026-06-11
- Current status: unverified, risk record
- Scope of influence: Claude Code plugin, manual installer, npm installer mixed use scenario

### Phenomenon

The README clearly reminds not to overlap plugin install and full manual installer. Repeated installations may result in the same skills, commands, rules, or hooks existing in both the user directory and the plugin directory.

### environment

- Operating system: To be verified
- Runtime version: Node `>=18`
- Project version/Commit:`c888d2b73f26d605ff6c172b433d4cad2200206f`
- Key dependencies: Claude Code plugin, manual installer, npm `ecc-universal`

### Reproduction steps

1. Install the Claude plugin.
2. Run the full profile manual installer again.
3. Check whether skills/hooks with the same name appear repeatedly.

Status: Not executed.

### Preliminary judgment

- Possible reason: Both plugin and manual installer expose similar assets to harness.
- Exclusions: It has not been confirmed whether minimal profile also causes duplication.

### Subsequent processing

- Use `ecc plan` or `--dry-run` first.
- Log install-state.
- Verify `ecc uninstall` or manually rollback the path.

## Problem: Mistakenly believing that Codex will execute Claude-style hooks

- Discovery time: 2026-06-11
- Current status: Document level confirmed, running unverified
- Scope of influence: Codex integration, quality access control, security access control, session hooks

### Phenomenon

README and cross-harness architecture documents indicate that the Codex path mainly relies on `AGENTS.md`, plugin metadata, skills, MCP config and instruction-backed constraints, and does not have Claude-style hook parity.

### Preliminary judgment

- Possible reasons: The same repository contains `hooks/hooks.json`, and it is easy to mistakenly think that all harnesses will be executed.
- Conclusion: Codex cannot regard hook blocking as enabling security control, and the actual capabilities of Codex must be independently verified.

### Subsequent processing

- Codex paths only record instruction-backed verification.
- If strong access control is required, it should be verified in CI, pre-commit, wrapper script or harness that supports hooks.

## Problem: The installation write range is unknown

- Discovery time: 2026-06-11
- Current status: Not verified
- Scope of influence: user directory, project directory, team repository

### Phenomenon

ECC supports multiple targets and profiles. Different targets may be written to locations such as `~/.claude/`, `~/.codex/`, projects `.cursor/`, `.opencode/`, `.zed/`, etc.

### Preliminary judgment

- Possible reasons: There are many combinations of target adapter and profile.
- Risk: Direct install in the main environment may pollute the global configuration.

### Subsequent processing

```bash
npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json
npx --yes --package ecc-universal ecc install --profile minimal --target codex --dry-run --json
```

Install only after confirming planned file operations.

## Problem: README/release notes/plugin manifest capability number drifts

- Discovery time: 2026-06-11
- Current status: pending verification
- Scope of influence: collecting data, judging external capabilities, learning tasks

### Phenomenon

The README and release notes mention 261 skills; `.codex-plugin/plugin.json`’s short description mentions 249 skills. The two may come from different build times or statistical calibers.

### Preliminary judgment

- Possible reasons: catalog update or plugin manifest not synchronized.
- Risk: collect data is prone to expire when referencing specific quantities.

### Subsequent processing

- Run `npm run catalog:check` or `node scripts/ci/catalog.js --text` for review.
- The collect document gives priority to description of capability types and relies less on specific quantities.

## Problem: `npx ecc` may resolve the wrong npm package

- Discovery time: 2026-06-11
- Current status: confirmed npm metadata, not run ECC CLI
- Scope of impact: All verification commands that use npm to temporarily execute the ECC CLI

### Phenomenon

This review of `npm view ecc-universal name version bin --json` shows that the official package name is `ecc-universal@2.0.0`, and the bin contains `ecc`. Also `npm view ecc name version --json` shows that a separate `ecc@0.0.2` package exists on npm. Therefore, executing `npx ecc ...` directly may resolve to an old/unrelated package named `ecc` instead of the `ecc` bin exposed by `ecc-universal`.

### Preliminary judgment

- Possible reason: npm package name is inconsistent with bin name, and the README example uses bin name.
- Risk: The verification command appears to run ECC, but actually runs the wrong package.

### Subsequent processing

- Use explicit package selector:

```bash
npx --yes --package ecc-universal ecc --help
```

- Or use the local entrance after cloning the repository:

```bash
node scripts/ecc.js --help
```

- All commands to be verified in collect data use explicit package selectors.

## Problem: Hook blocking affects normal development

- Discovery time: 2026-06-11
- Current status: Not verified
- Scope of influence: Claude Code / OpenCode / Cursor hook-backed scenarios

### Phenomenon

`hooks/hooks.json` Contains configuration protection, MCP health check, quality gate, fact-forcing, format/typecheck, console.log check and other scripts. Strict profiles may block tool invocation or file editing.

### Preliminary judgment

- Possible reasons: hook profile, timeout, environment variables and project status jointly affect the behavior.
- Risk: Enabling strict hooks in unfamiliar projects may cause false blocking.

### Subsequent processing

- Start with minimal or standard profile.
- Record the matcher, id, stdout/stderr, and exit code of each hook.
- Read `scripts/hooks/` source code separately for blocking class hooks.

## Issue: Windows PowerShell paths and shell quoting

- Discovery time: 2026-06-11
- Current status: Not verified
- Scope of impact: Windows installer, PowerShell, Node hook runner

### Phenomenon

The project contains `install.ps1` and a large number of Node/shell hook commands. The release notes mention Windows path normalization and stdin prompt related hardening.

### Preliminary judgment

- Possible reasons: Cross-platform path, shell quoting, Node version and plugin root parsing are complex.
- Risk: Installation and hook execution under Windows need to be tested separately, and the results cannot be directly applied to macOS/Linux.

### Subsequent processing

- Dry-run in a temporary Windows test user or temporary project.
- Prioritize verification of planned output for `.\install.ps1 --profile minimal --target claude`.
- Log PATH, Node, PowerShell version and write files.

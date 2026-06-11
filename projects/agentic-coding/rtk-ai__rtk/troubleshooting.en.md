# RTK problem troubleshooting record

## 1. Installation and version

### Phenomenon: `rtk --version` succeeds but `rtk gain` does not work

- Possible reason: Another package with the same name `rtk` is installed on crates.io instead of `rtk-ai/rtk`.
-Based on: name collision warning in README.
- troubleshooting: Confirm the installation source, giving priority to using GitHub release, Homebrew or `cargo install --git https://github.com/rtk-ai/rtk`.
- Status: Not natively verified.

### Phenomenon: The README version example is inconsistent with the source code version

- Phenomenon: The README example is written as `rtk 0.28.2`, and the source code snapshot `Cargo.toml` version is `0.42.2`.
- Possible reasons: README examples are not synchronized, or there is a drift between the default branch and release documents.
- troubleshooting: Check GitHub release, tag and actual binary version.
- Status: pending verification.

## 2. Hook and Agent integration

### Phenomenon: There is no automatic rewriting command in Codex

- Possible reason: The Codex path is `AGENTS.md` / `RTK.md` prompt-level guidance, not a program-level hook.
- Based on: `hooks/codex/README.md` and `hooks/README.md`.
- troubleshooting: Confirm the writing position of `rtk init --codex` and check whether the Codex reads the corresponding instructions; explicitly call `rtk` if necessary.
- Status: pending verification.

### Phenomenon: Claude / Cursor hook does not rewrite the command

- Possible reasons: hook is not installed, settings are not patched, `rtk` is not in PATH, command does not match registry, command contains redirection or substitution is judged to be unverifiable.
- Based on: `src/hooks/README.md`, `src/hooks/rewrite_cmd.rs`, `src/discover/registry.rs`.
- Troubleshooting: Execute `rtk rewrite "<cmd>"` first, and then execute the hook check / verify command of the target Agent.
- Status: pending verification.

### Phenomenon: The command is rewritten but still requires user confirmation

- Possible reasons: host permission does not explicitly allow, RTK maps Default to ask.
- Based on: `src/hooks/permissions.rs` and `src/hooks/rewrite_cmd.rs` test instructions.
- Troubleshooting: Check the deny / ask / allow configuration of hosts such as Claude / Cursor / Gemini.
- Status: Source code sampling has been read, not_run.

## 3. Output filtering

### Phenomenon: Key debug details are missing after filtering

- Possible reasons: RTK outputs summary by default and does not guarantee to retain all raw output.
- troubleshooting: Use verbose, passthrough, `--no-compact` or tee full-output hint, and run native commands directly if necessary.
- Status: pending verification.

### Phenomenon: The command fails but the complete log cannot be seen

- Possible reasons: tee disabled, output is too short, `RTK_TEE=0`, tee directory cannot be written.
- Basis: `src/core/tee.rs`.
- troubleshooting: Set `RTK_TEE_DIR` to a temporary writable directory and reproduce the failed command.
- Status: pending verification.

## 4. Privacy and Telemetry

### Phenomenon: Worry about telemetry sending data

- Basis: README and `docs/TELEMETRY.md` declare that telemetry is turned off by default, requires explicit opt-in, and can be blocked by `RTK_TELEMETRY_DISABLED=1`.
- troubleshooting: run `rtk telemetry status`, check config and environment variables.
- Status: The document has been read, and the source code sending path needs to be verified.

## 5. Platform differences

### Phenomenon: Hook does not work automatically on Windows

- Possible reasons: README explains that the hook system under native Windows is limited, and WSL supports complete hooks.
- troubleshooting: Explicitly call `rtk <cmd>` in native Windows, or verify automatic rewriting in WSL.
- Status: Not natively installed and verified.

## Follow-up troubleshooting list

- [ ] `rtk --version` is aligned with release / Cargo version.
- [ ] `rtk rewrite "git status"` The output is as expected.
- [ ] `rtk rewrite` The handling of redirect, substitution and compound commands is in compliance with permission expectations.
- [ ] `rtk git diff`, `rtk cargo test`, `rtk pytest` output is readable and retains necessary failure information.
- [ ] `RTK_TEE_DIR` Recovery path available.
- [ ] The actual write range of `rtk init --codex` and the target Agent can be rolled back.

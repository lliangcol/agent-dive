# RTK source reading notes

## Read path

- `Cargo.toml`
- `src/main.rs`
- `src/hooks/rewrite_cmd.rs`
- `src/hooks/init.rs`
- `src/hooks/permissions.rs`
- `src/discover/registry.rs`
- `src/core/runner.rs`
- `src/core/filter.rs`
- `src/core/tracking.rs`
- `src/core/tee.rs`
- `src/cmds/git/git.rs`
- `hooks/README.md`
- `hooks/codex/README.md`
- `src/hooks/README.md`

## Important findings

- `rewrite_cmd.rs` Map allow / passthrough / deny / ask to different exit codes.
- Default in `permissions.rs` is not equal to Allow, the default should be ask.
- `registry.rs` will handle env prefix, git global opts, compound command and partial redirect / substitution boundaries.
- `core/runner.rs` provides three execution modes: captured, streamed, and passthrough.
- `tee.rs` Make local save and path prompt for failed raw output.

## To be verified

- Specific test coverage for each command filter.
- Whether the Rust test suite all passes.
- Whether the files written by hook installer are all atomic/backed up.
- Whether Codex guidance will be stably read in the actual Codex environment.

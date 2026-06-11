# RTK First impressions

## Impression in one sentence

RTK is a command output compression layer used by AI coding assistants. It is not an Agent framework, but a tool chain infrastructure that allows Agents to read less lengthy shell output.

## Worth paying attention to

- Rust single binary, with wide coverage of cross-ecological command filtering.
- The Hook document clearly distinguishes deployed hook, hook lifecycle, rewrite registry and command filters.
- The Codex path is prompt-level guidance, which needs to be distinguished from the Claude / Cursor transparent hook.
- There are tracking, tee recovery and telemetry opt-in documentation, indicating that the project is more than simple alias.

## Questions to be verified

- Whether the 60-90% savings of README can be reproduced in real workflows.
- Why the README version example is inconsistent with the `Cargo.toml` version.
- `rtk init --codex` What file is actually written and whether it is easy to roll back.
- Hook whether the permission model on the compound command is consistent with the document.

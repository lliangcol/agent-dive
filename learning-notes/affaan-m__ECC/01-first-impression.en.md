# ECC First impressions

## Positioning in one sentence

ECC is more like a workflow operating system across AI coding tools, rather than a simple prompt library, dotfiles or an Agent SDK.

## Initial Highlights

- Put skills, agents, commands, rules, hooks, MCP config, installer, sessions, and operator tools into the same project system.
- Clearly describe the boundaries of harnesses such as Codex, Claude Code, OpenCode, Cursor, etc.
- Installation and management do not just rely on manual copying of README, but have the concepts of selective install and manifest.
- Good for learning the governance, validation, context and security boundaries of agentic coding.

## Preliminary risks

- The scope is very large and you must study it in separate topics.
- Installation may affect user-level configuration and requires dry-run first.
- Hook behavior depends on harness and cannot be generalized across tools.
- The number of capabilities may drift with release.

## Questions to be verified

- Whether the output from `ecc plan` accurately explains the write range.
- Which skills and MCP configurations are actually exposed by the Codex plugin.
- Whether Claude plugin hooks are triggered stably.
- Whether `npm test` and catalog validators pass.

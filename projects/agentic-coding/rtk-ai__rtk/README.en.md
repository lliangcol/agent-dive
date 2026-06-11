# RTK

RTK, or Rust Token Killer, is a Rust CLI proxy for AI coding workflows. It rewrites common development commands to `rtk` equivalents and filters command output before it enters an LLM context.

## collect information

| Field | value |
|---|---|
| Project name | RTK |
| Project ID | `rtk-ai__rtk` |
| GitHub | https://github.com/rtk-ai/rtk |
| Project home page | https://www.rtk-ai.app |
| Main category | `agentic-coding` |
| Auxiliary tags | `token-optimization`、`cli-proxy`、`command-output-filtering`、`hooks`、`codex`、`claude-code` |
| collectlevel | Level B standard collect |
| Current status | `analyzing` |
| Default branch | `develop` |
| collect snapshot | 2026-06-11 |
| Analysis Commit | `6785a6c7695d7273e722214a295249a84819b6f0` |
| Whether to run verification locally | no |

## Why collect

- Explicitly related to AI coding Agent: README and hooks documentation indicate that it supports AI coding tools such as Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Hermes, Copilot, etc.
- Clear learning value: suitable for learning command output compression, hook command rewriting, Agent permission boundaries, context cost observation and development tool chain integration.
- High engineering reference value: The source code includes Rust CLI, command routing, ecological filter module, rewrite registry, hook installer, tracking SQLite, tee raw-output recovery and telemetry consent documents.
- Complementary to the existing AgentDive sample: it is more focused on "contextual input cost management" and "command output compression", and can be compared and learned with Caveman's output style compression and Graphify's code graph context management.

## Data generated

- [project deep dive](project-analysis.en.md)
- [source reading record](source-code-reading.en.md)
- [integration guide](integration-guide.en.md)
- [Problem troubleshooting records](troubleshooting.en.md)
- [Learning Todo List](learning-todo-list.md)
- [collectreport](collect-report.en.md)
- [diagrams directory](assets/diagrams/)

## Current validation boundaries

Verified:

- GitHub repository exists publicly.
- GitHub API shows that the default branch is `develop`, the main language is Rust, the License is Apache-2.0, and the homepage is `https://www.rtk-ai.app`.
- `git ls-remote --symref` displays HEAD pointing to `refs/heads/develop`, and the current HEAD is `6785a6c7695d7273e722214a295249a84819b6f0`.
- README describes CLI proxy, command filtering, auto-rewrite hook, analytics, tee raw-output recovery, telemetry opt-in and multi-agent support.
- Temporary shallow clone reads `Cargo.toml`, `src/main.rs`, `src/hooks/`, `src/discover/registry.rs`, `src/core/`, `hooks/`, `docs/contributing/ARCHITECTURE.md` and related README.

Not verified:

- `rtk` is not installed on this machine.
- not_run `rtk init`, `rtk rewrite`, `rtk gain` or any real filtering command.
- The actual writing and running effects of hooks on target Agents such as Claude Code / Codex / Gemini / Cursor have not been verified.
- The 60-90% token savings statistics in the README are not reproduced.
- The Rust test suite, installation script, or release binary was not executed.

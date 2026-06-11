# Caveman

Caveman is an output compression skill/plugin for AI coding assistants. It uses a set of prompt word rules, installers, hooks, status bars, and auxiliary tools to allow agents such as Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Cline, Copilot, etc. to express the same technical information in shorter replies.

## collect information

| Field | value |
|---|---|
| Project name | Caveman |
| Project ID | `JuliusBrussee__caveman` |
| GitHub | https://github.com/JuliusBrussee/caveman |
| Project home page | https://getcaveman.dev/ |
| Main category | `agentic-coding` |
| Auxiliary tags | `prompt-engineering`、`skills`、`claude-code`、`codex`、`mcp-tools`、`token-optimization` |
| collectlevel | Level B standard collect |
| Current status | `analyzing` |
| Default branch | `main` |
| collect snapshot | 2026-06-11 |
| Analysis Commit | `655b7d9c5431f822264b7732e9901c5578ac84cf` |
| Whether to run verification locally | no |

## Why collect

- Clearly related to AI Agent: README positions the project as Claude Code skill/plugin, and lists multiple Agent access methods such as Codex, Gemini, Cursor, Windsurf, Cline, and Copilot.
- The learning value is clear: it can be used to understand Agent reply style constraints, skill distribution, plug-in installation, hooks, status bar, token statistics, memory compression and MCP tool description compression.
- The engineering reference value is clear: the warehouse contains unified Node installer, shell / PowerShell shim, Claude Code hooks, Codex / Gemini command stubs, OpenCode plugin, MCP proxy, test and benchmark / eval directories.
- Suitable for generating diagrams and learning tasks: it can be split into installation path diagrams, hook activation diagrams, skill rule diagrams, MCP shrink diagrams and compression verification flow diagrams.

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
- GitHub API shows that the default branch is `main`, the main language is JavaScript, the License is MIT, and the homepage is `https://getcaveman.dev/`.
- `git ls-remote --symref` displays HEAD pointing to `refs/heads/main`, and the current HEAD is `655b7d9c5431f822264b7732e9901c5578ac84cf`.
- README/INSTALL.md describes unified installer, per-agent installation, `/caveman` mode, `caveman-compress`, `caveman-stats`, `caveman-shrink` and cavecrew sub-agents.
- GitHub tree shows that the repository contains `bin/install.js`, `skills/`, `src/hooks/`, `src/mcp-servers/caveman-shrink/`, `plugins/caveman/`, `tests/`, `benchmarks/` and `evals/`.

Not verified:

- `install.sh`, `install.ps1`, or `node bin/install.js` was not executed, so the native installation write range was not verified.
- `npx skills add JuliusBrussee/caveman -a codex` is not executed.
- The complete call chain of installer, Claude Code hooks, OpenCode plugin, MCP shrink, token stats and compress scripts has not been confirmed at the source code level.
- not_run Node/Python tests and benchmark/eval.

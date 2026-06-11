# ECC

ECC is a workflow operating system for AI coding tools and agent harnesses. It organizes skills, agents, commands, hooks, rules, MCP configurations, installation manifests, session/orchestration tools, and security gates into engineering assets that are portable across tools such as Claude Code, Codex, OpenCode, Cursor, Gemini, Zed, and more.

## Collection Information

| Field | value |
|---|---|
| Project name | ECC |
| Project ID | `affaan-m__ECC` |
| GitHub | https://github.com/affaan-m/ECC |
| Project home page | https://ecc.tools |
| Main category | `agentic-coding` |
| Auxiliary tags | `agent-harness`, `claude-code`, `codex`, `opencode`, `mcp-tools`, `security`, `workflow-automation` |
| Collection level | Level A in-depth collection |
| Current status | `analyzing` |
| Default branch | `main` |
| Collection snapshot | 2026-06-11 |
| Analysis Commit | `c888d2b73f26d605ff6c172b433d4cad2200206f` |
| Whether to run verification locally | no |

## Why Collect

- Explicitly related to AI Agent: Both README and `package.json` position the project as an agent workflow / operator system for harnesses such as Codex, Claude Code, OpenCode, Cursor, Gemini, etc.
- High learning value: can break down skills format, cross-harness adaptation, hook life cycle, security access control, MCP configuration, installation list, session recording, worktree orchestration and operator dashboard.
- High engineering reference value: The repository contains complete productized surfaces such as `scripts/`, `skills/`, `agents/`, `commands/`, `hooks/`, `rules/`, `.codex-plugin/`, `.claude-plugin/`, `.opencode/`, `ecc2/`, `tests/`, etc.
- Suitable for deep collection: the project scale is large, the capabilities are wide, and it highly overlaps with AgentDive’s agentic coding/governance/validation learning objectives.

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

- The GitHub repository exists publicly, the GitHub API shows that the default branch is `main`, the main language is JavaScript, and the License is MIT.
- `git ls-remote --symref` displays HEAD pointing to `refs/heads/main`, and the current HEAD is `c888d2b73f26d605ff6c172b433d4cad2200206f`.
- GitHub API displays topics including `ai-agents`, `claude-code`, `developer-tools`, `llm`, `mcp`, `productivity`.
- README describes the agent workflow surface across Codex, Claude Code, Cursor, OpenCode, Gemini, Zed, GitHub Copilot.
- `package.json` displays the npm package name `ecc-universal`, version `2.0.0`, bin contains `ecc`, `ecc-control-pane`, `ecc-install`, and the Node engine is `>=18`.
- npm metadata review shows that `ecc-universal@2.0.0` exposes `ecc` bin, and there is an independent `ecc@0.0.2` package on npm; subsequent verification should use explicit package selector or local source code script to avoid `npx ecc` parsing into the wrong package.
- `docs/architecture/cross-harness.md` Description: The durable workflow is placed in `skills/`, `rules/`, `hooks/`, `scripts/`, `mcp-configs/`, and each harness only performs thin adaptation.
- `hooks/hooks.json` Contains hook life cycle configurations such as PreToolUse, PreCompact, SessionStart, PostToolUse, Stop, SessionEnd, etc.

Not verified:

- The Claude plugin, Codex plugin or npm package is not installed locally.
- not_run `npx --package ecc-universal ecc ...`, local `node scripts/ecc.js ...`, `ecc install`, `ecc plan`, `ecc doctor`, `npm test`.
- The actual triggering behavior of hooks in Claude Code, OpenCode, and Cursor has not been verified.
- The loading effect of Codex's skill, plugin, and MCP configurations has not been verified.
- Completely track all call chains of install, hook, control-pane, session, and worktree lifecycle at the source code level.
- It has not been verified whether the number of capabilities in the README / release notes / plugin manifest is exactly the same.

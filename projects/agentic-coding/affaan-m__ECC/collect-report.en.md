# ECC collection report

## 1. Basic information

- GitHub address: https://github.com/affaan-m/ECC
- Collection time: 2026-06-11
- Project name: ECC
- Project ID: `affaan-m__ECC`
- Project category: `agentic-coding`
- Collection level: Level A in-depth collection
- Current status: `analyzing`
- Whether collection is recommended: Yes
- Collector / Agent: Codex

## 2. collection basis

- Relevance to AI Agent: Explicitly relevant. The project description, README, `package.json`, and plugin manifest all revolve around AI coding harnesses such as Claude Code, Codex, OpenCode, Cursor, and Gemini.
- Project learning value: high. Covers topics such as skills, agents, commands, hooks, rules, MCP, install manifests, session adapters, worktree lifecycle, operator dashboard, security gates, etc.
- Engineering reference value: high. Contains CLI, selective installer, hook runtime, plugin manifests, OpenCode adapter, Codex config, tests and CI validators.
- Documentation and source code analyzability: High. README, Chinese README, multi-language docs, architecture docs, release notes, source code and test directories are complete.
- License preliminary judgment: MIT.
- Whether this is a duplicate collection: `PROJECTS.md` was not found before collect or there is already `affaan-m/ECC` in the repository.

## 3. Risk

- Operational risks: not installed, not executed CLI, not verified plugin and hook behavior.
- Maintenance risk: The project capabilities are very broad, and the number and terminology of manifest, plugin, catalog, and README may drift.
- Security risks: hooks, MCP configuration, installer and operator tools involve local files, commands, configurations and possible global writes, which require strict auditing.
- Document expiration risk: README, release notes, and plugin manifest may not be at the same generation point.
- Conclusion Items to be verified: Codex plugin loading, Claude hook triggering, OpenCode event adapter, Windows installer, Node version compatibility, catalog/test status.

## 4. Generate file list

- [x] `projects/agentic-coding/affaan-m__ECC/README.md`
- [x] `projects/agentic-coding/affaan-m__ECC/meta.json`
- [x] `projects/agentic-coding/affaan-m__ECC/project-analysis.md`
- [x] `projects/agentic-coding/affaan-m__ECC/source-code-reading.md`
- [x] `projects/agentic-coding/affaan-m__ECC/integration-guide.md`
- [x] `projects/agentic-coding/affaan-m__ECC/troubleshooting.md`
- [x] `projects/agentic-coding/affaan-m__ECC/learning-todo-list.md`
- [x] `projects/agentic-coding/affaan-m__ECC/collect-report.md`
- [x] `projects/agentic-coding/affaan-m__ECC/assets/diagrams/`
- [x] `learning-notes/affaan-m__ECC/`
- [x] `PROJECTS.md` Update
- [x] `LEARNING_PROGRESS.md` Update

## 5. Verified content

- GitHub API displays the public repository, default branch `main`, main language JavaScript, and License MIT.
- GitHub API shows Star 212486, Fork 32632, and `open_issues_count` are 60; GitHub Search API is split into open issues 20 and open PRs 40. topics include `ai-agents`, `claude-code`, `developer-tools`, `llm`, `mcp`, `productivity`.
- `git ls-remote --symref` shows that HEAD points to `refs/heads/main` and commit is `c888d2b73f26d605ff6c172b433d4cad2200206f`.
- GitHub languages ​​API shows JavaScript, Rust, Python, Shell, TypeScript, Swift, CSS, PowerShell.
- README describes ECC v2.0.0 as a cross-harness agent workflow/operator system, covering Codex, Claude Code, Cursor, OpenCode, Gemini, Zed, GitHub Copilot, etc.
- `package.json` Display npm package `ecc-universal`, version `2.0.0`, bin `ecc` / `ecc-control-pane` / `ecc-install`, Node `>=18`.
- npm metadata review shows that `ecc-universal@2.0.0` is exposed `ecc` bin, and there is also an independent `ecc@0.0.2` package; subsequent verification commands should avoid writing `npx ecc ...` directly.
- `docs/architecture/cross-harness.md` Describes the boundaries of shared workflow sources and harness adapters.
- `hooks/hooks.json` Contains PreToolUse, PreCompact, SessionStart, PostToolUse, Stop, SessionEnd.
- The first round of source code check confirms the existence of entrances such as `scripts/ecc.js`, `scripts/install-plan.js`, `scripts/install-apply.js`, `scripts/lib/install-manifests.js`, `scripts/lib/install-executor.js`, `scripts/control-pane.js`.

## 6. Unverified content

- The complete source code has not been cloned and cached in this repository.
- Not executed `npx --package ecc-universal ecc ...`, local `node scripts/ecc.js ...`, `ecc plan`, `ecc install`, `ecc doctor`.
- `npm test` or catalog/hook/manifest validators not executed.
- The Claude plugin, Codex plugin, OpenCode package or Cursor adapter is not installed.
- Unverified hook actual triggering, blocking and timeout behavior.
- Did not verify that Codex MCP/skills/plugin is actually loaded.
- Control pane, session adapters, state store, worktree lifecycle not verified.

## 7. Matters awaiting manual confirmation

- [ ] Whether the License meets the AgentDive reference and learning collation strategy.
- [ ] Level A in-depth collection is in line with the current learning priority.
- [ ] Whether to allow actual installation of ECC minimal profile in an isolated environment.
- [ ] Whether to use the Codex path as the priority verification object.
- [ ] Whether special comparison with existing local AGENTS/skills/governance tools is required.

## 8. Next step suggestions

Follow-up actions: Do read-only verification first. Execute `npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json` and `npx --yes --package ecc-universal ecc consult "tdd code review security" --target codex`, record output and write range. Only after the dry-run results are acceptable, verify the Codex minimal profile and Claude plugin hook behavior in the staging environment.

## 9. Information snapshot

- Snapshot date: 2026-06-11
- GitHub API:https://api.github.com/repos/affaan-m/ECC
- README:https://raw.githubusercontent.com/affaan-m/ECC/main/README.md
- GitHub page: https://github.com/affaan-m/ECC
- Cross-harness architecture:https://raw.githubusercontent.com/affaan-m/ECC/main/docs/architecture/cross-harness.md
- Release notes:https://raw.githubusercontent.com/affaan-m/ECC/main/docs/releases/2.0.0/release-notes.md

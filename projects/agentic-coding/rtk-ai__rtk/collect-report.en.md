# RTK collect report

## 1. Basic information

- GitHub address: https://github.com/rtk-ai/rtk
-Collect time: 2026-06-11
- Project name: RTK
- Project ID: `rtk-ai__rtk`
- Project Category: `agentic-coding`
-Collect level: Level B standard collect
- Current status: `analyzing`
-Whether collect is recommended: Yes
- collect Person/Agent: Codex

## 2. collect basis

- Relevance to AI Agent: README is explicitly oriented to AI coding tools such as Claude Code, Codex, Gemini CLI, Cursor, Windsurf, OpenCode, Hermes, Copilot, etc.
- Project learning value: Covers command output compression, hook rewrite, AI tool integration, token savings analytics, raw-output recovery, telemetry consent and permission boundaries.
- Engineering reference value: Rust single binary, split filters according to ecology, hook as thin delegate, rewrite registry as single rule source.
- Documentation and source code analyzeability: The repository contains README, INSTALL.md, docs, hooks, src, tests fixtures, scripts and Cargo configurations.
- License preliminary judgment: GitHub API shows Apache-2.0.
- Whether to repeat collect: Repeat the check before collect and no existing entries of `rtk-ai__rtk` or `rtk-ai/rtk` were found.

## 3. Risk

- Operation risk: RTK has not been installed natively, `rtk init` or any target Agent hook has not been executed.
- Document drift risk: The README verification example is `rtk 0.28.2`, and the current source code `Cargo.toml` is `0.42.2`.
- Permission risk: The command rewrite involves host permission and Deny/Ask/Allow and compound command must be verified.
- Evidence risk: 60-90% savings in the README have not been reproduced and cannot be regarded as a verified conclusion in this warehouse.
- Platform risk: native Windows has limited automatic hooking capabilities, and WSL and Linux paths are more complete.
- Collection process limit: subsequent requests to the GitHub contents API trigger rate limit; source code structure is changed to temporary shallow clone reading for confirmation.

## 4. Generate file list

- [x] `projects/agentic-coding/rtk-ai__rtk/README.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/meta.json`
- [x] `projects/agentic-coding/rtk-ai__rtk/project-analysis.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/source-code-reading.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/integration-guide.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/troubleshooting.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/learning-todo-list.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/collect-report.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/assets/diagrams/`
- [x] `learning-notes/rtk-ai__rtk/`
- [x] `PROJECTS.md` Update
- [x] `LEARNING_PROGRESS.md` Update

## 5. Verified content

- GitHub API basic metadata: default branch `develop`, main language Rust, License Apache-2.0, homepage.
- `git ls-remote --symref`: HEAD points to `refs/heads/develop`, and HEAD commit is `6785a6c7695d7273e722214a295249a84819b6f0`.
- README: installation, quick start, command categories, hook scope, Windows limitation, telemetry opt-in.
- Source code sampling: `Cargo.toml`, `src/main.rs`, `src/hooks/`, `src/discover/registry.rs`, `src/core/runner.rs`, `src/core/tracking.rs`, `src/core/tee.rs`, `hooks/README.md`.

## 6. Matters awaiting manual confirmation

- [ ] Select the actual installation source and confirm `rtk --version`.
- [ ] Reproduce `rtk rewrite "git status"` and some command filtering effects.
- [ ] Verify `rtk init --codex` actual write location and rollback path.
- [ ] Verify that there is at least one transparent hook or plugin such as Claude Code / Cursor / Gemini / Hermes.
- [ ] Execute Rust test suite or minimal smoke.
- [ ] Reproduce or calibrate token savings statistical caliber.
- [ ] Audit telemetry build-time gating, opt-in, forget and server endpoint behavior.

## 7. Next step suggestions

1. Install or build RTK in a temporary environment and confirm the version.
2. Use the public small warehouse to verify `rtk rewrite`, `rtk git status`, `rtk git diff`, `rtk test`, `rtk gain`.
3. First verify the raw-output recovery under `RTK_TEE_DIR`, and then enter the hook installation.
4. Verify Codex and Claude Code separately because their integration mechanisms are different.
5. After completing a round of test suite and fixture reading, decide whether to upgrade to Level A.

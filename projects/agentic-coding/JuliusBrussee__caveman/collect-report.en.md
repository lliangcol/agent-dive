# Caveman collect report

## 1. Basic information

- GitHub address: https://github.com/JuliusBrussee/caveman
-Collect time: 2026-06-11
- Project name: Caveman
- Project ID: `JuliusBrussee__caveman`
- Project Category: `agentic-coding`
-Collect level: Level B standard collect
- Current status: `analyzing`
-Whether collect is recommended: Yes
- collect Person/Agent: Codex

## 2. collect basis

- Relevance to AI Agent: The README is clearly positioned as Claude Code skill/plugin, and lists Agent support such as Codex, Gemini, Cursor, Windsurf, Cline, Copilot, etc.
- Project learning value: Covers prompt compression, AI coding assistant skill, plug-in distribution, Claude Code hooks, statusline, token stats, memory compression, MCP metadata compression and subagents.
- Project reference value: It can be used as a project example of "how to distribute a set of Agent behavior rules across platforms and maintain installation/uninstallation/dry-run boundaries."
- Documentation and source code analyzeability: The repository contains README, INSTALL.md, CLAUDE.md, `bin/`, `skills/`, `src/hooks/`, `src/mcp-servers/`, `plugins/`, `tests/`, `benchmarks/` and `evals/`.
- License preliminary judgment: GitHub API displays MIT License.
- Whether to repeat collect: The repeated check before collect did not find the existing entry of `JuliusBrussee__caveman` or Caveman.

## 3. Risk

- Run risk: The installer has not been executed natively; one-liner or `--all` may write multiple user-level Agent configurations.
- Maintenance risk: There are many Agent platforms and installation commands supported, and INSTALL.md and source code provider matrix need to be verified simultaneously.
- Security risk: `caveman-compress` will process user-specified memory files and may process content through Anthropic SDK or Claude CLI; the installer and hooks involve user configuration writing.
- Document expiration risk: The current information is based on the 2026-06-11 snapshot and commit `655b7d9c5431f822264b7732e9901c5578ac84cf`.
- Conclusion Items to be verified: installer provider detection, dry-run no write guarantee, Codex installation path, Claude hooks, MCP shrink transparent transmission semantics, stats statistical caliber, benchmark recurrence.

## 4. Generate file list

- [x] `projects/agentic-coding/JuliusBrussee__caveman/README.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/meta.json`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/project-analysis.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/source-code-reading.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/integration-guide.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/troubleshooting.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/learning-todo-list.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/collect-report.md`
- [x] `projects/agentic-coding/JuliusBrussee__caveman/assets/diagrams/`
- [x] `learning-notes/JuliusBrussee__caveman/`
- [x] `PROJECTS.md` Update
- [x] `LEARNING_PROGRESS.md` Update

## 5. Matters awaiting manual confirmation

- [ ] Whether the License meets the target publishing and citation methods.
- [ ] `node bin/install.js --dry-run --all` Whether there is no writing at all.
- [ ] Whether Codex single-agent installation affects only the intended configuration.
- [ ] Whether Claude Code hooks, statusline and mode flag work as documented.
- [ ] `caveman-shrink` Whether to compress only expected metadata fields.
- [ ] Whether `caveman-compress`'s backups, paths, sizes, and API/CLI fallback meet security expectations.
- [ ] Whether benchmark / eval is reproducible and whether the statistical caliber is suitable for learning in this warehouse.

## 6. Next step suggestions

1. Execute `node bin/install.js --list` and `node bin/install.js --dry-run --all` in temporary clones.
2. Read `bin/install.js`, `src/hooks/*.js`, `src/mcp-servers/caveman-shrink/*.js` and `skills/caveman-compress/scripts/*.py`.
3. Use the test Agent or isolation configuration directory to perform single-path installation and uninstallation verification.
4. Verify `caveman-shrink` and `caveman-compress` using a test MCP server with a non-sensitive memory file.
5. After reproducing a set of benchmarks/evals, decide whether to upgrade to Level A depth collection.

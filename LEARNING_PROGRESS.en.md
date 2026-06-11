# Learning Progress

This document records an overview of global learning progress. Detailed learning notes and progress of a single project should be placed at `learning-notes/<owner__repo>/`.

## Overall learning status

- Current stage: the first batch of project quality governance and learning closed-loop verification stage
- Current focus: Unifying the metadata, evidence files, learning TODOs and progress records of Hermes Agent, ECC, Ruflo, Graphify, Caveman, RTK, Claude HUD and CodeGraph
- Last updated: 2026-06-11
- Quality gate control: Before the project is promoted to `study-ready`, `in-study` or `completed`, it must pass `python scripts/check-agent-dive.py` and have real operation or source code verification records in `evidence.md`

## The project currently being studied

| Project name | Project ID | current stage | Completion progress | stuck problem | next steps |
|---|---|---|---:|---|---|
| Hermes Agent | NousResearch__hermes-agent | analyzing | 4/36 | The source code has not been cloned, and the installation and `hermes doctor` have not been run locally. | Fixed verification of source code call chain and minimum run after commit |
| ECC | affaan-m__ECC | analyzing | 0/43 | not_run native CLI; not verified Codex plugin / Claude hooks / install write scope | First execute the read-only `npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json`, and then trace the install and hook call chains |
| Ruflo | ruvnet__ruflo | analyzing | 0/39 | not_run CLI/init/MCP; Claude hooks, Codex `.agents` configuration and plugin marketplace behavior not verified | First execute read-only `npx --yes ruflo@latest --version`, `npx --yes ruflo@latest --help`, and then trace the CLI/MCP/Swarm/Memory call chain |
| Graphify | safishamsi__graphify | analyzing | 0/36 | not_run native CLI; source call chain not verified; Codex install write scope not verified | Read the official architecture and security documents, and use the public small repository to run `graphify .` |
| Caveman | JuliusBrussee__caveman | analyzing | 0/35 | not_run unified installer dry-run; installer, hooks, MCP shrink and memory compression call chains not verified | Execute `node bin/install.js --list` and `node bin/install.js --dry-run --all` in temporary clones |
| RTK | rtk-ai__rtk | analyzing | 0/36 | No native binary installed; no verification of `rtk rewrite`, filtered output, hook writing, and token savings statistics | Execute `rtk rewrite "git status"` in the temporary environment, and then verify `rtk git status`, tee recovery and target Agent integration |
| Claude HUD | jarrodwatts__claude-hud | analyzing | 0/35 | plugin/setup not installed in real Claude Code; Windows temporary `npm test` currently fails | First use temporary `CLAUDE_CONFIG_DIR` to verify setup writing, and then locate the Windows test failure group |
| CodeGraph | colbymchenry__codegraph | analyzing | 15/33 | completed cache cloning, build, CLI version/help, `init -i`, `status`, query/callers/impact, MCP initialize/tools-list, and a focus test; full testing is still pending | Continue Level 3 source reading and confirm the full test or focused test subset criteria |

## completed projects

| Project name | Project ID | completion time | Summary link |
|---|---|---|---|
| - | - | - | - |

## Stuck problem

- Hermes Agent: The source code function level verification has not been completed, and the local installation and runtime verification has not been completed.
- ECC: CLI dry-run, Codex plugin loading, Claude/OpenCode hook execution and install write range verification were not completed.
- Ruflo: CLI/init/MCP native run verification not completed, Claude Code plugin, Codex `.agents` configuration, hooks and web UI not verified.
- Graphify: Native CLI run, source call chain verification, and Codex project install write scope verification were not completed.
- Caveman: Unified installer dry-run, single-agent installation/uninstallation, Claude hooks, MCP shrink, memory compression and benchmark replication verification have not been completed.
- RTK: Local installation, `rtk rewrite` smoke, command filter comparison, hook write range, raw-output recovery and token savings replication verification have not been completed.
- Claude HUD: Not completing real Claude Code plugin install, `/claude-hud:setup` write verification, HUD display verification and Windows test failure location.
- CodeGraph: CLI build, `init -i`, `status`, query/callers/impact, MCP initialize/tools-list and a spotlight test passed; full test suite, MCP tools/call sampling and npm audit risk review not completed.

## Suggestions for next step of study

- [x] Select at least 1 Level A project as an in-depth collection sample.
- [x] Generate project deep dive, diagrams and learning Todo List for project collection.
- [x] Complete unified `meta.json`, `evidence.md`, `progress.json` and structured Learning Todo List.
- [x] Added AI Agent continuous learning protocol.
- [x] Add `python scripts/check-agent-dive.py` consistency check.
- [x] Perform a real CLI/MCP minimum run verification against CodeGraph.
- [ ] Supplement CodeGraph with MCP `tools/call` sampling, full testing, or an approved subset of focused testing.
- [ ] Perform an isolation environment rewrite / filter / tee smoke on RTK.
- [ ] Complete basic topics such as Agent Loop, Tool Calling, RAG, and MCP according to the learning route.

## Review plan

| review topic | Related projects | Plan time | state |
|---|---|---|---|
| The boundary between Agent Loop and Tool Calling | - | Not scheduled | Not started |
| Retrieval and generation links of RAG Agent | - | Not scheduled | Not started |
| MCP tool access process | colbymchenry__codegraph | Not scheduled | Started |

# Hermes Agent collect report

## 1. Basic information

- GitHub address: https://github.com/NousResearch/hermes-agent
-Collect time: 2026-06-10
- Project name: Hermes Agent
- Project ID: `NousResearch__hermes-agent`
- Project Category: `product-agents`
-Collect level: Level A deep collect
- Current status: `analyzing`
-Whether collect is recommended: Yes
- collect Person/Agent: Codex

## 2. collect basis

- Relevance to AI Agent: The README is clearly positioned as a self-improving AI Agent and describes learning loops, skills, memory, tool calling, gateway, cron, MCP, and multi-run backends.
- Project learning value: Covers the complete engineering aspect of product-level Agent, which can be used to learn Agent Loop, tool system, memory system, message gateway, MCP, scheduling and security boundaries.
- Engineering reference value: The official architecture page provides entrance, core modules, data flow and recommended reading order; the warehouse includes CLI, gateway, tools, cron, providers, skills, plugins, tests and other modules.
- Documentation and source code analyzeability: The GitHub repository is public, and the README, official docs, and root directory contents API are all accessible.
- License preliminary judgment: GitHub API displays MIT License.
- Whether to repeat collect: No existing entry for `NousResearch__hermes-agent` was found during collect; if other items are added to the index later, it will not affect the deduplication conclusion of this project.

## 3. Information snapshot

- Snapshot date: 2026-06-10
- Default branch: `main`
- Collection commit: `a72bb03757c0c925c686f9774eefc8dc5a77b329`
- Main language: Python
- Stars at collect：189655
- Forks at collect：32817
- Open issues at collect：19701
- Repo updated at：2026-06-10T15:34:40Z
- Repo pushed at：2026-06-10T15:24:05Z

The above counts are from the GitHub API at the time of collection and will change later.

## 4. Risks

- Run risk: The installer will handle multiple dependencies and runtimes, and differences in actual environments may cause failure; currently it is not_run.
- Maintenance risk: The warehouse is active and changes rapidly, and the conclusion must be bound to date and commit.
- Security risks: terminal, file, browser, MCP, gateway and remote backend may trigger high-risk side effects.
- Risk of document expiration: README, official website documents and source code may be out of sync, and subsequent source code review is required.
- Conclusion Items to be verified: `AIAgent` Function-level main loop, tool registration details, memory persistence, gateway authorization, cron status update, MCP error handling.

## 5. Generate file list

- [x] `projects/product-agents/NousResearch__hermes-agent/README.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/project-analysis.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/source-code-reading.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/integration-guide.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/troubleshooting.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/learning-todo-list.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/collect-report.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/assets/diagrams/`
- [x] `learning-notes/NousResearch__hermes-agent/README.md`
- [x] `PROJECTS.md` Update
- [x] `LEARNING_PROGRESS.md` Update

## 6. Verified content

- The GitHub repository exists and is a public repository.
- The GitHub API shows that the default branch is `main`, the primary language is Python, and the License is MIT.
- README Description Hermes Agent has CLI, gateway, tools, skills, memory, MCP, cron, subagents and multi-run backend.
- The official architecture page describes the core `AIAgent`, tool registry, session storage, gateway, cron and recommended source reading order.

## 7. Unverified content

- The installation script was not executed.
- `hermes`, `hermes doctor`, `hermes model`, `hermes tools` are not executed.
- The source code is not cloned for function-level call chain verification.
- Provider, MCP, gateway, cron, terminal backend or skills self-improvement capabilities are not verified.
- Mermaid diagrams are not exported to PNG/SVG.

## 8. Matters awaiting manual confirmation

- [ ] Whether the License meets the current warehouse reference, summary and learning arrangement methods.
- [ ] Whether the core call chain is consistent with the source code.
- [ ] Whether Quick Start can actually run through the target environment.
- [ ] Whether the diagrams are consistent with the source code implementation.
- [ ] Level A Depth collection investment is in line with the current learning priority.

## 9. Next step suggestions

1. Clone the source code to `.cache/sources/NousResearch__hermes-agent/` or the temporary isolation directory.
2. Fixed commit `a72bb03757c0c925c686f9774eefc8dc5a77b329`.
3. Verify the portal, Agent Loop, tool registry, memory, gateway, MCP and cron in the order of `source-code-reading.md`.
4. Perform a minimal installation and `hermes doctor` in an isolated environment.
5. Update the diagrams based on the actual source code and operation results, and advance the `PROJECTS.md` status from `analyzing` to `documented` or `study-ready`.

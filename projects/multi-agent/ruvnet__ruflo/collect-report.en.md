# Ruflo collect report

## 1. Basic information

- GitHub address: https://github.com/ruvnet/ruflo
-Collect time: 2026-06-11
- Project name: Ruflo
- Project ID: `ruvnet__ruflo`
- Project Category: `multi-agent`
-Collect level: Level A deep collect
- Current status: `analyzing`
-Whether collect is recommended: Yes
- collect Person/Agent: Codex

## 2. collect basis

- Relevance to AI Agent: Explicitly relevant. The README is positioned as a multi-agent AI harness for Claude Code and Codex, covering agents, swarm, memory, MCP, hooks, federation and Web UI.
- Project learning value: high. Suitable for learning multi-agent coordination, MCP stdio, memory backend, plugin lifecycle, hook boundaries, Codex / Claude Code integration differences.
- Engineering reference value: high. The repository contains npm packages, CLI, MCP server, domain runtime, plugin marketplace, Web UI, security policy, and signed witness verification.
- Documentation and source code analyzeability: high. README, package metadata, plugin manifests, runtime source, and verification docs can all be read; however, the complete running path still requires subsequent actual testing.
- License preliminary judgment: MIT.
- Whether to repeat collect: `PROJECTS.md` was not found before collect or there is already `ruvnet/ruflo` in the warehouse.

## 3. Risk

- Operation risk: CLI init will write the project/harness configuration; MCP server may pull npm packages and heavy dependencies.
- Maintenance risk: Ruflo / Claude Flow naming coexistence, the number of README, npm packages, plugin manifest and source code may drift.
- Security risks: hooks, MCP tools, memory, Web UI, federation, and provider config all involve local file, command, network, and data boundaries.
- Document expiration risk: The number of agents, commands, plugins, and MCP tools in the README needs to be reviewed with the actual tool list/inventory.
- Conclusion items to be verified: CLI help/version, MCP tool list, Claude Code plugin, CLI full init, Codex `.agents` config, hooks, Web UI, witness scripts.

## 4. Generate file list

- [x] `projects/multi-agent/ruvnet__ruflo/README.md`
- [x] `projects/multi-agent/ruvnet__ruflo/meta.json`
- [x] `projects/multi-agent/ruvnet__ruflo/project-analysis.md`
- [x] `projects/multi-agent/ruvnet__ruflo/source-code-reading.md`
- [x] `projects/multi-agent/ruvnet__ruflo/integration-guide.md`
- [x] `projects/multi-agent/ruvnet__ruflo/troubleshooting.md`
- [x] `projects/multi-agent/ruvnet__ruflo/learning-todo-list.md`
- [x] `projects/multi-agent/ruvnet__ruflo/collect-report.md`
- [x] `projects/multi-agent/ruvnet__ruflo/assets/diagrams/`
- [x] `learning-notes/ruvnet__ruflo/`
- [x] `PROJECTS.md` Update
- [x] `LEARNING_PROGRESS.md` Update

## 5. Matters awaiting manual confirmation

- [ ] Level A depth collection is in line with the current learning priority.
- [ ] Whether to prioritize the Codex `.agents` path or the Claude Code plugin path.
- [ ] Whether the specific quantity in the README needs to be solidified after running inventory / tool list.
- [ ] Whether to allow Ruflo full init in temporary projects.
- [ ] Web UI / mcp-bridge Whether to be included in the current learning scope.

## 6. Next step suggestions

Follow-up actions: Do read-only verification first. Execute `npx --yes ruflo@latest --version`, `npx --yes ruflo@latest --help`, `npx --yes ruflo@latest mcp start --help`. If the output and environment are acceptable, execute `init wizard` in the temporary project and record the writing range. Finally, use MCP client to verify the tool list and backfill the actual results into the integration notes.

## 7. Basis for this verification

- GitHub page: https://github.com/ruvnet/ruflo
- GitHub raw / temporary shallow clone HEAD: `6a2964ac94e10ca9916da030302686c725638adb`
- npm metadata：`ruflo@3.10.41`、`claude-flow@3.10.41`、`@claude-flow/cli@3.10.41`、`@claude-flow/codex@3.0.0-alpha.12`
- Key source code: `ruflo/bin/ruflo.js`, `v3/@claude-flow/cli/bin/cli.js`, `v3/@claude-flow/cli/src/commands/index.ts`, `v3/@claude-flow/cli/src/mcp-tools/index.ts`, `v3/src/*`

## Quality check items

- [x] No spurious run results are generated.
- [x] Not writing the README retelling as a verified operational conclusion.
- [x] collect level matches output requirements.
- [x] Directory ID uses `ruvnet__ruflo`.

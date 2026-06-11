# Ruflo Evidence

## Snapshot

- Project ID: `ruvnet__ruflo`
- GitHub: https://github.com/ruvnet/ruflo
- Category: `multi-agent`
- Collect level: Level A
- Current status: `analyzing`
- Source snapshot commit: `6a2964ac94e10ca9916da030302686c725638adb`
- Source cache path: `.cache/sources/ruvnet__ruflo`
- TODO progress at migration: 0/39

## Verification Status

| Area | Status | Notes |
|---|---|---|
| Runtime / CLI | `not_run` | Unless the evidence of the command below is recorded as `pass`, local running will not be counted as verified. |
| Test suite | `not_run` | not_run yet. |
| Source review | `partial` | The first round of source code or document analysis has been completed, but function-level verification has not yet been completed. |
| Diagrams | `draft` | Mermaid diagrams are available; renderings and source code level accuracy still need to be reviewed. |
| Learning notes | `created` | The learning notes skeleton already exists and must be updated one by one along with the tasks. |

## Command Evidence

| Date | Environment | Command / Operation | Scope | Result | Output summary | Follow-up |
|---|---|---|---|---|---|---|
| 2026-06-11 | AgentDive Document Analysis | Viewed GitHub metadata, README/docs and partial source code paths | Public repository and generated AgentDive files | `partial` | Metadata and first round analysis have been recorded; local run pass is not declared. | Continue to advance Level 2 and Level 3 missions. |
| pending | `.cache/sources/ruvnet__ruflo` | Run the smoke command | Isolated clones or temporary configurations | `not_run` | Not implemented yet. | Before marking a running task as complete, log the command, exit code, output summary, and write range. |

## Known gaps

- Local Ruflo CLI and init commands are not verified
- MCP server tool list is not verified
- Claude Code plugin marketplace behavior is not verified
- Codex .agents config and skills loading are not verified
- Web UI and mcp-bridge are not verified

## Next action

- Run read-only version/help commands for ruflo
- Compare explicit @claude-flow/cli claude-flow bin
- Trace CLI, command registry, MCP tools, swarm, workflow, and memory backends

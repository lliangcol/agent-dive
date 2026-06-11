# Caveman Evidence

## Snapshot

- Project ID: `JuliusBrussee__caveman`
- GitHub: https://github.com/JuliusBrussee/caveman
- Category: `agentic-coding`
- Collect level: Level B
- Current status: `analyzing`
- Source snapshot commit: `655b7d9c5431f822264b7732e9901c5578ac84cf`
- Source cache path: `.cache/sources/JuliusBrussee__caveman`
- TODO progress at migration: 0/35

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
| pending | `.cache/sources/JuliusBrussee__caveman` | Run the smoke command | Isolated clones or temporary configurations | `not_run` | Not implemented yet. | Before marking a running task as complete, log the command, exit code, output summary, and write range. |

## Known gaps

- Unified installer dry-run is not verified
- Local agent installation and uninstall behavior are not verified
- Source-level call chains for installer, hooks, MCP shrink, and memory compression are not verified
- Benchmarks and token statistics are not reproduced

## Next action

- Run installer --list in a temporary clone
- Run installer dry-run and record write scope
- Trace installer, hooks, MCP shrink, and memory compression scripts

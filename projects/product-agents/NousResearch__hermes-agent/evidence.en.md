# Hermes Agent Evidence

## Snapshot

- Project ID: `NousResearch__hermes-agent`
- GitHub: https://github.com/NousResearch/hermes-agent
- Category: `product-agents`
- Collect level: Level A
- Current status: `analyzing`
- Source snapshot commit: `a72bb03757c0c925c686f9774eefc8dc5a77b329`
- Source cache path: `.cache/sources/NousResearch__hermes-agent`
- TODO progress at migration: 4/36

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
| 2026-06-10 | AgentDive Document Analysis | Viewed GitHub metadata, README/docs and partial source code paths | Public repository and generated AgentDive files | `partial` | Metadata and first round analysis have been recorded; local run pass is not declared. | Continue to advance Level 2 and Level 3 missions. |
| pending | `.cache/sources/NousResearch__hermes-agent` | Run the smoke command | Isolated clones or temporary configurations | `not_run` | Not implemented yet. | Before marking a running task as complete, log the command, exit code, output summary, and write range. |

## Known gaps

- Source is not cloned locally
- Local install and hermes doctor are not verified
- Provider, MCP, gateway, cron, and terminal backend behavior are not verified

## Next action

- Clone source into .cache/sources/NousResearch__hermes-agent and pin commit
- Run hermes doctor in an isolated environment
- Verify AIAgent, tool registry, memory, gateway, MCP, and cron call chains

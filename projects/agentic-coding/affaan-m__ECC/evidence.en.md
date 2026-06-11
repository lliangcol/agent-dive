# ECC Evidence

## Snapshot

- Project ID: `affaan-m__ECC`
- GitHub: https://github.com/affaan-m/ECC
- Category: `agentic-coding`
- Collection level: Level A
- Current status: `analyzing`
- Source snapshot commit: `c888d2b73f26d605ff6c172b433d4cad2200206f`
- Source cache path: `.cache/sources/affaan-m__ECC`
- TODO progress at migration: 0/43

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
| pending | `.cache/sources/affaan-m__ECC` | Run the smoke command | Isolated clones or temporary configurations | `not_run` | Not implemented yet. | Before marking a running task as complete, log the command, exit code, output summary, and write range. |

## Known gaps

- Local ECC CLI and npm commands are not verified
- Codex plugin and MCP loading are not verified
- Claude/OpenCode hook execution is not verified
- Full source-level call chains are not verified

## Next action

- Run read-only ECC plan command with explicit npm package selector
- Trace scripts/ecc.js, install-plan.js, install-apply.js, and hooks/hooks.json
- Record dry-run write scope in evidence.md

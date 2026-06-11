# Claude HUD Evidence

## Snapshot

- Project ID: `jarrodwatts__claude-hud`
- GitHub: https://github.com/jarrodwatts/claude-hud
- Category: `agentic-coding`
- Collect level: Level B
- Current status: `analyzing`
- Source snapshot commit: `9650a43600e9bcc94057fbd693a7f05aba4ee1ff`
- Source cache path: `.cache/sources/jarrodwatts__claude-hud`
- TODO progress at migration: 0/35

## Verification Status

| Area | Status | Notes |
|---|---|---|
| Runtime / CLI | `not_run` | Unless the evidence of the command below is recorded as `pass`, local running will not be counted as verified. |
| Test suite | `fail` | fail - collection note says npm ci succeeded but npm test failed on Windows; rerun with captured logs before counting as stable evidence. |
| Source review | `partial` | The first round of source code or document analysis has been completed, but function-level verification has not yet been completed. |
| Diagrams | `draft` | Mermaid diagrams are available; renderings and source code level accuracy still need to be reviewed. |
| Learning notes | `created` | The learning notes skeleton already exists and must be updated one by one along with the tasks. |

## Command Evidence

| Date | Environment | Command / Operation | Scope | Result | Output summary | Follow-up |
|---|---|---|---|---|---|---|
| 2026-06-11 | AgentDive Document Analysis | Viewed GitHub metadata, README/docs and partial source code paths | Public repository and generated AgentDive files | `partial` | Metadata and first round analysis have been recorded; local run pass is not declared. | Continue to advance Level 2 and Level 3 missions. |
| pending | `.cache/sources/jarrodwatts__claude-hud` | Run the smoke command | Isolated clones or temporary configurations | `not_run` | Not implemented yet. | Before marking a running task as complete, log the command, exit code, output summary, and write range. |

## Known gaps

- Real Claude Code plugin install is not verified
- Windows npm test currently fails
- Real statusline stdin and transcript JSONL samples are not captured

## Next action

- Verify setup writes with a temporary CLAUDE_CONFIG_DIR
- Isolate the Windows npm test failure group
- Install in a test Claude Code profile and restart to verify HUD

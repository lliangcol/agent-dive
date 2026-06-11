# RTK Evidence

## Snapshot

- Project ID: `rtk-ai__rtk`
- GitHub: https://github.com/rtk-ai/rtk
- Category: `agentic-coding`
- Collect level: Level B
- Current status: `analyzing`
- Source snapshot commit: `6785a6c7695d7273e722214a295249a84819b6f0`
- Source cache path: `.cache/sources/rtk-ai__rtk`
- TODO progress at migration: 0/36

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
| pending | `.cache/sources/rtk-ai__rtk` | Run the smoke command | Isolated clones or temporary configurations | `not_run` | Not implemented yet. | Before marking a running task as complete, log the command, exit code, output summary, and write range. |

## Known gaps

- Local RTK install and version verification are not complete
- rtk rewrite and command-filter smoke tests are not run
- Target-agent hook install and rollback paths are not verified
- Token savings numbers are not reproduced
- Rust test suite and telemetry source path are not fully verified

## Next action

- Install or build RTK in a temporary environment
- Run rtk rewrite and command filter smoke tests
- Verify raw-output tee recovery with RTK_TEE_DIR in a temporary directory

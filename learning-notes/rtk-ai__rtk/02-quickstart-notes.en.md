# RTK Quickstart notes

## Current status

not run.

## Command to be executed

```bash
rtk --version
rtk rewrite "git status"
git status
rtk git status
rtk gain
```

## Verification record template

| Check items | Order | expected | actual | state |
|---|---|---|---|---|
| binary source | `rtk --version` | GitHub RTK, not Rust Type Kit | To be filled in | Not verified |
| rewrite | `rtk rewrite "git status"` | Output `rtk git status` | To be filled in | Not verified |
| filter output | `rtk git status` | compact status | To be filled in | Not verified |
| tracking | `rtk gain` | Can read local statistics | To be filled in | Not verified |
| tee recovery | Failed command + `RTK_TEE_DIR` | full-output hint | To be filled in | Not verified |

## Notes

- Do not execute global `rtk init -g` without confirming the write range.
- Windows native behaves differently from WSL, and the isolation environment is preferred for hook verification.

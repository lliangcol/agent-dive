# RTK integration notes

## Current status

Not integrated.

## Target path

1. Local explicit command: first use `rtk git status`, `rtk git diff`, `rtk test` to verify the value.
2. Codex: Verify `rtk init --codex` writes `$CODEX_HOME` or `~/.codex` `RTK.md` / `AGENTS.md` relationship.
3. Claude Code: Verify transparent PreToolUse hook, permission ask / allow / deny behavior.
4. Cursor/Gemini/Hermes: Verify later as needed.

## Write range record template

| Agent | Order | write file | backup | rollback | state |
|---|---|---|---|---|---|
| Codex | To be filled in | To be filled in | To be filled in | To be filled in | Not verified |
| Claude Code | To be filled in | To be filled in | To be filled in | To be filled in | Not verified |

## integration principle

- Manual command first, then hook.
- First project/temp config, then global.
- Confirm raw output recovery first, then rely on filtered output.

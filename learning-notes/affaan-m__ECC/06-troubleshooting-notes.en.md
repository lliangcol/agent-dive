# ECC problem troubleshooting notes

## List of current issues

| question | state | Next step |
|---|---|---|
| Repeated installation results in duplicate hooks/skills | To be verified | First dry-run, record install-state |
| Codex hook parity misunderstanding | Document level validation | Verify by instruction-backed |
| Unknown writing range | To be verified | Run `ecc plan --json` |
| Ability quantity drift | To be verified | Run catalog check |
| Windows installer behavior | To be verified | Testing in an isolated environment |

## troubleshooting principle

- Retain original command and exit code for each issue.
- Do not record tokens, accounts, and private paths.
- Distinguish between README description, source code judgment and local operation results.

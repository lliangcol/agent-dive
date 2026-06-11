# Ruflo problem troubleshooting notes

## Issue identified

| question | Current status | Next step |
|---|---|---|
| Plugin lite is confused with full install | README level confirmation | split path verification |
| Codex supports unclear boundaries | Initial confirmation at source code level | Test `.agents` and `@claude-flow/codex` |
| Hooks are not blocked if they fail | Source code level confirmation | trigger hook smoke |
| Windows hooks are different from POSIX hooks | Source code level confirmation | Windows Temporary Project Verification |
| MCP stdout pollution | Source code protected | MCP client smoke |
| Ability quantity drift | To be verified | Run inventory/tool ​​list |
| CLI init has a large writing range | README level confirmation | Temporary project verification |

## Recording requirements

- Document the command, environment, output, writing to files, and rollback methods for each problem.
- Security-related issues must distinguish between "prompt/assisted" and "hard blocking".
- Windows and POSIX behavior are documented separately.

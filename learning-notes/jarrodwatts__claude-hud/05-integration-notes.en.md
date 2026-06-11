# integrationnotes

## integration boundary

Claude HUD writes user-level Claude Code configuration and should not be submitted to the business repository. `settings.json` should be backed up before actual execution.

## Recommended verification order

1. Temporary source code construction.
2. Temporary `CLAUDE_CONFIG_DIR` setup is written.
3. Test the Claude Code profile installation.
4. Main environment installation.

## Current blocking

- Windows `npm test` failed.
- The real Claude Code statusline stdin is not sampled.
- Unsampled real transcript JSONL.

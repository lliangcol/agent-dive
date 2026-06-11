# Claude HUD Study Plan

## Target

- Understand the input, output, and configuration write boundaries of the Claude Code statusline plugin.
- Understand how transcript JSONL becomes Tool, Agent, Todo and MCP activity rows.
- Verify test failures and real setup behavior in Windows environment.

## Stage

1. Document reading: README, README.zh.md, setup/configure command.
2. source reading:`src/index.ts`, `src/stdin.ts`, `src/transcript.ts`, `src/config.ts`, `src/render/`.
3. Isolated verification: temporary `CLAUDE_CONFIG_DIR` writes settings and config.
4. Real verification: Install the plugin in the test profile and restart Claude Code.
5. Review: summarize the project boundaries of the statusline observation layer.

## Current record

- completed first-pass collect.
- Temporary shallow cloning of `npm ci` and `npm test` was performed and the test failed.
- The real Claude Code plugin install is not performed.

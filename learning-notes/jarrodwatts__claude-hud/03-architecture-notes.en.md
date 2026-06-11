# Architecture Notes

## Main link

Claude Code calls `statusLine.command` and passes the status JSON to HUD through stdin. The HUD then reads transcript, configuration, git, and other local status, and finally outputs a set of lines of text.

## Key components

- `commands/setup.md`: Interactive process that writes statusLine.
- `commands/configure.md`: Interactive process for writing HUD config.
- `src/index.ts`: Runtime orchestration entry.
- `src/stdin.ts`: statusline stdin parsing.
- `src/transcript.ts`: Activity analysis.
- `src/config.ts`: Configure default values, migration and verification.
- `src/render/`: Terminal output.

## Architecture judgment

Claude HUD is a single-machine local observation layer, not server-side observability. Its accuracy relies on the stdin and transcript provided by Claude Code.

# source reading notes

## Read

- `src/index.ts`
- `src/stdin.ts`
- `src/transcript.ts`
- `src/config.ts`
- `src/render/index.ts`
- `src/git.ts`
- `src/external-usage.ts`
- `.claude-plugin/plugin.json`
- `commands/setup.md`
- `commands/configure.md`

## Discover

- `MainDeps` Make the main entrance easy to test.
- `readStdin` has first byte timeout, idle timeout and 256 KB limit.
- context percent gives priority to Claude Code native `used_percentage`.
- The transcript cache is isolated by transcript path hash.
- `render/index.ts` Specially handles ANSI, OSC8 hyperlink, and CJK/emoji widths.
- setup has clear handling of Windows PowerShell performance and BOM issues.

## To be read

- `src/config-reader.ts`
- `src/extra-cmd.ts`
- `src/version.ts`
- `tests/core.test.js`
- `tests/integration.test.js`
- `tests/git.test.js`

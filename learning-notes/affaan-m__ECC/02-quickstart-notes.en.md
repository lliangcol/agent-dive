# ECC Quick Start Notes

## Current status

not run.

## Plan to verify the environment

- Node.js: To be logged
- OS: To be recorded
- Shell: to be recorded
- Target harness: Codex first, Claude Code second

## Command to be executed

```bash
npx --yes --package ecc-universal ecc --help
npx --yes --package ecc-universal ecc plan --list-profiles
npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json
npx --yes --package ecc-universal ecc consult "tdd code review security" --target codex
npx --yes --package ecc-universal ecc install --profile minimal --target codex --dry-run --json
```

Note: Do not use `npx ecc ...` directly as the verification command. There is a separate `ecc@0.0.2` package on npm, which may not be the CLI provided by `ecc-universal`.

## Record template

| Order | Whether to write to file | exit code | key output | question |
|---|---|---:|---|---|
| - | - | - | - | - |

## To be confirmed

- Whether network access to npm is required.
- Whether dry-run really does not write files.
- Whether the JSON output is sufficient to playback or review the installation plan.

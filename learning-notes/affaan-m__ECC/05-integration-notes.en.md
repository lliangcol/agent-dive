# ECC integration notes

## Current status

Not integrated.

## integration principle

- Plan first, then dry-run, and finally install.
- Prioritize target Codex minimal profile.
- Do not use full profile directly in the main user directory.
- Record file differences before and after each actual write.
- Do not extrapolate Claude hook behavior to Codex behavior.

## Path to be verified

### Codex

```bash
npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json
npx --yes --package ecc-universal ecc install --profile minimal --target codex --dry-run --json
```

### Claude Code

```text
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

### OpenCode

To be determined after reading `.opencode/README.md`.

## Rollback record

to be completed.

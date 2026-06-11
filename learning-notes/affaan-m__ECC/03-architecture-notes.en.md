# ECC Architecture Notes

## Current understanding

The core structure of ECC is:

1. Share workflow source: `skills/`, `rules/`, `hooks/`, `commands/`, `mcp-configs/`.
2. Harness adapter: `.claude-plugin/`, `.codex-plugin/`, `.opencode/`, `.cursor/`, etc.
3. Installation and management: `scripts/ecc.js`, `install-plan.js`, `install-apply.js`, manifest and install-state.
4. Access control during operation: hook-backed harness uses `hooks/hooks.json` and `scripts/hooks/`.
5. Operator observations: sessions, status, work-items, control-pane, worktree lifecycle.

## Architecture judgment

- `skills/` is the most stable multiplexing unit.
- Hook is a powerful capability, but not all harnesses support it.
- Codex paths should be verified as instruction-backed.
- The installer is the key entry point into understanding the engineering level of a project.

## to be completed

- manifest data model.
- list of target adapters.
- state DB schema.
- control pane API.
- tests coverage of architectural drift.

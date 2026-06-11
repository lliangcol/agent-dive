# ECC source reading notes

## Current status

Only the first round of file-level entry identification has been completed, and the complete call chain reading has not been completed.

## Entrance identified

- `scripts/ecc.js`
- `scripts/install-plan.js`
- `scripts/install-apply.js`
- `scripts/lib/install-manifests.js`
- `scripts/lib/install-executor.js`
- `hooks/hooks.json`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `scripts/control-pane.js`

## Next round of reading questions

1. Where is each target adapter of `SUPPORTED_INSTALL_TARGETS` registered?
2. How to define the manifest schema of profile, module and component.
3. `applyInstallPlan()` How to handle overwriting, backup, and install-state.
4. How hook profile minimal/standard/strict takes effect.
5. How the skills path and MCP servers path of the Codex plugin are read by Codex.
6. How to implement the read-only/action-enabled boundary of control pane.

## To be run for verification

- `npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json`
- `npm run catalog:check`
- `npm test`

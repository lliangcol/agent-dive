# Ruflo integration notes

## integration strategy

Priority:

1. Read-only CLI verification.
2. MCP server tool list verification.
3. Claude Code plugin lite verification.
4. Codex `.agents` verification.
5. Temporary project CLI full init verification.
6. Web UI/mcp-bridge verification.

## List to be verified

- [ ] `ruflo --version` does not trigger heavy import.
- [ ] `ruflo --help` Do not write to the file.
- [ ] `ruflo mcp start --help` for quick return.
- [ ] `mcp start` stdout holds JSON-RPC.
- [ ] Claude plugin lite does not register the full MCP server.
- [ ] CLI init write range is auditable and rollable.
- [ ] Codex can read `.agents/config.toml`.
- [ ] Codex can expose `.agents/skills/*`.

## Risk Boundary

- Do not execute `init wizard` directly in the main repository.
- Do not extrapolate Claude Code hook behavior to Codex.
- Do not treat hook output as CI gate.
- Don't enable Web UI provider/token configuration without auditing.

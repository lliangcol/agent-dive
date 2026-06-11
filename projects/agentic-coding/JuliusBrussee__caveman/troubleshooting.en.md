# Caveman problem troubleshooting record

## Problem: Don’t run full one-liner directly in the main environment

- Discovery time: 2026-06-11
- Current status: awaiting local verification
- Scope of impact: Installation and rollback

### Phenomenon

README/INSTALL.md provides shell and PowerShell one-liner and explains that multiple AI coding assistants will be detected. Direct execution on the main machine may write multiple user-level Agent configurations.

### environment

- Operating system: Windows / PowerShell and other shells
- Runtime version: To be verified
- Project version/Commit:`655b7d9c5431f822264b7732e9901c5578ac84cf`
- Key dependencies: Node 18+, target Agent CLI/configuration directory

### Reproduction steps

1. Execute `node bin/install.js --dry-run --all` in a temporary clone.
2. Record the output provider, command, and write path.
3. Compare the default behavior of real one-liner.

### Preliminary judgment

- Possible reasons: The goal of the unified installer is to "install all detectable Agents at once", which is convenient for the learning environment, but for the main environment, the write range needs to be audited first.
- Exclusions: The Caveman project itself is not installable.

### Solution

- Final processing: dry-run first, then select Agent installation only.
- Verify command: pending execution.
- Residual risk: The detection and writing logic of different providers require source code verification.

## Problem: Codex path may not automatically take effect globally

- Discovery time: 2026-06-11
- Current status: pending verification
- Scope of influence: Codex users

### Phenomenon

INSTALL.md's per-agent command for the Codex CLI is `npx skills add JuliusBrussee/caveman -a codex` and lists automatic activation as per-session `/caveman`.

### Preliminary judgment

- Possible reason: The automatic activation mechanism of Codex skill installation and Claude Code hooks is different.
- Exclusion: Claude Code's SessionStart hook behavior cannot be applied directly to Codex.

### Solution

- Test `/caveman` with a new session after installation.
- Explicitly log whether it needs to be triggered per session.
- Don't write "Codex is automatically permanently on" in the documentation unless verification is run.

## Problem: `caveman-compress` may handle sensitive memory files

- Discovery time: 2026-06-11
- Current status: To be verified by source code and operation
- Scope of influence: CLAUDE.md, AGENTS.md, project notes, preference files and other memory materials

### Phenomenon

SECURITY.md Description `caveman-compress` Read the file explicitly specified by the user, compress it and write it back to the same path, and create a `.original.md` backup. The certification path may take Anthropic SDK or Claude CLI fallback.

### Preliminary judgment

- Possible reasons: Memory files often contain project preferences, paths, internal context and even sensitive information. API/CLI data boundaries need to be clarified before compression.
- Exclusion: MIT License does not equate to runtime data security guarantees.

### Solution

- Execute on non-sensitive test files first.
- Confirm backups, file size limits, path limits, and exception rollbacks.
- Check if private memory files will be sent to external API or Claude CLI before execution.

## Issue: Output compression may impact high-risk communication clarity

- Discovery time: 2026-06-11
- Current status: pending behavioral verification
- Scope of impact: security warnings, deletion operations, migrations, production changes, legal/medical/financial high-risk answers

### Phenomenon

The main skill rule contains automatic clarity boundaries. Compression should be reduced when encountering security warnings, irreversible operation confirmations, multi-step sequences that are easy to misread, etc.

### Preliminary judgment

- Possible reasons: Fragmented expression is suitable for ordinary engineering communication, but high-risk scenarios require a complete sequence and clear conditions.
- Exclusions: Not all short replies are safe.

### Solution

- Test the destructive operation prompt to confirm whether articulation is restored automatically.
- Make it clear in team specifications: High-risk changes are not forced to use extreme compression mode.
- Additional manual review of `/caveman ultra` and `wenyan` patterns.

## Problem: MCP shrink cannot destroy protocol semantics

- Discovery time: 2026-06-11
- Current status: To be verified by source code and MCP client
- Scope of impact: MCP server metadata, tool schema, tool call response

### Phenomenon

MCP shrink README means that the proxy compresses the description field in the list response without changing the request body and tool call response.

### Preliminary judgment

- Possible reasons: Too long tool description will increase context cost, but schema, identifier, path, URL, code-like token and return value cannot be changed by mistake.

### Solution

- Compare the complete JSON before and after wrapping with a test MCP server.
- Verify that `tools/call` response byte-level or semantic-level has not been overwritten.
- Only add a wrapper to the production MCP server after confirming compatibility.

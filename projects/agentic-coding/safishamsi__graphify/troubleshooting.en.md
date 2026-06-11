# Graphify problem troubleshooting record

## Problem: `/graphify .` not applicable in PowerShell

- Discovery time: 2026-06-10
- Current status: awaiting local verification
-Affected: Windows PowerShell users

### Phenomenon

README reminds you to use `graphify .` in PowerShell, not `/graphify .`. In PowerShell, the leading `/` is easily used as a path separator or parameter prefix, causing the command interpretation to not comply with the assistant slash command semantics.

### environment

- Operating System: Windows/PowerShell
- Runtime version: To be verified
- Project version/Commit:`5504c84324fc9249eb4c9d0cca86da7140250032`
- Key dependency: `graphifyy`

### Reproduction steps

1. Try `/graphify .` in PowerShell.
2. Compare and execute `graphify .`.
3. Document error output and actual behavior.

### Preliminary judgment

- Possible reason: PowerShell command parsing and AI assistant slash command semantics are different.
- Exclusion: It is not the Graphify graph build itself that fails.

### Positioning process

| step | operate | result | in conclusion |
|---|---|---|---|
| 1 | Read README PowerShell note | README clearly recommends using `graphify .` | First execute via CLI |

### Solution

- Final processing: Prioritize using `graphify .` under Windows PowerShell.
- Verify command: pending execution.
- Residual risk: different shell and assistant built-in command semantics still need to be documented separately.

## Problem: PyPI package name is inconsistent with CLI command name

- Discovery time: 2026-06-10
- Current status: awaiting local verification
- Scope of Impact: Installation and PATH troubleshooting

### Phenomenon

The README states that the official PyPI package is `graphifyy`, but the CLI command is `graphify`. If you install other `graphify*` packages by mistake, you may get an error project or the command may not be available.

### Preliminary judgment

- Possible reasons: The package name and command name are different.
- Exclusions: Not that the GitHub repository does not exist.

### Solution

- Use `uv tool install graphifyy` or `pipx install graphifyy`.
- After installation, execute `graphify --help` or `graphify --version` to confirm the source of the command.
- Avoid installing other similar packages with the same name without confirming the source.

## Problem: The data boundaries of semantic extraction of non-code materials in private warehouses are unclear.

- Discovery time: 2026-06-10
- Current status: pending source code and configuration verification
- Scope of influence: private code, internal documents, pictures, videos, transcribed content

### Phenomenon

Graphify not only has local static parsing, but also supports backend extras such as OpenAI, Anthropic, Gemini, Azure, Bedrock, Ollama, etc. The Privacy description of the README states that code files are processed locally through Tree-sitter, videos/audio are transcribed locally, and docs, PDFs, and images will be sent to the user-configured AI assistant/backend. Before using a private repository, you need to confirm whether non-code materials are allowed to be sent out.

### Preliminary judgment

- Possible reasons: semantic extraction and static parsing are different stages, and the data outgoing boundary depends on the backend and input type.
- Exclusion: Runtime data security cannot be determined based on the MIT License alone.

### Solution

- Read `SECURITY.md` and `docs/how-it-works.md` first.
- Use a public warehouse for dry run.
- Private repositories first disable or restrict non-code semantic extraction such as docs, PDFs, pictures, etc. until the outgoing content is confirmed.
- Document backends, environment variables, input scopes, and build results.

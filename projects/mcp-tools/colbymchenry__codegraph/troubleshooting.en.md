# CodeGraph problem troubleshooting record

## Problem: The `codegraph` command cannot be found after installation

- Discovery time: 2026-06-10
- Current status: Not verified
- Scope of impact: First time installation and Windows PowerShell usage

### Phenomenon

The README reminds that the installer will put `codegraph` in PATH, but will not change the current shell, so the current terminal may still not be able to parse the command after installation.

### Solution

- Final processing: Re-open the terminal and then run `codegraph --version`.
- Verification command: `codegraph --version`
- Residual risk: Enterprise endpoint policies may prevent PATH modification.

## Problem: MCP tools reports that the project is not initialized

- Discovery time: 2026-06-10
- Current status: Not verified
- Scope of influence: Agent is connected but the target warehouse does not `.codegraph/`

### Phenomenon

`src/mcp/server-instructions.ts` explicitly takes the absence of `.codegraph/` as a limitation: `codegraph init -i` needs to be run when the project is not initialized.

### Solution

```bash
cd your-project
codegraph init -i
codegraph status
```

Residual risk: If the warehouse is large, the first index may take a long time.

## Problem: Node version is incompatible

- Discovery time: 2026-06-10
- Current status: Not verified
- Scope of influence: npm installation, development source code, SDK embedding

### Phenomenon

`package.json` marks Node `>=20.0.0 <25.0.0`; `src/bin/codegraph.ts` has a hard check on Node 25+ and older versions; Library Usage of README states that the embedded API requires Node 22.5+ `node:sqlite`.

### Solution

- CLI users prefer the self-contained installer provided in the README.
- npm/source development users check Node version.

```bash
node --version
npm test
```

Residual risk: Different installation paths have different runtime requirements and must be verified according to the actual path.

## Problem: Index results are expired or watcher is not working

- Discovery time: 2026-06-10
- Current status: Not verified
- Scope of influence: query immediately after editing, sandbox, network file system

### Phenomenon

README description MCP server uses watcher and debounce to automatically synchronize; when watcher is unavailable in `src/mcp/engine.ts`, it will prompt to run `codegraph sync`. The tool results may appear with a pending sync / staleness banner.

### Solution

```bash
codegraph status
codegraph sync
```

If the Agent tool results indicate that a file is pending re-index, use raw reading for the file or wait for automatic sync and try again.

## Problem: Static analysis cannot prove runtime behavior

- Discovery time: 2026-06-10
- Current status: Objective limitations
- Scope of influence: dynamic languages, reflection, runtime routing, framework magic, cross-language bridging

### Preliminary judgment

CodeGraph's reference resolution is static best-effort. Both the README and source code emphasize that it complements compilers, tests, and linters, not replaces real verification.

### Solution

- Use CodeGraph to locate influence surfaces.
- Use project native testing, type checking, and integration testing to verify behavior.
- Keep the "to be run for verification" annotation on dynamic call chains.

## Problem: The documentation and source code are not completely consistent

- Discovery time: 2026-06-10
- Current status: Recorded
- Scope of impact: Understand whether the installer writes instructions files

### Phenomenon

`site/src/content/docs/reference/mcp-server.md` still says that the installer will write guidance into the agent instructions file; but the current README and `src/mcp/server-instructions.ts`, `src/installer/targets/codex.ts`, `src/installer/targets/claude.ts` all show that tool guidance is provided by MCP initialize response, and clean up the old instructions block.

### Solution

This collect is based on the current status of the source code and README; if you want to submit an upstream issue later, you can point out that the docs reference page may need to be synchronized.

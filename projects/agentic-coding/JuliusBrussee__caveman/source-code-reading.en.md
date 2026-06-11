# Caveman source reading record

## 1. Reading objectives

- The question to be understood in this round: How Caveman distributes a set of output compression rules to multiple AI coding assistants and takes effect in the Claude Code / MCP / memory compression scenario.
- Related functions: unified installer, skill rules, Claude Code hooks, statusline, MCP shrink, memory file compression, cavecrew sub-Agent.
- Expected output: Confirm core module boundaries, critical call chains, write ranges, uninstall paths, test coverage and security boundaries.

## 2. Source code entry

| Entrance | path | effect | in accordance with |
|---|---|---|---|
| unified installer | `bin/install.js` | `caveman` package bin entry, install/uninstall/dry-run/provider matrix | `package.json`、INSTALL.md |
| Main skill | `skills/caveman/SKILL.md` | Output compression behavior rules and strength patterns | skill file |
| Claude Code hook | `src/hooks/caveman-activate.js` | SessionStart automatically activated | hooks README, pending source code verification |
| Mode tracker | `src/hooks/caveman-mode-tracker.js` | UserPromptSubmit parsing mode switch | hooks README, pending source code verification |
| Statusline | `src/hooks/caveman-statusline.ps1` / `.sh` | Show current mode and savings statistics | hooks README, to be run for verification |
| MCP shrink | `src/mcp-servers/caveman-shrink/index.js` | MCP stdio proxy entrance | MCP shrink README, pending source code verification |
| Memory compress | `skills/caveman-compress/scripts/cli.py` | Memory file compression CLI thread | tree, SECURITY.md, pending source code verification |
| OpenCode plugin | `src/plugins/opencode/plugin.js` | OpenCode native plug-in | CLAUDE.md, pending source code verification |
| Tests | `tests/` | Installer, hooks, compress, MCP shrink and other tests | GitHub tree |

## 3. Module map

| module | path | Responsibilities | Dependencies |
|---|---|---|---|
| installer | `bin/install.js`、`bin/lib/settings.js`、`bin/lib/openclaw.js` | Parameter parsing, provider detection, configuration writing, dry-run, uninstall | Call system commands, read and write agent configuration, pending source code verification |
| Skill source | `skills/` | Behavior rules, command descriptions, sub-skills | Distributed by plugins and consumed by `npx skills add` |
| Plug-in distribution | `.claude-plugin/`、`plugins/caveman/` | Claude Code plugin manifest and image file | CLAUDE.md calls partial by CI sync |
| Command stubs | `commands/` | Codex / Gemini slash command template | To be confirmed which installation paths are read |
| Claude hooks | `src/hooks/` | activation, mode tracking, status bar, stats | Write the flag file in the configuration directory and wait for source code confirmation |
| MCP proxy | `src/mcp-servers/caveman-shrink/` | Pack the upstream MCP server and compress the metadata description field | JSON-RPC stdio, to be confirmed by source code |
| OpenCode plugin | `src/plugins/opencode/` | OpenCode session hook and slash commands | pending source code verification |
| Benchmarks / evals | `benchmarks/`、`evals/` | token reduction measurement and control experiments | To be reproduced |
| Tests | `tests/` | Node/Python testing | To be executed |

## 4. Recommended reading order

1. `README.md`: Confirm product positioning, support platform and function matrix.
2. `INSTALL.md`: Confirm the installation entry, dry-run, per-agent commands and uninstall path.
3. `CLAUDE.md`: Understand the source code directory, single source of truth and synchronization rules defined by the maintainer.
4. `package.json`: Confirm package bin mapping and test script.
5. `bin/install.js`: Enter provider matrix, write scope and uninstall from parameter parsing.
6. `skills/caveman/SKILL.md`: Confirm compression rules, trigger semantics and security degradation boundaries.
7. `src/hooks/README.md`, then read `src/hooks/*.js`, `.ps1`, `.sh`.
8. `src/mcp-servers/caveman-shrink/README.md`, then read `index.js` and `compress.js`.
9. `skills/caveman-compress/SECURITY.md`, read `scripts/*.py` again.
10. `tests/`, `benchmarks/`, `evals/`: Confirm behavioral testing and income measurement caliber.

## 5. Key call chain

### Call chain 1: Install all detected Agents

- Trigger condition: execute one-liner or `node bin/install.js --all`.
- Starting point: `bin/install.js`, pending source code confirmation.
- Key steps: parse flags -> create provider list -> detect local agent -> execute per-agent installation command -> optionally write hooks / statusline / MCP shrink / rule files.
- Endpoint: The skill/plugin/rule configurations of multiple Agents are written.
- Input: CLI flags, environment variables, agent configuration path.
- Output: configuration files, hook files, plug-in installation results or dry-run logs.
- Error handling: pending source code confirmation, including insufficient permissions, merging existing configurations, missing commands, repeated installation and uninstallation failures.
- Based on: INSTALL.md, CLAUDE.md.

### Call chain 2: Claude Code mode activation

- Trigger condition: Claude Code session starts or user submits prompt.
- Starting point: SessionStart/UserPromptSubmit hooks, pending source code confirmation.
- Key steps: write or read active flag -> inject rule or per-turn reminder -> statusline read flag -> stats write suffix.
- End point: Claude Code reply is output according to the current caveman mode, and the status bar displays the mode.
- Input: user prompt, hook environment variable, configuration directory.
- Output: hidden context, flag file, statusline text.
- Error handling: To be confirmed by the source code, including symlink security, status file corruption, and Windows PowerShell execution policy.
-Based on: hooks README.

### Call chain 3: MCP metadata compression

- Trigger condition: MCP client starts `caveman-shrink <upstream-command> [...args]`.
- Starting point: `src/mcp-servers/caveman-shrink/index.js`, pending source code confirmation.
- Key steps: spawn upstream server -> transparently transmit JSON-RPC -> compress prose field for list response -> retain code / URL / path / identifier.
- End point: client receives shorter tool / prompt / resource metadata.
- Input: MCP JSON-RPC messages, environment variable `CAVEMAN_SHRINK_FIELDS`.
- Output: compressed metadata responses.
- Error handling: pending source code confirmation, including upstream exit, invalid JSON, stderr forwarding, and field whitelist.
-Based on: MCP shrink README.

### Call chain 4: Memory file compression

- Trigger condition: The user specifies a memory file for compression.
- Starting point: `skills/caveman-compress/scripts/cli.py` or skill call chain, pending source code confirmation.
- Key steps: path and size verification -> back up the original file -> call Anthropic SDK or Claude CLI -> verify the compression result -> write back the file.
- Endpoint: The original file is compressed and `.original.md` the backup is retained.
- Input: user specified file, API key or Claude CLI auth.
- Output: compressed markdown and backup files.
- Error handling: SECURITY.md mentions fixed argv, stdin transfer and file size limit; the specific exception path needs to be verified by the source code.
-Based on: SECURITY.md, tree.

## 6. Read notes

- Important discovery: The engineering value of Caveman is not only in the "short reply prompt word", but also in the combination of cross-agent distribution, installation write boundary, hook state management, MCP metadata compression and memory file compression.
- Uncertainty: The unified installer's accuracy in detecting 30+ Agents, failure rollback and uninstall idempotence require source code and dry-run verification.
- To be run and verified: `node bin/install.js --dry-run --all`, `node bin/install.js --list`, Codex single-path installation, MCP shrink packaging a test server, Node / Python test.

## To-do check items

- [ ] Find the provider matrix of `bin/install.js`.
- [ ] Confirm that dry-run is completely write-free.
- [ ] Confirm `--only codex` / Codex skill installation path.
- [ ] Confirm `--uninstall`'s rollback range for each platform.
- [ ] Confirm which files Claude Code hooks write and read.
- [ ] Confirm that statusline does not overwrite existing custom configuration logic.
- [ ] Confirm that `caveman-shrink` does not rewrite the tool call response.
- [ ] Confirm path, size, backup and API/CLI fallback boundaries for `caveman-compress`.
- [ ] Run `npm test` or the actual test entry of the warehouse.
- [ ] Reproduce at least one set of benchmark / eval to confirm the token statistical caliber.

# Caveman project deep dive

## 1. Basic project information

- Project name: Caveman
- Project ID: `JuliusBrussee__caveman`
- GitHub：https://github.com/JuliusBrussee/caveman
- Project homepage: https://getcaveman.dev/（GitHub API homepage / README link)
- Category: `agentic-coding`
-Collect level: Level B standard collect
- Current status: `analyzing`
- Main language: JavaScript
- License：MIT
- Analysis date: 2026-06-11
- Analysis version/Commit:`655b7d9c5431f822264b7732e9901c5578ac84cf`
- Default branch: `main`
- Whether to run verification: No
- Analysis basis: GitHub API, README, INSTALL.md, CLAUDE.md, `src/hooks/README.md`, `src/mcp-servers/caveman-shrink/README.md`, `skills/caveman-compress/SECURITY.md`, GitHub tree, `package.json`, `git ls-remote --symref`; no local installation, testing or source code call chain verification has been done.

## 2. Positioning in one sentence

Caveman is a reply compression skill/plugin across AI coding assistants that allows agents to maintain technical information density with fewer output tokens through prompt word rules, installers, and auxiliary hooks.

## 3. Problems solved by the project

AI coding assistants often output a lot of pleasantries, repetitive foreshadowing, and low information density text when explaining, reviewing, fixing suggestions, and troubleshooting code. For scenarios such as long sessions, repeated reviews, CI debugging, and document organization, this will increase reading costs and output token costs.

The learning value of Caveman lies in:

- Output style constraints: Write "speak less but never lose technical information" as a reusable skill rule.
- Cross-Agent distribution: The same set of behaviors is distributed through Claude Code plugin, Codex skill, Gemini extension, OpenCode plugin and other agent rule files.
- Runtime activation: Claude Code hooks maintain mode state during SessionStart and UserPromptSubmit phases.
- Cost observations: `caveman-stats` and statusline are used to show savings estimates, but statistical caliber still needs to be verified.
- Context compression: `caveman-compress` is for memory file compression; `caveman-shrink` is for MCP tool/prompt/resource description compression.

Basis: README, INSTALL.md, hooks README and SECURITY.md; specific implementation details are subject to source code verification.

## 4. Project main line

Based on README / INSTALL.md, the typical main line of use is as follows:

1. The user calls the unified installer through shell / PowerShell one-liner or `npx`.
2. `bin/install.js` Detect or select the target Agent according to parameters, and call the corresponding installation path.
3. For Claude Code, install plugin/skills and configure hooks, statusline and optional MCP shrink.
4. For Codex / Cursor / Windsurf / Cline, etc., use `npx skills add` or rule file to write the corresponding configuration.
5. The user inputs `/caveman` or natural language trigger in the session, and the Agent compresses the output according to skill rules.
6. Optional commands handle commit message, review comment, stats, memory file compression, and MCP description compression.

Unverified: The above process has not yet been executed on the local machine. The specific file writing, idempotent behavior, uninstallation behavior and error handling need to be confirmed by execution.

## 5. Quick Start

- Environment requirements: README/INSTALL.md mentions that the unified installer requires Node 18+.
- Windows installation entrance: `irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex`。
- macOS / Linux / WSL installation entry: `curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash`。
- Dry-run: INSTALL.md provides `--dry-run` path to preview writes and commands first.
- Codex single-agent installation: INSTALL.md lists `npx skills add JuliusBrussee/caveman -a codex`.
- Trigger method: README describes `/caveman`, and provides `lite`, `full`, `ultra`, `wenyan` and other modes.

These commands are not executed by the current repository. Since the installation may write user-level Agent configuration, this collect only records the official path and boundaries to be verified.

## 6. Core architecture

According to README, INSTALL.md, CLAUDE.md, GitHub tree and package.json, the currently identifiable module clues are:

| module | effect | in accordance with | Verification status |
|---|---|---|---|
| `bin/install.js` | Unified installer, detects or selects the target Agent, and performs installation/uninstallation/dry-run | INSTALL.md、CLAUDE.md、package.json | pending source code verification |
| `install.sh` / `install.ps1` | Platform shim, transfer to Node installer | GitHub tree、INSTALL.md | pending verification |
| `skills/caveman/` | Master compression behavior rules including multiple strengths and boundaries | skill file | Summary of read rules, pending installation verification |
| `skills/caveman-compress/` | Zip memory file containing Python scripts and security instructions | GitHub tree、SECURITY.md | Awaiting source code/operation verification |
| `skills/caveman-stats/` | Statistical token usage and savings display | README、tree | pending source code verification |
| `skills/cavecrew/` / `agents/` | caveman style subagent and delegation guide | README、tree、CLAUDE.md | Awaiting source code/behavior verification |
| `src/hooks/` | Claude Code SessionStart, UserPromptSubmit, statusline and other hooks | hooks README、CLAUDE.md | Awaiting source code/operation verification |
| `src/mcp-servers/caveman-shrink/` | MCP stdio proxy, compress tool / prompt / resource description field | MCP README、tree | Awaiting source code/operation verification |
| `plugins/caveman/` | Claude Code plugin distribution directory | CLAUDE.md、tree | To be verified by synchronization process |
| `benchmarks/` / `evals/` | token reduction benchmark and three-way evaluation | README、tree | To be reproduced |
| `tests/` | Node and Python testing | GitHub tree、package.json | To be executed |

See `assets/diagrams/architecture.mmd`, `install-flow.mmd`, `hook-flow.mmd` and `mcp-shrink-flow.mmd` for draft diagrams.

## 7. Core Principles

### Output compression skill

`skills/caveman/SKILL.md` Break down the compression behavior into intensity, rules, triggering methods and safety boundaries. The key idea is not to reduce reasoning, but to reduce low information density text in the final reply. It requires keeping technical terms, code, paths, error messages, and API names accurate while removing small talk, hedging, and repetitive explanations.

Basis: `skills/caveman/SKILL.md`; to be verified by real session.

### Unified installer

INSTALL.md means that the unified installer is responsible for automatically detecting the installed Agent and taking the plugin, extension, skill, rule file or hook paths according to different platforms. `package.json` exposes `caveman` bin pointing to `bin/install.js`, indicating that the Node installer is the main entrance.

Based on: INSTALL.md, package.json, CLAUDE.md; to be verified by source code and dry-run.

### Claude Code hooks and status files

hooks README shows Claude Code path using SessionStart hook, UserPromptSubmit hook and statusline script. The core bridge object is the mode flag file in the configuration directory; the hook writes or deletes the mode, and the statusline displays the current mode after reading it.

Basis: `src/hooks/README.md`; to be installed and verified on this machine.

### Memory file compression

`caveman-compress` Generate a compressed version of the user-specified memory file and keep a `.original.md` backup. SECURITY.md states that it may use the Anthropic SDK or Claude CLI fallback, limits large files, and states that it will not read paths not specified by the user.

Basis: `skills/caveman-compress/SECURITY.md`; To be verified by source code and operation.

### MCP description compression

`caveman-shrink` is stdio proxy, located between the MCP client and the upstream server. It conservatively compresses the description fields in metadata responses such as `tools/list`, `prompts/list`, `resources/list`, without rewriting the tool call request body or tool call response.

Basis: `src/mcp-servers/caveman-shrink/README.md`; pending source code and MCP client verification.

## 8. Source code structure

The main structure displayed by GitHub tree:

- `bin/`: Unify the installer and configuration writing auxiliary logic.
- `skills/`: The source files of each skill, including `caveman`, `caveman-compress`, `caveman-stats`, `caveman-commit`, `caveman-review`, `cavecrew`.
- `agents/`: cavecrew sub-Agent definition.
- `commands/`：Codex / Gemini command stubs。
- `src/hooks/`: Claude Code hooks, statusline script and hook installer.
- `src/mcp-servers/caveman-shrink/`：MCP shrink middleware。
- `src/plugins/opencode/`：OpenCode plugin。
- `plugins/caveman/`: Claude Code plugin distribution directory.
- `benchmarks/`: token benchmark prompts and runner.
- `evals/`: Three-way evaluation harness and result snapshot.
- `tests/`: installer, hooks, compress safety, MCP shrink and other tests.

Waiting for source code confirmation:

- Provider detection, dry-run, write scope and uninstall behavior for `bin/install.js`.
- Input, output and safety boundaries of `src/hooks/caveman-activate.js` / `caveman-mode-tracker.js`.
- JSON-RPC processing and field compression rules for `src/mcp-servers/caveman-shrink/index.js` / `compress.js`.
- File path verification, backup, API/CLI fallback and error handling for `skills/caveman-compress/scripts/`.

## 9. Key call chain

### Call chain 1: unified installer

- Trigger condition: user runs one-liner, `npx -y github:JuliusBrussee/caveman` or local `node bin/install.js`.
- Starting point: `bin/install.js`, pending source code confirmation.
- Key steps: Parse parameters -> Detect provider -> Select per-agent install command -> Optional installation hooks / statusline / MCP shrink / rule files -> Output results.
- Endpoint: The target Agent's skill/plugin/rule/hook configuration is written, or dry-run only prints the plan.
-Based on: INSTALL.md, package.json.
-Status: pending source code and operation verification.

### Call chain 2: Claude Code automatically activated

- Trigger condition: A new session of Claude Code is started, plugin or standalone hooks are installed.
- Starting point: SessionStart hook, pending source code confirmation.
- Key steps: write active mode flag -> inject compression rule context -> statusline read flag -> UserPromptSubmit hook parses `/caveman` or closes statement when user prompts.
- Endpoint: Subsequent replies are compressed and output according to the current mode.
-Based on: hooks README.
- Status: pending verification.

### Call chain 3: MCP shrink proxy

- Trigger condition: MCP client calls wrapper to start the upstream server.
- Starting point: `src/mcp-servers/caveman-shrink/index.js`, pending source code confirmation.
- Key steps: start upstream command -> forward JSON-RPC -> intercept list type response -> compress specified prose field -> transparently transmit request and tool call response.
- End point: Agent reads shorter MCP metadata.
-Based on: MCP shrink README.
-Status: pending source code and operation verification.

### Call chain 4: Memory file compression

- Trigger condition: The user executes `/caveman-compress <file>` or the corresponding script entry.
- Starting point: `skills/caveman-compress/scripts/cli.py` or skill execution path, pending source code confirmation.
- Key steps: Verify user-specified path and size -> Read file -> Call Anthropic SDK or Claude CLI -> Write back compression result -> Save `.original.md` backup.
- End point: the memory file becomes shorter and a backup of the original file exists.
-Based on: README, SECURITY.md, GitHub tree.
-Status: pending source code and operation verification.

## 10. integration method

It is suitable to do three kinds of integration experiments first:

1. Dry-run unified installer: Execute `node bin/install.js --dry-run --all` and `node bin/install.js --list` in temporary clones to confirm the provider matrix and write plan.
2. Codex single-path installation: After explicitly agreeing to write the user-level Codex skill, execute `npx skills add JuliusBrussee/caveman -a codex` to confirm the actual writing location and uninstallable method.
3. MCP shrink wrapper: Use an MCP server without sensitive information to do the wrapper test, compare the length of the list response field, and confirm that the tool call response has not been rewritten.

It is currently not recommended to execute the full one-liner directly in the main working environment; it is more stable to dry-run and verify in the isolation environment first.

## 11. Problemshooting

Priority troubleshooting direction:

- Installation write range: one-liner may detect multiple Agents and write user-level configuration; use `--dry-run` first.
- Node version: README / INSTALL.md requires Node 18+; Windows environment needs to confirm that `node` and `npx` are available.
- PowerShell execution policy: `install.ps1` or hook statusline scripts may be affected by execution policy.
- Codex activation method: INSTALL.md shows that Codex requires per-session `/caveman`. Do not mistakenly think that it will be automatically activated.
- Statistical caliber: `caveman-stats` and benchmark conclusions need to distinguish between real API tokens, estimates, historical session logs and current sessions.
- Memory compression risk: Confirm the backup, path, file size and API/CLI fallback before performing compression on important memory files.

## 12. Objective evaluation

### advantage

- For the real AI coding assistant workflow, not just the prompt word fragments in the README.
- Also covers skill rules, plugin distribution, installer, hooks, status bar, MCP proxy, benchmark and tests.
- It has direct learning value for Agent output cost, reading efficiency and context governance.
- License is MIT, suitable for learning and secondary research.

### shortcoming

- Technical value is easily obscured by meme-style packaging. When analyzing, return to installer, hooks, MCP proxy and security boundaries.
- The installation path covers a large number of Agents, and the write range and idempotence must be verified through dry-run/temporary environment.
- Output compression does not mean correct conclusions. Complex safety reminders, irreversible operations and multi-step processes still need to be expressed clearly.
- Benchmark and stats need to be reproducible and cannot be directly used as general benefits for all tasks.

### Applicable scenarios

- Learn AI coding assistant skill/plugin ecology and multi-platform distribution.
- Research output token compression, prompt word style constraints and information density.
- Research Claude Code hooks, statusline and session state mechanisms.
- Research MCP metadata compression and Agent tool directory token costs.

### not applicable scenario

- When serious, complete, explanatory documentation for non-technical users is required, it should not be reduced to fragmented expressions by default.
- Compression rules must give way to clarity when high-risk communications such as legal, medical, safety, confirmation of irreversible operations, etc. are required.
- It is not suitable to directly run the full installer when the write range is not audited.
- Not suitable as evidence that the model is smarter; it mainly changes the output layer expression.

## 13. Learning Todo List

See [learning-todo-list.md](learning-todo-list.en.md). It is recommended to complete Level 1 to Level 2 before entering source code level verification and isolation environment installation testing.

## 14. Summary

Caveman is worth collecting as a Level B project in the direction of `agentic-coding`. It connects prompt word compression, Agent skill distribution, Claude Code hooks, MCP metadata compression and token cost observation, and is suitable as a learning example of "how AI coding assistants can reduce output redundancy while maintaining technical information."

The next step should be to perform dry-run installation verification and source code to confirm the true boundaries of installer, hooks, MCP shrink and memory compression.

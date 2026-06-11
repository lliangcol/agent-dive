#Caveman integration guide

## 1. integration goal

- Target systems: Native AI Coding Assistant environment and optional MCP client.
- Target capability: Make Agent output shorter and less pleasantries while retaining technical facts, code, paths, and error messages.
- Integration method: unified installer, per-agent skill install, Claude Code hooks, optional MCP shrink, optional memory compression.
- Constraints: The current document has not been verified for local operation. All installation commands must first verify the writing range in an isolation environment or dry-run.

## 2. Preconditions

- Running environment: Node 18+; Windows requires PowerShell 5.1+ or available `node` / `npx`.
- Dependencies: The unified installer is based on Node; `caveman-compress` contains Python scripts; different Agent installation paths may require that the corresponding CLI has been installed and logged in.
- Permission requirements: The installation may write user-level configuration, agent plug-in directory, hook file, statusline configuration or current warehouse rule files.
- Safety premise: Before executing on the main environment, confirm the dry-run output, uninstall command and backup strategy.

## 3. Minimum integration path

### Path A: Only preview the installation plan

1. Clone or download the Caveman repository to a temporary directory.
2. Execution: `node bin/install.js --list`.
3. Execution: `node bin/install.js --dry-run --all`.
4. Record which Agents will be detected, which commands will be executed, and which paths will be written.
5. Verify that the dry-run does not actually write.

Status: pending verification.

### Path B: Codex single Agent integration

1. Confirm the current Codex skill installation location and existing configuration.
2. Execute the official per-agent command: `npx skills add JuliusBrussee/caveman -a codex`.
3. Open a new Codex session and enter `/caveman` or request a short reply.
4. Record the normal output and caveman output for the same technical problem, and compare the completeness of the information.
5. Find the uninstall or rollback method and record it.

Status: pending verification.

### Path C: Claude Code integration

1. Perform a dry-run in the temporary Claude configuration directory or test machine.
2. Execute `node bin/install.js --only claude --dry-run`.
3. Confirm the write plan for plugin, hooks, statusline and MCP shrink.
4. Perform a real installation in a test environment.
5. Open a new session and check automatic activation, `/caveman lite | full | ultra`, shutdown command and statusline behavior.

Status: pending verification.

### Path D: MCP shrink integration

1. Prepare an MCP server without sensitive information.
2. Use `caveman-shrink` to wrap the server.
3. Compare the field lengths of `tools/list`, `prompts/list`, and `resources/list` before and after packaging.
4. Call a tool and confirm that the request body and tool response have not been overwritten.
5. Log the `CAVEMAN_SHRINK_FIELDS` configuration and debug output.

Status: pending source code and runtime verification.

## 4. Interface and data flow

| enter | processing module | output | Remark |
|---|---|---|---|
| one-liner / `npx` / local node command | `bin/install.js` | agent plugin / skill / hook / rule writes plans or results | Need to dry-run first |
| `/caveman` or natural language trigger | skill / hooks | Compressed Agent reply | Does not change model inference, only changes output constraints |
| Claude Code session events | `src/hooks/` | active flag, hidden context, statusline text | Waiting for local verification |
| MCP list response | `caveman-shrink` | Shorter metadata description | tool call response should not be changed |
| memory markdown file | `caveman-compress` | Compressed files and `.original.md` backups | API/CLI fallback and sensitive data boundaries need to be confirmed |
| benchmark prompts | `benchmarks/` / `evals/` | token reduction measurement | Statistical caliber needs to be reproduced |

## 5. Java/Spring Boot integration concerns

Caveman does not embed the Java/Spring Boot runtime. It is more suitable as an output specification and tool chain configuration at the development assistant level.

- Bean life cycle: Spring Bean is not involved.
- Configuration management: Do not write Agent user-level configuration, API key or local path to the business warehouse.
- Permissions and auditing: The installer's writing of user configurations needs to be recorded independently and cannot be mixed with business code changes.
- Logs and link tracing: Keep commands and versions for installation, uninstallation, stats, compress, and MCP shrink runs.
- Team collaboration: If you add rule files to the team repository, they should be included as part of an explicit code review, not as a by-product of a personal one-liner.

## 6. Integration risks

- Write scope risk: `--all` or one-liner may overwrite the user-level configuration of multiple Agents.
- Risk of platform differences: The install path and script execution behavior of Windows PowerShell, Git Bash, WSL, macOS/Linux are different.
- Semantic compression risk: output that is too short may omit necessary context, especially safety, compliance, irreversible operations, and multi-step execution sequences.
- Risk of statistical misreading: README benchmark, stats and statusline are caliber indicators and cannot be directly equated to the cost and benefit of all workflows.
- Sensitive data risk: `caveman-compress` will process user-specified files and may send content through SDK or Claude CLI; boundaries must be confirmed first for private memory files.
- MCP compatibility risk: proxy needs to keep JSON-RPC semantics unchanged; field compression should not destroy the necessary precision of schema, identifier, or tool descriptions.

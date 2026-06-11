# Claude HUD integration guide

## 1. integration goal

- Target system: local Claude Code environment.
- Target capabilities: View project, model, context, subscription usage, git, tool, Skill, MCP, Agent, Todo and session status in real time through statusline.
- Integration method: Claude Code plugin marketplace, `/claude-hud:setup`, `/claude-hud:configure`, user-level `statusLine.command`.
- Constraints: The current document is not installed in the real Claude Code environment; all operations of writing user-level configurations need to be backed up first.

## 2. Preconditions

- Claude Code v1.0.80+。
- Windows: Node.js 18+, and the current shell can find `node`.
- macOS/Linux: Node.js 18+ or Bun.
- Claude Code plugin marketplace feature available.
- If you already have `statusLine`, first confirm which tool it came from and keep the recovery path.

## 3. Minimum integration path

### Path A: Only do source code and test verification

1. Shallow clone the repository in the temporary directory.
2. Execute `npm ci`.
3. Execute `npm run build`.
4. Selectively perform non-environmentally sensitive testing.
5. Log Node version, OS, shell, and failures.

Results of this round: `npm ci` succeeded, `npm test` failed in Windows environment.

### Path B: Isolated Claude configuration verification

1. Create temporary `CLAUDE_CONFIG_DIR`.
2. Prepare the minimum `settings.json` in this directory.
3. Generate statusLine command according to the platform branch of `commands/setup.md`.
4. Confirm that setup creates backups and does not overwrite unknown statuslines.
5. Check whether the written JSON has no BOM and can be read by Claude Code.

Status: pending verification.

### Path C: Real Claude Code installation

1. Run `/plugin marketplace add jarrodwatts/claude-hud` in Claude Code.
2. Run `/plugin install claude-hud`.
3. Run `/reload-plugins`.
4. Run `/claude-hud:setup`.
5. Follow the prompts to back up or replace the existing statusline.
6. Completely restart Claude Code.
7. Verify that the HUD appears below the input area.

Status: pending verification.

### Path D: Functional Verification

1. Execute a file read and grep to make the tools line contain content.
2. Execute a multi-step task with Todo and verify the todo progress.
3. If subagent is enabled, observe the Agent line.
4. Configure an MCP server and observe the MCP activity line.
5. Execute `/claude-hud:configure` to enable Chinese labels, tools, agents, todos, and session info.

Status: pending verification.

## 4. Interface and data flow

| enter | processing module | output | Remark |
|---|---|---|---|
| Claude Code statusline stdin JSON | `src/stdin.ts`、`src/index.ts` | model/context/rate limit/cwd and other status | The real schema requires sampling and verification |
| transcript JSONL | `src/transcript.ts` | tools、skills、MCP、agents、todos、session tokens | Read local transcript path |
| HUD config | `src/config.ts` | layout, color, threshold, display switches | `plugins/claude-hud/config.json` |
| git repo cwd | `src/git.ts` | branch、dirty、ahead/behind、file stats | 1-2 seconds timeout at most |
| Claude config files | `src/config-reader.ts` | CLAUDE.md / rules / MCP / hooks counts | Current Windows test failure related modules |
| render context | `src/render/` | stdout HUD lines | Presented by Claude Code statusline |

## 5. Java/Spring Boot integration concerns

Claude HUD is not embedded in the Java/Spring Boot runtime and should not be written to the production configuration of the business repository.

- Bean life cycle: Spring Bean is not involved.
- Configuration management: HUD configuration is user-level Claude Code configuration and does not belong to business application configuration.
- Permissions and auditing: setup will modify user level `settings.json` and should be audited as a change to native development tools.
- Team collaboration: Teams can recommend in documentation, but should not be forced to submit individual `~/.claude` configurations.
- CI: The upstream Node test suite can be used as a learning example, but currently Windows failures need to be located first and then included in the team inspection.

## 6. Integration risks

- Overwriting risk: setup may replace existing `statusLine.command`.
- Platform risk: Windows PowerShell, Git Bash/MSYS2, and WSL have different command formats.
- Version drift risk: Claude Code statusline stdin and transcript JSONL schema may change.
- Usability risk: subscriber usage depends on `rate_limits` in Claude Code stdin, API-key-only users will not have the same data.
- Performance risk: statusline is refreshed frequently, and the git/config/transcript/cache logic needs to be avoided from being too slow.
- Test risk: The current Windows temporary environment `npm test` failed.

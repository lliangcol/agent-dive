#RTK integration guide

## 1. integration goal

- Target system: AI coding assistant workflow.
- Target capability: Let common shell command output be RTK compressed before entering the LLM context.
- Integration method: First manually call the `rtk` command to verify, and then select hook / plugin / prompt guidance according to the target Agent.
- Constraints: No installation is performed in this round, only recommended paths and risk boundaries are recorded.

## 2. Preconditions

- Running environment: Rust binary or release binary is available; Windows native and WSL support are quite different.
- Dependencies: The installation methods include Homebrew, GitHub install script, GitHub Cargo install or release zip.
- Model or service configuration: RTK itself does not require a model API key.
- Permission requirements: `rtk init` may write user-level Agent configuration, and you need to confirm the writing path and backup first.

## 3. Minimum integration path

It is recommended to perform isolation verification in the following order:

1. Install or build RTK in a staging environment.
2. Execute `rtk --version` to confirm that it is not the Rust Type Kit with the same name as crates.io.
3. Execute `rtk rewrite "git status"` and confirm that the registry can return `rtk git status`.
4. Execute `git status` and `rtk git status` in a non-sensitive test repository and compare the output.
5. Construct the failed command, set `RTK_TEE_DIR` to the temporary directory, and verify the full-output hint.
6. Execute `rtk gain` to confirm whether tracking is recorded.
7. Select only one target Agent for installation verification and do not directly install all paths globally.

## 4. Interface and data flow

| enter | processing module | output | Remark |
|---|---|---|---|
| `git status` | Agent hook -> `rtk rewrite` | `rtk git status` | Transparent hook depends on specific Agent |
| `rtk git diff` | `src/cmds/git/git.rs` | compact diff + stat | Raw diff may be truncated |
| `rtk pytest` | `src/cmds/python/pytest_cmd.rs` | failures-focused output | Need to test fixture verification |
| failed command output | `src/core/tee.rs` | filtered output + raw-output hint | Can be quarantined via `RTK_TEE_DIR` |
| command history | `src/core/tracking.rs` | `rtk gain` summary | Native SQLite |
| telemetry opt-in | `src/core/telemetry.rs` | anonymous aggregate ping | Off by default, explicit consent required |

## 5. Java/Spring Boot integration concerns

RTK is not a Java SDK, but can assist Agent workflows in Java/Spring projects:

- Bean life cycle: does not directly enter the application process.
- Configuration management: only involves the RTK config and Agent hook config of the developer environment.
- Permissions and Auditing: Must distinguish between `rtk mvn` / `rtk gradlew` filtering of output and real build results.
- Log and link tracing: RTK compresses log reading, but is not a replacement for application-level tracing.
- Timeouts, retries and throttling: Controlled by native commands and CI, RTK primarily changes output rendering.
- Database or message queue: no direct access, commands such as `rtk psql` only compress CLI output.

## 6. Integration risks

- Global hook writing risk: `rtk init -g` may modify user-level Agent configuration.
- Permission risk: rewrite should not expand host permission and needs to be verified Deny / Ask / Allow.
- Evidence risk: filtered output is not a complete original log, and raw output must be read back during auditing.
- Statistical risk: token savings are estimates or local statistics and do not equal model quality improvements.
- Platform risk: Automatic hooking capabilities under Windows native are limited, and WSL is closer to the Linux path.
- Document drift risk: README version example is inconsistent with current `Cargo.toml`.

## To-do check items

- [ ] Install RTK in a staging environment.
- [ ] Verify `rtk rewrite "git status"`.
- [ ] Verify filtered output for 3 to 5 common commands.
- [ ] Verify raw-output recovery under `RTK_TEE_DIR`.
- [ ] Confirm installation and rollback paths for Codex / Claude Code respectively.

## Quality check items

- [x] Does not contain real keys or internal addresses.
- [x] Clearly distinguish between verified and unverified content.
- [x] Did not write README savings as a reproduced result.

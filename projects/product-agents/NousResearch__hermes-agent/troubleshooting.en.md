# Hermes Agent problem troubleshooting record

Currently, Hermes installation or running commands have not been executed on this machine, so this file first records the expected troubleshooting list. Whenever you encounter a real problem in the future, you should add the original text of the error, environment, reproduction steps, positioning process and verification results according to "one problem and one section".

## Problem: Installation script failed

- Discovery time: To be verified
- Current status: Not reproduced
- Scope of impact: first installation, dependency preparation, CLI startup

### Phenomenon

Will be recorded after actual operation. Focus on retaining the installer output and deleting the local account, private path and key.

### environment

- Operating System: To be logged
- Runtime version: To be documented
- Project version/Commit:`a72bb03757c0c925c686f9774eefc8dc5a77b329`
- Key dependencies: Python 3.11, uv, Node.js, ripgrep, ffmpeg, Git Bash

### Preliminary judgment

Possible reasons:

- The network cannot access the installation script, PyPI, npm, GitHub, or binary download sources.
- Python/uv/Node.js version conflict.
- Windows native shell conflicts with Git Bash path.
- blocked by terminal permissions, anti-virus software or proxy configuration.

## Problem: Provider or model configuration failed

- Discovery time: To be verified
- Current status: Not reproduced
- Scope of influence: model calling, tool gateway, OAuth

### Preliminary judgment

Possible reasons:

- The API key is missing, expired, or written to an incorrect location.
- provider/model alias does not match runtime provider resolution.
- OAuth incomplete or credential pool missed.
- Base_url, region, organization ID, or proxy configuration errors.

## Problem: Tool calling permissions are too wide

- Discovery time: To be verified
- Current status: Not reproduced
- Scope of influence: terminal, file, browser, MCP, remote backend

### Preliminary judgment

Key inspections are required:

- toolsets enabled in `hermes tools`.
- Whether the terminal backend is local, docker, ssh, modal, daytona or singularity.
- Whether dangerous command approval overrides write, delete, network and credential reading.
- Whether the MCP server exposes mutating tools that exceed requirements.

## Problem: Gateway messages cannot be sent and received

- Discovery time: To be verified
- Current status: Not reproduced
- Scope of influence: Telegram, Discord, Slack, WhatsApp, Signal and other platforms

### Preliminary judgment

Possible reasons:

- Platform token, OAuth or bot permissions are configured incorrectly.
- allowlist or DM pairing is not complete.
- Session key parsing error causes context discontinuity.
- The delivery fails but is not clearly exposed to the user.
- Gateway PID or token lock conflicts when multiple profiles are concurrent.

## Problem: MCP server is unavailable

- Discovery time: To be verified
- Current status: Not reproduced
- Scope of influence: External tool access

### Preliminary judgment

Possible reasons:

- The stdio server command is not executable.
- The remote HTTP server is unreachable or OAuth is not completed.
- tool include filter configuration error.
- The server probe failed but the installation process used the default toolset.
- MCP tool schema is incompatible with Hermes tool registry packaging.

## Positioning process template

| step | operate | result | in conclusion |
|---|---|---|---|
| 1 | Logging commands and environments | to be completed | to be completed |
| 2 | View Hermes output and logs | to be completed | to be completed |
| 3 | Minimal configuration reproduction | to be completed | to be completed |
| 4 | Compare source code and official documentation | to be completed | to be completed |

## To-do check items

- [ ] Log first installation errors or confirm that there are no errors.
- [ ] Log `hermes doctor` output.
- [ ] Record provider configuration results.
- [ ] Log at least one read-only tool call.
- [ ] Log minimum verification results for MCP/Gateway/Cron.

## Quality check items

- [x] No real key or internal address written.
- [x] Unrecurred issues are not written as resolved.
- [x] README description is not treated as the result of running on this machine.

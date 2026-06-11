# Hermes Agent source reading record

## 1. Reading objectives

- Questions to understand in this round: How Hermes connects CLI, gateway, tools, skills, memory, MCP and cron to the same Agent Loop.
- Related functions: Agent Loop, Tool Calling, Memory, MCP, Gateway, Cron, Terminal Backends.
- Expected output: key entry table, module map, 3 source code call chains and subsequent source code verification checklist.

Current status: partial completed. A reading route has been established based on the official architecture page and GitHub contents API, and the source code has not been cloned for function-level verification.

## 2. Source code entry

| Entrance | path | effect | in accordance with |
|---|---|---|---|
| CLI | `cli.py` | One of the interactive terminal entrances | Official architecture page |
| CLI subcommands | `hermes_cli/main.py` | `hermes` Subcommand entry | Official architecture page |
| Core Agent | `run_agent.py` | `AIAgent` core conversation loop | Official architecture page |
| Gateway | `gateway/run.py` | Messaging platform gateway runner | Official architecture page |
| Batch | `batch_runner.py` | batch trajectory generation | Official architecture page |
| MCP server | `mcp_serve.py` | MCP related service entrance, source code confirmation required | GitHub contents API |

## 3. Module map

| module | path | Responsibilities | Dependencies |
|---|---|---|---|
| Agent internals | `agent/` | prompt assembly、context compression、model metadata、memory manager、skills commands | Called by `run_agent.py` and the entry layer |
| CLI | `hermes_cli/` | Commands, configuration, provider auth, tools/skills config, plugins, gateway commands | For user commands and setup |
| Tools | `tools/` | Implementation of registry, terminal, file, web, browser, MCP, delegation and other tools | `model_tools.py` Responsible for discovery and dispatch |
| Toolsets | `toolsets.py` | Tool grouping and platform preset | Works with tool configuration and registry |
| Model tools | `model_tools.py` | Tool schema collection and tool call distribution | Connect Agent Loop and tools registry |
| Gateway | `gateway/` | Platform message access, session, delivery, pairing, hooks, status | Call `AIAgent` and handle platform differences |
| Cron | `cron/` | jobs and schedulers | Create Agent task and deliver results |
| Session state | `hermes_state.py`、`gateway/session.py` | SQLite + FTS5 session/state storage | Agent Loop and Gateway sharing |
| Providers | `providers/`、`hermes_cli/runtime_provider.py` | provider/model parsing and runtime credentials | Shared by CLI, Gateway, Cron, ACP |
| Skills | `skills/`、`optional-skills/` | Built-in and optional skills | Inject or call via CLI/Agent |
| Plugins | `plugins/` | Extensions such as memory provider and context engine | Discovered via plugin manager |

## 4. Recommended reading order

1. `README.md` and the official Architecture page to establish the entrance and data flow.
2. `run_agent.py`, confirm the main loop, retries, tool calls and persistence of `AIAgent`.
3. `agent/prompt_builder.py`、`agent/context_compressor.py`、`agent/prompt_caching.py`。
4. `hermes_cli/runtime_provider.py`、`hermes_cli/auth.py`、`providers/`。
5. `tools/registry.py`、`model_tools.py`、`toolsets.py`、`tools/mcp_tool.py`。
6. `hermes_state.py`、`gateway/session.py`。
7. `gateway/run.py`、`gateway/platforms/`、`gateway/delivery.py`、`gateway/pairing.py`。
8. `cron/jobs.py`、`cron/scheduler.py`。
9. `tools/environments/`, focus on the permission boundaries of local, docker, ssh, modal, daytona, and singularity.
10. `tests/`, looking for regression use cases corresponding to the main line.

## 5. Key call chain

### Call chain 1: CLI Conversation Loop

- Trigger condition: The user enters a normal message in the CLI.
- Starting point: `HermesCLI.process_input()`.
- Key steps: `AIAgent.run_conversation()` -> system prompt assembly -> provider runtime resolution -> provider API -> optional tool call -> `model_tools.handle_function_call()` -> loop.
- Endpoint: The final response is displayed and the session is saved.
- Input: user message, profile/config, session history, enabled toolsets.
- Output: assistant response, tool output, session record.
- Error handling: retry pending source code verification, fallback, interrupt and tool exception packaging.
- Basis: Official architecture page.

### Call chain 2: Tool Registration and Dispatch

- Trigger condition: Agent needs to expose the tool schema to the model or execute a tool call.
- Starting point: `tools/registry.py`.
- Key steps: tool file import-time registration -> `model_tools.py` triggers discovery/collection -> tool call dispatch -> tool implementation.
- End point: tool result returns Agent Loop.
- Input: enabled toolsets, platform configuration, model tool call arguments.
- Output: tool schema or tool result.
- Error handling: pending source code verification availability check, dangerous command approval, MCP failures.
-Based on: official architecture page and tools documentation.

### Call chain 3: Gateway Message

- Trigger condition: platform adapter receives the message.
- Starting point: `Adapter.on_message()`.
- Key steps: `GatewayRunner._handle_message()` -> authorize user -> resolve session key -> create `AIAgent` with history -> run conversation -> deliver response.
- Endpoint: The message platform receives a reply.
- Input: platform event, user identity, session key, message text.
- Output: platform messages, session update.
- Error handling: DM pairing, allowlist, delivery failure, token lock pending source code verification.
- Basis: Official architecture page.

## 6. Read notes

Important findings:

- It is worth reading the core of Hermes from `AIAgent` instead of gateway or CLI, because the official architecture page shows that multiple portals reuse the same core Agent.
- The tool system uses registry + import-time registration, which is suitable for key analysis tools discoverability, schema generation and execution permissions.
- Memory has two layers that need to be distinguished: curated memory file injection system prompt, session storage uses SQLite + FTS5 to save conversations and retrieve.
- Cron is an Agent task, not a normal shell cron; this affects permissions, context, and result delivery model.

Uncertain points:

- `run_agent.py` Is it too large? Do I need to read it by class/function slice first?
- Skills self-improved trigger conditions and persistence paths.
- MCP tool schema packaging, error handling and dynamic toolset naming.
- Approval, isolation, and credential delivery boundaries for terminal backends.

To be run for verification:

- After cloning the source code, run a static search to confirm the above path.
- Run `hermes doctor` with a read-only configuration.
- No real task execution will be performed until the writing terminal/file tool is enabled.

## To-do check items

- [x] Entry file found.
- [ ] Find the function-level implementation of the main process or Agent Loop.
- [ ] Find the model calling location.
- [ ] Locate tool registration and execution locations.
- [ ] Locate configuration, logging and error handling locations.

## Quality check items

- [x] The calling relationship to be verified is not written as source code fact.
- [x] Key concepts are named consistent with official documents.
- [x] Questions to be read are clearly documented.

# Hermes Agent project deep dive

## 1. Basic project information

- Project name: Hermes Agent
- Project ID: `NousResearch__hermes-agent`
- GitHub：https://github.com/NousResearch/hermes-agent
- Official documentation: https://hermes-agent.nousresearch.com/docs/
- Category: `product-agents`
-Collect level: Level A deep collect
- Current status: `analyzing`
- Main language: Python
- License：MIT
- Analysis date: 2026-06-10
- Analysis version/Commit:`a72bb03757c0c925c686f9774eefc8dc5a77b329`
- Whether to run verification: No
- Analysis basis: GitHub API, README, official document structure page, warehouse root directory API list

## 2. Positioning in one sentence

Hermes Agent is a product-level self-improving AI Agent that can run in CLI, messaging platforms and remote environments. The core learning value lies in how the complete Agent product organizes models, tools, skills, memory, MCP, scheduling and multi-backend execution.

## 3. Problems solved by the project

Hermes tries to solve the problem of continuity and deployment boundaries when individuals or teams use Agent for a long time: Agent not only completes one-time tasks in the local terminal, but can continue conversations through CLI, Telegram, Discord, Slack, WhatsApp, Signal and other portals, continue context through persistent memory and session search, precipitate reusable processes through skills, and execute tools through back-end execution tools such as local, Docker, SSH, Modal, Daytona, and Singularity.

Suitable topics for study:

- Product-level Agent entrance design: CLI, gateway, ACP, batch runner, API server.
- Agent Loop: model invocation, prompt assembly, tool scheduling, compression, persistence and callback.
- Tool Calling: Tool registration, toolsets, platform-level enable/disable and terminal backend.
- Memory: cross-session memory, SQLite + FTS5 session storage, profile isolation.
- MCP: External tool server access, tool discovery, tool filtering and credential configuration.
- Automation: How to turn a cron job into an agent task instead of a normal shell task.
- Security boundaries: command approval, messaging platform authorization, remote execution environment, key and tool permissions.

## 4. Project main line

Based on the official architecture page, the CLI will enter the interaction from `cli.py` or `hermes_cli/main.py`, and user input will enter `AIAgent.run_conversation()` via `HermesCLI.process_input()`. Agent constructs a system prompt, parses the provider and model, and calls the corresponding API mode; if the model returns tool call, it is handed over to `model_tools.handle_function_call()` to trigger tool distribution, and then continues to loop until the final response is generated and the session is saved.

The Gateway mainline and CLI share the core `AIAgent`: After the platform adapter receives the message, the gateway performs user authorization and session key parsing, then creates an Agent instance with history, executes the same conversation loop, and finally the platform adapter sends back a response.

The Cron mainline does not simply run the shell, but the scheduler loads the expired job, creates a new Agent, injects attached skills, runs the job prompt, and delivers the results to the target platform.

The above main line is based on the official architecture page and has not been verified function by function using local source code.

## 5. Quick Start

The installation entry given by the official README:

- Linux / macOS / WSL2 / Termux：`curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
- Windows PowerShell：`iex (irm https://hermes-agent.nousresearch.com/install.ps1)`
- Commonly used commands after installation: `hermes`, `hermes model`, `hermes tools`, `hermes config set`, `hermes gateway`, `hermes setup`, `hermes update`, `hermes doctor`

Currently collect does not execute these commands, so:

- Do not log any successful installation conclusions for this machine.
- Does not determine whether native Windows installation is available on the current machine.
- Does not determine whether the provider, gateway or MCP has been configured successfully.

For subsequent operation verification, the isolation environment should be used first, and the complete command, output, failure reason and key desensitization method should be recorded.

## 6. Core architecture

The official architecture page divides Hermes into four groups: entry layer, core Agent, storage and tool backend:

- Entry layer: CLI, Gateway, ACP, Batch Runner, API Server, Python Library.
- Core Agent: `AIAgent` in `run_agent.py`, including prompt builder, provider resolution, tool dispatch, compression, caching and persistence.
- Storage layer: `hermes_state.py`, `gateway/session.py`, using SQLite + FTS5 for session storage.
- Tool backend: terminal, browser, web, MCP, file, vision and other tool capabilities. Terminal has multiple backends.

diagrams see:

- `assets/diagrams/architecture.mmd`
- `assets/diagrams/agent-loop.mmd`
- `assets/diagrams/gateway-flow.mmd`

## 7. Core Principles

### Agent Loop

The core class is marked `AIAgent` in the official document. It takes care of provider selection, prompt construction, tool execution, retries, fallbacks, callbacks, compression, and persistence. Currently, only the official architecture description has been confirmed, and function-level implementation details have not yet been determined.

### Tool Calling

The official tool documentation explains that tools are functions that extend Agent capabilities, are organized by toolsets, and can be enabled or disabled by platform. The official architecture page explains that the central registry is located at `tools/registry.py`, tool files are registered when imported, and `model_tools.py` collects schema and distributes calls.

### Memory and Session

The official memory documentation states that Hermes uses bounded curated memory and injects `MEMORY.md` and `USER.md` into the system prompt when the session is started. The official architecture page also states that session storage uses SQLite + FTS5 and supports lineage, platform isolation and atomic writes. The specific writing timing and conflict handling of the two require source code verification.

### MCP

The official MCP documentation states that Hermes can connect to the local stdio server and remote HTTP MCP server, discover and register tools at startup, and support per-server tool filtering. MCP tools will eventually enter Hermes' tool calling system, but the specific schema packaging and error handling paths require source code verification.

### Skills

Both the README and the official architecture page list skills as one of the core capabilities. It can currently be confirmed that its positioning is procedural memory / reusable capabilities. The specific creation, storage, self-improvement and calling timing need to be continued under `agent/skill_commands.py`, `hermes_cli/skills_hub.py`, `hermes_cli/skills_config.py` and `skills/`.

### Cron

The official architecture page explains that cron job is triggered by scheduler tick, loads due jobs, creates a fresh agent, and delivers the results to the platform. Need to continue reading `cron/jobs.py`, `cron/scheduler.py` and gateway delivery related code.

## 8. Source code structure

Based on the GitHub contents API and official architecture page, give priority to:

- Entry files: `cli.py`, `hermes_cli/main.py`, `run_agent.py`, `gateway/run.py`, `batch_runner.py`, `mcp_serve.py`
- Core packages/modules: `agent/`, `hermes_cli/`, `tools/`, `gateway/`, `cron/`, `providers/`, `skills/`, `optional-skills/`, `plugins/`
- Configuration location: `cli-config.yaml.example`, `.env.example`, `hermes_cli/config.py`
- Examples and documentation: `docs/`, `website/`, `datagen-config-examples/`
- Test directory: `tests/`
- Installation and packaging: `pyproject.toml`, `setup.py`, `Dockerfile`, `docker-compose.yml`, `setup-hermes.sh`

## 9. Key call chain

### Call chain 1: CLI session

- Trigger condition: The user enters a message in the CLI.
- Starting point: `HermesCLI.process_input()`.
- Key steps: `AIAgent.run_conversation()` -> `prompt_builder.build_system_prompt()` -> `runtime_provider.resolve_runtime_provider()` -> provider API -> optional tool call -> `model_tools.handle_function_call()`.
- Endpoint: The final response is displayed and saved to SessionDB.
- Basis: Official architecture page.
- To be verified: specific exception handling, retry, compression and session writing code.

### Call chain 2: Message platform Gateway

- Trigger condition: Telegram, Discord, Slack and other platform adapters receive messages.
- Starting point: `Adapter.on_message()`.
- Key steps: `GatewayRunner._handle_message()` -> Authorization -> session key -> Create `AIAgent` with history -> `AIAgent.run_conversation()`.
- Endpoint: Deliver the response through the adapter.
- Basis: Official architecture page.
- To be verified: authentication, current limiting, retry and abnormal delivery paths of adapters on different platforms.

### Call chain 3: Cron Job

- Trigger condition: scheduler tick detects due job.
- Starting point: scheduler loads `jobs.json`.
- Key steps: create fresh Agent -> inject attached skills -> run job prompt -> delivery.
- End point: update job state and next_run.
- Basis: Official architecture page.
- To be verified: job storage format, failure retry, platform delivery failure handling.

## 10. integration method

Considerable integration paths:

- Use as an end product: After installation, talk to the Agent through `hermes`.
- Used as a messaging platform Agent: configure `hermes gateway setup/start` and then connect to the target platform.
- Use as MCP client: Configure `mcp_servers` in `~/.hermes/config.yaml` to let Hermes use external MCP server tools.
- Learning sample as a scalable tool system: Read the registration/distribution patterns of `tools/registry.py`, `toolsets.py` and `model_tools.py`.
- As a remote execution agent learning sample: focus on verifying the permission model and sandbox boundaries of terminal backends.

It is currently not recommended to directly connect to business systems without isolation and key management. First make read-only tools and minimal provider configuration, and then move to write-type tools and remote execution.

## 11. Problemshooting

Prioritize recording the following issues:

- The installation script failed to download dependencies: distinguish between network, Python, uv, Node.js, Git Bash, and ffmpeg.
- Provider configuration failed: distinguishing API key, base_url, model alias, OAuth and credential pool.
- Tool permissions are too wide: check `hermes tools`, terminal backend, approval configuration and dangerous command detection.
- Gateway messages cannot be received or sent: check platform credentials, allowlist, DM pairing, session routing and delivery.
- MCP server is not available: check stdio/HTTP configuration, OAuth, server startup, tool include filter.
- Memory results are not as expected: check session startup snapshot, memory tool writing and next session injection boundaries.

See `troubleshooting.md` for details.

## 12. Objective evaluation

### advantage

- Can be used as a complete case study of product-level Agent, covering entrance, tools, memory, scheduling, gateway, MCP and execution environment.
- The official document provides the architecture, data flow and reading order, which is suitable for intensive reading of source code.
- Mainly based on Python, the directory structure is clear and easy to disassemble by module.
- Supports multiple providers and multiple running backends, suitable for studying the extended design of platform-based Agents.

### shortcoming

- The ability range is very broad, and it is easy to stop at the README for the first time.
- Installation and operation involve keys, messaging platforms and remote execution, and verification costs are high.
- Tool execution and remote backends bring security risks, and require separate permission model analysis.
- The warehouse is updated quickly, and documents and source code conclusions need to be marked with date and commit.

### Applicable scenarios

- Learn the product-level Agent architecture.
- Learn the engineering organization of tool systems, MCP, skills, memory, gateway and cron.
- Compare Agent products or frameworks such as Claude Code, OpenAI Codex, OpenHands, LangGraph, etc.
- Study the permission boundaries of remote execution and messaging platform agents.

### not applicable scenario

- I just want to find a lightweight SDK to embed business services.
- Unwillingness to deal with model provider, messaging platform, MCP and tool permission configuration.
- Requires stable enterprise-grade SLA but has not yet completed self-deployment verification.
- Only the RAG pipeline is required, not the full Agent product.

## 13. Learning Todo List

See `learning-todo-list.md`.

## 14. Summary

Hermes Agent deserves a Level A in-depth collection because it is not a single-point demo, but a large-scale engineering sample covering the Agent product life cycle. The current first version of collect has completed the public metadata, official documents, preliminary architecture, learning tasks and draft diagrams; the follow-up focus is to clone the source code and verify the real call chain of `AIAgent`, tool registry, session storage, gateway, MCP and cron in the official recommended reading order, and then perform minimal installation and read-only tool verification.

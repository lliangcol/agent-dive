#Hermes Agent integration guide

## 1. integration goal

- Target system: local isolated learning environment.
- Target ability: run through the minimal dialogue of Hermes CLI, and then verify tools, memory, MCP, gateway and cron step by step.
- Integration method: Use it as an independent CLI product first, and then evaluate MCP client, messaging platform gateway and read-only tool extensions.
- Constraints: Real keys must not be written to the document; high-risk writing tools or remote execution backends must not be enabled without confirming permission boundaries.

## 2. Preconditions

- Running environment: The official README supports Linux, macOS, WSL2, Termux and Windows PowerShell; currently not natively verified.
- Dependencies: The installer will handle Python 3.11, uv, Node.js, ripgrep, ffmpeg, Git Bash and other dependencies; please refer to the official installation script for details.
- Model or service configuration: You need to select a provider. You can use officially supported Nous Portal, OpenRouter, NovitaAI, NVIDIA NIM, OpenAI, custom endpoint, etc.
- Permission requirements: terminal/file/browser/MCP/gateway Related capabilities require separate review of permissions and credentials.

## 3. Minimum integration path

It is recommended to implement it in three stages.

### Phase 1: Read-only quick verification

1. Prepare a new isolation shell or virtual machine.
2. Install Hermes according to the official installation instructions.
3. Execute `hermes doctor` and record the output.
4. Execute `hermes model` and select a test provider.
5. Execute `hermes tools` to confirm that the tool is enabled by default.
6. Start `hermes` and only conduct ordinary text conversations, without authorizing file writing or command execution.

### Phase 2: Tool and Memory Verification

1. Enable only the secure read-only toolset.
2. Verify that `memory` and `session_search` work according to the official documentation behavior.
3. Verify whether the tool call output is visible, interruptible, and auditable.
4. Record tool schema, approval prompts and failure output.

### Phase 3: MCP/Gateway/Cron Verification

1. Configure a read-only MCP server, such as a restricted filesystem or public API.
2. Verify MCP server tool discovery and tool filtering.
3. Select a messaging platform test gateway and give priority to using the test account.
4. Create a low-risk cron job that only outputs text to the test platform.
5. Check session, memory, delivery and log boundaries.

## 4. Interface and data flow

| enter | processing module | output | Remark |
|---|---|---|---|
| CLI text message | `cli.py` / `hermes_cli/` -> `AIAgent` | Terminal response, session record | Official architecture page basis |
| Platform news | `gateway/platforms/` -> `GatewayRunner` -> `AIAgent` | Platform reply, session record | Requires authorization and pairing |
| Tool call | `model_tools.py` -> `tools/registry.py` -> tool implementation | tool result | Need to review toolsets |
| MCP server config | `tools/mcp_tool.py` / MCP client | Dynamic MCP tools | Requires credentials and include filter |
| Cron job | `cron/` -> fresh `AIAgent` -> delivery | Timing results | Not a normal shell cron |

## 5. Java/Spring Boot integration concerns

Hermes is currently more suitable for learning as an independent Agent product or external tool process, and is not suitable for being directly embedded in the Spring Boot process. For integration with Java services, give priority to process boundaries or MCP boundaries:

- Bean life cycle: Do not host Hermes directly as a Spring Bean, preferring to interact through the HTTP/MCP/CLI process.
- Configuration management: API key, provider, MCP server and gateway credentials must be placed in independent configuration and do not enter the business warehouse.
- Permissions and auditing: Only necessary read-only tools are opened; write-type tools require approval and logs.
- Logs and link tracing: Log request IDs, user identities, tool calls, and failure reasons to avoid logging keys.
- Timeout, retry and current limit: Set timeout for external process calls; avoid long Agent tasks from occupying business threads.
- Database or message queue: do not directly grant write permission to the Agent database, but preferentially go through the restricted MCP server or read-only API.

## 6. Integration risks

- Dependent version: The installer manages multiple runtimes, and differences in environments may cause installation failure.
- Model costs: Multiple providers and tool gateways may incur invisible costs that require budgets and limits.
- Tool permissions: terminal/file/browser/MCP may cause high-risk side effects.
- Data security: gateway, memory, session storage and remote backend may all come into contact with sensitive content.
- Operational stability: The messaging platform, MCP server, provider and remote backend have independent failure modes.

## To-do check items

- [x] Clarify the integration goals and methods.
- [x] Write the minimum verification steps.
- [x] Document input, output and error handling concerns.
- [x] Mark verified and unverified content.

# Hermes Agent

## collect status

- Project ID: `NousResearch__hermes-agent`
- GitHub：https://github.com/NousResearch/hermes-agent
- Official documentation: https://hermes-agent.nousresearch.com/docs/
- Main category: `product-agents`
- Auxiliary tags: `agent-frameworks`, `agentic-coding`, `mcp-tools`, `memory-context`, `tool-calling`, `automation`
-Collect level: Level A deep collect
- Current status: `analyzing`
- Whether to run through: No
- Whether to perform source code analysis: partial
- Whether there are diagrams: partial
- Whether there are learning notes: Yes
- Last updated: 2026-06-10

## Positioning in one sentence

Hermes Agent is a product-level self-improving AI Agent built by Nous Research, covering CLI, message gateway, tool system, skill system, persistent memory, MCP, scheduling tasks and multi-run backend.

## Current data boundary

Verified:

- The GitHub repository exists and is a public repository.
- The GitHub API shows that the default branch is `main`, the primary language is Python, and the License is MIT.
- README and official documentation state that it includes CLI, gateway, tools, skills, memory, MCP, cron, terminal backends and other capabilities.
- The official architecture page gives the entrance, core modules, data flow and recommended source reading order.

Not verified:

- The installation command was not executed on this machine.
- not run `hermes`、`hermes doctor`、`hermes model`、`hermes tools`。
- The source code is not cloned for function-level call chain verification.
- Each provider, tool, messaging platform, MCP server or remote running backend has not been verified.

## File list

- [project deep dive](project-analysis.en.md)
- [source reading record](source-code-reading.en.md)
- [integration guide](integration-guide.en.md)
- [Problem troubleshooting records](troubleshooting.en.md)
- [Learning Todo List](learning-todo-list.md)
- [collectreport](collect-report.en.md)
- [diagrams directory](assets/diagrams/)
- [learning notes](../../../learning-notes/NousResearch__hermes-agent/README.en.md)

## drafts of diagrams

The current diagrams are all Mermaid source files, generated based on README, GitHub API and official documents. They have not been exported to PNG/SVG and have not been reviewed at the source code function level.

- [architecture.mmd](assets/diagrams/architecture.mmd)
- [agent-loop.mmd](assets/diagrams/agent-loop.mmd)
- [tool-and-skill-flow.mmd](assets/diagrams/tool-and-skill-flow.mmd)
- [memory-and-session-flow.mmd](assets/diagrams/memory-and-session-flow.mmd)
- [gateway-flow.mmd](assets/diagrams/gateway-flow.mmd)
- [mcp-integration-flow.mmd](assets/diagrams/mcp-integration-flow.mmd)
- [cron-scheduling-flow.mmd](assets/diagrams/cron-scheduling-flow.mmd)

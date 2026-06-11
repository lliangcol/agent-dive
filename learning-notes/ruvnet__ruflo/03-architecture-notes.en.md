# Ruflo Architecture Notes

## Current understanding

Ruflo's architecture can be viewed as four concentric layers:

1. User portal: Ruflo CLI, Claude Code plugin, Codex `.agents`, Web UI.
2. Tool surface: CLI commands and MCP tools.
3. Runtime domain:Agent, SwarmCoordinator, WorkflowEngine, MemoryBackend, PluginManager.
4. External systems: Claude Code, Codex, AgentDB/RuVector, provider APIs, Docker/Web UI, verification CI.

## Key boundaries

- Claude Code plugin lite is not equivalent to CLI full install.
- Codex `.agents` is not equal to Claude Code hooks.
- MCP stdio server must ensure that stdout only carries JSON-RPC.
- The existence of the Hook file does not mean that the forced access control is enabled.
- Web UI/mcp-bridge is the product side and needs to be verified separately from CLI/MCP runtime.

## diagrams

Project data has been generated:

- `projects/multi-agent/ruvnet__ruflo/assets/diagrams/architecture.mmd`
- `projects/multi-agent/ruvnet__ruflo/assets/diagrams/install-surface.mmd`
- `projects/multi-agent/ruvnet__ruflo/assets/diagrams/mcp-memory-flow.mmd`
- `projects/multi-agent/ruvnet__ruflo/assets/diagrams/plugin-boundary.mmd`

## to be completed

- Actual MCP tool list.
- CLI init generates file graph.
- Codex `.agents` loading process.
- Web UI/mcp-bridge request link.

# MCP

## Definition

MCP is the Model Context Protocol that standardizes how model applications access tools, resources, and prompts.

## Role in the AI Agent project

MCP can connect file systems, databases, browsers, code libraries, design tools and other capabilities to Agent, and reduce the cost of adaptation between different clients and tool services.

## Typical implementation

- MCP server exposes tools, resources and prompts.
- Client discovers capabilities and calls them by protocol.
- The tool parameter schema defines the input boundaries.
- Resource reading provides contextual material.

## Common misunderstandings

- Treat MCP as a normal HTTP API and do not pay attention to capability discovery and permissions.
- The tool is exposed too broadly and lacks minimum permissions.
- Ignore sensitive data boundaries for resource reads.
- No auditing of tool calls is logged.

## Recommended learning tasks

- Find out if the project supports MCP access.
- Analyze the input and output of an MCP tool.
- Check whether there are permission restrictions on resource reading.
- Design MCP interface draft for a read-only capability.

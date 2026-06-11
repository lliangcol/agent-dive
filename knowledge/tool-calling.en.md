# Tool Calling

## Definition

Tool Calling refers to the process in which a model or Agent selects tools, fills in parameters, executes external capabilities and receives execution results according to a structured protocol.

## Role in the AI Agent project

Tool calls allow Agents to scale from text generation to file operations, retrieval, databases, browsers, code execution, and business APIs. It is also a critical boundary for security, permissions, and observability.

## Typical implementation

- Function calls based on JSON Schema.
- Tool registry and unified executor.
- Tool permission whitelist and parameter verification.
- The execution results are passed back to the model to enter the next round of inference.

## Common misunderstandings

- Only focus on the number of tools and do not check permission boundaries.
- The parameter schema is written too wide, resulting in uncontrollable input.
- Tool exceptions are exposed directly to the model or user.
- No audit log and retry policy.

## Recommended learning tasks

- Find the tool registration location and executor.
- Analyze a tool's parameter schema.
- The error return method when the recording tool fails.
- Add a read-only custom tool and verify logs.

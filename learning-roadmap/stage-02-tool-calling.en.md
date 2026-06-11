# Stage 02:Tool Calling

## Stage goal

Understand tool registration, parameter schema, executors, permissions, error postbacks and logging.

## Essential knowledge

- JSON Schema or function signature.
- External API calls.
- Permission whitelist and parameter verification.

## Recommended tasks

- Locate the tool registry in the project.
- Analyze a tool's input, output, and exception handling.
- Add a read-only tool and record the call trace.

## Practice output

- Tool call chain description.
- A custom tool to access notes.

## Check for issues

- How does the model know what tools are available?
- Are the tool parameters verified?
- How is the result returned to the Agent after the tool fails?

## Next stage entrance

Enter Stage 03 to learn how Agent uses external knowledge.

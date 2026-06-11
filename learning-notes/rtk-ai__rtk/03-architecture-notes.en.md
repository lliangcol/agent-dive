# RTK Architecture Notes

## Preliminary module diagram

- `src/main.rs`:CLI facade.
- `src/cmds/`: Filter split by ecology.
- `src/core/`:runner, stream, config, tracking, tee, telemetry, filter.
- `src/discover/`:rewrite registry, lexer, rules, report.
- `src/hooks/`:hook lifecycle, permission, integrity, rewrite command.
- `hooks/`: Thin delegates deployed to each Agent.

## Key judgment

- The core of RTK is not to "make the model smarter", but to change the shape of the tool output into the context.
- The hook just rewrites the entry; the actual filtering still happens within the RTK binary.
- Codex integration should currently be understood according to prompt guidance, and automatic interception of commands cannot be assumed.
- tee recovery is a safety valve that filtering tools must have, and subsequent verification is required.

## To be filled

- Draw the filter strategy of each command ecosystem.
- Read how `src/parser/` supports test output parsing.
- Confirm telemetry compile-time switch and runtime consent judgment.

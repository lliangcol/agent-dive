# Context Engineering

## Definition

Context Engineering is an engineering approach to organizing information around the model context window, including selection, sorting, compression, clipping, referencing, and injection.

## Role in the AI Agent project

The quality of an agent largely depends on whether the context contains the correct materials, constraints, and task states. Project deep dives, code analysis, and tool invocations all require a stable context organization strategy.

## Typical implementation

- System prompts, developer prompts and user input layering.
- RAG search results organized by relevance and source.
- Long conversation summaries and task status compression.
- Important constraints are forwarded and low-value history is clipped.

## Common misunderstandings

- Tuck all material into context.
- The key constraint is located too far back.
- Mix facts, speculation and user preferences.
- There is no documentation of where the context comes from.

## Recommended learning tasks

- Record the entry to the project construction prompt.
- Analyze what material the context contains.
- Find cropping, summarization or compression logic.
- Use a failure case to check why the context is missing.

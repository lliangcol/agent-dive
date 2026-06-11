# Memory

## Definition

Memory is the mechanism by which the Agent retains information within a task or between tasks, including short-term context, session history, long-term preferences, external state, and retrievable knowledge.

## Role in the AI Agent project

Memory determines whether the Agent can continue to learn user preferences, save task progress, reuse historical experience, and avoid starting from scratch every time. In learning systems it is also used to save project progress and review questions.

## Typical implementation

- Session level message history.
- Long-term memory after digest compression.
- Vector database or document library.
- Clearly structured `progress.json`, task status and user preferences.

## Common misunderstandings

- Preserve all history as memory.
- Does not differentiate between user facts, task states, and model inferences.
- Memory has no expiration, error correction and deletion mechanisms.
- Sensitive information is stored for long periods of time.

## Recommended learning tasks

- Find where the project saves its state.
- Distinguish between short-term and long-term memory.
- Examine how memory is injected into the context.
- Design a deletable and auditable learning progress record.

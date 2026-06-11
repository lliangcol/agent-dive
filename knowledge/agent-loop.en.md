# Agent Loop

## Definition

Agent Loop is the core execution loop of the Agent system, which usually includes observing input, planning or thinking, calling the model, selecting actions, executing tools, receiving results, and determining whether to terminate.

## Role in the AI Agent project

It determines whether the Agent can advance from an input to a verifiable result, and also determines behaviors such as the maximum number of steps, failure recovery, tool result return, and user interruption. When analyzing the project, priority should be given to finding the entry and termination conditions of the Agent Loop.

## Typical implementation

- ReAct style think-act-observe loop.
- Two-stage process of Planner + Executor.
- Workflow node-driven directed graph execution.
- Asynchronous loop driven by event queue or task queue.

## Common misunderstandings

- Only look at model calls, not loop status and termination conditions.
- Ignore how to advance to the next round after a tool fails.
- Mistaking a prompt call for a complete Agent.
- No maximum steps, timeouts and manual takeover paths are set.

## Recommended learning tasks

- Find the entry point in the project that triggers the Agent Loop.
- Draw a flow chart of a task from input to completion.
- Record the maximum number of steps, termination conditions and error handling strategies.
- Compare loop differences between this project and another Agent framework.

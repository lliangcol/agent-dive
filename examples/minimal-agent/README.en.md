# Minimal Agent

A minimal Agent Loop example demonstrating the core pattern: user input → tool selection → tool execution → context accumulation → termination check.

## Run immediately

```bash
# Math
python examples/minimal-agent/agent.py "What is 3 + 4?"

# Word count
python examples/minimal-agent/agent.py "word count: hello world foo bar"

# Default question (no args)
python examples/minimal-agent/agent.py
```

**No external dependencies required.** Runs on Python 3.10+.

## Sample output

```
Question: What is 3 + 4?
  step 1: add({'a': 3.0, 'b': 4.0}) -> 7.0
  step 2: finish({'answer': '7.0'}) -> 7.0
Answer:   7.0
```

## Core structure

```python
context = [{"role": "user", "content": question}]

while step < MAX_STEPS:
    action = model(context)      # <- swap in real LLM here
    result = execute(action)
    context.append(result)
    if action["tool"] == "finish":
        break
```

## Built-in tools

| Tool | Params | Description |
|------|--------|-------------|
| `add` | `a`, `b` | Add two numbers |
| `word_count` | `text` | Count words |
| `finish` | `answer` | Surface the final answer and stop the loop |

## Swap in a real LLM

Replace the body of the `model()` function in `agent.py` with an actual API call:

```python
def model(context: list[dict]) -> dict:
    response = anthropic_client.messages.create(
        model="claude-sonnet-4-6",
        messages=context,
        tools=[...],  # tool definitions
    )
    return parse_tool_call(response)
```

The return format stays the same — `{"tool": <name>, "args": {...}}` — and the loop needs no changes.

## Design notes

- `MAX_STEPS = 5`: hard cap preventing infinite loops
- `context` list: the agent's working memory across the entire loop
- `finish` tool: explicit termination signal (no implicit exit)
- Tool exceptions are caught: one failing tool does not crash the agent

---

## Real LLM integration: agent_sdk.py

`agent_sdk.py` is the next step up from `agent.py` — it uses the Anthropic SDK's
native tool_use feature instead of the toy router.

### Install and run

```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...
python examples/minimal-agent/agent_sdk.py "What is 12 + 30?"
```

If the package is missing or the key is not set, the script prints a clear message
and exits with a non-zero code — no silent failure.

### Comparison

| | agent.py | agent_sdk.py |
|---|---|---|
| Model layer | Local toy router | Anthropic SDK tool_use |
| External deps | None | `pip install anthropic` |
| API key | Not required | `ANTHROPIC_API_KEY` |
| Tool format | Custom dict | Anthropic `input_schema` |

### Core pattern (client is injected for easy mocking in tests)

```python
def run_agent_sdk(question: str, client: Any, *, verbose: bool = True) -> str:
    messages = [{"role": "user", "content": question}]
    for step in range(1, MAX_STEPS + 1):
        response = client.messages.create(model=..., tools=TOOL_DEFS, messages=messages)
        if response.stop_reason == "end_turn":
            return response.content[0].text
        # Execute tool calls, append results to messages, continue loop

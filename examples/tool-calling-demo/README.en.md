# Tool-Calling Demo

A minimal runnable example demonstrating tool registration, JSON-schema-style parameter validation, tool execution, structured error passback, and call logging.

## Run immediately

```bash
python examples/tool-calling-demo/demo.py
```

**No external dependencies required.** Runs on Python 3.10+.

## Sample output

```
Registered tools: ['add', 'multiply', 'truncate', 'word_count']

[ok ] add({'a': 3, 'b': 4}) -> 7.0  (0.0 ms)
[ok ] multiply({'a': 6, 'b': 7}) -> 42.0  (0.0 ms)
[ok ] word_count({'text': 'the quick brown fox'}) -> 4  (0.0 ms)
[ok ] truncate({'text': 'Hello, world!', 'max_chars': 5}) -> Hello...  (0.0 ms)
[ok ] truncate({'text': 'Hi', 'max_chars': 10}) -> Hi  (0.0 ms)
[err] add({'a': 'not_a_number', 'b': 1}) -> {'error': "...", 'type': 'TypeError'}  (0.0 ms)
[err] unknown({}) -> {'error': '"unknown tool \'unknown\'"', 'type': 'KeyError'}  (0.0 ms)

7 calls logged.
```

## Core components

### ToolRegistry

```python
registry = ToolRegistry()
registry.register(ToolSpec(
    name="add",
    description="Return the sum of two numbers.",
    params=[Param("a", float), Param("b", float)],
    fn=lambda a, b: a + b,
))

record = registry.execute("add", {"a": 3, "b": 4})
# {"tool": "add", "args": {...}, "ok": True, "result": 7.0, "latency_ms": 0.02}
```

### Built-in tools

| Tool | Params | Description |
|------|--------|-------------|
| `add` | `a: float`, `b: float` | Add two numbers |
| `multiply` | `a: float`, `b: float` | Multiply two numbers |
| `word_count` | `text: str` | Count words |
| `truncate` | `text: str`, `max_chars: int` | Truncate a string |

### Error passback format

Tools never raise exceptions to the caller. All errors are returned as structured records:

```python
# Unknown tool
{"ok": False, "result": {"error": "unknown tool 'foo'", "type": "KeyError"}}

# Type error
{"ok": False, "result": {"error": "param 'a': expected float, got 'x'", "type": "TypeError"}}

# Missing required param
{"ok": False, "result": {"error": "missing required param 'b'", "type": "TypeError"}}
```

### Call log

```python
registry.log()
# [
#   {"tool": "add", "args": {"a": 3, "b": 4}, "ok": True, "result": 7.0, "latency_ms": 0.02},
#   ...
# ]
```

## Design notes

- **Param validation**: each `Param` declares a type and `required` flag; `_validate_args()` handles type coercion and missing-key checks
- **Error isolation**: any exception is caught and converted to `{"error": ..., "type": ...}` — subsequent calls are unaffected
- **Call log**: every `execute()` appends an entry regardless of outcome; `log()` returns a copy to prevent external mutation
- **`safe` flag**: `ToolSpec.safe=True` marks read-only / non-destructive tools — reserved for future permission checks
- **`build_registry()`**: factory function, convenient for tests and extension

## Wiring to a real LLM

The current `main()` uses a hard-coded call sequence. To drive it with a real LLM:

```python
# Inside your agent loop, pass the LLM's tool_call to the registry
action = llm.decide(context)           # {"tool": "add", "args": {"a": 3, "b": 4}}
record = registry.execute(action["tool"], action["args"])
context.append({"role": "tool", "result": record["result"], "ok": record["ok"]})
```

The `ToolRegistry` interface stays the same — no other changes needed.

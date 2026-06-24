# Tool-Calling Demo

展示工具注册、JSON Schema 风格参数校验、工具执行、错误回传和调用日志记录的最小可运行示例。

## 立即运行

```bash
python examples/tool-calling-demo/demo.py
```

**无需任何外部依赖**，Python 3.10+ 即可运行。

## 输出示例

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

## 核心组件

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

### 内置工具

| 工具 | 参数 | 说明 |
|------|------|------|
| `add` | `a: float`, `b: float` | 两数相加 |
| `multiply` | `a: float`, `b: float` | 两数相乘 |
| `word_count` | `text: str` | 统计词数 |
| `truncate` | `text: str`, `max_chars: int` | 截断字符串 |

### 错误回传格式

工具不会抛出异常到调用方，所有错误封装为结构化回传：

```python
# 未知工具
{"ok": False, "result": {"error": "unknown tool 'foo'", "type": "KeyError"}}

# 类型错误
{"ok": False, "result": {"error": "param 'a': expected float, got 'x'", "type": "TypeError"}}

# 缺少必填参数
{"ok": False, "result": {"error": "missing required param 'b'", "type": "TypeError"}}
```

### 调用日志

```python
registry.log()
# [
#   {"tool": "add", "args": {"a": 3, "b": 4}, "ok": True, "result": 7.0, "latency_ms": 0.02},
#   ...
# ]
```

## 设计说明

- **参数校验**：每个 `Param` 定义类型和是否必填，`_validate_args()` 做类型强制转换和缺失检查
- **错误隔离**：任何异常都被捕获并转为 `{"error": ..., "type": ...}`，不中断后续调用
- **调用日志**：每次 `execute()` 无论成败都追加日志，`log()` 返回副本防止外部修改
- **safe 标志**：`ToolSpec.safe=True` 标记只读/非破坏性工具，为未来权限控制预留扩展点
- **`build_registry()`**：工厂函数，方便测试和扩展（替换或追加工具）

## 替换为真实 LLM

`demo.py` 的 `main()` 目前是手写的调用序列。替换为真实 LLM 驱动时只需：

```python
# 在 Agent loop 中，把 model 返回的 tool_call 传给 registry.execute()
action = llm.decide(context)           # {"tool": "add", "args": {"a": 3, "b": 4}}
record = registry.execute(action["tool"], action["args"])
context.append({"role": "tool", "result": record["result"], "ok": record["ok"]})
```

`ToolRegistry` 的接口不变，其余代码无需修改。

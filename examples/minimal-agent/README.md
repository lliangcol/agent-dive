# Minimal Agent

最小 Agent Loop 示例，展示核心模式：用户输入 → 工具选择 → 工具执行 → 上下文积累 → 终止判断。

## 立即运行

```bash
# 数学计算
python examples/minimal-agent/agent.py "What is 3 + 4?"

# 词数统计
python examples/minimal-agent/agent.py "word count: hello world foo bar"

# 默认问题（无参数）
python examples/minimal-agent/agent.py
```

**无需任何外部依赖**，Python 3.10+ 即可运行。

## 输出示例

```
Question: What is 3 + 4?
  step 1: add({'a': 3.0, 'b': 4.0}) -> 7.0
  step 2: finish({'answer': '7.0'}) -> 7.0
Answer:   7.0
```

## 核心结构

```python
context = [{"role": "user", "content": question}]

while step < MAX_STEPS:
    action = model(context)      # ← 此处替换为真实 LLM 调用
    result = execute(action)
    context.append(result)
    if action["tool"] == "finish":
        break
```

## 内置工具

| 工具 | 参数 | 说明 |
|------|------|------|
| `add` | `a`, `b` | 两数相加 |
| `word_count` | `text` | 统计词数 |
| `finish` | `answer` | 返回最终答案，触发终止 |

## 替换为真实 LLM

将 `agent.py` 中 `model()` 函数的实现替换为 Anthropic/OpenAI 等 API 调用：

```python
def model(context: list[dict]) -> dict:
    # 传入 context，让 LLM 决定调用哪个工具
    response = anthropic_client.messages.create(
        model="claude-sonnet-4-6",
        messages=context,
        tools=[...],  # 工具定义
    )
    return parse_tool_call(response)
```

返回格式不变：`{"tool": <name>, "args": {...}}`，其余循环逻辑无需修改。

## 设计说明

- `MAX_STEPS = 5`：防止无限循环的安全上限
- `context` 列表：贯穿整个循环的"工作记忆"
- `finish` 工具：显式终止信号，而非隐式退出
- 工具异常有捕获：单个工具出错不会终止整个 Agent

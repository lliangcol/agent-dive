#!/usr/bin/env python3
"""
Minimal Agent Loop — examples/minimal-agent/agent.py

Core pattern:
  context = [initial user message]
  while step < MAX_STEPS:
      action = model(context)      # ← swap in real LLM here
      result = execute(action)
      context.append(result)
      if action["tool"] == "finish": break

No external dependencies. Runs on Python 3.10+.
"""
from __future__ import annotations

import re
import sys

MAX_STEPS = 5

# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------

def tool_add(a: float, b: float) -> str:
    """Return the sum of two numbers as a string."""
    return str(a + b)


def tool_word_count(text: str) -> str:
    """Return the word count of the given text as a string."""
    return str(len(text.split()))


def tool_finish(answer: str) -> str:
    """Signal the end of the loop and surface the final answer."""
    return answer


TOOLS: dict[str, dict] = {
    "add":        {"fn": tool_add,        "params": ["a", "b"]},
    "word_count": {"fn": tool_word_count, "params": ["text"]},
    "finish":     {"fn": tool_finish,     "params": ["answer"]},
}


# ---------------------------------------------------------------------------
# Toy model — replace this function body with a real LLM call
# ---------------------------------------------------------------------------

def model(context: list[dict]) -> dict:
    """
    Decide the next action given the conversation context.

    Returns {"tool": <name>, "args": {<param>: <value>, ...}}.

    Replace the body of this function with an actual LLM API call that
    receives `context` and returns a structured action dict.
    """
    # If the previous step produced a tool result, wrap it in finish.
    # A real LLM would generate this "summarise and conclude" step naturally.
    last = context[-1] if context else {}
    if last.get("role") == "tool" and last.get("tool") != "finish":
        return {"tool": "finish", "args": {"answer": last["result"]}}

    user_text = next(
        (m["content"] for m in reversed(context) if m["role"] == "user"), ""
    )
    # Route to "add" when the input looks like an arithmetic expression
    if "+" in user_text:
        nums = re.findall(r"\d+(?:\.\d+)?", user_text)
        if len(nums) >= 2:
            return {"tool": "add", "args": {"a": float(nums[0]), "b": float(nums[1])}}
    # Route to "word_count" when the user asks for a word count
    if "word" in user_text.lower() and "count" in user_text.lower():
        return {"tool": "word_count", "args": {"text": user_text}}
    # Fall back to finishing with an explicit "unknown" answer
    return {"tool": "finish", "args": {"answer": f"(unknown: {user_text!r})"}}


# ---------------------------------------------------------------------------
# Agent loop
# ---------------------------------------------------------------------------

def run_agent(question: str, *, verbose: bool = True) -> str:
    """
    Run the agent loop for the given question.

    Returns the final answer string. Terminates early on a "finish" tool call
    or after MAX_STEPS steps (whichever comes first).
    """
    context: list[dict] = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        action = model(context)
        tool_name = action.get("tool", "")
        args = action.get("args", {})

        if tool_name not in TOOLS:
            result = f"[unknown tool: {tool_name!r}]"
        else:
            try:
                result = TOOLS[tool_name]["fn"](**args)
            except Exception as exc:  # noqa: BLE001
                result = f"[error: {exc}]"

        context.append({"role": "tool", "tool": tool_name, "result": result})

        if verbose:
            print(f"  step {step}: {tool_name}({args}) -> {result}")

        if tool_name == "finish":
            return result

    return "[max steps reached]"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "What is 3 + 4?"
    print(f"Question: {question}")
    answer = run_agent(question)
    print(f"Answer:   {answer}")

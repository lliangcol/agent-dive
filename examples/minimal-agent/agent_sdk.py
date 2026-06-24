#!/usr/bin/env python3
"""
Minimal Agent Loop with Anthropic SDK — examples/minimal-agent/agent_sdk.py

Shows how to replace the toy model() in agent.py with a real Anthropic API call
using the official SDK's tool_use feature.

Requires:
    pip install anthropic

Usage:
    export ANTHROPIC_API_KEY=sk-ant-...
    python examples/minimal-agent/agent_sdk.py "What is 12 + 30?"
"""
from __future__ import annotations

import os
import sys
from typing import Any

MAX_STEPS = 10

# ---------------------------------------------------------------------------
# Tools — pure functions, no anthropic dependency
# ---------------------------------------------------------------------------

def tool_add(a: float, b: float) -> str:
    """Add two numbers and return their sum as a string."""
    return str(a + b)


def tool_word_count(text: str) -> str:
    """Return the number of whitespace-separated words in text."""
    return str(len(str(text).split()))


TOOLS: dict[str, dict] = {
    "add": {
        "fn": tool_add,
        "description": "Add two numbers and return their sum as a string.",
        "schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"},
            },
            "required": ["a", "b"],
        },
    },
    "word_count": {
        "fn": tool_word_count,
        "description": "Return the number of whitespace-separated words in text.",
        "schema": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Input text"},
            },
            "required": ["text"],
        },
    },
}

# Tool definitions in Anthropic API format — built once at import time
TOOL_DEFS: list[dict] = [
    {
        "name": name,
        "description": meta["description"],
        "input_schema": meta["schema"],
    }
    for name, meta in TOOLS.items()
]


# ---------------------------------------------------------------------------
# Agent loop — client is injected so tests can pass a mock
# ---------------------------------------------------------------------------

def run_agent_sdk(
    question: str,
    client: Any,
    *,
    model: str = "claude-haiku-4-5-20251001",
    verbose: bool = True,
) -> str:
    """
    Run the agent loop using the Anthropic SDK's tool_use feature.

    Args:
        question: The user's question.
        client:   An anthropic.Anthropic instance (or any duck-typed mock).
        model:    Anthropic model ID to use.
        verbose:  Print each tool call to stdout when True.

    Returns:
        The final answer string, or a sentinel like "[max steps reached]".
    """
    messages: list[dict] = [{"role": "user", "content": question}]

    for step in range(1, MAX_STEPS + 1):
        response = client.messages.create(
            model=model,
            max_tokens=1024,
            tools=TOOL_DEFS,
            messages=messages,
        )

        if response.stop_reason == "end_turn":
            for block in response.content:
                if block.type == "text":
                    return block.text
            return "(no text in response)"

        # stop_reason == "tool_use": execute each tool call and collect results
        tool_results = []
        for block in response.content:
            if block.type != "tool_use":
                continue

            tool_name = block.name
            tool_input = block.input

            if tool_name in TOOLS:
                try:
                    result = str(TOOLS[tool_name]["fn"](**tool_input))
                except Exception as exc:  # noqa: BLE001
                    result = f"[error: {exc}]"
            else:
                result = f"[unknown tool: {tool_name!r}]"

            if verbose:
                print(f"  step {step}: {tool_name}({tool_input}) -> {result}")

            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                }
            )

        messages.append({"role": "assistant", "content": response.content})
        if tool_results:
            messages.append({"role": "user", "content": tool_results})

    return "[max steps reached]"


# ---------------------------------------------------------------------------
# Entry point — dependency checks live here so the module is importable without
# anthropic installed (enables unit-testing run_agent_sdk with a mock client).
# ---------------------------------------------------------------------------

def main() -> None:
    try:
        import anthropic  # noqa: PLC0415
    except ImportError:
        print(
            "anthropic package not found.\n"
            "Install it with:  pip install anthropic",
            file=sys.stderr,
        )
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print(
            "ANTHROPIC_API_KEY environment variable is not set.\n"
            "Export it before running:\n"
            "  export ANTHROPIC_API_KEY=sk-ant-...",
            file=sys.stderr,
        )
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    question = " ".join(sys.argv[1:]) or "What is 12 + 30?"
    print(f"Question: {question}")
    answer = run_agent_sdk(question, client)
    print(f"Answer:   {answer}")


if __name__ == "__main__":
    main()

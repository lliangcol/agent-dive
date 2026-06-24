#!/usr/bin/env python3
"""
Parallel Tool Call Demo — examples/tool-calling-demo/parallel_demo.py

Demonstrates: dispatching multiple tool calls concurrently with
              ThreadPoolExecutor, preserving result order, then
              aggregating results in the same order as the original batch.

This mirrors the "parallel tool use" pattern where an LLM returns
several tool_use blocks in a single turn and the host executes them
concurrently before sending results back.

No external dependencies. Runs on Python 3.10+.

Usage:
    python examples/tool-calling-demo/parallel_demo.py
"""
from __future__ import annotations

import importlib.util
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Import ToolRegistry from sibling demo.py (no package install required)
# ---------------------------------------------------------------------------

_DEMO_PATH = Path(__file__).parent / "demo.py"
_spec = importlib.util.spec_from_file_location("_tool_calling_demo_base", _DEMO_PATH)
_demo_mod = importlib.util.module_from_spec(_spec)  # type: ignore[arg-type]
sys.modules["_tool_calling_demo_base"] = _demo_mod
_spec.loader.exec_module(_demo_mod)  # type: ignore[union-attr]

build_registry = _demo_mod.build_registry
ToolRegistry = _demo_mod.ToolRegistry


# ---------------------------------------------------------------------------
# Parallel dispatcher
# ---------------------------------------------------------------------------

def dispatch_parallel(
    registry: "ToolRegistry",
    calls: list[tuple[str, dict[str, Any]]],
    *,
    max_workers: int = 4,
) -> list[dict[str, Any]]:
    """
    Execute *calls* concurrently and return results in the same order.

    Each call is a (tool_name, args_dict) tuple.  Results preserve the
    original index order regardless of which future completes first.
    """
    results: list[dict[str, Any] | None] = [None] * len(calls)

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {
            pool.submit(registry.execute, name, args): idx
            for idx, (name, args) in enumerate(calls)
        }
        for future in as_completed(futures):
            idx = futures[future]
            results[idx] = future.result()

    return results  # type: ignore[return-value]


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    registry = build_registry()

    # Simulate a model returning multiple tool_use blocks in one turn
    batch: list[tuple[str, dict[str, Any]]] = [
        ("add",        {"a": 10,  "b": 20}),
        ("multiply",   {"a": 6,   "b": 7}),
        ("word_count", {"text": "the quick brown fox jumps"}),
        ("add",        {"a": 100, "b": 200}),
    ]

    print(f"Dispatching {len(batch)} tool calls in parallel...\n")
    t0 = time.monotonic()
    results = dispatch_parallel(registry, batch)
    elapsed_ms = round((time.monotonic() - t0) * 1000, 2)

    for (name, args), record in zip(batch, results):
        status = "ok " if record["ok"] else "err"
        print(f"  [{status}] {name}({args}) -> {record['result']}")

    print(f"\nAll {len(results)} calls completed in {elapsed_ms} ms.")
    print(f"Total calls logged in registry: {len(registry.log())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

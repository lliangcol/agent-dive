#!/usr/bin/env python3
"""
RAG Agent Demo — examples/rag-agent-demo/rag.py

Demonstrates Retrieval-Augmented Generation without external dependencies:

  1. Corpus:    a small set of text chunks with source labels
  2. Embed:     bag-of-words term-frequency vectors (no numpy, no model)
  3. Retrieve:  cosine similarity, return top-k chunks
  4. Generate:  toy answer formatter that surfaces retrieved context
                (replace with a real LLM call in production)

No external dependencies. Runs on Python 3.10+.

Usage:
    python examples/rag-agent-demo/rag.py "What is an AI agent?"
    python examples/rag-agent-demo/rag.py          # uses default question
"""
from __future__ import annotations

import math
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------

@dataclass
class Chunk:
    """A single retrievable unit of text."""
    id: str
    text: str
    source: str


@dataclass
class RetrievedChunk:
    """A chunk paired with its retrieval score."""
    chunk: Chunk
    score: float


# ---------------------------------------------------------------------------
# Embedding: bag-of-words term frequency
# ---------------------------------------------------------------------------

_STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "in", "on", "at", "to", "for", "of", "and", "or", "but", "with",
    "it", "its", "this", "that", "by", "as", "from", "can", "do", "not",
    "have", "has", "had", "will", "would", "could", "should",
}


def tokenize(text: str) -> Counter:
    """
    Lowercase, split on non-alphanumeric characters, remove stopwords.
    Returns a Counter of token frequencies.
    """
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    return Counter(t for t in tokens if t not in _STOPWORDS)


def cosine_sim(a: Counter, b: Counter) -> float:
    """
    Cosine similarity between two term-frequency Counter objects.
    Returns 0.0 when either vector is zero.
    """
    if not a or not b:
        return 0.0
    dot = sum(a[t] * b[t] for t in a if t in b)
    norm_a = math.sqrt(sum(v * v for v in a.values()))
    norm_b = math.sqrt(sum(v * v for v in b.values()))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot / (norm_a * norm_b)


# ---------------------------------------------------------------------------
# Corpus helpers
# ---------------------------------------------------------------------------

def embed_corpus(chunks: list[Chunk]) -> list[tuple[Chunk, Counter]]:
    """Pre-compute token vectors for every chunk."""
    return [(chunk, tokenize(chunk.text)) for chunk in chunks]


def retrieve(
    query: str,
    embedded: list[tuple[Chunk, Counter]],
    *,
    top_k: int = 3,
) -> list[RetrievedChunk]:
    """
    Score every chunk by cosine similarity to the query and return
    the top-k results, highest score first.
    """
    q_vec = tokenize(query)
    scored = [
        RetrievedChunk(chunk=chunk, score=cosine_sim(q_vec, vec))
        for chunk, vec in embedded
    ]
    scored.sort(key=lambda r: r.score, reverse=True)
    return scored[:top_k]


# ---------------------------------------------------------------------------
# Generation (toy — replace body with a real LLM call)
# ---------------------------------------------------------------------------

def generate(question: str, results: list[RetrievedChunk]) -> str:
    """
    Format retrieved context into an answer.

    In production: pass question + context to an LLM API and return its reply.
    Here we surface the best-matching chunk text directly so the demo is
    runnable without an API key.
    """
    if not results or results[0].score == 0.0:
        return "(no relevant context found)"

    best = results[0]
    context_lines = "\n".join(
        f"  [{r.score:.2f}] ({r.chunk.source}) {r.chunk.text}"
        for r in results
        if r.score > 0.0
    )
    return (
        f"Based on '{best.chunk.source}' (score {best.score:.2f}):\n"
        f"{best.chunk.text}\n\n"
        f"--- retrieved context ---\n{context_lines}"
    )


# ---------------------------------------------------------------------------
# Default corpus — small, self-contained, covers Agent topics
# ---------------------------------------------------------------------------

DEFAULT_CHUNKS: list[Chunk] = [
    Chunk(
        id="agent-def",
        source="AI Agents Overview",
        text=(
            "An AI agent is a system that perceives its environment, "
            "makes decisions, and takes actions to achieve a goal. "
            "Agents typically have a planning component, memory, and tools."
        ),
    ),
    Chunk(
        id="rag-def",
        source="RAG Explainer",
        text=(
            "Retrieval-Augmented Generation (RAG) combines a retrieval step "
            "with a language model. The retriever finds relevant documents; "
            "the generator synthesises an answer grounded in those documents."
        ),
    ),
    Chunk(
        id="tool-use",
        source="Tool Use Patterns",
        text=(
            "Tool use lets an LLM call external functions such as web search, "
            "calculators, or databases. The model receives structured results "
            "and incorporates them into its next response."
        ),
    ),
    Chunk(
        id="memory",
        source="Agent Memory",
        text=(
            "Agent memory can be short-term (current context window) or "
            "long-term (external vector store or key-value store). "
            "Long-term memory allows the agent to recall past interactions."
        ),
    ),
    Chunk(
        id="planning",
        source="Planning in Agents",
        text=(
            "Planning breaks a complex goal into sub-tasks. Common strategies "
            "include Chain-of-Thought prompting, ReAct (Reason + Act), and "
            "tree-of-thought search over possible action sequences."
        ),
    ),
    Chunk(
        id="embedding",
        source="Embeddings",
        text=(
            "Embeddings map text to dense numeric vectors. Similar texts have "
            "vectors that are close in cosine distance. Production RAG systems "
            "use neural embedding models rather than bag-of-words."
        ),
    ),
]


# ---------------------------------------------------------------------------
# Top-level pipeline
# ---------------------------------------------------------------------------

def run_rag(
    question: str,
    chunks: list[Chunk] | None = None,
    *,
    top_k: int = 3,
    verbose: bool = True,
) -> str:
    """
    Run the full RAG pipeline: embed corpus → retrieve → generate.

    Args:
        question: The user's question.
        chunks:   Corpus to search (defaults to DEFAULT_CHUNKS).
        top_k:    Number of chunks to retrieve.
        verbose:  Print retrieval scores to stdout when True.

    Returns:
        The generated answer string.
    """
    corpus = chunks if chunks is not None else DEFAULT_CHUNKS
    embedded = embed_corpus(corpus)
    results = retrieve(question, embedded, top_k=top_k)

    if verbose:
        print(f"Query: {question!r}")
        print(f"Top-{top_k} results:")
        for r in results:
            print(f"  score={r.score:.3f}  [{r.chunk.source}] {r.chunk.text[:60]}...")
        print()

    return generate(question, results)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    question = " ".join(sys.argv[1:]) or "What is an AI agent?"
    answer = run_rag(question)
    print("Answer:")
    print(answer)
    return 0


if __name__ == "__main__":
    sys.exit(main())

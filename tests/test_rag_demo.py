"""Unit tests for examples/rag-agent-demo/rag.py"""

from __future__ import annotations

import importlib.util
import math
import runpy
import subprocess
import sys
from collections import Counter
from pathlib import Path

import pytest

_RAG = Path(__file__).resolve().parents[1] / "examples" / "rag-agent-demo" / "rag.py"
_spec = importlib.util.spec_from_file_location("rag_demo", _RAG)
_mod = importlib.util.module_from_spec(_spec)  # type: ignore[arg-type]
sys.modules["rag_demo"] = _mod
_spec.loader.exec_module(_mod)  # type: ignore[union-attr]

Chunk = _mod.Chunk
RetrievedChunk = _mod.RetrievedChunk
tokenize = _mod.tokenize
cosine_sim = _mod.cosine_sim
embed_corpus = _mod.embed_corpus
retrieve = _mod.retrieve
generate = _mod.generate
run_rag = _mod.run_rag
DEFAULT_CHUNKS = _mod.DEFAULT_CHUNKS


# ---------------------------------------------------------------------------
# tokenize
# ---------------------------------------------------------------------------

def test_tokenize_returns_counter():
    result = tokenize("hello world")
    assert isinstance(result, Counter)


def test_tokenize_lowercases():
    result = tokenize("Hello WORLD")
    assert "hello" in result
    assert "world" in result


def test_tokenize_removes_stopwords():
    result = tokenize("the quick brown fox")
    assert "the" not in result
    assert "quick" in result
    assert "brown" in result
    assert "fox" in result


def test_tokenize_empty_string():
    result = tokenize("")
    assert result == Counter()


def test_tokenize_punctuation_split():
    result = tokenize("hello, world!")
    assert "hello" in result
    assert "world" in result


def test_tokenize_counts_frequencies():
    result = tokenize("cat cat dog")
    assert result["cat"] == 2
    assert result["dog"] == 1


# ---------------------------------------------------------------------------
# cosine_sim
# ---------------------------------------------------------------------------

def test_cosine_sim_identical_vectors():
    a = Counter({"ai": 2, "agent": 1})
    assert cosine_sim(a, a) == pytest.approx(1.0)


def test_cosine_sim_orthogonal_vectors():
    a = Counter({"ai": 1})
    b = Counter({"robot": 1})
    assert cosine_sim(a, b) == pytest.approx(0.0)


def test_cosine_sim_partial_overlap():
    a = Counter({"agent": 1, "planning": 1})
    b = Counter({"agent": 1, "memory": 1})
    sim = cosine_sim(a, b)
    assert 0.0 < sim < 1.0


def test_cosine_sim_empty_a():
    assert cosine_sim(Counter(), Counter({"x": 1})) == 0.0


def test_cosine_sim_empty_b():
    assert cosine_sim(Counter({"x": 1}), Counter()) == 0.0


def test_cosine_sim_both_empty():
    assert cosine_sim(Counter(), Counter()) == 0.0


def test_cosine_sim_zero_norm():
    # Counter with zero-value entries: norm = 0, but not falsy
    a = Counter({"x": 0})
    b = Counter({"y": 1})
    assert cosine_sim(a, b) == 0.0


def test_cosine_sim_symmetry():
    a = Counter({"tool": 2, "agent": 1})
    b = Counter({"tool": 1, "memory": 3})
    assert cosine_sim(a, b) == pytest.approx(cosine_sim(b, a))


# ---------------------------------------------------------------------------
# embed_corpus
# ---------------------------------------------------------------------------

def test_embed_corpus_returns_list_of_pairs():
    chunks = [Chunk(id="c1", text="hello world", source="s")]
    result = embed_corpus(chunks)
    assert len(result) == 1
    chunk, vec = result[0]
    assert chunk.id == "c1"
    assert isinstance(vec, Counter)


def test_embed_corpus_preserves_order():
    chunks = [
        Chunk(id="a", text="alpha beta", source="s"),
        Chunk(id="b", text="gamma delta", source="s"),
    ]
    result = embed_corpus(chunks)
    assert result[0][0].id == "a"
    assert result[1][0].id == "b"


# ---------------------------------------------------------------------------
# retrieve
# ---------------------------------------------------------------------------

def test_retrieve_returns_top_k():
    chunks = [Chunk(id=str(i), text=f"agent tool memory {i}", source="s") for i in range(5)]
    embedded = embed_corpus(chunks)
    results = retrieve("agent tool", embedded, top_k=2)
    assert len(results) == 2


def test_retrieve_sorted_by_score_descending():
    chunks = [
        Chunk(id="exact", text="agent planning memory tool",  source="s"),
        Chunk(id="partial", text="agent",                     source="s"),
        Chunk(id="unrelated", text="cat dog bird",            source="s"),
    ]
    embedded = embed_corpus(chunks)
    results = retrieve("agent planning", embedded, top_k=3)
    scores = [r.score for r in results]
    assert scores == sorted(scores, reverse=True)


def test_retrieve_best_match_first():
    chunks = [
        Chunk(id="rag", text="retrieval augmented generation rag",    source="RAG"),
        Chunk(id="agent", text="agent planning tool memory",          source="Agent"),
    ]
    embedded = embed_corpus(chunks)
    results = retrieve("rag retrieval", embedded, top_k=2)
    assert results[0].chunk.id == "rag"


def test_retrieve_returns_retrieved_chunk_type():
    embedded = embed_corpus(DEFAULT_CHUNKS)
    results = retrieve("agent", embedded, top_k=1)
    assert isinstance(results[0], RetrievedChunk)
    assert hasattr(results[0], "score")
    assert hasattr(results[0], "chunk")


def test_retrieve_empty_corpus():
    results = retrieve("agent", [], top_k=3)
    assert results == []


def test_retrieve_top_k_larger_than_corpus():
    chunks = [Chunk(id="x", text="agent", source="s")]
    results = retrieve("agent", embed_corpus(chunks), top_k=10)
    assert len(results) == 1


# ---------------------------------------------------------------------------
# generate
# ---------------------------------------------------------------------------

def test_generate_no_results_returns_no_context():
    assert generate("?", []) == "(no relevant context found)"


def test_generate_zero_score_returns_no_context():
    r = RetrievedChunk(chunk=Chunk(id="c", text="irrelevant", source="s"), score=0.0)
    assert generate("?", [r]) == "(no relevant context found)"


def test_generate_includes_source():
    r = RetrievedChunk(
        chunk=Chunk(id="c", text="AI agents perceive and act.", source="Overview"),
        score=0.5,
    )
    answer = generate("agent?", [r])
    assert "Overview" in answer


def test_generate_includes_chunk_text():
    r = RetrievedChunk(
        chunk=Chunk(id="c", text="agents use tools and memory", source="s"),
        score=0.4,
    )
    answer = generate("agents?", [r])
    assert "agents use tools and memory" in answer


def test_generate_skips_zero_score_in_context():
    r1 = RetrievedChunk(chunk=Chunk(id="a", text="relevant text", source="A"), score=0.5)
    r2 = RetrievedChunk(chunk=Chunk(id="b", text="unrelated", source="B"), score=0.0)
    answer = generate("?", [r1, r2])
    assert "B" not in answer or "0.00" not in answer  # zero-score chunk excluded from context


# ---------------------------------------------------------------------------
# DEFAULT_CHUNKS corpus
# ---------------------------------------------------------------------------

def test_default_chunks_nonempty():
    assert len(DEFAULT_CHUNKS) > 0


def test_default_chunks_have_required_fields():
    for chunk in DEFAULT_CHUNKS:
        assert chunk.id
        assert chunk.text
        assert chunk.source


def test_default_chunks_ids_unique():
    ids = [c.id for c in DEFAULT_CHUNKS]
    assert len(ids) == len(set(ids))


# ---------------------------------------------------------------------------
# run_rag integration
# ---------------------------------------------------------------------------

def test_run_rag_returns_string():
    result = run_rag("What is an AI agent?", verbose=False)
    assert isinstance(result, str)
    assert len(result) > 0


def test_run_rag_agent_query_finds_agent_chunk():
    result = run_rag("What is an AI agent?", verbose=False)
    assert "AI Agents Overview" in result or "agent" in result.lower()


def test_run_rag_rag_query_finds_rag_chunk():
    result = run_rag("How does retrieval augmented generation work?", verbose=False)
    assert "RAG" in result or "retrieval" in result.lower()


def test_run_rag_custom_corpus():
    corpus = [Chunk(id="c1", text="Python is a programming language.", source="Python Docs")]
    result = run_rag("python programming", corpus, verbose=False)
    assert "Python" in result


def test_run_rag_no_match_returns_no_context():
    corpus = [Chunk(id="c1", text="alpha beta gamma", source="s")]
    result = run_rag("zzzzzz", corpus, verbose=False)
    assert "(no relevant context found)" in result


def test_run_rag_verbose_prints(capsys):
    run_rag("agent memory", verbose=True)
    captured = capsys.readouterr()
    assert "Query:" in captured.out
    assert "Top-" in captured.out


def test_run_rag_top_k_respected():
    embedded = embed_corpus(DEFAULT_CHUNKS)
    results = retrieve("agent", embedded, top_k=2)
    assert len(results) <= 2


# ---------------------------------------------------------------------------
# main()
# ---------------------------------------------------------------------------

def test_main_returns_zero():
    assert _mod.main() == 0


def test_main_with_argv(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["rag.py", "What", "is", "RAG?"])
    _mod.main()
    captured = capsys.readouterr()
    assert "Answer:" in captured.out


# ---------------------------------------------------------------------------
# __main__ subprocess + runpy
# ---------------------------------------------------------------------------

def test_runs_as_script():
    result = subprocess.run(
        [sys.executable, str(_RAG), "What is an AI agent?"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Answer:" in result.stdout


def test_main_block_via_runpy(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["rag.py"])
    with pytest.raises(SystemExit) as exc:
        runpy.run_path(str(_RAG), run_name="__main__")
    assert exc.value.code == 0

# RAG

## Definition

RAG is the abbreviation of Retrieval-Augmented Generation, which refers to retrieving relevant content from external knowledge sources and then injecting the retrieval results into context-assisted model generation.

## Role in the AI Agent project

RAG allows Agents to use project documents, code, knowledge bases or business materials, reducing the illusion caused by pure model memory. For code learning systems, RAG is often used to locate files, answer source code questions, and organize learning materials.

## Typical implementation

- Document segmentation, vectorization and vector retrieval.
- Hybrid recall of keyword retrieval and vector retrieval.
- Reordering, context compression and reference postback.
- Symbol index, call graph or knowledge graph for your code.

## Common misunderstandings

- Only vector retrieval is performed, recall quality is not evaluated.
- The cut particles are too large or too small.
- Without retaining source citations, conclusions cannot be traced.
- Filling the search results directly with context will reduce the quality.

## Recommended learning tasks

- Sort out the data import, index and retrieval links of the project.
- Record chunk strategy and metadata.
- Check whether the generated answer comes with a source.
- Compare the effectiveness of different search strategies using the same question.

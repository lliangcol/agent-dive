# Projects

This directory saves the AI ​​Agent project deep dive data collected by AgentDive.

## Naming convention

Each project directory uses `owner__repo` as the stable ID. For example:

```text
projects/agent-frameworks/langchain-ai__langgraph/
learning-notes/langchain-ai__langgraph/
```

Don't just use the project name as the directory name to avoid conflicts with warehouses with the same name.

## Classification

| Classification | illustrate |
|---|---|
| `agent-frameworks` | Common Agent Framework |
| `agentic-coding` | AI coding agents and development aids |
| `rag-agents` | RAG / Knowledge Agent |
| `mcp-tools` | MCP tools, services and ecological projects |
| `multi-agent` | Multi-Agent collaboration framework and practices |
| `evaluation-observability` | Measurement, monitoring, tracking and observability |
| `product-agents` | Product-level Agent application |

## Single project proposal structure

```text
projects/<category>/<owner__repo>/
├── README.md
├── meta.json
├── project-analysis.md
├── source-code-reading.md
├── integration-guide.md
├── troubleshooting.md
├── learning-todo-list.md
├── collect-report.md
└── assets/
    └── diagrams/
```

## Write boundaries

When collecting a project, only the current project directory is modified, corresponding to `learning-notes/<owner__repo>/`, `PROJECTS.md` and `LEARNING_PROGRESS.md`.

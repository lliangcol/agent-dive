# Projects

本目录保存被 AgentDive 收录的 AI Agent 项目精读资料。

## 命名规范

每个项目目录使用 `owner__repo` 作为稳定 ID。例如：

```text
projects/agent-frameworks/langchain-ai__langgraph/
learning-notes/langchain-ai__langgraph/
```

不要只用项目名作为目录名，避免同名仓库冲突。

## 分类

| 分类 | 说明 |
|---|---|
| `agent-frameworks` | 通用 Agent 框架 |
| `agentic-coding` | AI 编码 Agent 和开发辅助工具 |
| `rag-agents` | RAG / Knowledge Agent |
| `mcp-tools` | MCP 工具、服务和生态项目 |
| `multi-agent` | 多 Agent 协作框架和实践 |
| `evaluation-observability` | 评测、监控、追踪和可观测性 |
| `product-agents` | 产品级 Agent 应用 |

## 单项目建议结构

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

## 写入边界

收录一个项目时，只修改当前项目目录、对应 `learning-notes/<owner__repo>/`、`PROJECTS.md` 和 `LEARNING_PROGRESS.md`。

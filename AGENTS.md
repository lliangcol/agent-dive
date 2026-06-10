# AGENTS.md

本文件面向 AI 编码助手、自动化代理和维护者，说明 AgentDive 仓库的协作边界。

## 项目定位

AgentDive 是一个中文 AI Agent 开源项目精读与学习资料仓库。核心产物是项目分析、图解、学习任务、学习笔记和验证证据，不是 Awesome List，也不是第三方项目源码镜像。

## 工作规则

- 默认使用简体中文撰写文档和总结。
- 不修改 `docs/` 下的原始需求资料，除非任务明确要求。
- 不提交账号、密钥、token、本机私有路径、私有配置或未脱敏日志。
- 不伪造运行结果、源码结论、项目状态、Star 数、许可证或上游能力。
- 没有真实运行、测试或源码验证证据时，必须在对应 `evidence.md`、`meta.json` 或正文中标注 `not_run`、`pending`、`partial` 或明确的推断边界。
- 新增项目使用稳定 ID：`owner__repo`。
- 单次项目收录通常只修改 `projects/<category>/<owner__repo>/`、`learning-notes/<owner__repo>/`、`PROJECTS.md` 和 `LEARNING_PROGRESS.md`。
- 修改模板、脚本、索引或项目资料后运行 `python scripts/check-agent-dive.py`。

## 代码发现

本项目使用 codebase-memory-mcp 维护代码知识图谱。做代码发现时始终优先使用 MCP 图谱工具，不要先从 grep、glob 或文件搜索开始。

优先级：

1. `search_graph`：按名称、自然语言或模式查找函数、类、路由和变量。
2. `trace_path`：追踪调用方、被调用方、数据流或跨服务路径。
3. `get_code_snippet`：读取已定位符号的源码片段。
4. `query_graph`：执行复杂图查询。
5. `get_architecture`：获取项目结构和架构摘要。

仅在以下情况 fallback 到 `rg`、文件列表或直接阅读文件：

- 搜索字符串字面量、错误消息、配置值或非代码文件。
- MCP 图谱工具不可用、项目未索引或返回结果不足。
- 任务本身是 GitHub 配置、Markdown、许可证、模板、脚本说明等非代码内容。

## Pull Request 预期

- PR 描述应列出变更范围、验证命令和未完成事项。
- 影响项目状态的 PR 必须同步更新项目目录、学习笔记、`PROJECTS.md` 和 `LEARNING_PROGRESS.md`。
- 不要把 `study-ready`、`in-study` 或 `completed` 用作宣传性状态；状态必须由证据支撑。

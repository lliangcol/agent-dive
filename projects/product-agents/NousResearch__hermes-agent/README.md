# Hermes Agent

## 收录状态

- 项目 ID：`NousResearch__hermes-agent`
- GitHub：https://github.com/NousResearch/hermes-agent
- 官方文档：https://hermes-agent.nousresearch.com/docs/
- 主分类：`product-agents`
- 辅助标签：`agent-frameworks`、`agentic-coding`、`mcp-tools`、`memory-context`、`tool-calling`、`automation`
- 收录等级：Level A 深度收录
- 当前状态：`analyzing`
- 是否跑通：否
- 是否源码分析：部分
- 是否有图解：部分
- 是否有学习笔记：是
- 最近更新：2026-06-10

## 一句话定位

Hermes Agent 是 Nous Research 构建的产品级自改进 AI Agent，覆盖 CLI、消息网关、工具系统、技能系统、持久记忆、MCP、调度任务和多运行后端。

## 当前资料边界

已验证：

- GitHub 仓库存在且为公开仓库。
- GitHub API 显示默认分支为 `main`，主要语言为 Python，License 为 MIT。
- README 和官方文档声明其包含 CLI、gateway、tools、skills、memory、MCP、cron、terminal backends 等能力。
- 官方架构页给出入口、核心模块、数据流和推荐源码阅读顺序。

未验证：

- 未在本机执行安装命令。
- 未运行 `hermes`、`hermes doctor`、`hermes model`、`hermes tools`。
- 未克隆源码做函数级调用链验证。
- 未验证各 provider、工具、消息平台、MCP server 或远程运行后端。

## 文件清单

- [项目精读](project-analysis.md)
- [源码阅读记录](source-code-reading.md)
- [集成指南](integration-guide.md)
- [问题排查记录](troubleshooting.md)
- [Learning Todo List](learning-todo-list.md)
- [收录报告](collect-report.md)
- [图解目录](assets/diagrams/)
- [学习笔记](../../../learning-notes/NousResearch__hermes-agent/README.md)

## 图解草稿

当前图解均为 Mermaid 源文件，依据 README、GitHub API 和官方文档生成，尚未导出 PNG/SVG，也未经过源码函数级复核。

- [architecture.mmd](assets/diagrams/architecture.mmd)
- [agent-loop.mmd](assets/diagrams/agent-loop.mmd)
- [tool-and-skill-flow.mmd](assets/diagrams/tool-and-skill-flow.mmd)
- [memory-and-session-flow.mmd](assets/diagrams/memory-and-session-flow.mmd)
- [gateway-flow.mmd](assets/diagrams/gateway-flow.mmd)
- [mcp-integration-flow.mmd](assets/diagrams/mcp-integration-flow.mmd)
- [cron-scheduling-flow.mmd](assets/diagrams/cron-scheduling-flow.mmd)


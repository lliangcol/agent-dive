# Graphify 源码阅读记录

## 1. 阅读目标

- 本轮要理解的问题：Graphify 如何从项目目录构建知识图谱，并如何接入 AI 编码助手。
- 关联功能：CLI、Tree-sitter 静态解析、semantic extraction、图谱输出、Codex / Claude Code skill 安装、MCP server。
- 预期产出：确认核心模块边界、关键调用链、运行验证命令和安全边界。

## 2. 源码入口

| 入口 | 路径 | 作用 | 依据 |
|---|---|---|---|
| CLI | `graphify.__main__:main` | `graphify` 命令入口 | pyproject.toml，待源码验证 |
| MCP server | `graphify.serve:_main` | `graphify-mcp` 命令入口 | pyproject.toml，待源码验证 |
| 包目录 | `graphify/` | 核心 Python 包 | GitHub contents API |
| 文档 | `docs/`、`ARCHITECTURE.md`、`SECURITY.md` | 架构、安全和使用说明 | GitHub contents API |
| 测试 | `tests/` | 回归测试和行为样例 | GitHub contents API |

## 3. 模块地图

| 模块 | 路径 | 职责 | 依赖关系 |
|---|---|---|---|
| CLI 层 | `graphify/__main__.py` 或相邻入口文件 | 参数解析、命令分发 | 待源码验证 |
| 安装器 | `graphify/` 内 installer / skill 相关模块 | 写入不同助手平台的 skill、AGENTS、hook 配置 | 待源码验证 |
| 文件扫描 | `graphify/` 内 scan / ingest 相关模块 | 遍历项目文件、过滤路径、增量缓存 | 待源码验证 |
| 代码抽取 | `graphify/` 内 parser / tree-sitter 相关模块 | 提取函数、类、导入、调用关系 | 待源码验证 |
| 语义抽取 | `graphify/` 内 LLM / extraction 相关模块 | 处理文档、图片、转写等语义节点 | 待源码验证 |
| 图构建 | `graphify/` 内 graph 相关模块 | 构建节点、边、社区或子图查询 | 待源码验证 |
| 导出层 | `graphify/` 内 export / report 相关模块 | 生成 HTML、Markdown、JSON、GraphML、Neo4j 等输出 | 待源码验证 |
| MCP 服务 | `graphify/serve.py` 或相邻模块 | 暴露图谱查询能力 | 待源码验证 |

## 4. 推荐阅读顺序

1. `README.md`：确认官方使用路径、输出和平台支持。
2. `ARCHITECTURE.md`：先看作者定义的架构边界。
3. `SECURITY.md`：确认数据外发、hook、命令执行和敏感文件处理边界。
4. `pyproject.toml`：确认入口、extras、依赖和包数据。
5. CLI 入口：沿 `graphify.__main__:main` 看命令分发。
6. 图谱构建主线：找到扫描、解析、抽取、建图、写出文件的串联位置。
7. 平台安装器：核对 Codex / Claude Code / Cursor 等平台写入了哪些文件。
8. MCP server：确认工具接口、输入输出和图谱文件读取逻辑。
9. `tests/`：找覆盖 CLI、install、graph build、query、MCP 的回归测试。

## 5. 关键调用链

### 调用链 1：构建图谱

- 触发条件：执行 `graphify .`。
- 起点：`graphify.__main__:main`，待源码确认。
- 关键步骤：解析路径和 backend 参数 -> 扫描文件 -> Tree-sitter 本地抽取代码结构 -> 对 docs、PDF、图片等非代码材料做语义抽取 -> 构建图 -> 写出 `graphify-out/`。
- 终点：`graph.html`、`GRAPH_REPORT.md`、`graph.json`。
- 输入：项目目录、可选 backend、可选 extras 能力。
- 输出：图谱文件和报告。
- 错误处理：待源码确认，包括依赖缺失、非代码语义抽取 API key 缺失、解析失败、缓存损坏。
- 依据：README、Privacy 说明和 pyproject.toml。

### 调用链 2：安装 Codex 集成

- 触发条件：执行 `graphify install --platform codex` 或 `graphify install --project --platform codex`。
- 起点：安装命令分发，待源码确认。
- 关键步骤：检测平台 -> 生成 Codex 指令块 -> 写入 `AGENTS.md` 或项目级配置 -> 写入 `.codex/hooks.json`。
- 终点：后续 Codex 搜索/读取前被提醒优先查询图谱。
- 输入：平台参数、是否 project-scoped。
- 输出：助手配置文件。
- 错误处理：待验证已有文件合并、卸载、权限不足、重复安装。
- 依据：README Codex 安装说明。

### 调用链 3：MCP 查询

- 触发条件：启动 `graphify-mcp` 并由支持 MCP 的 Agent 调用。
- 起点：`graphify.serve:_main`，待源码确认。
- 关键步骤：加载图谱 -> 注册工具 -> 接收查询 -> 返回相关节点、边或报告片段。
- 终点：Agent 使用更小上下文回答代码库问题。
- 输入：MCP 请求和图谱路径。
- 输出：查询结果。
- 错误处理：待源码确认。
- 依据：pyproject.toml 和 README extras。

## 6. 阅读笔记

- 重要发现：Graphify 的关键学习点不是单一算法，而是“静态代码图 + 语义抽取 + Agent 工作流注入 + 查询输出”的组合。
- 不确定点：README 提到的平台很多，需要确认每个平台安装器是否共享一套模板，还是分别维护。
- 待运行验证：安装包、构建小仓库图谱、打开 HTML、查询 JSON、验证 Codex project install 写入范围。

## 待办检查项

- [ ] 找到入口文件。
- [ ] 找到图谱构建主流程。
- [ ] 找到 LLM backend 配置和调用位置。
- [ ] 找到 Tree-sitter parser 注册和语言支持表。
- [ ] 找到 MCP server 工具定义。
- [ ] 找到 Codex 安装器写入逻辑。
- [ ] 检查安全边界和敏感文件过滤。

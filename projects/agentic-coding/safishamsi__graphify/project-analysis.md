# Graphify 项目精读

## 1. 项目基本信息

- 项目名称：Graphify
- 项目 ID：`safishamsi__graphify`
- GitHub：https://github.com/safishamsi/graphify
- 项目主页：https://graphifylabs.ai/（GitHub API homepage / README 链接）
- 分类：`agentic-coding`
- 收录等级：Level B 标准收录
- 当前状态：`analyzing`
- 主要语言：Python
- License：MIT
- 分析日期：2026-06-10
- 分析版本 / Commit：`5504c84324fc9249eb4c9d0cca86da7140250032`
- 默认分支：`v8`
- 是否运行验证：否
- 分析依据：GitHub README、GitHub API、`git ls-remote --symref`、GitHub contents API、pyproject.toml；未做本机安装和源码调用链验证。

## 2. 一句话定位

Graphify 是一个给 AI 编码助手使用的项目知识图谱构建与查询工具，用图谱化上下文替代大范围全文读取和临时搜索。

## 3. 项目解决的问题

AI 编码 Agent 在真实仓库中经常需要理解模块关系、调用关系、文档背景、数据库 schema、基础设施配置和多媒体材料。直接把大量文件塞进上下文会浪费 token，也容易让 Agent 只基于局部 grep 结果做判断。

Graphify 的学习价值在于：

- 代码库理解：把函数、类、导入、调用、文档概念等整理成图谱。
- 上下文工程：让 Agent 查询相关子图，而不是读取整个仓库。
- 编码助手集成：通过 skill、AGENTS.md、hook 或命令把图谱查询纳入工作流。
- 多模态知识组织：除代码外，还覆盖文档、PDF、图片、视频和音频转写等材料。

依据：README 和 GitHub 仓库描述；具体实现边界待源码验证。

## 4. 项目主线

基于 README，典型使用主线如下：

1. 用户安装 PyPI 包 `graphifyy`，CLI 命令为 `graphify`。
2. 用户在项目目录运行 `graphify install` 或平台专用安装命令，把 Graphify skill / 指令 / hook 写入目标 AI 助手环境。
3. 用户让助手执行 `/graphify .` 或 Codex 场景中的 `$graphify`。
4. Graphify 扫描目标目录，构建知识图谱。
5. 生成 `graphify-out/graph.html`、`graphify-out/GRAPH_REPORT.md`、`graphify-out/graph.json`。
6. 后续代码库问题通过图谱查询、报告或 MCP server 等方式辅助回答。

未验证：上述步骤尚未在本机执行，具体 CLI 参数和输出文件内容待运行确认。

## 5. 快速开始

- 环境要求：Python 3.10+；README 推荐 `uv`，也支持 `pipx` 或 `pip`。
- 推荐安装：`uv tool install graphifyy`。
- 注册助手 skill：`graphify install`。
- 构建当前目录图谱：README 在多数助手场景使用 `/graphify .`；PowerShell 场景应使用 `graphify .`，因为 `/` 是路径分隔符。
- 主要输出：`graph.html`、`GRAPH_REPORT.md`、`graph.json`。
- 已知限制：本仓库未执行安装和运行验证；涉及 docs、PDF、图片等非代码材料的 semantic extraction 时，需要检查 API key、网络、backend 和敏感数据边界。

## 6. 核心架构

根据 README、GitHub contents API 和 pyproject.toml，当前可确认的模块线索：

| 模块 | 作用 | 依据 | 验证状态 |
|---|---|---|---|
| CLI `graphify` | 命令行入口，执行安装、构建、导出和查询 | pyproject `[project.scripts]` 摘要 | 待源码验证 |
| Skill installer | 向 Claude Code、Codex、Cursor、Gemini CLI 等平台写入指令或 skill | README 平台安装表 | 待运行验证 |
| Code extraction | 使用 Tree-sitter 等静态分析能力提取代码结构 | README 文件处理和 Privacy 说明 | 待源码验证 |
| Semantic extraction | 对 docs、PDF、图片等非代码材料做语义抽取 | README 文件处理、optional extras 和 Privacy 说明 | 待源码验证 |
| Graph outputs | 生成 HTML、Markdown report、JSON、可选 Neo4j / MCP 等输出 | README 输出说明 | 待运行验证 |
| MCP server | 暴露 `graphify-mcp` 入口，供工具协议查询 | pyproject.toml `[project.scripts]` | 待源码验证 |

图解草稿见 `assets/diagrams/architecture.mmd`、`flow.mmd` 和 `sequence.mmd`。

## 7. 核心原理

### 知识图谱化上下文

Graphify 的核心思想是把项目材料拆成节点和关系，再让 Agent 查询相关子图。这样可以降低全量读取成本，并让代码、文档、schema、图片和转写文本有统一检索入口。

依据：README 对 `graph.json`、`GRAPH_REPORT.md`、`graph.html` 和 queryable knowledge graph 的描述。

### 静态结构抽取

README 和 pyproject.toml 显示，代码结构解析依赖 Tree-sitter，目标是提取类、函数、导入、调用关系和注释等确定性结构。该设计适合作为源码阅读入口，但不能替代人工验证关键调用链。

依据：GitHub README 和 pyproject.toml；待源码验证。

### Agent 工具集成

Graphify 不是单纯离线分析器，它重点服务 AI 编码助手。README 列出了 Claude Code、Codex、OpenCode、Cursor、Gemini CLI 等平台，并说明 Codex 通过 `AGENTS.md` 和 hook 提醒走图谱路径。

依据：README 平台安装说明；待运行验证。

### MCP 与导出

pyproject.toml 显示存在 `graphify-mcp = "graphify.serve:_main"`，README extras 也包含 `mcp` 和 `neo4j`。这说明项目不仅生成静态图，还可能作为可查询服务接入 Agent 工具生态。

依据：pyproject.toml；待源码验证。

### 数据和隐私边界

README 的 Privacy 章节明确区分了处理路径：代码文件通过 Tree-sitter 在本地抽取，code-only corpus 不需要 API key；视频 / 音频通过 faster-whisper 本地转写；docs、PDF、图片会发送到用户配置的 AI assistant / backend 做语义抽取。私有仓库使用前，重点不是笼统禁止 Graphify，而是先确认输入范围、backend、环境变量、查询日志和非代码材料是否允许外发。

依据：README Privacy 和 file handling 说明；待本机配置验证。

## 8. 源码结构

GitHub 页面显示的根目录结构：

- `.github/`：CI 或自动化配置，待检查。
- `docs/`：项目文档，包含 how-it-works 等说明。
- `graphify/`：核心 Python 包，待源码阅读。
- `tests/`：测试目录，待检查覆盖范围。
- `tools/`：辅助工具目录，待检查。
- `worked/`：示例或工作材料目录，待检查。
- `pyproject.toml`：包元数据、CLI 入口、extras 和开发依赖。
- `ARCHITECTURE.md`、`SECURITY.md`、`CHANGELOG.md`：架构、安全和变更资料入口。

待源码确认：

- CLI 主入口：`graphify.__main__:main`
- MCP server 入口：`graphify.serve:_main`
- 解析、抽取、图构建、导出、查询的真实模块边界。

## 9. 关键调用链

### 调用链 1：CLI 构建图谱

- 触发条件：用户在项目目录执行 `graphify .` 或助手触发 `/graphify .`。
- 起点：`graphify.__main__:main`，待源码确认。
- 关键步骤：解析参数 -> 扫描文件 -> 静态结构抽取 -> 语义抽取 -> 构建图 -> 写出 `graphify-out/`。
- 终点：生成 `graph.html`、`GRAPH_REPORT.md`、`graph.json`。
- 依据：README 和 pyproject.toml。
- 状态：待源码和运行验证。

### 调用链 2：Codex 集成提醒

- 触发条件：执行 `graphify install --platform codex` 或类似安装。
- 起点：安装命令，待源码确认。
- 关键步骤：写入 AGENTS 指令 -> 写入 Codex hook 配置 -> 后续搜索类操作前提醒优先查询图谱。
- 终点：Codex 工作流中优先走 Graphify 查询。
- 依据：README Codex 安装说明。
- 状态：待运行验证。

### 调用链 3：MCP 查询

- 触发条件：安装 `mcp` extra 并启动 `graphify-mcp`。
- 起点：`graphify.serve:_main`，待源码确认。
- 关键步骤：读取图谱文件 -> 暴露查询工具 -> Agent 调用工具获取相关节点、边或报告片段。
- 终点：Agent 获得更小的上下文。
- 依据：pyproject.toml 和 README extras。
- 状态：待源码和运行验证。

## 10. 集成方式

适合先做三种集成实验：

1. 本地仓库静态图谱：选一个小型示例仓库执行 `graphify .`，检查输出文件和查询质量。
2. Codex 工作流集成：执行 `graphify install --platform codex --project`，确认写入的 `AGENTS.md` 和 hook 配置。
3. MCP 查询集成：安装 `graphifyy[mcp]`，验证 `graphify-mcp` 或 README 中的 `--mcp` / query 命令是否能读取图谱并响应查询。

Java / Spring Boot 项目的集成重点不是 SDK 嵌入，而是把 Java 仓库作为输入材料，生成图谱后用于架构理解、调用链定位和知识问答。

## 11. 问题排查

优先排查方向：

- PowerShell 命令差异：不要在 PowerShell 中使用 `/graphify .`，应直接执行 `graphify .`。
- 包名与命令名不同：PyPI 包名是 `graphifyy`，CLI 命令仍是 `graphify`。
- PATH 问题：优先使用 `uv tool install` 或 `pipx install`，避免 plain `pip` 后命令不可见。
- 敏感数据边界：代码 AST 路径按 README 为本地处理；docs、PDF、图片等非代码材料执行 semantic extraction 前，应确认哪些内容会发往外部模型或 assistant backend。
- 生成图谱不准：先区分静态代码抽取、文档语义抽取、报告总结和查询策略，不要把报告当作源码事实。

## 12. 客观评价

### 优点

- 面向真实 AI 编码助手工作流，不只是离线可视化工具。
- 支持代码、文档、SQL schema、基础设施和多模态材料统一建图。
- 输出包含 HTML、Markdown report 和 JSON，兼顾人读、可视化和机器查询。
- 有明确的 Codex、Claude Code、Cursor、Gemini CLI 等平台集成路径。
- MIT License，适合学习和二次研究。

### 缺点

- 能力范围很大，初学者容易停留在 README 级理解。
- 涉及多平台安装、hook、LLM backend、MCP、Neo4j 和多模态依赖，验证成本不低。
- README 的平台和功能列表更新快，文档与源码可能存在版本漂移，需要按 commit 验证。
- 对敏感仓库中的 docs、PDF、图片等非代码材料使用 semantic extraction 前必须确认数据外发边界。

### 适用场景

- 学习代码库知识图谱和上下文压缩。
- 给 Codex / Claude Code 等编码助手建立仓库级知识入口。
- 对大型仓库做架构探索、模块关系梳理和文档生成辅助。
- 研究 MCP server 如何服务于代码理解类工具。

### 不适用场景

- 需要直接替代源码审查或安全审计。
- 无法接受外部模型或 assistant backend 处理的敏感项目，除非明确只处理本地 AST / 本地转写路径，或显式选择本地 backend。
- 只想要轻量 grep 或单文件问答的小任务。
- 尚未验证 hook 和安装写入行为的生产仓库。

## 13. Learning Todo List

见 [learning-todo-list.md](learning-todo-list.md)。建议先完成 Level 1 到 Level 2，再进入源码级验证。

## 14. 总结

Graphify 值得收录为 `agentic-coding` 方向的 Level B 项目。它把代码库理解、知识图谱、Agent 工具集成和上下文工程连接在一起，适合作为“AI 编码助手如何更稳地理解大型项目”的学习样例。

下一步应执行本机最小运行验证，并源码确认 CLI 构建、Codex 安装、MCP server 和 semantic extraction 的真实边界。

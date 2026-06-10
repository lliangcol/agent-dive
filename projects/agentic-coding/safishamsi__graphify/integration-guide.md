# Graphify 集成指南

## 1. 集成目标

- 目标系统：本地代码仓库和 AI 编码助手。
- 目标能力：为编码助手提供可查询的项目知识图谱，减少全文读取和临时搜索。
- 集成方式：CLI 生成图谱；按平台安装 skill / 指令 / hook；可选 MCP server。
- 约束条件：当前文档未做本机运行验证，所有命令需在独立测试仓库先验证。

## 2. 前置条件

- 运行环境：Python 3.10+。
- 依赖：README 推荐 `uv`；也可用 `pipx`。
- 模型或服务配置：代码 AST 抽取按 README 为本地路径；docs、PDF、图片等非代码材料的 semantic extraction 可能需要 OpenAI、Anthropic、Gemini、Bedrock、Azure、Ollama 或 Claude CLI 等 backend 配置。
- 权限要求：对目标仓库有读权限；project-scoped install 会写入仓库配置文件，执行前应检查工作树。

## 3. 最小集成路径

### 路径 A：只生成本地图谱

1. 在测试仓库安装工具：`uv tool install graphifyy`。
2. 在目标目录执行：`graphify .`。
3. 检查 `graphify-out/graph.html`、`graphify-out/GRAPH_REPORT.md`、`graphify-out/graph.json`。
4. 用一个代码库问题测试报告是否能定位相关模块。
5. 记录命令输出、耗时、错误和生成文件大小。

状态：待运行验证。

### 路径 B：Codex 项目级集成

1. 先保存目标仓库工作树状态。
2. 执行：`graphify install --project --platform codex`。
3. 检查写入的 `AGENTS.md`、`.codex/hooks.json` 或 README 所述配置。
4. 在 Codex 中提出一个代码定位问题，确认是否优先使用 Graphify 查询路径。
5. 记录生成配置和卸载方式。

状态：待运行验证。

### 路径 C：MCP 集成

1. 安装 MCP extra：`uv tool install "graphifyy[mcp]"`。
2. 构建一次图谱。
3. 启动或配置 `graphify-mcp`，或按 README 使用 `graphify . --mcp` / query 相关命令。
4. 让支持 MCP 的 Agent 查询一个具体函数、模块或架构问题。
5. 检查返回内容是否可追溯到图谱。

状态：待源码和运行验证。

## 4. 接口与数据流

| 输入 | 处理模块 | 输出 | 备注 |
|---|---|---|---|
| 项目目录 | CLI / scanner | 待解析文件集合 | 需确认 ignore 规则 |
| 源码文件 | Tree-sitter 静态抽取 | 类、函数、导入、调用、注释节点 | README 依据，待源码确认 |
| 文档 / PDF / 图片 | semantic extraction | 概念节点和语义关系 | 可能调用外部模型或 assistant backend |
| 视频 / 音频 | faster-whisper 转写后入图 | 转写文本和相关节点 | README 称转写本地执行，仍需验证依赖和输出范围 |
| 图谱数据 | exporter | HTML、Markdown、JSON | README 明确列出 |
| 图谱文件 | MCP server / query | 子图或相关上下文 | 待验证 |
| 平台参数 | installer | skill / AGENTS / hook 配置 | 写入范围必须检查 |

## 5. Java / Spring Boot 集成关注点

Graphify 更适合作为外部代码库理解工具，而不是直接嵌入 Spring Boot 运行时。

- Bean 生命周期：不涉及应用内 Bean，除非后续自行封装查询服务。
- 配置管理：Graphify 配置应与业务应用配置分离，避免混入生产密钥。
- 权限和审计：不要让 Agent 在未审计情况下读取敏感代码、配置或数据库 dump。
- 日志和链路追踪：记录 Graphify 运行命令、版本、commit 和输入范围。
- 超时、重试和限流：非代码语义抽取调用外部模型时需要限制成本和失败重试。
- 数据库或消息队列：可把 SQL schema 作为输入材料分析，但不能代替真实数据库权限审计。

## 6. 集成风险

- 依赖版本：Python、uv/pipx、Tree-sitter extras、多模态 extras 可能影响安装。
- 模型成本：docs、PDF、图片等非代码 semantic extraction 可能产生 API 调用成本；代码-only AST 路径按 README 不需要 API key。
- 工具权限：安装 hook 或助手配置会改变 Agent 工作流，必须可审计、可回滚。
- 数据安全：确认代码、文档、图片、视频和转写内容分别走本地路径还是外部模型 / assistant backend。
- 运行稳定性：大型仓库首轮图谱构建可能耗时，需要缓存和增量策略验证。

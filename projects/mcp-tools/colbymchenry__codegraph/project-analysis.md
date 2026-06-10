# CodeGraph 项目精读

## 1. 项目基本信息

- 项目名称：CodeGraph
- 项目 ID：`colbymchenry__codegraph`
- GitHub：https://github.com/colbymchenry/codegraph
- 官方文档：https://colbymchenry.github.io/codegraph/
- 分类：`mcp-tools`
- 收录等级：Level A 深度收录
- 当前状态：`analyzing`
- 主要语言：TypeScript
- License：MIT
- 分析日期：2026-06-10
- 分析版本 / Commit：`16c73e2b0e027411e22039baeb32fbe60ab42b4c`
- 是否运行验证：否
- 分析依据：GitHub API、README、官方文档源码、`package.json`、`src/` 源码浅读

## 2. 一句话定位

CodeGraph 是一个本地优先的代码知识图谱和 MCP 工具层，让 AI 编码 Agent 通过预索引的符号、调用关系、文件结构和源码片段理解代码库，而不是每次从 grep/read 文件开始探索。

## 3. 项目解决的问题

AI 编码 Agent 在陌生仓库中通常需要反复列目录、搜索、读文件、追调用链，这会消耗大量 token 和工具调用，也容易漏掉跨文件、跨语言或动态分发关系。CodeGraph 的做法是先用 tree-sitter 和解析器把代码库转成 `.codegraph/codegraph.db`，再通过 CLI 和 MCP tools 提供结构化查询。

学习价值主要在三类：

- MCP 工具如何为 Agent 提供可检索、可追踪、可编辑前评估的代码上下文。
- 静态代码索引如何从文件扫描、AST 提取、SQLite 存储、引用解析走到调用图和影响面分析。
- 多 Agent 安装器如何把同一个 MCP server 接入 Claude Code、Codex CLI、Cursor、Gemini CLI 等不同宿主。

## 4. 项目主线

用户先安装 `codegraph` CLI，然后在目标仓库执行 `codegraph init -i` 建立本地索引。索引流程会扫描源码文件、按语言加载 tree-sitter WASM grammar、提取节点和边、写入 SQLite，再运行引用解析和框架特定解析。Agent 侧通过 `codegraph serve --mcp` 连接 MCP server，调用 `codegraph_explore`、`codegraph_search`、`codegraph_callers`、`codegraph_callees`、`codegraph_impact`、`codegraph_node`、`codegraph_files`、`codegraph_status` 等工具获取上下文。

依据：README 的 Get Started、How It Works、MCP Tools；源码 `src/bin/codegraph.ts`、`src/index.ts`、`src/extraction/index.ts`、`src/mcp/tools.ts`、`src/mcp/engine.ts`。

## 5. 快速开始

- 环境要求：README 提供 shell/PowerShell 安装器；npm 包的 `package.json` 标注 Node `>=20.0.0 <25.0.0`，README 的 Library Usage 另外提示嵌入式 API 依赖 Node 22.5+ 的 `node:sqlite`。
- 安装步骤：

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.sh | sh

# Windows PowerShell
irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 | iex

# 或 npm
npm i -g @colbymchenry/codegraph
```

- Agent 接入：

```bash
codegraph install
```

- 项目初始化：

```bash
cd your-project
codegraph init -i
```

- 最小查询：

```bash
codegraph status
codegraph query UserService --kind class --limit 10
codegraph callers handleRequest --json
```

- 已知限制：本次未安装和运行，以上为 README/CLI 文档级步骤；实际 Windows PATH、生效 shell、agent 配置写入和项目索引耗时需要单独验证。

## 6. 核心架构

CodeGraph 可以拆成六层：

- CLI 层：`src/bin/codegraph.ts` 定义安装、初始化、索引、同步、状态、查询、调用链、影响面、MCP server 等命令。
- 安装器层：`src/installer/` 负责检测和写入不同 Agent 的 MCP 配置，目标注册在 `src/installer/targets/registry.ts`。
- 核心 facade：`src/index.ts` 的 `CodeGraph` 类组织数据库连接、提取器、解析器、图查询、上下文构建和文件 watcher。
- 提取层：`src/extraction/` 负责文件扫描、语言检测、tree-sitter WASM grammar 加载、AST 节点和边提取。
- 图存储和查询层：`src/db/schema.sql` 定义 nodes、edges、files、unresolved_refs、FTS5 等表；`src/graph/` 提供 traversal 和 query manager。
- MCP 层：`src/mcp/engine.ts` 管理共享 CodeGraph 实例和 watcher；`src/mcp/tools.ts` 定义 MCP tools、参数校验、输出预算和 staleness/worktree 提示。

图解见 `assets/diagrams/architecture.mmd`。

## 7. 核心原理

### 7.1 预索引知识图谱

CodeGraph 的核心不是在线搜索，而是先离线建立项目级 SQLite 知识图谱。`src/db/schema.sql` 中的 `nodes` 表保存函数、类、方法、变量等符号，`edges` 表保存 calls、references、imports、extends、implements 等关系，`files` 表保存文件 hash 和语言信息，FTS5 用于全文符号搜索。

### 7.2 AST 提取与语言支持

`src/extraction/grammars.ts` 用文件扩展名映射语言，按需加载 tree-sitter WASM grammar。README 标称支持 20+ 语言，源码中还包括 Vue、Svelte、Liquid、Razor、YAML/properties 等特殊处理路径。

### 7.3 引用解析

`src/resolution/index.ts` 聚合 import 解析、名称匹配、框架 resolver、callback synthesizer、路径 alias、Go module 和 workspace package 等信息，把提取阶段的 unresolved references 解析成跨文件关系。源码注释明确说明跨文件 resolution 是 best-effort，遇到歧义可能返回多个候选。

### 7.4 Agent 工具层

MCP tools 的主入口是 `codegraph_explore`，目标是一次返回相关符号的源码片段、关系和影响信息。工具层还提供 search、callers、callees、impact、node、files、status。`src/mcp/server-instructions.ts` 将工具使用策略通过 MCP initialize response 提供给客户端，当前 README 和源码都说明新版不再把这套说明写入 `CLAUDE.md` / `AGENTS.md`。

### 7.5 自动同步

`src/index.ts` 的 `watch()` 通过 `FileWatcher` 触发增量 `sync()`，`src/mcp/engine.ts` 在 MCP server 初始化后启动 watcher，并在首次工具调用前做 catch-up sync。README 说明 watcher 使用 FSEvents / inotify / ReadDirectoryChangesW，默认 debounce 约 2 秒。

## 8. 源码结构

- 入口文件：`src/bin/codegraph.ts`
- 核心 facade：`src/index.ts`
- MCP server：`src/mcp/`
- 提取器：`src/extraction/`
- 解析器：`src/resolution/`
- 图查询：`src/graph/`
- 数据库：`src/db/`
- 安装器：`src/installer/`
- 同步机制：`src/sync/`
- 测试目录：`__tests__/`
- 文档站：`site/src/content/docs/`
- 构建配置：`package.json`、`tsconfig.json`、`vitest.config.ts`

## 9. 关键调用链

### 调用链 1：初始化与全量索引

- 触发条件：用户执行 `codegraph init -i` 或 `codegraph index`
- 起点：`src/bin/codegraph.ts`
- 关键步骤：CLI 解析命令 -> `CodeGraph.init()` / `CodeGraph.open()` -> `indexAll()` -> `ExtractionOrchestrator.indexAll()` -> `resolveReferencesBatched()` -> 写入 nodes/edges/files metadata
- 输出：`.codegraph/codegraph.db` 和索引统计
- 错误处理：文件锁避免并发索引；解析超时、无效 `.gitignore`、大文件和默认忽略目录都有保护逻辑
- 依据：`src/bin/codegraph.ts`、`src/index.ts`、`src/extraction/index.ts`

### 调用链 2：Agent 提问到 MCP 探索结果

- 触发条件：Agent 调用 `codegraph_explore`
- 起点：`src/mcp/tools.ts`
- 关键步骤：MCP tool 参数校验 -> `ToolHandler.handleExplore()` -> 获取 `CodeGraph` 实例 -> `findRelevantContext()` -> 按文件聚合节点 -> 预算裁剪 -> 返回源码片段和关系提示
- 输出：面向 Agent 的 Markdown 文本结果
- 错误处理：输入长度限制、路径校验、输出预算、staleness banner、worktree mismatch notice
- 依据：`src/mcp/tools.ts`、`src/mcp/engine.ts`、`src/index.ts`

### 调用链 3：安装器接入多个 Agent

- 触发条件：用户执行 `codegraph install`
- 起点：`src/installer/index.ts`
- 关键步骤：检测可用目标 -> 解析 `--target` -> 选择 global/local -> 每个 target 写入 MCP 配置 -> 可选设置 Claude auto-allow -> local 模式初始化项目
- 输出：Claude/Cursor/Codex/opencode/Hermes/Gemini/Antigravity/Kiro 对应配置
- 错误处理：目标不支持 local 时跳过并提示；Codex 只支持 global；旧 instructions block 会被清理
- 依据：`src/installer/index.ts`、`src/installer/targets/registry.ts`、`src/installer/targets/codex.ts`、`src/installer/targets/claude.ts`

## 10. 集成方式

### CLI / MCP 集成

最直接的集成是把 CodeGraph 作为独立 CLI 和 MCP Server：安装 CLI，运行 `codegraph install` 写入 agent 配置，在每个目标项目执行 `codegraph init -i`。

### SDK / 嵌入式集成

README 提供 `import CodeGraph from '@colbymchenry/codegraph'` 的 Library Usage，可在 Node 进程中调用 `CodeGraph.init()`、`indexAll()`、`searchNodes()`、`getCallers()`、`buildContext()`、`getImpactRadius()`、`watch()` 等 API。该路径适合 Electron 或自建开发工具，但需要单独验证 Node 版本和 SQLite backend。

### Java / Spring Boot 关系

CodeGraph 不是 Java/Spring Boot 库。Java 项目中更合适的方式是作为外部 CLI/MCP 索引器使用，让 Agent 或 CI 脚本通过 `codegraph affected`、`codegraph impact` 辅助变更影响面判断。

## 11. 问题排查

详见 [troubleshooting.md](troubleshooting.md)。首轮重点包括 PATH 未生效、项目未初始化、Node 版本不兼容、watcher 不可用、索引过期、文档与源码表述漂移。

## 12. 客观评价

### 优点

- 与 Agent 工作流高度贴合，MCP tools 覆盖搜索、探索、调用关系、影响面和文件结构。
- 本地 SQLite 和本地解析，默认不需要外部服务或 API key。
- TypeScript 源码结构清晰，CLI、installer、MCP、extraction、resolution、graph 分层明确。
- 多语言和多 Agent 覆盖面广，适合学习 MCP 工具产品化。
- 测试目录覆盖面广，包括 installer、MCP、sync、framework routes、bridge、search、security 等主题。

### 缺点

- 静态解析对动态调用、运行时反射、框架魔法和跨语言桥接只能做到 best-effort。
- 对 Agent 的收益依赖 Agent 是否真的优先使用 CodeGraph tools；如果继续 grep/read，收益会下降。
- 支持语言和框架多，维护复杂度高，具体语言的精度需要逐项验证。
- README benchmark 未在本次收录复跑，不能作为本地实测结论。

### 适用场景

- 大中型代码库的 Agent 辅助代码阅读、影响面分析、重构前定位。
- 希望把本地代码索引通过 MCP 暴露给多个 AI 编码工具。
- 学习 MCP server、代码图谱、AST 提取、引用解析和 Agent 工具设计。

### 不适用场景

- 需要运行时真实调用链、生产 trace 或性能 profiling 的场景。
- 不允许在项目目录生成 `.codegraph/` 索引文件的受限环境。
- 只处理文档、配置、二进制或非源码资产的仓库。

## 13. Learning Todo List

详见 [learning-todo-list.md](learning-todo-list.md)。

## 14. 总结

CodeGraph 值得作为 Level A 深度收录项目：它既是 MCP 工具体系的代表，也展示了静态代码知识图谱如何服务 Agentic Coding。下一轮学习应优先真实跑通 `codegraph init -i`、检查生成 DB 和 MCP tools 返回，再复核 `codegraph_explore` 与普通 grep/read 在一个本地中型仓库上的差异。

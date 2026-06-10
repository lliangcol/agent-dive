# CodeGraph 源码阅读记录

## 1. 阅读目标

- 本轮要理解的问题：CodeGraph 如何把代码库变成 Agent 可用的本地知识图谱。
- 关联功能：CLI 初始化、索引、MCP tools、自动同步、多 Agent 安装器。
- 预期产出：模块地图、推荐阅读顺序、关键调用链和待验证问题。

## 2. 源码入口

| 入口 | 路径 | 作用 | 依据 |
|---|---|---|---|
| CLI | `src/bin/codegraph.ts` | 定义 `init`、`index`、`sync`、`status`、`query`、`serve --mcp`、`install` 等命令 | 源码 |
| 核心 facade | `src/index.ts` | 暴露 `CodeGraph` 类，组织 DB、提取、解析、图查询、watcher | 源码 |
| MCP tools | `src/mcp/tools.ts` | 定义 `codegraph_explore` 等 MCP 工具和工具处理逻辑 | 源码 |
| MCP engine | `src/mcp/engine.ts` | 维护共享 CodeGraph 实例、watcher 和 tool handler | 源码 |
| 安装器 | `src/installer/index.ts` | 多 Agent 检测、配置写入和项目初始化 | 源码 |

## 3. 模块地图

| 模块 | 路径 | 职责 | 依赖关系 |
|---|---|---|---|
| CLI | `src/bin/` | 用户命令入口、版本和运行时检查 | 调用 `src/index.ts`、`src/installer/`、`src/mcp/` |
| Core | `src/index.ts` | 项目生命周期、索引、同步、搜索、图查询、watch | 组合 DB、extraction、resolution、graph、context、sync |
| Extraction | `src/extraction/` | 扫描文件、语言检测、tree-sitter 解析、提取节点/边 | 写入 QueryBuilder，依赖 tree-sitter WASM |
| Resolution | `src/resolution/` | 引用解析、import/name matching、framework resolver、callback edge | 读取 nodes/unresolved refs，写入 edges |
| DB | `src/db/` | SQLite schema、连接、查询封装 | 被 Core、Graph、Resolution、MCP 共享 |
| Graph | `src/graph/` | BFS/DFS、caller/callee、impact、依赖图查询 | 基于 QueryBuilder |
| MCP | `src/mcp/` | MCP server、tools、session、daemon、server instructions | 打开 CodeGraph，返回 Agent 工具结果 |
| Installer | `src/installer/` | 写入 Claude/Codex/Cursor/Gemini 等配置 | 目标实现位于 `targets/` |
| Sync | `src/sync/` | file watcher、git hook、worktree 检测 | 被 Core 和 MCP engine 调用 |
| Tests | `__tests__/` | 单元、集成、MCP、installer、framework、security 等测试 | Vitest |

## 4. 推荐阅读顺序

1. `README.md`：先理解产品定位、工具列表、安装和索引流程。
2. `package.json`：确认 CLI bin、构建命令、测试命令、运行时版本。
3. `src/bin/codegraph.ts`：从 CLI 命令入口建立全局地图。
4. `src/index.ts`：理解 `CodeGraph` 类如何串联索引、同步、解析、查询。
5. `src/extraction/grammars.ts` 和 `src/extraction/index.ts`：看语言支持、扫描规则和提取流程。
6. `src/db/schema.sql`：看图谱数据模型。
7. `src/resolution/index.ts`：理解 unresolved refs 如何变成跨文件边。
8. `src/mcp/tools.ts` 和 `src/mcp/server-instructions.ts`：理解 Agent 如何消费图谱。
9. `src/installer/targets/`：理解不同 Agent 的配置差异。
10. `__tests__/integration/` 和 MCP 相关测试：验证实现假设。

## 5. 关键调用链

### 调用链 1：`codegraph init -i`

- 触发条件：用户初始化项目并要求立即索引。
- 起点：`src/bin/codegraph.ts` 的 `init [path]` 命令。
- 关键步骤：
  1. 解析项目路径，检查是否已初始化。
  2. 调用 `CodeGraph.init(projectPath, { index: false })` 创建 `.codegraph/` 和 DB。
  3. 若带索引参数，调用 `indexAll()`。
  4. `ExtractionOrchestrator` 扫描源码、加载 grammar、提取 nodes/edges/unresolved refs。
  5. `ReferenceResolver` 批量解析引用并补充 calls/imports/extends 等边。
  6. 写入索引版本和提取版本 metadata。
- 终点：本地 `.codegraph/codegraph.db` 可被 CLI/MCP 查询。
- 输入：项目路径、索引选项。
- 输出：索引统计、SQLite 图谱。
- 错误处理：文件锁、防并发、忽略默认依赖目录、解析超时、无效 `.gitignore` 容错。
- 依据：`src/bin/codegraph.ts`、`src/index.ts`、`src/extraction/index.ts`。

### 调用链 2：`codegraph_explore`

- 触发条件：Agent 问“某个模块如何工作”或编辑前需要上下文。
- 起点：`src/mcp/tools.ts` 的 `ToolHandler.execute()` 分发到 `handleExplore()`。
- 关键步骤：
  1. 校验 query、projectPath、maxFiles。
  2. 获取默认或指定项目的 `CodeGraph` 实例。
  3. 根据项目文件数选择输出预算。
  4. 调用 `findRelevantContext()` 找到相关子图。
  5. 对 named symbols 做补充 seed，按文件聚合节点。
  6. 过滤低价值测试/图标/i18n 文件，裁剪源码片段。
  7. 添加关系、完整性提示、staleness/worktree notice。
- 终点：返回 Agent 可直接使用的 Markdown 工具结果。
- 输入：自然语言 query 或符号/文件名集合。
- 输出：相关源码、关系图、未展示文件、预算提示。
- 错误处理：输入长度上限、输出长度上限、路径校验、pending sync 提示。
- 依据：`src/mcp/tools.ts`。

### 调用链 3：MCP server 启动和共享引擎

- 触发条件：Agent 配置启动 `codegraph serve --mcp`。
- 起点：CLI `serve` 命令和 `src/mcp/engine.ts`。
- 关键步骤：
  1. MCP server 启动后创建 `MCPEngine`。
  2. `ensureInitialized()` 从当前目录向上查找 `.codegraph/`。
  3. 打开 `CodeGraph` DB，设置默认实例。
  4. 启动 watcher，做 catch-up sync。
  5. 多个 session 共享同一个 engine 和 SQLite WAL。
- 终点：MCP tools 可以查询同一个项目索引。
- 输入：当前工作目录或显式 projectPath。
- 输出：共享 ToolHandler 和 CodeGraph 实例。
- 错误处理：未初始化时保留重试语义；打开失败写 stderr；watcher 不可用时提示运行 sync。
- 依据：`src/mcp/engine.ts`。

### 调用链 4：多 Agent 安装

- 触发条件：用户执行 `codegraph install`。
- 起点：`src/installer/index.ts`。
- 关键步骤：
  1. 解析 `--target` 或交互选择。
  2. `detectAll()` 检测支持的 Agent。
  3. 选择 global/local 配置位置。
  4. 对每个 target 调用 `install()`。
  5. 写入 MCP server 配置；Claude 可写 permissions；旧 instructions block 被清理。
- 终点：Agent 下次启动时可以加载 CodeGraph MCP。
- 输入：target、location、autoAllow、yes 等选项。
- 输出：各 Agent 配置文件变更。
- 错误处理：Codex 不支持 local；未知 target 抛错；写入使用原子写。
- 依据：`src/installer/index.ts`、`src/installer/targets/registry.ts`、`src/installer/targets/codex.ts`、`src/installer/targets/claude.ts`。

## 6. 阅读笔记

- 重要发现：当前版本把 Agent 工具指导放在 MCP initialize response，不再依赖写入 `CLAUDE.md` / `AGENTS.md`。这对避免重复系统提示和跨 Agent 一致性很关键。
- 重要发现：`codegraph_explore` 不是简单搜索，它包含 adaptive output budget、named symbol seeding、低价值文件过滤、staleness 提示和输出截断策略。
- 重要发现：索引 freshness 由 watcher、connect-time catch-up、manual sync 三层共同维护。
- 不确定点：不同语言 extractor 的准确率未逐项验证。
- 不确定点：README benchmark 未复跑，不能确认本机或不同模型下收益。
- 待运行验证：安装 CLI、对一个中型 TypeScript 项目执行 `codegraph init -i`、比较 MCP tools 输出和普通文件搜索结果。

## 待办检查项

- [x] 找到入口文件。
- [x] 找到主流程或任务调度主线。
- [x] 明确模型调用位置不适用：本项目不是模型调用框架，核心是 MCP 工具和代码索引。
- [x] 找到工具注册和执行位置。
- [x] 找到上下文管理和 MCP 指令位置。
- [ ] 运行验证 CLI 和 MCP server。
- [ ] 复核完整测试套件。

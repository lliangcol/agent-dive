# CodeGraph 集成指南

## 1. 集成目标

- 目标系统：AI 编码 Agent 和本地代码仓库。
- 目标能力：让 Agent 使用本地预索引代码图谱进行搜索、源码探索、调用链和影响面分析。
- 集成方式：CLI + MCP Server；可选 Node SDK 嵌入。
- 约束条件：本次收录未运行验证，以下步骤来自 README、官方文档和源码。

## 2. 前置条件

- 操作系统：Windows、macOS、Linux 均在 README 支持范围内。
- CLI 依赖：可使用自包含安装器；npm 路径需要 Node，`package.json` 标注 `>=20.0.0 <25.0.0`。
- Agent：Claude Code、Cursor、Codex CLI、opencode、Hermes Agent、Gemini CLI、Antigravity IDE、Kiro 之一。
- 权限要求：需要写入用户级或项目级 Agent MCP 配置；项目目录会生成 `.codegraph/`。
- 安全要求：索引包含源码结构和源码片段，虽然 README 标称本地运行，仍需避免把 `.codegraph/` 当作可公开发布资产。

## 3. 最小集成路径

### 3.1 安装 CLI

```powershell
irm https://raw.githubusercontent.com/colbymchenry/codegraph/main/install.ps1 | iex
```

或：

```bash
npm i -g @colbymchenry/codegraph
```

验证：

```bash
codegraph --version
```

### 3.2 配置 Agent

```bash
codegraph install
```

非交互示例：

```bash
codegraph install --yes
codegraph install --target=codex --yes
codegraph install --target=claude,cursor --location=local
```

注意：源码显示 Codex CLI target 只支持 global 配置。

### 3.3 初始化项目索引

```bash
cd your-project
codegraph init -i
codegraph status
```

### 3.4 Agent 使用路径

Agent 启动后由 MCP 配置运行：

```bash
codegraph serve --mcp
```

常用工具：

- `codegraph_explore`：理解区域或编辑前获取上下文。
- `codegraph_search`：查找符号位置。
- `codegraph_callers` / `codegraph_callees`：追调用关系。
- `codegraph_impact`：评估修改影响。
- `codegraph_node`：读取单个符号或索引文件源码。
- `codegraph_files`：查看索引文件结构。
- `codegraph_status`：检查索引健康。

## 4. 接口与数据流

| 输入 | 处理模块 | 输出 | 备注 |
|---|---|---|---|
| 源码文件 | `src/extraction/` | nodes、edges、files、unresolved refs | tree-sitter WASM 和特殊 extractor |
| unresolved refs | `src/resolution/` | calls/imports/extends/references 等边 | best-effort 静态解析 |
| Agent query | `src/mcp/tools.ts` | Markdown 工具结果 | 带输出预算和 staleness 提示 |
| 变更文件 | `src/sync/` | 增量索引更新 | watcher 或手动 `sync` |
| Agent install target | `src/installer/targets/` | MCP 配置文件 | target 差异由各文件处理 |

## 5. Java / Spring Boot 集成关注点

CodeGraph 不作为 Java 库嵌入 Spring Boot。建议把它当作开发侧辅助工具或 CI 辅助工具：

- Bean 生命周期：不涉及业务进程 Bean，避免把 CodeGraph DB 放进生产应用生命周期。
- 配置管理：把 `.codegraph/` 视为本地开发索引，按团队策略决定是否 gitignore。
- 权限和审计：Agent 读取源码片段前应确认 MCP 工具权限边界。
- 日志和链路追踪：CodeGraph 提供静态调用关系，不替代运行时 tracing。
- 超时、重试和限流：大仓库首次索引可能较慢，CI 使用时要设置超时。
- 数据库或消息队列：`.codegraph/codegraph.db` 是本地 SQLite，不应与业务数据库混用。

## 6. 集成风险

- 依赖版本：npm 路径受 Node 版本影响；README 和 `package.json` 对 CLI/SDK 的 Node 要求有不同上下文。
- 模型成本：CodeGraph 自身不调用模型，但 Agent 如何消费工具结果会影响 token。
- 工具权限：MCP tools 可返回源码片段，企业环境需明确 allowlist 和审计策略。
- 数据安全：索引 DB 可能包含敏感源码符号和片段，不应上传。
- 运行稳定性：watcher 在某些 sandbox/网络文件系统中可能不可用，需要 `codegraph sync`。
- 文档漂移：site docs 的 MCP Server 页仍有“installer writes instructions”的表述，当前 README 和源码显示指导从 MCP initialize response 提供。

## 7. 验证清单

- [ ] `codegraph --version`
- [ ] `codegraph init -i`
- [ ] `codegraph status`
- [ ] Agent 中看到 `codegraph_status`
- [ ] 对一个符号运行 `codegraph_explore`
- [ ] 修改源码后观察 staleness banner 或自动 sync
- [ ] 运行项目自己的 test/lint，确认 CodeGraph 只提供结构上下文，不替代真实验证

# Hermes Agent 源码阅读记录

## 1. 阅读目标

- 本轮要理解的问题：Hermes 如何把 CLI、gateway、tools、skills、memory、MCP 和 cron 接到同一个 Agent Loop。
- 关联功能：Agent Loop、Tool Calling、Memory、MCP、Gateway、Cron、Terminal Backends。
- 预期产出：关键入口表、模块地图、3 条源码调用链和后续源码验证清单。

当前状态：部分完成。已基于官方架构页和 GitHub contents API 建立阅读路线，尚未克隆源码做函数级验证。

## 2. 源码入口

| 入口 | 路径 | 作用 | 依据 |
|---|---|---|---|
| CLI | `cli.py` | 交互式终端入口之一 | 官方架构页 |
| CLI subcommands | `hermes_cli/main.py` | `hermes` 子命令入口 | 官方架构页 |
| Core Agent | `run_agent.py` | `AIAgent` 核心 conversation loop | 官方架构页 |
| Gateway | `gateway/run.py` | 消息平台 gateway runner | 官方架构页 |
| Batch | `batch_runner.py` | batch trajectory generation | 官方架构页 |
| MCP server | `mcp_serve.py` | MCP 相关服务入口，需源码确认职责 | GitHub contents API |

## 3. 模块地图

| 模块 | 路径 | 职责 | 依赖关系 |
|---|---|---|---|
| Agent internals | `agent/` | prompt assembly、context compression、model metadata、memory manager、skills commands | 被 `run_agent.py` 和入口层调用 |
| CLI | `hermes_cli/` | 命令、配置、provider auth、tools/skills config、plugins、gateway 命令 | 面向用户命令和 setup |
| Tools | `tools/` | registry、terminal、file、web、browser、MCP、delegation 等工具实现 | `model_tools.py` 负责发现和 dispatch |
| Toolsets | `toolsets.py` | 工具分组和平台 preset | 与工具配置和 registry 配合 |
| Model tools | `model_tools.py` | 工具 schema 收集和 tool call 分发 | 连接 Agent Loop 与 tools registry |
| Gateway | `gateway/` | 平台消息接入、session、delivery、pairing、hooks、status | 调用 `AIAgent` 并处理平台差异 |
| Cron | `cron/` | jobs 和 scheduler | 创建 Agent task 并投递结果 |
| Session state | `hermes_state.py`、`gateway/session.py` | SQLite + FTS5 session/state storage | Agent Loop 和 Gateway 共享 |
| Providers | `providers/`、`hermes_cli/runtime_provider.py` | provider/model 解析和运行时凭据 | 被 CLI、Gateway、Cron、ACP 共用 |
| Skills | `skills/`、`optional-skills/` | 内置和可选技能 | 通过 CLI/Agent 注入或调用 |
| Plugins | `plugins/` | memory provider、context engine 等扩展 | 通过 plugin manager 发现 |

## 4. 推荐阅读顺序

1. `README.md` 和官方 Architecture 页面，建立入口和数据流。
2. `run_agent.py`，确认 `AIAgent` 的主循环、重试、工具调用和持久化。
3. `agent/prompt_builder.py`、`agent/context_compressor.py`、`agent/prompt_caching.py`。
4. `hermes_cli/runtime_provider.py`、`hermes_cli/auth.py`、`providers/`。
5. `tools/registry.py`、`model_tools.py`、`toolsets.py`、`tools/mcp_tool.py`。
6. `hermes_state.py`、`gateway/session.py`。
7. `gateway/run.py`、`gateway/platforms/`、`gateway/delivery.py`、`gateway/pairing.py`。
8. `cron/jobs.py`、`cron/scheduler.py`。
9. `tools/environments/`，重点看 local、docker、ssh、modal、daytona、singularity 的权限边界。
10. `tests/`，寻找对应主线的回归用例。

## 5. 关键调用链

### 调用链 1：CLI Conversation Loop

- 触发条件：用户在 CLI 输入普通消息。
- 起点：`HermesCLI.process_input()`。
- 关键步骤：`AIAgent.run_conversation()` -> system prompt assembly -> provider runtime resolution -> provider API -> optional tool call -> `model_tools.handle_function_call()` -> loop。
- 终点：最终响应显示并保存 session。
- 输入：用户消息、profile/config、session history、enabled toolsets。
- 输出：assistant response、tool output、session record。
- 错误处理：待源码验证重试、fallback、interrupt 和工具异常包装。
- 依据：官方架构页。

### 调用链 2：Tool Registration and Dispatch

- 触发条件：Agent 需要向模型暴露工具 schema 或执行 tool call。
- 起点：`tools/registry.py`。
- 关键步骤：工具文件 import-time registration -> `model_tools.py` 触发 discovery/collection -> tool call dispatch -> tool implementation。
- 终点：tool result 返回 Agent Loop。
- 输入：enabled toolsets、平台配置、模型 tool call arguments。
- 输出：tool schema 或 tool result。
- 错误处理：待源码验证 availability check、dangerous command approval、MCP failures。
- 依据：官方架构页和 tools 文档。

### 调用链 3：Gateway Message

- 触发条件：平台 adapter 收到消息。
- 起点：`Adapter.on_message()`。
- 关键步骤：`GatewayRunner._handle_message()` -> authorize user -> resolve session key -> create `AIAgent` with history -> run conversation -> deliver response。
- 终点：消息平台收到回复。
- 输入：平台事件、用户身份、session key、message text。
- 输出：平台消息、session update。
- 错误处理：待源码验证 DM pairing、allowlist、delivery failure、token lock。
- 依据：官方架构页。

## 6. 阅读笔记

重要发现：

- Hermes 的核心值得从 `AIAgent` 而不是 gateway 或 CLI 开始读，因为官方架构页显示多个入口复用同一个核心 Agent。
- 工具系统采用 registry + import-time registration，适合重点分析工具 discoverability、schema 生成和执行权限。
- Memory 有两层需要区分：curated memory 文件注入 system prompt，session storage 使用 SQLite + FTS5 保存对话和检索。
- Cron 是 Agent task，不是普通 shell cron；这会影响权限、上下文和结果投递模型。

不确定点：

- `run_agent.py` 是否过大，是否需要先按类/函数切片阅读。
- skills 自改进的触发条件和持久化路径。
- MCP tool schema 包装、错误处理和动态 toolset 命名。
- terminal backend 的审批、隔离和凭据传递边界。

待运行验证：

- 克隆源码后运行静态搜索确认上述路径。
- 用只读配置运行 `hermes doctor`。
- 不启用写入型 terminal/file 工具前，不做真实任务执行。

## 待办检查项

- [x] 找到入口文件。
- [ ] 找到主流程或 Agent Loop 的函数级实现。
- [ ] 找到模型调用位置。
- [ ] 找到工具注册和执行位置。
- [ ] 找到配置、日志和错误处理位置。

## 质量检查项

- [x] 未把待验证调用关系写成源码事实。
- [x] 关键概念与官方文档命名一致。
- [x] 待读问题已明确记录。


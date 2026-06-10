# Hermes Agent 集成指南

## 1. 集成目标

- 目标系统：本地隔离学习环境。
- 目标能力：跑通 Hermes CLI 的最小对话，随后逐步验证 tools、memory、MCP、gateway 和 cron。
- 集成方式：先作为独立 CLI 产品使用，再评估 MCP client、消息平台 gateway 和只读工具扩展。
- 约束条件：不得写入真实密钥到文档；不得在未确认权限边界前启用高风险写入工具或远程执行后端。

## 2. 前置条件

- 运行环境：官方 README 支持 Linux、macOS、WSL2、Termux 和 Windows PowerShell；当前未本机验证。
- 依赖：安装器会处理 Python 3.11、uv、Node.js、ripgrep、ffmpeg、Git Bash 等依赖；具体以官方安装脚本为准。
- 模型或服务配置：需要选择 provider，可使用官方支持的 Nous Portal、OpenRouter、NovitaAI、NVIDIA NIM、OpenAI、自定义 endpoint 等。
- 权限要求：terminal/file/browser/MCP/gateway 相关能力需要单独审查权限和凭据。

## 3. 最小集成路径

建议分三阶段执行。

### 阶段 1：只读快速验证

1. 准备新的隔离 shell 或虚拟机。
2. 按官方安装说明安装 Hermes。
3. 执行 `hermes doctor`，记录输出。
4. 执行 `hermes model`，选择一个测试 provider。
5. 执行 `hermes tools`，确认默认启用工具。
6. 启动 `hermes`，只进行普通文本对话，不授权文件写入或命令执行。

### 阶段 2：工具和记忆验证

1. 只启用安全的只读工具集。
2. 验证 `memory` 和 `session_search` 是否按官方文档行为工作。
3. 验证工具调用输出是否可见、可中断、可审计。
4. 记录工具 schema、审批提示和失败输出。

### 阶段 3：MCP / Gateway / Cron 验证

1. 配置一个只读 MCP server，例如受限 filesystem 或公开 API。
2. 验证 MCP server tool discovery 和 tool filtering。
3. 选择一个消息平台测试 gateway，优先使用测试账号。
4. 创建一个低风险 cron job，只输出文本到测试平台。
5. 检查 session、memory、delivery 和日志边界。

## 4. 接口与数据流

| 输入 | 处理模块 | 输出 | 备注 |
|---|---|---|---|
| CLI 文本消息 | `cli.py` / `hermes_cli/` -> `AIAgent` | 终端响应、session record | 官方架构页依据 |
| 平台消息 | `gateway/platforms/` -> `GatewayRunner` -> `AIAgent` | 平台回复、session record | 需要授权和 pairing |
| Tool call | `model_tools.py` -> `tools/registry.py` -> tool implementation | tool result | 需要审查 toolsets |
| MCP server config | `tools/mcp_tool.py` / MCP client | 动态 MCP tools | 需要凭据和 include filter |
| Cron job | `cron/` -> fresh `AIAgent` -> delivery | 定时结果 | 不是普通 shell cron |

## 5. Java / Spring Boot 集成关注点

Hermes 当前更适合作为独立 Agent 产品或外部工具进程学习，不宜直接嵌入 Spring Boot 进程内。若要与 Java 服务集成，优先考虑进程边界或 MCP 边界：

- Bean 生命周期：不把 Hermes 作为 Spring Bean 直接托管，优先通过 HTTP/MCP/CLI 进程交互。
- 配置管理：API key、provider、MCP server 和 gateway 凭据必须放在独立配置，不进入业务仓库。
- 权限和审计：只开放必要的只读工具；写入型工具需要审批和日志。
- 日志和链路追踪：记录请求 ID、用户身份、工具调用和失败原因，避免记录密钥。
- 超时、重试和限流：为外部进程调用设置超时；避免 Agent 长任务占用业务线程。
- 数据库或消息队列：不直接给 Agent 数据库写权限，优先通过受限 MCP server 或只读 API。

## 6. 集成风险

- 依赖版本：安装器管理多个运行时，环境差异可能导致安装失败。
- 模型成本：多 provider 和工具网关可能产生不可见成本，需要预算和限额。
- 工具权限：terminal/file/browser/MCP 可能造成高风险副作用。
- 数据安全：gateway、memory、session storage 和 remote backend 都可能接触敏感内容。
- 运行稳定性：消息平台、MCP server、provider 和远程后端都有独立失败模式。

## 待办检查项

- [x] 明确集成目标和方式。
- [x] 写出最小验证步骤。
- [x] 记录输入、输出和错误处理关注点。
- [x] 标注已验证和未验证内容。


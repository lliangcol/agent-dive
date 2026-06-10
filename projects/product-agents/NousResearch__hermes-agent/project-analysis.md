# Hermes Agent 项目精读

## 1. 项目基本信息

- 项目名称：Hermes Agent
- 项目 ID：`NousResearch__hermes-agent`
- GitHub：https://github.com/NousResearch/hermes-agent
- 官方文档：https://hermes-agent.nousresearch.com/docs/
- 分类：`product-agents`
- 收录等级：Level A 深度收录
- 当前状态：`analyzing`
- 主要语言：Python
- License：MIT
- 分析日期：2026-06-10
- 分析版本 / Commit：`a72bb03757c0c925c686f9774eefc8dc5a77b329`
- 是否运行验证：否
- 分析依据：GitHub API、README、官方文档架构页、仓库根目录 API 列表

## 2. 一句话定位

Hermes Agent 是一个可在 CLI、消息平台和远程环境中运行的产品级自改进 AI Agent，核心学习价值在于完整 Agent 产品如何组织模型、工具、技能、记忆、MCP、调度和多后端执行。

## 3. 项目解决的问题

Hermes 试图解决的是个人或团队长期使用 Agent 时的连续性和部署边界问题：Agent 不只在本机终端里完成一次性任务，而是可以通过 CLI、Telegram、Discord、Slack、WhatsApp、Signal 等入口持续对话，通过持久记忆和 session search 延续上下文，通过 skills 沉淀可复用过程，并通过本地、Docker、SSH、Modal、Daytona、Singularity 等后端执行工具。

适合学习的主题：

- 产品级 Agent 的入口设计：CLI、gateway、ACP、batch runner、API server。
- Agent Loop：模型调用、prompt assembly、工具调度、压缩、持久化和回调。
- Tool Calling：工具注册、toolsets、平台级启用/禁用和终端后端。
- Memory：跨会话记忆、SQLite + FTS5 session storage、profile 隔离。
- MCP：外部工具服务器接入、工具发现、工具过滤和凭据配置。
- Automation：cron job 如何变成 agent task，而不是普通 shell task。
- 安全边界：命令审批、消息平台授权、远程执行环境、密钥和工具权限。

## 4. 项目主线

基于官方架构页，CLI 会从 `cli.py` 或 `hermes_cli/main.py` 进入交互，用户输入经 `HermesCLI.process_input()` 进入 `AIAgent.run_conversation()`。Agent 构造 system prompt，解析 provider 和 model，调用对应 API mode；如模型返回 tool call，则交给 `model_tools.handle_function_call()` 触发工具分发，然后继续循环，直到生成最终响应并保存 session。

Gateway 主线与 CLI 共享核心 `AIAgent`：平台 adapter 接收消息后，gateway 进行用户授权和 session key 解析，再创建带历史的 Agent 实例，执行同一套 conversation loop，最后由平台 adapter 发回响应。

Cron 主线不是简单运行 shell，而是 scheduler 加载到期 job，创建新 Agent，注入 attached skills，运行 job prompt，并把结果投递到目标平台。

以上主线依据官方架构页，尚未用本地源码逐函数验证。

## 5. 快速开始

官方 README 给出的安装入口：

- Linux / macOS / WSL2 / Termux：`curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
- Windows PowerShell：`iex (irm https://hermes-agent.nousresearch.com/install.ps1)`
- 安装后常用命令：`hermes`、`hermes model`、`hermes tools`、`hermes config set`、`hermes gateway`、`hermes setup`、`hermes update`、`hermes doctor`

当前收录未执行这些命令，因此：

- 不记录任何本机成功安装结论。
- 不判断 Windows 原生安装是否在当前机器可用。
- 不判断 provider、gateway 或 MCP 是否已经配置成功。

后续运行验证应优先使用隔离环境，并记录完整命令、输出、失败原因和密钥脱敏方式。

## 6. 核心架构

官方架构页把 Hermes 分为入口层、核心 Agent、存储和工具后端四组：

- 入口层：CLI、Gateway、ACP、Batch Runner、API Server、Python Library。
- 核心 Agent：`AIAgent` in `run_agent.py`，包含 prompt builder、provider resolution、tool dispatch、compression、caching 和 persistence。
- 存储层：`hermes_state.py`、`gateway/session.py`，使用 SQLite + FTS5 做 session storage。
- 工具后端：terminal、browser、web、MCP、file、vision 等工具能力，terminal 有多个后端。

图解见：

- `assets/diagrams/architecture.mmd`
- `assets/diagrams/agent-loop.mmd`
- `assets/diagrams/gateway-flow.mmd`

## 7. 核心原理

### Agent Loop

核心类是官方文档标注的 `AIAgent`。它承担 provider 选择、prompt 构造、工具执行、重试、fallback、callback、压缩和持久化。当前只确认官方架构说明，尚未定位到函数级实现细节。

### Tool Calling

官方工具文档说明 tools 是扩展 Agent 能力的函数，并按 toolsets 组织，可按平台启用或禁用。官方架构页说明 central registry 位于 `tools/registry.py`，工具文件在导入时注册，`model_tools.py` 收集 schema 并分发调用。

### Memory 和 Session

官方 memory 文档说明 Hermes 使用 bounded curated memory，并将 `MEMORY.md` 和 `USER.md` 注入 session 启动时的 system prompt。官方架构页还说明 session storage 使用 SQLite + FTS5，支持 lineage、平台隔离和 atomic writes。二者的具体写入时机和冲突处理需源码验证。

### MCP

官方 MCP 文档说明 Hermes 可连接本地 stdio server 和远程 HTTP MCP server，在启动时发现并注册工具，并支持 per-server tool filtering。MCP 工具最终会进入 Hermes 的 tool calling 体系，但具体 schema 包装和错误处理路径需源码验证。

### Skills

README 和官方架构页都把 skills 作为核心能力之一。当前可确认其定位是 procedural memory / reusable capabilities，具体创建、存储、自改进和调用时机需在 `agent/skill_commands.py`、`hermes_cli/skills_hub.py`、`hermes_cli/skills_config.py` 和 `skills/` 下继续阅读。

### Cron

官方架构页说明 cron job 由 scheduler tick 触发，加载 due jobs 后创建 fresh Agent，并将结果投递到平台。需要继续阅读 `cron/jobs.py`、`cron/scheduler.py` 和 gateway delivery 相关代码。

## 8. 源码结构

基于 GitHub contents API 和官方架构页，优先关注：

- 入口文件：`cli.py`、`hermes_cli/main.py`、`run_agent.py`、`gateway/run.py`、`batch_runner.py`、`mcp_serve.py`
- 核心包 / 模块：`agent/`、`hermes_cli/`、`tools/`、`gateway/`、`cron/`、`providers/`、`skills/`、`optional-skills/`、`plugins/`
- 配置位置：`cli-config.yaml.example`、`.env.example`、`hermes_cli/config.py`
- 示例和文档：`docs/`、`website/`、`datagen-config-examples/`
- 测试目录：`tests/`
- 安装和打包：`pyproject.toml`、`setup.py`、`Dockerfile`、`docker-compose.yml`、`setup-hermes.sh`

## 9. 关键调用链

### 调用链 1：CLI 会话

- 触发条件：用户在 CLI 输入消息。
- 起点：`HermesCLI.process_input()`。
- 关键步骤：`AIAgent.run_conversation()` -> `prompt_builder.build_system_prompt()` -> `runtime_provider.resolve_runtime_provider()` -> provider API -> optional tool call -> `model_tools.handle_function_call()`。
- 终点：最终响应显示并保存到 SessionDB。
- 依据：官方架构页。
- 待验证：具体异常处理、重试、压缩和 session 写入代码。

### 调用链 2：消息平台 Gateway

- 触发条件：Telegram、Discord、Slack 等平台 adapter 收到消息。
- 起点：`Adapter.on_message()`。
- 关键步骤：`GatewayRunner._handle_message()` -> 授权 -> session key -> 创建带历史的 `AIAgent` -> `AIAgent.run_conversation()`。
- 终点：通过 adapter 投递响应。
- 依据：官方架构页。
- 待验证：不同平台 adapter 的认证、限流、重试和异常投递路径。

### 调用链 3：Cron Job

- 触发条件：scheduler tick 检测到 due job。
- 起点：scheduler 加载 `jobs.json`。
- 关键步骤：创建 fresh Agent -> 注入 attached skills -> 运行 job prompt -> delivery。
- 终点：更新 job state 和 next_run。
- 依据：官方架构页。
- 待验证：job 存储格式、失败重试、平台投递失败处理。

## 10. 集成方式

可考虑的集成路径：

- 作为终端产品使用：安装后通过 `hermes` 与 Agent 对话。
- 作为消息平台 Agent 使用：配置 `hermes gateway setup/start` 后接入目标平台。
- 作为 MCP client 使用：在 `~/.hermes/config.yaml` 配置 `mcp_servers`，让 Hermes 使用外部 MCP server 工具。
- 作为可扩展工具系统学习样本：阅读 `tools/registry.py`、`toolsets.py` 和 `model_tools.py` 的注册/分发模式。
- 作为远程执行 Agent 学习样本：重点验证 terminal backends 的权限模型和沙箱边界。

当前不建议在缺少隔离和密钥治理的情况下直接接入业务系统。先做只读工具和最小 provider 配置，再进入写入型工具和远程执行。

## 11. 问题排查

优先记录以下问题：

- 安装脚本下载依赖失败：区分网络、Python、uv、Node.js、Git Bash、ffmpeg。
- Provider 配置失败：区分 API key、base_url、model alias、OAuth 和 credential pool。
- 工具权限过宽：检查 `hermes tools`、terminal backend、approval 配置和危险命令检测。
- Gateway 消息收不到或发不出：检查平台凭据、allowlist、DM pairing、session routing 和 delivery。
- MCP server 不可用：检查 stdio/HTTP 配置、OAuth、server 启动、tool include filter。
- Memory 结果不符合预期：检查 session 启动快照、memory tool 写入和下次 session 注入边界。

详见 `troubleshooting.md`。

## 12. 客观评价

### 优点

- 能作为产品级 Agent 的完整案例学习，覆盖入口、工具、记忆、调度、网关、MCP 和执行环境。
- 官方文档给出架构、数据流和阅读顺序，适合做源码精读。
- Python 为主，目录结构清晰，便于按模块拆解。
- 支持多 provider 和多运行后端，适合研究平台化 Agent 的扩展设计。

### 缺点

- 能力面很宽，第一次学习容易停留在 README 复述。
- 安装和运行涉及密钥、消息平台和远程执行，验证成本高。
- 工具执行和远程后端带来安全风险，需要单独做权限模型分析。
- 仓库更新很快，文档和源码结论需要标注日期与 commit。

### 适用场景

- 学习产品级 Agent 架构。
- 学习工具系统、MCP、skills、memory、gateway 和 cron 的工程组织方式。
- 对比 Claude Code、OpenAI Codex、OpenHands、LangGraph 等 Agent 产品或框架。
- 研究远程执行和消息平台 Agent 的权限边界。

### 不适用场景

- 只想找一个轻量 SDK 嵌入业务服务。
- 不愿处理模型 provider、消息平台、MCP 和工具权限配置。
- 需要稳定企业级 SLA 但尚未完成自部署验证。
- 只需要 RAG pipeline，而不是完整 Agent 产品。

## 13. Learning Todo List

见 `learning-todo-list.md`。

## 14. 总结

Hermes Agent 值得 Level A 深度收录，因为它不是单点 demo，而是覆盖 Agent 产品生命周期的大型工程样本。当前第一版收录已经完成公开元数据、官方文档、初步架构、学习任务和图解草稿；后续重点是克隆源码后按官方推荐阅读顺序验证 `AIAgent`、tool registry、session storage、gateway、MCP 和 cron 的真实调用链，再执行最小安装和只读工具验证。


# Caveman 集成指南

## 1. 集成目标

- 目标系统：本地 AI 编码助手环境和可选 MCP client。
- 目标能力：让 Agent 输出更短、更少寒暄，同时保留技术事实、代码、路径和错误信息。
- 集成方式：统一安装器、per-agent skill install、Claude Code hooks、可选 MCP shrink、可选 memory compression。
- 约束条件：当前文档未做本机运行验证，所有安装命令需先在隔离环境或 dry-run 中验证写入范围。

## 2. 前置条件

- 运行环境：Node 18+；Windows 需要 PowerShell 5.1+ 或可用的 `node` / `npx`。
- 依赖：统一安装器基于 Node；`caveman-compress` 包含 Python scripts；不同 Agent 安装路径可能要求对应 CLI 已安装并已登录。
- 权限要求：安装可能写用户级配置、agent 插件目录、hook 文件、statusline 配置或当前仓库 rule files。
- 安全前提：对主力环境执行前，先确认 dry-run 输出、卸载命令和备份策略。

## 3. 最小集成路径

### 路径 A：只做安装计划预览

1. 克隆或下载 Caveman 仓库到临时目录。
2. 执行：`node bin/install.js --list`。
3. 执行：`node bin/install.js --dry-run --all`。
4. 记录将检测哪些 Agent、将执行哪些命令、将写入哪些路径。
5. 确认 dry-run 没有实际写入。

状态：待运行验证。

### 路径 B：Codex 单 Agent 集成

1. 确认当前 Codex 技能安装位置和已有配置。
2. 执行官方 per-agent 命令：`npx skills add JuliusBrussee/caveman -a codex`。
3. 新开 Codex 会话，输入 `/caveman` 或请求短回复。
4. 对同一技术问题分别记录普通输出和 caveman 输出，比较信息完整性。
5. 查找卸载或回滚方式并记录。

状态：待运行验证。

### 路径 C：Claude Code 集成

1. 在临时 Claude 配置目录或测试机器中执行 dry-run。
2. 执行 `node bin/install.js --only claude --dry-run`。
3. 确认 plugin、hooks、statusline 和 MCP shrink 的写入计划。
4. 在测试环境执行真实安装。
5. 新开会话，检查自动激活、`/caveman lite|full|ultra`、关闭命令和 statusline 行为。

状态：待运行验证。

### 路径 D：MCP shrink 集成

1. 准备一个无敏感信息的 MCP server。
2. 使用 `caveman-shrink` 包装该 server。
3. 对比包装前后的 `tools/list`、`prompts/list`、`resources/list` 字段长度。
4. 调用一个 tool，确认 request body 和 tool response 未被改写。
5. 记录 `CAVEMAN_SHRINK_FIELDS` 配置和 debug 输出。

状态：待源码和运行验证。

## 4. 接口与数据流

| 输入 | 处理模块 | 输出 | 备注 |
|---|---|---|---|
| one-liner / `npx` / local node command | `bin/install.js` | agent plugin / skill / hook / rule 写入计划或结果 | 需先 dry-run |
| `/caveman` 或自然语言触发 | skill / hooks | 压缩后的 Agent 回复 | 不改变模型推理，只改变输出约束 |
| Claude Code session events | `src/hooks/` | active flag、hidden context、statusline 文本 | 待本机验证 |
| MCP list 响应 | `caveman-shrink` | 更短的 metadata description | 不应改 tool call response |
| memory markdown 文件 | `caveman-compress` | 压缩文件和 `.original.md` 备份 | 需确认 API / CLI fallback 和敏感数据边界 |
| benchmark prompts | `benchmarks/` / `evals/` | token reduction measurement | 需复现统计口径 |

## 5. Java / Spring Boot 集成关注点

Caveman 不嵌入 Java / Spring Boot 运行时。它更适合作为开发助手层面的输出规范和工具链配置。

- Bean 生命周期：不涉及 Spring Bean。
- 配置管理：不要把 Agent 用户级配置、API key 或本机路径写入业务仓库。
- 权限和审计：安装器对用户配置的写入需要独立记录，不能混同业务代码变更。
- 日志和链路追踪：对安装、卸载、stats、compress、MCP shrink 运行都要保留命令和版本。
- 团队协作：若要在团队仓库加入 rule files，应作为显式代码评审内容，而不是个人 one-liner 的副产物。

## 6. 集成风险

- 写入范围风险：`--all` 或 one-liner 可能覆盖多个 Agent 的用户级配置。
- 平台差异风险：Windows PowerShell、Git Bash、WSL、macOS/Linux 的 install path 和脚本执行行为不同。
- 语义压缩风险：输出过短可能省略必要上下文，尤其是安全、合规、不可逆操作和多步骤执行顺序。
- 统计误读风险：README benchmark、stats 和 statusline 是有口径的指标，不能直接等同于所有工作流的成本收益。
- 敏感数据风险：`caveman-compress` 会处理用户指定文件，并可能通过 SDK 或 Claude CLI 发送内容；对私有记忆文件必须先确认边界。
- MCP 兼容风险：proxy 需要保持 JSON-RPC 语义不变；字段压缩不应破坏 schema、identifier 或 tool 描述的必要精度。

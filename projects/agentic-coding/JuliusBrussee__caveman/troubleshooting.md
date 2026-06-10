# Caveman 问题排查记录

## 问题：不要直接在主力环境跑全量 one-liner

- 发现时间：2026-06-11
- 当前状态：待本机验证
- 影响范围：安装和回滚

### 现象

README / INSTALL.md 提供 shell 和 PowerShell one-liner，并说明会检测多个 AI 编码助手。对主力机器直接执行可能写入多个用户级 Agent 配置。

### 环境

- 操作系统：Windows / PowerShell 以及其他 shell
- 运行时版本：待验证
- 项目版本 / Commit：`655b7d9c5431f822264b7732e9901c5578ac84cf`
- 关键依赖：Node 18+、目标 Agent CLI / 配置目录

### 复现步骤

1. 在临时克隆中执行 `node bin/install.js --dry-run --all`。
2. 记录输出的 provider、命令和写入路径。
3. 对比真实 one-liner 的默认行为。

### 初步判断

- 可能原因：统一安装器的目标是“一次安装所有可检测 Agent”，这对学习环境方便，但对主力环境需要先审计写入范围。
- 排除项：不是 Caveman 项目本身不可安装。

### 解决方案

- 最终处理：先 dry-run，再只选单 Agent 安装。
- 验证命令：待执行。
- 剩余风险：不同 provider 的检测和写入逻辑需要源码验证。

## 问题：Codex 路径可能不是自动全局生效

- 发现时间：2026-06-11
- 当前状态：待运行验证
- 影响范围：Codex 用户

### 现象

INSTALL.md 对 Codex CLI 的 per-agent 命令是 `npx skills add JuliusBrussee/caveman -a codex`，并把自动激活列为 per-session `/caveman`。

### 初步判断

- 可能原因：Codex skill 安装和 Claude Code hooks 的自动激活机制不同。
- 排除项：不能把 Claude Code 的 SessionStart hook 行为直接套到 Codex。

### 解决方案

- 安装后用新会话测试 `/caveman`。
- 明确记录是否需要每个会话触发。
- 不在文档里写“Codex 自动永久开启”，除非运行验证证明。

## 问题：`caveman-compress` 可能处理敏感记忆文件

- 发现时间：2026-06-11
- 当前状态：待源码和运行验证
- 影响范围：CLAUDE.md、AGENTS.md、项目笔记、偏好文件等记忆材料

### 现象

SECURITY.md 说明 `caveman-compress` 读取用户显式指定的文件，压缩后写回同一路径，并创建 `.original.md` 备份。认证路径可能走 Anthropic SDK 或 Claude CLI fallback。

### 初步判断

- 可能原因：记忆文件往往包含项目偏好、路径、内部上下文甚至敏感信息，压缩前需要明确 API / CLI 数据边界。
- 排除项：MIT License 不等同于运行时数据安全保证。

### 解决方案

- 先在无敏感测试文件上执行。
- 确认备份、文件大小限制、路径限制和异常回滚。
- 对私有记忆文件执行前，检查是否会发送到外部 API 或 Claude CLI。

## 问题：输出压缩可能影响高风险沟通清晰度

- 发现时间：2026-06-11
- 当前状态：待行为验证
- 影响范围：安全警告、删除操作、迁移、生产变更、法律 / 医疗 / 财务类高风险回答

### 现象

主 skill 规则包含自动清晰度边界，遇到安全警告、不可逆操作确认、多步骤顺序容易误读等情况应降低压缩。

### 初步判断

- 可能原因：片段化表达适合普通工程沟通，但高风险场景需要完整顺序和明确条件。
- 排除项：不是所有短回复都安全。

### 解决方案

- 测试 destructive operation prompt，确认是否自动恢复清晰表达。
- 在团队规范里明确：高风险变更不强制使用极限压缩模式。
- 对 `/caveman ultra` 和 `wenyan` 模式做额外人工审查。

## 问题：MCP shrink 不能破坏协议语义

- 发现时间：2026-06-11
- 当前状态：待源码和 MCP 客户端验证
- 影响范围：MCP server metadata、tool schema、tool call response

### 现象

MCP shrink README 表示 proxy 压缩 list 响应中的描述字段，不改 request body 和 tool call response。

### 初步判断

- 可能原因：tool description 太长会增加上下文成本，但 schema、identifier、path、URL、code-like token 和返回值不能被误改。

### 解决方案

- 用测试 MCP server 比较包装前后的完整 JSON。
- 验证 `tools/call` response byte-level 或 semantic-level 未改写。
- 只在确认兼容后给生产 MCP server 加 wrapper。

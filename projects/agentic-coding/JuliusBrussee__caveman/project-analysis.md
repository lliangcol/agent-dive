# Caveman 项目精读

## 1. 项目基本信息

- 项目名称：Caveman
- 项目 ID：`JuliusBrussee__caveman`
- GitHub：https://github.com/JuliusBrussee/caveman
- 项目主页：https://getcaveman.dev/（GitHub API homepage / README 链接）
- 分类：`agentic-coding`
- 收录等级：Level B 标准收录
- 当前状态：`analyzing`
- 主要语言：JavaScript
- License：MIT
- 分析日期：2026-06-11
- 分析版本 / Commit：`655b7d9c5431f822264b7732e9901c5578ac84cf`
- 默认分支：`main`
- 是否运行验证：否
- 分析依据：GitHub API、README、INSTALL.md、CLAUDE.md、`src/hooks/README.md`、`src/mcp-servers/caveman-shrink/README.md`、`skills/caveman-compress/SECURITY.md`、GitHub tree、`package.json`、`git ls-remote --symref`；未做本机安装、测试或源码调用链验证。

## 2. 一句话定位

Caveman 是一个跨 AI 编码助手的回复压缩 skill / plugin，通过提示词规则、安装器和辅助 hooks 让 Agent 用更少输出 token 保持技术信息密度。

## 3. 项目解决的问题

AI 编码助手在代码解释、review、修复建议和排查时常常输出大量寒暄、重复铺垫和低信息密度文本。对长会话、反复 review、CI 调试、文档整理等场景，这会增加阅读成本和输出 token 成本。

Caveman 的学习价值在于：

- 输出风格约束：把“少说但不丢技术信息”写成可复用 skill 规则。
- 跨 Agent 分发：同一套行为通过 Claude Code plugin、Codex skill、Gemini extension、OpenCode plugin 和其他 agent rule files 分发。
- 运行时激活：Claude Code hooks 可在 SessionStart 和 UserPromptSubmit 阶段维护模式状态。
- 成本观测：`caveman-stats` 和 statusline 用于展示节省估算，但仍需验证统计口径。
- 上下文压缩：`caveman-compress` 针对记忆文件压缩；`caveman-shrink` 针对 MCP tool / prompt / resource 描述压缩。

依据：README、INSTALL.md、hooks README 和 SECURITY.md；具体实现细节待源码验证。

## 4. 项目主线

基于 README / INSTALL.md，典型使用主线如下：

1. 用户通过 shell / PowerShell one-liner 或 `npx` 调用统一安装器。
2. `bin/install.js` 检测或按参数选择目标 Agent，并调用对应安装路径。
3. 对 Claude Code，安装 plugin / skills，并配置 hooks、statusline 和可选 MCP shrink。
4. 对 Codex / Cursor / Windsurf / Cline 等，使用 `npx skills add` 或 rule file 方式写入对应配置。
5. 用户在会话中输入 `/caveman` 或自然语言触发，Agent 按 skill 规则压缩输出。
6. 可选命令处理 commit message、review comment、stats、memory file compression 和 MCP description compression。

未验证：上述流程尚未在本机执行，具体写入文件、幂等行为、卸载行为和错误处理待运行确认。

## 5. 快速开始

- 环境要求：README / INSTALL.md 提到统一安装器需要 Node 18+。
- Windows 安装入口：`irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex`。
- macOS / Linux / WSL 安装入口：`curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash`。
- Dry-run：INSTALL.md 提供 `--dry-run` 路径，可先预览写入和命令。
- Codex 单 Agent 安装：INSTALL.md 列出 `npx skills add JuliusBrussee/caveman -a codex`。
- 触发方式：README 描述 `/caveman`，并提供 `lite`、`full`、`ultra`、`wenyan` 等模式。

当前仓库未执行这些命令。由于安装可能写入用户级 Agent 配置，本次收录只记录官方路径和待验证边界。

## 6. 核心架构

根据 README、INSTALL.md、CLAUDE.md、GitHub tree 和 package.json，当前可确认的模块线索：

| 模块 | 作用 | 依据 | 验证状态 |
|---|---|---|---|
| `bin/install.js` | 统一安装器，检测或选择目标 Agent，执行安装 / 卸载 / dry-run | INSTALL.md、CLAUDE.md、package.json | 待源码验证 |
| `install.sh` / `install.ps1` | 平台 shim，转入 Node 安装器 | GitHub tree、INSTALL.md | 待运行验证 |
| `skills/caveman/` | 主压缩行为规则，包括多种强度和边界 | skill 文件 | 已读规则摘要，待安装验证 |
| `skills/caveman-compress/` | 压缩记忆文件，包含 Python scripts 和安全说明 | GitHub tree、SECURITY.md | 待源码 / 运行验证 |
| `skills/caveman-stats/` | 统计 token 使用与节省展示 | README、tree | 待源码验证 |
| `skills/cavecrew/` / `agents/` | caveman 风格子 Agent 和 delegation 指南 | README、tree、CLAUDE.md | 待源码 / 行为验证 |
| `src/hooks/` | Claude Code SessionStart、UserPromptSubmit、statusline 等 hooks | hooks README、CLAUDE.md | 待源码 / 运行验证 |
| `src/mcp-servers/caveman-shrink/` | MCP stdio proxy，压缩 tool / prompt / resource 描述字段 | MCP README、tree | 待源码 / 运行验证 |
| `plugins/caveman/` | Claude Code plugin 分发目录 | CLAUDE.md、tree | 待同步流程验证 |
| `benchmarks/` / `evals/` | token reduction benchmark 和三路评测 | README、tree | 待复现 |
| `tests/` | Node 和 Python 测试 | GitHub tree、package.json | 待执行 |

图解草稿见 `assets/diagrams/architecture.mmd`、`install-flow.mmd`、`hook-flow.mmd` 和 `mcp-shrink-flow.mmd`。

## 7. 核心原理

### 输出压缩 skill

`skills/caveman/SKILL.md` 把压缩行为拆成强度、规则、触发方式和安全边界。关键思想不是减少推理，而是减少最终回复中的低信息密度文本。它要求保持技术术语、代码、路径、错误信息和 API 名称准确，同时删除寒暄、hedging 和重复解释。

依据：`skills/caveman/SKILL.md`；待真实会话验证。

### 统一安装器

INSTALL.md 表示统一安装器负责自动检测已安装 Agent，并按不同平台走 plugin、extension、skill、rule file 或 hook 路径。`package.json` 暴露 `caveman` bin 指向 `bin/install.js`，说明 Node 安装器是主要入口。

依据：INSTALL.md、package.json、CLAUDE.md；待源码和 dry-run 验证。

### Claude Code hooks 和状态文件

hooks README 显示 Claude Code 路径使用 SessionStart hook、UserPromptSubmit hook 和 statusline 脚本。核心桥接物是配置目录下的 mode flag 文件；hook 写入或删除模式，statusline 读取后显示当前模式。

依据：`src/hooks/README.md`；待本机安装验证。

### 记忆文件压缩

`caveman-compress` 针对用户指定的记忆文件生成压缩版并保留 `.original.md` 备份。SECURITY.md 说明它可能使用 Anthropic SDK 或 Claude CLI fallback，限制大文件，并声明不会读取用户未指定路径。

依据：`skills/caveman-compress/SECURITY.md`；待源码和运行验证。

### MCP description 压缩

`caveman-shrink` 是 stdio proxy，位于 MCP client 和上游 server 之间。它保守地压缩 `tools/list`、`prompts/list`、`resources/list` 这类元数据响应里的描述字段，而不改写 tool call request body 或 tool call response。

依据：`src/mcp-servers/caveman-shrink/README.md`；待源码和 MCP 客户端验证。

## 8. 源码结构

GitHub tree 显示的主要结构：

- `bin/`：统一安装器和配置写入辅助逻辑。
- `skills/`：各 skill 的源头文件，包括 `caveman`、`caveman-compress`、`caveman-stats`、`caveman-commit`、`caveman-review`、`cavecrew`。
- `agents/`：cavecrew 子 Agent 定义。
- `commands/`：Codex / Gemini command stubs。
- `src/hooks/`：Claude Code hooks、statusline 脚本和 hook installer。
- `src/mcp-servers/caveman-shrink/`：MCP shrink middleware。
- `src/plugins/opencode/`：OpenCode plugin。
- `plugins/caveman/`：Claude Code plugin 分发目录。
- `benchmarks/`：token benchmark prompts 和 runner。
- `evals/`：三路评测 harness 和结果 snapshot。
- `tests/`：installer、hooks、compress safety、MCP shrink 等测试。

待源码确认：

- `bin/install.js` 的 provider detection、dry-run、write scope 和 uninstall 行为。
- `src/hooks/caveman-activate.js` / `caveman-mode-tracker.js` 的输入输出和安全边界。
- `src/mcp-servers/caveman-shrink/index.js` / `compress.js` 的 JSON-RPC 处理和字段压缩规则。
- `skills/caveman-compress/scripts/` 的文件路径校验、备份、API / CLI fallback 和错误处理。

## 9. 关键调用链

### 调用链 1：统一安装器

- 触发条件：用户运行 one-liner、`npx -y github:JuliusBrussee/caveman` 或本地 `node bin/install.js`。
- 起点：`bin/install.js`，待源码确认。
- 关键步骤：解析参数 -> 检测 provider -> 选择 per-agent install command -> 可选安装 hooks / statusline / MCP shrink / rule files -> 输出结果。
- 终点：目标 Agent 的 skill/plugin/rule/hook 配置被写入，或 dry-run 只打印计划。
- 依据：INSTALL.md、package.json。
- 状态：待源码和运行验证。

### 调用链 2：Claude Code 自动激活

- 触发条件：Claude Code 新会话启动，plugin 或 standalone hooks 已安装。
- 起点：SessionStart hook，待源码确认。
- 关键步骤：写入 active mode flag -> 注入压缩规则上下文 -> statusline 读取 flag -> 用户 prompt 时 UserPromptSubmit hook 解析 `/caveman` 或关闭语句。
- 终点：后续回复按当前 mode 压缩输出。
- 依据：hooks README。
- 状态：待运行验证。

### 调用链 3：MCP shrink proxy

- 触发条件：MCP client 调用 wrapper 启动上游 server。
- 起点：`src/mcp-servers/caveman-shrink/index.js`，待源码确认。
- 关键步骤：启动上游命令 -> 转发 JSON-RPC -> 拦截 list 类响应 -> 压缩指定 prose 字段 -> 透传请求和 tool call response。
- 终点：Agent 读取更短的 MCP metadata。
- 依据：MCP shrink README。
- 状态：待源码和运行验证。

### 调用链 4：记忆文件压缩

- 触发条件：用户执行 `/caveman-compress <file>` 或对应脚本入口。
- 起点：`skills/caveman-compress/scripts/cli.py` 或 skill 执行路径，待源码确认。
- 关键步骤：校验用户指定路径和大小 -> 读取文件 -> 调用 Anthropic SDK 或 Claude CLI -> 写回压缩结果 -> 保存 `.original.md` 备份。
- 终点：记忆文件变短，原始文件备份存在。
- 依据：README、SECURITY.md、GitHub tree。
- 状态：待源码和运行验证。

## 10. 集成方式

适合先做三种集成实验：

1. Dry-run 统一安装器：在临时克隆中执行 `node bin/install.js --dry-run --all` 和 `node bin/install.js --list`，确认 provider matrix 和写入计划。
2. Codex 单路径安装：在明确同意写入用户级 Codex skill 后，执行 `npx skills add JuliusBrussee/caveman -a codex`，确认实际写入位置和可卸载方式。
3. MCP shrink wrapper：用一个无敏感信息的 MCP server 做 wrapper 测试，对比 list 响应字段长度，并确认 tool call response 未被改写。

当前不建议直接在主力工作环境执行全量 one-liner；先 dry-run 和隔离环境验证更稳。

## 11. 问题排查

优先排查方向：

- 安装写入范围：one-liner 可能检测多个 Agent 并写用户级配置；先用 `--dry-run`。
- Node 版本：README / INSTALL.md 要求 Node 18+；Windows 环境需确认 `node` 和 `npx` 可用。
- PowerShell 执行策略：`install.ps1` 或 hook statusline 脚本可能受执行策略影响。
- Codex 激活方式：INSTALL.md 显示 Codex 需要 per-session `/caveman`，不要误以为一定自动激活。
- 统计口径：`caveman-stats` 和 benchmark 结论需区分真实 API token、估算、历史 session log 和当前会话。
- 记忆压缩风险：先确认备份、路径、文件大小和 API / CLI fallback，再对重要记忆文件执行压缩。

## 12. 客观评价

### 优点

- 面向真实 AI 编码助手工作流，不只是 README 里的提示词片段。
- 同时覆盖 skill 规则、插件分发、安装器、hooks、状态栏、MCP proxy、benchmark 和 tests。
- 对 Agent 输出成本、阅读效率和上下文治理有直接学习价值。
- License 为 MIT，适合学习和二次研究。

### 缺点

- 技术价值容易被 meme 风格包装掩盖，分析时要回到 installer、hooks、MCP proxy 和安全边界。
- 安装路径覆盖大量 Agent，写入范围和幂等性必须通过 dry-run / 临时环境验证。
- 输出压缩不等于结论正确，复杂安全提醒、不可逆操作和多步流程仍需要清晰表达。
- benchmark 和 stats 需要复现口径，不能直接当作所有任务通用收益。

### 适用场景

- 学习 AI 编码助手 skill / plugin 生态和多平台分发。
- 研究输出 token 压缩、提示词风格约束和信息密度。
- 研究 Claude Code hooks、statusline 和 session state 机制。
- 研究 MCP metadata 压缩和 Agent 工具目录 token 成本。

### 不适用场景

- 需要严肃、完整、面向非技术用户的解释文档时，不应默认压缩到片段化表达。
- 需要法律、医疗、安全、不可逆操作确认等高风险沟通时，压缩规则必须让位于清晰性。
- 不适合在未审计写入范围时直接跑全量安装器。
- 不适合作为“模型更聪明”的证据；它主要改变输出层表达。

## 13. Learning Todo List

见 [learning-todo-list.md](learning-todo-list.md)。建议先完成 Level 1 到 Level 2，再进入源码级验证和隔离环境安装测试。

## 14. 总结

Caveman 值得收录为 `agentic-coding` 方向的 Level B 项目。它把提示词压缩、Agent skill 分发、Claude Code hooks、MCP metadata 压缩和 token 成本观测连接在一起，适合作为“AI 编码助手如何在保持技术信息的同时降低输出冗余”的学习样例。

下一步应执行 dry-run 安装验证，并源码确认 installer、hooks、MCP shrink 和 memory compression 的真实边界。

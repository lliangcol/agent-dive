# Claude HUD 项目精读

## 1. 项目基本信息

- 项目名称：Claude HUD
- 项目 ID：`jarrodwatts__claude-hud`
- GitHub：https://github.com/jarrodwatts/claude-hud
- 分类：`agentic-coding`
- 收录等级：Level B 标准收录
- 当前状态：`analyzing`
- 主要语言：TypeScript
- License：MIT
- 分析日期：2026-06-11
- 分析版本 / Commit：`9650a43600e9bcc94057fbd693a7f05aba4ee1ff`
- 默认分支：`main`
- 包版本：`0.1.1`
- 是否运行验证：否。已在临时浅克隆执行 `npm ci` 和 `npm test`，但测试失败；未在真实 Claude Code 中安装或启用 HUD。
- 分析依据：GitHub 页面、raw README、raw `package.json`、浅克隆源码、`.claude-plugin/plugin.json`、`commands/setup.md`、`commands/configure.md`、`src/index.ts`、`src/stdin.ts`、`src/transcript.ts`、`src/config.ts`、`src/render/index.ts`、`src/external-usage.ts`、`src/git.ts`、测试输出。

## 2. 一句话定位

Claude HUD 是一个 Claude Code statusline 插件，把 Claude Code 会话的上下文窗口、订阅用量、工具活动、子 Agent、Todo、git 状态和配置状态渲染成始终可见的终端 HUD。

## 3. 项目解决的问题

Claude Code 会话的关键状态分散在 `/context`、transcript、settings、git、MCP 配置、hooks 和用户记忆文件中。用户在长任务、并行子 Agent、复杂工具调用或接近上下文上限时，往往需要主动查询才能知道当前状态。

Claude HUD 的学习价值在于：

- 观察层设计：不改变 Agent loop，而是利用 statusline API 提供低侵入运行期观测。
- 上下文治理：直接读取 Claude Code stdin 中的 context window 信息，优先使用官方 used percentage，再做 fallback。
- 活动汇总：解析 transcript JSONL，把 tool、Skill、MCP、Task/Agent、TodoWrite、TaskCreate/TaskUpdate 转成短状态行。
- 配置治理：用 `config.json` 支持布局、语言、阈值、颜色、git 样式、usage 展示、外部 usage snapshot 等选项。
- 跨平台 setup：`/claude-hud:setup` 明确处理 macOS/Linux、Windows PowerShell、Windows Git Bash/MSYS2、WSL、Bun/Node 差异，以及已有 statusline 备份。

## 4. 项目主线

典型主线如下：

1. 用户在 Claude Code 中添加 marketplace 并安装 `claude-hud` plugin。
2. 用户执行 `/claude-hud:setup`。
3. setup command 检查 ghost install、平台/shell/runtime、已有 statusLine，并生成合适的 statusLine command。
4. setup command 备份并更新 Claude Code `settings.json` 的 `statusLine.command`。
5. Claude Code 每次刷新 statusline 时，把 stdin JSON 传给 `dist/index.js` 或 wrapper。
6. `src/index.ts` 读取 stdin、解析 transcript、读取配置、git、usage、memory、version 和 extra command。
7. render 层根据 compact / expanded 布局输出一到多行 HUD。

未验证：第 1 到第 5 步没有在真实 Claude Code 环境中执行。本次确认的是源码和命令文档设计。

## 5. 快速开始

README 给出的安装路径：

1. 在 Claude Code 中运行 `/plugin marketplace add jarrodwatts/claude-hud`。
2. 运行 `/plugin install claude-hud`。
3. 运行 `/reload-plugins`。
4. 运行 `/claude-hud:setup`。
5. 重启 Claude Code，让新的 `statusLine` 配置生效。

环境要求：

- Claude Code v1.0.80+。
- macOS/Linux：Node.js 18+ 或 Bun。
- Windows：Node.js 18+，setup 文档明确要求 Windows 使用 Node，不走 Bun。

当前仓库未执行真实 plugin install 或 setup 写入。由于 setup 会写用户级 Claude Code 配置，本次只做源码和临时测试验证。

## 6. 核心架构

| 模块 | 作用 | 依据 | 验证状态 |
|---|---|---|---|
| `.claude-plugin/plugin.json` | Claude Code plugin manifest，声明 setup/configure commands | manifest | 已读取 |
| `commands/setup.md` | 生成并写入 statusLine command，处理平台、runtime、已有 statusline、备份和验证 | setup command | 已读取，未真实执行 |
| `commands/configure.md` | guided config flow，修改 HUD 布局、语言、preset 和显示元素 | configure command | 已读取，未真实执行 |
| `src/index.ts` | statusline 主入口，汇总 stdin、transcript、config、git、usage、memory、version 后渲染 | 源码 | 已读取 |
| `src/stdin.ts` | 读取 Claude Code stdin JSON，计算 context percent，解析 rate_limits 和 provider label | 源码 | 已读取 |
| `src/transcript.ts` | 流式解析 transcript JSONL，提取工具、Skill、MCP、Agent、Todo、session tokens、advisor 等 | 源码 | 已读取 |
| `src/config.ts` | 默认配置、配置迁移、类型校验、颜色和阈值约束 | 源码 | 已读取 |
| `src/render/` | compact / expanded 渲染、宽度计算、ANSI/OSC8 处理、activity lines | 源码 | 已读取 |
| `src/git.ts` | 获取 branch、dirty、ahead/behind、file stats、line diff 和 GitHub branch URL | 源码 | 已读取 |
| `src/external-usage.ts` | 读取或写入外部 usage snapshot，支持 balance label 和 freshness 校验 | 源码 | 已读取 |
| `tests/` | Node test suite，覆盖 config、stdin、transcript、render、git、integration 等 | 测试输出 | 已运行，当前 Windows 环境失败 |

图解草稿见 `assets/diagrams/architecture.mmd`、`statusline-flow.mmd`、`transcript-activity-flow.mmd` 和 `setup-config-flow.mmd`。

## 7. 核心原理

### Statusline stdin 驱动

`src/index.ts` 调用 `readStdin()`。如果没有 stdin，会输出初始化提示，供 setup verification 使用。若有 stdin，则读取 Claude Code 提供的 `transcript_path`、`cwd`、`context_window`、`rate_limits`、`model` 等字段。

依据：`src/index.ts`、`src/stdin.ts`。

### Context 和 usage 展示

context percent 优先使用 Claude Code 较新版本提供的 `context_window.used_percentage`。如果该字段缺失或为未填充的 0，源码再基于 token 和 context window size 计算。subscriber usage 通过 `rate_limits` 读取；Bedrock / Vertex 等 routed provider 有特殊显示边界。

依据：`src/stdin.ts`、README。

### Transcript 活动解析

`src/transcript.ts` 逐行读取 JSONL，提取：

- tool_use / tool_result：工具运行和完成状态。
- `Skill` 工具：active skill。
- `mcp__server__tool` 命名模式：MCP server 活动。
- `Task` / `Agent`：子 Agent，支持 background completion。
- `TodoWrite`、`TaskCreate`、`TaskUpdate`：todo progress。
- assistant usage：session token 累加。
- `compact_boundary`：区分压缩后真实低 token 与 stdin glitch。

依据：`src/transcript.ts`。

### 配置和渲染

`src/config.ts` 提供默认 expanded layout，并允许用户按 element order、merge groups、颜色、阈值和开关调整。render 层处理 ANSI、OSC8 hyperlink、CJK/emoji 宽度、截断和换行，以尽量避免 statusline 破版。

依据：`src/config.ts`、`src/render/index.ts`。

### Setup 的工程边界

`commands/setup.md` 是项目最重的工程文档之一。它要求先检测 ghost install，再分平台生成 statusLine command；写入 `settings.json` 前先备份，遇到已有 statusline 时询问用户。Windows PowerShell 路径还会生成 Node launcher，避免每次刷新启动 PowerShell 过慢或 cache glob 出错。

依据：`commands/setup.md`。

## 8. 关键调用链

### 调用链 1：statusline 渲染

- 起点：Claude Code 调用 `statusLine.command`，stdin 传入 statusline JSON。
- 关键步骤：`readStdin` -> `parseTranscript` -> `applyContextWindowFallback` -> `countConfigs` -> `loadConfig` -> `getGitStatus` -> `getUsageFromStdin` / external snapshot -> `render`。
- 终点：stdout 输出 HUD lines。
- 状态：源码确认，未在真实 Claude Code statusline 中验证。

### 调用链 2：transcript 到活动行

- 起点：stdin 中的 `transcript_path`。
- 关键步骤：canonicalize path -> stat/cache -> stream JSONL -> process tool_use / tool_result / queue-operation / Todo records -> 写 transcript cache。
- 终点：render 层拿到 tools、skills、mcpServers、agents、todos、sessionName 和 sessionTokens。
- 状态：源码确认；真实 transcript payload 未采样验证。

### 调用链 3：setup 写入 statusLine

- 起点：用户执行 `/claude-hud:setup`。
- 关键步骤：检测 ghost install -> 检测平台/shell/runtime -> 定位 plugin cache version -> 生成 statusLine command -> 测试命令 -> 备份 `settings.json` -> 处理已有 statusline -> 写入 JSON。
- 终点：Claude Code 重启后调用 HUD。
- 状态：命令文档确认；未执行写入。

### 调用链 4：guided configure

- 起点：用户执行 `/claude-hud:configure`。
- 关键步骤：读取 `~/.claude/plugins/claude-hud/config.json` -> 按新用户或已有配置选择问题流 -> 生成 preview -> 写入 config。
- 终点：HUD 读取新配置并改变 layout / language / displayed elements。
- 状态：命令文档确认；未执行写入。

## 9. 集成方式

建议先做三层验证：

1. 临时源码验证：在浅克隆中执行 `npm ci`、`npm run build`、有选择地跑非环境敏感测试。
2. 隔离 Claude 配置验证：设置临时 `CLAUDE_CONFIG_DIR`，演练 setup command 生成和 `settings.json` 写入逻辑。
3. 真实 Claude Code 验证：在确认已有 statusline 备份后安装 plugin、运行 setup、重启 Claude Code，并用最小 transcript 场景验证工具/agent/todo/usage 展示。

当前不建议直接在主力 Claude Code 配置中跳过备份执行 setup。

## 10. 问题排查

优先排查方向：

- GitHub API rate limit：收录时 REST API 已限流，可退回 GitHub 页面、raw 文件和浅克隆。
- Windows runtime：README 和 setup 文档要求 Windows 使用 Node.js LTS；Bun 路径仅适用于 macOS/Linux。
- statusLine 现有配置：setup 会替换 `statusLine.command`，必须先备份并确认是否覆盖其他 statusline。
- shell mismatch：Windows + Git Bash/MSYS2 不应使用 PowerShell command format。
- usage 不显示：API-key-only、Bedrock、Vertex 或 `rate_limits` 缺失时，usage 展示有边界。
- 测试失败：当前 Windows 临时环境 `npm test` 失败，不能把测试套件标为通过。

## 11. 客观评价

### 优点

- 把 Claude Code 的原生 statusline、stdin payload 和 transcript JSONL 用成了轻量观测层。
- setup 文档对跨平台、已有配置备份、ghost install、Windows shell mismatch 的处理非常具体。
- 配置验证和 render 宽度处理较细，适合学习终端 UI 的边界条件。
- 不依赖私有 API 抓取 subscriber usage，优先使用 Claude Code 官方 stdin 信息。

### 缺点

- 功能强依赖 Claude Code statusline API 和 transcript 格式，随 Claude Code 版本变化可能漂移。
- setup 流程会写用户级配置，错误操作可能覆盖已有 statusline。
- 当前 Windows 临时测试输出存在失败项，需要进一步判断是项目回归还是环境差异。
- 它是可观测性 HUD，不是完整 tracing、evaluation 或 audit 系统。

### 适用场景

- 学习 Claude Code plugin 和 statusline 机制。
- 研究 Agent 会话状态可视化和 context usage 提醒。
- 研究 transcript JSONL 活动解析。
- 给长任务、并行 Agent、复杂工具调用场景提供低侵入状态提示。

### 不适用场景

- 需要跨 Agent / 跨模型统一 observability 后端时，Claude HUD 的范围太局部。
- 需要合规审计或可复现评测时，HUD 状态行不足以替代日志系统。
- 对主力配置没有备份时，不适合直接覆盖已有 statusline。

## 12. Learning Todo List

见 [learning-todo-list.md](learning-todo-list.md)。建议先验证 setup 写入边界和 Windows 测试失败，再做真实 Claude Code 安装体验。

# Ponytail 项目精读

## 1. 项目基本信息

- 项目名称：Ponytail
- 项目 ID：`DietrichGebert__ponytail`
- GitHub：https://github.com/DietrichGebert/ponytail
- 分类：`agentic-coding`
- 收录等级：Level B 标准收录
- 当前状态：`analyzing`
- 主要语言：JavaScript
- License：MIT
- 分析日期：2026-06-25
- 分析版本 / Commit：`a945778b4a73b0b78c3c781a594b62cd3a324637`
- 默认分支：`main`
- 收录时最新 release：`v4.8.3`
- 是否运行验证：未做真实宿主安装；临时 venv 中执行 full `npm test` 通过。

## 2. 一句话定位

Ponytail 是一个把“少写、少依赖、少抽象，但不牺牲边界验证”的工程准则注入 AI 编码 Agent 的跨宿主 ruleset / skill / plugin 包。

## 3. 项目解决的问题

AI 编码 Agent 容易把简单任务扩大成多文件、多依赖、多抽象的实现。Ponytail 试图在 Agent 每次动手前插入一条固定决策梯：

1. 需求是否真的需要实现。
2. 标准库是否已经覆盖。
3. 平台原生能力是否已经覆盖。
4. 已安装依赖是否已经覆盖。
5. 是否可以是一行。
6. 只有前面都不成立时，才写最小可用实现。

它的重点不是让 Agent “偷懒省测试”，而是删除不必要的工程形态，并明确保留 trust boundary validation、避免数据丢失的错误处理、安全、可访问性、硬件校准和用户明确要求的内容。

## 4. 项目主线

Ponytail 的主线可以拆成四层：

| 层 | 作用 | 已确认文件 |
|---|---|---|
| 规则源 | 定义 lazy senior dev mode、强度级别、边界和输出风格 | `skills/ponytail/SKILL.md`、`AGENTS.md` |
| 命令技能 | 提供 `ponytail`、`ponytail-review`、`ponytail-audit`、`ponytail-debt`、`ponytail-help` | `skills/*/SKILL.md`、`commands/*.toml`、`.opencode/command/*.md` |
| 生命周期注入 | 在 session start、user prompt submit 或 subagent start 时注入规则、跟踪模式、写状态文件 | `hooks/ponytail-activate.js`、`hooks/ponytail-mode-tracker.js`、`hooks/ponytail-subagent.js`、`hooks/ponytail-runtime.js` |
| 宿主适配 | 将同一规则集分发到 Codex、Claude Code、Copilot CLI、OpenCode、Gemini、Pi、OpenClaw 和 instruction-only 宿主 | `.codex-plugin/`、`.claude-plugin/`、`.github/plugin/`、`.opencode/`、`gemini-extension.json`、`pi-extension/`、`.openclaw/`、`.cursor/` 等 |

## 5. 快速开始边界

README 给出了多宿主安装方式。收录时只确认文档和文件存在，未真实执行安装：

- Claude Code：通过 `/plugin marketplace add DietrichGebert/ponytail` 和 `/plugin install ponytail@ponytail`。
- Codex：通过 `codex plugin marketplace add DietrichGebert/ponytail` 后在 `/plugins` 安装，并在 `/hooks` 审核信任 hooks。
- Copilot CLI：通过 `copilot plugin marketplace add` 与 `copilot plugin install`。
- OpenCode：从仓库 checkout 引用 `.opencode/plugins/ponytail.mjs`。
- Gemini CLI / Antigravity：使用 extension 或 `AGENTS.md` 规则。
- Cursor、Windsurf、Cline、Kiro、VS Code Codex extension：主要通过规则文件或 `AGENTS.md` 加载。

真实安装前应先检查 hook 写入范围、插件数据目录、用户级配置文件和 Node 路径。

## 6. 核心架构

### 规则和强度模式

`skills/ponytail/SKILL.md` 定义 `lite`、`full`、`ultra` 三个强度。`hooks/ponytail-instructions.js` 会读取该 skill 文件，根据当前模式过滤强度表和示例，生成注入到宿主系统提示中的内容；读取失败时使用 fallback instruction。

### 配置解析

`hooks/ponytail-config.js` 的默认模式解析顺序是：

1. `PONYTAIL_DEFAULT_MODE` 环境变量。
2. `XDG_CONFIG_HOME/ponytail/config.json`、Unix `~/.config/ponytail/config.json` 或 Windows `%APPDATA%/ponytail/config.json`。
3. 默认 `full`。

它同时提供 `CLAUDE_CONFIG_DIR` 对 `~/.claude` 的覆盖，用于 Claude Code 兼容。

### 生命周期 hooks

`hooks/claude-codex-hooks.json` 注册三个核心事件：

- `SessionStart`：调用 `ponytail-activate.js`，写 `.ponytail-active` 状态并输出规则上下文。
- `UserPromptSubmit`：调用 `ponytail-mode-tracker.js`，识别 `/ponytail`、`@ponytail`、`$ponytail` 及 `stop ponytail`、`normal mode`，更新状态。
- `SubagentStart`：调用 `ponytail-subagent.js`，在子代理启动时读取当前模式并输出 hook-specific JSON。

Windows 命令使用 PowerShell `$env:CLAUDE_PLUGIN_ROOT`，测试中有专门回归，防止误写成 cmd.exe 的 `%VAR%`。

### 多宿主输出格式

`hooks/ponytail-runtime.js` 根据环境变量区分输出协议：

- Codex：检测 `PLUGIN_DATA`，输出包含 `systemMessage` 和 `hookSpecificOutput.additionalContext` 的 JSON。
- Copilot：检测 `COPILOT_PLUGIN_DATA`，SessionStart 输出 `additionalContext`。
- Claude Code：输出纯文本上下文。

这说明 Ponytail 的核心不是单一平台功能，而是同一规则在不同宿主协议下的薄适配。

### Benchmark 和验证

仓库包含 promptfoo benchmark、agentic benchmark、正确性检查器、examples 和成本复核报告。当前收录只确认了 benchmark 文件与说明，未使用 API key 复现。`npm test` 会运行 Node test 和 Pi extension test，其中 CSV correctness 依赖 Python `pandas`，且 Windows 下要确认 `python3` 命中临时 venv。

## 7. 关键调用链

### 调用链 1：Codex / Claude Code 会话启动

1. 宿主触发 `SessionStart` hook。
2. `hooks/claude-codex-hooks.json` 调用 Node 执行 `ponytail-activate.js`。
3. `ponytail-config.js` 解析默认模式。
4. 若模式不是 `off`，`ponytail-runtime.js` 写 `.ponytail-active`。
5. `ponytail-instructions.js` 读取 `skills/ponytail/SKILL.md`，按模式过滤内容。
6. runtime 按宿主协议输出 system message 或 additional context。

状态：源码抽样验证和本地测试通过；真实宿主未运行。

### 调用链 2：用户切换模式

1. 用户输入 `/ponytail lite`、`@ponytail ultra` 或类似命令。
2. `UserPromptSubmit` hook 调用 `ponytail-mode-tracker.js`。
3. 脚本解析 prompt，写入 `lite`、`full`、`ultra`、`review` 或清理 `off`。
4. 后续回合读取状态并注入相应规则。

状态：本地 hook 聚焦测试通过；真实宿主未运行。

### 调用链 3：OpenCode 注入

1. OpenCode 加载 `.opencode/plugins/ponytail.mjs`。
2. `experimental.chat.system.transform` 在每轮读取当前模式。
3. 若模式不是 `off`，将 `getPonytailInstructions(mode)` 追加到 system prompt。
4. `command.execute.before` 处理 `/ponytail` 命令并持久化模式。

状态：OpenCode plugin 聚焦测试通过；真实 OpenCode 未运行。

### 调用链 4：Pi extension 注入

1. Pi 加载 `pi-extension/index.js`。
2. extension 注册 `/ponytail`、`/ponytail-review`、`/ponytail-audit`、`/ponytail-debt`、`/ponytail-help`。
3. `before_agent_start` 按当前模式追加系统提示。
4. review/audit/debt/help 命令代理到 skill。

状态：`npm test` 链式执行 Pi extension 测试，15 个测试通过；真实 Pi harness 未运行。

### 调用链 5：Codex / Claude Code 子代理启动

1. 宿主触发 `SubagentStart` hook。
2. `ponytail-subagent.js` 读取 `.ponytail-active` 当前模式。
3. 模式为 `off` 时保持静默。
4. 模式开启时调用 `getPonytailInstructions(mode)` 并通过 `writeHookOutput('SubagentStart', ...)` 输出。

状态：`tests/hooks.test.js` 覆盖 Claude 和 Codex 分支；真实宿主未运行。

## 8. 客观评价

### 优点

- 规则源集中，adapter 薄，适合学习跨 Agent 平台的分发设计。
- 对 over-engineering 有明确、可执行的检查语义，不只是笼统提示“写简单点”。
- 有 hook、Windows、OpenCode、Pi、OpenClaw、Gemini、Copilot、command 文件同步等回归测试。
- benchmark 文档主动标注了 Claude 结果、OpenAI reasoning 模型成本反转、Gemini quota 待复现等边界。

### 缺点

- 本质上是规则和技能注入，不是可独立执行任务的 Agent 框架。
- always-on ruleset 每轮注入可能增加输入 token 和推理开销；短任务或 reasoning 模型上不一定省钱。
- “最小实现”规则如果被误用，可能与团队架构约束、长期可维护性或显式产品要求冲突。
- 真实宿主中的 hook 信任、SubagentStart 子代理注入和 statusline 体验仍未验证。

### 适用场景

- 给 AI 编码助手加“先删复杂度”的工作流约束。
- 学习 Codex / Claude Code lifecycle hook 和 skill 分发。
- 审查 diff 或全仓库中的过度抽象、冗余依赖和手写标准库。
- 研究 prompt benchmark 如何同时记录 LOC、成本、延迟和正确性 gate。

### 不适用场景

- 需要完整 Agent planning、工具编排、长期 memory 或多 Agent 协作。
- 无法接受第三方 plugin hook 进入主力开发配置的环境。
- 把 benchmark headline 当作所有模型、所有 session 都成立的成本承诺。
- 安全、支付、合规、数据迁移等高风险改动中用“少写”覆盖必要验证。

## 9. 总结

Ponytail 值得作为 `agentic-coding` 方向 Level B 收录。它提供了一个很清晰的样例：如何把工程判断变成可复用 skill，并通过插件、hooks、commands 和规则文件分发到多种 AI 编码宿主。下一步的关键不是继续摘录 README，而是在隔离 profile 中验证真实 Codex / Claude Code 安装、hook 信任、mode 切换和完整测试环境。

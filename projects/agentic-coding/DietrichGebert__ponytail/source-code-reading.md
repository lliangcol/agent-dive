# Ponytail 源码阅读记录

## 1. 阅读目标

- 本轮要理解的问题：Ponytail 如何把同一套最小实现规则分发到多个 AI 编码宿主。
- 关联功能：skill、AGENTS 规则、插件 manifest、生命周期 hook、模式配置、OpenCode / Pi 适配、benchmark 和测试。
- 预期产出：确认核心模块边界、调用链、运行验证命令和未验证风险。

## 2. 源码入口

| 入口 | 路径 | 作用 | 验证状态 |
|---|---|---|---|
| 核心 skill | `skills/ponytail/SKILL.md` | 完整 lazy senior dev mode 指令、强度级别和边界 | 已读取 |
| 通用规则 | `AGENTS.md` | 给 instruction-only Agent 读取的紧凑规则 | 已读取 |
| instruction builder | `hooks/ponytail-instructions.js` | 读取 skill 并按模式过滤注入内容 | 已读取 |
| 配置解析 | `hooks/ponytail-config.js` | 解析默认模式、config 路径、Claude 配置目录 | 已读取 |
| runtime 输出 | `hooks/ponytail-runtime.js` | 根据 Codex / Copilot / Claude 输出不同 hook payload | 已读取 |
| SessionStart hook | `hooks/ponytail-activate.js` | 激活模式、写状态文件、输出上下文 | 已读取 |
| UserPromptSubmit hook | `hooks/ponytail-mode-tracker.js` | 解析 `/ponytail` 等命令并切换模式 | 已读取 |
| Codex manifest | `.codex-plugin/plugin.json` | Codex 插件元数据、skills 目录和 UI 信息 | 已读取 |
| Claude manifest | `.claude-plugin/plugin.json` | Claude Code 插件元数据 | 已读取 |
| Copilot manifest | `.github/plugin/plugin.json` | Copilot CLI 插件命令、skills、hooks 入口 | 已读取 |
| OpenCode plugin | `.opencode/plugins/ponytail.mjs` | 每轮 system prompt transform 和 mode persistence | 已读取 |
| Pi extension | `pi-extension/index.js` | Pi 命令注册、session mode 和 system prompt 注入 | 已读取 |
| Gemini extension | `gemini-extension.json` | 指向 `AGENTS.md` 的 extension manifest | 已读取 |
| 便携性说明 | `docs/agent-portability.md` | 宿主到文件的映射表 | 已读取 |

## 3. 模块地图

| 模块 | 路径 | 职责 | 依赖关系 |
|---|---|---|---|
| Core rules | `skills/ponytail/SKILL.md`、`AGENTS.md` | 定义决策梯、强度、边界、输出格式 | 被 hooks、extensions、instruction-only adapters 复用 |
| Skill commands | `skills/ponytail-review`、`skills/ponytail-audit`、`skills/ponytail-debt`、`skills/ponytail-help` | 复杂度审查、全仓审计、债务台账、帮助 | 被 Codex、Claude、Pi、OpenCode、Gemini 等宿主暴露 |
| Command adapters | `commands/*.toml`、`.opencode/command/*.md` | 把 skill 命令映射到宿主命令格式 | 与 Pi command set 有测试同步 |
| Hook config | `hooks/claude-codex-hooks.json`、`hooks/copilot-hooks.json` | 声明生命周期 hook | 指向 `hooks/*.js` |
| Hook runtime | `hooks/ponytail-*.js` | 配置、状态、规则生成、宿主输出 | 读写 `.ponytail-active` 和 config |
| Plugin manifests | `.codex-plugin/`、`.claude-plugin/`、`.github/plugin/` | 宿主插件元数据 | 引用 commands、skills、hooks |
| Other adapters | `.cursor/`、`.windsurf/`、`.clinerules/`、`.kiro/`、`.openclaw/`、`gemini-extension.json`、`.agents/` | instruction-only 或生成式适配 | 需要与核心规则保持一致 |
| Benchmark | `benchmarks/`、`examples/` | promptfoo 配置、LOC/correctness 指标、示例输出 | 依赖 Node、Python、pandas、API key |
| Tests | `tests/`、`pi-extension/test/` | adapter 文件存在、hook 行为、SubagentStart、Windows regression、rule copy、一致性 | 临时 venv 中 full pass |

## 4. 关键发现

### 4.1 单一规则源不是完全单文件

Ponytail 的主规则在 `skills/ponytail/SKILL.md`，紧凑版在 `AGENTS.md`，并通过 `scripts/check-rule-copies.js` 检查规则副本一致性。`docs/agent-portability.md` 明确要求 adapter 保持 thin，宿主支持 skills 或 hooks 时优先指向现有目录。

### 4.2 Codex 与 Copilot 通过环境变量区分

`hooks/ponytail-runtime.js` 使用：

- `PLUGIN_DATA` 判断 Codex。
- `COPILOT_PLUGIN_DATA` 判断 Copilot。
- 如果两者都存在，Copilot 优先。

这影响状态文件写入目录和 stdout payload 格式。测试覆盖了 Copilot 不应误写 Codex `PLUGIN_DATA` 的场景。

### 4.3 Windows hook 有明确回归测试

`tests/hooks-windows.test.js` 防止 `commandWindows` 使用 cmd.exe 的 `%VAR%` 语法，并检查 hook 命令引用的脚本确实存在。这对跨平台插件很关键，因为 PowerShell 不会展开 `%CLAUDE_PLUGIN_ROOT%`。

### 4.4 benchmark 自带边界说明

`benchmarks/README.md`、`benchmarks/results/2026-06-17-cost-verification.md`、`benchmarks/results/2026-06-18-agentic.md` 和 `benchmarks/results/2026-06-22-issue-245-217-comprehension.md` 不只展示正向结论，也记录了 OpenAI reasoning 模型成本可能升高、Gemini quota 未完成、React / FastAPI correctness 只是结构检查、agentic safety / comprehension 需要单独看等边界。收录时不能把 README headline 简化成“所有场景都省钱”。

## 5. 推荐阅读顺序

1. `README.md`：先确认项目定位、安装面和 benchmark 宣称。
2. `AGENTS.md` 与 `skills/ponytail/SKILL.md`：理解规则本体。
3. `docs/agent-portability.md`：看宿主文件映射。
4. `hooks/ponytail-config.js`、`hooks/ponytail-instructions.js`、`hooks/ponytail-runtime.js`：看共享逻辑。
5. `hooks/ponytail-activate.js`、`hooks/ponytail-mode-tracker.js`：看事件触发。
6. `.codex-plugin/plugin.json`、`.claude-plugin/plugin.json`、`.github/plugin/plugin.json`：看插件元数据。
7. `.opencode/plugins/ponytail.mjs`、`pi-extension/index.js`：看非 Codex / Claude 宿主。
8. `tests/*.test.js`、`pi-extension/test/*.test.js`：用测试确认边界。
9. `benchmarks/README.md` 与 `benchmarks/results/`：读 benchmark 方法和限制。

## 6. 待源码确认项

- [ ] Codex desktop 安装后真实插件路径和 `PLUGIN_DATA` 布局。
- [ ] Claude Code `/hooks` 信任流程与 hook stdout 是否与当前宿主版本完全兼容。
- [ ] 真实宿主中的 `SubagentStart` 是否与本地测试输出一致。
- [ ] `.openclaw/skills/` 是否在 release 流程中持续由 `skills/` 生成。
- [ ] `.agents/plugins/marketplace.json` 对 Antigravity / VS Code Codex 的真实读取路径。
- [x] `package.json` 版本与插件 manifest / release 版本是否一致；2026-06-25 快照均为 `4.8.3`。

## 7. 本轮验证命令

已执行：

```powershell
git ls-remote --symref https://github.com/DietrichGebert/ponytail HEAD
git clone --depth 1 https://github.com/DietrichGebert/ponytail <temp>\ponytail
node --version
npm --version
node scripts\check-rule-copies.js
npm test
python --version
python -c "import pandas; print(pandas.__version__)"
```

结果摘要：

- Node `v24.16.0`、npm `11.13.0`、Python `3.12.13`。
- `node scripts\check-rule-copies.js` 通过。
- 用户级 `python -c "import pandas"` 报 `ModuleNotFoundError`。
- 临时 venv 安装 `pandas 3.0.3` 后，需要额外提供 venv-local `python3.exe`，因为 upstream correctness harness 优先探测 `python3`。
- `npm test` 全量通过：主仓库 61/61，Pi extension 15/15。

# Ponytail 验证证据

## 1. 快照信息

- 验证日期：2026-06-25
- GitHub：https://github.com/DietrichGebert/ponytail
- 项目 ID：`DietrichGebert__ponytail`
- 分类：`agentic-coding`
- 默认分支：`main`
- 收录快照 HEAD：`a945778b4a73b0b78c3c781a594b62cd3a324637`
- 收录时最新 release：`v4.8.3`，发布时间 `2026-06-24T02:38:23Z`
- release 名称：`v4.8.3: lazy in subagents too`
- License：MIT
- 主语言：JavaScript

## 2. GitHub 元数据

2026-06-25 通过 GitHub REST API 获取：

| 字段 | 值 |
|---|---:|
| stars | 56052 |
| forks | 2833 |
| open issues | 71 |

其他字段：

- `pushed_at`：`2026-06-24T13:37:06Z`
- `created_at`：`2026-06-12T00:52:37Z`
- `updated_at`：`2026-06-25T06:36:25Z`

## 3. 已执行命令

### 3.1 Git 分支和 commit

```powershell
git ls-remote --symref https://github.com/DietrichGebert/ponytail HEAD
```

结果摘要：

- 收录时 `HEAD` 指向 `refs/heads/main`。
- 收录时 commit 为 `a945778b4a73b0b78c3c781a594b62cd3a324637`。

### 3.2 临时浅克隆

```powershell
git clone --depth 1 https://github.com/DietrichGebert/ponytail <temp>\ponytail
git rev-parse HEAD
```

结果摘要：

- 临时浅克隆成功。
- `git rev-parse HEAD` 返回 `a945778b4a73b0b78c3c781a594b62cd3a324637`。
- 源码未写入当前仓库 `.cache/`，只用于本轮只读检查。

### 3.3 版本和依赖环境

```powershell
node --version
npm --version
python --version
python -c "import pandas; print(pandas.__version__)"
```

结果摘要：

- Node：`v24.16.0`
- npm：`11.13.0`
- Python：`3.12.13`
- 用户级 `python -c "import pandas"`：`ModuleNotFoundError`
- 临时 venv：`pandas 3.0.3`
- Windows 下 `python3.exe` 默认指向 uv 全局解释器；本轮为验证 upstream harness，复制临时 venv 的 `python.exe` 为 venv-local `python3.exe` 并把 venv `Scripts` 放到 `PATH` 前面。

### 3.4 规则副本检查

```powershell
node scripts\check-rule-copies.js
```

结果摘要：

- 通过。
- 输出显示 rule copies 匹配 `AGENTS.md`，并且 8 条 rule invariants 存在于 `SKILL.md` 与 `AGENTS.md`。

### 3.5 未补齐 venv 前的全量测试

```powershell
npm test
```

结果摘要：

- 主仓库 61 个测试中 60 个通过，1 个失败。
- 失败项：`csv: correct pandas one-liner passes`。
- 原因：`benchmarks/correctness.js` 优先探测 `python3`，本机 `python3.exe` 指向无 pandas 的 uv 全局解释器；只让临时 venv 的 `python` 可用不足以覆盖该探测顺序。

### 3.6 临时 venv 补齐 pandas 后的全量测试

```powershell
python -m venv .venv-agentdive
.\.venv-agentdive\Scripts\python -m pip install --upgrade pip pandas
Copy-Item .\.venv-agentdive\Scripts\python.exe .\.venv-agentdive\Scripts\python3.exe -Force
$env:PATH = (Resolve-Path .\.venv-agentdive\Scripts).Path + ';' + $env:PATH
npm test
```

结果摘要：

- 主仓库 61 个测试通过。
- `npm test` 链式执行 `npm test --prefix pi-extension`，Pi extension 15 个测试通过。
- 覆盖范围包括 behavior gate、command adapter、Copilot plugin、correctness gate、Gemini extension、Windows hook、SubagentStart hook、OpenClaw skill、OpenCode plugin、uninstall script 和 Pi extension。

### 3.7 版本一致性

```powershell
Get-Content package.json
Get-Content .codex-plugin\plugin.json
Get-Content .claude-plugin\plugin.json
Get-Content .github\plugin\plugin.json
```

结果摘要：

- `package.json` 版本为 `4.8.3`。
- Codex plugin manifest 版本为 `4.8.3`。
- Claude Code plugin manifest 版本为 `4.8.3`。
- Copilot plugin manifest 版本为 `4.8.3`。

## 4. 已阅读文件

- `README.md`
- `AGENTS.md`
- `docs/agent-portability.md`
- `package.json`
- `LICENSE`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `.github/plugin/plugin.json`
- `gemini-extension.json`
- `.opencode/plugins/ponytail.mjs`
- `pi-extension/index.js`
- `hooks/claude-codex-hooks.json`
- `hooks/copilot-hooks.json`
- `hooks/ponytail-config.js`
- `hooks/ponytail-instructions.js`
- `hooks/ponytail-activate.js`
- `hooks/ponytail-mode-tracker.js`
- `hooks/ponytail-runtime.js`
- `hooks/ponytail-subagent.js`
- `skills/ponytail/SKILL.md`
- `skills/ponytail-review/SKILL.md`
- `skills/ponytail-audit/SKILL.md`
- `skills/ponytail-debt/SKILL.md`
- `commands/ponytail.toml`
- `benchmarks/README.md`
- `benchmarks/results/2026-06-17-cost-verification.md`
- `benchmarks/results/2026-06-18-agentic.md`
- `benchmarks/results/2026-06-22-issue-245-217-comprehension.md`
- `tests/hooks.test.js`
- `tests/hooks-windows.test.js`
- `tests/commands.test.js`
- `tests/correctness.test.js`

## 5. 未验证内容

- `not_run`：未在真实 Codex、Codex desktop、Claude Code、Copilot CLI、OpenCode、Gemini CLI、Pi 或 OpenClaw 中安装。
- `not_run`：未信任真实 lifecycle hooks。
- `not_run`：未在真实 Codex / Claude Code 宿主中验证 `SubagentStart` 是否给子代理注入规则。
- `not_run`：未执行 promptfoo API benchmark。
- `not_run`：未验证真实 statusline 展示。
- `not_run`：未验证跨平台 shell 中 Node PATH 行为。
- `partial`：源码阅读为抽样阅读，未逐行阅读全部 adapters、benchmark scripts 和 examples。

## 6. 证据结论

Ponytail 与 AI 编码 Agent 明确相关，具备标准收录价值。当前可以确认其规则源、插件 manifest、生命周期 hook、OpenCode / Pi / Gemini 等适配和测试结构；最新快照 full `npm test` 已在临时 venv 中通过。由于真实宿主安装、hook 信任、SubagentStart 宿主行为和 API benchmark 未运行，项目状态保持 `analyzing`，是否跑通为“否”，源码分析和图解为“部分”。

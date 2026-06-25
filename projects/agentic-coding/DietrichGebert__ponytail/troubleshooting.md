# Ponytail 问题排查记录

## 1. `npm test` 在 CSV correctness 失败

现象：

- 未设置 venv-local `python3.exe` 时，`npm test` 输出 61 个测试，60 个通过，1 个失败。
- 失败项：`csv: correct pandas one-liner passes`。

本轮确认：

```powershell
python --version
python -c "import pandas; print(pandas.__version__)"
```

结果：

- Python 为 `3.12.13`。
- 用户级 `import pandas` 报 `ModuleNotFoundError`。
- 临时 venv 中 `pandas 3.0.3` 可用。

原因判断：

- upstream workflow 的 `.github/workflows/test.yml` 在 `npm test` 前执行 `pip install pandas`。
- 最新 correctness harness 优先探测 `python3`，Windows 下本机 `python3.exe` 可能不是临时 venv 的解释器。
- 只把 venv `python.exe` 放到 PATH 前面仍可能失败；本轮复制 venv `python.exe` 为 venv-local `python3.exe` 后 full `npm test` 通过。

建议：

- 用临时 venv 安装 pandas，并确认 `python3 -c "import pandas"` 命中同一 venv。
- 不要安装到用户全局 Python。
- 若仍失败，先检查 `Get-Command python3`。

## 2. lifecycle hooks 没有生效

可能原因：

- Node 不在非交互式 shell 的 `PATH`。
- 宿主未信任 hook。
- Codex / Copilot / Claude 的插件数据目录环境变量不符合预期。
- 默认模式为 `off`。

检查方向：

- 在同样的非交互式 shell 中执行 `node --version`。
- Codex 场景检查 `PLUGIN_DATA` 目录中是否出现 `.ponytail-active`。
- Copilot 场景检查 `COPILOT_PLUGIN_DATA` 目录。
- Claude Code 场景检查 `CLAUDE_CONFIG_DIR` 或 `~/.claude`。

## 3. Windows hook 路径错误

Ponytail 的测试已覆盖一个关键回归：Windows `commandWindows` 必须使用 PowerShell `$env:VAR` 语法，不能使用 cmd.exe 的 `%VAR%`。如果 Windows 下 hook 报找不到路径，应先检查：

- 当前安装的 `hooks/claude-codex-hooks.json` 或 `hooks/copilot-hooks.json` 是否和源码一致。
- `commandWindows` 中是否仍有 `%CLAUDE_PLUGIN_ROOT%`。
- 被引用的 `hooks/*.js` 是否真实存在。

本轮聚焦测试里 `tests/hooks-windows.test.js` 已通过。

## 4. mode 切换不符合预期

Ponytail 会识别：

- `/ponytail lite`
- `/ponytail full`
- `/ponytail ultra`
- `/ponytail off`
- `@ponytail lite`
- `$ponytail ultra`
- `stop ponytail`
- `normal mode`

排查方向：

- 确认宿主是否把用户输入传给 `UserPromptSubmit` hook。
- 检查 `.ponytail-active` 中的模式值。
- 检查 `PONYTAIL_DEFAULT_MODE` 是否覆盖了 config。
- 检查 config 文件 `defaultMode` 是否为允许值。

## 5. README benchmark 与本机结果不一致

常见原因：

- README 的主结论主要来自 Claude API 单轮 promptfoo benchmark。
- benchmark 成本不是订阅 plan quota，而是 API telemetry。
- OpenAI reasoning 模型可能因 ruleset 输入和 reasoning token 额外开销导致成本升高。
- Gemini 结果在 upstream cost verification 文档中仍有 quota 未完成边界。
- React 和 FastAPI correctness 不是完整运行时测试，包含结构性判断。

处理方式：

- 复现时记录模型、日期、repeat、promptfoo config、API provider、失败样本和排除规则。
- 不把一次小样本复现推广到所有模型或真实多轮 session。

## 6. 与仓库自身规则冲突

Ponytail 是“更少实现”的偏好注入，不是上位规则。若目标仓库已有 AGENTS、CLAUDE、合规、支付、安全或测试规则，应优先遵守目标仓库规则。对高风险改动，Ponytail 可以用于删除无关抽象，但不能删掉必要校验、审计证据和回归测试。

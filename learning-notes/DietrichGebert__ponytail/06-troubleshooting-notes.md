# Ponytail 排查笔记

## full npm test 的 Python 解释器

本机直接跑 `npm test` 时，CSV correctness benchmark 需要 pandas。上游 GitHub Actions 明确先安装 pandas；Windows 下还要注意 correctness harness 优先探测 `python3`。

当前处理：

- tests_status 已更新为 `pass`。
- evidence 记录了未设置 venv-local `python3.exe` 时的 60/61 失败，以及设置后 full pass。
- 不污染用户级 Python 环境。

## Windows hooks

Windows hook 排查优先看 PowerShell 语法。Ponytail 已有测试防止 `%VAR%` 这种 cmd.exe 写法出现在 `commandWindows` 中。

## Node PATH

README 明确提醒 Claude Code 和 Codex plugins 运行 Node lifecycle hooks。nvm、Nix 或非交互 shell 可能导致交互式终端能找到 Node，但 hook 运行时找不到。

## 模式没生效

优先检查：

- 是否已经信任 hooks。
- 状态文件所在目录是否正确。
- 环境变量是否设置了 `PONYTAIL_DEFAULT_MODE=off`。
- 用户输入是否被宿主传给 `UserPromptSubmit`。
- 子代理场景是否触发 `SubagentStart`。

## Benchmark 差异

如果复现结果和 README 不同，先记录 provider、模型、日期、repeat、promptfoo 版本和 API telemetry。不要只比较 headline。

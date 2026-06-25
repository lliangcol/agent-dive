# Ponytail 复习题

## 概念题

1. Ponytail 的六级决策梯分别是什么？
2. `lite`、`full`、`ultra` 三种模式的差异是什么？
3. 为什么 Ponytail 不能替代安全、正确性和可访问性检查？
4. instruction-only adapter 和 plugin / hook adapter 的能力差异是什么？
5. 为什么 README 的成本结论不能泛化到所有模型和多轮 session？

## 源码题

1. `getDefaultMode` 的配置优先级是什么？
2. `getPonytailInstructions` 如何按模式过滤 skill 内容？
3. `writeHookOutput` 如何区分 Codex、Copilot 和 Claude Code？
4. `ponytail-mode-tracker.js` 支持哪些命令前缀？
5. `ponytail-subagent.js` 在模式关闭和开启时分别输出什么？
6. Windows hook 测试防止了哪类路径变量错误？

## 实操题

1. 在临时环境中让 `node scripts\check-rule-copies.js` 通过。
2. 说明为什么 Windows 下只补齐 venv `python` 不一定足够，以及如何确认 `python3` 命中 venv。
3. 在隔离 Codex profile 中安装插件并验证 `@ponytail ultra`。
4. 用临时 `CLAUDE_CONFIG_DIR` 验证 SessionStart 和 SubagentStart hook 输出。
5. 复现一轮小样本 benchmark，并标明模型、日期、repeat 和成本口径。

## 当前答题状态

尚未完成复习题。完成前不把 `review_questions_done` 改为 true。

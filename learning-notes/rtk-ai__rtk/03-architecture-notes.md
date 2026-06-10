# RTK 架构笔记

## 初步模块图

- `src/main.rs`：CLI facade。
- `src/cmds/`：按生态拆分的过滤器。
- `src/core/`：runner、stream、config、tracking、tee、telemetry、filter。
- `src/discover/`：rewrite registry、lexer、rules、report。
- `src/hooks/`：hook lifecycle、permission、integrity、rewrite command。
- `hooks/`：部署到各 Agent 的 thin delegates。

## 关键判断

- RTK 的核心不是“让模型更聪明”，而是改变工具输出进入上下文的形态。
- hook 只是改写入口；实际过滤仍然发生在 RTK binary 内。
- Codex 集成目前应按 prompt guidance 理解，不能假定自动拦截命令。
- tee recovery 是过滤工具必须有的安全阀，后续需要重点验证。

## 待补

- 画出每个 command ecosystem 的 filter 策略。
- 阅读 `src/parser/` 如何支撑测试输出解析。
- 确认 telemetry 编译期开关和运行时 consent 判断。

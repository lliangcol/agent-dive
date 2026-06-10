# RTK 学习计划

## 学习目标

- 理解 RTK 在 AI coding workflow 中解决的上下文成本问题。
- 跑通最小 rewrite 和过滤命令。
- 源码确认 hook rewrite、command filters、tracking 和 tee recovery。
- 明确 Codex / Claude Code / Cursor 等 Agent 集成机制差异。

## 阶段计划

1. 文档理解：README、INSTALL、architecture、hooks、telemetry。
2. 本机 smoke：安装来源、版本、`rtk rewrite`、`rtk git status`。
3. 源码阅读：`src/main.rs`、`src/discover/`、`src/hooks/`、`src/core/`、`src/cmds/`。
4. 集成验证：先隔离配置目录，再单 Agent 安装。
5. 总结对比：与 Caveman、Graphify、CodeGraph 做上下文治理对比。

## 当前边界

本轮只完成收录和源码抽样，没有安装和运行 RTK。

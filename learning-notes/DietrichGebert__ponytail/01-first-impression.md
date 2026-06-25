# Ponytail 第一印象

## 项目印象

Ponytail 不是一个执行任务的 Agent，也不是代码生成模型封装。它更像一个“工程判断偏好包”：把少抽象、少依赖、少 boilerplate 的判断前置到 Agent 每次写代码之前。

最有价值的点在于它不是只写一句“保持简单”。仓库把规则做成了：

- `skills/ponytail/SKILL.md` 的完整技能。
- `AGENTS.md` 的紧凑 always-on 指令。
- Codex / Claude / Copilot 的插件 manifest。
- OpenCode / Pi 的运行时适配。
- Cursor / Windsurf / Cline / Kiro 等规则文件。
- promptfoo benchmark 和 correctness gate。

## 初步判断

适合 Level B 标准收录。它对 AgentDive 的价值在于展示“如何分发 Agent 行为规则”和“如何用测试守住多平台 adapter 不漂移”。

## 需要警惕

- README 的成本和速度数字需要按模型、日期、provider 和单轮/多轮边界记录。
- “少写代码”不等于少验证；项目自身也强调 trust boundary、安全、可访问性和非平凡逻辑的一条可运行检查。
- 真实安装需要信任 lifecycle hooks，不能直接放进主力环境。

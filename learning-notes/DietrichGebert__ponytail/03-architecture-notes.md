# Ponytail 架构笔记

## 架构分层

Ponytail 的架构可以理解为五个层次：

1. 规则层：`skills/ponytail/SKILL.md` 和 `AGENTS.md`。
2. 命令层：review、audit、debt、help 等技能和宿主命令文件。
3. 注入层：`hooks/ponytail-instructions.js` 负责按模式生成上下文。
4. 状态层：`ponytail-config.js` 和 `ponytail-runtime.js` 负责默认模式、状态文件和宿主输出协议。
5. 适配层：不同平台的 manifest、plugin、extension、rules 文件。

## 关键设计

- adapter 要薄：能引用 `skills/` 和 `hooks/` 时就不复制逻辑。
- mode 是持久化状态：通过 `.ponytail-active` 或宿主配置目录保存。
- 默认模式可配置：环境变量优先，其次用户级 config，最后 `full`。
- 输出协议分宿主：Codex JSON、Copilot additionalContext、Claude text。
- 测试防漂移：command 文件、OpenClaw skill、Windows hook、manifest 版本都有测试。

## 架构风险

- 多宿主适配文件多，版本和行为容易漂移。
- ruleset 每轮注入对 token 成本有影响。
- instruction-only 宿主没有 mode 切换和 hook 能力，体验不等价。
- 用户级 config 和环境变量可能让团队中的 Agent 行为不一致。

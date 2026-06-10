# ECC 第一印象

## 一句话定位

ECC 更像一套跨 AI 编码工具的工作流操作系统，而不是单纯 prompt library、dotfiles 或某个 Agent SDK。

## 初步亮点

- 把 skills、agents、commands、rules、hooks、MCP config、installer、sessions、operator tools 放到同一工程体系里。
- 对 Codex、Claude Code、OpenCode、Cursor 等 harness 的边界有明确描述。
- 安装和治理不只依赖 README 手工复制，而是有 selective install 和 manifest 概念。
- 适合学习 agentic coding 的治理、验证、上下文和安全边界。

## 初步风险

- 范围很大，必须拆主题学习。
- 安装可能影响用户级配置，需要先 dry-run。
- Hook 行为依赖 harness，不能跨工具泛化。
- 能力数量可能随 release 漂移。

## 待验证问题

- `ecc plan` 的输出是否能准确解释写入范围。
- Codex plugin 实际暴露哪些 skills 和 MCP 配置。
- Claude plugin hooks 是否稳定触发。
- `npm test` 和 catalog validators 是否通过。

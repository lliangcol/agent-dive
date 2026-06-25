# Ponytail 源码阅读笔记

## 已读主线

本轮已经阅读：

- `skills/ponytail/SKILL.md`
- `AGENTS.md`
- `docs/agent-portability.md`
- `hooks/ponytail-config.js`
- `hooks/ponytail-instructions.js`
- `hooks/ponytail-activate.js`
- `hooks/ponytail-mode-tracker.js`
- `hooks/ponytail-runtime.js`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `.github/plugin/plugin.json`
- `.opencode/plugins/ponytail.mjs`
- `pi-extension/index.js`
- `tests/hooks.test.js`
- `tests/hooks-windows.test.js`
- `tests/commands.test.js`

## 重要源码点

- `filterSkillBodyForMode` 只过滤强度表和示例，不会误删普通带冒号的规则 bullet。
- `getPonytailInstructions` 读取 skill 文件失败时有 fallback 指令。
- `getDefaultMode` 的顺序是 env、config、default。
- `getClaudeDir` 支持 `CLAUDE_CONFIG_DIR`，便于隔离测试。
- `writeHookOutput` 对 Codex、Copilot、Claude 三种输出协议不同。
- `ponytail-mode-tracker.js` 支持 `/`、`@`、`$` 三类前缀。

## 待继续阅读

- `hooks/ponytail-statusline.ps1` 和 `hooks/ponytail-statusline.sh`。
- `.openclaw/skills/` 生成流程。
- benchmark 里的 `loc.js`、`behavior.js`、`robustness-audit.js`。
- examples 的真实 model output 与 correctness gate 对照。

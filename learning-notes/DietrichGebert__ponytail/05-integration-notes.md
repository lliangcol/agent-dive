# Ponytail 集成笔记

## Codex

Codex 是最值得优先验证的宿主。关键点不是 marketplace 命令是否能运行，而是安装后 `/hooks` 信任流程和 `PLUGIN_DATA` 状态目录。

待验证：

- `SessionStart` 是否注入 `systemMessage` 和 additional context。
- `@ponytail lite` 是否写 `.ponytail-active`。
- `@ponytail off` 或 `normal mode` 是否关闭。
- Codex desktop 重启后是否加载同一个插件。

## Claude Code

Claude Code 需要重点看 `CLAUDE_CONFIG_DIR` 和 statusline。Ponytail 会在缺少 statusLine 时提示用户配置，但本次没有让它修改真实 `~/.claude/settings.json`。

## OpenCode

OpenCode plugin 直接在 system prompt transform 中追加规则，设计清晰。风险是它依赖 OpenCode 的 plugin API 名称，例如 `experimental.chat.system.transform` 和 `command.execute.before`，这些 API 如果变化，适配会断。

## Pi

Pi extension 的测试比较完整，覆盖命令解析、session mode 和 default mode。真实 harness 还没跑，不能写成 runtime pass。

## Instruction-only

Cursor、Windsurf、Cline、Kiro、Copilot editor、VS Code Codex extension 主要读取规则文件。这种集成最轻，但没有 hook 和 mode persistence，适合低风险试用。

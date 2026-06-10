# RTK 集成笔记

## 当前状态

未集成。

## 目标路径

1. 本地显式命令：先用 `rtk git status`、`rtk git diff`、`rtk test` 验证价值。
2. Codex：验证 `rtk init --codex` 写入 `$CODEX_HOME` 或 `~/.codex` 的 `RTK.md` / `AGENTS.md` 关系。
3. Claude Code：验证 transparent PreToolUse hook、permission ask / allow / deny 行为。
4. Cursor / Gemini / Hermes：后续按需要验证。

## 写入范围记录模板

| Agent | 命令 | 写入文件 | 备份 | 回滚 | 状态 |
|---|---|---|---|---|---|
| Codex | 待填 | 待填 | 待填 | 待填 | 未验证 |
| Claude Code | 待填 | 待填 | 待填 | 待填 | 未验证 |

## 集成原则

- 先手动命令，再 hook。
- 先 project / temp config，再 global。
- 先确认 raw output recovery，再依赖 filtered output。

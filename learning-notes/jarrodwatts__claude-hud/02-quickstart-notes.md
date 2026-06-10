# 快速开始笔记

## 官方路径

```text
/plugin marketplace add jarrodwatts/claude-hud
/plugin install claude-hud
/reload-plugins
/claude-hud:setup
```

setup 写入后需要完全重启 Claude Code。

## 当前状态

- 未在真实 Claude Code 中执行安装。
- 已确认 README 要求 Windows 使用 Node.js 18+。
- 已确认 setup command 会检测已有 statusline 并创建备份。

## 验证前检查

- [ ] 当前是否已有 `statusLine.command`。
- [ ] `node` 是否可用。
- [ ] 是否在 Git Bash/MSYS2/Cygwin，避免误用 PowerShell command format。
- [ ] 是否准备了恢复 `settings.json` 的备份路径。


# 问题排查笔记

## 已遇到

- GitHub REST API rate limit。
- Windows 临时克隆 `npm test` 失败，退出码 1。

## 待定位失败组

- `countConfigs`。
- `writeExternalUsageSnapshot`。
- `runExtraCmd`。
- `getGitStatus`。
- `index entrypoint`。
- integration newline / added dirs layout。
- `getClaudeCodeVersion`。

## 可能排查方向

- PowerShell vs Git Bash 行为差异。
- Windows 权限位和 POSIX 权限断言差异。
- `cmd.exe` / `.cmd` resolution。
- `mkdir -p` 在 Windows native shell 中不可用。
- CRLF / LF 期望差异。


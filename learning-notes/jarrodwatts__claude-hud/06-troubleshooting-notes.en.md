# Troubleshooting notes

## Encountered

- GitHub REST API rate limit.
- Windows temporary clone `npm test` failed with exit code 1.

## Failure group to be positioned

- `countConfigs`.
- `writeExternalUsageSnapshot`.
- `runExtraCmd`.
- `getGitStatus`.
- `index entrypoint`.
- integration newline / added dirs layout.
- `getClaudeCodeVersion`.

## Possible troubleshooting directions

- PowerShell vs Git Bash behavior differences.
- Windows permission bits and POSIX permission assertion differences.
- `cmd.exe` / `.cmd` resolution.
- `mkdir -p` is not available in Windows native shell.
- CRLF/LF Expectation Difference.

# Quickstart notes

## Official path

```text
/plugin marketplace add jarrodwatts/claude-hud
/plugin install claude-hud
/reload-plugins
/claude-hud:setup
```

Claude Code needs to be completely restarted after setup is written.

## Current status

- The installation was not performed in real Claude Code.
- Confirmed README requires Node.js 18+ for Windows.
- Confirmed setup command will detect existing statusline and create backup.

## Check before verification

- [ ] Whether there is currently `statusLine.command`.
- [ ] `node` is available.
- [ ] Whether in Git Bash/MSYS2/Cygwin to avoid misuse of PowerShell command format.
- [ ] Whether the backup path to restore `settings.json` is prepared.

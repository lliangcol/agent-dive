# Claude HUD 复习问题

1. Claude HUD 为什么选择 Claude Code statusline 而不是单独 TUI？
2. `src/index.ts` 的主调用链是什么？
3. `readStdin()` 如何避免没有 stdin 时卡住？
4. context percent 的 native value 和 fallback value 有什么差异？
5. transcript JSONL 中 tool、Agent、Todo 分别如何识别？
6. background Agent 的完成时间为什么不能只看 tool_result？
7. `config.json` 里哪些字段会影响 expanded layout？
8. setup 为什么要检测已有 statusline 并创建备份？
9. Windows PowerShell 和 Git Bash 的 statusLine command 为什么不能混用？
10. subscriber usage 为什么不能对 API-key-only 用户保证可见？
11. external usage snapshot 的路径和 freshness 有哪些限制？
12. 当前 Windows `npm test` 失败需要如何分组定位？


# 源码阅读笔记

## 已读

- `src/index.ts`
- `src/stdin.ts`
- `src/transcript.ts`
- `src/config.ts`
- `src/render/index.ts`
- `src/git.ts`
- `src/external-usage.ts`
- `.claude-plugin/plugin.json`
- `commands/setup.md`
- `commands/configure.md`

## 发现

- `MainDeps` 让主入口易于测试。
- `readStdin` 有 first byte timeout、idle timeout 和 256 KB 上限。
- context percent 优先使用 Claude Code native `used_percentage`。
- transcript cache 用 transcript path hash 隔离。
- `render/index.ts` 对 ANSI、OSC8 hyperlink、CJK/emoji 宽度做了专门处理。
- setup 对 Windows PowerShell 性能和 BOM 问题有明确处理。

## 待读

- `src/config-reader.ts`
- `src/extra-cmd.ts`
- `src/version.ts`
- `tests/core.test.js`
- `tests/integration.test.js`
- `tests/git.test.js`


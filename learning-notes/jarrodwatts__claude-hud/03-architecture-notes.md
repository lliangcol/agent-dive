# 架构笔记

## 主链路

Claude Code 调用 `statusLine.command`，把状态 JSON 通过 stdin 传给 HUD。HUD 再读取 transcript、配置、git 和其他本地状态，最后输出一组文本行。

## 关键组件

- `commands/setup.md`：写入 statusLine 的交互式流程。
- `commands/configure.md`：写入 HUD config 的交互式流程。
- `src/index.ts`：运行时编排入口。
- `src/stdin.ts`：statusline stdin 解析。
- `src/transcript.ts`：活动解析。
- `src/config.ts`：配置默认值、迁移和校验。
- `src/render/`：终端输出。

## 架构判断

Claude HUD 是单机本地观测层，不是 server-side observability。它的准确性依赖 Claude Code 提供的 stdin 和 transcript。


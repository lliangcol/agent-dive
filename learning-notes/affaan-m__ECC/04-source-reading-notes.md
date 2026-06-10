# ECC 源码阅读笔记

## 当前状态

只完成首轮文件级入口识别，未完成完整调用链阅读。

## 已识别入口

- `scripts/ecc.js`
- `scripts/install-plan.js`
- `scripts/install-apply.js`
- `scripts/lib/install-manifests.js`
- `scripts/lib/install-executor.js`
- `hooks/hooks.json`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `scripts/control-pane.js`

## 下一轮阅读问题

1. `SUPPORTED_INSTALL_TARGETS` 的每个 target adapter 在哪里注册。
2. profile、module、component 的 manifest schema 如何定义。
3. `applyInstallPlan()` 如何处理覆盖、备份、install-state。
4. hook profile minimal/standard/strict 如何生效。
5. Codex plugin 的 skills 路径和 MCP servers 路径如何被 Codex 读取。
6. control pane 的 read-only/action-enabled 边界如何实现。

## 待运行验证

- `npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json`
- `npm run catalog:check`
- `npm test`

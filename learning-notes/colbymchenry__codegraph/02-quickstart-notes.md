# CodeGraph 快速开始笔记

## 环境

- 日期：2026-06-11
- 范围：`.cache/sources/colbymchenry__codegraph`
- Git: 2.54.0.windows.1
- Node: v24.16.0
- npm: 11.9.0
- Commit：`16c73e2b0e027411e22039baeb32fbe60ab42b4c`

## 已完成

- `git clone --no-tags --depth 1` 成功，并检出预期 commit。
- `npm ci --ignore-scripts` 在缓存克隆内成功。
- `npm run build` 成功，并生成 `dist/bin/codegraph.js`。
- `node dist/bin/codegraph.js --version` 返回 `0.9.9`。
- `node dist/bin/codegraph.js --help` 展示了预期 CLI 命令集。
- `node dist/bin/codegraph.js init -i .` 完成索引。
- `node dist/bin/codegraph.js status .` 报告 216 files、3,533 nodes、14,388 edges、DB size 12.55 MB，且索引为 up to date。
- `node dist/bin/codegraph.js query buildContext -p . --json` 返回匹配的方法、接口和 import 节点。
- `node dist/bin/codegraph.js callers buildContext -p . --json` 返回有效 JSON，该符号 caller 为空。
- `node dist/bin/codegraph.js impact buildContext -p . --json` 返回两个受影响的 `buildContext` method 节点。
- `node dist/bin/codegraph.js serve --mcp --no-watch -p .` 接受 line-based JSON-RPC initialize 和 tools/list 消息。
- MCP tools/list 返回 `codegraph_search`、`codegraph_callers`、`codegraph_callees`、`codegraph_impact`、`codegraph_node`、`codegraph_explore`、`codegraph_status`、`codegraph_files`。
- `npx vitest run __tests__/context.test.ts` 通过 17 个测试。

## 待补

- 如后续学习任务需要，补充一次受控 MCP `tools/call` 采样。
- 运行完整测试套件，或明确认可的聚焦测试子集。
- 复核 npm audit 风险：`npm ci --ignore-scripts` 报告 8 个漏洞。

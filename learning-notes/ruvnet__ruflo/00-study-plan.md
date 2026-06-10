# Ruflo 学习计划

## 学习目标

- 理解 Ruflo 如何把 multi-agent swarm、MCP tools、memory、hooks 和 plugins 组合成 agent harness。
- 找到 Claude Code plugin、CLI full install、Codex `.agents` config 和 Web UI 的边界。
- 验证 Ruflo CLI、MCP server、init 写入范围和 hook 行为。
- 总结可借鉴和不可照搬的设计。

## 阶段安排

1. 文档阅读：README、package metadata、Claude plugin manifest、`.agents/config.toml`。
2. 只读验证：`ruflo --version`、`ruflo --help`、`ruflo mcp start --help`、`ruflo init --help`。
3. 源码阅读：wrapper、CLI/MCP entry、command registry、MCP tools、SwarmCoordinator、WorkflowEngine、HybridBackend。
4. 最小集成：临时项目验证 Claude plugin lite、CLI full init、MCP tool list、Codex `.agents`。
5. 对比复盘：与 ECC、CodeGraph、Graphify、Caveman 做边界对比。

## 当前边界

本笔记尚未包含任何本机运行结果。所有命令都需要后续单独记录输出。

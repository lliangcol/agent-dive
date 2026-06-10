# Ruflo 复盘总结

## 当前状态

尚未进入正式复盘。本文件用于后续完成运行验证、源码深读和最小集成后总结。

## 待回答问题

- Ruflo 的 multi-agent runtime 是否能独立于 Claude Code 稳定运行？
- MCP tool list 和 README 能力描述是否一致？
- Claude Code plugin lite 与 full install 的用户体验差异是否清晰？
- Codex `.agents` 路径能否作为可靠集成方式？
- hooks 默认 no-op on failure 的设计在安全和可用性之间如何取舍？
- Web UI / mcp-bridge 是否适合作为本地团队工具？

## 预期复盘维度

- 架构设计
- 本机运行稳定性
- 安全边界
- 可维护性
- 学习迁移价值
- 与 ECC / CodeGraph / Graphify / Caveman 的差异

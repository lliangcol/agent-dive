# Ruflo 集成笔记

## 集成策略

优先顺序：

1. 只读 CLI 验证。
2. MCP server tool list 验证。
3. Claude Code plugin lite 验证。
4. Codex `.agents` 验证。
5. 临时项目 CLI full init 验证。
6. Web UI / mcp-bridge 验证。

## 待验证清单

- [ ] `ruflo --version` 不触发 heavy import。
- [ ] `ruflo --help` 不写入文件。
- [ ] `ruflo mcp start --help` 可快速返回。
- [ ] `mcp start` stdout 保持 JSON-RPC。
- [ ] Claude plugin lite 不注册 full MCP server。
- [ ] CLI init 写入范围可审计、可回滚。
- [ ] Codex 能读取 `.agents/config.toml`。
- [ ] Codex 能暴露 `.agents/skills/*`。

## 风险边界

- 不在主力仓库直接执行 `init wizard`。
- 不把 Claude Code hook 行为推断到 Codex。
- 不把 hook 输出当作 CI gate。
- 不在未审计情况下启用 Web UI provider / token 配置。

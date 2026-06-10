# 第一印象

Claude HUD 的核心不是创建 Agent，而是把 Claude Code 会话运行状态放到一个始终可见的 statusline 上。它适合学习 Agent 工具链里的“运行期可观测性”。

第一眼最值得关注的点：

- setup 文档非常重，说明真实难点在跨平台 statusLine command 和用户配置保护。
- transcript 解析覆盖 tools、Skill、MCP、Agent、Todo，适合学习 Claude Code transcript 结构。
- 配置项很多，但默认保持相对克制。
- 当前 Windows 本地测试失败，后续需要把环境差异和项目问题分开。


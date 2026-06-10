# Claude HUD 学习计划

## 目标

- 理解 Claude Code statusline 插件的输入、输出和配置写入边界。
- 理解 transcript JSONL 如何变成工具、Agent、Todo 和 MCP 活动行。
- 验证 Windows 环境下测试失败和真实 setup 行为。

## 阶段

1. 文档阅读：README、README.zh.md、setup/configure command。
2. 源码阅读：`src/index.ts`、`src/stdin.ts`、`src/transcript.ts`、`src/config.ts`、`src/render/`。
3. 隔离验证：临时 `CLAUDE_CONFIG_DIR` 写入 settings 和 config。
4. 真实验证：测试 profile 中安装 plugin，重启 Claude Code。
5. 复盘：总结 statusline 观测层的工程边界。

## 当前记录

- 已完成 first-pass 收录。
- 已执行临时浅克隆 `npm ci` 和 `npm test`，测试失败。
- 未执行真实 Claude Code plugin install。


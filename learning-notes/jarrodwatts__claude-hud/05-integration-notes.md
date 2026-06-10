# 集成笔记

## 集成边界

Claude HUD 写的是用户级 Claude Code 配置，不应提交到业务仓库。真实执行前应备份 `settings.json`。

## 推荐验证顺序

1. 临时源码构建。
2. 临时 `CLAUDE_CONFIG_DIR` setup 写入。
3. 测试 Claude Code profile 安装。
4. 主力环境安装。

## 当前阻塞

- Windows `npm test` 失败。
- 未采样真实 Claude Code statusline stdin。
- 未采样真实 transcript JSONL。


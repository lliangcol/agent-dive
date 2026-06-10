# Hermes Agent 问题排查记录

当前尚未在本机执行 Hermes 安装或运行命令，因此本文件先记录预期排查清单。后续每遇到一个真实问题，应按“一问题一小节”补充错误原文、环境、复现步骤、定位过程和验证结果。

## 问题：安装脚本失败

- 发现时间：待验证
- 当前状态：未复现
- 影响范围：首次安装、依赖准备、CLI 启动

### 现象

待实际运行后记录。重点保留安装器输出，并删除本机账号、私有路径和密钥。

### 环境

- 操作系统：待记录
- 运行时版本：待记录
- 项目版本 / Commit：`a72bb03757c0c925c686f9774eefc8dc5a77b329`
- 关键依赖：Python 3.11、uv、Node.js、ripgrep、ffmpeg、Git Bash

### 初步判断

可能原因：

- 网络无法访问安装脚本、PyPI、npm、GitHub 或二进制下载源。
- Python / uv / Node.js 版本冲突。
- Windows 原生 shell 与 Git Bash 路径冲突。
- 终端权限、杀毒软件或代理配置阻断。

## 问题：Provider 或模型配置失败

- 发现时间：待验证
- 当前状态：未复现
- 影响范围：模型调用、工具网关、OAuth

### 初步判断

可能原因：

- API key 缺失、过期或写入位置不正确。
- provider/model alias 与 runtime provider resolution 不匹配。
- OAuth 未完成或 credential pool 未命中。
- base_url、region、组织 ID 或代理配置错误。

## 问题：工具调用权限过宽

- 发现时间：待验证
- 当前状态：未复现
- 影响范围：terminal、file、browser、MCP、remote backend

### 初步判断

需要重点检查：

- `hermes tools` 中启用的 toolsets。
- terminal backend 是否为 local、docker、ssh、modal、daytona 或 singularity。
- dangerous command approval 是否覆盖写入、删除、网络和凭据读取。
- MCP server 是否暴露了超出需求的 mutating tools。

## 问题：Gateway 消息无法收发

- 发现时间：待验证
- 当前状态：未复现
- 影响范围：Telegram、Discord、Slack、WhatsApp、Signal 等平台

### 初步判断

可能原因：

- 平台 token、OAuth 或 bot 权限配置错误。
- allowlist 或 DM pairing 未完成。
- session key 解析错误导致上下文不连续。
- delivery 失败但没有清晰暴露给用户。
- 多 profile 并发时 gateway PID 或 token lock 冲突。

## 问题：MCP server 不可用

- 发现时间：待验证
- 当前状态：未复现
- 影响范围：外部工具接入

### 初步判断

可能原因：

- stdio server 命令不可执行。
- remote HTTP server 不可达或 OAuth 未完成。
- tool include filter 配置错误。
- server probe 失败但安装流程使用了默认工具集。
- MCP tool schema 与 Hermes tool registry 包装不兼容。

## 定位过程模板

| 步骤 | 操作 | 结果 | 结论 |
|---|---|---|---|
| 1 | 记录命令和环境 | 待补充 | 待补充 |
| 2 | 查看 Hermes 输出和日志 | 待补充 | 待补充 |
| 3 | 最小化配置复现 | 待补充 | 待补充 |
| 4 | 对照源码和官方文档 | 待补充 | 待补充 |

## 待办检查项

- [ ] 记录首次安装错误或确认无错误。
- [ ] 记录 `hermes doctor` 输出。
- [ ] 记录 provider 配置结果。
- [ ] 记录至少一次只读工具调用。
- [ ] 记录 MCP / Gateway / Cron 的最小验证结果。

## 质量检查项

- [x] 未写入真实密钥或内部地址。
- [x] 未把未复现问题写成已解决。
- [x] 未把 README 说明当作本机运行结果。


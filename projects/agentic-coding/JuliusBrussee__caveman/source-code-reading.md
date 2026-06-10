# Caveman 源码阅读记录

## 1. 阅读目标

- 本轮要理解的问题：Caveman 如何把一套输出压缩规则分发到多个 AI 编码助手，并在 Claude Code / MCP / memory compression 场景中生效。
- 关联功能：统一安装器、skill 规则、Claude Code hooks、statusline、MCP shrink、memory file compression、cavecrew 子 Agent。
- 预期产出：确认核心模块边界、关键调用链、写入范围、卸载路径、测试覆盖和安全边界。

## 2. 源码入口

| 入口 | 路径 | 作用 | 依据 |
|---|---|---|---|
| 统一安装器 | `bin/install.js` | `caveman` package bin 入口，安装 / 卸载 / dry-run / provider matrix | `package.json`、INSTALL.md |
| 主 skill | `skills/caveman/SKILL.md` | 输出压缩行为规则和强度模式 | skill 文件 |
| Claude Code hook | `src/hooks/caveman-activate.js` | SessionStart 自动激活 | hooks README，待源码验证 |
| Mode tracker | `src/hooks/caveman-mode-tracker.js` | UserPromptSubmit 解析模式切换 | hooks README，待源码验证 |
| Statusline | `src/hooks/caveman-statusline.ps1` / `.sh` | 显示当前模式和节省统计 | hooks README，待运行验证 |
| MCP shrink | `src/mcp-servers/caveman-shrink/index.js` | MCP stdio proxy 入口 | MCP shrink README，待源码验证 |
| Memory compress | `skills/caveman-compress/scripts/cli.py` | 记忆文件压缩 CLI 线索 | tree、SECURITY.md，待源码验证 |
| OpenCode plugin | `src/plugins/opencode/plugin.js` | OpenCode 原生插件 | CLAUDE.md，待源码验证 |
| Tests | `tests/` | installer、hooks、compress、MCP shrink 等测试 | GitHub tree |

## 3. 模块地图

| 模块 | 路径 | 职责 | 依赖关系 |
|---|---|---|---|
| 安装器 | `bin/install.js`、`bin/lib/settings.js`、`bin/lib/openclaw.js` | 参数解析、provider detection、配置写入、dry-run、uninstall | 调用系统命令、读写 agent 配置，待源码验证 |
| Skill 源头 | `skills/` | 行为规则、命令说明、子 skill | 被插件分发和 `npx skills add` 消费 |
| 插件分发 | `.claude-plugin/`、`plugins/caveman/` | Claude Code plugin manifest 和镜像文件 | CLAUDE.md 称部分由 CI sync |
| 命令 stubs | `commands/` | Codex / Gemini slash command 模板 | 待确认被哪些安装路径读取 |
| Claude hooks | `src/hooks/` | 激活、模式跟踪、状态栏、stats | 写配置目录 flag 文件，待源码确认 |
| MCP proxy | `src/mcp-servers/caveman-shrink/` | 包装上游 MCP server，压缩 metadata 描述字段 | JSON-RPC stdio，待源码确认 |
| OpenCode plugin | `src/plugins/opencode/` | OpenCode session hook 和 slash commands | 待源码验证 |
| Benchmarks / evals | `benchmarks/`、`evals/` | token reduction 测量和对照实验 | 待复现 |
| Tests | `tests/` | Node / Python 测试 | 待执行 |

## 4. 推荐阅读顺序

1. `README.md`：确认产品定位、支持平台和功能矩阵。
2. `INSTALL.md`：确认安装入口、dry-run、per-agent 命令和卸载路径。
3. `CLAUDE.md`：理解维护者定义的源码目录、单一事实源和同步规则。
4. `package.json`：确认 package bin 映射和测试脚本。
5. `bin/install.js`：从参数解析进入 provider matrix、write scope 和 uninstall。
6. `skills/caveman/SKILL.md`：确认压缩规则、触发语义和安全降级边界。
7. `src/hooks/README.md`，再读 `src/hooks/*.js`、`.ps1`、`.sh`。
8. `src/mcp-servers/caveman-shrink/README.md`，再读 `index.js` 和 `compress.js`。
9. `skills/caveman-compress/SECURITY.md`，再读 `scripts/*.py`。
10. `tests/`、`benchmarks/`、`evals/`：确认行为测试和收益测量口径。

## 5. 关键调用链

### 调用链 1：安装所有检测到的 Agent

- 触发条件：执行 one-liner 或 `node bin/install.js --all`。
- 起点：`bin/install.js`，待源码确认。
- 关键步骤：解析 flags -> 建立 provider 列表 -> 检测本机 agent -> 执行 per-agent 安装命令 -> 可选写 hooks / statusline / MCP shrink / rule files。
- 终点：多个 Agent 的 skill/plugin/rule 配置被写入。
- 输入：CLI flags、环境变量、agent 配置路径。
- 输出：配置文件、hook 文件、插件安装结果或 dry-run 日志。
- 错误处理：待源码确认，包括权限不足、已有配置合并、命令缺失、重复安装和卸载失败。
- 依据：INSTALL.md、CLAUDE.md。

### 调用链 2：Claude Code 模式激活

- 触发条件：Claude Code 会话启动或用户提交 prompt。
- 起点：SessionStart / UserPromptSubmit hooks，待源码确认。
- 关键步骤：写入或读取 active flag -> 注入规则或 per-turn reminder -> statusline 读取 flag -> stats 写入 suffix。
- 终点：Claude Code 回复按当前 caveman 模式输出，状态栏显示模式。
- 输入：用户 prompt、hook 环境变量、配置目录。
- 输出：隐藏上下文、flag 文件、statusline 文本。
- 错误处理：待源码确认，包括 symlink 安全、状态文件损坏、Windows PowerShell 执行策略。
- 依据：hooks README。

### 调用链 3：MCP metadata 压缩

- 触发条件：MCP client 启动 `caveman-shrink <upstream-command> [...args]`。
- 起点：`src/mcp-servers/caveman-shrink/index.js`，待源码确认。
- 关键步骤：spawn 上游 server -> 透传 JSON-RPC -> 针对 list 响应压缩 prose 字段 -> 保留 code / URL / path / identifier。
- 终点：client 收到更短的 tool / prompt / resource metadata。
- 输入：MCP JSON-RPC messages、环境变量 `CAVEMAN_SHRINK_FIELDS`。
- 输出：压缩后的 metadata responses。
- 错误处理：待源码确认，包括上游退出、invalid JSON、stderr forwarding、字段白名单。
- 依据：MCP shrink README。

### 调用链 4：记忆文件压缩

- 触发条件：用户指定一个 memory file 进行压缩。
- 起点：`skills/caveman-compress/scripts/cli.py` 或 skill 调用链，待源码确认。
- 关键步骤：路径和大小校验 -> 备份原文件 -> 调用 Anthropic SDK 或 Claude CLI -> 验证压缩结果 -> 写回文件。
- 终点：原文件被压缩，`.original.md` 备份保留。
- 输入：用户指定文件、API key 或 Claude CLI auth。
- 输出：压缩后的 markdown 和备份文件。
- 错误处理：SECURITY.md 提到固定 argv、stdin 传递和文件大小限制；具体异常路径待源码验证。
- 依据：SECURITY.md、tree。

## 6. 阅读笔记

- 重要发现：Caveman 的工程价值不只在“短回复提示词”，而在跨 Agent 分发、安装写入边界、hook 状态管理、MCP metadata 压缩和记忆文件压缩组合。
- 不确定点：统一安装器检测 30+ Agent 的准确性、失败回滚和卸载幂等性需要源码和 dry-run 验证。
- 待运行验证：`node bin/install.js --dry-run --all`、`node bin/install.js --list`、Codex 单路径安装、MCP shrink 包装一个测试 server、Node / Python 测试。

## 待办检查项

- [ ] 找到 `bin/install.js` 的 provider matrix。
- [ ] 确认 dry-run 是否完全无写入。
- [ ] 确认 `--only codex` / Codex skill 安装路径。
- [ ] 确认 `--uninstall` 对各平台的回滚范围。
- [ ] 确认 Claude Code hooks 写入和读取哪些文件。
- [ ] 确认 statusline 不覆盖已有自定义配置的逻辑。
- [ ] 确认 `caveman-shrink` 不改写 tool call response。
- [ ] 确认 `caveman-compress` 的路径、大小、备份和 API / CLI fallback 边界。
- [ ] 运行 `npm test` 或仓库实际测试入口。
- [ ] 复现至少一组 benchmark / eval，确认 token 统计口径。

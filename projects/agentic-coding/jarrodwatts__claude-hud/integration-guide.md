# Claude HUD 集成指南

## 1. 集成目标

- 目标系统：本地 Claude Code 环境。
- 目标能力：通过 statusline 实时查看项目、模型、上下文、订阅用量、git、工具、Skill、MCP、Agent、Todo 和会话状态。
- 集成方式：Claude Code plugin marketplace、`/claude-hud:setup`、`/claude-hud:configure`、用户级 `statusLine.command`。
- 约束条件：当前文档未在真实 Claude Code 环境执行安装；所有写用户级配置的操作都需要先备份。

## 2. 前置条件

- Claude Code v1.0.80+。
- Windows：Node.js 18+，且当前 shell 能找到 `node`。
- macOS/Linux：Node.js 18+ 或 Bun。
- Claude Code plugin marketplace 功能可用。
- 如果已有 `statusLine`，先确认它来自哪个工具，并保留恢复路径。

## 3. 最小集成路径

### 路径 A：只做源码和测试验证

1. 在临时目录浅克隆仓库。
2. 执行 `npm ci`。
3. 执行 `npm run build`。
4. 选择性执行非环境敏感测试。
5. 记录 Node 版本、OS、shell 和失败项。

本轮结果：`npm ci` 成功，`npm test` 在 Windows 环境失败。

### 路径 B：隔离 Claude 配置验证

1. 创建临时 `CLAUDE_CONFIG_DIR`。
2. 在该目录中准备最小 `settings.json`。
3. 按 `commands/setup.md` 的平台分支生成 statusLine command。
4. 确认 setup 会创建备份，不覆盖未知 statusline。
5. 检查写入 JSON 是否无 BOM、可被 Claude Code 读取。

状态：待验证。

### 路径 C：真实 Claude Code 安装

1. 在 Claude Code 中运行 `/plugin marketplace add jarrodwatts/claude-hud`。
2. 运行 `/plugin install claude-hud`。
3. 运行 `/reload-plugins`。
4. 运行 `/claude-hud:setup`。
5. 按提示备份或替换已有 statusline。
6. 完全重启 Claude Code。
7. 验证 HUD 是否出现在输入区域下方。

状态：待验证。

### 路径 D：功能验证

1. 执行一次文件读取和 grep，让 tools line 有内容。
2. 执行一个带 Todo 的多步任务，验证 todo progress。
3. 如果启用 subagent，观察 Agent line。
4. 配置一个 MCP server，观察 MCP activity line。
5. 执行 `/claude-hud:configure`，启用中文 labels、tools、agents、todos、session info。

状态：待验证。

## 4. 接口与数据流

| 输入 | 处理模块 | 输出 | 备注 |
|---|---|---|---|
| Claude Code statusline stdin JSON | `src/stdin.ts`、`src/index.ts` | model/context/rate limit/cwd 等状态 | 真实 schema 需采样验证 |
| transcript JSONL | `src/transcript.ts` | tools、skills、MCP、agents、todos、session tokens | 读取本地 transcript path |
| HUD config | `src/config.ts` | layout、颜色、阈值、display switches | `plugins/claude-hud/config.json` |
| git repo cwd | `src/git.ts` | branch、dirty、ahead/behind、file stats | 最多 1-2 秒 timeout |
| Claude config files | `src/config-reader.ts` | CLAUDE.md / rules / MCP / hooks counts | 当前 Windows 测试失败相关模块 |
| render context | `src/render/` | stdout HUD lines | 由 Claude Code statusline 展示 |

## 5. Java / Spring Boot 集成关注点

Claude HUD 不嵌入 Java / Spring Boot 运行时，也不应写入业务仓库的生产配置。

- Bean 生命周期：不涉及 Spring Bean。
- 配置管理：HUD 配置是用户级 Claude Code 配置，不属于业务应用配置。
- 权限和审计：setup 会修改用户级 `settings.json`，应作为本机开发工具变更审计。
- 团队协作：团队可在文档中推荐，但不应强制提交个人 `~/.claude` 配置。
- CI：上游 Node test suite 可作为学习样例，但当前 Windows 失败需先定位再纳入团队检查。

## 6. 集成风险

- 覆盖风险：setup 可能替换已有 `statusLine.command`。
- 平台风险：Windows PowerShell、Git Bash/MSYS2、WSL 的 command format 不同。
- 版本漂移风险：Claude Code statusline stdin 和 transcript JSONL schema 可能变化。
- 可用性风险：subscriber usage 依赖 Claude Code stdin 中的 `rate_limits`，API-key-only 用户不会有同样数据。
- 性能风险：statusline 高频刷新，git/config/transcript/cache 逻辑需要避免过慢。
- 测试风险：当前 Windows 临时环境 `npm test` 未通过。


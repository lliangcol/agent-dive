# Claude HUD 问题排查记录

## 1. 当前已知问题

| 问题 | 状态 | 依据 | 下一步 |
|---|---|---|---|
| GitHub API rate limit | 已遇到 | `Invoke-RestMethod` 返回 API rate limit exceeded | 使用 GitHub 页面、raw 文件、浅克隆；后续可用认证 API 补齐精确元数据 |
| Windows 临时环境 `npm test` 失败 | 已遇到 | `npm test` 退出码 1，采样 31 个唯一失败测试名 | 在 CI / macOS/Linux / Git Bash / PowerShell 7 中对比 |
| 真实 Claude Code install 未验证 | 未验证 | 本次未执行 plugin install/setup | 用临时 Claude profile 先验证写入 |
| statusLine 可能覆盖其他工具 | 风险 | `commands/setup.md` 明确检测已有 statusline 并询问 | 执行前备份 settings |
| Windows runtime / shell mismatch | 风险 | setup 文档区分 PowerShell、cmd、Git Bash、MSYS2、Cygwin | 先运行 shell 检测，不混用 command format |

## 2. 安装阶段排查

### 插件装不上

优先确认：

- Claude Code plugin marketplace 是否可用。
- 是否执行过 `/plugin marketplace add jarrodwatts/claude-hud`。
- 是否执行过 `/plugin install claude-hud`。
- Linux 上 `/tmp` 和 home 是否跨文件系统，导致 `EXDEV: cross-device link not permitted`。
- 是否存在 ghost install：cache 有目录但 registry 无记录，或 registry 有记录但 cache 缺失。

依据：README、`commands/setup.md`。

### Windows 提示找不到 JavaScript runtime

README 和 setup 文档要求 Windows 使用 Node.js LTS。

待验证命令：

```powershell
Get-Command node -ErrorAction SilentlyContinue
```

若找不到，需要安装 Node.js LTS 并重启 shell，再重新执行 `/claude-hud:setup`。

### Git Bash / MSYS2 下 PowerShell command 失效

setup 文档明确说明：在 Windows + Git Bash/MSYS2/Cygwin 环境中，bash 会先展开 PowerShell 变量，导致 PowerShell command format 不安全。应走 Windows + Git Bash 分支。

## 3. HUD 不显示

优先检查：

- setup 写入后是否完全重启 Claude Code。
- `settings.json` 是否有 `statusLine.command`。
- statusLine command 手动执行是否有输出。
- plugin cache 是否能定位到最新 `claude-hud` 版本目录。
- Windows PowerShell 路径是否生成了 `statusline.mjs` wrapper。
- stdout 是否只显示 initializing，是否因 command path 或 plugin dir 解析失败。

## 4. Usage 不显示

可能原因：

- 当前是 API-key-only 使用方式，没有 Claude subscriber `rate_limits`。
- Claude Code 还没有完成第一轮模型响应，`rate_limits` 尚未填充。
- 使用 Bedrock / Vertex 等 provider routed session，usage/cost 展示会隐藏或降级。
- `display.showUsage` 被设为 `false`。
- external usage snapshot 路径无效、过期、JSON schema 不合法或 freshness 超时。

依据：README、`src/stdin.ts`、`src/external-usage.ts`。

## 5. 工具 / Agent / Todo 行不显示

可能原因：

- config 中 `display.showTools`、`display.showAgents`、`display.showTodos` 默认或当前值为关闭。
- transcript 中还没有对应 tool_use、Task/Agent、TodoWrite/TaskCreate/TaskUpdate 记录。
- transcript path 缺失或无法读取。
- transcript cache 命中旧状态，需要确认 file state 是否更新。
- activity name 被 sanitize 后为空。

依据：`src/transcript.ts`、`src/render/tools-line.ts`、`src/render/agents-line.ts`、`src/render/todos-line.ts`。

## 6. 当前测试失败摘要

本轮命令：

```text
npm ci
npm test
```

结果：

- `npm ci` 成功。
- `npm test` 退出码为 1。
- 失败采样集中在：
  - `countConfigs` 配置计数和 cache。
  - `writeExternalUsageSnapshot` 文件权限。
  - `runExtraCmd` 外部命令 JSON 输出。
  - `getGitStatus` Windows 文件/目录场景。
  - `index entrypoint`。
  - integration 输出换行和 added dirs layout。
  - `getClaudeCodeVersion` Windows command resolution。

判断边界：

- 不能把上游测试标为通过。
- 不能仅凭本机 Windows 失败断言项目不可用。
- 需要在上游 CI 同等环境、Windows Git Bash、PowerShell 7、macOS/Linux 中对比。

## 7. 待人工确认

- [ ] 真实 Claude Code plugin install 是否成功。
- [ ] `/claude-hud:setup` 是否生成正确 statusLine command。
- [ ] 已有 statusline 备份和恢复是否可用。
- [ ] Windows `statusline.mjs` wrapper 是否被正确写入且无 BOM。
- [ ] HUD 在真实 transcript 下是否展示 tools / agents / todos。
- [ ] 测试失败是否为 Windows 环境差异。


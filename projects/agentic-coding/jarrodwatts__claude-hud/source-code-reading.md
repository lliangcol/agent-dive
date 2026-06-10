# Claude HUD 源码阅读记录

## 1. 阅读目标

- 本轮要理解的问题：Claude HUD 如何通过 Claude Code statusline stdin 和 transcript JSONL 生成实时 HUD。
- 关联功能：plugin manifest、setup/configure command、stdin 解析、context/usage 计算、transcript 活动解析、配置合并、git 状态、render 宽度处理、测试套件。
- 预期产出：确认核心模块边界、关键调用链、写入范围、测试风险和后续源码阅读顺序。

## 2. 源码入口

| 入口 | 路径 | 作用 | 依据 |
|---|---|---|---|
| Plugin manifest | `.claude-plugin/plugin.json` | 声明 Claude Code plugin 元数据和 commands | manifest |
| Setup command | `commands/setup.md` | 检测平台和 runtime，生成并写入 statusLine command | command 文档 |
| Configure command | `commands/configure.md` | guided flow 修改 HUD layout、preset、language 和 display options | command 文档 |
| Statusline 主入口 | `src/index.ts` | 读取 stdin、解析 transcript、加载配置并调用 render | 源码 |
| Stdin 解析 | `src/stdin.ts` | 读取 Claude Code statusline JSON，计算 context 和 usage | 源码 |
| Transcript 解析 | `src/transcript.ts` | 解析 JSONL，提取 tools、skills、MCP、agents、todos、tokens | 源码 |
| 配置 | `src/config.ts` | 默认配置、迁移、校验、路径 | 源码 |
| 渲染 | `src/render/index.ts` | compact/expanded layout、宽度、截断、换行 | 源码 |
| Tests | `tests/` | Node test suite | 已运行，当前 Windows 环境失败 |

## 3. 模块地图

| 模块 | 路径 | 职责 | 依赖关系 |
|---|---|---|---|
| 插件分发 | `.claude-plugin/`、`commands/` | Claude Code plugin metadata 和 slash commands | Claude Code plugin runtime |
| 主程序 | `src/index.ts` | 编排读取、解析、配置、git、usage、render | 调用多个本地模块 |
| 输入层 | `src/stdin.ts`、`src/types.ts` | statusline stdin schema 和 rate limit/context 解析 | Claude Code stdin payload |
| transcript 层 | `src/transcript.ts` | JSONL stream parse、activity cache、agent/todo/session tokens | transcript file path |
| 配置层 | `src/config.ts`、`src/config-reader.ts`、`src/claude-config-dir.ts` | HUD config、Claude config/rules/MCP/hook 计数、路径定位 | `CLAUDE_CONFIG_DIR`、home dir、project cwd |
| 状态源 | `src/git.ts`、`src/memory.ts`、`src/version.ts`、`src/external-usage.ts`、`src/extra-cmd.ts` | git、RAM、Claude version、usage snapshot、外部命令标签 | OS、git、文件系统、child process |
| 渲染层 | `src/render/` | line renderers、颜色、宽度、activity lines | ANSI terminal |
| 国际化 | `src/i18n/` | English 和 Simplified Chinese labels | config language |
| 测试 | `tests/` | 单元和集成测试 | Node test runner |

## 4. 推荐阅读顺序

1. `README.md`：确认功能定位、安装路径、配置选项和限制。
2. `.claude-plugin/plugin.json`：确认 Claude Code plugin 分发方式。
3. `commands/setup.md`：理解 statusLine 写入、备份、跨平台 runtime 选择。
4. `src/index.ts`：沿主链路读一遍。
5. `src/stdin.ts`：理解 context percent、rate limits、provider label。
6. `src/transcript.ts`：理解 activity parse 和 cache。
7. `src/config.ts`：理解 defaults、migration 和 validation。
8. `src/render/index.ts` 以及 `src/render/*-line.ts`：理解显示策略。
9. `src/config-reader.ts`、`src/external-usage.ts`、`src/git.ts`：定位当前测试失败相关模块。
10. `tests/core.test.js`、`tests/integration.test.js`、`tests/git.test.js`：解释 Windows 测试失败。

## 5. 关键调用链

### 调用链 1：主渲染链路

- 触发条件：Claude Code 调用 statusLine command，并通过 stdin 传入 JSON。
- 起点：`src/index.ts` 的 `main()`。
- 关键步骤：读取 stdin -> 解析 transcript -> context fallback -> 计数配置 -> 读取 HUD config -> git status -> usage data -> extra command -> version/memory/effort -> render。
- 终点：stdout 输出一组 HUD lines。
- 错误处理：主入口 catch 后输出 `[claude-hud] Error: ...`。

### 调用链 2：stdin 和 context percent

- 起点：`readStdin()`。
- 关键步骤：非 TTY 才读；设置 first byte / idle timeout；限制最大 256 KB；尝试 JSON parse；计算 context percent。
- 终点：返回 `StdinData` 或 `null`。
- 关注点：fresh session 的 `used_percentage=0` 会 fallback 到 token 计算，避免初始系统 prompt 被隐藏。

### 调用链 3：transcript activity

- 起点：`parseTranscript(transcriptPath)`。
- 关键步骤：canonicalize path -> 读取 file state -> 命中 cache 则返回 -> 流式读 JSONL -> process tool blocks -> 处理 queue-operation completion -> 更新 cache。
- 终点：`TranscriptData` 包含 tools、skills、mcpServers、agents、todos、sessionStart、sessionName、sessionTokens、advisorModel 等。
- 关注点：background agent 的完成时间优先来自 queue-operation，不只看 tool_result。

### 调用链 4：setup 写入配置

- 起点：`/claude-hud:setup` command。
- 关键步骤：检测 ghost install -> 检测 platform/shell/runtime -> 生成 command -> 测试 command -> 检测已有 statusline -> 备份 settings -> 写入 JSON。
- 终点：`settings.json` 含 `statusLine: { type: "command", command: ... }`。
- 关注点：已有 statusline 可能属于其他工具，必须显式确认替换。

## 6. 已读代码要点

- `src/index.ts` 的依赖都通过 `MainDeps` 可覆盖，便于测试。
- `src/stdin.ts` 对 Bedrock / Vertex / enterprise plan alias 做了 provider label 和 usage/cost 边界处理。
- `src/transcript.ts` 对活动名做 ANSI 和控制字符清理，并限制显示长度。
- transcript cache 路径使用 transcript path 的 sha256，写入 `plugins/claude-hud/transcript-cache/`。
- `src/config.ts` 有 legacy `layout` 到 `lineLayout/showSeparators` 的迁移逻辑。
- render 层对 OSC8 hyperlink 的截断做了关闭处理，避免终端后续文本被错误下划线包住。
- `src/external-usage.ts` 只接受 absolute `.json` write path，且不创建缺失 parent directory。

## 7. 本轮测试记录

在临时浅克隆中执行：

```text
npm ci
npm test
```

结果：

- `npm ci` 成功，安装 62 个包，audit 显示 0 vulnerabilities。
- `npm test` 执行 `npm run build && node --test`。
- `npm run build` 在 `npm test` 流程中完成，随后由 Node test runner 运行测试。
- `npm test` 退出码为 1。
- 失败项采样到 31 个唯一测试名，集中在：
  - `countConfigs` 和 config cache。
  - `writeExternalUsageSnapshot` 文件权限断言。
  - `runExtraCmd` JSON output。
  - `getGitStatus` Windows 下 `mkdir` / 文件名场景。
  - `index` direct entrypoint。
  - integration output newline / added dirs layout。
  - `getClaudeCodeVersion` Windows command resolution。

该结果只能说明当前 Windows 收录环境下测试未通过，不能直接断言上游 main 一定不可用；下一步应在维护者推荐环境和 CI 环境对比。

## 8. 待办检查项

- [ ] 在真实 Claude Code 中验证 plugin install、setup、restart 后 HUD 是否出现。
- [ ] 用临时 `CLAUDE_CONFIG_DIR` 复现 setup 写入，不碰主力配置。
- [ ] 解释 `npm test` Windows 失败项，区分环境问题和项目回归。
- [ ] 采集一份真实 statusline stdin JSON 样例，确认字段与 `src/types.ts` 一致。
- [ ] 采集一份真实 transcript JSONL，验证 tools / agents / todos / MCP 展示。
- [ ] 验证 `display.externalUsageWritePath` 的权限模式在 Windows 和 POSIX 的差异。
- [ ] 验证 PowerShell、Git Bash、WSL 的 setup command 选择。
- [ ] 验证已有 statusline 备份和 restoration 路径。
- [ ] 验证中文 labels 和 CJK 宽度处理。
- [ ] 验证 Bedrock / Vertex / API-key-only 场景 usage/cost 是否按文档隐藏或降级。

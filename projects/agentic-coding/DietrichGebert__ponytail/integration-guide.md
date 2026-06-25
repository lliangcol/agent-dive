# Ponytail 集成指南

## 1. 集成前检查

Ponytail 会把规则注入 AI 编码 Agent 的上下文，并可能运行 lifecycle hooks。不要直接在主力开发配置中试装，先准备隔离环境：

- 确认 Node 在非交互式 shell 的 `PATH` 中。
- 确认要测试的宿主：Codex、Claude Code、Copilot CLI、OpenCode、Gemini CLI、Pi 或 OpenClaw。
- 准备临时插件数据目录或临时 profile。
- 备份已有 `AGENTS.md`、Codex plugin 配置、Claude Code hooks / settings、OpenCode config。
- 明确团队是否允许第三方插件 hook 读取 prompt payload、写状态文件或修改用户级 config。

## 2. Codex 集成

README 给出的路径：

```bash
codex plugin marketplace add DietrichGebert/ponytail
codex
```

随后在 Codex 中：

1. 打开 `/plugins`。
2. 选择 Ponytail marketplace 并安装 Ponytail。
3. 打开 `/hooks`。
4. 审核并信任 lifecycle hooks。
5. 启动新 thread。

当前收录未执行真实安装。建议先在测试 profile 中验证：

- `PLUGIN_DATA` 下是否写入 `.ponytail-active`。
- `SessionStart` hook 输出是否包含 `PONYTAIL:<MODE>` 和 `additionalContext`。
- `SubagentStart` hook 是否在子代理中注入同一规则集。
- `@ponytail lite`、`@ponytail ultra`、`normal mode` 是否按预期切换。
- hooks 被禁用或 Node 不在 PATH 时，插件是否静默降级。

## 3. Claude Code 集成

README 给出的路径：

```text
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

Claude Code 场景还涉及 statusline 提醒。`ponytail-activate.js` 会检查 `~/.claude/settings.json` 中是否已有 `statusLine`，没有时会追加提示，让用户主动配置状态栏命令。

建议验证：

- 使用临时 `CLAUDE_CONFIG_DIR`，避免写入真实 `~/.claude`。
- 检查 `.ponytail-active` 是否写入临时目录。
- 检查 Windows 下 statusline 命令使用 PowerShell，非 Windows 下使用 bash。
- 先不要让插件改真实 statusline；手动审查后再应用。

## 4. OpenCode 集成

README 说明 OpenCode 需要从 Ponytail checkout 引用插件：

```json
{ "plugin": ["./.opencode/plugins/ponytail.mjs"] }
```

该插件会在 `experimental.chat.system.transform` 中追加规则，在 `command.execute.before` 中持久化 `/ponytail` 模式。因为路径相对项目 `opencode.json` 解析，多项目复用时应使用绝对路径指向 `.opencode/plugins/ponytail.mjs`。

验证点：

- OpenCode 是否能加载 ESM plugin。
- `.config/opencode/.ponytail-active` 是否按命令变化。
- `/ponytail off` 后 transform 是否不再注入。

## 5. Pi extension 集成

`package.json` 的 `pi` 字段声明：

- extensions：`./pi-extension/index.js`
- skills：`./skills`

Pi extension 注册 `/ponytail` 和 skill alias，并在 `before_agent_start` 注入规则。本轮 `npm test` 链式执行 Pi extension 测试，15 个测试通过，但未在真实 Pi harness 中安装。

## 6. Instruction-only 集成

部分宿主不运行 plugin 或 hook，只读取规则文件：

- Cursor：`.cursor/rules/ponytail.mdc`
- Windsurf：`.windsurf/rules/ponytail.md`
- Cline：`.clinerules/ponytail.md`
- GitHub Copilot editor：`.github/copilot-instructions.md`
- Kiro：`.kiro/steering/ponytail.md`
- VS Code Codex extension 或通用 Agent：`AGENTS.md`

这种模式只提供 always-on 规则，不提供 mode persistence、生命周期 hook、命令切换和 statusline。

## 7. Benchmark 复现

Claude benchmark 需要 API key 和 promptfoo：

```bash
cp .env.example .env
npx promptfoo@latest eval -c benchmarks/promptfooconfig.yaml --env-file .env --repeat 10
npx promptfoo@latest view
```

本地 benchmark 或 correctness gate 还需要：

- Node.js。
- Python 3。
- `pandas`，CSV correctness check 会用到。

当前收录没有运行 API benchmark。最新快照的 `npm test` 已在临时 venv 中通过；Windows 下需确保 `python3` 也命中该 venv，因为 correctness harness 会优先探测 `python3`，不建议为一次收录污染用户级 Python 环境。

## 8. 安全和治理边界

- Ponytail 会改变 Agent 的实现偏好，不应覆盖仓库自身 AGENTS / CLAUDE / security 规则。
- 高风险路径，例如支付、权限、迁移、审计、安全修复，不应因为“少写”而删掉必要验证。
- hook 会读取 prompt payload 并写模式状态，接入前要审查源码和权限。
- mode 配置可能来自环境变量或用户级 config，团队环境要避免隐藏默认值造成行为不一致。
- benchmark 是 prompt generation 实验，不等同于真实多轮 agent session 成本。

## 9. 推荐验证矩阵

| 阶段 | 命令或动作 | 通过标准 |
|---|---|---|
| 静态检查 | `node scripts/check-rule-copies.js` | 规则副本一致 |
| 插件聚焦测试 | `node --test tests\hooks.test.js ...` | hook、adapter、command tests 通过 |
| Pi 测试 | `npm test --prefix pi-extension` | Pi extension tests 通过 |
| 完整测试 | `npm test` | Python pandas 可用且全部测试通过 |
| Codex smoke | 安装到测试 profile 并信任 hooks | `@ponytail` 可切换模式 |
| Claude smoke | 使用临时 `CLAUDE_CONFIG_DIR` | 状态文件、SubagentStart 和 statusline 提示符合预期 |
| Benchmark | promptfoo repeat 小样本 | 记录成本、延迟、正确性和原始配置 |

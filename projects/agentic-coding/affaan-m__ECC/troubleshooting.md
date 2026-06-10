# ECC 问题排查记录

## 问题：重复安装导致重复 skills、rules 或 hooks

- 发现时间：2026-06-11
- 当前状态：未验证，风险记录
- 影响范围：Claude Code plugin、manual installer、npm installer 混用场景

### 现象

README 明确提醒不要叠加 plugin install 和 full manual installer。重复安装可能导致相同 skills、commands、rules 或 hooks 在用户目录和 plugin 目录同时存在。

### 环境

- 操作系统：待验证
- 运行时版本：Node `>=18`
- 项目版本 / Commit：`c888d2b73f26d605ff6c172b433d4cad2200206f`
- 关键依赖：Claude Code plugin、manual installer、npm `ecc-universal`

### 复现步骤

1. 安装 Claude plugin。
2. 再运行 full profile manual installer。
3. 检查同名 skills/hooks 是否重复出现。

状态：未执行。

### 初步判断

- 可能原因：plugin 和 manual installer 都向 harness 暴露同类资产。
- 排除项：尚未确认 minimal profile 是否也会造成重复。

### 后续处理

- 先使用 `ecc plan` 或 `--dry-run`。
- 记录 install-state。
- 验证 `ecc uninstall` 或手动回滚路径。

## 问题：误以为 Codex 会执行 Claude-style hooks

- 发现时间：2026-06-11
- 当前状态：文档级确认，运行未验证
- 影响范围：Codex 集成、质量门禁、安全门禁、session hooks

### 现象

README 和 cross-harness architecture 文档说明 Codex 路径主要依赖 `AGENTS.md`、plugin metadata、skills、MCP config 和 instruction-backed 约束，不具备 Claude-style hook parity。

### 初步判断

- 可能原因：同一仓库包含 `hooks/hooks.json`，容易误以为所有 harness 都会执行。
- 结论：Codex 不能把 hook 阻断当成已启用安全控制，必须单独验证 Codex 实际能力。

### 后续处理

- Codex 路径只记录 instruction-backed 验证。
- 如需强门禁，应放在 CI、pre-commit、wrapper script 或支持 hook 的 harness 中验证。

## 问题：安装写入范围不明

- 发现时间：2026-06-11
- 当前状态：未验证
- 影响范围：用户目录、项目目录、团队仓库

### 现象

ECC 支持多个 target 和 profile，不同目标可能写入 `~/.claude/`、`~/.codex/`、项目 `.cursor/`、`.opencode/`、`.zed/` 等位置。

### 初步判断

- 可能原因：target adapter 和 profile 组合多。
- 风险：在主力环境直接 install 可能污染全局配置。

### 后续处理

```bash
npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json
npx --yes --package ecc-universal ecc install --profile minimal --target codex --dry-run --json
```

只有确认 planned file operations 后再安装。

## 问题：README / release notes / plugin manifest 能力数量漂移

- 发现时间：2026-06-11
- 当前状态：待验证
- 影响范围：收录资料、对外能力判断、学习任务

### 现象

README 和 release notes 提到 261 skills 等数量；`.codex-plugin/plugin.json` 的 short description 提到 249 skills。两者可能来自不同构建时间或统计口径。

### 初步判断

- 可能原因：catalog 更新或 plugin manifest 未同步。
- 风险：收录资料引用具体数量时容易过期。

### 后续处理

- 运行 `npm run catalog:check` 或 `node scripts/ci/catalog.js --text` 复核。
- 收录文档优先描述能力类型，少依赖具体数量。

## 问题：`npx ecc` 可能解析到错误 npm 包

- 发现时间：2026-06-11
- 当前状态：已确认 npm 元数据，未运行 ECC CLI
- 影响范围：所有用 npm 临时执行 ECC CLI 的验证命令

### 现象

本次复核 `npm view ecc-universal name version bin --json` 显示官方包名为 `ecc-universal@2.0.0`，bin 包含 `ecc`。同时 `npm view ecc name version --json` 显示 npm 上存在独立的 `ecc@0.0.2` 包。因此直接执行 `npx ecc ...` 可能解析到包名为 `ecc` 的旧/无关包，而不是 `ecc-universal` 暴露的 `ecc` bin。

### 初步判断

- 可能原因：npm package name 与 bin name 不一致，而 README 示例使用了 bin name。
- 风险：验证命令看似运行 ECC，实际运行了错误 package。

### 后续处理

- 使用显式 package selector：

```bash
npx --yes --package ecc-universal ecc --help
```

- 或 clone 仓库后使用本地入口：

```bash
node scripts/ecc.js --help
```

- 收录资料中的待验证命令统一使用显式 package selector。

## 问题：Hook 阻断影响正常开发

- 发现时间：2026-06-11
- 当前状态：未验证
- 影响范围：Claude Code / OpenCode / Cursor hook-backed 场景

### 现象

`hooks/hooks.json` 包含配置保护、MCP health check、quality gate、fact-forcing、format/typecheck、console.log 检查等脚本。严格 profile 可能阻断工具调用或文件编辑。

### 初步判断

- 可能原因：hook profile、timeout、环境变量和项目状态共同影响行为。
- 风险：在不熟悉项目中启用 strict hooks 可能造成误阻断。

### 后续处理

- 从 minimal 或 standard profile 开始。
- 记录每次 hook 的 matcher、id、stdout/stderr、exit code。
- 对阻断类 hook 单独阅读 `scripts/hooks/` 源码。

## 问题：Windows PowerShell 路径和 shell quoting

- 发现时间：2026-06-11
- 当前状态：未验证
- 影响范围：Windows installer、PowerShell、Node hook runner

### 现象

项目包含 `install.ps1` 和大量 Node/shell hook command。release notes 提到 Windows path normalization 和 stdin prompt 相关 hardening。

### 初步判断

- 可能原因：跨平台 path、shell quoting、Node 版本和 plugin root 解析复杂。
- 风险：Windows 下安装和 hook 执行需要单独测试，不能直接套用 macOS/Linux 结果。

### 后续处理

- 在临时 Windows 测试用户或临时项目中 dry-run。
- 优先验证 `.\install.ps1 --profile minimal --target claude` 的计划输出。
- 记录 PATH、Node、PowerShell 版本和写入文件。

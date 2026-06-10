# RTK 问题排查记录

## 1. 安装和版本

### 现象：`rtk --version` 成功但 `rtk gain` 不工作

- 可能原因：安装到了 crates.io 上另一个同名 `rtk` 包，而不是 `rtk-ai/rtk`。
- 依据：README 的 name collision warning。
- 排查：确认安装来源，优先使用 GitHub release、Homebrew 或 `cargo install --git https://github.com/rtk-ai/rtk`。
- 状态：未本机验证。

### 现象：README 版本示例和源码版本不一致

- 现象：README 示例写 `rtk 0.28.2`，本次源码快照 `Cargo.toml` version 为 `0.42.2`。
- 可能原因：README 示例未同步，或 default branch 与 release 文档存在漂移。
- 排查：检查 GitHub release、tag 和实际 binary version。
- 状态：待验证。

## 2. Hook 和 Agent 集成

### 现象：Codex 中没有自动重写命令

- 可能原因：Codex 路径是 `AGENTS.md` / `RTK.md` prompt-level guidance，不是程序级 hook。
- 依据：`hooks/codex/README.md` 和 `hooks/README.md`。
- 排查：确认 `rtk init --codex` 写入位置，检查 Codex 是否读取相应 instructions；必要时显式调用 `rtk`。
- 状态：待运行验证。

### 现象：Claude / Cursor hook 没有改写命令

- 可能原因：hook 未安装、settings 未 patch、`rtk` 不在 PATH、命令不匹配 registry、命令含重定向或 substitution 被判定不可验证。
- 依据：`src/hooks/README.md`、`src/hooks/rewrite_cmd.rs`、`src/discover/registry.rs`。
- 排查：先执行 `rtk rewrite "<cmd>"`，再执行目标 Agent 的 hook check / verify 命令。
- 状态：待运行验证。

### 现象：命令被改写但仍需要用户确认

- 可能原因：host permission 没有明确 allow，RTK 将 Default 映射为 ask。
- 依据：`src/hooks/permissions.rs` 和 `src/hooks/rewrite_cmd.rs` 测试说明。
- 排查：检查 Claude / Cursor / Gemini 等 host 的 deny / ask / allow 配置。
- 状态：源码抽样已读，未运行。

## 3. 输出过滤

### 现象：过滤后缺少关键 debug 细节

- 可能原因：RTK 默认输出摘要，不保证保留所有 raw output。
- 排查：使用 verbose、passthrough、`--no-compact` 或 tee full-output hint，必要时直接运行原生命令。
- 状态：待运行验证。

### 现象：命令失败但看不到完整日志

- 可能原因：tee disabled、输出太短、`RTK_TEE=0`、tee directory 不可写。
- 依据：`src/core/tee.rs`。
- 排查：设置 `RTK_TEE_DIR` 到临时可写目录并复现失败命令。
- 状态：待运行验证。

## 4. 隐私和遥测

### 现象：担心 telemetry 发送数据

- 依据：README 和 `docs/TELEMETRY.md` 声明 telemetry 默认关闭，需要显式 opt-in，可用 `RTK_TELEMETRY_DISABLED=1` 阻断。
- 排查：运行 `rtk telemetry status`，检查 config 和环境变量。
- 状态：文档已读，源码发送路径待继续验证。

## 5. 平台差异

### 现象：Windows 上 hook 不自动工作

- 可能原因：README 说明 native Windows 下 hook 系统有限，WSL 支持完整 hook。
- 排查：在 native Windows 显式调用 `rtk <cmd>`，或在 WSL 中验证自动重写。
- 状态：未本机安装验证。

## 后续排查清单

- [ ] `rtk --version` 与 release / Cargo version 对齐。
- [ ] `rtk rewrite "git status"` 输出符合预期。
- [ ] `rtk rewrite` 对 redirect、substitution 和 compound command 的处理符合权限预期。
- [ ] `rtk git diff`、`rtk cargo test`、`rtk pytest` 输出可读且保留必要失败信息。
- [ ] `RTK_TEE_DIR` 恢复路径可用。
- [ ] `rtk init --codex` 和目标 Agent 的实际写入范围可回滚。

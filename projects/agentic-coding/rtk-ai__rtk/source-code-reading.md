# RTK 源码阅读记录

## 1. 阅读目标

- 本轮要理解的问题：RTK 如何把原始 shell 命令重写为 `rtk` 命令，并如何执行、过滤、记录输出。
- 关联功能：CLI routing、command filters、hook rewrite、permission model、tracking、tee recovery、telemetry boundary。
- 预期产出：确认源码入口、模块地图、关键调用链和下一轮源码阅读计划。

## 2. 源码入口

| 入口 | 路径 | 作用 | 依据 |
|---|---|---|---|
| CLI 入口 | `src/main.rs` | Clap command 定义，`run_cli` 分发到各生态模块 | 源码抽样 |
| Hook rewrite 入口 | `src/hooks/rewrite_cmd.rs` | `rtk rewrite` 命令，根据权限和 registry 返回改写结果 | 源码抽样 |
| Rewrite registry | `src/discover/registry.rs` | 识别支持命令、拆 compound command、处理 ignored / unsupported | 源码抽样 |
| Hook installer | `src/hooks/init.rs` | `rtk init` 安装不同 Agent 的 hook / guidance / plugin | 源码抽样 |
| 通用执行器 | `src/core/runner.rs` | 捕获原生命令输出、调用 filter、记录 tracking | 源码抽样 |
| Git 过滤样例 | `src/cmds/git/git.rs` | `git status`、`diff`、`log` 等过滤实现 | 源码抽样 |

## 3. 模块地图

| 模块 | 路径 | 职责 | 依赖关系 |
|---|---|---|---|
| CLI facade | `src/main.rs` | 命令定义、参数解析、路由 | 调用 `cmds`、`hooks`、`analytics`、`discover` |
| Command filters | `src/cmds/` | 各生态命令输出过滤 | 使用 `core::runner`、`core::stream`、特定 parser |
| Core runtime | `src/core/` | config、runner、stream、filter、tracking、tee、telemetry | 被所有命令模块复用 |
| Rewrite discovery | `src/discover/` | 命令识别、rewrite rules、missed savings | 被 hooks 和 audit 使用 |
| Hook lifecycle | `src/hooks/` | init、verify、permission、rewrite、trust、integrity | 读取 host 配置，调用 discover |
| Deployed hooks | `hooks/` | 各 Agent 的 hook / plugin / rules artifacts | 调用 `rtk rewrite` |
| Parser | `src/parser/` | 结构化测试/工具输出解析 | 被 Vitest / Playwright 等模块使用 |
| Analytics | `src/analytics/`、`src/learn/` | gain、session、discover report 等 | 读取 tracking / session 数据 |

## 4. 推荐阅读顺序

1. `src/main.rs`：先理解 CLI surface 和 `Commands::*` 路由。
2. `src/discover/rules.rs` 与 `src/discover/registry.rs`：理解哪些命令会被重写。
3. `src/hooks/rewrite_cmd.rs` 与 `src/hooks/permissions.rs`：确认 rewrite exit code 和权限边界。
4. `hooks/README.md` 与目标 Agent 子目录：确认部署 hook 如何调用 binary。
5. `src/core/runner.rs` 与一个具体命令模块，例如 `src/cmds/git/git.rs`。
6. `src/core/tracking.rs`、`src/core/tee.rs`、`docs/TELEMETRY.md`：确认统计、恢复和隐私边界。
7. `tests/` 与 fixtures：用测试样本反证过滤行为。

## 5. 关键调用链

### 调用链 1：hook rewrite

- 触发条件：Agent hook 收到 shell command。
- 起点：`hooks/<agent>/...` 调用 `rtk rewrite <cmd>`。
- 关键步骤：`rewrite_cmd::run` -> `permissions::check_command` -> `lexer::contains_unattestable_construct` -> `registry::rewrite_command`。
- 终点：stdout 输出 rewritten command，exit code 区分 allow / passthrough / deny / ask。
- 输入：原始 shell command string。
- 输出：RTK command string 或 passthrough。
- 错误处理：文档要求 hooks 在异常路径 fail-open，不阻塞原命令。
- 依据：`hooks/README.md`、`src/hooks/rewrite_cmd.rs`、`src/hooks/permissions.rs`。

### 调用链 2：filtered command execution

- 触发条件：执行 `rtk git diff`、`rtk pytest`、`rtk cargo test` 等。
- 起点：`main.rs::run_cli`。
- 关键步骤：match `Commands::*` -> 调用对应 `cmds` 模块 -> 原生命令执行 -> filter 输出 -> tracking。
- 终点：终端输出压缩结果，保留 exit code。
- 输入：RTK command args。
- 输出：filtered stdout / stderr。
- 错误处理：部分模块失败时跳过过滤或输出 stderr，tee 可保存 full output。
- 依据：`src/main.rs`、`src/core/runner.rs`、`src/cmds/git/git.rs`。

### 调用链 3：tracking / gain

- 触发条件：命令过滤完成。
- 起点：`tracking::TimedExecution::start`。
- 关键步骤：计算 raw / filtered token 估算 -> 写入 SQLite -> `rtk gain` 汇总读取。
- 终点：本地 savings history。
- 输入：原始输出、过滤后输出、命令标签。
- 输出：tracking DB 记录和 gain summary。
- 错误处理：待继续确认 DB 初始化和权限失败路径。
- 依据：`src/core/tracking.rs`。

## 6. 阅读笔记

- 重要发现：Codex 路径是 prompt-level guidance，不能和 Claude / Cursor 透明 hook 等同。
- 重要发现：`permissions.rs` 要求 compound command 每个 segment 都匹配 allow rule 才能自动 allow。
- 重要发现：`rewrite_cmd.rs` 对 command substitution、file redirect 等 unattestable construct 选择 passthrough / ask，降低 rewrite 权限风险。
- 重要发现：`tee.rs` 让 filtered output 保留回到 raw output 的路径，适合失败排查。
- 不确定点：README 版本示例与 `Cargo.toml` version 不一致，需要 release / build 验证。
- 不确定点：各 Agent hook 的真实安装路径、备份文件、幂等和卸载行为尚未运行。
- 待运行验证：`rtk rewrite`、`rtk git status`、`rtk err`、`rtk test`、`rtk gain`、`rtk init --codex --dry-run` 或等价安全路径。

## 待办检查项

- [x] 找到入口文件。
- [x] 找到命令重写主线。
- [x] 找到命令执行与过滤主线。
- [x] 找到 tracking 和 tee recovery。
- [ ] 找到每类 ecosystem filter 的测试覆盖。
- [ ] 源码级确认 telemetry 编译期开关与发送路径。
- [ ] 执行本地构建和测试。

## 质量检查项

- [x] 调用链有路径或文档依据。
- [x] 未声称已运行本机验证。
- [x] 已标注 Codex prompt guidance 与 transparent hook 的差异。
- [x] 已记录版本示例不一致风险。

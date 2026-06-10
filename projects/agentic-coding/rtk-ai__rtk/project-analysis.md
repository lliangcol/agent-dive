# RTK 项目精读

## 1. 项目基本信息

- 项目名称：RTK
- 项目 ID：`rtk-ai__rtk`
- GitHub：https://github.com/rtk-ai/rtk
- 项目主页：https://www.rtk-ai.app
- 分类：`agentic-coding`
- 收录等级：Level B 标准收录
- 当前状态：`analyzing`
- 主要语言：Rust
- License：Apache-2.0
- 分析日期：2026-06-11
- 分析版本 / Commit：`6785a6c7695d7273e722214a295249a84819b6f0`
- 默认分支：`develop`
- 是否运行验证：否
- 分析依据：GitHub API、README、`git ls-remote --symref`、临时浅克隆、`Cargo.toml`、`src/main.rs`、`src/hooks/README.md`、`hooks/README.md`、`src/discover/registry.rs`、`src/core/runner.rs`、`src/core/tracking.rs`、`src/core/tee.rs`、`docs/contributing/ARCHITECTURE.md`、`docs/TELEMETRY.md`。

## 2. 一句话定位

RTK 是面向 AI 编码助手的 Rust CLI 代理，通过命令重写和输出过滤，把常见开发命令的冗长输出压缩后再交给 LLM。

## 3. 项目解决的问题

AI coding agent 经常通过 shell 调用 `git status`、`git diff`、`cargo test`、`pytest`、`pnpm`、`docker`、`kubectl` 等命令。原始输出通常包含重复日志、完整 diff、依赖树、测试通过噪声和构建细节，会快速消耗上下文窗口。

RTK 的核心价值是把这些命令输出变成更适合 LLM 消费的摘要，同时保留退出码、错误重点和必要恢复路径。它不是 Agent 框架，也不负责模型推理；它是 AI 编码工作流中的上下文成本治理层。

学习价值：

- 如何设计一个跨生态命令过滤 CLI。
- 如何把 hook / plugin / prompt guidance 接入不同 AI coding tools。
- 如何处理命令安全权限、不可验证 shell 结构和 rewrite fail-open。
- 如何用 SQLite 记录 token savings，并在失败时保存原始输出用于恢复。

## 4. 项目主线

典型流程基于 README、hooks 文档和源码抽样：

1. 用户安装 RTK binary。
2. 用户执行 `rtk init`，为目标 Agent 写入 hook、plugin 或 guidance。
3. Agent 后续发起 shell 命令，例如 `git status`。
4. 对支持透明重写的 Agent，hook 调用 `rtk rewrite "git status"`。
5. `src/discover/registry.rs` 匹配 rewrite rule，返回 `rtk git status`。
6. Agent 执行 RTK 命令。
7. `src/main.rs` 路由到对应 `src/cmds/**` 模块。
8. 命令模块执行原生命令、捕获输出、过滤摘要、保留退出码。
9. `src/core/tracking.rs` 记录 token savings 估算。
10. 如果失败输出较大，`src/core/tee.rs` 可保存原始输出并给出恢复提示。

未验证：本轮没有在本机安装 RTK，也没有真实触发任何 Agent hook。

## 5. 快速开始

README 给出的入口：

- Homebrew：`brew install rtk`
- Linux / macOS quick install：`curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh`
- Cargo：`cargo install --git https://github.com/rtk-ai/rtk`
- Windows：下载 release zip，将 `rtk.exe` 放入 PATH，native Windows 下 hook 不会自动重写，WSL 支持更完整。

README 给出的验证命令：

- `rtk --version`
- `rtk gain`

注意：本次源码快照的 `Cargo.toml` version 为 `0.42.2`，而 README 的验证示例仍写 `rtk 0.28.2`。这可能是 README 示例未同步，后续需要用实际 release 或本地构建确认。

## 6. 核心架构

| 模块 | 作用 | 依据 | 验证状态 |
|---|---|---|---|
| `src/main.rs` | Clap CLI 定义和命令路由，连接 `Commands::*` 到各生态模块 | 源码抽样 | 已读入口和路由 |
| `src/cmds/` | 按生态实现过滤器，如 git、rust、js、python、go、dotnet、cloud、system | tree、README、源码抽样 | 部分阅读 |
| `src/core/runner.rs` | 统一执行原生命令、捕获输出、调用 filter、记录 tracking | 源码抽样 | 已读 |
| `src/core/filter.rs` | `rtk read` / `smart` 使用的语言感知代码过滤 | 源码抽样 | 已读 |
| `src/discover/registry.rs` | 将原始 shell 命令识别为 RTK 等价命令 | 源码抽样 | 已读 |
| `src/hooks/` | hook lifecycle：install、uninstall、verify、rewrite、trust、permission | hook README、源码抽样 | 部分阅读 |
| `hooks/` | 部署到 Agent 侧的 hook / plugin / rules 文件 | hooks README、tree | 已读文档 |
| `src/core/tracking.rs` | SQLite 记录 command、token savings、耗时和汇总 | 源码抽样 | 已读 |
| `src/core/tee.rs` | 失败时保存原始输出并返回 full-output hint | 源码抽样 | 已读 |
| `docs/TELEMETRY.md` | 说明匿名聚合 telemetry，默认关闭，需显式 opt-in | 文档 | 已读 |

图解草稿见 `assets/diagrams/architecture.mmd`、`hook-rewrite-flow.mmd`、`command-filter-flow.mmd` 和 `tracking-telemetry-flow.mmd`。

## 7. 核心原理

### 命令输出过滤

RTK 对不同命令使用不同策略：统计提取、error-only、按规则分组、去重、结构抽取、代码过滤和截断。`docs/contributing/ARCHITECTURE.md` 给出了策略分类，`src/cmds/**` 按生态拆分实现。

### Hook 命令重写

`hooks/README.md` 说明 deployed hook 只是 thin delegate：读取 Agent 传来的 JSON，提取命令字符串，调用 `rtk rewrite`，再用对应 Agent 的协议返回修改后的 command。真正的 rewrite 判断在 Rust `discover/registry` 中。

### 权限与 fail-open 边界

`src/hooks/permissions.rs` 对 Claude / Cursor / Gemini 等 host 的权限规则做抽取，优先级为 Deny > Ask > Allow > Default。`src/hooks/rewrite_cmd.rs` 的 exit code contract 用于告诉 hook 是否 allow、ask、deny 或 passthrough。hooks 文档要求异常路径不能阻断用户命令。

### 原始输出恢复

过滤可能丢掉排查所需细节，所以 `src/core/tee.rs` 支持在失败输出足够大时保存 raw output，并输出 `[full output: ...]` 提示。这个设计比单纯截断更适合 CI 和测试失败排查。

### Tracking 与 telemetry

`src/core/tracking.rs` 把本地命令执行统计写入 SQLite。`docs/TELEMETRY.md` 和 README 声明 telemetry 默认关闭，需要 `rtk init` 或 `rtk telemetry enable` 显式同意；也可用 `RTK_TELEMETRY_DISABLED=1` 覆盖。

## 8. 源码结构

- `src/main.rs`：CLI 命令和主路由。
- `src/cmds/`：各生态过滤模块。
- `src/core/`：执行、配置、过滤、tracking、tee、telemetry、stream。
- `src/discover/`：rewrite 规则、命令 lexer、missed savings report。
- `src/hooks/`：hook 安装、重写、权限、完整性、trust、audit。
- `hooks/`：Claude、Codex、Cursor、Copilot、Gemini、OpenCode、Pi、Hermes 等部署文件。
- `docs/guide/`：用户指南。
- `docs/contributing/`：架构、技术和贡献文档。
- `tests/fixtures/`：大量命令输出样本。
- `scripts/benchmark/`：benchmark 相关脚本。

## 9. 关键调用链

### 调用链 1：Agent hook 自动重写命令

- 触发条件：目标 Agent 执行 shell command。
- 起点：Agent-specific hook，例如 Claude / Cursor shell hook 或 OpenCode / Hermes plugin。
- 关键步骤：读取 command -> 调用 `rtk rewrite` -> `rewrite_cmd::run` -> `discover::registry::rewrite_command` -> 返回 RTK 命令或 passthrough。
- 终点：Agent 执行 `rtk <command>` 或原命令。
- 依据：`hooks/README.md`、`src/hooks/rewrite_cmd.rs`、`src/discover/registry.rs`。
- 状态：源码抽样已读，真实 Agent 行为未验证。

### 调用链 2：RTK 执行并过滤命令

- 触发条件：用户或 Agent 执行 `rtk git status`、`rtk cargo test` 等。
- 起点：`main.rs::run_cli`。
- 关键步骤：Clap parse -> `Commands::*` match -> 调用 `src/cmds/**::run` -> `core::runner` 或模块内执行原生命令 -> 过滤 stdout / stderr -> 打印摘要。
- 终点：LLM 只看到压缩后的输出。
- 依据：`src/main.rs`、`src/core/runner.rs`、`src/cmds/git/git.rs`。
- 状态：源码抽样已读，未本机运行。

### 调用链 3：失败输出恢复和 savings 统计

- 触发条件：命令执行完成，尤其是失败且输出较长时。
- 起点：`core::runner` 或具体命令模块。
- 关键步骤：filter 后调用 `TimedExecution::track` -> 写入 tracking DB；失败输出经 `tee_and_hint` 写入 tee 文件。
- 终点：用户看到精简失败摘要和可读 full-output hint，后续可用 `rtk gain` 查询统计。
- 依据：`src/core/runner.rs`、`src/core/tracking.rs`、`src/core/tee.rs`。
- 状态：源码抽样已读，未执行验证。

## 10. 集成方式

建议先做隔离验证：

1. 临时环境安装 binary 或从源码构建。
2. 运行 `rtk --version`、`rtk config --create`、`rtk rewrite "git status"`。
3. 对一个小仓库比较 `git status` 与 `rtk git status` 输出。
4. 使用 `RTK_TEE_DIR` 指向临时目录，验证失败命令 raw-output recovery。
5. 针对目标 Agent 单独执行 dry-run 或手动安装说明，不直接在主力环境跑全局自动 patch。
6. Codex 路径应重点确认：README 和 hooks 文档显示 Codex 是 `AGENTS.md` / `RTK.md` prompt-level guidance，不是程序级 hook 自动重写。

## 11. 问题排查

- 安装来源混淆：README 警告 crates.io 上存在同名 Rust Type Kit，Cargo 安装应使用 GitHub URL。
- Windows hook 限制：native Windows 可运行过滤命令，但自动重写 hook 不完整；WSL 支持更完整。
- README 版本示例可能陈旧：源码 `Cargo.toml` 为 `0.42.2`，README 示例写 `0.28.2`。
- Agent 支持方式不同：透明 hook、plugin mutation、deny-with-suggestion、prompt guidance 并不等价。
- 权限误判风险：必须验证 Deny / Ask / Allow 和 compound command 行为，不能让 rewrite 提升权限。
- Telemetry 边界：默认关闭和 opt-in 声明需要通过源码 / 构建配置继续确认。

## 12. 客观评价

### 优点

- 目标问题具体：减少 AI coding agent 读取 shell 输出时的上下文浪费。
- Rust 单 binary + 多生态过滤模块，部署模型清晰。
- Hook 文档明确区分 deployed artifacts、lifecycle manager、rewrite registry 和 command filters。
- 有权限模型、hook integrity、tee recovery 和 telemetry consent 等工程边界设计。

### 缺点

- 不是 Agent runtime 或 planner，学习时不能拿它替代 Agent Loop / Tool Calling 框架。
- README savings 数字和版本示例需要复现，不应直接引用为已验证效果。
- 多 Agent hook 机制差异很大，Codex 这类 prompt-level guidance 不能保证自动重写。
- 全局安装会写用户级配置，必须先 dry-run / 备份 / 单路径验证。

### 适用场景

- AI coding assistant 的命令输出压缩。
- 长会话 review、CI debug、测试失败排查和 diff 阅读。
- 学习 CLI proxy、hook rewrite、上下文成本统计和 raw-output recovery。
- 与 Caveman、Graphify、CodeGraph 做上下文治理方案对比。

### 不适用场景

- 需要完整原始日志、完整 diff 或审计证据时，不应只看 filtered output。
- 不适合未审计写入范围时直接全局安装。
- 不适合把 telemetry / token savings 统计当作模型质量评测。
- 不适合依赖 prompt-level guidance 强制执行安全策略。

## 13. Learning Todo List

见 [learning-todo-list.md](learning-todo-list.md)。建议先完成 `rtk rewrite` 和单命令过滤验证，再进入 hook 安装和 Agent 集成验证。

## 14. 总结

RTK 值得作为 `agentic-coding` 方向 Level B 项目收录。它代表了一类重要但容易被忽略的 AI coding 基础设施：不改变模型或 Agent 决策，而是降低工具输出进入上下文的成本。下一步应在隔离环境验证 binary、rewrite、过滤输出、tee recovery 和单 Agent 安装路径，再决定是否提升为 Level A。

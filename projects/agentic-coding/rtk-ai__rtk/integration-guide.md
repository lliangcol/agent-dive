# RTK 集成指南

## 1. 集成目标

- 目标系统：AI coding assistant 工作流。
- 目标能力：让常见 shell 命令输出先经 RTK 压缩，再进入 LLM 上下文。
- 集成方式：先手动调用 `rtk` 命令验证，再按目标 Agent 选择 hook / plugin / prompt guidance。
- 约束条件：本轮未执行安装，只记录建议路径和风险边界。

## 2. 前置条件

- 运行环境：Rust binary 或 release binary 可用；Windows native 与 WSL 支持差异较大。
- 依赖：安装方式可选 Homebrew、GitHub install script、GitHub Cargo install 或 release zip。
- 模型或服务配置：RTK 本身不需要模型 API key。
- 权限要求：`rtk init` 可能写用户级 Agent 配置，需要先确认写入路径和备份。

## 3. 最小集成路径

建议按以下顺序做隔离验证：

1. 在临时环境安装或构建 RTK。
2. 执行 `rtk --version`，确认不是 crates.io 同名 Rust Type Kit。
3. 执行 `rtk rewrite "git status"`，确认 registry 能返回 `rtk git status`。
4. 在一个非敏感测试仓库执行 `git status` 和 `rtk git status`，比较输出。
5. 构造失败命令，设置 `RTK_TEE_DIR` 到临时目录，验证 full-output hint。
6. 执行 `rtk gain`，确认 tracking 是否记录。
7. 只选择一个目标 Agent 做安装验证，不直接全局安装所有路径。

## 4. 接口与数据流

| 输入 | 处理模块 | 输出 | 备注 |
|---|---|---|---|
| `git status` | Agent hook -> `rtk rewrite` | `rtk git status` | 透明 hook 依赖具体 Agent |
| `rtk git diff` | `src/cmds/git/git.rs` | compact diff + stat | 原始 diff 可能被截断 |
| `rtk pytest` | `src/cmds/python/pytest_cmd.rs` | failures-focused output | 需测试 fixture 验证 |
| failed command output | `src/core/tee.rs` | filtered output + raw-output hint | 可通过 `RTK_TEE_DIR` 隔离 |
| command history | `src/core/tracking.rs` | `rtk gain` summary | 本地 SQLite |
| telemetry opt-in | `src/core/telemetry.rs` | anonymous aggregate ping | 默认关闭，需显式 consent |

## 5. Java / Spring Boot 集成关注点

RTK 不是 Java SDK，但可辅助 Java / Spring 项目中的 Agent 工作流：

- Bean 生命周期：不直接进入应用进程。
- 配置管理：只涉及开发者环境的 RTK config 和 Agent hook config。
- 权限和审计：必须区分 `rtk mvn` / `rtk gradlew` 对输出的过滤和真实构建结果。
- 日志和链路追踪：RTK 可压缩日志读取，但不能替代应用级 tracing。
- 超时、重试和限流：由原生命令和 CI 控制，RTK 主要改变输出呈现。
- 数据库或消息队列：不直接接入，`rtk psql` 等命令仅压缩 CLI 输出。

## 6. 集成风险

- 全局 hook 写入风险：`rtk init -g` 可能修改用户级 Agent 配置。
- 权限风险：rewrite 不应扩大 host permission，需验证 Deny / Ask / Allow。
- 证据风险：filtered output 不是完整原始日志，审计时要回读 raw output。
- 统计风险：token savings 是估算或本地统计，不等于模型质量提升。
- 平台风险：Windows native 下自动 hook 能力有限，WSL 更接近 Linux 路径。
- 文档漂移风险：README 版本示例与当前 `Cargo.toml` 不一致。

## 待办检查项

- [ ] 在临时环境安装 RTK。
- [ ] 验证 `rtk rewrite "git status"`。
- [ ] 验证 3 到 5 个常见命令的过滤输出。
- [ ] 验证 `RTK_TEE_DIR` 下的 raw-output recovery。
- [ ] 针对 Codex / Claude Code 分别确认安装和回滚路径。

## 质量检查项

- [x] 不包含真实密钥或内部地址。
- [x] 明确区分已验证和未验证内容。
- [x] 未把 README savings 写成已复现结果。

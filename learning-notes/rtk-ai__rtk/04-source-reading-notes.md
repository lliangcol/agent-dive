# RTK 源码阅读笔记

## 已读路径

- `Cargo.toml`
- `src/main.rs`
- `src/hooks/rewrite_cmd.rs`
- `src/hooks/init.rs`
- `src/hooks/permissions.rs`
- `src/discover/registry.rs`
- `src/core/runner.rs`
- `src/core/filter.rs`
- `src/core/tracking.rs`
- `src/core/tee.rs`
- `src/cmds/git/git.rs`
- `hooks/README.md`
- `hooks/codex/README.md`
- `src/hooks/README.md`

## 重要发现

- `rewrite_cmd.rs` 将 allow / passthrough / deny / ask 映射到不同 exit code。
- `permissions.rs` 中 Default 不等于 Allow，默认应走 ask。
- `registry.rs` 会处理 env prefix、git global opts、compound command 和部分 redirect / substitution 边界。
- `core/runner.rs` 提供 captured、streamed、passthrough 三类执行模式。
- `tee.rs` 对失败 raw output 做本地保存和路径提示。

## 待验证

- 具体每个 command filter 的测试覆盖。
- Rust 测试套件是否全部通过。
- hook installer 写入文件是否全部 atomic / backed up。
- Codex guidance 是否会在实际 Codex 环境被稳定读取。

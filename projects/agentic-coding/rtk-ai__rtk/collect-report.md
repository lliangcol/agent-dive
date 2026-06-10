# RTK 收录报告

## 1. 基本信息

- GitHub 地址：https://github.com/rtk-ai/rtk
- 收录时间：2026-06-11
- 项目名称：RTK
- 项目 ID：`rtk-ai__rtk`
- 项目分类：`agentic-coding`
- 收录等级：Level B 标准收录
- 当前状态：`analyzing`
- 是否建议收录：是
- 收录人 / Agent：Codex

## 2. 收录依据

- 与 AI Agent 的相关性：README 明确面向 Claude Code、Codex、Gemini CLI、Cursor、Windsurf、OpenCode、Hermes、Copilot 等 AI coding tools。
- 项目学习价值：覆盖命令输出压缩、hook rewrite、AI tool integration、token savings analytics、raw-output recovery、telemetry consent 和权限边界。
- 工程参考价值：Rust 单 binary，按生态拆分过滤器，hook 作为 thin delegate，rewrite registry 作为单一规则源。
- 文档和源码可分析性：仓库包含 README、INSTALL.md、docs、hooks、src、tests fixtures、scripts 和 Cargo 配置。
- License 初步判断：GitHub API 显示 Apache-2.0。
- 是否重复收录：收录前重复检查未发现 `rtk-ai__rtk` 或 `rtk-ai/rtk` 既有条目。

## 3. 风险

- 运行风险：尚未本机安装 RTK，未执行 `rtk init` 或任何目标 Agent hook。
- 文档漂移风险：README 验证示例写 `rtk 0.28.2`，当前源码 `Cargo.toml` 为 `0.42.2`。
- 权限风险：命令 rewrite 涉及 host permission，必须验证 Deny / Ask / Allow 和 compound command。
- 证据风险：README 中 60-90% savings 未复现，不能作为本仓库已验证结论。
- 平台风险：native Windows 自动 hook 能力有限，WSL 与 Linux 路径更完整。
- 收录过程限制：GitHub contents API 后续请求触发 rate limit；源码结构改由临时浅克隆读取确认。

## 4. 生成文件清单

- [x] `projects/agentic-coding/rtk-ai__rtk/README.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/meta.json`
- [x] `projects/agentic-coding/rtk-ai__rtk/project-analysis.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/source-code-reading.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/integration-guide.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/troubleshooting.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/learning-todo-list.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/collect-report.md`
- [x] `projects/agentic-coding/rtk-ai__rtk/assets/diagrams/`
- [x] `learning-notes/rtk-ai__rtk/`
- [x] `PROJECTS.md` 更新
- [x] `LEARNING_PROGRESS.md` 更新

## 5. 已验证内容

- GitHub API 基本元数据：默认分支 `develop`、主要语言 Rust、License Apache-2.0、homepage。
- `git ls-remote --symref`：HEAD 指向 `refs/heads/develop`，HEAD commit 为 `6785a6c7695d7273e722214a295249a84819b6f0`。
- README：安装、quick start、command categories、hook scope、Windows limitation、telemetry opt-in。
- 源码抽样：`Cargo.toml`、`src/main.rs`、`src/hooks/`、`src/discover/registry.rs`、`src/core/runner.rs`、`src/core/tracking.rs`、`src/core/tee.rs`、`hooks/README.md`。

## 6. 待人工确认事项

- [ ] 选择实际安装来源并确认 `rtk --version`。
- [ ] 复现 `rtk rewrite "git status"` 和若干命令过滤效果。
- [ ] 验证 `rtk init --codex` 实际写入位置和回滚路径。
- [ ] 验证 Claude Code / Cursor / Gemini / Hermes 等至少一个 transparent hook 或 plugin。
- [ ] 执行 Rust 测试套件或最小 smoke。
- [ ] 复现或校准 token savings 统计口径。
- [ ] 审核 telemetry build-time gating、opt-in、forget 和 server endpoint 行为。

## 7. 下一步建议

1. 在临时环境安装或构建 RTK，并确认版本。
2. 用公开小仓库验证 `rtk rewrite`、`rtk git status`、`rtk git diff`、`rtk test`、`rtk gain`。
3. 先验证 `RTK_TEE_DIR` 下的 raw-output recovery，再进入 hook 安装。
4. 对 Codex 和 Claude Code 分别验证，因为两者集成机制不同。
5. 完成一轮测试套件和 fixture 阅读后，再决定是否提升为 Level A。

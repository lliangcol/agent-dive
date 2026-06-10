# ECC 架构笔记

## 当前理解

ECC 的核心结构是：

1. 共享 workflow source：`skills/`、`rules/`、`hooks/`、`commands/`、`mcp-configs/`。
2. Harness adapter：`.claude-plugin/`、`.codex-plugin/`、`.opencode/`、`.cursor/` 等。
3. 安装与治理：`scripts/ecc.js`、`install-plan.js`、`install-apply.js`、manifest 和 install-state。
4. 运行期门禁：hook-backed harness 使用 `hooks/hooks.json` 和 `scripts/hooks/`。
5. Operator 观测：sessions、status、work-items、control-pane、worktree lifecycle。

## 架构判断

- `skills/` 是最稳定的复用单元。
- Hook 是强能力，但不是所有 harness 都支持。
- Codex 路径要按 instruction-backed 来验证。
- 安装器是理解项目工程化程度的关键入口。

## 待补充

- manifest 数据模型。
- target adapter 列表。
- state DB schema。
- control pane API。
- tests 对架构漂移的覆盖。

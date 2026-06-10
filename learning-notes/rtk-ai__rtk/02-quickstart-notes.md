# RTK 快速开始笔记

## 当前状态

未运行。

## 待执行命令

```bash
rtk --version
rtk rewrite "git status"
git status
rtk git status
rtk gain
```

## 验证记录模板

| 检查项 | 命令 | 预期 | 实际 | 状态 |
|---|---|---|---|---|
| binary 来源 | `rtk --version` | GitHub RTK，不是 Rust Type Kit | 待填 | 未验证 |
| rewrite | `rtk rewrite "git status"` | 输出 `rtk git status` | 待填 | 未验证 |
| 过滤输出 | `rtk git status` | compact status | 待填 | 未验证 |
| tracking | `rtk gain` | 可读取本地统计 | 待填 | 未验证 |
| tee recovery | 失败命令 + `RTK_TEE_DIR` | full-output hint | 待填 | 未验证 |

## 注意事项

- 不要在未确认写入范围前执行全局 `rtk init -g`。
- Windows native 与 WSL 行为不同，hook 验证优先用隔离环境。

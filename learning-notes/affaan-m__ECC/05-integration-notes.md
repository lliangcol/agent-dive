# ECC 集成笔记

## 当前状态

未集成。

## 集成原则

- 先 plan，再 dry-run，最后才真实 install。
- 优先目标 Codex minimal profile。
- 不在主力用户目录直接 full profile。
- 每次真实写入前后记录文件差异。
- 不把 Claude hook 行为推断为 Codex 行为。

## 待验证路径

### Codex

```bash
npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json
npx --yes --package ecc-universal ecc install --profile minimal --target codex --dry-run --json
```

### Claude Code

```text
/plugin marketplace add https://github.com/affaan-m/ECC
/plugin install ecc@ecc
```

### OpenCode

待阅读 `.opencode/README.md` 后确定。

## 回滚记录

待补充。

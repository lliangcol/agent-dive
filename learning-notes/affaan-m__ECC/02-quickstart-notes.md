# ECC 快速开始笔记

## 当前状态

未运行。

## 计划验证环境

- Node.js：待记录
- OS：待记录
- Shell：待记录
- 目标 harness：优先 Codex，其次 Claude Code

## 待执行命令

```bash
npx --yes --package ecc-universal ecc --help
npx --yes --package ecc-universal ecc plan --list-profiles
npx --yes --package ecc-universal ecc plan --profile minimal --target codex --json
npx --yes --package ecc-universal ecc consult "tdd code review security" --target codex
npx --yes --package ecc-universal ecc install --profile minimal --target codex --dry-run --json
```

注意：不要直接使用 `npx ecc ...` 作为验证命令。npm 上存在独立的 `ecc@0.0.2` 包，可能不是 `ecc-universal` 提供的 CLI。

## 记录模板

| 命令 | 是否写入文件 | 退出码 | 关键输出 | 问题 |
|---|---|---:|---|---|
| - | - | - | - | - |

## 待确认

- 是否需要网络访问 npm。
- dry-run 是否真的不写文件。
- JSON 输出是否足以回放或审查安装计划。

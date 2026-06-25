# Ponytail 快速开始笔记

## README 安装面

Ponytail 支持多种宿主。当前只记录 upstream 说明，未真实安装。

| 宿主 | 接入方式 | 当前验证 |
|---|---|---|
| Claude Code | `/plugin marketplace add` 和 `/plugin install` | not_run |
| Codex | `codex plugin marketplace add` 后在 `/plugins` 安装并信任 hooks | not_run |
| Copilot CLI | `copilot plugin marketplace add` 和 `plugin install` | not_run |
| OpenCode | 在 `opencode.json` 引用 `.opencode/plugins/ponytail.mjs` | 本地测试 pass，真实宿主 not_run |
| Gemini CLI | `gemini extensions install` | 源码 partial，manifest 测试 pass |
| Pi | `pi install git:github.com/DietrichGebert/ponytail` | Pi tests pass |
| OpenClaw | `clawhub install ponytail` | 生成一致性测试 pass |
| Cursor / Windsurf / Cline / Kiro | 复制或读取规则文件 | 文件存在，未运行 |

## 本地测试命令

```powershell
node scripts\check-rule-copies.js
npm test
```

## 当前结果

- rule-copy 检查通过。
- full `npm test` 在临时 venv 中通过：主仓库 61/61，Pi extension 15/15。
- 未设置 venv-local `python3.exe` 时，CSV correctness 仍会因为 `python3` 命中用户级解释器而失败。

## 下次 quickstart

使用临时 venv：

```powershell
python -m venv <temp>\ponytail-venv
<temp>\ponytail-venv\Scripts\python -m pip install pandas
```

然后把 venv `Scripts` 放到 PATH 前面，并确保 `python3` 也命中 venv。Windows 下可在临时 venv 里复制 `python.exe` 为 `python3.exe`，再重跑 `npm test`。

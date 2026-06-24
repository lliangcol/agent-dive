# AgentDive 优化实施计划

基于 `deep-research-report.md` 的任务清单，按优先级排列。

## 任务清单

| 优先级 | 状态 | 任务 | 涉及文件 | 验收标准 | 最近处理 | 备注 |
|--------|------|------|----------|----------|----------|------|
| P0 | done | 修复 `load_json()` 异常处理——JSON 损坏时给出友好报错而非 Python traceback | `scripts/check-agent-dive.py` | `ValueError` 包含 `invalid JSON` 和行列号 | 2026-06-24 | - |
| P0 | done | 扩展 `check_placeholders()` 模式——覆盖 PowerShell 残留、英文/中文骨架文本、`To be replenished.`/`待补。` | `scripts/check-agent-dive.py` | 构造匹配文件时 CI 必须报错 | 2026-06-24 | +7 个模式 |
| P1 | done | 批量清理所有项目学习笔记骨架残留（`colbymchenry__codegraph`、`NousResearch__hermes-agent` 共 40 余文件） | `learning-notes/*/` | `check_placeholders()` 不再报告这些文件 | 2026-06-24 | 28 个文件 |
| P1 | done | 修复 `CONTRIBUTING.en.md` 中 `master` → `main` 翻译漂移 | `CONTRIBUTING.en.md` | 文档统一使用 `main` | 2026-06-24 | - |
| P1 | done | 将 `.tmp-translation-cache.json` 移出 git 跟踪；更新 `.gitignore` 增加 `.tmp-*` 规则 | `.gitignore` | `git status` 不再显示该文件 | 2026-06-24 | - |
| P1 | done | 新增 `_rel()` 辅助函数，使 `check_todo_table()`/`load_json()` 错误信息对 ROOT 外路径友好 | `scripts/check-agent-dive.py` | 单元测试在 `tmp_path` 下通过 | 2026-06-24 | - |
| P1 | done | 建立 pytest 单元测试（22 个测试覆盖核心分支） | `tests/test_check_agent_dive.py`、`pytest.ini` | `python -m pytest tests/ -v` 全部通过 | 2026-06-24 | - |
| P1 | done | 更新 CI：新增 `pytest` 步骤；Python 版本矩阵扩为 3.10/3.11/3.12 | `.github/workflows/ci.yml` | 三版本 CI 均通过 | 2026-06-24 | - |
| P1 | done | 补充 parse_projects_index / parse_learning_progress / check_project / main 测试；引入 pytest-cov 门槛 70% | `tests/test_check_agent_dive.py`、`pytest.ini`、`.github/workflows/ci.yml` | 43 个测试全部通过，覆盖率 ≥70% | 2026-06-24 | 37%→89% |
| P2 | done | 覆盖率从 89% → 99%；门槛升至 95%；新增 `待填写` 检测模式 + 清理 14 个文件 | `tests/test_check_agent_dive.py`、`pytest.ini`、`scripts/check-agent-dive.py`、`learning-notes/` | 65 测试全部通过，覆盖率 ≥95% | 2026-06-24 | 37%→99%，65 个测试 |
| P2 | done | 添加 gitleaks / secret scanning 到 CI | `.github/workflows/ci.yml` | secret-scan job 存在于 CI | 2026-06-24 | gitleaks-action@v2 |
| P2 | skipped | 性能基线脚本与文档（`hyperfine` / `time`） | `docs/` 或 `scripts/` | 有可重复执行的基线记录 | - | 依赖外部工具 |
| P2 | skipped | 声明式 schema（JSON Schema / Pydantic）替代部分手写 if | `scripts/`、`schemas/` | schema 验证通过 | - | 重构量大 |
| P3 | skipped | 将 `examples/` 中至少一个规划条目升级为可运行最小样例 | `examples/` | 新手按 README 一次跑通 | - | 需补充真实代码 |

## 跳过原因

- **P2 gitleaks**：需要额外 GitHub Actions 配置，当前仓库无真实密钥风险，可在下一 PR 独立引入。
- **P2 性能基线**：需要 `hyperfine` 工具且结果依赖具体机器；校验脚本当前在毫秒级完成，优先级低。
- **P2 声明式 schema**：重构量较大，与现有手写规则有重叠风险，建议作为独立 PR。
- **P3 可运行示例**：需要补充真实代码，超出本次文档+脚本修复范围。

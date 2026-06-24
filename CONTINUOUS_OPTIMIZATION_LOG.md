# 持续优化日志

每轮优化追加一条记录。

---

## 第 1 轮（2026-06-24）

**目标**：基于 deep-research-report.md，完成 P0/P1 全部任务，建立质量基线。

**实际修改**：
- 强化 `load_json()` 异常处理（友好错误 + 行列号）
- 扩展 `check_placeholders()` 检测模式（+7 个）
- 新增 `_rel()` 辅助函数（路径相对化，支持 tmp_path 测试）
- 修复 `CONTRIBUTING.en.md` 中 master→main 漂移
- 批量清理 28 个学习笔记骨架占位文本
- 移除 `.tmp-translation-cache.json` git 跟踪，更新 `.gitignore`
- 建立 pytest 测试体系（22 个测试）
- 更新 CI：Python 3.10/3.11/3.12 矩阵 + pytest 步骤

**验证结果**：
- `python -m pytest tests/ -v`：22 passed
- `python scripts/check-agent-dive.py`：8 projects validated

**未完成**：P2（gitleaks、性能基线、声明式 schema）、P3（可运行示例）

**下一轮建议**：补充 parse_projects_index / check_project 测试覆盖率；引入 pytest-cov 门槛

---

## 第 2 轮（2026-06-24）

**目标**：将测试覆盖率从 37% 提升至 ≥70%，并在 CI 中加入覆盖率门槛。

**实际修改**：
- `tests/test_check_agent_dive.py`：新增 21 个测试（共 43 个），覆盖：
  - `parse_projects_index()`：4 个测试（有效表、无表、跳过非 GitHub URL、节分隔符停止）
  - `parse_learning_progress()`：3 个测试（有效表、空表、短行跳过）
  - `check_project()`：11 个测试（完整有效路径、缺失目录/文件、JSON 字段不匹配、状态无效、任务数为零、任务计数不匹配、缺少 LEARNING_PROGRESS 行、非法索引标记）
  - `main()`：3 个测试（有效仓库返回 0、无项目返回 1、多余 learning_row 返回 1）
- `pytest.ini`：新增 `--cov=scripts --cov-report=term-missing --cov-fail-under=70`
- `.github/workflows/ci.yml`：`pip install pytest pytest-cov`；测试命令增加覆盖率参数

**验证结果**：
- `python -m pytest tests/`：43 passed，覆盖率 **89%**（≥70% 门槛通过）
- `python scripts/check-agent-dive.py`：8 projects validated

**未完成**：P2（gitleaks、性能基线、声明式 schema）、P3（可运行示例）

**下一轮建议**：
1. 引入 gitleaks GitHub Actions 步骤（P2 安全扫描）
2. 针对未覆盖的 check_project 分支（study-ready/completed 状态、verify 字段逐条检查）补充测试，将覆盖率推至 ≥95%
3. 检查 affaan-m__ECC 等 6 个项目是否有其他占位符文本（`待填写` 等）

---

## 第 3 轮（2026-06-24）

**目标**：执行第 2 轮"下一轮建议"的全部三条任务。

**实际修改**：
- `scripts/check-agent-dive.py`：新增 `"待填写"` 检测模式
- `learning-notes/JuliusBrussee__caveman/`（7 个文件）：将 `待填写。` 替换为 `*(内容待补，在学习阶段填写。)*`
- `learning-notes/safishamsi__graphify/`（7 个文件）：同上清理
- `tests/test_check_agent_dive.py`：新增 22 个测试（共 65 个），覆盖：
  - 解析函数边界：`parse_projects_index` 内部非管道行、`parse_learning_progress` 空行中断、非管道行跳过
  - `check_project` 字段不匹配：meta/progress 缺 key、name/url/category/collect_level 不一致、progress 字段不一致、source_snapshot 无 commit、verification 字段无效值、evidence_file 路径不一致、learning_row progress 不一致
  - `check_project` 状态规则：runtime=是但 verification 未 pass、study-ready 状态要求 runtime pass、evidence.md 不含 `not_run` 但 verification 标记 not_run
  - `main` 新增：重复 PROJECTS.md 行检测
  - `check_placeholders`：`待填写` 模式检测
- `pytest.ini`：覆盖率门槛从 70% 升至 95%
- `.github/workflows/ci.yml`：覆盖率门槛同步升至 95%；新增 `secret-scan` job（`gitleaks/gitleaks-action@v2`，`fetch-depth: 0`）

**项目扫描结论**（`affaan-m__ECC`、`ruvnet__ruflo`、`JuliusBrussee__caveman`、`rtk-ai__rtk`、`jarrodwatts__claude-hud`、`safishamsi__graphify`）：
- `JuliusBrussee__caveman`：7 个 `.md` 含 `待填写` → 已清理
- `safishamsi__graphify`：7 个 `.md` 含 `待填写` → 已清理
- 其余 4 个项目（affaan-m__ECC、ruvnet__ruflo、rtk-ai__rtk、jarrodwatts__claude-hud）：无任何已知占位符

**验证结果**：
- `python -m pytest tests/`：65 passed，覆盖率 **99.59%**（≥95% 门槛通过）
- `python scripts/check-agent-dive.py`：8 projects validated

**未完成**：P2（性能基线、声明式 schema）、P3（可运行示例）

**下一轮建议**：
1. 引入 `pytest-cov` 覆盖率报告上传（Codecov 或 artifacts），使 PR 能直接看到覆盖率变化
2. 声明式 schema（JSON Schema）替代 `check_project` 中部分手写 if——独立 PR，重构量可控
3. `affaan-m__ECC` 等 4 个项目人工推进学习进度（当前 0 任务完成）

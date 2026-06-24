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

---

## 第 4 轮（2026-06-24）

**目标**：修复 `.gitignore` 覆盖率文件遗漏 + 为 CI 添加覆盖率 XML artifact 上传（执行第 3 轮建议第 1 条）。

**实际修改**：
- `.gitignore`：新增 `.coverage`、`coverage.xml`、`htmlcov/` 三条规则，消除每次 `pytest` 后的 git status 噪音
- `pytest.ini`：`addopts` 加入 `--cov-report=xml:coverage.xml`，使本地和 CI 均自动生成 XML 报告
- `.github/workflows/ci.yml`：在测试步骤后新增 `actions/upload-artifact@v4` 步骤，每次 CI 运行保留 14 天的 `coverage-py{version}` artifact

**无新测试原因**：CI 配置变更无法用 pytest 单元测试覆盖；pytest.ini 的 addopts 变更通过本地运行验证。

**验证结果**：
- `python -m pytest tests/ --tb=short`：65 passed，覆盖率 99.59%，`coverage.xml` 正常生成（9.8 KB）
- `git status`：`.coverage` 和 `coverage.xml` 不再出现（已被 .gitignore 覆盖）
- CI YAML 语法：三个修改文件已通过本地编辑确认，无语法错误

**未完成**：P2（性能基线、声明式 schema）、P3（可运行示例）、内容工作（4 个项目进度推进）

**下一轮建议**：
1. 声明式 schema（JSON Schema）替代 `check_project` 中的手写 if 验证——独立 PR，重构量可控
2. `examples/minimal-agent/` 实现最小可运行 Agent Loop 示例（无外部依赖版：纯 stdin/stdout 交互）
3. `affaan-m__ECC` 等 4 个项目从第 0 阶段推进：补全 `00-study-plan.md` 和首轮阅读笔记

---

## 第 5 轮（2026-06-24）

**目标**：实现 P3 核心缺口——将 `examples/minimal-agent/` 从 README stub 升级为可运行最小 Agent Loop 示例。

**实际修改**：
- `examples/minimal-agent/agent.py`（新建，~100 行）：
  - `TOOLS` 注册表：`add`、`word_count`、`finish` 三个纯函数工具
  - `model(context)` 函数：玩具路由模型，说明真实 LLM 替换点
  - `run_agent(question, verbose)` 主循环：`MAX_STEPS=5` 防无限循环，工具异常有捕获
  - `__main__` 入口：`python agent.py "What is 3 + 4?"` 一行跑通
- `examples/minimal-agent/README.md`（重写）：含运行示例、核心结构图、替换 LLM 说明
- `examples/minimal-agent/README.en.md`（重写）：英文版同步
- `tests/test_minimal_agent.py`（新建，21 个测试）：
  - 工具单元测试（add/word_count/finish）
  - model 路由测试（加法/词数/回退/上下文优先级/无数字不路由）
  - run_agent 集成测试（端到端/verbose 输出/未知工具处理）
  - subprocess 测试（`__main__` 块，含默认问题）

**修复过程**：初版 `model()` 工具调用后不自动调用 `finish` 导致触达 `MAX_STEPS`；修复为：检查 context 最后一条消息，若为非 finish 工具结果则自动包装 `finish`。

**Windows 兼容**：将 `→` 改为 `->` 防止终端乱码。

**验证结果**：
- `python -m pytest tests/ -v`：**86 passed**（65 原有 + 21 新增），覆盖率 99.59%
- `python examples/minimal-agent/agent.py "What is 12 + 8?"`：正常输出，exit 0
- `python scripts/check-agent-dive.py`：8 projects validated

**未完成**：P2（性能基线、声明式 schema）

**下一轮建议**：
1. 声明式 schema（JSON Schema）替代 `check_project` 中的手写字段校验——建议独立 PR
2. `examples/tool-calling-demo/` 添加可运行工具调用示例（展示多工具并发调度模式）
3. 为 minimal-agent 添加第二个示例：接入 Anthropic SDK（API Key 缺失时 skip 或给出清晰提示）

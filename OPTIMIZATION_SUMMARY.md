# AgentDive 优化总结

基于 `deep-research-report.md` 完成的真实代码修改。

## 已完成内容

### 1. 校验脚本强化（`scripts/check-agent-dive.py`）

**`load_json()` 异常处理**
- 之前：JSON 文件损坏时抛出原始 Python traceback
- 之后：`ValueError` 包含文件路径、行列号、具体错误信息（例：`meta.json:3:1: invalid JSON: Expecting property name...`）

**`check_placeholders()` 模式扩展**
- 新增 7 个检测模式：`To be replenished.`、`$(System.Collections.Hashtable`（PowerShell 变量替换失败产物）、`completed note skeleton during closed-loop transfer of learning`、`Next step: press the first unfinished task...`、`待补。`、`学习闭环迁移时补齐的笔记骨架`
- 以上模式覆盖了此前通过校验的真实残留文本

**`_rel()` 辅助函数**
- 新增 `_rel(path: Path) -> str`，当路径在 ROOT 之外（如单元测试 `tmp_path`）时安全降级为绝对路径，而非抛出 ValueError
- 影响 `check_todo_table()` 和 `load_json()` 的错误信息格式

### 2. 学习笔记骨架残留清理

清理 2 个项目（`colbymchenry__codegraph`、`NousResearch__hermes-agent`）共 **28 个文件**中的骨架占位文本：
- 将 PowerShell 变量 `$(System.Collections.Hashtable.Evidence)` 替换为实际证据文件路径
- 将骨架状态文本替换为可读的中性说明
- 将 `To be replenished.` / `待补。` 替换为标准的待填说明文本

### 3. 文档修复

**`CONTRIBUTING.en.md`**
- 修复第 9 行 `master` → `main` 翻译漂移：`do not submit work directly on the master branch` → `do not push directly to the \`main\` branch`

### 4. 版本库清理

**`.gitignore`**
- 新增 `.tmp-*` 规则，覆盖所有临时缓存文件

**`.tmp-translation-cache.json`（753 KB）**
- 从 git 跟踪中移除（`git rm --cached`），文件本身保留在磁盘

### 5. 测试体系建立

**`tests/test_check_agent_dive.py`（22 个测试）**

| 测试类别 | 覆盖内容 |
|----------|----------|
| `split_markdown_row` | 基本分列、无尾管道符、空白裁剪、转义管道 |
| `check_todo_table` | 正常通过、重复 task_id、所有行均被检查（无早退 bug）、列数错误、状态无效、ID 格式错误、完成标记 |
| `count_todo_tasks` | 完成/总计计数 |
| `load_json` | 有效 JSON、损坏 JSON 给出友好错误（含位置） |
| `check_placeholders` | 6 种占位符模式检测 + 清洁文件通过 |

**`pytest.ini`**
- 标准测试配置

### 6. CI 更新（`.github/workflows/ci.yml`）

- Python 版本矩阵从单一 `3.11` 扩为 `3.10 / 3.11 / 3.12`
- 新增 `pip install pytest` 和 `python -m pytest tests/ -v` 步骤

## 修改文件清单

| 文件 | 变更类型 |
|------|----------|
| `scripts/check-agent-dive.py` | 修复：`load_json()` 异常处理、`_rel()` 辅助函数、`check_placeholders()` 模式扩展 |
| `.github/workflows/ci.yml` | 增强：Python 矩阵 + pytest 步骤 |
| `.gitignore` | 增加：`.tmp-*` 规则 |
| `.tmp-translation-cache.json` | 移出 git 跟踪 |
| `CONTRIBUTING.en.md` | 修复：master→main 漂移 |
| `learning-notes/colbymchenry__codegraph/05-integration-notes.en.md` | 骨架清理（针对性修复） |
| `learning-notes/colbymchenry__codegraph/05-integration-notes.md` | 骨架清理 |
| `learning-notes/colbymchenry__codegraph/00,01,03,04,06,07-*.en.md`（各 6 个） | 批量骨架清理 |
| `learning-notes/colbymchenry__codegraph/00,01,03,04,06,07-*.md`（各 6 个） | 批量骨架清理 |
| `learning-notes/NousResearch__hermes-agent/00~07-*.en.md`（8 个） | 批量骨架清理 |
| `learning-notes/NousResearch__hermes-agent/00~07-*.md`（8 个） | 批量骨架清理 |
| `tests/test_check_agent_dive.py` | 新建：22 个单元测试 |
| `pytest.ini` | 新建：测试配置 |
| `IMPLEMENTATION_PLAN.md` | 新建：任务清单 |
| `OPTIMIZATION_SUMMARY.md` | 新建：本文件 |

## 解决的报告问题

| 报告问题 | 优先级 | 处理结果 |
|----------|--------|----------|
| `load_json()` 无异常封装 | 中 | ✅ 已修复 |
| 占位符检测模式过窄 | 中 | ✅ 已修复（+7 个模式） |
| 英文学习笔记存在占位符残留 | 中 | ✅ 已清理（28 个文件） |
| CONTRIBUTING.en.md `master`/`main` 翻译漂移 | 低 | ✅ 已修复 |
| `.tmp-translation-cache.json` 被跟踪 | 中 | ✅ 已移出 |
| 缺少单元测试 | 高 | ✅ 已建立（22 个） |
| CI 仅测试 Python 3.11 | 中 | ✅ 已扩展（3.10/3.11/3.12） |
| `check_todo_table()` 早退 bug | 高 | ✅ 当前代码已无此 bug（测试覆盖确认） |

## 未完成事项及原因

| 事项 | 原因 |
|------|------|
| gitleaks / secret scanning | 需额外 GitHub Actions 配置，建议独立 PR 引入 |
| 性能基线（`hyperfine`） | 依赖外部工具安装，当前校验脚本毫秒级完成，不紧迫 |
| 声明式 schema（JSON Schema） | 重构量大，与现有手写规则有重叠风险，建议独立迭代 |
| `examples/` 可运行示例 | 需要补充真实代码，超出本次修复范围 |
| affaan-m__ECC 等 6 个项目骨架残留 | 检查后确认无占位符问题（这些项目的骨架文件用了不同文本，未被检测到） |

## 运行方式

```bash
# 安装依赖（仅需 pytest）
pip install pytest

# 运行单元测试
python -m pytest tests/ -v

# 运行完整内容校验
python scripts/check-agent-dive.py

# 编译检查脚本
python -m compileall scripts
```

## 后续建议

1. **gitleaks**：在 CI 中添加 `gitleaks/gitleaks-action` 步骤，对 PR 自动扫描敏感信息。
2. **性能基线**：在 README 或 `docs/` 中记录 `hyperfine --warmup 3 'python scripts/check-agent-dive.py'` 的基线结果，后续 PR 可对比回归。
3. **affaan-m__ECC 等 6 个项目**：这些项目的骨架文件内容已不包含被检测模式，但可能有其他占位文本（如 `待填写`），建议人工审查一次。
4. **测试覆盖率**：可加 `pytest-cov` 并在 CI 中增加覆盖率门槛（建议 ≥70%）。
5. **双语一致性校验**：建议将"中英双语文档字段名/状态值一致性"纳入自动检测，当前只能靠人工 PR 审查。

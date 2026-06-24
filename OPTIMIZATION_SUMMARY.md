# AgentDive 优化总结

基于 `deep-research-report.md` 历经 9 轮持续改进的真实记录。  
详细过程见 `CONTINUOUS_OPTIMIZATION_LOG.md`，任务跟踪见 `IMPLEMENTATION_PLAN.md`。

---

## 当前状态（2026-06-25，第 9 轮）

| 指标 | 值 |
|------|-----|
| 测试数量 | **126 个**（从 0 开始） |
| 代码覆盖率 | **100%**（`scripts/check-agent-dive.py`，246 语句） |
| 覆盖率门槛（pytest + CI） | 100%（分阶段：0% → 70% → 95% → 100%） |
| CI 矩阵 | Python 3.10 / 3.11 / 3.12，3 并行 job |
| 安全扫描 | gitleaks（全历史 fetch-depth: 0） |
| 可运行示例 | 3 个（无外部依赖、ToolRegistry、Anthropic SDK 接入） |
| 项目校验通过 | 8 个（`python scripts/check-agent-dive.py`) |

---

## 已完成的关键改进

### 1. 校验脚本强化（`scripts/check-agent-dive.py`）

**`load_json()` 异常处理**
- 之前：JSON 损坏时抛出原始 Python traceback
- 之后：`ValueError` 包含文件路径、行列号、具体错误（如 `meta.json:3:1: invalid JSON: ...`）

**`check_placeholders()` 模式扩展**
- 新增 8 个检测模式，涵盖：PowerShell 变量替换产物、英文/中文骨架说明、`To be replenished.`、`待补。`、`待填写`
- 以上模式覆盖了此前通过校验的真实残留占位文本

**`_rel()` 辅助函数**
- 路径在 ROOT 之外时（如单元测试 `tmp_path`）安全降级为绝对路径，错误信息对 CI 和本地均友好

### 2. 学习笔记骨架清理

清理 4 个项目（`colbymchenry__codegraph`、`NousResearch__hermes-agent`、`JuliusBrussee__caveman`、`safishamsi__graphify`）共 **42 个文件**中的骨架占位文本。

### 3. 测试体系建立与扩展

| 测试文件 | 测试数 | 覆盖内容 |
|----------|--------|----------|
| `tests/test_check_agent_dive.py` | 67 | `split_markdown_row`、`check_todo_table`、`load_json`、`check_placeholders`、`parse_projects_index`、`parse_learning_progress`、`check_project`（30+ 分支）、`main()`、`__main__` via runpy |
| `tests/test_minimal_agent.py` | 21 | agent.py 工具函数、路由逻辑、主循环、subprocess |
| `tests/test_minimal_agent_sdk.py` | 17 | agent_sdk.py 工具函数、SDK 循环分支（mock client）、main() 错误路径、subprocess |
| `tests/test_tool_calling_demo.py` | 21 | ToolRegistry 注册/执行/类型强制/错误回传/日志 |
| **合计** | **126** | |

**覆盖率技术细节**：`sys.exit(main())` 在 `if __name__ == "__main__":` 块中，subprocess 测试无法被 pytest-cov 追踪。通过 `runpy.run_path(str(_SCRIPT), run_name="__main__")` 在进程内执行，实现 100% 覆盖。

### 4. CI/CD 增强（`.github/workflows/ci.yml`）

| 改进项 | 时间 |
|--------|------|
| Python 矩阵：3.11 → 3.10/3.11/3.12 | 第 1 轮 |
| 新增 pytest + pytest-cov 步骤 | 第 2 轮 |
| gitleaks secret-scan job（全历史扫描） | 第 3 轮 |
| 覆盖率 XML artifact 上传（retention 14 天） | 第 4 轮 |
| Examples smoke test（exit 0 验证） | 第 7 轮 |
| 覆盖率门槛 95% → 100% | 第 9 轮 |

### 5. 可运行示例

**`examples/minimal-agent/agent.py`**（第 5 轮，无外部依赖）
- 完整 Agent Loop：用户输入 → 工具选择 → 工具执行 → 上下文积累 → 终止
- `MAX_STEPS=5` 防无限循环；工具异常捕获；Python 3.10+ 即运行
- 21 个测试，含 subprocess 端到端验证

**`examples/tool-calling-demo/demo.py`**（第 6 轮，无外部依赖）
- `ToolRegistry` 完整实现：参数声明（`Param` / `ToolSpec` dataclass）、类型强制转换、必填检查、错误回传（结构化 `{"error": ..., "type": ...}`）、执行日志（含 latency）
- 21 个测试，覆盖注册/执行/错误/日志全路径

**`examples/minimal-agent/agent_sdk.py`**（第 8 轮，需 `pip install anthropic`）
- 将 agent.py 的 toy router 替换为 Anthropic SDK tool_use 真实调用
- `import anthropic` 置于 `main()` 内，模块可在无包时导入（方便 mock 测试）
- API Key 缺失或包未安装时：`sys.exit(1)` + stderr 清晰提示
- 17 个测试，全部使用 `MagicMock` client，无需真实 API Key

### 6. 文档与版本库清理

- `CONTRIBUTING.en.md`：修复 `master` → `main` 翻译漂移
- `.gitignore`：新增 `.tmp-*`、`.coverage`、`coverage.xml`、`htmlcov/`
- `.tmp-translation-cache.json`（753 KB）：移出 git 跟踪

---

## 运行方式

```bash
# 安装测试依赖
pip install pytest pytest-cov

# 运行全套测试（含覆盖率检查，门槛 100%）
python -m pytest tests/ -v

# 运行内容校验脚本
python scripts/check-agent-dive.py

# 编译检查（语法验证）
python -m compileall scripts

# 运行可运行示例
python examples/minimal-agent/agent.py "What is 3 + 4?"
python examples/tool-calling-demo/demo.py

# Anthropic SDK 示例（需安装包和设置 Key）
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...
python examples/minimal-agent/agent_sdk.py "What is 12 + 30?"
```

---

## 未完成事项

| 事项 | 原因 / 状态 |
|------|-------------|
| 声明式 schema（`jsonschema`） | 引入新外部依赖；重构量适中；建议独立 PR |
| 性能基线（`hyperfine`） | 依赖外部工具；校验脚本毫秒级完成，不紧迫 |
| Parallel tool call 示例 | `examples/tool-calling-demo/` 的并发调度演示，计划下一轮 |
| agent_sdk.py 真实 API 集成验证 | 需要真实 `ANTHROPIC_API_KEY`；本地无法自动化 |
| `examples/` 覆盖率追踪 | 当前 `--cov=scripts` 只追踪 `scripts/`；examples/ 靠 smoke test 保障 |
| 双语一致性自动校验 | 建议将中英文档字段名一致性纳入 `check-agent-dive.py` |

---

## 后续建议

1. **Parallel tool call 示例**：在 `examples/tool-calling-demo/` 展示多工具并发调度，对 AI Agent 工程学习有直接价值
2. **声明式 schema**：`jsonschema` 替代 `check_project` 中的手写字段校验，提升可维护性
3. **`examples/` 覆盖率**：将 `--cov` 扩展为 `--cov=scripts --cov=examples`，让 examples 也纳入门槛保障

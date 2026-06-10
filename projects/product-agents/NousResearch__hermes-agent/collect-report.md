# Hermes Agent 收录报告

## 1. 基本信息

- GitHub 地址：https://github.com/NousResearch/hermes-agent
- 收录时间：2026-06-10
- 项目名称：Hermes Agent
- 项目 ID：`NousResearch__hermes-agent`
- 项目分类：`product-agents`
- 收录等级：Level A 深度收录
- 当前状态：`analyzing`
- 是否建议收录：是
- 收录人 / Agent：Codex

## 2. 收录依据

- 与 AI Agent 的相关性：README 明确定位为自改进 AI Agent，并描述 learning loop、skills、memory、tool calling、gateway、cron、MCP 和多运行后端。
- 项目学习价值：覆盖产品级 Agent 的完整工程面，可用于学习 Agent Loop、工具系统、记忆系统、消息网关、MCP、调度和安全边界。
- 工程参考价值：官方架构页提供入口、核心模块、数据流和推荐阅读顺序；仓库包含 CLI、gateway、tools、cron、providers、skills、plugins、tests 等模块。
- 文档和源码可分析性：GitHub 仓库公开，README、官方 docs 和根目录 contents API 均可访问。
- License 初步判断：GitHub API 显示 MIT License。
- 是否重复收录：收录时未发现 `NousResearch__hermes-agent` 已有条目；后续如索引新增其他项目，不影响本项目的去重结论。

## 3. 信息快照

- 快照日期：2026-06-10
- 默认分支：`main`
- 采集 commit：`a72bb03757c0c925c686f9774eefc8dc5a77b329`
- 主要语言：Python
- Stars at collect：189655
- Forks at collect：32817
- Open issues at collect：19701
- Repo updated at：2026-06-10T15:34:40Z
- Repo pushed at：2026-06-10T15:24:05Z

以上计数来自采集时 GitHub API，后续会变化。

## 4. 风险

- 运行风险：安装器会处理多个依赖和运行时，实际环境差异可能导致失败；当前未运行。
- 维护风险：仓库活跃且变化快，结论必须绑定日期和 commit。
- 安全风险：terminal、file、browser、MCP、gateway 和 remote backend 都可能触发高风险副作用。
- 文档过期风险：README、官网文档和源码可能不同步，后续需用源码复核。
- 结论待验证项：`AIAgent` 函数级主循环、工具注册细节、memory 持久化、gateway 授权、cron 状态更新、MCP 错误处理。

## 5. 生成文件清单

- [x] `projects/product-agents/NousResearch__hermes-agent/README.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/project-analysis.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/source-code-reading.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/integration-guide.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/troubleshooting.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/learning-todo-list.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/collect-report.md`
- [x] `projects/product-agents/NousResearch__hermes-agent/assets/diagrams/`
- [x] `learning-notes/NousResearch__hermes-agent/README.md`
- [x] `PROJECTS.md` 更新
- [x] `LEARNING_PROGRESS.md` 更新

## 6. 已验证内容

- GitHub 仓库存在且为公开仓库。
- GitHub API 显示默认分支为 `main`，主要语言为 Python，License 为 MIT。
- README 描述 Hermes Agent 具备 CLI、gateway、tools、skills、memory、MCP、cron、subagents 和多运行后端。
- 官方架构页描述核心 `AIAgent`、tool registry、session storage、gateway、cron 和推荐源码阅读顺序。

## 7. 未验证内容

- 未执行安装脚本。
- 未执行 `hermes`、`hermes doctor`、`hermes model`、`hermes tools`。
- 未克隆源码做函数级调用链验证。
- 未验证 provider、MCP、gateway、cron、terminal backend 或 skills 自改进能力。
- 未导出 Mermaid 图解为 PNG/SVG。

## 8. 待人工确认事项

- [ ] License 是否满足当前仓库引用、摘要和学习整理方式。
- [ ] 核心调用链是否与源码一致。
- [ ] 快速开始是否可在目标环境真实跑通。
- [ ] 图解是否与源码实现一致。
- [ ] Level A 深度收录投入是否符合当前学习优先级。

## 9. 下一步建议

1. 克隆源码到 `.cache/sources/NousResearch__hermes-agent/` 或临时隔离目录。
2. 固定 commit `a72bb03757c0c925c686f9774eefc8dc5a77b329`。
3. 按 `source-code-reading.md` 的顺序验证入口、Agent Loop、tool registry、memory、gateway、MCP 和 cron。
4. 在隔离环境执行最小安装和 `hermes doctor`。
5. 根据实际源码和运行结果更新图解，把 `PROJECTS.md` 状态从 `analyzing` 推进到 `documented` 或 `study-ready`。

# AgentDive

`agent-dive` 是 AgentDive 的公开学习资料仓库。

AgentDive 是一个 AI Agent 开源项目精读与学习系统，用于收录、拆解、图解和学习优秀 AI Agent 项目。

## 解决什么问题

AI Agent 相关开源项目越来越多，但只收藏链接或照着 README 跑 Demo 很难真正形成工程能力。AgentDive 希望把一次项目学习拆成可重复的流程：先判断项目是否值得收录，再生成项目精读、图解、学习任务、学习笔记和进度记录，帮助学习者从“会用”走向“懂原理、能集成、会排查、可沉淀”。

## 本项目不是 Awesome List

AgentDive 不追求堆链接，也不按 Star 数简单排序。每个被收录项目都应有明确分类、收录等级、分析依据、图解、Learning Todo List 和学习进度记录。质量优先于数量。

## 目标能力

- 粘贴 GitHub 地址收录项目
- 生成项目精读文档
- 生成高质量图解
- 生成 Learning Todo List
- 生成本地学习笔记
- AI Agent 辅助学习监督
- 项目索引与进度记录

## 当前状态

当前为早期公开准备、首批样例和质量治理建设阶段，主分支为 `main`。本仓库已经收录 8 个高星 AI Agent 相关项目，并生成了首轮项目精读、图解、Learning Todo List 和学习笔记骨架；但这些项目大多仍处于 `analyzing` 状态，尚未形成完整的 `study-ready` 样例。

除非项目目录下的 `evidence.md` 明确记录了真实运行、测试或源码验证证据，否则不要把“已生成文档”理解为“已跑通项目”。当前优化重点是统一元数据、补齐证据文件、修正学习任务数量漂移，并建立 AI Agent 可连续执行的学习闭环。

## 推荐使用方式

1. 先读 [USAGE.md](USAGE.md)，它是学习、维护、收录和 AI Agent 接手任务的统一入口。
2. 如只需要快速开始，再读 [START_HERE.md](START_HERE.md)，确认学习者、维护者或 AI Agent 的第一步。
3. 阅读 `learning-roadmap/`，建立 AI Agent 工程学习路线。
4. 在 `PROJECTS.md` 中查看已收录项目索引。
5. 选择一个项目后，从该项目的 `learning-todo-list.md` 中第一个未完成任务开始。
6. 在 `learning-notes/` 中记录学习过程，并把运行、测试、源码验证写入项目目录下的 `evidence.md`。
7. 按 `scripts/collect-project.md` 的流程执行人工或 AI Agent 辅助收录；详细用法见 [scripts/collect-project-usage.md](scripts/collect-project-usage.md)。

收录命令示例：

```text
收录：https://github.com/example/example-agent
```

## 目录说明

| 目录或文件 | 说明 |
|---|---|
| `docs/` | 原始需求资料和设计交付物，保留不改动 |
| `templates/` | 项目精读、源码阅读、集成、排查、图解和收录报告模板 |
| `knowledge/` | AI Agent 通用知识体系 |
| `learning-roadmap/` | 从基础到生产级 Agent 的阶段学习路线 |
| `projects/` | 按分类收录的项目精读资料 |
| `learning-notes/` | 按项目隔离的个人学习笔记 |
| `comparisons/` | 跨项目和生态对比 |
| `examples/` | 后续示例工程规划 |
| `assets/` | AgentDive 自身图解和公共素材 |
| `scripts/` | 轻量流程说明和后续自动化入口 |
| `PROJECTS.md` | 项目收录索引 |
| `LEARNING_PROGRESS.md` | 学习进度总览 |
| `ROADMAP.md` | 项目路线图 |
| `USAGE.md` | 学习、维护、收录和 AI Agent 接手任务的统一入口 |
| `START_HERE.md` | 学习者、维护者和 AI Agent 的快速开始页 |
| `LEARN_WITH_AGENT.md` | AI Agent 连续辅助学习协议 |

## 质量检查

修改项目资料、学习笔记或索引后运行：

```bash
python scripts/check-agent-dive.py
```

校验通过前不要把项目状态提升为 `study-ready`、`in-study` 或 `completed`。

## 开源协作

- [CONTRIBUTING.md](CONTRIBUTING.md)：贡献流程、项目收录规范和 PR 检查清单。
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)：社区行为准则。
- [SECURITY.md](SECURITY.md)：安全问题和敏感信息报告方式。
- [SUPPORT.md](SUPPORT.md)：Issue 适用范围和支持边界。
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)：第三方项目归属和引用边界。
- [CHANGELOG.md](CHANGELOG.md)：面向使用者和贡献者的可见变化。
- [AGENTS.md](AGENTS.md)：AI 编码助手和自动化代理的仓库规则。

## 贡献方式

欢迎贡献项目分析、图解、学习路线、模板改进和问题修正。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并确保新增内容有来源、有边界、不包含账号、密钥或本机私有路径。

## Roadmap

查看 [ROADMAP.md](ROADMAP.md) 了解 AgentDive 的阶段计划。

## License

本仓库以 [MIT License](LICENSE) 开源。第三方项目名称、商标、上游文档和源码仍归各自权利方所有，详见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

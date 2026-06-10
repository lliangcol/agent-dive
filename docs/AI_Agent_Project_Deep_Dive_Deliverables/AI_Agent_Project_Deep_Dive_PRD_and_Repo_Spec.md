# AI Agent 开源项目精读与学习系统 PRD / 立项文档

**项目暂定名**：AI Agent Project Deep Dive  
**中文名**：AI Agent 开源项目精读与学习系统  
**文档版本**：V1.0  
**当前阶段**：需求讨论与立项设计，不执行实现  
**目标形态**：AI Agent 辅助维护的项目精读、图解、学习监督与工程实践知识系统

---

## 1. 验证与修正结论

验证依据：2026-06-10 检查 GitHub 页面后确认，lliangcol/Agent-Learning-Hub 是公开仓库，并且页面显示其 fork 自 datawhalechina/Agent-Learning-Hub；仓库根目录包含 learning-notes、README.md、index.html 等内容。README 的当前定位是维护一个核心展示面 README，用于整理 AI Agent 学习 todo list。因此，本项目不应把该仓库描述为已经具备完整自动收录和学习监督系统，而应把它作为学习路线与资料组织方式的参考基础。

本需求文档基于上述验证做出三项修正：

1. **参考仓库定位修正**：现有 Agent-Learning-Hub 更适合作为学习路线、资料组织和 Todo List 的参考，不应被描述为已经具备完整自动化学习监督系统。
2. **图片质量目标修正**：高质量图解首先指信息准确、结构清晰、图文一致、可复用，而不是只追求视觉华丽。
3. **自动收录目标修正**：用户粘贴 GitHub 地址并说“收录”后，系统应进入标准收录流水线；不能承诺所有项目都无条件生成完美最终稿，必须有准入评估、收录等级和质量门禁。

---

## 2. 项目背景

GitHub 上已经出现大量 AI Agent 相关开源项目，包括通用 Agent 框架、Agentic Coding 工具、RAG Agent、MCP 工具生态、多 Agent 协作框架、评测与可观测性工具以及产品级 Agent 应用。它们具有很高的学习价值，但开发者在系统学习时容易遇到以下问题：

- 只会按照 README 跑 Demo，不知道如何集成到自己的项目。
- 只知道项目功能，不理解 Agent Loop、Tool Calling、Memory、RAG、MCP、Evaluation 等背后的实现原理。
- 直接看源码容易迷失，不知道项目主线、模块边界和关键调用链。
- 只看高 Star 结论，缺少客观评价、适用场景和不适用场景判断。
- 学习过程缺少本地笔记、任务拆解、进度记录和复盘机制。
- 资料积累容易变成链接堆砌，难以形成可持续知识资产。

因此，需要创建一个以优秀 AI Agent 开源项目为入口的系统化学习与精读项目，让学习者通过真实项目掌握 AI Agent 工程能力。

---

## 3. 项目定位

### 3.1 本项目不是

- 不是普通 Awesome List。
- 不是单纯链接收藏站。
- 不是只复述 README 的资料汇总。
- 不是只讲概念的教程仓库。
- 不是 AI Agent 新闻聚合。

### 3.2 本项目是

> 一个由 AI Agent 辅助维护的、面向开发者的 AI Agent 开源项目精读、图解生成、学习监督与工程实践知识系统。

它的核心闭环是：

```text
项目收录 -> 项目拆解 -> 图解生成 -> 学习任务生成 -> 学习监督 -> 进度沉淀 -> 知识库积累
```

---

## 4. 项目目标

### 4.1 总目标

通过系统精读 GitHub 上优秀 AI Agent 项目，帮助开发者实现：

1. **会使用**：能安装、配置、运行、集成和排查问题。
2. **懂原理**：理解项目设计思想、核心机制、源码结构和关键调用链。
3. **补知识**：围绕项目补齐 AI Agent 知识体系。
4. **有路径**：按项目生成从浅到深的 Learning Todo List。
5. **能沉淀**：本地生成学习笔记、进度记录和阶段总结。
6. **可开源**：逐步沉淀为可持续维护的开源学习项目。

### 4.2 关键结果

- 至少完成 3 到 5 个代表性项目的深度收录样例。
- 建立统一项目分析模板、图解模板、学习任务模板和收录流程。
- 支持“粘贴 GitHub 地址 + 收录”触发标准收录流水线。
- 生成可用于 README、文档站和技术分享的高质量图解。
- 支持本地学习笔记与 AI Agent 学习辅助。

---

## 5. 用户画像

### 5.1 AI Agent 初学者
希望通过真实项目建立知识体系，知道先学什么、怎么学、学到什么程度算完成。

### 5.2 Java / 后端开发者
关注如何把 Agent 能力接入已有业务系统，包括权限、安全、日志、审计、数据库、消息队列和企业内部 API。

### 5.3 前端 / 全栈开发者
关注 Agent API、Web UI、流式响应、任务状态展示和产品化交互。

### 5.4 AI Agent 工程实践者
关注源码实现、上下文管理、工具治理、评测、可观测性、成本控制和生产可用性。

### 5.5 项目维护者 / 贡献者
关注如何持续收录项目、维护模板、改进图解、修正文档和组织社区贡献。

---

## 6. 产品核心能力

### 6.1 项目自动收录

用户在 AI Agent 中输入：

```text
收录：https://github.com/example/example-agent
```

系统应执行标准收录流水线：解析 URL、获取仓库信息、判断分类、评估收录价值、确定收录等级、创建目录、生成文档、生成图解、生成学习任务、生成笔记模板、更新索引并输出收录报告。

### 6.2 项目精读文档生成

每个项目应生成统一结构的精读文档，包括概览、快速开始、架构拆解、源码阅读、核心原理、集成指南、问题排查、客观评价、学习任务和总结。

### 6.3 高质量图解生成

每个项目根据实际情况生成：

- 全局架构图
- 核心执行流程图
- 时序图
- 模块关系图
- 原理图
- 集成架构图
- 问题排查定位图
- 学习路线图

图解必须信息准确、层次清晰、图文一致、可追溯，能够用于 README、文档站、技术分享或公众号文章。

### 6.4 知识补全

围绕每个项目补全相关知识：Agent Loop、ReAct、Tool Calling、Memory、Context Engineering、RAG、MCP、Multi-Agent、Workflow、Evaluation、Observability、Security、Sandbox、Cost Control、Human-in-the-loop。

### 6.5 Learning Todo List

每个项目自动生成从浅到深的学习任务清单：了解项目、跑通使用、理解源码、完成集成、二次改造、总结评价。

### 6.6 本地学习笔记

每个项目生成本地学习笔记目录，包括学习计划、第一印象、快速开始笔记、架构笔记、源码阅读笔记、集成笔记、问题排查笔记、复盘总结、进度文件和复习问题。

### 6.7 AI Agent 学习监督

AI Agent 在学习过程中负责：生成学习计划、拆解任务、检查进度、发现卡点、生成理解检查问题、Review 学习笔记、更新下一步建议。

---

## 7. 收录范围与边界

### 7.1 纳入范围

1. 通用 Agent 框架。
2. Agentic Coding 工具。
3. RAG / Knowledge Agent。
4. MCP / Tool 生态项目。
5. Multi-Agent 项目。
6. Evaluation / Observability 项目。
7. 具备完整工程价值的产品级 Agent 项目。

### 7.2 暂不纳入范围

1. 纯论文列表。
2. 纯 Prompt 收藏。
3. 无代码或几乎无实现的概念项目。
4. 无法运行且没有明显学习价值的仓库。
5. 纯资讯类内容。
6. 与 AI Agent 关系较弱的项目。

---

## 8. 收录等级

| 等级 | 名称 | 适用对象 | 输出要求 |
|---|---|---|---|
| Level A | 深度收录 | 核心重点项目 | 完整文档、源码拆解、图解、集成、排查、学习笔记、评价 |
| Level B | 标准收录 | 普通优秀项目 | 概览、快速开始、核心原理、基础图解、学习任务、简要评价 |
| Level C | 轻量收录 | 观察项目 | 项目简介、推荐理由、分类标签、后续分析建议 |
| Level D | 暂不收录 | 不符合要求项目 | 不收录原因、风险说明、替代项目建议 |

---

## 9. 项目生命周期状态

| 状态 | 含义 |
|---|---|
| candidate | 候选项目 |
| triaging | 正在评估 |
| accepted | 已通过收录评估 |
| analyzing | 正在分析 |
| documented | 文档已生成 |
| diagrammed | 图解已生成 |
| study-ready | 学习资料已就绪 |
| in-study | 正在学习 |
| completed | 学习完成 |
| archived | 归档或停止维护 |

---

## 10. 高质量图解要求

### 10.1 输出格式

建议同时保存源码图和导出图：

```text
assets/diagrams/
├── architecture.mmd
├── architecture.svg
├── architecture.png
├── sequence.mmd
├── sequence.svg
├── agent-loop.mmd
├── integration.mmd
└── troubleshooting.mmd
```

### 10.2 质量标准

- 每张图只表达一个核心主题。
- 图中模块名称与项目源码、文档或合理抽象一致。
- 箭头方向符合真实执行流程。
- 图中不出现无法验证的臆测内容。
- 图解与正文互相支撑，不互相矛盾。
- 同一项目图解风格保持一致。
- 支持 README、文档站和技术分享复用。

### 10.3 生成流程

1. 阅读 README、docs、examples。
2. 分析目录结构和关键模块。
3. 梳理核心调用链。
4. 生成 Mermaid / PlantUML 草稿。
5. 自检图中概念和箭头方向。
6. 导出 SVG / PNG。
7. 插入文档。
8. 在图下补充说明与依据。

---

## 11. AI Agent 自动收录流程

标准流程：

```text
用户粘贴 GitHub URL 并说“收录”
  -> 解析 URL
  -> 获取仓库元信息
  -> 阅读 README / docs / examples / source
  -> 判断是否与 AI Agent 相关
  -> 判断分类和收录等级
  -> 创建项目目录
  -> 生成项目分析文档
  -> 生成图解
  -> 生成 Learning Todo List
  -> 生成学习笔记模板
  -> 更新 PROJECTS.md / LEARNING_PROGRESS.md
  -> 输出收录报告
```

### 11.1 收录前置判断

AI Agent 需要判断：

- 是否与 AI Agent 相关。
- 是否有学习价值。
- 是否有足够源码或文档可分析。
- 是否可以运行或至少可静态分析。
- 是否重复收录。
- License 是否允许学习和引用。
- 是否应深度收录、标准收录、轻量收录或暂不收录。

---

## 12. 本地学习系统

### 12.1 学习笔记目录

```text
learning-notes/<project-name>/
├── README.md
├── 00-study-plan.md
├── 01-first-impression.md
├── 02-quickstart-notes.md
├── 03-architecture-notes.md
├── 04-source-reading-notes.md
├── 05-integration-notes.md
├── 06-troubleshooting-notes.md
├── 07-reflection.md
├── progress.json
└── review-questions.md
```

### 12.2 学习闭环

```text
生成学习计划 -> 执行学习任务 -> 记录学习笔记 -> Agent Review -> 生成复习问题 -> 更新下一步 -> 阶段总结
```

---

## 13. 非功能需求

| 类型 | 要求 |
|---|---|
| 可维护性 | 目录结构、模板和命名规则统一 |
| 可扩展性 | 可新增项目分类、模板、图解类型和 Agent 命令 |
| 可追溯性 | 关键结论要能追溯到源码、文档、运行结果或明确人工判断 |
| 本地优先 | 支持本地生成、编辑和沉淀 |
| 质量优先 | 少量高质量项目优先于大量低质量链接 |
| 可读性 | 初学者能读懂，工程师能落地，维护者能持续更新 |

---

## 14. MVP 版本

### 14.1 MVP 目标

验证“自动收录 + 文档生成 + 图解生成 + 学习任务 + 学习笔记模板”的闭环是否成立。

### 14.2 MVP 必须支持

1. 输入 GitHub 地址并执行收录。
2. 自动生成项目目录。
3. 自动生成标准文档骨架。
4. 自动生成至少 3 张基础图：架构图、核心流程图、时序图或学习路线图。
5. 自动生成 Learning Todo List。
6. 自动生成学习笔记模板。
7. 自动更新项目索引。
8. 自动输出收录报告。

### 14.3 MVP 暂不强求

- 所有项目都完成源码逐行分析。
- 所有图都达到视觉精修级别。
- 自动完成完整生产化验证。
- 完整社区协作流程。
- 自动生成网站。

---

## 15. 阶段规划

| 阶段 | 目标 | 主要产出 |
|---|---|---|
| 阶段 1 | 个人知识库期 | 模板、首批项目、基础路线 |
| 阶段 2 | 半自动化沉淀期 | 自动收录、图解生成、学习笔记 |
| 阶段 3 | 开源化期 | README、贡献指南、项目索引、社区协作 |
| 阶段 4 | 学习监督系统期 | 进度检查、笔记 Review、复习问题 |
| 阶段 5 | 知识体系平台期 | 方法论、选型指南、生产检查清单 |

---

## 16. 风险与应对

| 风险 | 说明 | 应对 |
|---|---|---|
| 范围过大 | 想收录所有项目容易失控 | MVP 只做 3 到 5 个样例 |
| 内容过期 | AI Agent 项目更新很快 | 标注日期、版本、commit、状态 |
| 质量不稳定 | AI 自动生成可能出现幻觉 | 质量门禁 + 人工复核 |
| 图解失真 | 图可能与源码不一致 | 图下标注依据与推测边界 |
| 链接堆积 | 项目退化为 Awesome List | 强制项目精读、评价、学习任务 |
| 学习监督形式化 | 只打勾不理解 | Review 问题、理解检查、反思总结 |

---

## 17. 成功标准

### 17.1 个人成功标准

- 能系统理解 AI Agent 主流项目。
- 能跑通、集成、排查和评价项目。
- 能补齐 AI Agent 相关知识短板。
- 能沉淀可复用学习资产。

### 17.2 项目成功标准

- README 清晰。
- 目录结构稳定。
- 模板可复用。
- 有高质量项目分析样例。
- 有图解、有学习任务、有进度记录。
- 能持续维护。

### 17.3 社区成功标准

- 他人能使用项目完成学习。
- 他人能贡献项目分析。
- 他人能基于模板补充内容。
- 项目能帮助开发者少走弯路。

---

## 18. 一句话定义

这是一个由 AI Agent 辅助驱动的 AI Agent 开源项目精读与学习系统：用户通过粘贴 GitHub 项目地址即可发起收录，系统自动生成项目分析、图解、学习路线、学习笔记模板与进度跟踪能力，帮助开发者从“会用”走向“懂原理、能集成、会排查、可沉淀”。


---

# 仓库目录设计、文档模板与收录流程规范

## 1. 仓库设计目标

仓库设计必须支持四个核心目标：

1. **项目精读**：每个项目都有结构统一的分析文档。
2. **图解沉淀**：每个项目都有可维护的图解源码和导出图。
3. **学习闭环**：每个项目都有 Learning Todo List 和本地学习笔记。
4. **AI Agent 友好**：用户可以通过“收录 GitHub 地址”触发标准流程，AI Agent 能根据约定生成内容。

---

## 2. 推荐仓库结构

```text
ai-agent-project-deep-dive/
├── README.md
├── ROADMAP.md
├── PROJECTS.md
├── LEARNING_PROGRESS.md
├── CONTRIBUTING.md
├── LICENSE
├── .agent/
│   ├── commands/
│   ├── prompts/
│   ├── workflows/
│   └── quality-gates/
├── templates/
│   ├── project-analysis-template.md
│   ├── quickstart-template.md
│   ├── architecture-template.md
│   ├── source-code-reading-template.md
│   ├── core-principles-template.md
│   ├── integration-guide-template.md
│   ├── troubleshooting-template.md
│   ├── evaluation-template.md
│   ├── learning-todo-template.md
│   ├── learning-notes-template.md
│   ├── collect-report-template.md
│   └── diagram-guidelines.md
├── knowledge/
│   ├── agent-loop.md
│   ├── tool-calling.md
│   ├── rag.md
│   ├── memory.md
│   ├── context-engineering.md
│   ├── mcp.md
│   ├── multi-agent.md
│   ├── workflow.md
│   ├── evaluation.md
│   ├── observability.md
│   ├── security.md
│   └── production-readiness.md
├── learning-roadmap/
│   ├── README.md
│   ├── stage-00-basics.md
│   ├── stage-01-agent-loop.md
│   ├── stage-02-tool-calling.md
│   ├── stage-03-rag.md
│   ├── stage-04-memory-context.md
│   ├── stage-05-workflow-agent.md
│   ├── stage-06-multi-agent.md
│   ├── stage-07-mcp.md
│   ├── stage-08-evaluation.md
│   ├── stage-09-agentic-coding.md
│   └── stage-10-production-agent.md
├── projects/
│   ├── agent-frameworks/
│   ├── agentic-coding/
│   ├── rag-agents/
│   ├── mcp-tools/
│   ├── multi-agent/
│   ├── evaluation-observability/
│   └── product-agents/
├── learning-notes/
├── comparisons/
│   ├── README.md
│   ├── agent-frameworks-comparison.md
│   ├── coding-agents-comparison.md
│   ├── rag-agent-comparison.md
│   └── mcp-ecosystem-comparison.md
├── examples/
│   ├── minimal-agent/
│   ├── tool-calling-demo/
│   ├── rag-agent-demo/
│   ├── mcp-demo/
│   └── java-integration-demo/
└── assets/
    ├── diagrams/
    └── images/
```

---

## 3. 单项目目录规范

```text
projects/<category>/<project-name>/
├── README.md
├── meta.json
├── 01-overview.md
├── 02-quickstart.md
├── 03-architecture.md
├── 04-source-code-reading.md
├── 05-core-principles.md
├── 06-integration-guide.md
├── 07-troubleshooting.md
├── 08-evaluation.md
├── 09-learning-todo-list.md
├── 10-summary.md
├── collect-report.md
└── assets/
    ├── diagrams/
    │   ├── architecture.mmd
    │   ├── architecture.svg
    │   ├── architecture.png
    │   ├── flow.mmd
    │   ├── flow.svg
    │   ├── sequence.mmd
    │   ├── sequence.svg
    │   ├── integration.mmd
    │   └── troubleshooting.mmd
    └── screenshots/
```

---

## 4. 学习笔记目录规范

```text
learning-notes/<project-name>/
├── README.md
├── 00-study-plan.md
├── 01-first-impression.md
├── 02-quickstart-notes.md
├── 03-architecture-notes.md
├── 04-source-reading-notes.md
├── 05-integration-notes.md
├── 06-troubleshooting-notes.md
├── 07-reflection.md
├── progress.json
└── review-questions.md
```

---

## 5. meta.json 元数据规范

```json
{
  "name": "example-agent",
  "github_url": "https://github.com/example/example-agent",
  "category": "agent-frameworks",
  "collect_level": "A",
  "status": "study-ready",
  "license": "MIT",
  "primary_language": "Python",
  "stars_at_collect": 12000,
  "forks_at_collect": 1500,
  "collected_at": "2026-06-10",
  "analyzed_commit": "unknown",
  "verified_run": false,
  "source_reading_status": "partial",
  "diagram_status": "generated",
  "learning_notes_status": "created",
  "tags": ["agent-loop", "tool-calling", "rag"],
  "suitable_for": ["learning", "prototype", "integration-reference"],
  "not_suitable_for": ["unreviewed-high-risk-automation"],
  "maintainer_notes": "First pass generated by AI Agent, requires human verification."
}
```

---

## 6. PROJECTS.md 索引规范

```markdown
# Projects Index

| Project | Category | Level | Status | Run Verified | Source Reading | Diagrams | Learning Notes | Last Updated |
|---|---|---|---|---|---|---|---|---|
| example-agent | agent-frameworks | A | study-ready | No | Partial | Yes | Yes | 2026-06-10 |
```

---

## 7. LEARNING_PROGRESS.md 规范

```markdown
# Learning Progress

## 正在学习

| Project | Current Stage | Completed | Blockers | Next Action |
|---|---|---:|---|---|
| example-agent | source-reading | 12/38 | Tool registry 未完全理解 | 阅读 executor 模块 |

## 已完成

| Project | Completed At | Summary |
|---|---|---|
| - | - | - |

## 待复习

- [ ] 复习 Agent Loop 与 Tool Calling 差异
- [ ] 对比 example-agent 与同类框架
```

---

## 8. AI Agent 命令约定

### 8.1 /collect

```text
/collect https://github.com/example/example-agent
```

作用：启动标准收录流水线。

### 8.2 /analyze-project

```text
/analyze-project projects/agent-frameworks/example-agent
```

作用：重新分析或补全文档。

### 8.3 /generate-diagrams

```text
/generate-diagrams projects/agent-frameworks/example-agent
```

作用：生成或更新架构图、流程图、时序图、集成图。

### 8.4 /generate-learning-plan

```text
/generate-learning-plan projects/agent-frameworks/example-agent
```

作用：生成 Learning Todo List、学习笔记模板和 review questions。

### 8.5 /check-progress

```text
/check-progress learning-notes/example-agent
```

作用：检查学习进度、识别卡点、给出下一步建议。

### 8.6 /review-notes

```text
/review-notes learning-notes/example-agent
```

作用：检查学习笔记质量，修正错误理解，补充待验证内容。

---

## 9. /collect 标准流程规范

### 9.1 输入

```text
收录：https://github.com/<owner>/<repo>
```

### 9.2 流程

1. 解析 GitHub URL。
2. 获取项目元信息。
3. 检查是否已收录。
4. 阅读 README、docs、examples。
5. 分析目录结构。
6. 判断是否与 AI Agent 相关。
7. 判断项目分类。
8. 判断收录等级。
9. 创建项目目录。
10. 创建 learning-notes 目录。
11. 生成 meta.json。
12. 生成项目文档。
13. 生成图解源码和导出图。
14. 生成 Learning Todo List。
15. 生成学习笔记模板。
16. 更新 PROJECTS.md。
17. 更新 LEARNING_PROGRESS.md。
18. 输出 collect-report.md。

### 9.3 输出

- `projects/<category>/<project-name>/`
- `learning-notes/<project-name>/`
- `PROJECTS.md` 更新
- `LEARNING_PROGRESS.md` 更新
- 收录报告

---

## 10. 收录评估 Checklist

```markdown
# 收录评估 Checklist

- [ ] 项目与 AI Agent 明确相关
- [ ] 有 README 或官方文档
- [ ] 有可分析源码
- [ ] 有 examples 或使用说明
- [ ] License 可接受
- [ ] 非重复收录
- [ ] 有学习价值
- [ ] 有工程参考价值
- [ ] 可生成 Learning Todo List
- [ ] 可生成至少一张有效图解
```

---

## 11. 项目分析模板

```markdown
# <Project Name> 项目精读

## 1. 项目基本信息

- GitHub：
- 官方文档：
- 分类：
- 收录等级：
- 主要语言：
- License：
- 分析日期：
- 分析版本 / Commit：
- 是否运行验证：

## 2. 一句话定位

用一句话说明这个项目解决什么问题。

## 3. 适合谁学习

- 初学者：
- 工程师：
- 研究者：
- 企业落地：

## 4. 项目解决的问题

说明项目面对的痛点、核心场景和价值。

## 5. 项目主线

描述从用户输入到最终输出的完整主流程。

## 6. 架构拆解

说明核心模块、模块职责和模块关系。

## 7. 核心原理

解释 Agent Loop、Tool Calling、Memory、RAG、MCP 等相关机制。

## 8. 源码阅读路线

说明推荐阅读顺序、关键文件和关键调用链。

## 9. 集成指南

说明如何接入自己的项目，包括 API、SDK、CLI、服务化、权限和日志。

## 10. 问题排查

列出安装、配置、模型调用、工具调用、上下文、权限、网络等问题。

## 11. 客观评价

### 优点

### 缺点

### 适用场景

### 不适用场景

## 12. Learning Todo List

分阶段学习任务。

## 13. 总结

写出这个项目最值得学习和借鉴的地方。
```

---

## 12. Learning Todo List 模板

```markdown
# <Project Name> Learning Todo List

## Level 1：了解项目

- [ ] 阅读 README
- [ ] 用一句话说明项目定位
- [ ] 说明项目解决的问题
- [ ] 判断项目适合什么场景

产出：一页项目初印象笔记。

## Level 2：跑通使用

- [ ] 安装依赖
- [ ] 配置 API Key / 模型
- [ ] 跑通最小 Demo
- [ ] 记录遇到的问题

产出：quickstart notes。

## Level 3：理解源码

- [ ] 找到入口文件
- [ ] 找到 Agent Loop
- [ ] 找到模型调用位置
- [ ] 找到工具注册逻辑
- [ ] 找到错误处理逻辑

产出：源码调用链图和阅读笔记。

## Level 4：完成集成

- [ ] 接入一个本地 Demo 项目
- [ ] 接入一个自定义工具
- [ ] 增加日志
- [ ] 记录集成问题

产出：integration notes。

## Level 5：二次改造

- [ ] 替换模型供应商
- [ ] 增加一个自定义 workflow
- [ ] 增加一个评测用例
- [ ] 优化上下文管理

产出：改造总结。

## Level 6：总结评价

- [ ] 写出项目优缺点
- [ ] 写出适用和不适用场景
- [ ] 与同类项目对比
- [ ] 总结可借鉴设计

产出：final reflection。
```

---

## 13. progress.json 模板

```json
{
  "project": "example-agent",
  "github": "https://github.com/example/example-agent",
  "status": "in-study",
  "current_stage": "source-reading",
  "completed_tasks": 12,
  "total_tasks": 38,
  "last_studied_at": "2026-06-10",
  "blocked_items": [
    "Tool registry implementation not fully understood"
  ],
  "next_actions": [
    "Read tool executor module",
    "Run custom tool demo",
    "Update architecture diagram"
  ],
  "review_questions_done": false,
  "final_summary_done": false
}
```

---

## 14. 图解规范模板

```markdown
# Diagram Guidelines

## 必须生成

- architecture.mmd
- flow.mmd
- sequence.mmd

## 可选生成

- integration.mmd
- troubleshooting.mmd
- agent-loop.mmd
- rag-flow.mmd
- mcp-tooling.mmd

## 图解要求

- 每张图只表达一个主题
- 模块命名与正文一致
- 箭头方向必须准确
- 推测内容必须标注
- 图下必须有解释说明
- 同一项目图解风格保持一致
```

---

## 15. 质量门禁

### 15.1 文档质量门禁

```markdown
- [ ] 是否说明项目定位
- [ ] 是否说明适用场景
- [ ] 是否说明不适用场景
- [ ] 是否包含快速开始
- [ ] 是否包含原理分析
- [ ] 是否包含源码阅读路线
- [ ] 是否包含集成指南
- [ ] 是否包含问题排查
- [ ] 是否包含客观评价
- [ ] 是否包含 Learning Todo List
```

### 15.2 图解质量门禁

```markdown
- [ ] 图是否有明确主题
- [ ] 模块名称是否准确
- [ ] 箭头方向是否合理
- [ ] 是否没有过度推测
- [ ] 是否与正文一致
- [ ] 是否可独立阅读
- [ ] 是否适合放入 README 或文档站
```

### 15.3 学习任务质量门禁

```markdown
- [ ] 是否从浅到深
- [ ] 每个任务是否可执行
- [ ] 每个阶段是否有产出
- [ ] 是否覆盖使用、源码、集成、总结
- [ ] 是否包含理解检查问题
```

---

## 16. 收录报告模板

```markdown
# <Project Name> 收录报告

## 1. 收录结论

- 收录等级：
- 分类：
- 状态：
- 是否推荐深度分析：

## 2. 收录理由

## 3. 项目风险

## 4. 已生成内容

- [ ] 项目目录
- [ ] 元数据
- [ ] 项目文档
- [ ] 图解
- [ ] Learning Todo List
- [ ] 学习笔记模板
- [ ] 索引更新

## 5. 待人工验证

## 6. 下一步建议
```

---

## 17. 推荐首批 MVP 项目类型

首批不建议追求数量，建议覆盖 3 到 5 类典型项目：

1. 一个通用 Agent 框架。
2. 一个 Agentic Coding 工具。
3. 一个 RAG / Knowledge Agent。
4. 一个 MCP / Tool 项目。
5. 一个 Evaluation / Observability 项目。

每类选择 1 个项目完成深度收录，用于验证模板和流程。

---

## 18. 最小可执行版本交付清单

```markdown
- [ ] README.md
- [ ] ROADMAP.md
- [ ] PROJECTS.md
- [ ] LEARNING_PROGRESS.md
- [ ] templates/ 全部基础模板
- [ ] learning-roadmap/ 初始路线
- [ ] projects/ 分类目录
- [ ] learning-notes/ 示例目录
- [ ] assets/diagrams/ 示例图
- [ ] 一个 Level A 收录样例
- [ ] 一个 /collect 流程说明
```

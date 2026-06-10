# AgentDive 项目收录使用说明

本文档说明如何使用 AgentDive 收录一个 AI Agent 开源项目，并以 `NousResearch/hermes-agent` 作为示例。本文档是操作说明，不代表示例项目已经被正式收录；正式收录仍需要按质量门禁生成项目资料、更新索引并记录验证边界。

## 适用范围

当用户输入以下指令时，进入项目收录流程：

```text
收录：https://github.com/<owner>/<repo>
```

收录目标是把一个项目整理成可学习、可拆解、可复盘的资料包，而不是只保存链接或复述 README。

## 执行边界

当前仓库处于骨架和规范阶段，没有实现真实自动化收录程序。收录应由人工或 AI Agent 辅助执行，并遵守以下边界：

- 不修改 `docs/` 原始资料。
- 不生成虚假的运行结果。
- 不把未验证结论写成事实。
- 不写入账号、密钥、token、本机绝对路径或私有配置。
- 单次收录只写入当前项目目录、对应学习笔记目录、`PROJECTS.md` 和 `LEARNING_PROGRESS.md`。

## 标准流程

1. 解析 GitHub URL，确认 `owner`、`repo` 和默认分支。
2. 获取项目基本信息，包括 README、License、主要语言、文档入口和源码结构。
3. 判断项目是否与 AI Agent 明确相关。
4. 判断收录分类和收录等级。
5. 检查是否已经重复收录。
6. 创建项目资料目录。
7. 生成项目精读文档。
8. 生成图解源文件和导出图。
9. 生成 Learning Todo List。
10. 创建学习笔记目录。
11. 更新 `PROJECTS.md`。
12. 更新 `LEARNING_PROGRESS.md`。
13. 输出收录报告。

## 目录命名

项目目录 ID 统一使用 GitHub 来源生成的 `owner__repo`。

```text
projects/<category>/<owner__repo>/
learning-notes/<owner__repo>/
```

示例：

```text
projects/product-agents/NousResearch__hermes-agent/
learning-notes/NousResearch__hermes-agent/
```

## 分类选择

优先从以下分类中选择一个主分类：

| 分类 | 适用对象 |
|---|---|
| `agent-frameworks` | 通用 Agent 框架 |
| `agentic-coding` | AI 编码 Agent 和开发辅助工具 |
| `rag-agents` | RAG / Knowledge Agent |
| `mcp-tools` | MCP 工具、服务和生态项目 |
| `multi-agent` | 多 Agent 协作框架和实践 |
| `evaluation-observability` | 评测、监控、追踪和可观测性 |
| `product-agents` | 产品级 Agent 应用 |

如果项目横跨多个方向，只选择一个主分类，并在项目文档中补充辅助标签。

## 收录等级

| 等级 | 名称 | 适用对象 | 输出要求 |
|---|---|---|---|
| Level A | 深度收录 | 核心重点项目 | 完整文档、源码拆解、图解、集成、排查、学习笔记、评价 |
| Level B | 标准收录 | 普通优秀项目 | 概览、快速开始、核心原理、基础图解、学习任务、简要评价 |
| Level C | 轻量收录 | 观察项目 | 项目简介、推荐理由、分类标签、后续分析建议 |
| Level D | 暂不收录 | 不符合要求项目 | 不收录原因、风险说明、替代项目建议 |

等级判断应以学习价值、工程参考价值、文档和源码可分析性为依据，不以 Star 数作为主要依据。

## 必须生成的内容

Level A 或 Level B 收录建议生成：

```text
projects/<category>/<owner__repo>/README.md
projects/<category>/<owner__repo>/project-analysis.md
projects/<category>/<owner__repo>/source-code-reading.md
projects/<category>/<owner__repo>/integration-guide.md
projects/<category>/<owner__repo>/troubleshooting.md
projects/<category>/<owner__repo>/learning-todo-list.md
projects/<category>/<owner__repo>/collect-report.md
projects/<category>/<owner__repo>/assets/diagrams/
learning-notes/<owner__repo>/README.md
```

## 项目精读写法

`project-analysis.md` 应回答工程问题，而不是复述 README。至少覆盖：

- 项目一句话定位。
- 项目解决的问题和目标用户。
- 用户输入到最终输出的主流程。
- Agent Loop、Tool Calling、Memory、RAG、MCP、Multi-Agent、Evaluation 等相关机制。
- 入口文件、核心包、配置位置、示例代码、测试目录和文档目录。
- 1 到 3 条关键调用链。
- 快速开始和运行验证边界。
- 集成方式和问题排查。
- 优点、缺点、适用场景和不适用场景。

每个结论应标注依据：

```text
README / 官方文档 / 源码文件 / 运行结果 / 人工判断
```

## 图解要求

图解源文件使用 Mermaid，放在项目目录的 `assets/diagrams/` 下。每张图只表达一个主题，并说明依据。

常见图解：

```text
architecture.mmd
agent-loop.mmd
tool-calling-flow.mmd
memory-flow.mmd
integration-flow.mmd
troubleshooting-flow.mmd
```

未源码验证的箭头必须标注为 README 依据、文档依据或待验证推断。

## Learning Todo List 写法

Learning Todo List 应从浅到深组织，避免只列阅读任务。

建议层级：

1. 了解项目：阅读 README、官方文档和项目定位。
2. 跑通使用：安装依赖、配置模型、运行最小示例。
3. 理解源码：找到入口、Agent Loop、模型调用、工具注册和错误处理。
4. 完成集成：接入一个本地 Demo、自定义工具或业务服务。
5. 二次改造：替换模型、增加 workflow、增加评测或优化上下文管理。
6. 总结评价：写出优缺点、适用场景、不适用场景和可借鉴设计。

## PROJECTS.md 更新规则

只有在实际生成对应资料后，才能把状态推进到 `documented`、`diagrammed` 或 `study-ready`。

候选评估阶段示例：

```markdown
| Hermes Agent | https://github.com/NousResearch/hermes-agent | product-agents | Level A | accepted | 否 | 否 | 否 | 否 | 2026-06-10 |
```

开始分析但尚未完成源码验证时示例：

```markdown
| Hermes Agent | https://github.com/NousResearch/hermes-agent | product-agents | Level A | analyzing | 否 | 部分 | 部分 | 是 | 2026-06-10 |
```

不要把未完成事项提前标为 `是`。

## LEARNING_PROGRESS.md 更新规则

`LEARNING_PROGRESS.md` 只记录全局学习总览，不承载完整项目精读内容。

可以记录：

- 当前正在学习的项目。
- 当前阶段和完成进度。
- 卡住的问题。
- 下一步行动。

完整分析、问题排查和学习笔记应放到项目目录或 `learning-notes/<owner__repo>/`。

## Hermes Agent 示例

示例指令：

```text
收录：https://github.com/NousResearch/hermes-agent
```

### 信息快照

快照日期：2026-06-10。

来源：

- GitHub 仓库：https://github.com/NousResearch/hermes-agent
- GitHub API：https://api.github.com/repos/NousResearch/hermes-agent
- README：https://raw.githubusercontent.com/NousResearch/hermes-agent/main/README.md

### 基本信息

| 字段 | 值 |
|---|---|
| 项目名称 | Hermes Agent |
| GitHub 地址 | https://github.com/NousResearch/hermes-agent |
| 项目 ID | `NousResearch__hermes-agent` |
| 项目描述 | The agent that grows with you |
| 默认分支 | `main` |
| 主要语言 | Python |
| License | MIT |
| 官网 | https://hermes-agent.nousresearch.com |

### 初步定位

Hermes Agent 是 Nous Research 构建的产品级 AI Agent。根据 README，它强调 self-improving agent、learning loop、skills、跨会话记忆、工具调用、消息网关、调度任务、子 Agent 并行、MCP 集成和多种运行后端。

这只是基于 README 和 GitHub 元数据的初步定位；正式收录时仍需通过源码和运行验证确认关键实现。

### 建议分类

主分类：

```text
product-agents
```

辅助标签：

```text
agent-frameworks
agentic-coding
mcp-tools
memory-context
tool-calling
```

理由：Hermes Agent 不是单纯 SDK，也不是只服务编码场景的工具。它更像产品级个人或云端 Agent，同时包含框架化能力。

### 建议收录等级

```text
Level A：深度收录
```

理由：

- 与 AI Agent 明确相关。
- 有 README、官网文档和源码。
- 能拆解 CLI、gateway、tools、skills、memory、MCP、cron、terminal backends 等多个工程模块。
- 适合生成架构图、工具调用图、记忆系统图、运行后端图和集成流程图。
- 范围较大，需要源码级验证，适合深度收录而不是轻量记录。

### 前置判断示例

| 检查项 | 结论 | 依据 |
|---|---|---|
| 是否与 AI Agent 明确相关 | 是 | README 明确描述为 AI agent |
| 是否有 README 或官方文档 | 是 | 仓库 README 和官网文档入口 |
| 是否有可分析源码 | 是 | GitHub 仓库公开且包含源码目录 |
| 是否有 examples、docs 或使用说明 | 是 | README 提供安装、CLI、gateway、文档入口 |
| License 是否允许学习整理和引用 | 初步可接受 | GitHub API 显示 MIT License |
| 是否已经重复收录 | 待检查 | 需要检查 `PROJECTS.md` |
| 是否具备学习价值 | 是 | learning loop、skills、memory、tools、MCP 等主题 |
| 是否具备工程参考价值 | 是 | CLI、gateway、运行后端、工具系统等工程模块 |
| 是否可以生成 Learning Todo List | 是 | 可按使用、源码、集成、改造分层 |
| 是否可以生成有效图解 | 是 | 可拆出多张流程和架构图 |

### 建议生成文件

```text
projects/product-agents/NousResearch__hermes-agent/README.md
projects/product-agents/NousResearch__hermes-agent/project-analysis.md
projects/product-agents/NousResearch__hermes-agent/source-code-reading.md
projects/product-agents/NousResearch__hermes-agent/integration-guide.md
projects/product-agents/NousResearch__hermes-agent/troubleshooting.md
projects/product-agents/NousResearch__hermes-agent/learning-todo-list.md
projects/product-agents/NousResearch__hermes-agent/collect-report.md
projects/product-agents/NousResearch__hermes-agent/assets/diagrams/
learning-notes/NousResearch__hermes-agent/README.md
```

### Hermes 项目精读问题

正式生成 `project-analysis.md` 时，至少回答：

1. Hermes Agent 是 CLI Agent、个人助理、Agent 平台，还是编码 Agent？
2. 主 Agent Loop 在哪里？
3. 模型 provider 如何抽象？如何切换 provider？
4. tools 和 toolsets 如何注册、启用、禁用和执行？
5. skills 如何创建、存储、调用和自我改进？
6. memory 如何持久化？跨会话检索如何工作？
7. gateway 如何连接 Telegram、Discord、Slack 等平台？
8. cron 调度如何触发任务？
9. MCP 接入边界在哪里？
10. local、Docker、SSH、Modal、Daytona 等 backend 如何抽象？
11. 命令执行、密钥、远程环境和消息平台身份有哪些安全边界？
12. 哪些结论来自 README，哪些来自源码，哪些来自运行验证？

### Hermes 图解建议

优先生成：

```text
architecture.mmd
agent-loop.mmd
tool-and-skill-flow.mmd
memory-and-session-flow.mmd
gateway-flow.mmd
terminal-backend-flow.mmd
mcp-integration-flow.mmd
cron-scheduling-flow.mmd
```

图解必须标注依据。示例：

```text
依据：README 描述，待源码验证。
依据：源码文件 <path>，函数 <qualified_name>。
依据：运行命令 <command> 输出。
```

### Hermes Learning Todo List 示例

#### Level 1：了解项目

- [ ] 阅读 README 和官方文档首页。
- [ ] 用一句话说明 Hermes Agent 的定位。
- [ ] 区分 CLI、gateway、skills、memory、tools、MCP、cron 的职责。
- [ ] 记录项目适合学习的主题。

#### Level 2：跑通使用

- [ ] 按官方说明安装 Hermes。
- [ ] 执行 `hermes doctor`。
- [ ] 执行 `hermes model` 选择 provider。
- [ ] 执行 `hermes tools` 查看工具配置。
- [ ] 记录安装和模型配置问题。

#### Level 3：理解源码

- [ ] 找到 CLI 入口。
- [ ] 找到 Agent Loop。
- [ ] 找到模型 provider 抽象。
- [ ] 找到 toolset 注册和执行路径。
- [ ] 找到 skills 和 memory 的持久化逻辑。

#### Level 4：完成集成

- [ ] 配置一个最小 provider。
- [ ] 启用一个安全的只读工具。
- [ ] 连接一个 MCP server。
- [ ] 尝试 gateway 或 cron 的最小配置。

#### Level 5：二次改造

- [ ] 增加一个自定义 skill。
- [ ] 增加一个只读工具。
- [ ] 记录日志、权限和错误处理边界。
- [ ] 补一条最小评测或回归检查。

#### Level 6：总结评价

- [ ] 写出 Hermes Agent 的优势和限制。
- [ ] 写出适用场景和不适用场景。
- [ ] 与其他 Agent 产品或框架对比。
- [ ] 总结可借鉴的工程设计。

### Hermes 收录报告示例

```text
收录结论：建议收录。
收录等级：Level A 深度收录。
分类：product-agents。
项目 ID：NousResearch__hermes-agent。

已验证内容：
- GitHub 仓库存在且为公开仓库。
- README 显示项目为 Hermes Agent。
- GitHub API 显示主要语言为 Python，License 为 MIT，默认分支为 main。
- README 描述了 CLI、gateway、tools、skills、memory、MCP、cron 和多运行后端等能力。

未验证内容：
- 未运行安装命令。
- 未验证 `hermes` CLI 是否能在本机启动。
- 未验证 Agent Loop、memory、skills、gateway 的源码调用链。
- 未验证所有 provider、工具和消息平台集成。

主要风险：
- 项目能力范围大，分析容易停留在 README 复述。
- 安装和运行涉及模型 provider、API key、工具权限和远程 backend，需要严格记录验证边界。
- 自动化、命令执行和远程环境能力涉及安全风险，必须单独分析权限模型。
```

## 完成标准

一次收录完成前，至少通过以下检查：

- `PROJECTS.md` 的项目状态与实际文件一致。
- `LEARNING_PROGRESS.md` 只记录总览。
- 项目目录包含收录报告和学习任务。
- 图解与正文一致，推测内容已标注。
- 未运行的命令没有写成已跑通。
- 未源码验证的调用链没有写成事实。
- 不包含密钥、账号、本机绝对路径或私有配置。


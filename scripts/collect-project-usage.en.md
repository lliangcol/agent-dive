# AgentDive project collect usage instructions

This document explains how to use AgentDive to collect an AI Agent open source project, using `NousResearch/hermes-agent` as an example. This document is an operation instruction and does not mean that the sample project has been officially collected; formal collection still requires generating project information according to quality gates, updating indexes, and recording verification boundaries.

## Scope of application

When the user enters the following command, the project collect process is entered:

```text
收录：https://github.com/<owner>/<repo>
```

The goal of collect is to organize a project into a data package that can be learned, disassembled, and replayed, rather than just saving links or reciting README.

## Execution boundaries

The current warehouse is in the skeleton and specification stage, and no real automated collection program has been implemented. collect should be executed manually or with the assistance of an AI agent and adhere to the following boundaries:

- Do not modify `docs/` original information.
- Does not generate spurious running results.
- Do not write unverified conclusions as facts.
- Do not write accounts, keys, tokens, local absolute paths or private configurations.
- A single collect only writes to the current project directory, the corresponding learning notes directory, `PROJECTS.md` and `LEARNING_PROGRESS.md`.

## Standard process

1. Parse the GitHub URL and confirm `owner`, `repo` and the default branch.
2. Obtain basic project information, including README, License, main language, document entry and source code structure.
3. Determine whether the project is clearly related to the AI ​​Agent.
4. Determine the collect classification and collect level.
5. Check whether collect has been repeated.
6. Create a project data directory.
7. Generate project deep dive documents.
8. Generate diagrams source files and export diagrams.
9. Generate Learning Todo List.
10. Create the learning notes directory.
11. Update `PROJECTS.md`.
12. Update `LEARNING_PROGRESS.md`.
13. Output the collect report.

## Directory naming

The project directory ID uses `owner__repo` generated from the GitHub source.

```text
projects/<category>/<owner__repo>/
learning-notes/<owner__repo>/
```

Example:

```text
projects/product-agents/NousResearch__hermes-agent/
learning-notes/NousResearch__hermes-agent/
```

## Category selection

Prioritize selecting a main category from the following categories:

| Classification | Applicable objects |
|---|---|
| `agent-frameworks` | Common Agent Framework |
| `agentic-coding` | AI coding agents and development aids |
| `rag-agents` | RAG / Knowledge Agent |
| `mcp-tools` | MCP tools, services and ecological projects |
| `multi-agent` | Multi-Agent collaboration framework and practices |
| `evaluation-observability` | Measurement, monitoring, tracking and observability |
| `product-agents` | Product-level Agent application |

If the project spans multiple directions, choose only one primary category and supplement the project documentation with auxiliary tags.

## collectlevel

| grade | name | Applicable objects | Output requirements |
|---|---|---|---|
| Level A | Depth collect | core key projects | Complete documentation, source code disassembly, diagrams, integration, troubleshooting, learning notes, evaluation |
| Level B | Standard collect | Ordinary outstanding projects | Overview, quick start, core principles, basic diagrams, learning tasks, brief evaluation |
| Level C | Lightweight collect | Observation items | Project introduction, recommendation reasons, classification tags, follow-up analysis suggestions |
| Level D | Not collecting yet | Items that do not meet the requirements | Reasons for not collecting, risk description, alternative project suggestions |

Level judgment should be based on learning value, engineering reference value, documentation and source code analyzability, and not on the number of stars as the main basis.

## Content that must be generated

Level A or Level B collect recommendations generate:

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

## project deep dive writing method

`project-analysis.md` Answer engineering questions, not recite the README. Cover at least:

- Position the project in one sentence.
- The problem the project solves and the target users.
- The main flow from user input to final output.
- Agent Loop, Tool Calling, Memory, RAG, MCP, Multi-Agent, Evaluation and other related mechanisms.
- Entry file, core package, configuration location, sample code, test directory and documentation directory.
- 1 to 3 critical call chains.
- Quickly get up and running with validation boundaries.
- Integration methods and problemshooting.
- Advantages, disadvantages, applicable scenarios and not applicable scenarios.

Each conclusion should be labeled with the basis for:

```text
README / 官方文档 / 源码文件 / 运行结果 / 人工判断
```

## diagrams requirements

The diagrams source file uses Mermaid and is placed under `assets/diagrams/` in the project directory. Each picture only expresses one theme and explains the basis.

Common diagrams:

```text
architecture.mmd
agent-loop.mmd
tool-calling-flow.mmd
memory-flow.mmd
integration-flow.mmd
troubleshooting-flow.mmd
```

Arrows that have not been verified by source code must be marked as README basis, document basis or inference to be verified.

## How to write Learning Todo List

The Learning Todo List should be organized from shallow to deep and avoid listing only reading tasks.

Recommended level:

1. Understand the project: read the README, official documentation and project positioning.
2. Run-through usage: install dependencies, configure models, and run minimal examples.
3. Understand the source code: find the entrance, Agent Loop, model calling, tool registration and error handling.
4. Complete integration: connect to a local demo, custom tool or business service.
5. Second transformation: replace the model, add workflow, add evaluation or optimize context management.
6. Summary and evaluation: write down the advantages and disadvantages, applicable scenarios, not applicable scenarios and design references.

## PROJECTS.md update rules

Only after the corresponding data is actually generated can the status be advanced to `documented`, `diagrammed` or `study-ready`.

Example of candidate evaluation stage:

```markdown
| Hermes Agent | https://github.com/NousResearch/hermes-agent | product-agents | Level A | accepted | 否 | 否 | 否 | 否 | 2026-06-10 |
```

Example when analysis starts but source code verification has not been completed:

```markdown
| Hermes Agent | https://github.com/NousResearch/hermes-agent | product-agents | Level A | analyzing | 否 | 部分 | 部分 | 是 | 2026-06-10 |
```

Don’t mark unfinished items as `是` in advance.

## LEARNING_PROGRESS.md Update rules

`LEARNING_PROGRESS.md` Only records the global learning overview and does not carry the complete project deep dive content.

Can record:

- The project you are currently studying.
- Current stage and completion progress.
- Stuck problem.
- Next steps.

Complete analysis, troubleshooting and learning notes should be placed in the project directory or `learning-notes/<owner__repo>/`.

## Hermes Agent Example

Example instructions:

```text
收录：https://github.com/NousResearch/hermes-agent
```

### Information Snapshot

Snapshot date: 2026-06-10.

source:

- GitHub repository: https://github.com/NousResearch/hermes-agent
- GitHub API：https://api.github.com/repos/NousResearch/hermes-agent
- README：https://raw.githubusercontent.com/NousResearch/hermes-agent/main/README.md

### Basic information

| Field | value |
|---|---|
| Project name | Hermes Agent |
| GitHub address | https://github.com/NousResearch/hermes-agent |
| Project ID | `NousResearch__hermes-agent` |
| Project description | The agent that grows with you |
| Default branch | `main` |
| main language | Python |
| License | MIT |
| Official website | https://hermes-agent.nousresearch.com |

### Initial positioning

Hermes Agent is a production-level AI Agent built by Nous Research. According to the README, it emphasizes self-improving agents, learning loops, skills, cross-session memory, tool invocation, message gateways, scheduled tasks, sub-agent parallelism, MCP integration, and multiple runtime backends.

This is only a preliminary positioning based on README and GitHub metadata; key implementations still need to be confirmed through source code and runtime verification when collecting officially.

### Suggested categories

Main category:

```text
product-agents
```

Auxiliary tags:

```text
agent-frameworks
agentic-coding
mcp-tools
memory-context
tool-calling
```

Reason: Hermes Agent is not a pure SDK, nor is it a tool that only serves coding scenarios. It is more like a product-level personal or cloud agent, and also includes framework capabilities.

### Recommended collect level

```text
Level A：深度收录
```

reason:

- Explicitly related to AI Agent.
- There are README, official website documents and source code.
- Can disassemble multiple engineering modules such as CLI, gateway, tools, skills, memory, MCP, cron, terminal backends, etc.
- Suitable for generating architecture diagrams, tool call diagrams, memory system diagrams, operation backend diagrams and integration flow diagrams.
- The scope is large and requires source code level verification. It is suitable for deep collection rather than lightweight recording.

### Prejudgment example

| Check items | in conclusion | in accordance with |
|---|---|---|
| Is it explicitly related to the AI ​​Agent? | yes | README clearly describes AI agent |
| Is there a README or official documentation? | yes | Warehouse README and official website documentation entrance |
| Is there source code that can be analyzed? | yes | GitHub repository is public and contains source code directory |
| Are there examples, docs or usage instructions? | yes | README provides installation, CLI, gateway, and document entry |
| Does the License allow learning to organize and quote? | Preliminarily acceptable | GitHub API shows MIT License |
| Whether the collect has been repeated | To be checked | Need to check `PROJECTS.md` |
| Whether it has learning value | yes | Learning loop, skills, memory, tools, MCP and other topics |
| Whether it has engineering reference value | yes | CLI, gateway, running backend, tool system and other engineering modules |
| Is it possible to generate a Learning Todo List? | yes | Can be layered by use, source code, integration, transformation |
| Is it possible to generate valid diagrams? | yes | Multiple process and architecture diagrams can be detached |

### It is recommended to generate files

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

### Hermes project deep dive problem

When formally generating `project-analysis.md`, at least answer:

1. Is Hermes Agent a CLI Agent, a personal assistant, an Agent platform, or a coding Agent?
2. Where is the main Agent Loop?
3. How to abstract model provider? How to switch providers?
4. How are tools and toolsets registered, enabled, disabled and executed?
5. How are skills created, stored, recalled and self-improved?
6. How is memory persisted? How does cross-session retrieval work?
7. How does gateway connect to platforms such as Telegram, Discord, and Slack?
8. How does cron scheduling trigger tasks?
9. Where are the MCP access boundaries?
10. How to abstract local, Docker, SSH, Modal, Daytona and other backends?
11. What are the security boundaries around command execution, keys, remote environments, and messaging platform identities?
12. Which conclusions come from README, which come from source code, and which come from running verification?

### Hermes diagrams suggestions

Prioritize generation:

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

Diagrams must be labeled with the basis. Example:

```text
依据：README 描述，待源码验证。
依据：源码文件 <path>，函数 <qualified_name>。
依据：运行命令 <command> 输出。
```

### Hermes Learning Todo List Example

#### Level 1: Understand the project

- [ ] Read the README and official documentation homepage.
- [ ] Explain the positioning of Hermes Agent in one sentence.
- [ ] Distinguish the responsibilities of CLI, gateway, skills, memory, tools, MCP, and cron.
- [ ] Record the topics that the project is suitable for learning.

#### Level 2: Run through

- [ ] Install Hermes according to official instructions.
- [ ] Execute `hermes doctor`.
- [ ] Execute `hermes model` to select provider.
- [ ] Execute `hermes tools` to view tool configuration.
- [ ] Log installation and model configuration issues.

#### Level 3: Understand the source code

- [ ] Find the CLI entry.
- [ ] Find Agent Loop.
- [ ] Find the model provider abstraction.
- [ ] Find toolset registration and execution paths.
- [ ] Find persistence logic for skills and memory.

#### Level 4: Complete integration

- [ ] Configure a minimal provider.
- [ ] Enable a secure read-only tool.
- [ ] Connect to an MCP server.
- [ ] Try minimal configuration of gateway or cron.

#### Level 5: Second transformation

- [ ] Add a custom skill.
- [ ] Add a read-only tool.
- [ ] Logging, permissions and error handling boundaries.
- [ ] Add a minimal evaluation or regression check.

#### Level 6: Summary evaluation

- [ ] Write the advantages and limitations of Hermes Agent.
- [ ] Write applicable scenarios and not applicable scenarios.
- [ ] Comparison with other Agent products or frameworks.
- [ ] Summarize engineering design that can be used for reference.

### Hermes collect report example

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

## Completion criteria

Before a collect is completed, at least the following checks must be passed:

- `PROJECTS.md`'s project status is consistent with the actual file.
- `LEARNING_PROGRESS.md` Only logs an overview.
- The project directory contains collect reports and learning tasks.
- The diagrams are consistent with the text, and the inferred content has been marked.
- The not_run command is not written as run.
- The call chain without source code verification is not written as a fact.
- Does not include keys, accounts, local absolute paths or private configurations.

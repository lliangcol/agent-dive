# AI Agent open source project deep dive and learning system PRD / project approval document

**Project tentative name**: AI Agent Project Deep Dive
**Chinese name**: AI Agent open source project deep dive and learning system
**Document version**: V1.0
**Current stage**: Requirements discussion and project design, no implementation
**Target form**: AI Agent assisted maintenance of project deep dive, diagrams, learning supervision and engineering practice knowledge system

---

## 1. Verify and revise conclusions

Verification basis: After checking the GitHub page on 2026-06-10, it was confirmed that lliangcol/Agent-Learning-Hub is a public repository, and the page shows that it is forked from datawhalechina/Agent-Learning-Hub; the repository root directory contains learning-notes, README.md, index.html and other contents. The current positioning of README is to maintain a core display surface README, which is used to organize the AI Agent learning todo list. Therefore, this project should not describe the repository as having a complete automatic collection and learning supervision system, but should use it as a reference basis for learning routes and data organization methods.

This requirements document makes three revisions based on the above verification:

1. **Reference repository positioning correction**: The existing Agent-Learning-Hub is more suitable as a reference for learning routes, material organization, and Todo List, and should not be described as having a complete automated learning supervision system.
2. **Picture quality target correction**: High-quality diagrams first refer to accurate information, clear structure, consistent graphics and text, and reusability, rather than just pursuing visual gorgeousness.
3. **Automatic collect target correction**: After the user pastes the GitHub address and says "collect", the system should enter the standard collection pipeline; it cannot promise that all projects will unconditionally generate perfect final drafts, and there must be access assessment, collection level and quality gate control.

---

## 2. Project background

A large number of AI Agent-related open source projects have appeared on GitHub, including general Agent frameworks, Agentic Coding tools, RAG Agents, MCP tool ecosystem, multi-Agent collaboration frameworks, evaluation and observability tools, and product-level Agent applications. They have high learning value, but developers are prone to encounter the following problems when learning the system:

- I can only run the demo according to the README, but I don’t know how to integrate it into my own project.
- Only knows the project functions, but does not understand the implementation principles behind Agent Loop, Tool Calling, Memory, RAG, MCP, Evaluation, etc.
- It is easy to get lost when looking directly at the source code, and you do not know the main line of the project, module boundaries and key call chains.
- Only looking at high-star conclusions lacks objective evaluation, applicable scenarios and not applicable scenario judgments.
- The learning process lacks local notes, task breakdown, progress recording and review mechanisms.
- Data accumulation can easily turn into link stacking, making it difficult to form sustainable knowledge assets.

Therefore, it is necessary to create a systematic learning and deep dive project with excellent AI Agent open source projects as the entrance, so that learners can master AI Agent engineering capabilities through real projects.

---

## 3. Project positioning

### 3.1 This project is not

- Not just any Awesome List.
- Not just a link to favorites.
- Not just a summary of the README.
- This is not a tutorial repository that only talks about concepts.
- Not an AI Agent news aggregation.

### 3.2 This project is

> A developer-oriented AI Agent open source project deep dive, diagram generation, learning supervision and engineering practice knowledge system maintained by AI Agent.

Its core closed loop is:

```text
project collection -> Project breakdown -> Diagram generation -> Learning task generation -> Learning supervision -> Progress accumulation -> Knowledge base accumulation
```

---

## 4. Project goals

### 4.1 Overall Goal

Through systematic and deep dive of excellent AI Agent projects on GitHub, we can help developers achieve:

1. **Know how to use**: Able to install, configure, run, integrate and troubleshoot problems.
2. **Understand the principles**: Understand the project design ideas, core mechanisms, source code structure and key call chains.
3. **Knowledge Supplement**: Complete the AI Agent knowledge system around the project.
4. **With path**: Generate a Learning Todo List from shallow to deep by project.
5. **Ability to Precipitate**: Locally generate learning notes, progress records and stage summaries.
6. **Open Source**: Gradually develop into an open source learning project that can be maintained sustainably.

### 4.2 Key Results

- Complete at least 3 to 5 in-depth collection samples of representative projects.
- Establish unified project analysis templates, diagrams templates, learning tasks templates and collection processes.
- Supports "paste GitHub address + collect" to trigger the standard collection pipeline.
- Generate high-quality diagrams that can be used for README, documentation sites, and technology sharing.
- Supports local learning notes and AI Agent learning assistance.

---

## 5. User portrait

### 5.1 AI Agent Beginner
I hope to establish a knowledge system through real projects and know what to learn first, how to learn it, and what level of learning is considered complete.

### 5.2 Java / Backend Developer
Focus on how to integrate Agent capabilities into existing business systems, including permissions, security, logs, audits, databases, message queues, and internal enterprise APIs.

### 5.3 Front-end/full-stack developer
Pay attention to Agent API, Web UI, streaming response, task status display and productized interaction.

### 5.4 AI Agent Engineering Practitioner
Focus on source code implementation, context management, tool governance, measurement, observability, cost control and production availability.

### 5.5 Project maintainer/contributor
Pay attention to how to continuously project collections, maintain templates, improve diagrams, revise documentation, and organize community contributions.

---

## 6. Product core capabilities

### 6.1 Automatic collection of projects

The user enters into the AI Agent:

```text
Collect: https://github.com/example/example-agent
```

The system should execute the standard collection pipeline: parse URL, obtain repository information, judge classification, evaluate collection value, determine collection level, create directory, generate documents, generate diagrams, generate learning tasks, generate note templates, update index and output collection report.

### 6.2 Project deep dive document generation

Each project should generate deep dive documents with a unified structure, including overview, quick start, architecture breakdown, source reading, core principles, integration guide, troubleshooting, objective evaluation, learning tasks and summary.

### 6.3 High-quality diagrams generation

Each project is generated according to the actual situation:

- Global architecture diagram
- Core execution flow chart
- Timing diagram
- Module relationship diagram
- Schematic
- integration architecture diagram
- Problem troubleshooting location map
- Learning roadmap

Diagrams must have accurate information, clear hierarchy, consistent graphics and text, and be traceable. They can be used in README, documentation sites, technology sharing or public account articles.

### 6.4 Knowledge completion

Complete relevant knowledge around each project: Agent Loop, ReAct, Tool Calling, Memory, Context Engineering, RAG, MCP, Multi-Agent, Workflow, Evaluation, Observability, Security, Sandbox, Cost Control, Human-in-the-loop.

### 6.5 Learning Todo List

Each project automatically generates a list of learning tasks from shallow to deep: understanding the project, running through the usage, understanding the source code, completing integration, secondary transformation, and summary evaluation.

### 6.6 Local learning notes

Each project generates a local learning notes directory, including study plans, first impressions, quick start notes, architecture notes, source reading notes, integration notes, troubleshooting notes, review summary, progress files and review questions.

### 6.7 AI Agent Learning Supervision

The AI Agent is responsible for: generating learning plans, dismantling tasks, checking progress, discovering stuck points, generating understanding check questions, reviewing learning notes, and updating next step suggestions.

---

## 7. collect range and boundaries

### 7.1 Inclusion scope

1. Universal Agent framework.
2. Agentic Coding Tools.
3. RAG / Knowledge Agent.
4. MCP/Tool ecological project.
5. Multi-Agent project.
6. Evaluation / Observability project.
7. A product-level Agent project with complete engineering value.

### 7.2 Not included in the scope yet

1. Pure paper list.
2. Pure Prompt collection.
3. Concept projects with no code or almost no implementation.
4. A repository that cannot be run and has no obvious learning value.
5. Purely informational content.
6. Projects that have a weak relationship with AI Agent.

---

## 8. collection level

| grade | name | Applicable objects | Output requirements |
|---|---|---|---|
| Level A | In-depth collection | Core focus projects | Complete documentation, source code breakdown, diagrams, integration, troubleshooting, learning notes, evaluation |
| Level B | Standard collection | Strong general projects | Overview, quick start, core principles, basic diagrams, learning tasks, brief evaluation |
| Level C | Lightweight collection | Projects to watch | Project introduction, recommendation reasons, classification tags, follow-up analysis suggestions |
| Level D | Not collecting yet | Projects that do not meet the requirements | Reasons for not collecting, risk description, alternative project suggestions |

---

## 9. Project life cycle status

| state | meaning |
|---|---|
| candidate | Candidate projects |
| triaging | Evaluating |
| accepted | Passed collection evaluation |
| analyzing | Analyzing |
| documented | Document has been generated |
| diagrammed | diagrams have been generated |
| study-ready | Study materials are ready |
| in-study | learning |
| completed | Study completed |
| archived | Archive or stop maintenance |

---

## 10. Requirements for high-quality diagrams

### 10.1 Output format

It is recommended to save the source code image and the exported image at the same time:

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

### 10.2 Quality Standards

- Each image expresses only one core theme.
- The module names in the figure are consistent with the project source code, documents or reasonable abstractions.
- The direction of the arrow corresponds to the actual execution process.
- There are no unverifiable conjectures in the picture.
- Diagrams and text support each other and do not contradict each other.
- Keep the same style of diagrams for the same project.
- Support README, document site and technology sharing and reuse.

### 10.3 Generation process

1. Read README, docs, examples.
2. Analyze the directory structure and key modules.
3. Sort out the core call chain.
4. Generate Mermaid/PlantUML draft.
5. The concepts and arrow directions in the self-check diagram.
6. Export SVG/PNG.
7. Insert the document.
8. Add explanation and basis under the figure.

---

## 11. AI Agent automated collection process

Standard process:

```text
User pastes GitHub URL and says "include"
-> Parse URL
-> Get repository metadata
-> Read README/docs/examples/source
-> Determine whether it is related to AI Agent
-> Determine classification and inclusion level
-> Create project directory
-> Generate project analysis documents
-> Generate diagram
-> Generate Learning Todo List
-> Generate Learning note template
-> Update PROJECTS.md / LEARNING_PROGRESS.md
-> Output collection report
```

### 11.1 collect pre-judgment

AI Agent needs to judge:

- Whether related to AI Agent.
- Is there any learning value?
- Whether there is enough source code or documentation to analyze.
- Is it runnable or at least statically analyzable.
- Whether this is a duplicate collection.
- Whether the License allows learning and citing.
- Whether it should be in-depth collection, standard collection, lightweight collection, or temporarily not collect.

---

## 12. Local learning system

### 12.1 learning notes directory

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

### 12.2 Learning closed loop

```text
Generate study plan -> Perform learning tasks -> Record Learning notes -> Agent Review -> Generate review questions -> Update next step -> Stage summary
```

---

## 13. Non-functional requirements

| type | Require |
|---|---|
| maintainability | Unified directory structure, templates and naming rules |
| Scalability | New project categories, templates, diagrams types and Agent commands can be added |
| Traceability | Key conclusions must be traceable to source code, documents, operating results, or clear human judgment. |
| local priority | Support local generation, editing and accumulation |
| Quality first | A small number of high-quality items are prioritized over a large number of low-quality links |
| readability | Beginners can understand it, engineers can implement it, and maintainers can continue to update it. |

---

## 14. MVP version

### 14.1 MVP Goals

Verify whether the closed loop of "automatic collect + document generation + diagrams generation + learning tasks + learning notes template" is established.

### 14.2 MVP must support

1. Enter the GitHub address and execute collect.
2. Automatically generate the project directory.
3. Automatically generate a standard document skeleton.
4. Automatically generate at least 3 basic diagrams: architecture diagram, core flow diagram, sequence diagram or learning road map.
5. Automatically generate Learning Todo List.
6. Automatically generate learning notes templates.
7. Automatically update project index.
8. Automatically output collection reports.

### 14.3 MVP is not required for the time being.

- All projects complete source code line-by-line analysis.
- All images have reached a level of visual refinement.
- Automatically complete complete production verification.
- Complete community collaboration process.
- Automatically generate website.

---

## 15. Stage planning

| stage | Target | Main output |
|---|---|---|
| Stage 1 | Personal knowledge base period | Templates, first batch of projects, basic routes |
| Stage 2 | Semi-automated settling period | Automatic collect, diagrams generation, learning notes |
| Stage 3 | Open source period | README, contribution guide, project index, community collaboration |
| Stage 4 | Learning supervision system period | Progress check, note review, review questions |
| Stage 5 | Knowledge system platform period | Methodology, Selection Guide, Production Checklist |

---

## 16. Risks and Responses

| Risk | Description | Response |
|---|---|---|
| Range is too large | It’s easy to get out of control if you want to collect all items | MVP only does 3 to 5 samples |
| Content expired | The AI Agent project is updated quickly | Mark date, version, commit, status |
| Unstable quality | AI automatically generates hallucinations | Quality access control + manual review |
| distortion of diagrams | The image may be inconsistent with the source code | Annotation basis and inferred boundary under the figure |
| link stacking | Project degenerates into Awesome List | Mandatory project deep dive, evaluation, learning tasks |
| Formalizing learning supervision | Just tick and don’t understand | Review questions, understanding checks, reflection summaries |

---

## 17. Success Criteria

### 17.1 Personal Success Criteria

- Ability to systematically understand mainstream AI Agent projects.
- Able to run through, integrate, troubleshoot and evaluate projects.
- Can fill in the gaps in knowledge related to AI Agent.
- Can accumulate reusable learning assets.

### 17.2 Project Success Criteria

- README is clear.
- Directory structure is stable.
- Templates can be reused.
- There are high-quality project analysis samples.
- There are diagrams, learning tasks, and progress records.
- Can be maintained continuously.

### 17.3 Community Success Criteria

- Others can use the project to complete their learning.
- Others can contribute project analysis.
- Others can add content based on the template.
- Projects can help developers avoid detours.

---

## 18. One sentence definition

This is an AI Agent open source project deep dive and learning system driven by AI Agent assistance: users can initiate collect by pasting the GitHub project address, and the system automatically generates project analysis, diagrams, learning routes, learning notes templates and progress tracking capabilities, helping developers move from "being able to use" to "understanding principles, being able to integrate, being able to troubleshoot, and being able to consolidate knowledge".


---

# repository catalog design, document templates and collection process specifications

## 1. repository design goals

repository design must support four core goals:

1. **project deep dive**: Each project has a uniformly structured analysis document.
2. **diagrams accumulation**: Each project has maintainable diagrams source code and exported diagrams.
3. **Learning closed loop**: Each project has a Learning Todo List and local learning notes.
4. **AI Agent friendly**: Users can trigger the standard process through "collect GitHub address", and the AI Agent can generate content according to the agreement.

---

## 2. Recommended repository structure

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

## 3. Single project directory specifications

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

## 4. Learning notes directory specifications

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

## 5. meta.json metadata specification

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

## 6. PROJECTS.md index specification

```markdown
# Projects Index

| Project | Category | Level | Status | Run Verified | Source Reading | Diagrams | Learning Notes | Last Updated |
|---|---|---|---|---|---|---|---|---|
| example-agent | agent-frameworks | A | study-ready | No | Partial | Yes | Yes | 2026-06-10 |
```

---

## 7. LEARNING_PROGRESS.md specification

```markdown
# Learning Progress

## is learning

| Project | Current Stage | Completed | Blockers | Next Action |
|---|---|---:|---|---|
| example-agent | source-reading | 12/38 | Tool registry not fully understood | Reading executor module |

## Completed

| Project | Completed At | Summary |
|---|---|---|
| - | - | - |

## To be reviewed

- [ ] Review the differences between Agent Loop and Tool Calling
- [ ] Compare example-agent with similar frameworks
```

---

## 8. AI Agent command convention

### 8.1 /collect

```text
/collect https://github.com/example/example-agent
```

Function: Start the standard collection pipeline.

### 8.2 /analyze-project

```text
/analyze-project projects/agent-frameworks/example-agent
```

Function: Reanalyze or complete the document.

### 8.3 /generate-diagrams

```text
/generate-diagrams projects/agent-frameworks/example-agent
```

Function: Generate or update architecture diagrams, flow charts, sequence diagrams, and integration diagrams.

### 8.4 /generate-learning-plan

```text
/generate-learning-plan projects/agent-frameworks/example-agent
```

Function: Generate Learning Todo List, learning notes templates and review questions.

### 8.5 /check-progress

```text
/check-progress learning-notes/example-agent
```

Function: Check learning progress, identify stuck points, and give suggestions for next steps.

### 8.6 /review-notes

```text
/review-notes learning-notes/example-agent
```

Function: Check the quality of learning notes, correct misunderstandings, and supplement content to be verified.

---

## 9. /collection standard process specification

### 9.1 Input

```text
Collect: https://github.com/<owner>/<repo>
```

### 9.2 Process

1. Parse the GitHub URL.
2. Get project metadata.
3. Check whether it has been collected.
4. Read README, docs, examples.
5. Analyze the directory structure.
6. Determine whether it is related to AI Agent.
7. Determine the project classification.
8. Determine the collection level.
9. Create a project directory.
10. Create the learning-notes directory.
11. Generate meta.json.
12. Generate project documentation.
13. Generate diagrams source code and export diagrams.
14. Generate Learning Todo List.
15. Generate learning notes template.
16. Update PROJECTS.md.
17. Update LEARNING_PROGRESS.md.
18. Output collect-report.md.

### 9.3 Output

- `projects/<category>/<project-name>/`
- `learning-notes/<project-name>/`
- `PROJECTS.md` Update
- `LEARNING_PROGRESS.md` Update
- collection reports

---

## 10. collect evaluation Checklist

```markdown
# Inclusion evaluation Checklist

- [ ] Projects explicitly related to AI Agent
- [ ] There is README or official documentation
- [ ] There is analyzable source code
- [ ] has examples or usage instructions
- [ ] License acceptable
- [ ] non-duplicate collection
- [ ] has learning value
- [ ] has engineering reference value
- [ ] can generate Learning Todo List
- [ ] can generate at least one valid Diagram
```

---

## 11. Project analysis template

```markdown
# <Project Name> project deep dive

## 1. Basic project information

- GitHub:
- Official documentation:
- Classification:
- Inclusion level:
- Main languages:
- License:
- Date of analysis:
- Analysis version/Commit:
- Whether to run verification:

## 2. Positioning in one sentence

In one sentence, explain what problem this project solves.

## 3. Who is suitable to study?

- Beginners:
- engineer:
- Researcher:
- Enterprise implementation:

## 4. Problems solved by the project

Explain the pain points, core scenarios and value of the project.

## 5. Project main line

Describe the complete main flow from user input to final output.

## 6. Architecture dismantling

Describe core modules, module responsibilities and module relationships.

## 7. Core Principles

Explain Agent Loop, Tool Calling, Memory, RAG, MCP and other related mechanisms.

## 8. Source code reading route

Explain the recommended reading order, key documents, and key call chains.

## 9. Integration Guide

Explain how to access your own project, including API, SDK, CLI, servitization, permissions and logs.

## 10. Troubleshooting

Lists issues with installation, configuration, model invocation, tool invocation, context, permissions, network, etc.

## 11. Objective evaluation

### advantage

### shortcoming

### Applicable scenarios

### Not applicable scenarios

## 12. Learning Todo List

Learning tasks in stages.

## 13. Summary

Write down what is most worth learning and learning from this project.
```

---

## 12. Learning Todo List Template

```markdown
# <Project Name> Learning Todo List

## Level 1: Understand the project

- [ ] Read README
- [ ] Describe the project positioning in one sentence
- [ ] Describe the problem solved by the project
- [ ] Determine what scenarios the project is suitable for

Output: One page of notes on initial impressions of the project.

## Level 2: Run through

- [ ] Install dependencies
- [ ] Configure API Key/Model
- [ ] Run through the smallest demo
- [ ] Record problems encountered

Output: quickstart notes.

## Level 3: Understand the source code

- [ ] Find the entry file
- [ ] Find Agent Loop
- [ ] Find the model calling location
- [ ] Find tool registration logic
- [ ] Find error handling logic

Output: Source code call chain diagram and reading notes.

## Level 4: Complete integration

- [ ] Access a local Demo project
- [ ] Access a custom tool
- [ ] Add log
- [ ] Log integration issues

Output: integration notes.

## Level 5: Second transformation

- [ ] Replace model provider
- [ ] Add a custom workflow
- [ ] Add an evaluation case
- [ ] Optimize context management

Output: Transformation summary.

## Level 6: Summary evaluation

- [ ] Write down the pros and cons of the project
- [ ] Write applicable and inapplicable scenarios
- [ ] Compare with similar projects
- [ ] Summarize the design that can be used for reference

Output: final reflection.
```

---

## 13. progress.json template

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

## 14. diagrams specification template

```markdown
# Diagram Guidelines

## Must be generated

- architecture.mmd
- flow.mmd
- sequence.mmd

## Optional generation

- integration.mmd
- troubleshooting.mmd
- agent-loop.mmd
- rag-flow.mmd
- mcp-tooling.mmd

## Diagram requirements

- Each picture only expresses one theme
- Module naming is consistent with the text
- Arrow direction must be accurate
- Speculative content must be marked
- There must be an explanation below the picture
- Keep the Diagram style consistent for the same project
```

---

## 15. Quality Access Control

### 15.1 Document Quality Access Control

```markdown
- [ ] Whether to describe the project positioning
- [ ] Whether to explain applicable scenarios
- [ ] Whether to indicate inapplicable scenarios
- [ ] Whether to include quick start
- [ ] Whether to include principle analysis
- [ ] Whether to include the source code reading route
- [ ] Whether to include integration guide
- [ ] Whether to include troubleshooting
- [ ] Whether to include objective evaluation
- [ ] Whether to include Learning Todo List
```

### 15.2 diagrams Quality Access Control

```markdown
- [ ] Whether the picture has a clear theme
- [ ] Is the module name accurate?
- [ ] Is the direction of the arrow reasonable?
- [ ] Whether there is no excessive speculation
- [ ] Is it consistent with the text?
- [ ] Whether it can be read independently
- [ ] Is it suitable to be placed in README or documentation site?
```

### 15.3 Learning tasks quality access control

```markdown
- [ ] Whether from light to dark
- [ ] Whether each task is executable
- [ ] Whether there is output at each stage
- [ ] Whether to cover usage, source code, integration, summary
- [ ] Whether to include comprehension check questions
```

---

## 16. collection report template

```markdown
# <Project Name> Inclusion report

## 1. Collection conclusion

- Inclusion level:
- Classification:
- state:
- Whether to recommend in-depth analysis:

## 2. Reason for inclusion

## 3. Project risks

## 4. Generated content

- [ ] project directory
- [ ] metadata
- [ ] Project Documentation
- [ ] Diagram
- [ ] Learning Todo List
- [ ] Learning note template
- [ ] index update

## 5. Awaiting manual verification

## 6. Next step suggestions
```

---

## 17. Recommend the first batch of MVP project types

It is not recommended to pursue quantity in the first batch, and it is recommended to cover 3 to 5 typical types of projects:

1. A general Agent framework.
2. An Agentic Coding tool.
3. A RAG/Knowledge Agent.
4. An MCP/Tool project.
5. An Evaluation / Observability project.

Select 1 project from each category to complete an in-depth collection to verify the template and process.

---

## 18. Minimum executable version delivery list

```markdown
- [ ] README.md
- [ ] ROADMAP.md
- [ ] PROJECTS.md
- [ ] LEARNING_PROGRESS.md
- [ ] templates/ All basic templates
- [ ] learning-roadmap/ initial route
- [ ] projects/ category directory
- [ ] learning-notes/ example directory
- [ ] assets/diagrams/ example diagrams
- [ ] A Level A collection sample
- [ ] A /collection process description
```

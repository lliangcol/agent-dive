# <Project Name> project deep dive

## Usage scenarios

Used to generate the master analysis document for a single AI Agent project. Suitable for Level A in-depth collection and Level B standard collection.

## Fill in the instructions

- Replace `<Project Name>` with the project name.
- Use `owner__repo` for the project directory ID.
- Try to label all conclusions with sources: README, official documents, source code files, running results or manual judgment.
- The content verified by not_run must indicate "not verified".

## Standard structure

### 1. Basic project information

- Project name:
- Project ID:
- GitHub:
- Official documentation:
- Category:
- Collection level:
- Current status:
- Main languages:
- License:
- Date of analysis:
- Analysis version/Commit:
- Whether to run verification:
- Analysis basis:

### 2. Positioning in one sentence

In one sentence, explain what problem this project solves.

### 3. Problems solved by the project

Explain the pain points, core users, main scenarios and learning value of the project.

### 4. Project main line

Describe the main process from user input, task planning, model calling, tool execution to final output.

### 5. Quick start

- Environmental requirements:
- Installation steps:
- Minimal running command:
- Configuration items:
- Expected output:
- Known limitations:

### 6. Core Architecture

Describe core modules, module responsibilities, module boundaries, and data flows. Quote the diagrams under `assets/diagrams/` when necessary.

### 7. Core Principles

Describe the Agent Loop, Tool Calling, Memory, RAG, MCP, Multi-Agent, Evaluation or other mechanisms involved in the project.

### 8. Source code structure

- Entry file:
- Core packages/modules:
- Configuration location:
- Sample code:
- Test directory:
- Document directory:

### 9. Key call chain

Record 1 to 3 of the most important call chains. Each call chain describes trigger conditions, key functions, input and output, and exception handling.

### 10. integration method

Explain how to connect to local demo, business system, CLI, SDK, HTTP API, message queue or Java / Spring Boot project.

### 11. troubleshooting

Document installation, configuration, model invocation, tool permissions, network, context, logs, and runtime environment issues.

### 12. Objective evaluation

#### Advantages

- Advantages:

#### Disadvantages

- Disadvantages:

#### Applicable scenarios

- Applicable scenarios:

#### not applicable scenarios

- not applicable scenario:

### 13. Learning Todo List

To quote or embed the hierarchical learning tasks of the project, it is recommended to generate `learning-todo-list.md` simultaneously.

### 14. Summary

Summarize the design and engineering experience worth learning from this project and the subsequent issues to be verified.

## To-do check items

- [ ] Basic project information has been completely filled in.
- [ ] The problems solved by the project and the main line of the project have been explained.
- [ ] Quick Start has been documented or explicitly stated that verification cannot be run.
- [ ] The core architecture and core principles have been explained.
- [ ] The source code structure and key call chain have been given.
- [ ] The integration method and problem troubleshooting have been explained.
- [ ] Applicable scenarios, not applicable scenarios and objective evaluations have been written.
- [ ] Already included Learning Todo List.

## Quality check items

- [ ] Did not treat README recitation as source code analysis.
- [ ] No unverifiable architectural conclusions are written.
- [ ] does not claim to have been run through but lacks running evidence.
- [ ] diagrams, text and index status are consistent.
- [ ] does not include accounts, keys, local absolute paths or private configurations.
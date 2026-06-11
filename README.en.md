# AgentDive

`agent-dive` is AgentDive’s public learning material repository.

AgentDive is an AI Agent open source project deep dive and learning system, used to collect, disassemble, diagrams and learn excellent AI Agent projects.

## What problem is solved?

There are more and more open source projects related to AI Agent, but it is difficult to truly develop engineering capabilities by just collecting links or running demos according to README. AgentDive hopes to break down a project learning into a repeatable process: first determine whether the project is worth collecting, and then generate project deep dives, diagrams, learning tasks, learning notes and progress records to help learners move from "being able to use" to "understanding principles, being able to integrate, being able to troubleshoot, and being able to settle".

## This project is not an Awesome List

AgentDive does not pursue heap linking, nor does it simply sort by star number. Each collected item should have clear classification, collection level, analysis basis, diagrams, Learning Todo List and learning progress record. Prioritize quality over quantity.

## Target ability

- Paste the GitHub address collect project
- Generate project deep dive documentation
- Generate high quality diagrams
- Generate Learning Todo List
- Generate local learning notes
- AI Agent assisted learning supervision
- Project index and progress record

## Current status

It is currently in the early public preparation, first batch of samples and quality governance construction stages, and the main branch is `main`. This warehouse has collected 8 high-star AI Agent related projects and generated the first round of project deep dive, diagrams, Learning Todo List and learning notes skeleton; however, most of these projects are still in `analyzing` status and have not yet formed complete `study-ready` samples.

Unless `evidence.md` in the project directory clearly records real running, testing or source code verification evidence, do not understand "generated documents" as "run through the project". The current optimization focus is to unify metadata, complete evidence files, correct the drift in the number of learning tasks, and establish a learning closed loop that can be continuously executed by the AI ​​Agent.

## Recommended usage

1. Read [USAGE.md](USAGE.en.md) first, which is a unified entrance for learning, maintenance, collection, and AI Agent tasks.
2. If you just need to get started quickly, read [START_HERE.md](START_HERE.en.md) again to confirm the first step of becoming a learner, maintainer or AI Agent.
3. Read `learning-roadmap/` and establish an AI Agent engineering learning route.
4. View the collected item index in `PROJECTS.md`.
5. After selecting a project, start with the first unfinished task in `learning-todo-list.md` for that project.
6. Record the learning process in `learning-notes/`, and write the operation, testing, and source code verification into `evidence.md` in the project directory.
7. Follow the process of `scripts/collect-project.md` to execute manual or AI Agent-assisted collect; see [scripts/collect-project-usage.md](scripts/collect-project-usage.en.md) for detailed usage.

collect command example:

```text
收录：https://github.com/example/example-agent
```

## Directory description

| directory or file | illustrate |
|---|---|
| `docs/` | The original requirements data and design deliverables shall be retained unchanged. |
| `templates/` | project deep dive, source reading, integration, troubleshooting, diagrams and collect report templates |
| `knowledge/` | AI Agent general knowledge system |
| `learning-roadmap/` | Staged learning route from basic to production-level Agent |
| `projects/` | Collect project deep dive data by category |
| `learning-notes/` | Personal learning notes isolated by project |
| `comparisons/` | Cross-project and ecological comparison |
| `examples/` | Follow-up example project planning |
| `assets/` | AgentDive's own diagrams and public materials |
| `scripts/` | Lightweight process description and subsequent automation entry |
| `PROJECTS.md` | Item collect index |
| `LEARNING_PROGRESS.md` | Overview of learning progress |
| `ROADMAP.md` | Project roadmap |
| `USAGE.md` | A unified entrance for learning, maintenance, collection and AI Agent tasks |
| `START_HERE.md` | Quick start page for learners, maintainers and AI agents |
| `LEARN_WITH_AGENT.md` | AI Agent continuous assisted learning protocol |

## Quality Check

Run after modifying project information, learning notes or index:

```bash
python scripts/check-agent-dive.py
```

Do not upgrade the project status to `study-ready`, `in-study` or `completed` before the verification is passed.

## Open source collaboration

- [CONTRIBUTING.md](CONTRIBUTING.en.md): Contribution process, project collect specifications and PR checklist.
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.en.md): Community Code of Conduct.
- [SECURITY.md](SECURITY.en.md): How to report security issues and sensitive information.
- [SUPPORT.md](SUPPORT.en.md): Issue applicable scope and support boundaries.
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.en.md): Third-party project ownership and citation boundaries.
- [CHANGELOG.md](CHANGELOG.en.md): Visible changes for users and contributors.
- [AGENTS.md](AGENTS.en.md): Warehouse rules for AI coding assistants and automation agents.

## Contribution method

Contributions of project analysis, diagrams, learning routes, template improvements, and bug fixes are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.en.md) first and ensure that the new content has a source, has boundaries, and does not contain accounts, keys, or local private paths.

## Roadmap

Check out [ROADMAP.md](ROADMAP.en.md) to learn about AgentDive’s phase plan.

## License

This repository is open sourced by [MIT License](LICENSE). Third-party project names, trademarks, upstream documents and source code are still owned by their respective rights holders, see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.en.md) for details.

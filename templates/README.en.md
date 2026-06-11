# Templates

This directory saves AgentDive's general templates, which are used for project collection, project deep dive, source reading, integration practice, troubleshooting, diagrams generation, learning tasks and collection reports.

## Usage principles

- The template is a starting point, not the final draft.
- Do not delete the "Based", "Risk" and "To be verified" fields.
- Do not write unverified conclusions as facts.
- Single project content should be saved to `projects/<category>/<owner__repo>/`.
- The content of the learning process should be saved to `learning-notes/<owner__repo>/`.

## Template list

| Template | Purpose |
|---|---|
| `project-analysis-template.md` | project deep dive main document |
| `source-code-reading-template.md` | source reading route and call chain record |
| `integration-guide-template.md` | Guidelines for integration into local or business projects |
| `troubleshooting-template.md` | Problem troubleshooting record |
| `learning-todo-template.md` | List of hierarchical learning tasks |
| `project-evaluation-template.md` | Objective evaluation of the project |
| `diagram-checklist-template.md` | diagrams types and quality checks |
| `collect-report-template.md` | A report of a collection process |

## General quality requirements

- Project name, GitHub address, analysis date and analysis version must be clear.
- runtime verification, source code analysis, and diagrams conclusions must be labeled with the basis.
- Speculated content must be written as "to be verified" or "human judgment".
- Do not write accounts, keys, local absolute paths or private configurations.
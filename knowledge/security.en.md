# Security

## Definition

AI Agent security focuses on tool permissions, data access, prompt injection, code execution, file operations, external requests, and human approval boundaries.

## Role in the AI Agent project

After the Agent can call the tool, the risk extends from "generating wrong text" to "performing wrong actions". The safety boundary determines whether the project can be used in a real engineering or production environment.

## Typical implementation

- Tool least privileges and whitelisting.
- Sandbox execution of code and file operations.
- Sensitive information filtering and desensitization logs.
- Manual approval of high-risk actions.
- Input and output checksum prompt injection protection.

## Common misunderstandings

- Actions selected by the default trust model.
- Tool permissions are too wide.
- Record keys or private data in the log.
- Ignore hint injection in third-party content.

## Recommended learning tasks

- List all high-risk tools in the project.
- Check tool parameter verification and permission control.
- Design a hint injection test case.
- Record a list of actions that require manual approval.

# Ruflo learning notes

Project ID: `ruvnet__ruflo`

Corresponding information directory: `projects/multi-agent/ruvnet__ruflo/`

## Current stage

- Current status: formal study has not started yet
- Current focus: First complete README / package / CLI / MCP / `.agents` boundary understanding and read-only command verification
- Last updated: 2026-06-11

## Note index

- [study plan](00-study-plan.en.md)
- [first impression](01-first-impression.en.md)
- [Quickstart notes](02-quickstart-notes.en.md)
- [Architecture Notes](03-architecture-notes.en.md)
- [source reading notes](04-source-reading-notes.en.md)
- [integration notes](05-integration-notes.en.md)
- [troubleshooting notes](06-troubleshooting-notes.en.md)
- [Review summary](07-reflection.en.md)
- [review questions](review-questions.en.md)

## Next step

1. Read README, `ruflo/package.json`, `.claude-plugin/plugin.json`, `.agents/config.toml`.
2. Execute the read-only commands `npx --yes ruflo@latest --version` and `npx --yes ruflo@latest --help`.
3. Record whether downloading occurs, time consumption, stdout/stderr and whether the file is written.
4. Do source reading along `ruflo/bin/ruflo.js`, `v3/@claude-flow/cli/bin/cli.js`, `mcp-tools/index.ts`.

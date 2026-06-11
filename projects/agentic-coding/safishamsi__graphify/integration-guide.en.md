# Graphify integration guide

## 1. integration goal

- Target system: local code repository and AI coding assistant.
- Target capability: Provide a queryable project knowledge graph for coding assistants to reduce full-text reading and temporary searches.
- Integration method: CLI generates graphs; installs skills/commands/hooks according to the platform; optional MCP server.
- Constraints: The current document has not been verified for local operation, and all commands must be verified in an independent test warehouse.

## 2. Preconditions

- Running environment: Python 3.10+.
- Dependencies: README recommends `uv`; `pipx` is also available.
- Model or service configuration: Code AST extraction is based on the local path according to README; semantic extraction of non-code materials such as docs, PDFs, pictures, etc. may require backend configuration such as OpenAI, Anthropic, Gemini, Bedrock, Azure, Ollama or Claude CLI.
- Permission requirements: Have read permission on the target warehouse; project-scoped install will write the warehouse configuration file, and the working tree should be checked before execution.

## 3. Minimum integration path

### Path A: Only generate this map

1. Install the tool in the test warehouse: `uv tool install graphifyy`.
2. Execute in the target directory: `graphify .`.
3. Check `graphify-out/graph.html`, `graphify-out/GRAPH_REPORT.md`, `graphify-out/graph.json`.
4. Use a code base question to test whether the report can locate relevant modules.
5. Record the command output, time taken, errors and generated file size.

Status: pending verification.

### Path B: Codex project-level integration

1. First save the working tree status of the target warehouse.
2. Execution: `graphify install --project --platform codex`.
3. Check the configuration described in the written `AGENTS.md`, `.codex/hooks.json` or README.
4. Raise a code positioning question in Codex to confirm whether the Graphify query path should be used first.
5. Record the generation configuration and uninstallation method.

Status: pending verification.

### Path C: MCP integration

1. Install MCP extra: `uv tool install "graphifyy[mcp]"`.
2. Construct a map.
3. Start or configure `graphify-mcp`, or press README to use `graphify . --mcp` / query related commands.
4. Ask the MCP-enabled Agent to query a specific function, module, or architectural issue.
5. Check whether the returned content can be traced back to the graph.

Status: pending source code and runtime verification.

## 4. Interface and data flow

| enter | processing module | output | Remark |
|---|---|---|---|
| Project directory | CLI / scanner | Collection of files to be parsed | Need to confirm ignore rule |
| Source code files | Tree-sitter static extraction | Class, function, import, call, annotation node | README basis, to be confirmed by source code |
| Documents/PDF/Images | semantic extraction | Concept nodes and semantic relationships | May call external model or assistant backend |
| Video/Audio | faster-whisper is transcribed into the image. | Transcribe text and related nodes | README says to transcribe local execution, dependencies and output scope still need to be verified |
| Map data | exporter | HTML、Markdown、JSON | README clearly lists |
| Map file | MCP server / query | subgraph or related context | To be verified |
| Platform parameters | installer | skill / AGENTS / hook configuration | The write range must be checked |

## 5. Java/Spring Boot integration concerns

Graphify is better suited as an external code base understanding tool rather than directly embedded into the Spring Boot runtime.

- Bean life cycle: does not involve in-application beans, unless the query service is subsequently encapsulated by itself.
- Configuration management: Graphify configuration should be separated from business application configuration to avoid mixing production keys.
- Permissions and auditing: Do not allow Agents to read sensitive code, configuration, or database dumps without auditing.
- Logs and link tracing: records Graphify run commands, versions, commits, and input scopes.
- Timeout, retry and current limit: When non-code semantic extraction calls external models, it is necessary to limit the cost and retry on failure.
- Database or message queue: SQL schema can be used as input material for analysis, but it cannot replace real database permission auditing.

## 6. Integration risks

- Dependent versions: Python, uv/pipx, Tree-sitter extras, multi-modal extras may affect installation.
- Model cost: Non-code semantic extraction such as docs, PDFs, pictures, etc. may incur API call costs; code-only AST paths do not require an API key according to README.
- Tool permissions: Installing hooks or assistant configurations will change the Agent workflow and must be auditable and rollable.
- Data security: Confirm whether code, documents, images, videos and transcribed content go to local paths or external models/assistant backends.
- Operational stability: The first round of map construction for large warehouses may be time-consuming and requires caching and incremental strategy verification.

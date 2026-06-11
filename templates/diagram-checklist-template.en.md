# <Project Name> diagrams list

## Usage scenarios

Used for planning, generating and checking project diagrams. Diagrams should help readers understand the architecture, processes, calling relationships, integration boundaries, and troubleshooting paths.

## Fill in the instructions

- Each image expresses only one core theme.
- Mermaid source files are saved as `.mmd` first.
- It is recommended to save the exported diagram as `.svg` or `.png`.
- Single-item diagrams are saved to `projects/<category>/<owner__repo>/assets/diagrams/`.

## Standard structure

### 1. Architecture diagram

- File: `architecture.mmd`
- Objective: Describe system modules, module responsibilities and major dependencies.
- Check: Whether the module naming is consistent with the source code or documentation.

### 2. Flowchart

- File: `flow.mmd`
- Objective: Describe the main flow from user input to final output.
- Check: Whether the arrow direction conforms to the actual execution sequence.

### 3. Timing diagram

- File: `sequence.mmd`
- Objective: Describe the sequence of interactions between users, agents, models, tools and external services.
- Check: synchronous, asynchronous, retry and error branches are clear.

### 4. Module relationship diagram

- File: `module-relations.mmd`
- Goal: Explain dependencies and boundaries between key modules.
- Check: Whether to avoid simply drawing the directory structure as an architectural conclusion.

### 5. Schematic diagram

- File: `principle.mmd`
- Objective: Explain core mechanisms such as Agent Loop, Tool Calling, RAG, Memory or MCP.
- Check: Whether the abstract concept is consistent with the project implementation.

### 6. integration diagram

- File: `integration.mmd`
- Objective: Explain how the project connects to local or business systems.
- Check: input and output, permissions, logs and failure paths are covered.

### 7. Troubleshooting diagram

- File: `troubleshooting.mmd`
- Objective: Explain the location path of common problems.
- Check: whether the troubleshooting steps are executable.

## diagramsquality standards

- [ ] Each picture has only one theme.
- [ ] The module name is consistent with the text, source code or official documentation.
- [ ] Arrow direction is accurate.
- [ ] Speculative content is marked.
- [ ] diagrams do not contradict the text.
- [ ] There are explanations and basis below the picture.
- [ ] The diagrams of the same project have the same style.
- [ ] can be used for README, documentation site or technology sharing.

## To-do check items

- [ ] The diagrams that must be generated for this project have been identified.
- [ ] Mermaid source file created.
- [ ] Checked that the diagrams are consistent with the text.
- [ ] Unvalidated assumptions about diagrams have been documented.

## Quality check items

- [ ] Not drawing unverifiable modules as facts.
- [ ] Don’t let one picture carry too many themes.
- [ ] File naming is clear and maintainable in the future.
# <Project Name> Collection Report

## Usage scenarios

Used to record the collection process of a project, describing the collection conclusion, basis, risks, generated documents and matters to be manually confirmed.

## Fill in the instructions

- The collection report must be saved to the corresponding project directory.
- Level D projects that are not yet suitable for collection can also keep reports, but do not create a complete project deep dive directory.
- Do not write unimplemented automation capabilities as completed.

## Standard structure

### 1. Basic information

- GitHub address:
- Collection time:
- Project name:
- Project ID:
- Project category:
- Collection level:
- Current status:
- Recommended for collection:
- Collector / Agent:

### 2. Collection basis

- Relevance to AI Agent:
- Project learning value:
- Engineering reference value:
- Documentation and source code analyzability:
- License preliminary judgment:
- Whether this is a duplicate collection:

### 3. Risks

- Operational risks:
- Maintenance risks:
- Security risks:
- Document expiration risk:
- Conclusion items to be verified:

### 4. Generated file list

- [ ] `projects/<category>/<owner__repo>/README.md`
- [ ] `projects/<category>/<owner__repo>/project-analysis.md`
- [ ] `projects/<category>/<owner__repo>/learning-todo-list.md`
- [ ] `projects/<category>/<owner__repo>/collect-report.md`
- [ ] `projects/<category>/<owner__repo>/assets/diagrams/`
- [ ] `learning-notes/<owner__repo>/`
- [ ] `PROJECTS.md` Update
- [ ] `LEARNING_PROGRESS.md` Update

### 5. Items awaiting manual confirmation

- [ ] Whether the license allows citation and learning use.
- [ ] Whether the core call chain is consistent with the source code.
- [ ] Whether the quick start has actually been run successfully.
- [ ] Are the diagrams accurate?
- [ ] Whether the collection level is appropriate.

### 6. Suggested next steps

- Follow-up actions:

## To-do check items

- [ ] The GitHub address, collection time, category and level have been filled in.
- [ ] States whether collection is recommended.
- [ ] Basis, risks, and generated files are listed.
- [ ] Items to be manually confirmed have been listed.

## Quality check items

- [ ] No false collection results are recorded.
- [ ] No exaggeration of automation capabilities.
- [ ] Collection level matches output requirements.
- [ ] Directory ID uses `owner__repo`.

# AI-usage-lessons

Personal knowledge management and course delivery system built on Claude Code.

## What is this

A system for managing:

- A semester course **"Прикладные задачи ИИ"** (Applied AI Tasks) for МГТУ Баумана students
- A project library of normative documents, references, and materials
- All powered by **Claude Code as the only runtime** -- no separate backend, no custom UI

Everything runs through subagents, skills, hooks, and MCP servers orchestrated by Claude Code.

## Quick start

1. Install [Claude Code](https://claude.ai/code)
2. Clone this repo
3. Run setup: see [`blueprint/setup.md`](blueprint/setup.md) for full instructions
4. Configure MCP servers: workspace-mcp (Google), github-mcp, document-loader, local-rag, drawio, open-ontologies

## Architecture

```
Google Drive  <-->  workspace-mcp  <-->  Claude Code  <-->  GitHub
                                              |
                document-loader --> local-rag (semantic search)
                open-ontologies (knowledge graph)
                drawio (diagrams)
```

## MCP Stack

| Server | Package | Purpose |
|--------|---------|---------|
| workspace-mcp | `workspace-mcp` | Read/write Google Docs, Sheets, Slides, Drive |
| document-loader | `awslabs.document-loader-mcp-server` | Read PDF, DOCX, XLSX, PPTX, images |
| local-rag | `mcp-local-rag` | Semantic search over ingested documents |
| drawio | `@drawio/mcp` | Generate/preview `.drawio` and Mermaid diagrams |
| github | `github-mcp-server` | Issues, PRs, repo operations |
| open-ontologies | `open-ontologies` | RDF/SPARQL + OWL reasoning + SHACL validation |

## Skills (9)

Skills live in `.claude/skills/` and are invoked via `/skill-name`.

| Skill | Purpose |
|-------|---------|
| `sync-library` | Pull changes from Google Drive |
| `catalog-docs` | Update document index and manifests |
| `extract-links` | Extract and track cross-references |
| `update-lecture` | Create/update lecture documents |
| `build-deck` | Build/update Google Slides decks |
| `diagram-refresh` | Regenerate diagrams from sources |
| `issue-from-change` | Create GitHub Issues from detected changes |
| `impact-check` | Analyze what changed and what it affects |
| `reflect` | Post-session analysis and lessons learned |

## Agents (5)

Agent definitions live in `.claude/agents/`.

| Agent | Responsibility |
|-------|---------------|
| `librarian` | Search, sync, export, index documents |
| `course-curator` | Link normative docs, lectures, materials, assignments |
| `doc-editor` | Edit Google Docs via workspace-mcp |
| `deck-editor` | Build/update Google Slides, insert diagrams |
| `issue-manager` | Create/triage GitHub Issues, track change queue |

## Ontology visualization

Graph and table views are available in [`catalog/exports/viz/`](catalog/exports/viz/).

- `ontology-graph.html` -- interactive force-directed graph of entities and relations
- `ontology-table.html` -- tabular view of all triples

Regenerate with: `python3 scripts/viz-ontology.py`

## Repository structure

```
blueprint/       -- portable agent setup for reproducing in new repos
catalog/         -- exported Google artifacts, RAG index, manifests
diagrams/        -- canonical .drawio files and exports
library/         -- source materials: normative, lectures, materials
models/          -- LanceDB embeddings and model data
notes/           -- decisions, reflections, experiments
ontology/        -- RDF schema (TTL), vocab, SPARQL queries
scripts/         -- utility scripts (viz, export, etc.)
templates/       -- reusable templates for lectures, slides, issues
workflows/       -- routine descriptions, checklists, triage rules
```

See [`CLAUDE.md`](CLAUDE.md) for full conventions, rules, and detailed layout.

## Course content

- 14-lesson semester plan covering AI across 6 industries
- Lecture 1 Google Doc: [Введение в прикладной ИИ](https://docs.google.com/document/d/1fJXhJMoSf-hRPGFnaTMB5z3rr0mJDs2iFaJBGIL36TE)
- Lecture 1 Slides: [Slide deck](https://docs.google.com/presentation/d/12THMwFst0CHGJ0GJNqsWI1IMmF3jQMO3L2VszVEfJwI)
- Semester roadmap diagram: [`diagrams/lecture-flows/semester-roadmap.drawio`](diagrams/lecture-flows/semester-roadmap.drawio)

## Google Drive

- [Working folder](https://drive.google.com/drive/folders/1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am) -- active documents and materials
- [Formal documents folder](https://drive.google.com/drive/folders/1fFxwUPu5V4dmCGMy5Y15xqzYF5CYD1yU) -- normative and reference materials

## Documentation

- [`CLAUDE.md`](CLAUDE.md) -- conventions, rules, MCP config, orchestration patterns
- [`blueprint/`](blueprint/) -- portable agent setup for reproducing in new repos
- [`notes/reflections/`](notes/reflections/) -- session analysis and lessons learned
- [`notes/decisions.md`](notes/decisions.md) -- decision log and accumulated best practices

## License

Private repository.

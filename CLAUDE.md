# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI-usage-lessons is a personal knowledge management and course delivery system built entirely on Claude Code as the runtime. It manages a project library (normative documents, references) and a semester course for students (lectures, slides, materials) using an agent-based orchestration approach with MCP integrations.

**Owner:** single maintainer — speed and simplicity over enterprise patterns.

## Architecture

### Runtime

Claude Code is the only runtime. No separate backend, no custom UI. All automation happens through subagents, skills, hooks, and MCP servers.

### MCP Stack (priority order)

| Layer | Server | Purpose |
|-------|--------|---------|
| Google | `workspace-mcp` | Read/write Google Docs, Sheets, Slides, Drive |
| Doc Loader | `document-loader` | Read PDF, DOCX, XLSX, PPTX, images — full office format support |
| Local RAG | `mcp-local-rag` | Semantic search over ingested documents (PDF, DOCX, TXT, MD) |
| Diagrams | `drawio` (@drawio/mcp) | Generate/preview `.drawio` and Mermaid diagrams |
| GitHub | `github` (github-mcp-server) | Issues, PRs, repo operations |
| Ontology | `open-ontologies` | RDF/SPARQL + OWL reasoning + SHACL validation (Oxigraph-based) |

**Tool selection rule:** `workspace-mcp` is the only Google integration server. Use it for all Google Workspace operations.

### MCP Configuration

- MCP servers are registered via `claude mcp add` or `.mcp.json` (NOT `.claude/settings.json`)
- Secrets (OAuth credentials, PATs) go in `.mcp.json` only — this file is gitignored
- `.claude/settings.json` is for non-secret server configs and permissions only
- After any MCP config change, restart Claude Code for changes to take effect
- Always verify registration with `claude mcp list` after adding a server

### Google Drive Work Folder

Primary working folder: `https://drive.google.com/drive/folders/1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am`

### Google Drive Folder Structure

| Path | ID | Contents |
|------|-----|----------|
| `00-course/` | `1sHXoLaIqCpBRv1IaLjS6lNtBdwI5cPc0` | Структура курса, нарратив, каталог тем (sheet), чит-шит |
| `01-formal/` | `1-sQ7H1CBNWaHvQIDE8TLCwVX2ilEeb0p` | РПД, ФОС, матрица компетенций |
| `02-lectures/` | `16osAMJ9y67Yem9T6fK6yDv1fXF8BGLEZ` | 17 папок лекций (lec-01 — lec-17), каждая: plan + slides + assets/ |
| `03-seminars/` | `1AZhb5q-yODrIJEnQBN8S1KJI0bby588J` | 17 папок семинаров (sem-01 — sem-17), каждая: task-brief + rubric |
| `04-resources/` | `1yDZrw9CcGtGljNGZ-QByyoUGIMVr9Tc4` | Библиотека промптов, статистика, список литературы |
| `archive/` | `1rZkywX5DufGJaf1htCa1Oa_zCKmUgKMT` | Старые версии |

**Правила размещения:**
- Ресурсы для одной лекции → `lec-NN/assets/` (не в 04-resources)
- Ресурсы для нескольких лекций → `04-resources/`
- Табличные данные → Google Sheets (не Docs с markdown-таблицами)
- Старые версии → `archive/` (перемещать, не удалять)

### GitHub Project Board

Issues and tasks are tracked at: `https://github.com/orgs/tellina-study/projects/1/views/1`

## Mandatory Git Rules

- **NEVER push to main directly** — always create feature branches and PRs. This is NON-NEGOTIABLE, even for "small" fixes, doc updates, or config changes.
- **Branch naming**: `issue-{NUMBER}-{short-description}`
- **Every commit references the issue**: `#{NUMBER}` in commit message
- **Workflow**: create branch → commit → push branch → create PR → review → merge
- **Never merge own PRs** without explicit user confirmation
- **No work without an issue.** If one doesn't exist, create it first.

---

## Orchestration Rule (ENFORCED)

Claude Code acts as **planner and orchestrator only**. It MUST NOT make implementation changes directly. ALL implementation work MUST be delegated to subagents (Agent tool with appropriate prompts).

**Claude Code does:**
- Plan and design (create/update design docs, issues, plans)
- Research (read files, search code, web search)
- Orchestrate (spawn subagents, review their output, gate phases)
- Communicate (present results to user, ask for approval)

**Claude Code does NOT:**
- Edit source content files directly — subagents do this
- Create/modify documents, lectures, diagrams without delegation

**Exception:** CLAUDE.md, design docs, GitHub issue descriptions, repo scaffolding, and system setup (MCP installation, git operations, `.gitignore`, settings files) may be done directly — these are infrastructure/planning artifacts, not implementation content.

---

## Subagent Rules

**Delegate to subagents:** MCP operations, web research, document editing, diagram creation, content writing, analysis.

**When spawning subagents, always include:**
- Specific MCP tool names the subagent should use
- User email: `kzlevko@gmail.com` (for Google operations)
- Specific file paths (not just directory names)
- Error handling instructions ("if auth fails, stop and report")

**If a subagent fails, do the work directly** — do not retry the same delegation.

---

## Roast-Before-Implement Rule (ENFORCED)

For non-trivial tasks, after planning and before implementation:
1. **ROAST the plan** — self-critique for: over-engineering, unverified assumptions, premature abstractions, missing owners for new files, bundled risky changes that should be isolated
2. **Improve** — fix issues found in roast
3. **Present improvements** — show user the roast findings and proposed changes
4. **Get approval** — user approves improved plan before implementation starts

Key roast questions:
- Is this the simplest version that works?
- Are there unverified external dependencies (APIs, tools, auth)?
- Who owns each new file/process?
- Can risky changes be isolated instead of bundled?

---

## Phase Gating Rule (ENFORCED)

Multi-phase implementations MUST follow this sequence per phase:
1. **Implement** — make the changes
2. **Verify** — validate the result (test, inspect, check consistency)
3. **Gate** — user explicitly approves. Do NOT start next phase until approved.

Never skip verification. Never proceed to next phase without gate.

---

## Anti-Patterns (NEVER DO THESE)

| Anti-Pattern | Correct Approach |
|--------------|------------------|
| Push to main directly | Always use feature branches + PRs |
| Work without a GitHub Issue | Every task gets an issue, no exceptions |
| Store task state only in memory | GitHub Issues are source of truth |
| Skip issue creation for "quick" tasks | Every task gets an issue |
| Bundle risky changes together | Isolate risky changes into separate branches/PRs |
| Make implementation changes as orchestrator | Delegate all implementation to subagents |
| Skip roast step for non-trivial work | Always roast before implement |
| Proceed without phase gate approval | Wait for explicit user approval between phases |

---

## Document Size Limit (ENFORCED)

**No single document may exceed 600 lines.** If a document grows beyond 600 lines, split it into logical parts with cross-links. Code files are exempt but should still favor smaller, focused modules.

---

## Best Practices Documentation

**Reference:** `notes/decisions.md` — accumulated findings, patterns, and anti-patterns.

### Update Rule
Every time a new finding, gotcha, or best practice is discovered during work, it MUST be added to `notes/decisions.md`. Before starting work, CHECK this file for existing findings relevant to your task.

---

## Working Conventions

### Subagents (`.claude/agents/`)

| Agent | Responsibility |
|-------|---------------|
| `librarian` | Search, sync, export, index documents |
| `course-curator` | Link normative docs, lectures, materials, assignments |
| `doc-editor` | Edit Google Docs via workspace-mcp |
| `deck-editor` | Build/update Google Slides, insert diagrams |
| `issue-manager` | Create/triage GitHub Issues, track change queue |

### Skills (`.claude/skills/`)

Eight core skills: `sync-library`, `catalog-docs`, `extract-links`, `update-lecture`, `build-deck`, `diagram-refresh`, `issue-from-change`, `impact-check`.

Skills are invoked via `/skill-name` (e.g., `/sync-library`). Each SKILL.md must be an executable recipe with concrete MCP tool names and parameters, not just a description of steps. If a skill cannot be executed as-is, it needs implementation work.

### Repository Layout

```
catalog/         — exported Google artifacts and RAG index
  exports/       — docs/, sheets/, slides/, pdf/
  index/         — knowledge-rag index data
  manifests/     — documents.yaml, lectures.yaml, decks.yaml, diagrams.yaml
diagrams/        — canonical .drawio files and exports
library/         — source materials: normative/, lectures/, materials/, project/
ontology/        — RDF schema (TTL), vocab, SPARQL queries
templates/       — reusable templates for lectures, slides, issues, requirements
workflows/       — routine descriptions, checklists, triage rules
notes/           — decisions, limitations, experiments log
```

### Ontology (Oxigraph)

**Entities:** Document, Section, Requirement, Lecture, SlideDeck, Diagram, Task, Topic

**Relations:** cites, covers, illustrates, depends_on, supersedes, tracked_by, belongs_to_topic

**Attributes:** source_url, source_system, updated_at, status, owner, version_label

Keep ontology minimal — store structural facts and references only, never duplicate document text in RDF.

## File Conventions

- Always save raw document exports to `catalog/exports/docs/` before any processing or ingestion
- Always save `.drawio` diagrams to `diagrams/` — never just open in browser without saving the XML file
- Update `catalog/manifests/*.yaml` after every export or ingestion operation
- Use `ingest_file` (from saved local path), not `ingest_data` (from strings) — file-based ingestion creates traceable provenance
- **Creating Google Docs:** use `import_to_google_doc` with `source_format="md"`, NOT `create_doc`. The import tool converts markdown headings, bold, lists, tables to native Google Docs formatting. `create_doc` inserts raw text with no formatting.

## Security Rules

- `catalog/exports/` must NEVER be committed to a public repository (contains exported Google docs).
- Limit `workspace-mcp` to read-heavy mode initially; write only for owned Docs/Sheets/Slides.
- GitHub MCP: restrict to repo/issues/PR toolsets, no org/admin scopes.
- No API keys, tokens, or credentials in committed files.

## Daily Cycle

1. **Sync:** `sync-library` skill pulls changes from Google Drive
2. **Catalog:** `catalog-docs` + `extract-links` update index and ontology
3. **Tasks:** changes trigger `issue-from-change` to create/update GitHub Issues
4. **Content:** `update-lecture`, `build-deck`, `diagram-refresh` as needed

## Weekly Cycle

- `impact-check` — what changed and what it affects
- Issue triage via `issue-manager`
- Update `notes/decisions.md`

## Reflection Process

After each working session:
1. Create `notes/reflections/{date}-{topic}/` folder (or `notes/reflections/{topic}.md` for single-file reflections)
2. Write separate reflection files per area: tools, workflow, content, user-feedback
3. Update `notes/decisions.md` with key findings from reflections
4. Reflections feed into next session's improvements — always check `notes/reflections/` before starting work

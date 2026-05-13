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
- **PR merge — только по прямому указанию пользователя.** Не мержить PR без явной команды («мерж», «merge», «давай», «go ahead»). Когда указание получено — Claude мержит сам через `gh pr merge <N> --merge --delete-branch`. НЕ перекладывать кнопку на пользователя.
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

**Additional ENFORCED rules:**
- **All critic agents must use 4-level verdict scale:** APPROVE-CLEAN / APPROVE-WITH-POLISH / REVISE / REJECT (replace APPROVE-WITH-MINOR catch-all per Lec 1 lessons). Counter-check: если ≥5 P1 issues но verdict = APPROVE-WITH-POLISH — STOP, change to REVISE.
- **Schema Readability Checklist:** for any schema slide, designer must pass + critic must verify (cross-ref `tools/presentation-build/README.md` §5.5).

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

## Pre-USER-GATE Walkthrough Rule (ENFORCED)

Before presenting any USER GATE to user:
1. **Mandatory:** invoke `/pre-user-gate` skill (orchestrator can also do manual walkthrough)
2. **Visual sweep:** для slides — open all PNG snapshots, 5-sec look per slide, can I state main message?
3. **Notes read:** 5-7 random speaker notes — verify 150-300 words connected text, no «Лектору» / no layout descriptions
4. **Cross-artifact grep:** terminology drift, orphan references, pacing math
5. **Designer-extras grep:** «Лектору» / «Вы здесь» / тайминг in visible content — should all be 0

**Если найдены P0/P1 issues — NOT present GATE.** Spawn revision first, re-run pre-gate, потом present.

**Why ENFORCED:** Лекция 1 production имела 3 раунда user feedback ПОСЛЕ critic APPROVE. Pre-gate walkthrough catches что critics miss (visual schema readability, designer-added extras, terminology drift).

---

## Orchestrator Self-Critique Rule

When making decisions on behalf of user:
- Slide composition (e.g., «which 4 breakthroughs in s09») — do **freshness pre-check** through web search before committing
- Term renames — do **cascade-of-changes** grep through all artifacts
- Slide adds/deletes — do **curriculum relevance** check (зачем это в лекции N?)
- Visual choices (palette deviations, motif breaks) — defer to designer/user, не decide alone

**Why:** Lec 1 — orchestrator chose Llama-3 + MCP в s09 (refused by user as «not прорывы»). Should have done freshness check.

---

## No Extra Content Rule (ENFORCED for all agents)

Agents do nothing not in task brief. Common temptations to RESIST:

- Designer adding «Лектору» sections, «Вы здесь» markers, timing on visible content, subtitles, callback frames, mini-dividers — FORBIDDEN
- Writer adding terminology variants without cross-artifact sync — FORBIDDEN
- Critic recommending content additions without curriculum relevance check — FORBIDDEN
- Orchestrator implementing «improvements» on behalf of user — FORBIDDEN

If agent SEES opportunity for improvement → REPORT to orchestrator. NEVER implement.

**Why:** Lec 1 had 8 designer-added items removed by user across 2 rounds.

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
| Designer-added extras без brief (subtitle, «вы здесь», тайминг, «Лектору») | Producer agents REPORT improvements, не apply (см. No Extra Content Rule) |
| Speaker notes как layout description («слева donut, справа bar») | Notes — readable student text 150-300 слов, derived from chapter+speech |
| Critic catch-all APPROVE-WITH-MINOR | 4-level verdict scale: APPROVE-CLEAN / APPROVE-WITH-POLISH / REVISE / REJECT |
| Term drift без cascade tracking | Glossary lock после chapter approval; cascade-of-changes grep при renames |

---

## Document Size Limit (ENFORCED)

**No single document may exceed 600 lines.** If a document grows beyond 600 lines, split it into logical parts with cross-links. Code files are exempt but should still favor smaller, focused modules.

---

## Best Practices Documentation

**Reference:** `notes/decisions.md` — accumulated findings, patterns, and anti-patterns.

### Update Rule
Every time a new finding, gotcha, or best practice is discovered during work, it MUST be added to `notes/decisions.md`. Before starting work, CHECK this file for existing findings relevant to your task.

---

## MCP Limitations Catalog (ENFORCED)

**Reference:** `notes/mcp-limitations.md` — централизованный каталог известных багов, отсутствующих фич и обходов в MCP-серверах + render-toolchain'е.

### Update Rule (обязательная актуализация)
Каждый раз, когда обнаружена новая limitation MCP-сервера или render-инструмента (failed tool call с явной причиной, баг внутри сервера, отсутствующая capability, render artifact), она **должна быть добавлена в `notes/mcp-limitations.md`** в той же сессии. Использовать готовый шаблон записи (см. начало файла).

### Read Rule (обязательная проверка)
**Перед использованием MCP-tool, который ранее давал проблемы**, или **в начале работы с малознакомым MCP-сервером**, агент **обязан** прочитать соответствующий раздел `notes/mcp-limitations.md`.

Это касается всех агентов (`presentation-designer`, `presentation-critic`, `librarian`, `course-curator`, `doc-editor`, `issue-manager`, `student-simulator`, `reader-simulator`) и Claude как orchestrator.

---

## Working Conventions

### Subagents (`.claude/agents/`)

**General-purpose / infrastructure:**
| Agent | Responsibility |
|-------|---------------|
| `librarian` | Search, sync, export, index documents |
| `course-curator` | Link normative docs, lectures, materials, assignments |
| `doc-editor` | Edit Google Docs via workspace-mcp |
| `issue-manager` | Create/triage GitHub Issues, track change queue |

**Lecture production (multi-artifact: chapter + slides + speech):**
| Agent | Producer/Critic | Responsibility |
|-------|---|---------------|
| `book-editor` | Producer | Пишет/правит главу методички (`chapter.md`, ~10k слов, academic) |
| `presentation-designer` | Producer | Визуальный дизайнер deck'а — рендер через PowerPoint MCP с visual-loop, Ocean palette + Anthropic anti-patterns |
| `speech-writer` | Producer | Пишет речь лектора (`speech.md`, ~5k слов, conversational) |
| `methodology-critic` | Critic | Pedagogical depth, LO coverage, sequence, assertion-evidence (применяется к chapter, plan, slides, speech) |
| `fact-checker` | Critic | Проверка фактов, цифр, дат, citations (использует WebSearch для verification) |
| `presentation-critic` | Critic | Методико-визуальный ревью slides (vision-enabled) |
| `student-simulator` | Critic | Симулирует студента в зале (PNG + speaker notes) |
| `reader-simulator` | Critic | 2 режима: `text-only` (md без рендера) и `rendered` (PNG+notes через 2 нед) |
| `consistency-checker` | Critic | Cross-artifact alignment: chapter ↔ slides ↔ speech |

### Lecture Production Pipeline (ENFORCED, multi-artifact)

**Canonical doc:** `tools/lecture-production/README.md` — полный 10-фазный pipeline для production лекции с **3 финальными артефактами**:
1. `library/lectures/lec-NN/chapter.md` — глава методички (~10k слов, **source of truth**, academic).
2. `library/lectures/lec-NN/rendered/lec-NN.pptx` — презентация со speaker notes (derived from chapter).
3. `library/lectures/lec-NN/speech.md` — речь лектора (~5k слов, conversational; derived from chapter+slides).

**Source of truth: book-first.** Chapter — primary, slides + speech derive. При conflict — fix slides/speech (если chapter сам не ошибается).

**3 USER GATEs** между phases 4-5 (chapter approved), 8-9 (slides approved), 11 (final). Не двигаться к следующей фазе без explicit user approval.

**Phase 9.5 (Pre-USER-GATE walkthrough)** — orchestrator must run pre-gate review before EACH USER GATE (см. `tools/lecture-production/README.md` + Pre-USER-GATE Walkthrough Rule выше).

**Critic agents применяются на каждом этапе** (промежуточные + финальные результаты — обязательное требование).

### Presentation Pipeline (slides-specific subset)

**Single source of truth:** `tools/presentation-build/README.md` — slides-specific pipeline + slide-types library (8 типов) + visual-loop workflow + 12-section design playbook + anti-patterns + tool catalog.

Используется в **Phase 5-8** lecture-production pipeline.

**Stack:**
- **Render-target:** PowerPoint (PPTX) через `office-powerpoint-mcp-server` (GongRzhe, `uvx`-установка, 37 tools).
- **Source-of-truth:** `library/lectures/lec-NN/deck.yaml` + `slides/*.md` (repo-first; Drive — только publish target, отложено).
- **Visual generation:** Generate→Convert (libreoffice + pdftoppm)→Inspect (Claude vision)→Fix цикл, **минимум 3 итерации на слайд** (Anthropic principle).
- **Visual elements:** PowerPoint MCP shapes + QuickChart API (charts) + mermaid CLI (diagrams) + ImageMagick + librsvg2-bin (icons recolor) + Lucide/Heroicons/Phosphor/LobeHub CDN.
- **Palette LOCKED:** Ocean Gradient (`#21295C` / `#065A82` / `#1C7293`) + Teal `#028090` secondary + Gold `#F0AB00` highlight ≥1×/слайд.
- **Visual motif:** «Ocean rounded box» (radius 12, surface `#F4F7FA`, stroke `#1C7293`) на каждом content слайде.

**Workflow:** `/build-deck N` — orchestrator-skill, спавнит `presentation-designer` для рендера + 3 QA agents (`presentation-critic` + `student-simulator` + `reader-simulator` mode=rendered) параллельно. `reader-simulator` mode=`text-only` запускается ДО рендера для методического контроля.

**Required reading для любого agent'а, работающего со слайдами:** `tools/presentation-build/README.md` (агенты начинаются с явной ссылки на этот файл). Также обязательно `notes/mcp-limitations.md` (PowerPoint MCP gotchas) и `notes/decisions.md` § «2026-05-12 — Presentation pipeline» (anti-patterns каталог).

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

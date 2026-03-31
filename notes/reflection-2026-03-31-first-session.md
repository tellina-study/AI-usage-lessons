# Reflection: First Working Session (2026-03-31)

Retrospective on the inaugural session of the AI-usage-lessons system. Honest assessment of what worked, what broke, and what was learned.

---

## What Was Accomplished

In a single session the system went from an empty repo to a functioning knowledge management platform:

- Repository scaffolded: CLAUDE.md, 5 agents, 8 skills, ontology schema, templates, workflows, notes
- 6 MCP servers installed and verified (211 tools total): workspace-mcp, github-mcp, document-loader, local-rag, drawio, open-ontologies
- Google OAuth completed for workspace-mcp
- All 7 files from Google Drive working folder read and analyzed
- Ontology loaded into Oxigraph (65 triples, 8 classes)
- 3 documents ingested into local-rag (222 chunks)
- Formal program (RPD) rewritten to match V2 course content
- Semester roadmap diagram created and saved as .drawio
- Issue-driven workflow established with GitHub Issues #1 and #3, labels, and project board

That is a lot for one session. The system bootstrap worked.

---

## Critical Problems

### 1. MCP Configuration Discovery Was Painful

The biggest time sink of the session. Three different configuration locations were tried before finding the right one:

1. `.claude/settings.json` mcpServers section -- did not register servers
2. `.claude/settings.local.json` -- also did not work
3. `.mcp.json` via `claude mcp add` -- this is the correct method

Multiple restarts were required. This is a documentation gap in Claude Code itself, but the lesson for this project is clear: **`.mcp.json` is the only MCP config location that matters.** The `settings.json` mcpServers section is either deprecated or serves a different purpose.

**Time wasted:** significant. This should have taken 10 minutes, not 45+.

### 2. Secrets Almost Committed

During the configuration dance, API tokens and OAuth credentials were briefly present in `settings.json`, which is tracked by git. This was caught before commit, but it was close. The root cause was the configuration confusion above -- if the right file (`.mcp.json`, which is gitignored) had been used from the start, secrets would never have touched a tracked file.

**Risk level:** high. A single careless `git add -A` would have leaked credentials to GitHub.

### 3. Subagent Permission Model Is Restrictive

Six parallel research subagents were launched and all six failed because they lacked access to WebSearch, WebFetch, and Bash. This forced all research back to the main conversation, defeating the orchestration model.

This is a fundamental constraint, not a bug. Subagents run in a sandboxed context. The CLAUDE.md orchestration rule ("delegate ALL implementation to subagents") needs a caveat: subagents cannot do web research. The orchestrator must handle research directly, then pass findings to subagents for implementation.

### 4. Raw Document Export Was Skipped

Documents were ingested into local-rag directly from MCP string content without first saving them as files to `catalog/exports/docs/`. This means:

- No local backup of the exported content
- No diffing capability for change detection
- The ingest pipeline is not reproducible (depends on live Google Drive state)

The correct flow is: Google Drive -> export to local file -> ingest from file. This was corrected for one document but the pattern was not consistently applied.

### 5. Diagram Save Convention Missing

The first diagram was created and opened in a browser but not saved to the repository. This is useless for version control. The convention must be: every diagram gets saved as a `.drawio` file in the `diagrams/` directory. Browser preview is optional; file save is mandatory.

### 6. Formal Program Rewrite Was Extremely Slow

The doc-editor subagent made 68 MCP API calls over ~47 minutes to rewrite the formal program. Editing a large Google Doc one paragraph at a time through the MCP API is architecturally wrong for bulk rewrites. Better approach: draft the full document locally, then import it as a single operation.

---

## Antipatterns Encountered

| Antipattern | What Happened | Lesson |
|-------------|---------------|--------|
| curl/python workarounds | Tried testing MCP servers via HTTP before they were natively available | If MCP is not available, fix config and restart. Never hack around it. |
| Synthetic test data | Attempted to create fake DOCX files with python-docx for testing | Always use real data from Google Drive. Test with production content. |
| Config file guessing | Tried 3 different files for MCP registration | Use `claude mcp add` or `.mcp.json` only. Period. |
| Secrets in tracked files | Tokens briefly in settings.json | Secrets go in `.mcp.json` (gitignored). Never elsewhere. |
| Ingest without export | Fed document content directly to RAG | Always save to disk first, then ingest from file. |
| Diagram without save | Opened in browser, not saved to repo | Always save `.drawio` to `diagrams/`. Browser is optional. |
| Pushed initial commit to main | First commit went directly to main branch | Even the very first commit should go through a branch + PR. |

---

## What Worked Well

### MCP Stack Is the Real Value

Once configured, the 6-server MCP stack is genuinely powerful:

- **workspace-mcp** (115 tools): read docs, list folders, create folders, copy files, edit documents -- all natively from Claude Code
- **open-ontologies**: loaded schema cleanly, SPARQL queries return correct results, ready for real entity data
- **local-rag**: ingestion and hybrid search both work, 222 chunks from 3 documents
- **drawio**: creates diagrams from Mermaid syntax and XML, exports work
- **github-mcp**: issues, labels, project board -- all functional
- **document-loader**: reads office formats (XLSX, PPTX, DOCX, PDF) that workspace-mcp cannot

The unified tool interface is the differentiator. One conversation can read Google Drive, query an ontology, search ingested documents, create diagrams, and manage GitHub issues. No context switching.

### Issue-Driven Workflow

Every task was traced to a GitHub issue. Branch naming followed the convention (`issue-1-mcp-setup`). Commits referenced issues. Labels were created and applied. This discipline held throughout the session despite the temptation to "just fix things quickly."

### Memory System

User preferences, project status, external references, and feedback were saved to memory. This will pay off in future sessions -- no need to re-explain the project context or user preferences.

### Ontology Schema

The minimal schema (8 classes, 7 relations) loaded without issues. It is correctly scoped -- structural facts and references only, no document text duplication. Ready for population with real entities.

---

## Skills and Agents Assessment

### Skills: Mostly Not Used Yet

| Skill | Status | Priority |
|-------|--------|----------|
| sync-library | Not built | HIGH -- no automated sync pipeline exists |
| catalog-docs | Manual only | HIGH -- manifests not updated |
| extract-links | Not used | MEDIUM -- needed for ontology population |
| update-lecture | Not applicable | LATER -- no lectures created yet |
| build-deck | Not applicable | LATER -- no slides created yet |
| diagram-refresh | Partially done | LOW -- convention established, needs automation |
| issue-from-change | Not used | MEDIUM -- needed for change detection |
| impact-check | Not used | MEDIUM -- needed for dependency analysis |

The skills exist as definitions but lack implementation. The highest priority is `sync-library` because without it, the daily cycle described in CLAUDE.md cannot run.

### Agents: Partially Validated

- **doc-editor**: Works but is slow for large rewrites. Needs a "bulk import" mode.
- **issue-manager**: Works for basic issue creation. Not tested for triage or change queue.
- **librarian**: Not properly tested. The export-then-ingest pipeline does not exist yet.
- **course-curator**: Did gap analysis work, but ontology is not populated with real entities.
- **deck-editor**: Not used. No slides created.

---

## CLAUDE.md Rule Compliance

| Rule | Followed? | Notes |
|------|-----------|-------|
| Orchestration (delegate to subagents) | Partially | Subagents did implementation, but research had to stay in main context due to permission issues |
| Roast-before-implement | Skipped | Acceptable for initial setup; must enforce for content work going forward |
| Phase gating | Partially | User approved each major phase, but gates were informal |
| No push to main | Violated once | Initial commit went to main. All subsequent work on branch. |
| Issue-driven | Yes | Every task had an issue |
| Branch naming | Yes | `issue-1-mcp-setup` convention followed |
| Document size limit (600 lines) | Not tested | V2 course plan (~49K chars) may exceed this; needs checking |
| Anti-patterns avoided | Mostly | Secrets near-miss, synthetic data rejected by user |

---

## Concrete Next Steps (Priority Order)

1. **Build sync-library pipeline**: Google Drive -> export to `catalog/exports/docs/` -> ingest to local-rag. This is the foundation for everything else.
2. **Save all raw document exports**: Every document from Google Drive must exist as a local file before ingestion.
3. **Update manifests**: `catalog/manifests/documents.yaml` should reflect all known documents with metadata.
4. **Populate ontology with real entities**: Load actual documents, lectures, and their relationships into open-ontologies.
5. **Rewrite FOS (assessment program)**: Still references old course content (expert systems, decision support). Needs V2 alignment.
6. **Review rewritten RPD**: User must verify the formal program rewrite for accuracy.
7. **Fix subagent research limitation**: Document that research stays in orchestrator; update CLAUDE.md if needed.
8. **Remove mcpServers from settings.json**: Eliminate the redundant/confusing config section.

---

## General Verdict

The system works. The MCP stack is genuinely useful and the unified interface delivers on its promise. The main pain was configuration discovery -- once that was solved, everything flowed.

The biggest gap is automation. The daily cycle (sync, catalog, extract, ingest) exists only on paper. Building the `sync-library` skill is the single most important next step because it unlocks everything downstream: change detection, auto-reingestion, manifest updates, and issue creation from changes.

The session proved the architecture is sound. Now it needs plumbing.

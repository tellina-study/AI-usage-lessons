# Improvements — Session 2 (2026-03-31)

### Test remaining 5 skills
- **Priority:** P0 (do now)
- **Effort:** M (1-3 hours)
- **Component:** `.claude/skills/` — catalog-docs, build-deck, update-lecture, diagram-refresh, issue-from-change
- **Action:** Run each skill with real data, verify output, fix any failures before merging PR #5
- **GitHub issue:** #4 (existing)

### Reorganize session 1 reflections into dated folder
- **Priority:** P1 (do this week)
- **Effort:** S (< 30 min)
- **Component:** `notes/reflections/`
- **Action:** Move the 7 loose reflection files from session 1 into `notes/reflections/2026-03-31-session-1/` folder structure matching the new convention
- **GitHub issue:** create

### Ingest exported docs into local-rag
- **Priority:** P1 (do this week)
- **Effort:** S (< 30 min)
- **Component:** `catalog/exports/docs/`, local-rag MCP
- **Action:** Run `ingest_file` for all 5 exported documents. Verify with `query_documents` that semantic search returns relevant results.
- **GitHub issue:** create

### Populate ontology with document entities
- **Priority:** P2 (do this month)
- **Effort:** M (1-3 hours)
- **Component:** `ontology/`, open-ontologies MCP
- **Action:** Create RDF entities for each document, lecture, and their relations (cites, covers, depends_on). Use onto_ingest or onto_load.
- **GitHub issue:** create

### Add "save output to file" requirement to all skills
- **Priority:** P1 (do this week)
- **Effort:** S (< 30 min)
- **Component:** `.claude/skills/*/SKILL.md`
- **Action:** Audit all 9 skills. Ensure each one that produces analysis output includes a step to write results to a specific file path. Currently some skills may only return output to conversation.
- **GitHub issue:** create

### Add pre-merge testing checklist to PR template
- **Priority:** P1 (do this week)
- **Effort:** S (< 30 min)
- **Component:** `.github/PULL_REQUEST_TEMPLATE.md`
- **Action:** Create PR template with a checklist requiring: all new skills tested, all new MCP tools verified, no untested functionality merged.
- **GitHub issue:** create

### Formalize roast step documentation
- **Priority:** P2 (do this month)
- **Effort:** S (< 30 min)
- **Component:** `workflows/`, CLAUDE.md
- **Action:** The roast-before-implement rule is in CLAUDE.md but has no detailed workflow like reflection-process.md. Create `workflows/roast-process.md` with specific questions and format.
- **GitHub issue:** create

### Test drawio and open-ontologies MCP tools
- **Priority:** P2 (do this month)
- **Effort:** M (1-3 hours)
- **Component:** drawio MCP, open-ontologies MCP
- **Action:** Neither server was used this session. Create a simple test for each: generate one diagram with drawio, load one TTL file with open-ontologies. Verify tools work before depending on them.
- **GitHub issue:** create

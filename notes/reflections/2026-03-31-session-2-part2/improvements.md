# Improvements — Session 2 Part 2 (2026-03-31)

### Switch all skills to import_to_google_doc
- **Priority:** P0 (do now)
- **Effort:** S (< 30 min)
- **Component:** `.claude/skills/update-lecture.md`, `.claude/skills/build-deck.md`, and any skill that creates Google Docs
- **Action:** Replace `create_doc` with `import_to_google_doc` as the default tool for creating Google Docs with markdown content. `create_doc` should only be used for empty documents.
- **GitHub issue:** create

### Pre-enable Google APIs in setup checklist
- **Priority:** P0 (do now)
- **Effort:** S (< 30 min)
- **Component:** `notes/decisions.md`, setup documentation
- **Action:** Add to decisions.md and any setup docs: enable Docs, Sheets, Slides, Drive, and Calendar APIs in Google Cloud Console before first use. These are not auto-enabled by OAuth.
- **GitHub issue:** create

### Update sync-library with new Drive folder IDs
- **Priority:** P1 (do this week)
- **Effort:** M (1-3 hours)
- **Component:** `.claude/skills/sync-library.md`, `catalog/manifests/`
- **Action:** Update sync-library skill to use the new 44-folder Drive structure. Update folder ID mappings so sync pulls from correct locations (lectures, seminars, exams, etc.).
- **GitHub issue:** create

### Update manifests after Drive restructure
- **Priority:** P1 (do this week)
- **Effort:** M (1-3 hours)
- **Component:** `catalog/manifests/documents.yaml`, `catalog/manifests/lectures.yaml`
- **Action:** Populate manifests with the 12 new documents and their Drive IDs, folder paths, and metadata.
- **GitHub issue:** create

### Make pyvis script read from ontology dynamically
- **Priority:** P2 (do this month)
- **Effort:** M (1-3 hours)
- **Component:** `diagrams/ontology/generate_graph.py`, `diagrams/ontology/generate_table.py`
- **Action:** Replace hardcoded nodes/edges with SPARQL queries to open-ontologies MCP. Scripts should query ontology state and generate visualization from live data.
- **GitHub issue:** create

### Add Python 3.12 compatibility note for OntoSpy
- **Priority:** P3 (backlog)
- **Effort:** S (< 30 min)
- **Component:** `notes/decisions.md`
- **Action:** Document that OntoSpy is broken on Python 3.12. If ontology visualization needs change, use pyvis or check if OntoSpy has been updated.
- **GitHub issue:** not needed — decisions.md note only

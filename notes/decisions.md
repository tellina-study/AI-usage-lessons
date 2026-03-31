# Decisions Log

## 2026-03-31 — Initial architecture

- Runtime: Claude Code only, no separate backend
- MCP stack: workspace-mcp (primary Google) + gws (fallback) + knowledge-rag + drawio-mcp + draw-mcp + github-mcp + oxigraph
- Ontology: minimal RDF with 8 entity types and 7 relation types
- Workflow: issue-driven, create-roast-revise cycle
- Priority: speed to working state over feature completeness

## 2026-03-31 — First session findings

### MCP configuration
- MCP servers register via `claude mcp add` → `.mcp.json` (NOT `.claude/settings.json`)
- `.mcp.json` contains secrets → must be gitignored
- `.claude/settings.json` is for non-secret configs only (document-loader, local-rag, drawio, open-ontologies)
- Each restart needed after config changes for MCP tools to appear

### Actual MCP stack (updated)
- workspace-mcp v3.2.0 (115 tools) — primary Google layer, OAuth with kzlevko@gmail.com
- github-mcp-server v0.32.0 (41 tools) — binary at ~/.local/bin, needs PAT
- awslabs.document-loader-mcp-server v3.2.0 (3 tools) — reads XLSX/PPTX/DOCX/PDF/images
- mcp-local-rag v1.0.0 (6 tools) — semantic search, hybrid mode
- @drawio/mcp v1.0.0 (3 tools) — Mermaid/XML/CSV diagrams
- open-ontologies v1.1.1 (43 tools) — replaces planned mcp-server-oxigraph, much richer

### Conventions discovered
- Always save raw exported docs to catalog/exports/docs/ BEFORE ingesting into RAG
- Always save .drawio files to diagrams/ — never just open in browser
- Never use curl/python workarounds for MCP — restart Claude Code for native access
- Work with real files from Google Drive, not synthetic test data
- Subagents cannot use WebSearch/WebFetch — do web research in main conversation

### Top priority: sync pipeline
- No automated Google Drive → local export → RAG ingest flow yet
- This is the #1 blocker for daily operations
- Needs: sync-library skill implementation

# Decisions Log

## 2026-03-31 — Initial architecture

- Runtime: Claude Code only, no separate backend
- MCP stack: workspace-mcp (primary Google) + gws (fallback) + knowledge-rag + drawio-mcp + draw-mcp + github-mcp + oxigraph
- Ontology: minimal RDF with 8 entity types and 7 relation types
- Workflow: issue-driven, create-roast-revise cycle
- Priority: speed to working state over feature completeness

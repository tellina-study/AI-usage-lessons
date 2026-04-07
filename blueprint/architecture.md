# System Architecture

Claude Code is the only runtime. No separate backend, no custom UI, no database server to manage. All automation runs through MCP servers, subagents, skills, and hooks.

---

## MCP Stack

| Server | Tools | Purpose | Auth |
|--------|:-----:|---------|------|
| workspace-mcp | 115 | Read/write Google Docs, Sheets, Slides, Drive, Gmail, Calendar, Tasks | Google OAuth (Desktop client) |
| github-mcp-server | 41 | Issues, PRs, branches, commits, code search | GitHub PAT (`ghp_*`) |
| open-ontologies | 43 | RDF/OWL knowledge graph: load, query (SPARQL), validate (SHACL), reason, diff | None (local binary) |
| local-rag | 6 | Semantic search over ingested documents (LanceDB + embeddings) | None |
| document-loader | 3 | Read PDF, DOCX, XLSX, PPTX, images with structured extraction | None |
| drawio | 3 | Generate diagrams from Mermaid, XML, or CSV -- opens in browser | None |

Total: ~211 tools available to the agent.

---

## Data Flows

### Google Drive Sync Flow

```
Google Drive (source of truth)
    |
    | workspace-mcp.list_drive_items
    v
File discovery (IDs, MIME types, names)
    |
    | workspace-mcp.get_doc_as_markdown    (Google Docs)
    | workspace-mcp.get_drive_file_content (uploaded DOCX)
    | workspace-mcp.get_drive_file_download_url (binary files)
    v
Save to catalog/exports/docs/{name}.md or .docx
    |
    | local-rag.ingest_file (from saved local file)
    v
LanceDB vector index (lancedb/)
    |
    | local-rag.query_documents
    v
Semantic search results
```

Key rule: ALWAYS save the raw file to `catalog/exports/docs/` BEFORE ingesting into RAG. Never pass content directly from workspace-mcp to `ingest_data` -- it creates untraceable base64 blobs.

### Knowledge Graph Flow

```
Documents in catalog/exports/
    |
    | Extract entities and relationships
    v
open-ontologies.onto_ingest (RDF triples)
    |
    | Entities: Document, Lecture, SlideDeck, Diagram, Requirement, Task, Topic
    | Relations: cites, covers, illustrates, depends_on, supersedes, tracked_by
    v
Oxigraph store (~/.open-ontologies/)
    |
    | open-ontologies.onto_query (SPARQL)
    v
Impact analysis, dependency chains, orphan detection
```

The ontology stores structural facts and references only. Never duplicate full document text in RDF.

### Diagram Flow

```
Content analysis (lecture topics, system architecture)
    |
    | Generate Mermaid or draw.io XML
    v
Write .drawio file to diagrams/{category}/{name}.drawio
    |
    | drawio.open_drawio_mermaid or open_drawio_xml (browser preview)
    v
Browser preview (optional, ephemeral)
```

The `.drawio` file in the repo IS the artifact. The browser preview is transient. There is no MCP-based export to PNG/SVG -- that requires draw.io desktop CLI (not installed).

### GitHub Issue Flow

```
Document change detected (sync-library)
    |
    | Query ontology for affected entities
    | open-ontologies.onto_query: what depends_on / cites this?
    v
Impact list (affected lectures, slides, requirements)
    |
    | github.create_issue (from template)
    v
GitHub Issue with labels, project board assignment
    |
    | Work on issue: branch, commits, PR
    v
PR merged, issue closed
```

---

## Tool Selection Rules

### Google Operations

| Need | Use | Why |
|------|-----|-----|
| Read Google Docs as markdown | workspace-mcp.get_doc_as_markdown | Best structured output |
| Quick content preview | workspace-mcp.get_drive_file_content | Plain text, smaller context |
| List folder contents | workspace-mcp.list_drive_items | Returns IDs, MIME types |
| Edit Google Docs (few changes) | workspace-mcp.modify_doc_text | Targeted find-and-replace |
| Rewrite Google Docs (bulk) | workspace-mcp.batch_update_doc or create new doc | 68-call rewrites are too slow |
| Read XLSX/PPTX with structure | document-loader.read_document | workspace-mcp flattens tables |
| Search across documents | local-rag.query_documents | Semantic + keyword hybrid search |

### GitHub Operations

| Need | Use | Why |
|------|-----|-----|
| Simple CRUD (create issue, open PR) | `gh` CLI via Bash | Faster, no MCP overhead |
| Search issues/PRs/code with filters | github-mcp search tools | Structured queries, pagination |
| Complex multi-step operations | github-mcp | Maintains state across calls |

### Ontology Operations

| Need | Use |
|------|-----|
| Load schema or instance data | open-ontologies.onto_load or onto_ingest |
| Query relationships | open-ontologies.onto_query (SPARQL) |
| Validate data constraints | open-ontologies.onto_shacl |
| Check reasoning (OWL inference) | open-ontologies.onto_reason |
| Compare schema versions | open-ontologies.onto_diff |

---

## Knowledge Retrieval Pipeline (#22)

4-tier hybrid retrieval. Skill: `/query-kb`. Start with cheapest tier, escalate as needed.

```
Query
  → Tier 1: Wiki Index (Read wiki/index.md → topic/lecture pages)   [1-3 reads, ~free]
  → Tier 2: Ontology SPARQL (onto_query for relations/chains)       [1-3 queries]
  → Tier 3: RAG Semantic Search (query_documents, EN + RU)          [1-2 queries]
  → Tier 4: Grep (exact match fallback)                             [1-2 searches]
  → Merge & deduplicate → Present with provenance
```

### Tier Selection

| Query Type | Tier | Example |
|------------|------|---------|
| Navigational | 1 (Wiki) | "What does Lecture 1 cover?" |
| Relational | 2 (Ontology) | "Which LOs fulfill PKS-3?" |
| Semantic/discovery | 3 (RAG) | "Papers on agent architectures" |
| Exact match | 4 (Grep) | "Find ПКС-3 text" |
| Cross-cutting | All | "Everything about AI agents" |

### Current Coverage (2026-04-07)

| Tier | Tool | Data | Scale |
|------|------|------|-------|
| Wiki | Read | 12 pages (10 topics, 1 lecture, 1 index) | Hundreds of pages |
| Ontology | onto_query | 352 triples, 12 topics, 8 lectures, 8 LOs | Millions of triples |
| RAG | query_documents | 61 docs, 13,712 chunks | Millions of chunks |
| Grep | Grep | All repo files | Thousands of files |

### Session Startup

Oxigraph is in-memory. At session start, load ontology:
1. `onto_load` schema.ttl
2. `onto_load` store.ttl

RAG (LanceDB) persists on disk — no startup needed.

---

## Subagent Architecture

Claude Code (orchestrator) delegates implementation to subagents via the Agent tool.

### What the orchestrator does directly
- Plan and design (issues, design docs, CLAUDE.md)
- Web research (WebSearch, WebFetch -- subagents cannot use these)
- Git operations (branch, commit, push, PR)
- MCP server setup and configuration
- System-level Bash commands

### What subagents do
- Edit Google Docs/Sheets/Slides via workspace-mcp
- Create diagrams via drawio MCP
- Perform gap analysis and structured content work
- Write files to the repo (Write, Edit tools)
- Query ontology and RAG for analysis

### Subagent limitations (discovered empirically)
- Cannot use WebSearch or WebFetch (permission denied)
- Cannot run arbitrary Bash commands (restricted)
- May enter a "death spiral" of 40+ failed tool calls before giving up
- Produce shallow output unless the prompt specifies depth, areas, and format
- Ideal scope: 2-3 related tasks, completable in under 5 minutes

---

## Repository Layout

```
blueprint/       -- this folder: portable agent setup documentation
catalog/
  exports/       -- docs/, sheets/, slides/, pdf/ (gitignored, local only)
  index/         -- knowledge-rag index data
  manifests/     -- documents.yaml, lectures.yaml, decks.yaml, diagrams.yaml
diagrams/        -- canonical .drawio files and exports
library/         -- source materials: normative/, lectures/, materials/, project/
ontology/        -- RDF schema (TTL), store (TTL), SPARQL queries
wiki/            -- compiled knowledge base (topics, lectures, index)
templates/       -- reusable templates for lectures, slides, issues, requirements
workflows/       -- routine descriptions, checklists, triage rules
notes/           -- decisions, limitations, experiments, reflections
.claude/
  agents/        -- agent role definitions (librarian, doc-editor, etc.)
  skills/        -- skill definitions (sync-library, catalog-docs, etc.)
  settings.json  -- non-secret config (committed)
.mcp.json        -- MCP server configs with secrets (gitignored)
```

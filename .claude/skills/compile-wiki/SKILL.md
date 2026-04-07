# compile-wiki

Compile and maintain the wiki knowledge base: index all sources, populate ontology, ingest into RAG, generate wiki pages.

**Current Phase: 1 (Reindex)** — update this as phases are implemented.

## Role

You are a wiki compiler agent. Your job is to ensure all knowledge sources are indexed, the ontology is populated, RAG has full coverage, and wiki pages are up-to-date. Run the steps for the CURRENT PHASE only.

## Constants

- Repo root: `/home/levko/AI-usage-lessons`
- Ontology schema: `ontology/schema.ttl`
- Ontology store: `ontology/store.ttl`
- Wiki manifest: `catalog/manifests/wiki-manifest.yaml`
- RAG tool: `mcp__local-rag__ingest_file`, `mcp__local-rag__query_documents`, `mcp__local-rag__list_files`
- Ontology tool: `mcp__open-ontologies__onto_load`, `mcp__open-ontologies__onto_query`, `mcp__open-ontologies__onto_save`
- Document loader: `mcp__document-loader__read_document`

## Source Directories (all content that should be indexed)

| Directory | Content | Format | Count |
|-----------|---------|--------|-------|
| `catalog/exports/docs/` | Google Drive exports | .md | ~16 |
| `notes/research/lecture-1/` | Lecture 1 research | .md | ~7 |
| `notes/research/` | Other research (blog, comparisons) | .md | ~15 |
| `library/papers/lecture-1/` | Downloaded PDFs | .pdf | ~15 |
| `ontology/store.ttl` | Ontology instance data | .ttl | 1 |

As lectures 2-17 are built, new directories will appear:
- `notes/research/lecture-N/` — research files per lecture
- `library/papers/lecture-N/` — papers per lecture

---

## Phase 1: Reindex (Current)

Ensure all existing content is loaded into RAG and ontology. No wiki page generation yet.

### Step 1.1: Load Ontology

Load the ontology schema and store into Oxigraph:

```
mcp__open-ontologies__onto_load(source="ontology/schema.ttl")
mcp__open-ontologies__onto_load(source="ontology/vocab.ttl")
mcp__open-ontologies__onto_load(source="ontology/store.ttl")
```

If store.ttl fails to load (syntax error), report the error line and stop. The syntax must be fixed manually before proceeding.

Verify with:
```
mcp__open-ontologies__onto_query(query="SELECT (COUNT(*) as ?count) WHERE { ?s ?p ?o }")
```
Expected: count > 0. If 0, loading failed silently.

### Step 1.2: Ingest Markdown Files into RAG

List currently indexed files:
```
mcp__local-rag__list_files()
```

Compare against source directories. For each .md file NOT already indexed:

**catalog/exports/docs/*.md:**
```
mcp__local-rag__ingest_file(file_path="/home/levko/AI-usage-lessons/catalog/exports/docs/{filename}")
```

**notes/research/lecture-1/*.md:**
```
mcp__local-rag__ingest_file(file_path="/home/levko/AI-usage-lessons/notes/research/lecture-1/{filename}")
```

**notes/research/*.md (non-lecture research):**
```
mcp__local-rag__ingest_file(file_path="/home/levko/AI-usage-lessons/notes/research/{filename}")
```

Skip files already in the index (check by filename match from list_files output).

### Step 1.3: Ingest PDFs into RAG

For each PDF in library/papers/lecture-1/:

First read the PDF to extract text:
```
mcp__document-loader__read_document(file_path="/home/levko/AI-usage-lessons/library/papers/lecture-1/{filename}.pdf")
```

Then ingest:
```
mcp__local-rag__ingest_file(file_path="/home/levko/AI-usage-lessons/library/papers/lecture-1/{filename}.pdf")
```

If ingest_file does not support PDF directly, save the extracted text as a temporary .md file and ingest that instead.

### Step 1.4: Verify

Run verification queries:

**RAG coverage:**
```
mcp__local-rag__list_files()
```
Count should be >= 38 (16 exports + 7 lecture-1 research + 15 papers).

**Ontology:**
```
mcp__open-ontologies__onto_query(query="SELECT ?type (COUNT(?s) as ?count) WHERE { ?s a ?type } GROUP BY ?type ORDER BY DESC(?count)")
```
Should show Document, Topic, and other class instance counts.

**Smoke test — Scenario 1:**
```
mcp__local-rag__query_documents(query="AI classification taxonomies", limit=5)
```
Should return results from classifications.md (previously returned 0 relevant results).

**Smoke test — Ontology:**
```
mcp__open-ontologies__onto_query(query="PREFIX aul: <https://ai-usage-lessons.local/ontology#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> SELECT ?topic ?label WHERE { ?topic a aul:Topic ; rdfs:label ?label }")
```
Should return 8+ topics.

### Step 1.5: Report

```
## Compile-Wiki Report (Phase 1: Reindex) — {date}

### Ontology
- Triples loaded: {count}
- Classes with instances: {list}
- Load errors: {any}

### RAG
- Files indexed (before): {count}
- Files indexed (after): {count}  
- New files ingested: {count}
- Ingest errors: {any}

### Smoke Tests
- RAG "classification taxonomies": {top result and score}
- Ontology topics query: {count} topics found
```

---

## Phase 2: Populate Ontology (After Phase 1 Gate)

Add missing instances to the ontology. Run Phase 1 steps first, then these.

### Step 2.1: Add Lecture Instances

For each of the 17 lectures, add to ontology via onto_ingest or direct TTL:

```turtle
aul:lec_01 a aul:Lecture ;
    rdfs:label "Lecture 1: Introduction" ;
    aul:source_url "https://docs.google.com/document/d/1UX671dOrhfQ8OgnadD_8ce4dhVJ9wDVrFqPq6p9S9uo/edit" ;
    aul:status "draft" ;
    aul:covers aul:topic_ai_fundamentals ;
    aul:updated_at "2026-04-07"^^xsd:dateTime .
```

Source for lecture-topic mapping: `catalog/exports/docs/course-structure.md`
Read this file to extract which lectures cover which topics.

### Step 2.2: Add Covers Triples

From course-structure.md, map each lecture to its primary topics. Example:
```turtle
aul:lec_01 aul:covers aul:topic_ai_fundamentals .
aul:lec_01 aul:covers aul:topic_ai_in_industry .
aul:lec_02 aul:covers aul:topic_ai_in_software .
aul:lec_03 aul:covers aul:topic_ai_in_finance .
```

### Step 2.3: Add Requirement + LearningOutcome

From `catalog/exports/docs/prog-otraslevoe-updated-formal.md`, extract:

```turtle
aul:req_pks3 a aul:Requirement ;
    rdfs:label "PKS-3: Classify and identify AI tasks" ;
    aul:source_url "..." .

aul:lo1 a aul:LearningOutcome ;
    rdfs:label "LO1: Classify AI solution types" ;
    aul:fulfills aul:req_pks3 .

aul:lec_01 aul:covers aul:lo1 .
aul:sem_05 aul:assesses aul:lo1 .
aul:sem_17 aul:assesses aul:lo1 .
```

Note: LearningOutcome class must be added to schema.ttl first (Phase 2 of ontology design).

### Step 2.4: Save and Verify

```
mcp__open-ontologies__onto_save(destination="ontology/store.ttl")
```

Verify with find_docs_for_lecture.rq:
```
mcp__open-ontologies__onto_query(query="PREFIX aul: <https://ai-usage-lessons.local/ontology#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> SELECT ?lecture ?label ?topic ?topicLabel WHERE { ?lecture a aul:Lecture ; rdfs:label ?label ; aul:covers ?topic . ?topic rdfs:label ?topicLabel }")
```
Should return 17+ rows.

---

## Phase 3: Generate Wiki Pages (After Phase 2 Gate)

Create wiki/ structure and compile index pages from source content.

### Step 3.1: Create Directory Structure

```bash
mkdir -p wiki/topics wiki/lectures wiki/documents wiki/concepts wiki/papers
```

### Step 3.2: Generate Master Index

Read all source directories and manifests. Generate `wiki/index.md`:
- List all topics with source counts
- Link to topic _index.md pages
- Link to lecture summaries
- Include compilation timestamp

Use template: `templates/wiki/topic-index.md` (if exists).

### Step 3.3: Generate Topic Index Pages

For each topic in ontology, create `wiki/topics/{slug}/_index.md`:
- List all sources belonging to this topic (from ontology belongs_to_topic + grep)
- List related lectures (from ontology covers)
- List papers (from paper manifest)
- List sub-topics if applicable

### Step 3.4: Generate Lecture Summaries

For each lecture with research notes, create `wiki/lectures/lec-NN.md`:
- Topics covered (from ontology)
- Research notes (from notes/research/lecture-N/)
- Papers (from library/papers/lecture-N/index.yaml)
- Assessment (from ontology assesses + seminar files)
- Normative requirements (from ontology fulfills)

### Step 3.5: Update Manifest

Write `catalog/manifests/wiki-manifest.yaml` with content hashes of all compiled pages.

---

## Phase 4: Full Compilation Pipeline (After Phase 3 Gate)

Full 3-pass pipeline with incremental compilation.

### Pass 1: Catalog
- Scan all source directories for new/changed/removed files
- Compare content hashes against wiki-manifest.yaml
- Output: change list

### Pass 2: Compile
- For changed sources: regenerate affected wiki pages
- Auto-classify papers by topic
- Extract cross-cutting concepts (patterns spanning 3+ topics)
- Update ontology with new instances

### Pass 3: Index
- Regenerate all index pages (master + topic)
- Update cross-links between wiki pages
- Ingest new/changed content into RAG
- Save updated ontology
- Update wiki-manifest.yaml
- Print compilation report

### Incremental Rule
Only recompile pages whose source files changed (by content hash). Full recompile on schema or template changes.

---

## Error Handling

- If ontology load fails: report error line, stop. Do not proceed with broken ontology.
- If RAG ingest fails for a file: log error, continue with remaining files. Report failures at end.
- If PDF extraction fails: log error, skip file. Note in report.
- If a wiki page would exceed 600 lines: split into sub-pages automatically.
- If any step fails: do NOT skip silently. Report all errors in the final report.

## Phase: Post-Compile (Mechanical — run after any content phase)

This phase handles all mechanical indexing operations. Run it after any content changes.

### Step 1: Load Ontology
```
mcp__open-ontologies__onto_load: path = /home/levko/AI-usage-lessons/ontology/schema.ttl
mcp__open-ontologies__onto_load: path = /home/levko/AI-usage-lessons/ontology/store.ttl
```
Verify: `SELECT (COUNT(*) as ?count) WHERE { ?s ?p ?o }` should return > 300.

### Step 2: Ingest Wiki Pages into RAG
For each .md file in wiki/:
```
mcp__local-rag__ingest_file: filePath = /home/levko/AI-usage-lessons/wiki/{path}
```
Files to ingest: wiki/index.md, wiki/lectures/*.md, wiki/topics/*/_index.md

### Step 3: Verify RAG Coverage
```
mcp__local-rag__status
```
Check documentCount >= 60 and chunkCount >= 13000.

### Step 4: Validate Wiki Links
Run `grep -r '\[\[' wiki/ --include='*.md'` — should return empty (no unresolved links).
Check all relative markdown links resolve to existing files.

### Step 5: Report
Print summary:
- Ontology: X triples loaded
- RAG: X documents, X chunks
- Wiki links: all valid / N broken

---

## When to Run

- **After /sync-library:** new Drive exports need indexing
- **After /update-lecture:** new research notes and papers need indexing
- **After manual paper import:** new PDFs need ingestion
- **Daily cycle:** run as part of the daily sync (step 2 after sync-library)
- **On demand:** user runs /compile-wiki directly

## Phase Advancement

Update "Current Phase" at the top of this file when:
- Phase 1 -> 2: after ontology store.ttl is fixed AND Phase 1 verification passes
- Phase 2 -> 3: after ontology has 17 lectures + covers triples + requirements
- Phase 3 -> 4: after wiki/index.md and topic pages exist and are useful

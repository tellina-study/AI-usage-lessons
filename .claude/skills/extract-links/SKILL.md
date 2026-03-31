# extract-links

Extract cross-references and relationships between documents and create RDF triples in the ontology.

## Role

You are a librarian agent. Your job is to read cataloged documents, identify cross-references and relationships between them, and record these as RDF triples (cites, depends_on, covers, belongs_to_topic) in the ontology.

## Constants

- Manifest: `/home/levko/AI-usage-lessons/catalog/manifests/documents.yaml`
- Lectures manifest: `/home/levko/AI-usage-lessons/catalog/manifests/lectures.yaml`
- Export directory: `/home/levko/AI-usage-lessons/catalog/exports/docs/`
- Ontology prefix: `aul: <https://ai-usage-lessons.local/ontology#>`
- Schema: `/home/levko/AI-usage-lessons/ontology/schema.ttl`

## Available relations (from schema.ttl)

- `aul:cites` — source cites target document/section
- `aul:covers` — lecture or deck covers a topic or requirement
- `aul:depends_on` — entity depends on another entity
- `aul:illustrates` — diagram illustrates a document, lecture, or concept
- `aul:supersedes` — newer version supersedes older
- `aul:belongs_to_topic` — entity belongs to a topic

## Execution

### Step 1: Load document inventory

Read `/home/levko/AI-usage-lessons/catalog/manifests/documents.yaml` using the Read tool.
Build a lookup table: { document_id => { title, local_path, source_url, slug } }

### Step 2: Read and analyze each document

For each document in the manifest that has a `local_path`:

**Markdown files**: Read using the Read tool.

**DOCX/PDF files**: Use document-loader:
```
mcp__document-loader__read_document(uri="file:///home/levko/AI-usage-lessons/<local_path>")
```

### Step 3: Identify cross-references

For each document, search its content for:

1. **Explicit citations**: References to other documents by name or title (e.g., "see Рабочая программа", "according to ФОС")
2. **URL references**: Links to other Google Docs/Sheets/Slides in the same Drive folder
3. **Topic overlap**: Documents covering the same topics (AI applications, specific industries, etc.)
4. **Dependency patterns**: Prerequisites, "based on", "in accordance with" phrases
5. **Supersession**: "replaces", "new version of", "V2" references

Also use RAG to find semantically related documents:
```
mcp__local-rag__query_documents(query="<document title or key topic>", limit=5)
```

Review RAG results to identify documents that cover overlapping topics.

### Step 4: Build relationship list

For each identified relationship, record:
- source entity slug (e.g., `doc_ai_v_raznyh_industriyah`)
- target entity slug (e.g., `doc_prog_otraslevoe_primenenie_AI`)
- relation type: `cites`, `depends_on`, `covers`, `supersedes`, `belongs_to_topic`
- evidence: brief quote or reason

### Step 5: Create Topic entities if needed

If topics are referenced but not yet in the ontology, create them:
```
mcp__open-ontologies__onto_load(
  data="@prefix aul: <https://ai-usage-lessons.local/ontology#> .\n\naul:topic_ai_in_industry a aul:Topic ;\n    rdfs:label \"AI in Industry\" .",
  format="turtle"
)
```

### Step 6: Load relationship triples into ontology

For each relationship, load the triple:

```
mcp__open-ontologies__onto_load(
  data="@prefix aul: <https://ai-usage-lessons.local/ontology#> .\n\naul:doc_ai_v_raznyh_industriyah aul:supersedes aul:doc_ai_v_tsikle_sozdaniya_po .\naul:doc_ai_v_raznyh_industriyah aul:depends_on aul:doc_prog_otraslevoe_primenenie_AI .",
  format="turtle"
)
```

Batch related triples together in a single `onto_load` call when possible to reduce round trips.

### Step 7: Verify loaded triples

Query the ontology to verify the triples were loaded:
```
mcp__open-ontologies__onto_query(
  query="PREFIX aul: <https://ai-usage-lessons.local/ontology#>\nSELECT ?s ?p ?o WHERE {\n  ?s ?p ?o .\n  FILTER(?p IN (aul:cites, aul:depends_on, aul:covers, aul:supersedes, aul:belongs_to_topic))\n}\nORDER BY ?s ?p"
)
```

### Step 8: Report

Print a summary:

```
## Link Extraction Report — <date>

### New relationships found
| Source | Relation | Target | Evidence |
|--------|----------|--------|----------|
| doc_ai_v_raznyh_industriyah | supersedes | doc_ai_v_tsikle_sozdaniya_po | "V2 course plan" |
| ... | ... | ... | ... |

### Topics created
- topic_ai_in_industry
- ...

### Statistics
- Documents analyzed: X
- New relationships: Y
- New topics: Z

### Errors
- <any errors>
```

# catalog-docs

Catalog exported documents into structured manifests and create RDF triples in the ontology.

## Role

You are a librarian agent. Your job is to scan the local catalog exports directory for files not yet recorded in the manifests, extract metadata, update manifests, and create corresponding RDF entities in the ontology via the open-ontologies MCP server.

## Constants

- Export directory: `/home/levko/AI-usage-lessons/catalog/exports/docs/`
- Manifests directory: `/home/levko/AI-usage-lessons/catalog/manifests/`
- Manifest files: `documents.yaml`, `lectures.yaml`, `decks.yaml`, `diagrams.yaml`
- Ontology prefix: `aul: <https://ai-usage-lessons.local/ontology#>`
- Schema reference: `/home/levko/AI-usage-lessons/ontology/schema.ttl`

## Execution

### Step 1: Scan exports directory

Use Bash to list all files in the export directories:
```bash
ls -la /home/levko/AI-usage-lessons/catalog/exports/docs/
```

Also check for slides, sheets, and diagram exports if they exist:
```bash
ls -la /home/levko/AI-usage-lessons/catalog/exports/slides/ 2>/dev/null
ls -la /home/levko/AI-usage-lessons/catalog/exports/sheets/ 2>/dev/null
ls -la /home/levko/AI-usage-lessons/catalog/exports/pdf/ 2>/dev/null
```

### Step 2: Read current manifests

Read all four manifest files using the Read tool:
- `/home/levko/AI-usage-lessons/catalog/manifests/documents.yaml`
- `/home/levko/AI-usage-lessons/catalog/manifests/lectures.yaml`
- `/home/levko/AI-usage-lessons/catalog/manifests/decks.yaml`
- `/home/levko/AI-usage-lessons/catalog/manifests/diagrams.yaml`

### Step 3: Identify uncataloged files

Compare the file list from Step 1 with entries in manifests (match by `local_path` field).
Build a list of files that exist on disk but are NOT in any manifest.

### Step 4: Extract metadata from uncataloged files

For each uncataloged file:

**Markdown files (.md)**:
Read the file using the Read tool (first 50 lines). Extract:
- `title`: first H1 heading, or filename if no heading
- `type`: infer from content (google-doc, lecture-notes, reference)
- `format`: markdown

**DOCX files (.docx)**:
```
mcp__document-loader__read_document(uri="file:///home/levko/AI-usage-lessons/catalog/exports/docs/<filename>")
```
Extract title from document metadata or first heading.

**PDF files (.pdf)**:
```
mcp__document-loader__read_document(uri="file:///home/levko/AI-usage-lessons/catalog/exports/pdf/<filename>")
```

**PPTX files (.pptx)**:
```
mcp__document-loader__extract_slides_as_images(uri="file:///home/levko/AI-usage-lessons/catalog/exports/slides/<filename>")
```

### Step 5: Update manifests

Add new entries to the appropriate manifest file using the Write tool.

For documents, add to `documents.yaml`:
```yaml
  - id: <generate-slug-from-filename>
    title: "<extracted title>"
    type: <inferred type>
    source_url: null  # local-only files have no source URL
    local_path: "catalog/exports/docs/<filename>"
    format: <markdown|docx|pdf>
    exported_at: "<today's date YYYY-MM-DD>"
```

Preserve all existing entries. Only append new ones.

### Step 6: Create RDF triples in ontology

For each newly cataloged document, load RDF triples into the ontology:

```
mcp__open-ontologies__onto_load(
  data="@prefix aul: <https://ai-usage-lessons.local/ontology#> .\n@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\naul:<entity-slug> a aul:Document ;\n    aul:source_system \"local\" ;\n    aul:source_url \"<source_url or local path>\" ;\n    aul:status \"active\" ;\n    aul:owner \"kzlevko@gmail.com\" ;\n    aul:updated_at \"<today ISO datetime>\"^^xsd:dateTime .",
  format="turtle"
)
```

Entity slug rules:
- Use filename without extension
- Replace spaces and special characters with underscores
- Prefix with `doc_` for documents, `lec_` for lectures, `deck_` for decks, `diag_` for diagrams

Example for a document `ai-v-raznyh-industriyah.md`:
```
mcp__open-ontologies__onto_load(
  data="@prefix aul: <https://ai-usage-lessons.local/ontology#> .\n@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\naul:doc_ai_v_raznyh_industriyah a aul:Document ;\n    aul:source_system \"google_drive\" ;\n    aul:source_url \"https://docs.google.com/document/d/1k0ASel9hqLeBhtaDjS8k83Kpf640WFe8lln_MaV-OFY/edit\" ;\n    aul:status \"active\" ;\n    aul:owner \"kzlevko@gmail.com\" ;\n    aul:updated_at \"2026-03-31T00:00:00\"^^xsd:dateTime .",
  format="turtle"
)
```

### Step 7: Report

Print a summary:

```
## Catalog Report — <date>

### Newly cataloged
| File | Title | Type | Manifest |
|------|-------|------|----------|
| ... | ... | ... | documents.yaml |

### Already cataloged (skipped)
- <count> files already in manifests

### RDF triples created
- <count> new Document entities loaded into ontology

### Errors
- <any errors>
```

### Step 8: Trigger compile-wiki

After cataloging new documents, remind the user to run `/compile-wiki` to ingest newly cataloged files into RAG and update wiki indexes with the new content.

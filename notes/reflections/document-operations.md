# Document Operations Analysis (First Session, 2026-03-31)

Detailed breakdown of every document reading, exporting, saving, and ingestion operation performed during the first session. This is the operational reference for building the `sync-library` skill.

---

## Google Drive Document Discovery

### What Happened

Used `list_drive_items` with `folder_id` to enumerate the root working folder. Found 3 items: 1 subfolder and 2 Google Docs. Then listed the subfolder and found 4 items: 1 Google Doc, 1 PNG screenshot, and 2 uploaded DOCX files. Total: 7 files across 2 levels of hierarchy.

### Assessment

Discovery worked cleanly with no issues. The `list_drive_items` tool returns file names, MIME types, and IDs in a single call per folder. Two calls were sufficient to map the entire working folder.

### Implications for sync-library

- Recursive folder traversal is straightforward -- just call `list_drive_items` per folder
- MIME type reliably distinguishes Google Docs (`application/vnd.google-apps.document`) from uploaded files (`application/vnd.openxmlformats-officedocument.*`) from images (`image/png`)
- The tool does not return file modification timestamps, which means change detection cannot rely on Drive metadata alone. This is a gap that needs investigation -- either the tool has a parameter we did not use, or we need `search_drive_files` with date filters, or we track last-sync timestamps locally in the manifest.

---

## Reading Google Docs

### get_drive_file_content

Read both Google Docs successfully. Full text was extracted as plain text. This is the "quick read" method -- useful for previewing content or extracting text for analysis. Tables are flattened to text, formatting is lost, but content is complete.

### get_doc_as_markdown

Exported both Google Docs as markdown:

- "AI v raznykh industriyakh" (V2 course plan): ~49K characters. Contains a detailed 14-lesson plan with timing, learning outcomes, notes, and competency tables.
- "AI v tsikle sozdaniya PO" (V1 course plan): ~52K characters. Similar structure with different content focus.

Markdown export handles tables well -- they come through as proper markdown tables. Some formatting nuances are lost (font styles, cell colors, merged cells) but the structural content is preserved accurately. For a knowledge management system that cares about content over presentation, markdown is the right export format for Google Docs.

### Context Window Impact

This is where things get dangerous. A single 50K-character document consumes a significant chunk of the context window. Reading both docs in a single session (~100K chars of raw content) plus the ongoing conversation, tool calls, and MCP responses left limited room for actual work.

Large responses triggered Claude Code's persistence mechanism -- output above ~2KB was saved to disk with only a preview shown in conversation. This is helpful but means the orchestrator cannot "see" the full document content after reading it. If analysis requires the full text, it must happen in the same turn as the read, or the content must be re-read.

### Lessons

- **Never read large documents "just to see what's in them."** Have a specific question or extraction goal before calling get_doc_as_markdown.
- **Prefer get_drive_file_content for triage.** It returns plain text which is smaller and sufficient for deciding whether a full markdown export is needed.
- **For sync-library: read and immediately write to disk.** Do not hold document content in context longer than necessary. Read -> save -> move on.

---

## Reading DOCX Files

### What Happened

Used `get_drive_file_content` on both uploaded DOCX files (prog-otraslevoe.docx and fos-otraslevoe.docx). The tool handles Microsoft Office files uploaded to Drive by unzipping and parsing the XML internally. Full text was extracted including table content.

### Assessment

This worked perfectly and with no special handling required. The caller does not need to know whether a file is a native Google Doc or an uploaded DOCX -- `get_drive_file_content` abstracts this away.

Table formatting is flattened to plain text (no markdown table structure), which is less useful than the markdown export of native Google Docs. For DOCX files that are table-heavy (like formal academic programs), the `document-loader` MCP server's `read_document` tool might produce better structured output since it is specifically designed for office format parsing.

### Comparison: workspace-mcp vs document-loader for DOCX

| Aspect | workspace-mcp (get_drive_file_content) | document-loader (read_document) |
|--------|---------------------------------------|--------------------------------|
| Source | Google Drive (by file ID) | Local file path |
| Tables | Flattened to plain text | Structured extraction |
| Images | Not extracted | Can extract embedded images |
| Requires download | No | Yes -- file must be on disk |
| Best for | Quick content preview | Detailed structured extraction |

The implication for the pipeline is clear: download DOCX to disk first, then use `document-loader` for high-fidelity extraction if needed. For simple text content, `get_drive_file_content` is faster and does not require a download step.

---

## Reading PNG

### What Happened

The screenshot PNG in the Drive subfolder was never read. It was discovered during `list_drive_items` but no read operation was attempted.

### Missed Opportunity

The `document-loader` MCP server has a `read_image` tool that could have been used to examine the image. Additionally, `get_drive_file_download_url` could have downloaded it to disk for local viewing. Neither was tried.

This is a gap in the exploration -- we do not know whether image reading works end-to-end in this stack. It should be tested early because course materials will contain diagrams, screenshots, and figures that need to be cataloged and potentially described for accessibility or ontology purposes.

### Action Item

Test the full image pipeline: `get_drive_file_download_url` -> download to `catalog/exports/docs/` -> `read_image` for content description. Add to the next session's task list.

---

## Export to PDF

### What Happened

Attempted `export_doc_to_pdf` on a Google Doc. The tool created a PDF file in Google Drive (in the root, not in the working folder). It does not have a `save_path` parameter and does not download to the local filesystem.

### Assessment

This tool is designed for Google Drive workflows (e.g., creating a PDF copy in Drive for sharing), not for local export. It is the wrong tool for the sync-library pipeline.

For local PDF export, the correct approach would be:
1. `get_drive_file_download_url` with `mimeType=application/pdf` for Google Docs (if the API supports export MIME types)
2. Or: export as markdown locally, then convert to PDF with a local tool
3. Or: accept that PDFs are not needed locally if markdown captures the content

The PDF that was created in Drive root is an orphan artifact that should be cleaned up.

### Lesson

Understand tool semantics before calling. "export_doc_to_pdf" sounds like it exports to disk, but it exports to Drive. Read tool descriptions carefully -- the workspace-mcp tool descriptions do specify this behavior.

---

## Saving Documents Locally

### What Happened -- The Critical Failure

This was the single biggest workflow mistake of the session. Documents were read from Google Drive and their content was passed directly to RAG ingestion without first saving the raw content to local files.

The timeline:
1. Before MCP restart: one DOCX (fos-otraslevoe) was downloaded via `get_drive_file_download_url` + curl to a local path. This was the correct approach.
2. After MCP restart: the remaining documents were read via `get_doc_as_markdown` and `get_drive_file_content`, and their content was passed directly to `ingest_data` as strings. No local files were created.

The user explicitly flagged this: "where raw docs before ingestion? why them not saved?"

### Why This Matters

Without local files in `catalog/exports/docs/`:

- **No version tracking.** Cannot diff current Drive content against previously exported content to detect changes.
- **No reproducible ingestion.** If the RAG index needs rebuilding, must re-read everything from Drive instead of re-ingesting from local files.
- **No offline access.** Content is only available via live MCP connection to Google Drive.
- **Violated the architecture.** `catalog/exports/` exists specifically for this purpose -- it was designed into the repo layout from the start and then ignored.
- **Manifest disconnection.** `catalog/manifests/documents.yaml` cannot reference files that do not exist on disk.

### The Correct Flow

```
Google Drive
    |
    v
list_drive_items (discover)
    |
    v
get_doc_as_markdown / get_drive_file_download_url (read/download)
    |
    v
Write to catalog/exports/docs/{name}.md or .docx  <-- THIS WAS SKIPPED
    |
    v
ingest_file from local path
    |
    v
Update catalog/manifests/documents.yaml
```

Every step after "discover" was done, but the critical "write to disk" step was skipped for 4 out of 5 documents. This is the most important thing for `sync-library` to get right.

---

## RAG Ingestion

### What Happened

Three documents were ingested into the local-rag system:

| Document | Method | Chunks | Source |
|----------|--------|--------|--------|
| fos-otraslevoe.docx | `ingest_file` (from downloaded file) | 196 | Local file |
| AI v raznykh industriyakh (V2 plan) | `ingest_data` (from string) | 18 | MCP string |
| AI v tsikle sozdaniya PO (V1 plan) | `ingest_data` (from string) | 8 | MCP string |

Total: 222 chunks. Hybrid search mode was enabled automatically.

### ingest_file vs ingest_data

`ingest_file` is the correct method -- it takes a local file path, handles format-specific parsing, and creates a clear provenance record linking the ingested content to a file on disk.

`ingest_data` takes a raw string and stores it in `lancedb/raw-data/` as a base64-named file. This creates several problems:
- File names are not human-readable (e.g., `QUkg0LIg0YDQsNC3...`)
- No connection between the ingested data and any file in `catalog/exports/`
- Cannot re-ingest selectively -- must re-read from Drive to get the content again
- The raw-data directory becomes an opaque blob store instead of a traceable archive

### Query Test

A test query returned relevant results with similarity scores in the 0.19-0.32 range. The results were contextually appropriate, confirming that the ingestion and search pipeline works. The scores seem low in absolute terms but this is typical for hybrid search systems -- relevance ranking matters more than absolute score values.

### Manifest Gap

After ingestion, `catalog/manifests/documents.yaml` was not updated. This means there is no single source of truth listing what has been ingested, when, from where, and with what parameters. The manifest should record:

```yaml
- name: "fos-otraslevoe"
  source_type: docx
  drive_id: "1abc..."
  local_path: "catalog/exports/docs/fos-otraslevoe.docx"
  ingested_at: "2026-03-31T..."
  chunks: 196
  rag_status: ingested
```

Without this, the system cannot answer basic questions like "is this document already ingested?" or "when was it last synced?"

---

## Formal Program Editing via MCP

### What Happened

A subagent (doc-editor) rewrote the formal academic program (RPD) in Google Docs using workspace-mcp's `modify_doc_text` tool. The document was a copy of the original, so the source was preserved.

The editing process:
1. `inspect_doc_structure` -- understood the document layout (sections, tables, headings)
2. `modify_doc_text` x 68 calls -- find-and-replace operations to rewrite competencies, module descriptions, content lists, literature references, and software requirements

Total time: approximately 47 minutes for a single document rewrite.

### Assessment

It worked, but it was painfully slow. Each `modify_doc_text` call does a single find-and-replace operation on the document text. For a document that needed near-total rewriting, this meant 68 sequential API calls, each with MCP round-trip overhead.

### Structural Challenges

- **Table editing is fragile.** Text inside tables must be matched exactly, including any whitespace or formatting artifacts. A mismatch means the replacement silently fails or targets the wrong text.
- **No bulk operations.** There is no "replace entire section" tool. Every paragraph, every table cell is a separate operation.
- **No preview.** Cannot see the result until all operations complete. If operation #45 corrupts the document, operations #46-68 may compound the damage.

### Better Approaches for Future Bulk Rewrites

1. **Draft locally, import once.** Write the entire document content as a local markdown or text file, then use `import_to_google_doc` or `create_doc` + `batch_update_doc` to create the final document in a single operation. This would reduce 68 calls to 1-2 calls.

2. **batch_update_doc.** The workspace-mcp has a `batch_update_doc` tool that accepts multiple operations in a single call. This was not used but should be the default for multi-edit scenarios. It would reduce round trips significantly.

3. **Replace rather than modify.** For near-total rewrites, creating a new document from scratch is faster than modifying an existing one paragraph by paragraph. Copy the document for backup, delete the content of the copy, insert new content.

### Lesson

The editing approach must match the scale of changes. For a few targeted edits, `modify_doc_text` is fine. For rewriting 80%+ of a document, it is the wrong tool. Use bulk creation/import instead.

---

## Context Window Impact -- Detailed Analysis

### Problem Statement

Document-heavy operations consume enormous context. In the first session, reading 5 documents in parallel (2 Google Docs as markdown + 2 DOCX files + the formal program for editing) created severe context pressure.

### Measurements

| Document | Approximate Size | Impact |
|----------|-----------------|--------|
| V2 course plan (markdown) | ~49K chars | Major |
| V1 course plan (markdown) | ~52K chars | Major |
| prog-otraslevoe.docx (text) | ~15K chars | Moderate |
| fos-otraslevoe.docx (text) | ~20K chars | Moderate |
| Formal program (for editing) | ~25K chars | Moderate |

Combined: ~161K characters of raw document content, plus all the tool call overhead, conversation history, and system instructions.

### Mitigation Strategies

1. **Read-and-save pattern.** Read a document, immediately write it to disk, then release the context. Do not hold multiple large documents in memory simultaneously.

2. **Targeted reads.** Use `get_drive_file_content` (plain text, smaller) for triage. Only use `get_doc_as_markdown` (larger, richer) when the markdown structure is actually needed.

3. **Subagent isolation.** Each document operation should be delegated to a subagent that handles one document at a time. The subagent's context is independent of the orchestrator's context.

4. **Chunked processing.** For very large documents, consider reading specific sections rather than the entire document. The `inspect_doc_structure` tool can identify sections, and targeted reads can extract only what is needed.

5. **Manifest-driven skipping.** If a document has not changed since last sync (per the manifest), skip reading it entirely. This requires the manifest to exist and be maintained -- another reason why the manifest gap must be fixed.

---

## Summary: What Should Have Happened

The ideal document operations flow for the first session, in retrospect:

1. `list_drive_items` on root folder and all subfolders -- discover all files with IDs and MIME types
2. For each Google Doc: `get_doc_as_markdown` -> `Write` to `catalog/exports/docs/{name}.md`
3. For each uploaded DOCX: `get_drive_file_download_url` -> download to `catalog/exports/docs/{name}.docx`
4. For each PNG/image: `get_drive_file_download_url` -> download to `catalog/exports/docs/{name}.png`
5. For each saved file: `ingest_file` from the local disk path (not `ingest_data` from strings)
6. Update `catalog/manifests/documents.yaml` with file metadata, timestamps, chunk counts
7. Only then proceed to content analysis and editing

Steps 2-6 are exactly what the `sync-library` skill should automate. The first session proved that each individual step works -- the failure was in not executing them in the right order and not persisting intermediate results.

---

## Findings for decisions.md

The following should be added to `notes/decisions.md`:

- **Always save to disk before ingesting.** Never pass document content directly to `ingest_data`. Download or export to `catalog/exports/` first, then use `ingest_file`.
- **Use `ingest_file`, not `ingest_data`.** The file-based method creates traceable provenance. The string-based method creates opaque base64 blobs.
- **Bulk rewrites need bulk tools.** For rewriting >50% of a Google Doc, use `create_doc` + `batch_update_doc` or `import_to_google_doc` instead of repeated `modify_doc_text` calls.
- **export_doc_to_pdf exports to Drive, not to disk.** Do not use it for local file saving.
- **Read documents with intent.** Never read a large document without a specific goal. Use plain text preview first, full markdown only when structure matters.
- **Manifest must be updated after every sync.** No ingestion is complete until `catalog/manifests/documents.yaml` reflects the new state.

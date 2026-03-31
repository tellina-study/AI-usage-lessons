# sync-library

Synchronize a Google Drive working folder with the local catalog, exporting new and changed files for indexing.

## When to Use

- At the start of every daily cycle
- When notified of a document change in Google Drive
- When a GitHub Issue requests a manual re-sync

## Inputs

| Input | Source | Example |
|-------|--------|---------|
| Drive folder ID | Configuration | `{{DRIVE_FOLDER_ID}}` |
| Current manifest | `catalog/manifests/documents.yaml` | YAML file with last-sync state |
| Reference issue | GitHub Issues | `#{{ISSUE_NUMBER}}` |

## Steps

1. **List remote files**
   - Use `workspace-mcp list_drive_items` with folder ID `{{DRIVE_FOLDER_ID}}`
   - Collect: file ID, name, MIME type, modified time

2. **Load current manifest**
   - Read `catalog/manifests/documents.yaml`
   - Build a map of `file_id -> last_synced_at`

3. **Diff remote vs. local**
   - New files: present in Drive but not in manifest
   - Changed files: Drive `modifiedTime` > manifest `last_synced_at`
   - Deleted files: present in manifest but not in Drive

4. **Export new/changed files**
   - Google Docs -> `catalog/exports/docs/` (as markdown via `get_doc_as_markdown`, or DOCX via gws)
   - Google Sheets -> `catalog/exports/sheets/` (as XLSX via gws)
   - Google Slides -> `catalog/exports/slides/` (as PPTX via gws)
   - PDFs and other files -> `catalog/exports/pdf/` (download via `get_drive_file_content`)

5. **Index new exports**
   - Use `local-rag ingest_file` for each new or changed export
   - Verify ingestion with `local-rag list_files`

6. **Update manifest**
   - Add entries for new files
   - Update `last_synced_at` for changed files
   - Mark deleted files (or remove entries, per policy)
   - Set `sync_timestamp` to current time
   - Write updated `catalog/manifests/documents.yaml`

7. **Report results**
   - Comment on the reference GitHub Issue with:
     - Files added: count and names
     - Files updated: count and names
     - Files removed: count and names
     - Errors: any failures with file IDs
   - If changes were found, note that downstream skills (catalog-docs, issue-from-change) should run

## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Exported files | `catalog/exports/{docs,sheets,slides,pdf}/` | DOCX, XLSX, PPTX, PDF, MD |
| Updated manifest | `catalog/manifests/documents.yaml` | YAML |
| RAG index updates | `catalog/index/` | local-rag internal |
| Issue comment | GitHub Issue `#{{ISSUE_NUMBER}}` | Markdown |

## Verification

- [ ] `catalog/manifests/documents.yaml` has a `sync_timestamp` newer than before
- [ ] Every file listed in Drive has a corresponding manifest entry
- [ ] Every new/changed file has an export in `catalog/exports/`
- [ ] `local-rag list_files` includes all exported files
- [ ] Reference issue has a sync report comment

## Configuration Placeholders

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{{DRIVE_FOLDER_ID}}` | Google Drive folder ID to sync | `1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am` |
| `{{ISSUE_NUMBER}}` | GitHub Issue tracking this sync run | `42` |
| `{{GITHUB_OWNER}}` | GitHub repository owner | `tellina-study` |
| `{{GITHUB_REPO}}` | GitHub repository name | `AI-usage-lessons` |

## Error Handling

- If a single file export fails, log the error and continue with remaining files
- If workspace-mcp is unavailable, retry once, then fall back to gws
- If local-rag ingestion fails, the export is still valid -- log and create a separate issue
- Never leave the manifest in a partially updated state -- write atomically after all exports complete

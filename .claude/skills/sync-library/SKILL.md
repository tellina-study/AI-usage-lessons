# sync-library

Synchronize Google Drive working folder with local catalog exports.

## Role

You are a librarian agent. Your job is to pull all documents from the Google Drive working folder, compare them against the local manifest, export new or changed files, update the manifest, and ingest into the local RAG index.

## Constants

- Google account: kzlevko@gmail.com
- Root folder ID: `1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am`
- 00-course: `1sHXoLaIqCpBRv1IaLjS6lNtBdwI5cPc0`
- 01-formal: `1-sQ7H1CBNWaHvQIDE8TLCwVX2ilEeb0p`
- 02-lectures: `16osAMJ9y67Yem9T6fK6yDv1fXF8BGLEZ`
- 03-seminars: `1AZhb5q-yODrIJEnQBN8S1KJI0bby588J`
- 04-resources: `1yDZrw9CcGtGljNGZ-QByyoUGIMVr9Tc4`
- archive: `1rZkywX5DufGJaf1htCa1Oa_zCKmUgKMT`
- Manifest path: `/home/levko/AI-usage-lessons/catalog/manifests/documents.yaml`
- Export directory: `/home/levko/AI-usage-lessons/catalog/exports/docs/`

## Execution

### Step 1: List Drive contents

Call `mcp__workspace-mcp__list_drive_items` for each folder:

```
mcp__workspace-mcp__list_drive_items(folder_id="1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am")
```

Then list subfolders:
```
mcp__workspace-mcp__list_drive_items(folder_id="1U74-dCQLq1Zz2GldV6p-v07WnT3mWCxg")
mcp__workspace-mcp__list_drive_items(folder_id="1-sQ7H1CBNWaHvQIDE8TLCwVX2ilEeb0p")
```

Collect all files with their: id, name, mimeType, modifiedTime.

### Step 2: Compare with manifest

Read `/home/levko/AI-usage-lessons/catalog/manifests/documents.yaml` using the Read tool.

For each file from Drive:
- If the file ID is NOT in the manifest => mark as NEW
- If the file ID IS in the manifest but modifiedTime is newer than `exported_at` => mark as CHANGED
- Otherwise => mark as UNCHANGED

### Step 3: Export new/changed files

For each NEW or CHANGED file, export based on mimeType:

**Google Docs** (mimeType `application/vnd.google-apps.document`):
```
mcp__workspace-mcp__get_doc_as_markdown(document_id="<FILE_ID>")
```
Save the result to `/home/levko/AI-usage-lessons/catalog/exports/docs/<slugified-name>.md` using the Write tool.
Slugify rule: lowercase, replace spaces/special chars with hyphens, transliterate Cyrillic to Latin.

**DOCX files** (mimeType `application/vnd.openxmlformats-officedocument.wordprocessingml.document`):
```
mcp__workspace-mcp__get_drive_file_download_url(file_id="<FILE_ID>")
```
Then download via Bash: `curl -L "<download_url>" -o /home/levko/AI-usage-lessons/catalog/exports/docs/<slugified-name>.docx`

**XLSX/PPTX/PDF/Images**: Same pattern — get download URL, then curl to the appropriate export path.

**Google Sheets** (mimeType `application/vnd.google-apps.spreadsheet`):
```
mcp__workspace-mcp__get_spreadsheet_info(spreadsheet_id="<FILE_ID>")
```
Export sheet data for reference. Save as `.yaml` or `.md` summary.

**Google Slides** (mimeType `application/vnd.google-apps.presentation`):
```
mcp__workspace-mcp__get_presentation(presentation_id="<FILE_ID>")
```
Save slide text content as `.md` summary.

### Step 4: Update manifest

Update `/home/levko/AI-usage-lessons/catalog/manifests/documents.yaml` using the Write tool.

For each new file, add an entry:
```yaml
  - id: <google_drive_file_id>
    title: "<original file name>"
    type: <google-doc|docx-uploaded|xlsx-uploaded|image|pdf>
    source_url: "https://docs.google.com/document/d/<id>/edit"  # or drive link for non-Docs
    local_path: "catalog/exports/docs/<slugified-name>.<ext>"
    format: <markdown|docx|xlsx|pdf|png>
    exported_at: "<today's date YYYY-MM-DD>"
```

For changed files, update the `exported_at` field.

### Step 5: Ingest into RAG

For each new or changed file that was exported as text-readable format (md, docx, pdf):
```
mcp__local-rag__ingest_file(file_path="/home/levko/AI-usage-lessons/catalog/exports/docs/<filename>")
```

### Step 6: Report

Print a summary table:

```
## Sync Report — <date>

| Status   | File                          | Action         |
|----------|-------------------------------|----------------|
| NEW      | <filename>                    | Exported + RAG |
| CHANGED  | <filename>                    | Re-exported    |
| UNCHANGED| <filename>                    | Skipped        |

Total: X new, Y changed, Z unchanged, E errors
```

Report any errors encountered during export or ingestion.

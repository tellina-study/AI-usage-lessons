# sync-library

Synchronize Google Drive working folder with local catalog.

## Steps
1. List files in Google Drive folder via workspace-mcp
2. Compare with `catalog/manifests/documents.yaml`
3. Export new/changed files via gws to `catalog/exports/`
4. Trigger knowledge-rag re-index
5. Update manifest with sync timestamp
6. Report changes to the calling issue

# Tools — Session 2 (2026-03-31)

## MCP Tools Used

| Server | Tools Called | Result |
|--------|-------------|--------|
| workspace-mcp | `list_drive_items`, `get_doc_as_markdown`, `get_drive_file_content`, `search_drive_files`, `list_docs_in_folder` | Success. Read course documents from Google Drive work folder. |
| document-loader | `read_document` | Success. Read DOCX file (FOS document). |
| github | `list_issues`, `issue_write`, `create_pull_request`, `merge_pull_request`, `list_pull_requests` | Success. Managed issues #1-#4, created PR #5, merged PR #2. |
| local-rag | `ingest_file`, `query_documents`, `list_files`, `status` | Success. Ingested exported docs, ran semantic queries. |
| open-ontologies | Not used this session | N/A — ontology population deferred to later phase. |
| drawio | Not used this session | N/A — no diagrams created yet. |

## Skill Test Results

| Skill | Tested | Result | Notes |
|-------|--------|--------|-------|
| sync-library | Yes | Working | Successfully listed Drive folder, exported docs to catalog/exports/docs/, updated manifests. |
| extract-links | Yes | Working | Extracted cross-references from exported documents. |
| impact-check | Yes | Working | Analyzed changes and produced impact assessment. |
| catalog-docs | Pending | Not yet tested | Queued for next session. |
| build-deck | Pending | Not yet tested | Queued for next session. |
| update-lecture | Pending | Not yet tested | Queued for next session. |
| diagram-refresh | Pending | Not yet tested | Queued for next session. |
| issue-from-change | Pending | Not yet tested | Queued for next session. |

3 of 8 skills tested and confirmed working.

## Subagent Usage

Subagents were used for all implementation work per CLAUDE.md orchestration rule:
- Subagent for CLAUDE.md fixes: success
- Subagent for blueprint creation: success
- Subagent for skill rewrites: success
- Subagent for agent definition rewrites: success
- Subagent for raw doc saves and manifest updates: success
- Subagent for skill testing (sync-library, extract-links, impact-check): success

**Success rate:** 100% — all subagent delegations completed without failure.

## Tool Failures

No MCP tool failures this session. All calls returned expected results.

## Permission Issues

- `.claude/settings.json` wildcard permissions were initially too restrictive for skill testing. Fixed by adding broader MCP tool patterns (e.g., `mcp__workspace-mcp__*`).
- No OAuth or auth failures encountered.

## Tool Selection Observations

- workspace-mcp was correctly used as primary Google layer (no gws fallback needed).
- document-loader was useful for reading the .docx file that workspace-mcp cannot parse directly.

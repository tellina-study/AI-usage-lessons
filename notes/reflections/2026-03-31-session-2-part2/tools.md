# Tools — Session 2 Part 2 (2026-03-31)

## MCP Tools Used

### workspace-mcp
- `create_drive_folder` — created 44 folders for Drive course structure
- `create_doc` — initial document creation (raw text, no formatting)
- `import_to_google_doc` — discovered mid-session, proper markdown-to-Docs conversion with formatting preserved
- `create_spreadsheet` / `modify_sheet_values` — references spreadsheet
- `create_presentation` — tested as part of build-deck skill validation
- `list_drive_items` — verified folder creation results

### github (MCP)
- Issue creation (#9, #11), PR creation (#10), branch operations
- Used throughout for issue-driven workflow

### open-ontologies
- `onto_query` — queried ontology for visualization data
- `onto_stats` — checked ontology state

### drawio
- Not used this part — visualization was done with pyvis instead

### document-loader
- Not directly used this part

## Tools That Failed

### OntoSpy (external, not MCP)
- **Error:** Broken on Python 3.12 — import errors in the library
- **Structural:** Not transient; the library has not been updated for 3.12 compatibility
- **Resolution:** Replaced with pyvis for graph visualization

### Google Slides API
- **Error:** API not enabled in Google Cloud project
- **Resolution:** User manually enabled Slides API in Google Cloud Console
- **Lesson:** All Google APIs needed should be pre-enabled during setup

### Google Sheets API
- **Error:** API not enabled — blocked references spreadsheet creation
- **Resolution:** User manually enabled Sheets API
- **Lesson:** Same as above — add to setup checklist

## Skills Invoked

All 9 skills tested and passing:
1. sync-library
2. catalog-docs
3. extract-links
4. update-lecture
5. build-deck (blocked until Slides API enabled, then passed)
6. diagram-refresh
7. issue-from-change
8. impact-check
9. reflect

## Subagents Used

4 parallel subagents for Drive folder structure creation (issue #11):
- Subagent 1: Course lectures folders (weeks 1-17)
- Subagent 2: Course seminars folders (weeks 1-17)
- Subagent 3: Course admin folders (exams, grades, general)
- Subagent 4: Document creation (12 docs + spreadsheet)
- **Success ratio:** 4/4 — all completed successfully

## New Tools Discovered

### import_to_google_doc
- Previously unknown — `create_doc` was being used which inserts raw markdown text without formatting
- `import_to_google_doc` converts markdown to proper Google Docs formatting (headings, lists, bold, etc.)
- **Impact:** All skills that create Google Docs should use this instead of `create_doc`

## Permission Issues

- Slides API and Sheets API needed manual enabling in Google Cloud Console
- OAuth scopes were already granted; the APIs themselves were just not turned on
- No other permission issues encountered

## Tool Selection Mistakes

- Initially used `create_doc` for Lecture 1 plan — resulted in raw markdown text in the document
- Corrected to `import_to_google_doc` after discovering it — document recreated with proper formatting
- OntoSpy was attempted before checking Python version compatibility — should have checked first

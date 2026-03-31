# issue-from-change

Detect document changes and create GitHub Issues with structured descriptions.

## Role

You are an issue-manager agent. Your job is to compare the current state of the Google Drive folder against the local manifest, detect changes (new, modified, removed files), assess impact, and create GitHub Issues for each change using the standard template.

## Constants

- Google account: kzlevko@gmail.com
- Google Drive folder ID: `1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am`
- 00-course: `1sHXoLaIqCpBRv1IaLjS6lNtBdwI5cPc0`
- 01-formal: `1-sQ7H1CBNWaHvQIDE8TLCwVX2ilEeb0p`
- 02-lectures: `16osAMJ9y67Yem9T6fK6yDv1fXF8BGLEZ`
- 03-seminars: `1AZhb5q-yODrIJEnQBN8S1KJI0bby588J`
- 04-resources: `1yDZrw9CcGtGljNGZ-QByyoUGIMVr9Tc4`
- Manifest: `/home/levko/AI-usage-lessons/catalog/manifests/documents.yaml`
- Issue template: `/home/levko/AI-usage-lessons/templates/issue-change-template.md`
- GitHub repo: `tellina-study/AI-usage-lessons`
- Ontology prefix: `aul: <https://ai-usage-lessons.local/ontology#>`

## Execution

### Step 1: Get current Drive state

List all files in Drive folders:
```
mcp__workspace-mcp__list_drive_items(folder_id="1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am")
mcp__workspace-mcp__list_drive_items(folder_id="1U74-dCQLq1Zz2GldV6p-v07WnT3mWCxg")
mcp__workspace-mcp__list_drive_items(folder_id="1-sQ7H1CBNWaHvQIDE8TLCwVX2ilEeb0p")
```

### Step 2: Read current manifest and template

Read using the Read tool:
1. `/home/levko/AI-usage-lessons/catalog/manifests/documents.yaml`
2. `/home/levko/AI-usage-lessons/templates/issue-change-template.md`

### Step 3: Detect changes

Compare Drive file list with manifest entries:

- **Added**: File ID in Drive but not in manifest
- **Modified**: File ID in both, but Drive modifiedTime > manifest exported_at
- **Removed**: File ID in manifest but not in Drive (or moved/trashed)

### Step 4: Assess impact for each change

For each detected change, query the ontology for affected entities:

```
mcp__open-ontologies__onto_query(
  query="PREFIX aul: <https://ai-usage-lessons.local/ontology#>\nSELECT ?entity ?type ?relation WHERE {\n    {\n        ?entity aul:cites aul:doc_<changed_doc_slug> .\n        BIND(\"cites\" AS ?relation)\n    } UNION {\n        ?entity aul:depends_on aul:doc_<changed_doc_slug> .\n        BIND(\"depends_on\" AS ?relation)\n    } UNION {\n        ?entity aul:covers aul:doc_<changed_doc_slug> .\n        BIND(\"covers\" AS ?relation)\n    } UNION {\n        ?entity aul:illustrates aul:doc_<changed_doc_slug> .\n        BIND(\"illustrates\" AS ?relation)\n    }\n    ?entity a ?type .\n}"
)
```

### Step 5: Check for duplicate issues

Before creating an issue, search for existing open issues about the same document:
```
mcp__github__search_issues(
  query="repo:tellina-study/AI-usage-lessons is:open <document title or ID>",
  sort="updated",
  order="desc"
)
```

Skip creating an issue if a matching open issue already exists. Add a comment to the existing issue instead.

### Step 6: Create GitHub Issues

For each change that needs a new issue, fill in the template and create:

```
mcp__github__issue_write(
  method="create",
  repo="tellina-study/AI-usage-lessons",
  title="[Change detected] <document title> — <change_type>",
  body="## Change Detected\n\n**Source:** <document title> (<source_url>)\n**Change type:** <added|modified|removed>\n**Detected:** <today's date>\n\n## Affected Entities\n\n| Entity | Type | Relation |\n|--------|------|----------|\n| <entity> | <Lecture/SlideDeck/Diagram> | <cites/depends_on/covers> |\n\n## Impact Assessment\n\n- [<x if affected>] Lectures affected\n- [<x if affected>] Slides need rebuild\n- [<x if affected>] Diagrams need update\n- [<x if affected>] Other documents cite this\n\n## Action Items\n\n1. Re-export document via sync-library\n2. <Update affected lecture(s)>\n3. <Rebuild affected deck(s)>\n4. <Refresh affected diagram(s)>",
  labels=["change-detected", "<change_type>"]
)
```

If adding to an existing issue:
```
mcp__github__add_issue_comment(
  repo="tellina-study/AI-usage-lessons",
  issue_number=<existing_issue_number>,
  body="## Update — <today>\n\nAdditional change detected for this document.\n\n**Change type:** <change_type>\n**New affected entities:** <list>"
)
```

### Step 7: Update ontology with tracking

For each created issue, link the document to the task in the ontology:
```
mcp__open-ontologies__onto_load(
  data="@prefix aul: <https://ai-usage-lessons.local/ontology#> .\n@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\naul:task_issue_<issue_number> a aul:Task ;\n    aul:source_url \"https://github.com/tellina-study/AI-usage-lessons/issues/<issue_number>\" ;\n    aul:source_system \"github\" ;\n    aul:status \"active\" ;\n    aul:updated_at \"<today>T00:00:00\"^^xsd:dateTime .\n\naul:doc_<slug> aul:tracked_by aul:task_issue_<issue_number> .",
  format="turtle"
)
```

### Step 8: Report

```
## Issue-from-Change Report — <date>

### Changes Detected
| Document | Change Type | Affected Entities |
|----------|-------------|-------------------|
| <title> | modified | 2 lectures, 1 deck |

### Issues Created
| Issue # | Title | Labels |
|---------|-------|--------|
| #<num> | [Change detected] <title> — modified | change-detected, modified |

### Issues Updated (existing)
| Issue # | Comment Added |
|---------|---------------|
| #<num> | Additional change detected |

### No Changes
- <count> documents unchanged

### Statistics
- Changes detected: X
- Issues created: Y
- Issues updated: Z
```

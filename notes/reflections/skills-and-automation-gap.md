# Skills and Automation Gap: Why Zero Out of Eight Skills Were Used

**Date:** 2026-03-31
**Session scope:** Initial repo setup, MCP configuration, document sync, ontology load, formal program rewrite, roadmap diagram
**Severity:** Architectural -- the entire daily/weekly cycle described in CLAUDE.md is inoperable

---

## The Fact

Eight skills were defined in `.claude/skills/` during the session:

| Skill | SKILL.md exists | Invoked via Skill tool | Steps executed manually |
|-------|:-:|:-:|:-:|
| sync-library | Yes | No | Partially (ad-hoc MCP calls) |
| catalog-docs | Yes | No | No (manifests still empty) |
| extract-links | Yes | No | No (ontology has schema only) |
| update-lecture | Yes | No | No (no lectures yet) |
| build-deck | Yes | No | No (no slides yet) |
| diagram-refresh | Yes | No | Partially (one diagram created manually) |
| issue-from-change | Yes | No | Partially (issues created via gh CLI) |
| impact-check | Yes | No | No |

Zero invocations. Not a single `/sync-library` or `/catalog-docs` was called during the entire session. The skills were created, registered, visible in the Skill tool's available list, and completely ignored.

---

## Why They Were Not Used

### 1. Skills are documentation, not automation

Each SKILL.md is a numbered recipe. Here is `sync-library/SKILL.md` in its entirety:

```
# sync-library

Synchronize Google Drive working folder with local catalog.

## Steps
1. List files in Google Drive folder via workspace-mcp
2. Compare with catalog/manifests/documents.yaml
3. Export new/changed files via gws to catalog/exports/
4. Trigger knowledge-rag re-index
5. Update manifest with sync timestamp
6. Report changes to the calling issue
```

This is 6 lines of prose describing what a human (or an AI) should do. It is not:
- A shell script that runs the steps
- An agent prompt that a subagent can execute
- A hook that triggers on events
- A scheduled job

Invoking `/sync-library` via the Skill tool would display this text to the conversation. That is all it would do. The steps would not execute. No MCP calls would fire. No files would sync. The skill would show the recipe, then wait for the operator to manually follow it.

### 2. The same problem affects all eight skills

Every SKILL.md follows the same pattern: a title, a one-line description, and a numbered list of steps referencing tools by name. None of them contain:
- MCP tool names with actual parameters
- Error handling logic
- Input/output specifications
- Precondition checks
- State management (how to resume if interrupted)

They are outlines of workflows, not implementations of workflows.

### 3. Manual execution filled the gap (partially)

Without executable skills, the session's work was done by hand:

**What sync-library should have done:**
1. `workspace-mcp.list_drive_items` for the working folder
2. Compare results with `catalog/manifests/documents.yaml`
3. Export changed files to `catalog/exports/docs/`
4. `local-rag.ingest_file` for each exported file
5. Update the manifest
6. Comment on the tracking issue

**What actually happened:**
1. `workspace-mcp.list_drive_items` was called manually
2. No comparison was made -- manifests were empty and stayed empty
3. `workspace-mcp.get_doc_as_markdown` was called for individual documents, content was fed directly to `local-rag.ingest_data` without saving to disk first
4. Manifests were never updated
5. No issue comment was posted

Steps 2, 3 (save-to-disk part), 5, and 6 were simply skipped. The skill recipe existed but nobody followed the full recipe.

**What catalog-docs should have done:**
Scan `catalog/exports/`, extract metadata, update manifests, create RDF triples.

**What actually happened:**
Nothing. `catalog/manifests/documents.yaml` still contains `documents: []`.

**What extract-links should have done:**
Read documents, identify cross-references, write triples to Oxigraph.

**What actually happened:**
Nothing. The ontology has 65 triples of schema (classes, properties, constraints) and zero triples of entity data. No documents, no lectures, no relationships.

**What issue-from-change should have done:**
Detect document changes, run impact assessment, create templated GitHub issues.

**What actually happened:**
Issues were created manually via `gh issue create`. No change detection. No impact assessment. No template used.

---

## What Each Skill Should Actually Be

### sync-library -- the foundation skill

This is the most important skill because every other skill depends on having up-to-date local copies of Google Drive content.

**Required behavior:**

```
Input:  Google Drive folder ID (from CLAUDE.md)
Output: Updated files in catalog/exports/, updated documents.yaml,
        ingested content in local-rag, change report

1. Call workspace-mcp.list_drive_items for folder
   1-f2hpJrlUbfnMcxhR-6vF3xCsXZUI6am (recursive)
2. Load catalog/manifests/documents.yaml
3. For each file in Drive:
   a. If file ID not in manifest OR modifiedTime > manifest timestamp:
      - Google Docs/Sheets/Slides: workspace-mcp.get_doc_as_markdown
        -> save to catalog/exports/docs/{sanitized_name}.md
      - Office formats (DOCX/XLSX/PPTX/PDF):
        workspace-mcp.get_drive_file_download_url -> download
        -> save to catalog/exports/docs/{original_name}
      - Call local-rag.ingest_file for the saved file
      - Record in change list
   b. If file in manifest but not in Drive:
      - Mark as deleted in manifest
      - Call local-rag.delete_file
4. Write updated manifest with file IDs, names, mimeTypes,
   modifiedTimes, local paths, sync timestamp
5. If running under a GitHub issue: post change summary as comment
```

**What is missing to make this work:**
- The manifest schema (what fields? what format?)
- Error handling (what if workspace-mcp auth has expired?)
- The file-saving step (Write tool? Bash? Where exactly?)
- Conflict resolution (what if a file was renamed?)

### catalog-docs -- the metadata layer

**Required behavior:**

```
Input:  Files in catalog/exports/
Output: Updated manifests, RDF triples for new entities

1. Scan catalog/exports/ recursively for all files
2. For each file not already in the appropriate manifest:
   a. Extract metadata: title (from filename or content),
      type (doc/sheet/slide/pdf), size, last modified
   b. Determine which manifest it belongs to
      (documents.yaml, lectures.yaml, decks.yaml, diagrams.yaml)
   c. Add entry to manifest
3. For each new entry:
   a. Create RDF triple: <entity> rdf:type <Document|Lecture|SlideDeck>
   b. Add attributes: source_url, updated_at, status
   c. Write to Oxigraph via open-ontologies.onto_ingest
4. Report: N new items cataloged, M existing items updated
```

### extract-links -- the relationship builder

**Required behavior:**

```
Input:  Documents in local-rag index
Output: RDF triples representing cross-references

1. For each document in catalog/manifests/documents.yaml:
   a. Query local-rag for the document content
   b. Identify references to other documents (by title, URL, or citation)
   c. Identify references to standards, regulations, requirements
   d. Map each reference to an ontology relation:
      - "see document X" -> cites
      - "based on standard Y" -> depends_on
      - "covers topic Z" -> covers
      - "as shown in diagram D" -> illustrates
2. For each identified relation:
   a. Check if the target entity exists in Oxigraph
   b. If not, create it (with status: unresolved)
   c. Write the relation triple
3. Report: N new links found, M unresolved references
```

### issue-from-change -- the change detection pipeline

**Required behavior:**

```
Input:  Change report from sync-library
Output: GitHub issues for affected content

1. Receive change details: which files changed, what type of change
2. For each changed file:
   a. Query Oxigraph: what entities depend on this file?
      SPARQL: SELECT ?affected WHERE {
        ?affected :depends_on|:cites|:covers <changed_entity> }
   b. For each affected entity: add to impact list
3. For each item in impact list:
   a. Load templates/issue-change-template.md
   b. Fill template with: source change, affected entity,
      relationship type, suggested action
   c. Create GitHub issue via github-mcp
   d. Apply labels per workflows/issue-triage.md
   e. Add to project board
```

### impact-check -- the weekly audit

**Required behavior:**

```
Input:  Time range (default: last 7 days)
Output: Impact report with cascading effects

1. Query Oxigraph for entities with updated_at in the time range
2. For each changed entity:
   a. Trace dependency chains up to 3 levels deep
   b. Record: entity -> direct dependents -> transitive dependents
3. Run orphan checks:
   a. Diagrams not referenced by any lecture or document
   b. Requirements not covered by any lecture
   c. Documents not cited by anything
4. Generate impact report (markdown)
5. Create/update GitHub issues for unresolved impacts
```

### diagram-refresh, update-lecture, build-deck

These three follow the same pattern: detect what changed, read current content, apply updates, save results, update manifests and ontology. Each references specific MCP tools (drawio for diagrams, workspace-mcp for documents and slides) but none specify the actual parameters, error handling, or state management needed for reliable execution.

---

## The Automation Gap

### What CLAUDE.md promises

```
Daily Cycle:
1. sync-library pulls changes from Google Drive
2. catalog-docs + extract-links update index and ontology
3. Changes trigger issue-from-change to create/update GitHub Issues
4. update-lecture, build-deck, diagram-refresh as needed

Weekly Cycle:
- impact-check: what changed and what it affects
- Issue triage via issue-manager
- Update notes/decisions.md
```

### What actually exists

- **sync-library:** A 6-line recipe. No executor.
- **catalog-docs:** A 5-line recipe. No executor.
- **extract-links:** A 5-line recipe. No executor.
- **issue-from-change:** A 6-line recipe. No executor.
- **impact-check:** A 6-line recipe. No executor.
- **update-lecture:** A 7-line recipe. No executor.
- **build-deck:** A 7-line recipe. No executor.
- **diagram-refresh:** A 7-line recipe. No executor.

The daily cycle cannot run. The weekly cycle cannot run. The system has an engine (MCP servers with 211 tools) but no transmission connecting the engine to the wheels (skills that invoke those tools in sequence).

### The manifests prove it

All four manifests are empty:

```yaml
# catalog/manifests/documents.yaml
documents: []

# catalog/manifests/lectures.yaml
lectures: []

# catalog/manifests/decks.yaml
decks: []

# catalog/manifests/diagrams.yaml
diagrams: []
```

If any skill had executed even once, at least one manifest would have data. Empty manifests are proof that the pipeline has never run.

---

## How to Fix This

### Option A: Agent-prompt skills

Convert each SKILL.md into a detailed subagent prompt. When `/sync-library` is invoked, Claude Code reads the SKILL.md and spawns an Agent with the content as the prompt, enriched with:
- Specific MCP tool names and their required parameters
- The Google Drive folder ID and manifest file paths
- Error handling instructions ("if auth fails, stop and report")
- Output format ("update documents.yaml with this schema, post issue comment with this format")

**Pros:**
- Leverages Claude Code's native Agent tool
- Flexible -- the prompt can handle edge cases through reasoning
- MCP tools are available to subagents (proven by the RPD rewrite)
- No external dependencies beyond what already exists

**Cons:**
- Each invocation costs tokens (a full agent conversation)
- Non-deterministic -- the agent may interpret steps differently each time
- May fail on permissions for Bash or Write operations
- No caching or incremental state between runs

**Implementation effort:** Medium. Rewrite each SKILL.md with concrete tool calls, parameters, and error handling. Test each one.

### Option B: Shell script skills

Create a shell script for each skill that uses CLI tools:
- `npx mcp-local-rag ingest /path/to/file` for RAG ingestion
- `gh issue create` for GitHub issues
- `yq` or `python` for YAML manifest updates
- Direct `curl` calls to Oxigraph's SPARQL endpoint

**Pros:**
- Deterministic -- same script, same behavior
- Fast -- no token cost per run
- Scriptable -- can be triggered by hooks, cron, or CI

**Cons:**
- Cannot use workspace-mcp, drawio-mcp, or open-ontologies MCP from shell -- these are session-bound servers
- Limited to what has a CLI interface (gh, local-rag CLI)
- Duplicates logic that MCP servers already handle
- Maintenance burden of keeping scripts in sync with MCP API changes

**Implementation effort:** High for skills that need MCP servers (most of them). Low for skills that only use CLI tools (issue-from-change could work with `gh` alone).

### Option C: Hybrid (recommended)

Split each skill into two layers:

1. **Shell-scriptable operations** -- run via hooks or Bash:
   - File system operations (save exports, scan directories)
   - YAML manifest updates (yq or python)
   - Git operations (commit, push)
   - GitHub CLI operations (gh issue, gh pr)
   - local-rag CLI operations (ingest, delete)

2. **MCP-dependent operations** -- run via Agent subagents:
   - Google Drive listing and document export (workspace-mcp)
   - Ontology queries and triple insertion (open-ontologies)
   - Diagram creation and validation (drawio-mcp)
   - Google Docs/Slides editing (workspace-mcp)

The Skill invocation triggers both layers in sequence: shell script first for deterministic setup, then agent prompt for MCP-dependent work.

**Pros:**
- Uses the right tool for each operation
- Shell parts are fast and deterministic
- MCP parts leverage the full server capabilities
- Partial execution possible (shell part can succeed even if MCP part fails)

**Cons:**
- More complex implementation
- Two systems to maintain
- Coordination between shell and agent layers needs design

**Implementation effort:** Medium-high initially, but lower ongoing maintenance than pure agent prompts.

---

## Priority Order for Implementation

| Priority | Skill | Rationale |
|:--------:|-------|-----------|
| 1 | sync-library | Foundation -- all other skills depend on having current local copies of Drive content |
| 2 | catalog-docs | Populates manifests that every other skill reads |
| 3 | extract-links | Populates ontology with real entity data and relationships |
| 4 | issue-from-change | Enables the change-detection pipeline; connects sync to task management |
| 5 | impact-check | Requires populated ontology (depends on extract-links) |
| 6 | diagram-refresh | Useful once diagrams reference real entities |
| 7 | update-lecture | For content updates once lectures exist |
| 8 | build-deck | For slide creation once lectures exist |

Items 1-4 form the minimum viable pipeline: sync content, catalog it, extract relationships, and create issues from changes. Without these four, the system is a manually operated toolkit.

Items 5-8 are content-production skills that become useful once the pipeline is running and there are actual lectures and slides to manage.

---

## The Deeper Problem: Planning vs. Building

The first session excelled at planning. It produced:
- A complete CLAUDE.md with architecture, conventions, and rules
- 5 agent definitions with clear responsibilities
- 8 skill definitions with step-by-step recipes
- An ontology schema with 8 classes and 7 relations
- 4 manifest files with correct headers
- Templates, workflows, and triage rules

All of this is planning artifact. None of it is executable. The session built an elaborate blueprint and then... stopped. The actual automation -- the code that makes the blueprint work -- was never written.

This is a known failure mode in AI-assisted development: the AI is exceptionally good at generating structured documentation that looks complete, and the human (or the AI itself in orchestrator mode) mistakes the documentation for implementation. The existence of a `sync-library/SKILL.md` file creates the illusion that sync-library is "done." It is not done. It is described.

### The gap in numbers

| Artifact type | Count | Status |
|--------------|:-----:|--------|
| SKILL.md files (recipes) | 8 | Written |
| Executable skill implementations | 0 | Not started |
| Agent prompts with concrete tool calls | 0 | Not started |
| Shell scripts for automatable steps | 0 | Not started |
| Hooks triggering skills on events | 0 | Not started |
| Manifests with actual data | 0 | Empty |
| Ontology entities (not schema) | 0 | None loaded |

The ratio of description to implementation is infinity. The system is 100% described and 0% automated.

---

## Concrete Next Steps

1. **Pick sync-library as the first skill to implement.** It unblocks everything else.
2. **Start with the hybrid approach:** write a shell script for file operations, write an agent prompt for MCP operations.
3. **Test the skill end-to-end:** invoke it, verify that `catalog/exports/` gets files, `documents.yaml` gets entries, and `local-rag` gets updated.
4. **Only then move to catalog-docs.** Each skill should be proven working before starting the next.
5. **Create a GitHub issue for each skill implementation.** Do not bundle them. Each skill is a separate deliverable with its own branch and PR.

The system's architecture is sound. The MCP stack works. The ontology schema is ready. What is missing is the wiring -- the executable code that connects these components into the pipeline that CLAUDE.md describes. Building that wiring is the single most important task for the next session.

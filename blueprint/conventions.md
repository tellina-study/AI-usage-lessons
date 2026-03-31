# Working Conventions

Rules and patterns for day-to-day work in this repo. Derived from CLAUDE.md governance rules and first-session experience.

---

## Git Workflow

### Every task starts with a GitHub Issue

No exceptions. Not for "quick fixes," not for doc updates, not for config changes. The issue is the source of truth for what was done and why.

### Branch naming

```
issue-{N}-{short-description}
```

Examples: `issue-1-mcp-setup`, `issue-5-sync-library`, `issue-12-lecture-3-slides`.

### Commits reference the issue

Every commit message includes `#{N}` where N is the issue number:

```
Add workspace-mcp OAuth configuration #1
```

### One branch per issue

Never commit work for issue #3 on a branch for issue #1. If issue #1's PR is not yet merged, either:
- Merge the PR first, then create the new branch from updated main
- Or create the new branch from the issue-1 branch (if the work depends on it), but keep commits cleanly separated

### Merge before moving on

Finish the cycle: branch -> commits -> push -> PR -> review -> merge. Do not start a new issue while the previous PR is still open and unmerged. Unmerged PRs that accumulate unrelated commits become unreviewable.

### Never push to main

Not even for "bootstrap." For an empty repo, push a single README commit to main, then immediately branch for real work.

---

## File Layout Rules

### Raw exports before ingestion

```
Google Drive -> workspace-mcp -> catalog/exports/docs/{name}.md
                                                            |
                                                   local-rag.ingest_file
```

Never pass document content directly from workspace-mcp to `ingest_data`. Always save the raw file to disk first. Reasons:
- Reproducible ingestion (re-ingest from local file, not live API)
- Version tracking (diff against previous export)
- Offline access
- Traceable data lineage

### Use `ingest_file`, not `ingest_data`

`ingest_file` takes a local file path and creates proper provenance in LanceDB. `ingest_data` takes a raw string and stores it as a base64-named blob in `lancedb/raw-data/` -- opaque and untraceable.

### Diagrams are files, not browser sessions

```
1. Generate .drawio XML content
2. Write to diagrams/{category}/{name}.drawio (THIS IS THE ARTIFACT)
3. Optionally preview: drawio.open_drawio_xml or open_drawio_mermaid
```

The `.drawio` file in the repo is the source of truth. The browser preview is ephemeral. If it is not committed, it does not exist.

### Manifests track everything

After every export or ingestion, update the relevant manifest in `catalog/manifests/`:

```yaml
# catalog/manifests/documents.yaml
documents:
  - name: "fos-otraslevoe"
    source_type: docx
    drive_id: "1abc..."
    local_path: "catalog/exports/docs/fos-otraslevoe.docx"
    ingested_at: "2026-03-31T14:30:00Z"
    chunks: 196
    rag_status: ingested
```

If the manifest does not reflect the current state, the pipeline is broken.

---

## Subagent Delegation

### When to delegate

| Task | Approach |
|------|----------|
| Edit Google Docs/Sheets/Slides | Delegate to subagent |
| Create diagrams | Delegate to subagent |
| Gap analysis, structured content work | Delegate to subagent |
| Web research (WebSearch, WebFetch) | Do directly -- subagents cannot use these |
| Git operations (branch, commit, push, PR) | Do directly |
| MCP server setup and testing | Do directly |
| System configuration | Do directly |

### Subagent prompt quality matters

A vague prompt produces shallow output. Specify:
- Expected depth and detail level
- Specific areas to cover
- Output format (markdown, YAML, file paths)
- Fail-fast instruction: "If you cannot access a required tool after 2 attempts, stop and report what you need"

### Bundle 2-3 related tasks per subagent

The sweet spot: related tasks that share context. Example: "Read this document, analyze gaps, create a Drive folder for the output." One agent, 9 tool calls, 2 minutes.

Anti-pattern: 6 parallel agents each doing independent web research. All fail. 3 minutes of compute, zero output.

### Bulk document editing

For rewriting >50% of a Google Doc, do NOT use `modify_doc_text` in a loop (68 calls, 47 minutes observed). Instead:
- Draft the full content locally as markdown
- Use `batch_update_doc` or `create_doc` + `import_to_google_doc` for a single bulk operation

---

## Orchestration Rules

### Roast before implement (content work)

For tasks that modify student-facing documents, lectures, or slides:
1. Plan the changes
2. Self-critique: Is this the simplest approach? Are assumptions verified? What could go wrong?
3. Present the critique to the user
4. Get approval before proceeding

Skip the roast for infrastructure tasks (MCP setup, config changes, gitignore updates).

### Phase gating (content work)

For multi-step content changes:
1. Implement phase N
2. Verify the result
3. Present to user, get explicit approval
4. Only then start phase N+1

Skip strict gating for infrastructure. Use light gating instead: "Completed X, continuing to Y unless you object."

---

## Session Hygiene

### Check decisions.md before starting

```bash
cat notes/decisions.md
```

This file contains accumulated findings, gotchas, and anti-patterns. Reading it before work prevents repeating known mistakes.

### Update decisions.md after every session

Every new finding, workaround, or anti-pattern discovered during work gets added to `notes/decisions.md`. This is the project's institutional memory.

### Reflections after substantive sessions

After sessions that involve content creation, significant debugging, or architectural decisions, write a reflection in `notes/reflections/{date}-{topic}/`. Cover:
- What was attempted and what happened
- What worked and what failed (with specifics)
- What the correct approach would have been
- Patterns to carry forward

### Read documents with intent

Never read a large Google Doc "just to see what is in it." The context window cost is high (50K+ characters per document). Have a specific question or extraction goal before calling `get_doc_as_markdown`. Use `get_drive_file_content` (plain text, smaller) for triage.

---

## Document Size Limit

No single file in this repo may exceed 600 lines. If a document grows beyond that, split it into logical parts with cross-links. Code files are exempt but should still favor focused modules.

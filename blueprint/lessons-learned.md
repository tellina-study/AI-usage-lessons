# Lessons Learned

Distilled from 7 detailed reflection files written after the first setup session (2026-03-31). Each lesson was learned the hard way -- through a failure, a near-miss, or a user correction.

---

## MCP Configuration

### Use `claude mcp add`, never edit settings.json for MCP servers

The first 45 minutes of the setup session were wasted trying to register MCP servers by adding a `mcpServers` block to `.claude/settings.json`. This is a documentation-reality mismatch: many examples show the settings.json format, but Claude Code reads MCP config from `.mcp.json`, which is created by `claude mcp add`.

**Symptoms of wrong config location:** `claude mcp list` shows nothing. No error message, no warning. The server simply does not exist.

**The fix:** Always use `claude mcp add`. Never hand-edit config files for MCP server registration.

### Verify `.gitignore` before any MCP configuration

`.mcp.json` contains secrets (OAuth credentials, PATs). It is not gitignored by default. Secrets were briefly placed in tracked files during the first session. They were caught before commit only by manual inspection, not by tooling.

**Rule:** Before running any `claude mcp add`, verify that `.mcp.json`, `.claude/settings.local.json`, and `.env` are all in `.gitignore`.

---

## Google OAuth

### Add the redirect URI BEFORE starting the auth flow

workspace-mcp OAuth requires `http://localhost:8000/oauth2callback` as an authorized redirect URI in the Google Cloud Console. If you start the auth flow without it, you get `redirect_uri_mismatch` and the auth URL expires. You then have to add the URI, wait for propagation, and regenerate a fresh auth URL.

**Time cost of getting this wrong:** 15-20 minutes. The fix is a 30-second check before starting.

### workspace-mcp needs HTTP mode for initial auth

The normal MCP mode (stdio) cannot handle browser redirects. For the one-time OAuth flow, start workspace-mcp with `--transport streamable-http --port 8000` in a separate terminal. After auth completes and the token is cached, switch back to stdio mode (which is what `claude mcp add` registers).

---

## Subagents

### Subagents cannot do web research

WebSearch and WebFetch are not available to subagents. This was discovered by launching 6 parallel research subagents -- all 6 failed with permission denied on every web-related tool call. Each agent burned 8-12 attempts before giving up.

**Rule:** All web research must be done directly in the main conversation. Never delegate it.

### Subagents can enter death spirals

When a subagent lacks the permissions for its task, it does not fail fast. One observed case: 44 tool calls, each denied, with increasingly creative workarounds attempted. The agent produced zero useful output.

**Mitigation:** Include in every subagent prompt: "If you cannot access a required tool after 2 attempts, stop immediately and report what you need."

### Prompt quality determines output quality

The first reflection subagent produced a shallow bullet-point summary ("MCP setup had issues"). After the user demanded specifics, a second attempt with a detailed prompt produced the thorough analysis that became the reflection files.

**Rule:** Specify expected depth, areas to cover, output format, and what "done" looks like. A subagent defaults to the minimum viable interpretation of a vague prompt.

---

## Document Operations

### Always save raw files before ingesting

Three documents were ingested into local-rag: one correctly via `ingest_file` from a saved local file (196 chunks), two incorrectly via `ingest_data` from strings (18 + 8 chunks). The string-based ingestions:
- Created untraceable base64-named blobs in `lancedb/raw-data/`
- Had no local file backup
- Were not reproducible without re-reading from Google Drive
- Produced lower-quality chunks

**The correct pipeline:** Google Drive -> export to `catalog/exports/docs/` -> `ingest_file` from the local path.

### `export_doc_to_pdf` exports to Drive, not to disk

The tool name is misleading. It creates a PDF copy in Google Drive (in the root folder, not in your working folder). It does not download anything to the local filesystem. For local export, use `get_doc_as_markdown` and save the output, or `get_drive_file_download_url` for binary download.

### Bulk document editing is painfully slow via MCP

A formal program rewrite required 68 sequential `modify_doc_text` calls over 47 minutes. Each call does one find-and-replace operation. For rewrites of >50% of a document, use `batch_update_doc` (multiple operations per call) or draft locally and use `create_doc`/`import_to_google_doc`.

### Read documents with intent, not curiosity

A single 50K-character Google Doc consumes significant context window space. Reading two large docs in one session (~100K chars) left limited room for actual work. Use `get_drive_file_content` (plain text, smaller) for triage. Only use `get_doc_as_markdown` when the markdown structure is needed.

---

## Skills and Automation

### Skills must be executable agent prompts, not recipes

Eight SKILL.md files were created in the first session. Each contained 5-7 lines of prose describing steps. None were ever invoked. When similar work was done, it was done ad-hoc through direct tool calls.

The problem: invoking `/sync-library` via the Skill tool displays the recipe text. It does not execute the steps. No MCP calls fire. No files sync.

**What a skill should be:** A detailed agent prompt with specific MCP tool names, parameters, error handling, input/output specs, and preconditions. When invoked, Claude Code reads the prompt and spawns a subagent that executes it.

### The gap between "defined" and "working" is the entire system

After the first session: 8 skills defined, 0 used as designed. 5 agents defined, 0 referenced during delegation. 4 manifests created, all empty. The system was 100% described and 0% automated. Planning artifacts that look complete can create the illusion that work is done.

---

## Workflow Discipline

### Roast step catches real problems

The roast step was skipped for every task in the first session. Had it been applied to the MCP stack plan, it would have caught the XLSX/PPTX format gap in local-rag before installation, saving the reactive addition of document-loader.

**When to enforce:** Content changes that affect students or stakeholders. Skip for infrastructure and config work where the cost of a wrong choice is just "uninstall and try again."

### Phase gating prevents cascading errors

The formal program rewrite proceeded from gap analysis to rewrite to commit without the user reviewing intermediate results. If the gap analysis was wrong (e.g., workspace-mcp's markdown rendering dropped a section), the rewrite would have introduced errors that propagated unchecked.

**When to enforce:** Any changes to Google Docs that students or stakeholders will read. The gate must be explicit: present changes, wait for confirmation.

### Merge the PR before starting the next issue

Issue #3 work landed on the issue-1 branch because PR #2 was never merged. This entangled two concerns in one PR, made review harder, and made selective revert impossible.

**Rule:** Finish the cycle (branch -> PR -> review -> merge) before starting new work. No exceptions.

---

## User Interaction Patterns

### Deliver artifacts, not status reports

"All 6 MCP servers operational" is not a result. The user measures value by artifacts produced: documents saved, diagrams created, programs rewritten. Infrastructure is invisible. Configuration is a prerequisite, not an achievement.

**After any tool interaction, ask:** "What tangible artifact did this produce?" If the answer is "proof that the tool works," that is not enough.

### Fix root causes, do not build workarounds

When MCP servers failed to load from `settings.json`, the assistant started building `curl` commands and Python scripts to simulate tool calls. The user stopped this: "I will restart Claude Code now." The fix was putting config in the right file and restarting -- 2 minutes vs. an hour of workaround engineering.

### Work with real data, not synthetic test files

Testing document-loader with a synthetic "hello world" DOCX proves nothing about whether it handles the user's actual documents (Cyrillic text, complex tables, embedded images). Always validate against production data.

### Go deep, not shallow

"MCP setup had issues" teaches nothing. "workspace-mcp OAuth silently expired after 47 minutes, causing the batch document fetch to fail at item 12 of 15 with no error message" teaches everything. Specifics over summaries, always.

### Act when the path is clear

If a gap analysis shows the formal program does not match the lectures, the next step is obviously to rewrite the formal program. Do not ask "what should we do?" when the answer is self-evident. Reserve questions for genuine decision points with multiple valid paths.

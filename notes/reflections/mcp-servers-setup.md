# MCP Servers Setup: What Actually Happened

Detailed post-mortem of installing and configuring 6 MCP servers on 2026-03-31.
Brutally honest account of every misstep, workaround, and time sink.

---

## The Configuration Saga (Start Here)

This deserves top billing because it was the single biggest time sink and affected every server.

### Timeline of Failure

1. **Attempt 1: `.claude/settings.json`**
   Put `mcpServers` block in `.claude/settings.json` following documentation examples and CLAUDE.md patterns. Ran `claude mcp list` -- shows nothing. Zero servers registered. No error message, no warning, just silence.

2. **Attempt 2: `.claude/settings.local.json`**
   Hypothesis: maybe secrets need to go in the `.local` variant. Created `settings.local.json` with env vars containing OAuth credentials and PATs. Still nothing. `claude mcp list` returns empty. Another restart. Still empty.

3. **Attempt 3: `claude mcp add` to `.mcp.json`**
   Out of frustration, tried the CLI command `claude mcp add`. This creates entries in `.mcp.json` at the project root. Suddenly `claude mcp list` shows all servers as connected. Three restarts, four config file iterations, approximately 45 minutes wasted.

### Root Cause

Claude Code reads MCP server configuration from `.mcp.json`, not from `.claude/settings.json`. The `mcpServers` key in `settings.json` either does nothing or serves some other undocumented purpose. Every MCP tutorial and example (including this project's own CLAUDE.md) shows the `settings.json` format. This is a documentation-reality mismatch in Claude Code itself.

### Collateral Damage

- `.mcp.json` contains secrets (PATs, OAuth credentials) by design
- `.mcp.json` is not gitignored by default -- had to add it manually
- `.claude/settings.json` still has a redundant `mcpServers` section that does nothing
- Secrets were briefly in `settings.json` (a tracked file) during attempt 1 -- nearly committed

### Lesson

Use `claude mcp add` exclusively. Do not hand-edit config files for MCP servers. Verify `.mcp.json` is in `.gitignore` before doing anything else.

---

## workspace-mcp (Google Workspace)

**Source:** taylorwilsdon/google_workspace_mcp on GitHub, `workspace-mcp` on PyPI
**Tools:** 115 (the largest server by far)
**Verdict:** Most valuable server, most painful setup

### Installation

1. Needed `uv` (Python package runner) -- not installed. Used the curl installer (`curl -LsSf https://astral.sh/uv/install.sh | sh`). This worked immediately.
2. `uvx workspace-mcp` launches the server. No compilation, no build step.

### OAuth Flow (The 30-Minute Ordeal)

This server requires Google OAuth, not just an API key. The flow:

1. Set `GOOGLE_OAUTH_CLIENT_ID` and `GOOGLE_OAUTH_CLIENT_SECRET` from an existing `dev_bot/.env` file (user's pre-existing Google Cloud project credentials).
2. First attempt to authenticate failed immediately: **redirect_uri_mismatch**. The Google Cloud Console OAuth client did not have `http://localhost:8000/oauth2callback` as an authorized redirect URI. User had to manually add it in the Google Cloud Console.
3. To run the OAuth browser flow, workspace-mcp needs to run as an HTTP server: `uvx workspace-mcp --transport streamable-http --port 8000`. This had to run in a separate terminal because Claude Code's stdio pipe cannot handle browser redirects.
4. First auth URL was generated inside a pipe that died before the user could click it. The URL expired. Had to regenerate.
5. Second fresh URL worked after the redirect URI was added to Google Cloud Console.
6. After successful auth, the token is cached locally. Subsequent launches in stdio mode (the normal MCP mode) work without browser interaction.

### What Actually Works

After setup, this server is genuinely excellent:
- Reads Google Docs as markdown (`get_doc_as_markdown`)
- Lists Drive folders and files
- Creates folders, copies files
- Edits documents (insert, modify, batch update)
- Manages presentations, sheets, forms, Gmail, Calendar, Tasks, Contacts
- Full CRUD on most Google Workspace products

### What Does Not Work Well

- **Bulk document editing is painfully slow.** Editing a large Google Doc one paragraph at a time via MCP API calls took 68 API calls over ~47 minutes for a single document rewrite. The correct approach for bulk rewrites is to draft locally and import as a single operation.
- **No raw file download.** Cannot download a DOCX/XLSX/PPTX binary directly -- that gap is why document-loader was added.

---

## github-mcp-server

**Source:** github/github-mcp-server (official GitHub)
**Tools:** 41
**Verdict:** Works well, but setup has sharp edges

### Installation

1. The npm package (`@github/mcp-server`) was deprecated since April 2025. `npx` would pull a dead package.
2. No Docker image available. No Go compiler on the system to build from source.
3. Found pre-built binary in GitHub releases: `gh release download` for Linux x86_64.
4. Placed binary in `~/.local/bin/github-mcp-server`. Worked immediately.

### Authentication Problem

The server requires `GITHUB_PERSONAL_ACCESS_TOKEN` -- specifically a `ghp_*` Personal Access Token, not the `gho_*` OAuth token that `gh auth` uses. The user's existing `gh` CLI was authenticated with an OAuth token (incompatible).

**Security incident:** User provided the PAT directly in the chat. This means the token is visible in conversation history. Not a breach, but poor hygiene. Should have been pasted into a file or environment variable outside the conversation.

### Scope Limitation

`GITHUB_TOOLSETS=repos,issues,pull_requests` was set to restrict the server to repository, issue, and PR operations only. Without this, the server exposes org-level and admin tools that are unnecessary and risky.

### Overlap with gh CLI

This server overlaps significantly with the built-in `gh` CLI tool. Both can create issues, manage PRs, list branches, etc. The MCP server adds search capabilities and some structured data access, but for simple operations (`gh issue create`, `gh pr create`) the CLI is faster and does not require a separate server.

**Unclear when to prefer one over the other.** Current heuristic: use `gh` CLI for simple CRUD, use github-mcp for search and complex queries.

---

## document-loader (AWS Labs)

**Source:** awslabs/document-loader-mcp-server (official AWS Labs)
**Tools:** 3 (read_document, read_image, extract_slides_as_images)
**Verdict:** Installed smoothly, but never actually tested with a real document

### Installation

`uvx awslabs.document-loader-mcp-server` -- installed and started without issues. The cleanest install of any server.

### Why It Was Added

This server was added **mid-session** as a reactive fix. The original plan had `mcp-local-rag` handling document reading. During actual use, it became clear that local-rag only supports PDF, DOCX, TXT, and MD. The project's Google Drive folder contains XLSX and PPTX files that local-rag cannot read. document-loader fills that gap with full office format support.

### The Honesty Problem

This server was registered, verified as connected, and its 3 tools appeared in the tool list. But **no actual document was read through it during the session.** The server was never tested against a real file. It might have format quirks, encoding issues, or size limits that remain unknown.

Adding an MCP server to the stack without testing it against production data is exactly the kind of premature integration that the roast-before-implement rule is supposed to catch. In this case, we declared it "working" based solely on the process starting successfully.

---

## mcp-local-rag (Local RAG / Semantic Search)

**Source:** shinpr/mcp-local-rag on npm
**Tools:** 6 (ingest_file, ingest_data, query_documents, list_files, delete_file, status)
**Verdict:** Works, but the ingestion workflow was wrong

### Installation

`npx -y mcp-local-rag` -- worked immediately. Node.js was already available.

### Format Limitations

Only supports: PDF, DOCX, TXT, MD. No XLSX, no PPTX, no HTML. This was discovered after installation, not before. The original architecture in CLAUDE.md listed this as the primary document ingestion layer without verifying format coverage. This oversight is why document-loader had to be added reactively.

### The Ingestion Mistake

Three documents were ingested during the session:
- One DOCX file via `ingest_file` (correct -- 196 chunks)
- Two documents via `ingest_data` as raw strings (wrong -- 18+8 chunks)

The `ingest_data` path takes a string and a filename. The problem: the actual content was read from Google Drive via workspace-mcp, converted to a string, and fed directly to `ingest_data` without saving to disk first. This means:

- No local file backup exists for those documents
- The ingest is not reproducible (depends on live Google Drive state at that moment)
- Change detection is impossible (no local file to diff against)
- The chunks are smaller and potentially lower quality than file-based ingestion

**The user caught this.** The correct pipeline is: Google Drive -> export to `catalog/exports/docs/` -> `ingest_file` from the local copy. The shortcut was tempting but wrong.

### Storage Side Effects

RAG creates `lancedb/` and `models/` directories in the project root. These contain the vector database and embedding model files. They are large and must not be committed. Had to add both to `.gitignore` after they appeared.

`BASE_DIR` env var was set in the configuration, but its effect when using `ingest_data` (string-based) versus `ingest_file` (path-based) is unclear.

### Query Quality

Hybrid search (semantic + keyword) returned relevant results in testing. However, the chunk size is small, which causes context loss for complex queries that need multiple paragraphs of context.

---

## drawio (@drawio/mcp)

**Source:** jgraph/drawio-mcp (official jgraph/draw.io)
**Tools:** 3 (open_drawio_xml, open_drawio_csv, open_drawio_mermaid)
**Verdict:** Works, but the "open" model is misleading

### Installation

`npx @drawio/mcp` -- installed and started cleanly.

### The "Open in Browser" Trap

All three tools **open diagrams in a browser**, they do not save files. When `open_drawio_mermaid` is called, it generates a URL and opens it in the default browser. On WSL2 this works because the browser is on the Windows side.

**First diagram attempt:** A Mermaid diagram was generated and "opened" successfully. The diagram appeared in the browser. But nothing was saved to the repository. The user caught this -- a diagram that exists only in a browser tab is useless for version control.

**Second attempt:** A subagent was used to generate the drawio XML directly, write it to `diagrams/lecture-flows/` as a `.drawio` file, and then optionally preview via the MCP tool. This is the correct workflow: file save first, browser preview second.

### API Quirk

The `open_drawio_mermaid` tool accepts a parameter called `content`, not `code`. The first API call used the wrong parameter name and failed silently. No error message, just no diagram. Had to check the tool schema to find the correct parameter name.

### Export Gap

There is no export capability in this MCP server. Converting a `.drawio` file to PNG or SVG requires either the draw.io desktop CLI or LibreOffice. Neither is installed. For now, diagrams exist only as `.drawio` XML files with browser-based preview.

---

## open-ontologies (Oxigraph-based RDF/OWL/SPARQL)

**Source:** fabio-rovai/open-ontologies on GitHub
**Tools:** 43 (by far the richest toolset after workspace-mcp)
**Verdict:** Surprisingly capable, smooth setup, but protocol version matters

### Installation

1. Downloaded Linux binary from GitHub releases.
2. Ran `open-ontologies init` -- created `~/.open-ontologies/` with database, config, and model files.
3. Server started and all 43 tools appeared.

### Protocol Version Gotcha

This server uses MCP protocol version `2024-11-05`. When initially configured with the newer `2025-03-26` protocol version, the tools list came back empty -- zero tools registered despite the server connecting successfully. Switching to the older protocol version restored all 43 tools.

This is a silent failure. The server appears connected, reports no errors, but exposes no tools. Without checking `claude mcp list` output carefully, you would assume the server is broken when it is actually a protocol mismatch.

### What Actually Worked

- Schema loading: `schema.ttl` loaded successfully (65 triples, 8 classes)
- SPARQL queries: `SELECT ?c WHERE { ?c a owl:Class }` returned all 8 expected classes
- Persistent storage: data survives server restarts (stored in `~/.open-ontologies/`)
- Rich toolset: import, query, validate (SHACL), reason (OWL), diff, history, lineage, align, lint

### What Is Not Yet Tested

The 43 tools include advanced features like ontology alignment, drift detection, clinical validation, versioning, and marketplace. None of these were tested. The server was validated for basic load+query only.

The ontology currently has schema only (class and property definitions). No instance data (actual documents, lectures, relationships) has been loaded. The real test will come when entity data is populated.

---

## Overall Assessment

### Time Breakdown (Approximate)

| Activity | Time |
|----------|------|
| Configuration file confusion (settings.json vs .mcp.json) | 45 min |
| workspace-mcp OAuth flow | 30 min |
| github-mcp binary discovery + PAT setup | 15 min |
| document-loader install | 2 min |
| local-rag install + ingestion | 10 min |
| drawio install + first diagram | 10 min |
| open-ontologies install + schema load | 10 min |
| **Total** | **~2 hours** |

Two-thirds of the time was spent on configuration and OAuth, not on actual server usage.

### What Should Have Been Done Differently

1. **Research `.mcp.json` vs `settings.json` BEFORE starting.** A single test with `claude mcp add` for one server would have revealed the correct config location in 2 minutes, saving 45 minutes of guessing.

2. **Verify format support before choosing servers.** The XLSX/PPTX gap in local-rag should have been caught during planning, not during implementation. A 5-minute check of each server's README would have identified document-loader as a day-one requirement.

3. **Test every server against real data before declaring it working.** document-loader was declared "installed" without reading a single document. This is the software equivalent of buying a tool and never taking it out of the box.

4. **Set up OAuth credentials proactively.** The redirect URI issue was foreseeable. Anyone who has done OAuth knows that redirect URIs must be whitelisted. This should have been verified before starting the auth flow.

5. **Never paste secrets into chat.** The PAT should have been set via `export GITHUB_PERSONAL_ACCESS_TOKEN=...` in a terminal, not typed into the conversation.

6. **Always save files before ingesting.** The pipeline should be: source -> local file -> ingest. Skipping the local file step trades reproducibility for speed, and that trade is never worth it.

### Server Value Ranking (After One Session)

| Rank | Server | Why |
|------|--------|-----|
| 1 | workspace-mcp | 115 tools, covers all Google Workspace, irreplaceable |
| 2 | open-ontologies | 43 tools, rich reasoning/validation, replaces planned Oxigraph |
| 3 | local-rag | Semantic search works, essential for knowledge retrieval |
| 4 | github-mcp | Functional but overlaps with gh CLI |
| 5 | drawio | Works but "open in browser" model is awkward; file save requires manual XML |
| 6 | document-loader | Theoretically useful, never actually tested |

### What Is Still Broken or Missing

- **No sync pipeline.** Google Drive -> local export -> RAG ingest does not exist as an automated flow. Every step is manual.
- **No export capability for diagrams.** Cannot convert `.drawio` to PNG/SVG without additional tools.
- **No change detection.** Without local file snapshots, there is no way to detect what changed in Google Drive.
- **Redundant config in settings.json.** The `mcpServers` section in `.claude/settings.json` still exists and does nothing. It should be removed to avoid confusion.
- **document-loader untested.** Needs to be validated against actual XLSX and PPTX files from the project.
- **github-mcp vs gh CLI decision.** No clear policy on when to use which.
- **Protocol version documentation.** The open-ontologies protocol version issue is not documented anywhere obvious.

### The Meta-Lesson

MCP servers are powerful but the ecosystem is immature. Installation is usually trivial (uvx, npx, binary download). Configuration is where everything breaks. Authentication adds another layer of complexity. And the gap between "server is connected" and "server is production-ready" is larger than it appears.

The correct approach for future MCP server additions:
1. Read the README completely, including format limitations and auth requirements
2. Use `claude mcp add` exclusively for registration
3. Verify `.mcp.json` is gitignored
4. Test against real production data before declaring success
5. Document the protocol version that works
6. Never paste credentials into conversations

# Setup Guide

Step-by-step installation of the full MCP stack. Tested on Ubuntu/WSL2 with Node.js 20, Python 3.12, and Claude Code CLI.

Total time: approximately 30 minutes if OAuth credentials are ready, 60+ minutes if you need to create a Google Cloud project first.

---

## 1. Clone the Repo

```bash
git clone <repo-url>
cd AI-usage-lessons
```

## 2. Install uv (Python Package Runner)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify: `uvx --version` should print the version. uv is required for workspace-mcp and document-loader.

## 3. Install MCP Servers

Install all 6 servers using `claude mcp add`. Each command registers the server in `.mcp.json` at the project root. Do NOT edit `.claude/settings.json` for MCP servers -- it does not work.

### 3.1 workspace-mcp (Google Workspace -- 115 tools)

```bash
claude mcp add workspace-mcp --scope project \
  -e GOOGLE_OAUTH_CLIENT_ID=<your-client-id> \
  -e GOOGLE_OAUTH_CLIENT_SECRET=<your-client-secret> \
  -- uvx workspace-mcp
```

Replace `<your-client-id>` and `<your-client-secret>` with values from your Google Cloud Console OAuth 2.0 Desktop client. See step 4 for the OAuth authentication flow.

### 3.2 github-mcp-server (GitHub -- 41 tools)

The npm package `@github/mcp-server` is deprecated. Use the pre-built binary:

```bash
gh release download --repo github/github-mcp-server --pattern "*Linux_x86_64*" -D /tmp
tar -xzf /tmp/github-mcp-server_*_Linux_x86_64.tar.gz -C /tmp
install /tmp/github-mcp-server ~/.local/bin/github-mcp-server
```

Then register:

```bash
claude mcp add github --scope project \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-ghp-token> \
  -e GITHUB_TOOLSETS=repos,issues,pull_requests \
  -- ~/.local/bin/github-mcp-server stdio
```

Use a `ghp_*` Personal Access Token (classic), not the `gho_*` OAuth token from `gh auth`. The `GITHUB_TOOLSETS` restriction limits the server to repo, issue, and PR operations -- no org-level or admin tools.

### 3.3 document-loader (AWS Labs -- 3 tools)

```bash
claude mcp add document-loader --scope project \
  -- uvx awslabs.document-loader-mcp-server@latest
```

Reads PDF, DOCX, XLSX, PPTX, and images. No authentication needed. The cleanest install of any server.

### 3.4 local-rag (Semantic Search -- 6 tools)

```bash
claude mcp add local-rag --scope project \
  -e BASE_DIR=./catalog/exports \
  -- npx -y mcp-local-rag
```

Creates `lancedb/` and `models/` directories in the project root on first use. Both are in `.gitignore`. Supports PDF, DOCX, TXT, MD only -- XLSX and PPTX require document-loader for reading first.

### 3.5 drawio (Diagrams -- 3 tools)

```bash
claude mcp add drawio --scope project \
  -- npx -y @drawio/mcp
```

Tools open diagrams in a browser (Mermaid, XML, CSV). They do NOT save files -- you must write `.drawio` XML to disk separately via the Write tool, then optionally preview with the MCP tool.

### 3.6 open-ontologies (RDF/OWL/SPARQL -- 43 tools)

```bash
gh release download --repo fabio-rovai/open-ontologies --pattern "*linux-gnu*" -D /tmp
install /tmp/open-ontologies ~/.local/bin/open-ontologies
open-ontologies init
```

Then register:

```bash
claude mcp add open-ontologies --scope project \
  -- ~/.local/bin/open-ontologies serve
```

Data persists in `~/.open-ontologies/`. Uses MCP protocol version `2024-11-05` -- if tools show as empty despite successful connection, check for protocol version mismatch.

---

## 4. Google OAuth Authentication

workspace-mcp requires a one-time OAuth flow through a browser.

### Prerequisites

In Google Cloud Console, for your OAuth 2.0 Desktop client:
1. Add `http://localhost:8000/oauth2callback` as an authorized redirect URI
2. Enable the Google Drive API, Google Docs API, Google Sheets API, Google Slides API

**Add the redirect URI BEFORE starting the auth flow. If you start first, it will fail with `redirect_uri_mismatch` and no useful error message.**

### Auth Flow

```bash
# Start workspace-mcp in HTTP mode (separate terminal)
GOOGLE_OAUTH_CLIENT_ID=<id> GOOGLE_OAUTH_CLIENT_SECRET=<secret> \
  uvx workspace-mcp --transport streamable-http --port 8000
```

Open the auth URL that appears in the terminal output. Complete the Google login flow. After successful auth, the token is cached locally. Kill the HTTP server (Ctrl+C).

Subsequent launches in stdio mode (the normal MCP mode used by Claude Code) use the cached token without browser interaction.

---

## 5. Set Permissions

Create `.claude/settings.local.json` (this file is gitignored):

```json
{
  "permissions": {
    "allow": [
      "WebSearch", "WebFetch",
      "Bash(gh:*)", "Bash(git:*)", "Bash(python3:*)", "Bash(claude:*)",
      "Bash(npx:*)", "Bash(uvx:*)", "Bash(ls:*)", "Bash(mkdir:*)", "Bash(chmod:*)", "Bash(curl:*)",
      "Read", "Write", "Edit",
      "mcp__workspace-mcp__*", "mcp__github__*", "mcp__document-loader__*",
      "mcp__local-rag__*", "mcp__drawio__*", "mcp__open-ontologies__*"
    ]
  }
}
```

See [permissions.md](permissions.md) for why wildcards are necessary.

---

## 6. Verify

```bash
# Restart Claude Code to pick up all changes
claude

# Inside Claude Code:
claude mcp list
```

Expected output: 6 servers, all connected. Tool counts: workspace-mcp ~115, github ~41, document-loader ~3, local-rag ~6, drawio ~3, open-ontologies ~43. Total: ~211 tools.

If a server shows 0 tools despite connecting, check:
- Protocol version mismatch (open-ontologies needs `2024-11-05`)
- Missing environment variables (workspace-mcp needs both OAuth vars)
- Binary not found (github-mcp-server, open-ontologies must be in PATH or absolute path)

---

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `claude mcp list` shows nothing | Config in wrong file | Use `claude mcp add`, not manual `.claude/settings.json` editing |
| `redirect_uri_mismatch` during OAuth | Missing redirect URI in Google Cloud Console | Add `http://localhost:8000/oauth2callback` as authorized redirect URI |
| github-mcp shows "invalid token" | Using `gho_*` OAuth token instead of `ghp_*` PAT | Create a classic Personal Access Token with repo scope |
| open-ontologies shows 0 tools | Protocol version mismatch | Ensure server uses protocol `2024-11-05` |
| local-rag fails on XLSX/PPTX | Format not supported | Use document-loader to read the file, then ingest the extracted text via `ingest_file` |
| drawio diagram not saved | MCP tools only open in browser | Write `.drawio` XML to disk with Write tool, then optionally preview with MCP |

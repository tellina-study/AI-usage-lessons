# Secrets Handling

Three secrets are required for the full MCP stack. Every one of them nearly ended up in a committed file during the first session. This document exists because of those near-misses.

---

## Required Secrets

| Secret | Used By | Format | Where to Get It |
|--------|---------|--------|-----------------|
| `GOOGLE_OAUTH_CLIENT_ID` | workspace-mcp | `*.apps.googleusercontent.com` | Google Cloud Console > APIs & Services > Credentials > OAuth 2.0 Client IDs |
| `GOOGLE_OAUTH_CLIENT_SECRET` | workspace-mcp | `GOCSPX-*` | Same location as client ID |
| `GITHUB_PERSONAL_ACCESS_TOKEN` | github-mcp-server | `ghp_*` (classic PAT) | GitHub > Settings > Developer settings > Personal access tokens (classic) |

---

## Where Secrets Live

### `.mcp.json` (project root)

Created automatically by `claude mcp add -e KEY=VALUE`. This file contains the full MCP server configuration including environment variables with secret values. Example:

```json
{
  "mcpServers": {
    "workspace-mcp": {
      "command": "uvx",
      "args": ["workspace-mcp"],
      "env": {
        "GOOGLE_OAUTH_CLIENT_ID": "actual-value-here",
        "GOOGLE_OAUTH_CLIENT_SECRET": "actual-value-here"
      }
    }
  }
}
```

This file MUST be in `.gitignore`. It is added there by default in this repo.

### What goes where

| File | Committed to Git | Contains Secrets | Purpose |
|------|:----------------:|:----------------:|---------|
| `.mcp.json` | NEVER | YES | MCP server registrations with env vars |
| `.claude/settings.local.json` | NEVER | NO (but has permissions) | Tool permission wildcards |
| `.claude/settings.json` | YES | NEVER | Non-secret MCP configs, project settings |
| `.env` | NEVER | YES (if used) | Shell environment variables |

---

## Rules

### 1. All secrets go in `.mcp.json` via `claude mcp add -e`

Never hand-edit `.mcp.json` to add secrets. Use the CLI:

```bash
claude mcp add workspace-mcp --scope project \
  -e GOOGLE_OAUTH_CLIENT_ID=<value> \
  -e GOOGLE_OAUTH_CLIENT_SECRET=<value> \
  -- uvx workspace-mcp
```

### 2. `.mcp.json` MUST be in `.gitignore`

Verify before any MCP configuration:

```bash
grep -q '.mcp.json' .gitignore || echo '.mcp.json' >> .gitignore
```

### 3. `.claude/settings.json` is for non-secret configs ONLY

This file IS committed. It may contain MCP server configs that have no secrets (document-loader, local-rag, drawio, open-ontologies). It must NEVER contain `GOOGLE_OAUTH_CLIENT_ID`, `GOOGLE_OAUTH_CLIENT_SECRET`, `GITHUB_PERSONAL_ACCESS_TOKEN`, or any other credential.

### 4. NEVER accept secrets in chat

If a user pastes a token into the conversation, it enters conversation history stored by the platform. This is not a public breach but means the secret exists in a location outside the user's direct control.

Instead, ask the user to:
- Set an environment variable: `export GITHUB_PERSONAL_ACCESS_TOKEN=ghp_...`
- Or use `claude mcp add -e` directly in their terminal
- Or paste into a local `.env` file that is gitignored

### 5. Verify `.gitignore` before starting any session

The first thing to check in any new session that touches configuration:

```bash
git diff --name-only --cached | grep -E '\.mcp\.json|\.env|settings\.local' && echo "WARNING: secret file staged for commit"
```

---

## What Went Wrong (First Session)

1. **Attempt 1:** OAuth credentials placed in `.claude/settings.json` (a tracked file). Would have been committed if a `git add .` had run at that point.
2. **Attempt 2:** Secrets moved to `.claude/settings.local.json` -- but `.gitignore` did not yet exclude it. Another near-miss.
3. **Attempt 3:** `claude mcp add` wrote secrets to `.mcp.json` -- also not yet in `.gitignore`. Added reactively.
4. **PAT in chat:** The GitHub PAT was provided as plain text in the conversation. Now exists in conversation history.

Every single near-miss was caught manually, not by tooling. The `.gitignore` entries were added after the fact. A pre-commit hook that checks for known secret patterns (`ghp_`, `GOCSPX-`, `*.apps.googleusercontent.com`) would have caught these automatically.

---

## Rotation

If a secret is accidentally committed:

1. **Immediately rotate the credential** (revoke and create new)
2. `git filter-branch` or `git-filter-repo` to remove from history (force-push required)
3. Update `.mcp.json` with the new credential
4. Verify the old credential no longer appears: `git log --all -p | grep 'ghp_'`

Even with force-push and history rewrite, assume the secret was compromised if the repo was ever public or if any clone exists.

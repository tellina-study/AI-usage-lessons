# Permissions Configuration

Claude Code requires explicit permission grants for tools. Without proper permissions, every MCP tool call triggers a confirmation prompt, and subagents fail silently or enter death spirals of denied tool calls.

---

## Recommended Permission Set

Create `.claude/settings.local.json` (this file is gitignored -- never commit it):

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

---

## Why Wildcards

### The subagent permission problem

When Claude Code spawns a subagent (via the Agent tool), the subagent inherits the parent session's permission set. If permissions are granular (e.g., `mcp__workspace-mcp__get_doc_as_markdown`), the subagent may need a tool that was not explicitly listed. It will attempt the call, get denied, try workarounds, get denied again, and eventually produce nothing after 20-40 failed attempts.

This is the "permission death spiral." It was observed in the first session: 6 parallel research subagents each burned 8-12 tool calls trying different approaches, all denied. 44 failed tool calls in one case before the agent gave up.

Wildcards (`mcp__workspace-mcp__*`) prevent this by granting access to all tools on a server. Since you control what MCP servers are installed, server-level wildcards are the right granularity.

### What each permission covers

| Permission | Scope |
|-----------|-------|
| `WebSearch`, `WebFetch` | Web research (orchestrator only -- subagents still cannot use these) |
| `Bash(gh:*)` | GitHub CLI commands |
| `Bash(git:*)` | Git operations |
| `Bash(python3:*)` | Python script execution |
| `Bash(claude:*)` | Claude CLI commands (e.g., `claude mcp list`) |
| `Bash(npx:*)`, `Bash(uvx:*)` | Node.js and Python package runners |
| `Bash(ls:*)`, `Bash(mkdir:*)`, `Bash(chmod:*)` | Basic filesystem operations |
| `Bash(curl:*)` | HTTP requests (for file downloads) |
| `Read`, `Write`, `Edit` | File system read/write operations |
| `mcp__workspace-mcp__*` | All 115 Google Workspace tools |
| `mcp__github__*` | All 41 GitHub tools |
| `mcp__document-loader__*` | All 3 document reading tools |
| `mcp__local-rag__*` | All 6 RAG tools |
| `mcp__drawio__*` | All 3 diagram tools |
| `mcp__open-ontologies__*` | All 43 ontology tools |

### What is NOT permitted (by omission)

- `Bash(rm:*)` -- no file deletion via shell
- `Bash(sudo:*)` -- no privilege escalation
- Arbitrary Bash commands without prefix match -- prevents unrestricted shell access
- MCP servers not in the list -- any new server must be explicitly added

---

## Committed vs. Local Settings

| File | Committed | Contains |
|------|:---------:|---------|
| `.claude/settings.json` | Yes | Non-secret MCP configs (document-loader, local-rag, drawio, open-ontologies) |
| `.claude/settings.local.json` | No | Permission wildcards (as above) |
| `.mcp.json` | No | MCP server registrations with environment variables (secrets) |

The separation is intentional: `.claude/settings.json` can be shared across clones because it has no secrets. `.claude/settings.local.json` and `.mcp.json` must be recreated per installation because they contain credentials or user-specific paths.

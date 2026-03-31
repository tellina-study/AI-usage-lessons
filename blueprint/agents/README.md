# Agent Definitions

This directory contains portable agent definitions for the AI-usage-lessons orchestration system. Each agent is a specialized subagent spawned by Claude Code (the orchestrator) to perform implementation work.

## Agents Overview

| Agent | File | Purpose |
|-------|------|---------|
| **librarian** | [librarian.md](librarian.md) | Search, sync, export, and index documents from Google Drive |
| **course-curator** | [course-curator.md](course-curator.md) | Link normative docs to lectures, maintain ontology relations |
| **doc-editor** | [doc-editor.md](doc-editor.md) | Edit Google Docs content via workspace-mcp |
| **deck-editor** | [deck-editor.md](deck-editor.md) | Build/update Google Slides, insert diagrams |
| **issue-manager** | [issue-manager.md](issue-manager.md) | Create/triage GitHub Issues, manage labels and project board |

## When to Use Each Agent

- **Content discovery or sync needed** -- spawn `librarian`
- **Linking docs to lectures, checking ontology** -- spawn `course-curator`
- **Editing text in a Google Doc** -- spawn `doc-editor`
- **Creating or updating slides** -- spawn `deck-editor`
- **Creating issues, triaging, labeling** -- spawn `issue-manager`

## How to Spawn a Subagent

Use the Claude Code Agent tool. The agent definition file provides the system prompt, and you pass a task-specific user prompt. Example:

```
Agent tool call:
  prompt: <content of librarian.md> + "\n\nTask: Sync the working folder and report new files."
```

In practice, the `.claude/agents/` directory wires this automatically -- Claude Code loads the agent definition from the file and you only provide the task prompt.

## Key Principles

1. **Orchestrator never implements** -- Claude Code plans and delegates; agents do the work.
2. **One agent per concern** -- do not ask librarian to edit slides or doc-editor to create issues.
3. **Issue-driven** -- every agent action traces back to a GitHub Issue.
4. **Tool priority** -- each agent lists its MCP tools in priority order. Prefer higher-priority tools.
5. **Manifest discipline** -- agents that modify catalog state must update the relevant YAML manifest.

# Agent Blueprint: AI-Usage-Lessons

Portable description of a Claude Code agent that manages a project library and semester course. Clone this repo, follow the setup, and you get a working system with Google Workspace integration, semantic search, knowledge graphs, and GitHub automation -- all running inside Claude Code with zero custom backend.

## What This Agent Does

- Syncs documents from Google Drive to a local catalog (Google Docs, DOCX, XLSX, PPTX, PDF)
- Ingests documents into a semantic search index (LanceDB-backed RAG)
- Maintains a knowledge graph of documents, lectures, requirements, and their relationships (RDF/OWL/SPARQL)
- Detects changes and creates GitHub Issues with impact analysis
- Generates and updates lecture slides, diagrams, and course materials
- Orchestrates all work through subagents -- Claude Code is the planner, subagents do implementation

## Prerequisites

- **Claude Code CLI** (latest version)
- **Node.js 20+** (for mcp-local-rag, @drawio/mcp)
- **Python 3.12+** (for workspace-mcp via uvx)
- **uv / uvx** (Python package runner -- installed in setup)
- **GitHub CLI (`gh`)** (for github-mcp-server binary download and repo operations)
- **Google Cloud project** with OAuth 2.0 Desktop client credentials

## Quick Start

1. Clone the repo and install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Run `claude mcp add` for each of the 6 MCP servers (see [setup.md](setup.md))
3. Complete Google OAuth flow for workspace-mcp (see [setup.md](setup.md) step 4)
4. Set permissions in `.claude/settings.local.json` (see [permissions.md](permissions.md))
5. Restart Claude Code, verify with `claude mcp list`

## Architecture

See [architecture.md](architecture.md) for the full MCP stack, data flows, and tool selection rules. The semester roadmap diagram is at `diagrams/lecture-flows/semester-roadmap.drawio`.

## Blueprint Documents

| Document | Contents |
|----------|----------|
| [setup.md](setup.md) | Step-by-step installation of all 6 MCP servers and OAuth |
| [architecture.md](architecture.md) | MCP stack, data flows, tool selection rules |
| [permissions.md](permissions.md) | Permission wildcards and why they matter for subagents |
| [secrets.md](secrets.md) | Where secrets live, what is gitignored, what is committed |
| [conventions.md](conventions.md) | Git workflow, file layout, subagent delegation rules |
| [lessons-learned.md](lessons-learned.md) | Distilled findings from 7 reflection files |

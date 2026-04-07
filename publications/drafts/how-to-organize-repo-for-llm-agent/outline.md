---
title: "How to Organize a Repository for an LLM Agent"
slug: how-to-organize-repo-for-llm-agent
date: 2026-04-07
status: draft
tags: [claude-code, repository, llm-agent, devops]
lang: en
wordpress_url: ""
pair_slug: how-to-organize-repo-for-llm-agent
---

# How to Organize a Repository for an LLM Agent

## Outline

### Target audience
Developers and technical leads who use LLM agents (Claude Code, Copilot Workspace, Cursor, etc.) as development tools and want to structure their repos for maximum agent effectiveness.

### Key thesis
A repository designed for an LLM agent needs explicit conventions, machine-readable metadata, and a clear separation of concerns -- the same things that help human developers, but taken further.

### Planned sections

1. **Why repo structure matters for agents** -- agents read your repo as context; poor structure = poor results
2. **CLAUDE.md / rules files** -- the "briefing document" pattern for agent instructions
3. **Directory layout conventions** -- predictable paths, manifests, catalogs
4. **Ontology and metadata** -- machine-readable relationships between artifacts
5. **Git workflow for agents** -- branch naming, issue-driven work, commit conventions
6. **Templates and skills** -- reusable recipes that agents can follow
7. **What we learned** -- real findings from this project (notes/decisions.md)

### Sources
- This repository's own structure and CLAUDE.md
- notes/decisions.md findings
- Anthropic Claude Code documentation
- Community practices (Cursor rules, Copilot instructions)

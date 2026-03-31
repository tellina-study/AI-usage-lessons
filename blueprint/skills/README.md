# Skill Templates

This directory contains portable skill templates for the AI-usage-lessons orchestration system. Skills are repeatable procedures that agents execute. Each skill maps to a specific agent and has defined dependencies.

## Skills Overview

| Skill | Agent | Dependencies | Priority | Description |
|-------|-------|-------------|----------|-------------|
| `sync-library` | librarian | none | P0 | Sync Google Drive folder with local catalog |
| `catalog-docs` | librarian | sync-library | P0 | Catalog exported documents into manifests |
| `extract-links` | course-curator | catalog-docs | P1 | Extract cross-references and relations from docs |
| `update-lecture` | doc-editor | extract-links | P2 | Update lecture content based on changed sources |
| `build-deck` | deck-editor | update-lecture | P2 | Build/rebuild slide deck from lecture content |
| `diagram-refresh` | deck-editor | catalog-docs | P1 | Refresh diagrams based on content changes |
| `issue-from-change` | issue-manager | sync-library | P1 | Create GitHub Issue when a change is detected |
| `impact-check` | course-curator | extract-links | P1 | Analyze impact of changes across knowledge base |
| `reflect` | (orchestrator) | none | P0 | Post-session reflection and improvement capture |

## Dependency Order

Skills must respect dependencies. The execution graph looks like this:

```
sync-library (P0)
  |
  +---> catalog-docs (P0)
  |       |
  |       +---> extract-links (P1)
  |       |       |
  |       |       +---> update-lecture (P2)
  |       |       |       |
  |       |       |       +---> build-deck (P2)
  |       |       |
  |       |       +---> impact-check (P1)
  |       |
  |       +---> diagram-refresh (P1)
  |
  +---> issue-from-change (P1)

reflect (P0) -- independent, runs after any session
```

## Priority Levels

- **P0** -- Foundation skills. Must work before anything else can run. These are the first to implement and test.
- **P1** -- Core pipeline skills. Enable the feedback loop between document changes and tracked work.
- **P2** -- Content production skills. Create or update student-facing materials.

## Skill Structure

Each skill definition follows this pattern:

```markdown
# skill-name

One-line description.

## When to Use
Trigger conditions -- when should this skill be invoked?

## Inputs
What the skill needs to start (files, IDs, issue references).

## Steps
Numbered procedure the agent follows.

## Outputs
What the skill produces (files updated, issues created, triples written).

## Verification
How to confirm the skill ran correctly.
```

See [sync-library-template.md](sync-library-template.md) for a complete portable example.

## Which Agent Runs Which Skill

| Agent | Skills |
|-------|--------|
| **librarian** | sync-library, catalog-docs |
| **course-curator** | extract-links, impact-check |
| **doc-editor** | update-lecture |
| **deck-editor** | build-deck, diagram-refresh |
| **issue-manager** | issue-from-change |
| **(orchestrator)** | reflect |

## Daily Cycle

The typical daily run executes skills in this order:

1. `sync-library` -- pull changes from Google Drive
2. `catalog-docs` -- update manifests from new exports
3. `extract-links` -- find new cross-references
4. `issue-from-change` -- create issues for detected changes
5. `diagram-refresh` -- update affected diagrams
6. `update-lecture` + `build-deck` -- as needed per issues
7. `reflect` -- end-of-session capture

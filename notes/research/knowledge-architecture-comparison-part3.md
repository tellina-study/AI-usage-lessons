---
title: "Knowledge Architecture for LLM-Native Workflows: Our Design"
part: 3
parts_total: 3
description: "Part 3: Designing a knowledge architecture for 1000+ sources — combining Karpathy's wiki pattern with ontology graphs and hybrid retrieval"
issue: "#18"
epic: "#17"
date: 2026-04-07
---

# Our Architecture: Designing for 1000+ Sources

> Part 3 of 3: From Research to Implementation
> See also: [Part 1 — Seven Approaches](knowledge-architecture-comparison-part1.md) | [Part 2 — Retrieval Strategies](knowledge-architecture-comparison-part2.md)

## Starting Point

We run a course-delivery and knowledge-management system built entirely on Claude Code as the runtime. Current state:
- 27 cataloged documents (Google Docs, Sheets, Slides)
- RDF ontology with 8 entity types, 7 relation types (Oxigraph via open-ontologies MCP)
- LanceDB vector store with 2-4 documents ingested
- 6 MCP servers (workspace-mcp, github, document-loader, local-rag, drawio, open-ontologies)
- Target: **thousands of sources and papers**

## What We Learned from the Research

### From Karpathy's LLM Wiki
- The 3-layer pattern (raw/wiki/schema) is the right foundation
- Compilation (raw -> wiki pages) is the key operation, not manual curation
- Index-first retrieval works up to ~500 sources — beyond that, you need vector search
- Concept extraction (auto-discovering cross-cutting themes) is more valuable than per-document summaries
- Coverage indicators (high/medium/low) tell users when to trust the wiki vs go to raw sources
- Incremental compilation (only recompile changed topics) is essential for maintainability

### From Zettelkasten/Dendron
- Dot-separated naming (or hierarchical folders) scales better than flat files
- Bidirectional links with backlink sections create navigable knowledge webs
- PageRank-sorted backlinks surface the most important connections
- Schemas/templates enforce consistency at scale

### From Docs-as-Code
- Formal content types (concept, task, reference) help both humans and LLMs navigate
- Build-time validation of cross-references catches broken links early
- Number-prefixed files provide deterministic ordering
- At 3000+ pages, build/compilation time becomes a real constraint

### From Johnny Decimal
- Numeric discipline is great for bounded, stable collections (lectures, seminars)
- But the 10x10 limit makes it unsuitable for open-ended collections (papers, research notes)
- The JDex (index file) pattern is useful even without the full numbering system

### What Breaks at Scale
- Flat folder structures collapse at ~200 files
- Single index files exceed 600 lines at ~300 sources
- Full graph rebuilds (Foam-style) become expensive at 1000+ linked notes
- Manual cross-referencing is unsustainable past ~50 documents
- PARA reclassification becomes a bottleneck past ~200 items

## Proposed Architecture

### Three Layers (Karpathy-adapted)

```
CLAUDE.md              -- Schema layer: conventions, content types, cross-ref rules
raw/                   -- Source layer: immutable inputs
  exports/             -- Google Drive exports (markdown, from workspace-mcp)
  papers/              -- PDFs, external papers (from document-loader MCP)
    by-topic/          -- Topic-based organization
  research/            -- Research notes (moved from notes/research/)
wiki/                  -- Wiki layer: LLM-compiled, auto-maintained
  index.md             -- Master index (taxonomy navigator, not full listing)
  topics/              -- Hierarchical topic pages
    ai-ethics/
      _index.md        -- Topic overview + sub-topic listing
      bias-fairness.md -- Sub-topic page
      ...
    prompt-engineering/
      _index.md
      ...
  lectures/            -- One summary per lecture (17 total)
    lec-01.md
    ...
  documents/           -- One summary per cataloged document
  concepts/            -- Cross-cutting concept pages (auto-discovered)
  glossary.md          -- Terms and definitions
```

### Content Types

| Type | Location | Template | Growth Pattern |
|------|----------|----------|----------------|
| Topic index | `wiki/topics/{topic}/_index.md` | topic-index.md | Splits into sub-topics when >100 sources |
| Topic page | `wiki/topics/{topic}/{subtopic}.md` | topic-page.md | One per sub-topic |
| Lecture summary | `wiki/lectures/lec-NN.md` | lecture-summary.md | Fixed at 17 |
| Document summary | `wiki/documents/{slug}.md` | document-summary.md | Grows to thousands |
| Concept page | `wiki/concepts/{concept}.md` | concept-page.md | Auto-discovered, grows organically |
| Paper note | `wiki/papers/{slug}.md` | paper-note.md | Grows to thousands |
| Decision record | `notes/decisions/{slug}.md` | decision-record.md | Low volume, stable |
| Reflection | `notes/reflections/{date}-{topic}.md` | reflection.md | Session-based |

Each type has YAML frontmatter with: title, type, topics (list), sources (list), status, coverage (high/medium/low), updated_at.

### Hierarchical Index Design

At 1000+ sources, a single `index.md` won't work. The index is a **tree**:

```
wiki/index.md                           -- Master: 17 topic clusters with counts
  -> wiki/topics/ai-ethics/_index.md    -- Topic: 47 sources, 5 sub-topics
    -> wiki/topics/ai-ethics/bias.md    -- Sub-topic: 12 sources detailed
```

Master index entry format:
```markdown
## AI Ethics (47 sources, 5 sub-topics)
Core questions: bias detection, fairness metrics, regulatory compliance, transparency, accountability
Lectures: 14, 15 | Key papers: [Smith2024], [EU-AI-Act]
-> [Full topic index](topics/ai-ethics/_index.md)
```

Auto-split rule: when a topic index exceeds 300 lines, spawn sub-topic pages.

### 4-Tier Retrieval Pipeline

```
Query --> Intent Classification
  |
  |--> Navigational ("show me lecture 5") --> Tier 1: Wiki Index
  |--> Relational ("what depends on RPD?") --> Tier 2: Ontology SPARQL
  |--> Semantic ("papers about fairness") --> Tier 3: Vector Search
  |--> Exact ("find ERROR_4532") --> Tier 4: Grep
  |
  v
Merge via RRF --> Answer with provenance (which tier found what)
```

**Tier 1 — Wiki Index:** Read master index, drill into topic/lecture pages. Near-zero cost. Handles: navigation, "everything about X", overview queries.

**Tier 2 — Ontology SPARQL:** Traverse typed relationships. Handles: dependencies ("what does Lecture 3 depend on?"), impact analysis ("if RPD changes, what breaks?"), provenance ("where does this requirement come from?"). Extended ontology with hierarchical topic taxonomy.

**Tier 3 — Vector Search:** LanceDB embeddings over all wiki + raw content. Handles: fuzzy/conceptual discovery, synonym matching, "find similar papers". This is a CORE tier at 1000+ sources, not a fallback.

**Tier 4 — Full-text Grep:** ripgrep for exact matches. Handles: specific IDs, error codes, exact phrases, proper names.

### Compilation Pipeline (Skill: /compile-wiki)

Inspired by sage-wiki's 5-pass pipeline, adapted for Claude Code + MCP:

1. **Diff:** Compare raw/ against wiki manifest (content hashes). Identify added/modified/removed sources.
2. **Summarize:** Subagent reads new/changed raw sources, generates summaries.
3. **Extract concepts:** Identify cross-cutting concepts spanning 3+ topics. Merge with existing concepts.
4. **Compile pages:** Generate/update wiki pages per topic, lecture, document, concept. Include coverage indicators.
5. **Link & index:** Generate cross-links, backlinks, update hierarchical indexes. Validate all links.

Incremental: only recompile topics whose sources changed. Full recompile on schema changes.

### Ontology Extension

Current: 8 entity types, 7 relations, ~20 instances.
Target: hierarchical topic taxonomy, thousands of entity instances, rich cross-references.

New entity types:
- `aul:Paper` — external academic paper
- `aul:Concept` — cross-cutting concept (auto-discovered)
- `aul:SubTopic` — sub-topic within a topic hierarchy

New relations:
- `aul:subtopic_of` — topic hierarchy
- `aul:cites_paper` — document/lecture references a paper
- `aul:related_concept` — concept-to-concept links

### Migration from Current State

Phase 1: Restructure (no content changes)
- Create wiki/, raw/ directories
- Move catalog/exports/docs/ -> raw/exports/
- Move notes/research/ -> raw/research/
- Reorganize notes/ into decisions/, reflections/
- Update CLAUDE.md, manifests, skills

Phase 2: Initial compilation
- Compile wiki pages from existing 27 documents
- Generate master index + topic indexes
- Populate ontology with all instances and relations
- Ingest everything into RAG

Phase 3: Scale preparation
- Create bulk import workflow for papers
- Test with 100 papers
- Validate hierarchical index auto-splitting
- Benchmark 4-tier retrieval

## What This Does NOT Include (Intentional Simplifications)

- No custom web UI — Claude Code is the only interface
- No real-time sync — compilation is triggered manually or by skill
- No multi-user access control — single maintainer
- No GraphRAG-style LLM community detection — too expensive for our budget, revisit later
- No automated paper discovery/crawling — manual import, then auto-processing

## Self-Roast (Pre-Implementation)

**Risk: Over-engineering.** 4 tiers, 5-pass pipeline, hierarchical indexes — is this simpler than what we have? Counter: what we have doesn't work at all for "find me everything about X." The complexity is earned.

**Risk: Wiki goes stale.** If compilation isn't triggered regularly, wiki diverges from raw sources. Mitigation: coverage indicators show staleness; /compile-wiki integrated into daily cycle.

**Risk: Ontology cold-start.** Populating thousands of entities is expensive. Mitigation: auto-extract from wiki compilation, not manual entry.

**Risk: LanceDB at thousands of docs.** Current setup has 2-4 docs. Will bulk ingestion work? Mitigation: test with 100 papers in Phase 3 before committing.

**Risk: 600-line limit creates too many small files.** At 1000 sources with topic pages, sub-topic pages, concept pages — we could have 500+ wiki files. Counter: that's the point. Many small, focused files > few huge files. The index tree makes them navigable.

## Next Steps

1. **#19** — Finalize this design with user feedback
2. **#20** — Define 3 test scenarios against current system
3. **#21** — Implement folder structure + initial compilation
4. **#22** — Implement 4-tier retrieval pipeline
5. **#23** — Run tests, compare before/after
6. **#24** — Roast, improve, update blueprint

## References

- Karpathy LLM Wiki pattern — [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- sage-wiki 5-pass pipeline — [GitHub](https://github.com/xoai/sage-wiki)
- ussumant/llm-wiki-compiler — coverage indicators, 81x compression
- Dendron dot-hierarchy — [GitHub](https://github.com/dendronhq/dendron)
- Kubernetes content types — [content guide](https://kubernetes.io/docs/contribute/style/content-guide/)
- HybridRAG — [arXiv 2408.04948](https://arxiv.org/abs/2408.04948)
- Microsoft GraphRAG — [arXiv 2404.16130](https://arxiv.org/html/2404.16130v2)

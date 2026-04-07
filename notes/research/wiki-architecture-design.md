---
title: "Wiki Architecture Design (v2 — Test-Informed)"
type: decision-record
issue: "#19"
epic: "#17"
date: 2026-04-07
status: approved
supersedes: "deleted draft v1"
---

# Wiki Architecture Design v2

## Decision

Adopt a 3-layer knowledge architecture (existing files + wiki index + knowledge graph) with 4-tier retrieval, designed for 3000+ sources. Informed by 6 baseline tests (3 tool tests + 3 E2E).

## Scale Context

- Lecture 1 references 204 external sources (110 papers, 60 websites, 20 books)
- 15 PDFs already downloaded, 7 research files written
- At 17 lectures with similar density: **3,000-3,500 sources** at full build-out
- Current indexed content: 16 files in RAG, 0 functional ontology triples

## Baseline Performance (2026-04-07)

| Scenario | E2E Quality | E2E Cost | Tool Test: Ontology | Tool Test: RAG |
|----------|-------------|----------|---------------------|----------------|
| 1: Single-doc | 13/9 found | 29 calls, 62s, 143K tokens | 0 results (empty store) | 0 relevant (notes/ not indexed) |
| 2: Cross-doc | 8/8 found | 35 calls, 88s, 151K tokens | 0 results (no agent topics) | 1 relevant EN, 0 RU |
| 3: Multi-hop | 5/5 hops | 32 calls, 79s, 123K tokens | Failed (syntax error + 0 instances) | Partial (fragments only) |

**Key finding:** Quality is already high via brute-force. The problem is cost (30+ calls, 60-90s). Two tiers are completely broken (ontology, RAG scope).

## What Changes vs Original Design (Part 3)

| Original Part 3 | v2 Change | Reason |
|-----------------|-----------|--------|
| Move catalog/exports/ -> raw/exports/ | **Keep existing paths** | Breaks skills, manifests, CLAUDE.md — rename cost exceeds benefit |
| Move notes/research/ -> raw/research/ | **Keep in notes/** | Research notes are our work, not "raw immutable sources" |
| 5-pass compilation pipeline | **Simplify to 3-pass** | Full sage-wiki pipeline is overkill for single maintainer |
| Content type templates (all 6) | **Keep all 6** | At 200+ sources per lecture, consistency templates are needed now |
| Hierarchical indexes "later" | **Hierarchical from start** | 204 sources for Lecture 1 alone busts flat index |
| Paper/Concept ontology "deferred" | **Add now** | 204 papers need tracking in ontology |
| Folder restructuring | **Minimal: add wiki/ and raw/papers/ only** | Don't move existing content, just add new layers |

## Folder Structure

### Additions (new directories only — no moves)

```
wiki/                              # NEW: LLM-compiled knowledge index layer
  index.md                         # Master index (taxonomy navigator, ~50-80 lines)
  topics/                          # One folder per top-level topic
    ai-fundamentals/
      _index.md                    # Topic index: sources, papers, lectures, sub-topics
    ai-ethics/
      _index.md
    ai-agents/
      _index.md
    ...                            # ~15-20 topic folders
  lectures/                        # One summary per lecture
    lec-01.md                      # Cross-links to research, papers, assessments
    ...
  documents/                       # One summary per cataloged document
  concepts/                        # Cross-cutting concepts (auto-discovered)
  papers/                          # Paper notes (one per ingested paper)
  glossary.md
raw/                               # NEW: External papers and bulk imports
  papers/
    inbox/                         # Drop zone for unclassified papers
    classified/                    # Auto-classified by topic
      ai-fundamentals/
      ai-agents/
      ...
    lecture-1/                     # Already exists at library/papers/lecture-1/
```

### Existing (unchanged)

```
catalog/exports/docs/              # KEEP: Google Drive markdown exports (16 files)
catalog/exports/viz/               # KEEP: visualizations
catalog/manifests/                 # KEEP + add wiki-manifest.yaml
notes/research/lecture-1/          # KEEP: 7 research files (richest content)
notes/decisions.md                 # KEEP (split into notes/decisions/ later if needed)
notes/reflections/                 # KEEP
ontology/                          # KEEP + fix + populate
library/papers/lecture-1/          # KEEP: 15 PDFs + index.yaml (gitignored PDFs)
```

### Migration Note
library/papers/ and raw/papers/ will coexist initially. New papers go to raw/papers/. Existing library/papers/lecture-1/ stays until we decide to consolidate. No breaking changes.

## Wiki Index Design (Hierarchical from Start)

### Master Index (wiki/index.md)

Taxonomy navigator, NOT a full listing. At 3000+ sources, this must be a 50-80 line entry point.

```markdown
# Knowledge Base Index
> Sources: 204 (Lecture 1) | Topics: 15 | Papers: 15 downloaded
> Last compiled: 2026-04-07

## Course Structure
- [Lectures](lectures/) — 17 lectures
- [Documents](documents/) — 27 cataloged
- [Glossary](glossary.md)

## Topics
- [AI Fundamentals](topics/ai-fundamentals/_index.md) — 45 sources, 9 sub-taxonomies
- [AI Agents](topics/ai-agents/_index.md) — 30 sources, 8 papers
- [AI Ethics](topics/ai-ethics/_index.md) — 12 sources
- [AI in Software](topics/ai-in-software/_index.md) — 15 sources
- [AI in Finance](topics/ai-in-finance/_index.md) — 10 sources
- ...

## Recent Changes
- 2026-04-07: Lecture 1 research complete, 15 papers downloaded
```

### Topic Index (wiki/topics/{slug}/_index.md)

Each topic gets its own index page. At 200+ sources for some topics, these will grow and may need sub-topic pages.

```markdown
---
title: "AI Fundamentals"
type: topic-index
sources_count: 45
sub_topics: [classification-taxonomies, history, definitions, benchmarks]
lectures: [1, 2]
coverage: high
updated_at: 2026-04-07
---

# AI Fundamentals

## Sub-topics
- **Classification Taxonomies** (9 taxonomies, 25 papers)
  - Primary: notes/research/lecture-1/classifications.md
  - Papers: library/papers/lecture-1/ (vaswani-2017, bommasani-2021, ...)
- **History and Definitions** (30+ sources)
  - Primary: notes/research/lecture-1/history-and-definitions.md
- **Human vs AI Capabilities** (20+ sources)
  - Primary: notes/research/lecture-1/human-vs-ai.md
- **Benchmarks (ARC-AGI, ImageNet)** (10 sources)
  - In: notes/research/lecture-1/human-vs-ai.md

## Lectures
- [[lec-01]] — introduction, covers all sub-topics
- [[lec-02]] — AI in software development (uses classification framework)

## Key Documents
- [[prog-otraslevoe-updated-formal]] — RPD: PKS-3 requires classification competency
- [[course-structure]] — LO1 maps to classification

## Assessment
- Sem 5 (Midterm 1): classification accuracy rubric, 0-3 pts
- Sem 17 (Final Exam): classification accuracy rubric, 0-3 pts
```

Auto-split rule: when a topic _index.md exceeds 400 lines, move sub-topic details into separate files.

### Lecture Summary (wiki/lectures/lec-NN.md)

```markdown
---
title: "Lecture 1: Introduction"
type: lecture-summary
number: 1
topics: [ai-fundamentals, ai-in-industry]
source_doc: "1UX671dOrhfQ8OgnadD_8ce4dhVJ9wDVrFqPq6p9S9uo"
coverage: high
updated_at: 2026-04-07
---

# Lecture 1: Introduction

## Topics Covered
- AI Fundamentals: 9 classification taxonomies
- AI in Industry: overview of applications

## Research Notes
- notes/research/lecture-1/classifications.md (184 lines, 9 taxonomies)
- notes/research/lecture-1/model-chat-agent-app.md (295 lines, agent architectures)
- notes/research/lecture-1/human-vs-ai.md (capabilities comparison)
- notes/research/lecture-1/history-and-definitions.md (foundations)
- notes/research/lecture-1/security-local-cloud.md (data privacy)
- notes/research/lecture-1/teaching-examples.md (pedagogy)
- notes/research/lecture-1/industry-examples.md (market data)

## Papers (15 downloaded)
See library/papers/lecture-1/index.yaml

## Normative Requirements
- PKS-3 -> LO1: classify AI solution types (assessed Sem 5 + Sem 17)

## Materials
- Plan: catalog/exports/docs/lec-01-plan.md
- Slides: catalog/exports/slides/lec-01-slides.pptx
```

## Ontology Design

### Phase 1: Fix and Populate Existing Schema

1. **Fix store.ttl syntax error** (line 136 missing period)
2. **Add 17 Lecture instances** with labels, source_urls, topics
3. **Add covers triples** linking lectures to topics
4. **Add PKS-3 Requirement** with indicators (KNOW, ABLE)
5. **Add belongs_to_topic** for all Document instances
6. **Verify 3 pre-written SPARQL queries return real data**

### Phase 2: Extend Schema for Papers

7. **Add Paper class** — external academic paper
8. **Add Concept class** — cross-cutting concept
9. **Add subtopic_of** — hierarchical topic taxonomy (9 classification sub-taxonomies)
10. **Add cites_paper** — document/lecture references a paper
11. **Add related_concept** — concept-to-concept links
12. **Add LearningOutcome class** — links Requirements to Lectures
13. **Add assessed_by property** — links Requirements to Seminars

### Target State
- 17 Lecture instances
- 15+ Topic instances (with subtopic_of hierarchy)
- 10+ Requirement/LO instances
- 200+ Paper instances (as we ingest Lecture 1 sources)
- covers, cites_paper, assessed_by triples forming traversable graph

### Scenario 3 as Single SPARQL Query (target)
```sparql
PREFIX aul: <https://ai-usage-lessons.local/ontology#>
SELECT ?req ?lo ?lecture ?research ?paper ?seminar WHERE {
  ?req a aul:Requirement ; aul:label "PKS-3" .
  ?lo aul:fulfills ?req .
  ?lecture aul:covers ?lo .
  ?research aul:supports ?lecture .
  ?research aul:cites_paper ?paper .
  ?seminar aul:assesses ?lo .
}
```

## RAG Design

### Phase 1: Expand Scope (fix blind spots)

1. **Ingest notes/research/lecture-1/*.md** (7 files, 2000+ lines) — the richest content, currently invisible
2. **Ingest 15 downloaded PDFs** via document-loader -> local-rag pipeline
3. **Re-test Russian queries** — if still poor (scores <0.3), proceed to Phase 2

### Phase 2: Scale and Multilingual

4. **Evaluate multilingual embedding model** — current Xenova/all-MiniLM-L6-v2 is English-optimized, Russian scores 0.19-0.31
5. **Bulk ingestion workflow** — script or skill for ingesting 50+ papers at once
6. **Filtered search** — scope queries by topic, document type, or lecture number

### Target State
- ALL research notes indexed (currently 0)
- ALL downloaded papers indexed (currently 0)
- ALL catalog exports indexed (currently 16 — keep)
- Russian queries returning relevant results (currently 0)
- Bulk ingest capability for future lecture research

## Compilation Pipeline (Simplified)

3-pass pipeline, not 5-pass. Runs as /compile-wiki skill.

### Pass 1: Catalog
- Scan catalog/manifests/, notes/research/, library/papers/ for all sources
- Compare against wiki-manifest.yaml (content hashes)
- Output: list of new/changed/removed sources

### Pass 2: Compile
- For new/changed sources: generate/update wiki pages (topic indexes, lecture summaries, paper notes)
- Use templates from templates/wiki/
- Include coverage indicators (high/medium/low based on source count)
- Auto-classify papers by topic

### Pass 3: Index
- Regenerate wiki/index.md and all topic _index.md pages
- Generate cross-links between wiki pages
- Update wiki-manifest.yaml with new hashes
- Ingest new content into RAG
- Update ontology with new instances/relations
- Report: what changed, what was compiled

### Incremental: Only recompile topics whose sources changed.

## Cross-Reference Conventions

- Wiki pages: `[[slug]]` resolves to wiki/{type}/{slug}.md
- Source files: relative path `[text](../../notes/research/lecture-1/file.md)`
- Google Drive: `[title](https://docs.google.com/...)`
- Ontology: `ontology:entity_id` (informational)
- GitHub: `#NN`

Coverage indicators in frontmatter:
- **high** (5+ sources) — trust wiki, skip sources
- **medium** (2-4) — wiki is overview, check sources for detail
- **low** (0-1) — placeholder, read sources directly

## Content Type Templates

6 templates in templates/wiki/ (already created in earlier draft, to be re-created):
1. **topic-index.md** — topic page with sub-topics, sources, lectures, papers
2. **lecture-summary.md** — lecture overview with cross-links
3. **document-summary.md** — Google Drive document metadata + key info
4. **paper-note.md** — academic paper summary + relevance
5. **concept-page.md** — cross-cutting concept definition + trade-offs
6. **decision-record.md** — ADR-style decision documentation

## /compile-wiki Skill (Phased)

The `/compile-wiki` skill exists from Phase 1 and grows in capability each phase. This avoids the "ontology/RAG go stale" problem — one skill, always available, increasingly powerful.

**Skill file:** `.claude/skills/compile-wiki/SKILL.md`

| Phase | Capability | Trigger |
|-------|-----------|---------|
| 1 (Reindex) | Load ontology + ingest all sources into RAG + verify | After /sync-library, /update-lecture, /catalog-docs, or manual paper import |
| 2 (Populate) | Phase 1 + add Lecture/Requirement/LO instances to ontology | After new lecture content is created |
| 3 (Generate) | Phase 2 + create wiki/ pages (index, topic indexes, lecture summaries) | After significant content changes |
| 4 (Full) | Phase 3 + incremental 3-pass compilation with change detection | Daily cycle or on demand |

**Integration with existing skills:**
- `/sync-library` Step 7: reminds user to run `/compile-wiki` after syncing Drive exports
- `/update-lecture` Step 9: reminds user to run `/compile-wiki` after creating lecture content
- `/catalog-docs` Step 8: reminds user to run `/compile-wiki` after cataloging new documents

**Daily cycle update:**
1. Sync: `/sync-library` pulls changes from Drive
2. **Compile: `/compile-wiki` updates RAG, ontology, and wiki indexes**
3. Catalog: `/catalog-docs` + `/extract-links` update manifests
4. Tasks: `/issue-from-change` creates issues from changes

## Implementation Phases

### Phase 1: Fix Broken Infrastructure + compile-wiki Phase 1
- [ ] Fix store.ttl syntax error (line 136)
- [ ] Populate ontology: 17 lectures, topic-lecture covers, PKS-3 requirement
- [ ] Create `/compile-wiki` skill (Phase 1: reindex)
- [ ] Run `/compile-wiki` — ingest all sources into RAG, load ontology
- [ ] Re-run tool tests for ontology and RAG — verify they return results
- **Gate:** ontology returns data for all 3 SPARQL queries, RAG finds research notes, `/compile-wiki` runs successfully

### Phase 2: Wiki Index Layer + compile-wiki Phase 2-3
- [ ] Create wiki/ directory structure
- [ ] Create wiki/index.md (master index)
- [ ] Create wiki/topics/ with 8+ topic _index.md pages
- [ ] Create wiki/lectures/lec-01.md (first lecture summary)
- [ ] Create templates/wiki/ (6 templates)
- [ ] Create catalog/manifests/wiki-manifest.yaml
- [ ] Extend ontology schema (Paper, Concept, subtopic_of, cites_paper, LearningOutcome, assessed_by)
- [ ] Advance `/compile-wiki` to Phase 2-3 (populate ontology + generate wiki pages)
- **Gate:** wiki index navigable, topic pages list all known sources, `/compile-wiki` generates pages

### Phase 3: Paper Storage and Bulk Ingestion
- [ ] Create raw/papers/ structure (inbox/, classified/)
- [ ] Build bulk ingestion into `/compile-wiki` Phase 3
- [ ] Test with remaining Lecture 1 sources (189 not yet downloaded)
- [ ] Update .gitignore for raw/papers/ PDFs
- **Gate:** can ingest 50+ papers in one `/compile-wiki` run

### Phase 4: Full Compilation Pipeline
- [ ] Advance `/compile-wiki` to Phase 4 (incremental 3-pass)
- [ ] Test incremental compilation (change 1 source, verify only affected pages recompile)
- [ ] Integrate into daily cycle
- **Gate:** compilation detects changes and only recompiles affected pages

### Re-Test
- [ ] Run all 3 E2E scenarios in fresh sessions
- [ ] Run all 3 tool test scenarios
- [ ] Compare against baselines
- [ ] Update issues #27, #28, #29 with post-improvement metrics

## Improvement Targets

| Scenario | Baseline E2E | Target E2E |
|----------|-------------|------------|
| 1: Single-doc | 29 calls, 62s, 143K tokens | <=3 calls, <10s |
| 2: Cross-doc | 35 calls, 88s, 151K tokens | <=5 calls, <20s |
| 3: Multi-hop | 32 calls, 79s, 123K tokens | <=5 calls, <15s |

## Risks

| Risk | Mitigation |
|------|-----------|
| Wiki pages go stale | Coverage indicators show staleness; /compile-wiki in daily cycle |
| Ontology cold-start (populating 200+ papers) | Auto-extract from compilation, not manual entry |
| RAG Russian still poor after re-indexing | Evaluate multilingual model (paraphrase-multilingual-MiniLM-L12-v2) |
| Too many wiki files (500+ at scale) | Hierarchical index tree makes them navigable; grep still works |
| Breaking existing skills during migration | Phase 1-2 only ADD new paths, never move existing content |

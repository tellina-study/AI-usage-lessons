---
title: "Wiki Architecture Roast: Test-Informed Design Review"
type: decision-record
issue: "#19"
epic: "#17"
date: 2026-04-07
status: review
---

# Wiki Architecture Roast

Based on 3 tool test baselines + 3 E2E baselines run on 2026-04-07.

## What the Tests Actually Showed

### The System Already Works (Expensively)

E2E results across all 3 scenarios:

| Scenario | Quality | Tool Calls | Time | Tokens |
|----------|---------|------------|------|--------|
| 1: Single-doc | 13/9 (found extras) | 29 | 61.6s | 143K |
| 2: Cross-doc | 8/8 + bonus | 35 | 87.9s | 151K |
| 3: Multi-hop | 5/5 hops complete | 32 | 79.4s | 123K |

The system delivers correct, comprehensive answers by brute-force grep+read via Explore agents. It compensates for missing infrastructure (ontology, RAG, wiki) by reading many files.

**This means:** The quality bar is already high. Any architecture change must either:
- Reduce cost (calls, time, tokens) while maintaining quality, OR
- Enable queries that brute-force cannot answer

### What's Actually Broken (Tool Tests)

| Component | Status | Impact |
|-----------|--------|--------|
| **Ontology store** | 0 triples loaded, syntax error in store.ttl line 136 | Tier 2 completely non-functional |
| **RAG index scope** | Only catalog/exports/ indexed (16 files) | notes/research/ (2000+ lines, richest content) invisible |
| **RAG Russian** | Scores 0.19-0.31, zero relevant results | Cross-language retrieval broken |
| **Cross-references** | None exist between files | Every query requires re-discovering connections |
| **File discoverability** | Requires knowing paths or brute-force grep | The #1 bottleneck -- grep finds files but not answers |

### What's NOT Broken

- **Grep works well** for file discovery (finds right files in 1-4 calls)
- **File content is rich** -- classifications.md, model-chat-agent-app.md are well-structured
- **Explore agent compensates** -- 28-34 calls is expensive but produces excellent results
- **Research notes quality is high** -- the content itself needs no improvement

## Roast of Proposed Architecture

### 1. The 5-Pass Compilation Pipeline Is Over-Engineered

**Proposed:** diff -> summarize -> extract concepts -> compile pages -> link & index

**Reality:** We have 27 documents. sage-wiki built this for production with hundreds of users. We have one maintainer. The Explore agent already synthesizes answers in 60-90s.

**Verdict:** Start with a 2-pass pipeline: (1) index/catalog all files with metadata, (2) generate cross-links. Skip summarization and concept extraction until we have 100+ sources. A simple file index that maps topics to file paths would eliminate the #1 bottleneck (discoverability) at near-zero cost.

### 2. Wiki Topic Pages May Not Add Much Value

**Proposed:** LLM-compiled wiki/topics/{topic}/_index.md pages aggregating all sources.

**Test evidence:** The E2E Explore agent effectively creates a "temporary wiki page" on every query -- it reads files, synthesizes, and presents a structured answer. A pre-compiled wiki page would save the 60-90s compute but goes stale between compilations.

**Verdict:** The real value isn't the compiled summary (the LLM can do that on-the-fly). The value is the **index** -- knowing WHICH files to read. A lightweight index.md mapping topics to file paths + brief descriptions would capture 80% of the value at 10% of the implementation cost.

### 3. Folder Restructuring Has High Cost, Unclear Benefit

**Proposed:** Move catalog/exports/docs/ -> raw/exports/, notes/research/ -> raw/research/, reorganize notes/ into subdirectories.

**Test evidence:** The E2E agents found everything using current paths. Moving files breaks every existing skill, manifest, and path reference in CLAUDE.md.

**Verdict:** Keep existing folders. Add raw/papers/ for new paper imports (this IS needed -- no current place for PDFs). Add wiki/ for the index layer. Don't move existing content -- the naming is fine, the structure works, the cost of migration exceeds the benefit.

**Exception:** raw/papers/inbox/ and raw/papers/classified/ ARE worth creating -- we have 15 PDFs with no home except library/papers/ which is gitignored. But this is a minor addition, not a restructuring.

### 4. The 4-Tier Retrieval Pipeline Is Right, But Priorities Are Wrong

**Proposed order:** Wiki Index -> Ontology -> Vector -> Grep

**Test evidence priority order:**
1. **Fix RAG scope** (Tier 3) -- notes/research/ not indexed is the single biggest blind spot. Adding 7 files to RAG would immediately make semantic search useful.
2. **Fix ontology data** (Tier 2) -- schema is correct, store is empty. Loading the existing store.ttl (after fixing syntax error) would enable SPARQL queries.
3. **Create wiki index** (Tier 1) -- a simple index.md mapping topics to files would eliminate the discoverability bottleneck.
4. **Grep already works** (Tier 4) -- no changes needed.

**Verdict:** Don't build the orchestration pipeline first. Fix the two broken tiers (RAG + ontology), then see if a simple index suffices before building complex retrieval routing.

### 5. Content Type Templates Are Premature

**Proposed:** 6 content type templates (topic-index, lecture-summary, document-summary, paper-note, concept-page, decision-record).

**Test evidence:** The E2E agents produce better answers than any template would because they read source files directly and synthesize context-aware responses.

**Verdict:** Create templates only when we start actually compiling wiki pages. For now, the only template needed is the wiki index entry format. Save template work for when we have 100+ sources and need consistency.

### 6. Ontology Schema Extension Is Good But Instance Data Matters More

**Proposed:** Add Paper, Concept, subtopic_of, cites_paper, related_concept classes/properties.

**Test evidence:** The EXISTING schema (Lecture, Requirement, Topic, covers, depends_on, belongs_to_topic) has ZERO instance data. Adding new classes to an empty store adds nothing.

**Verdict:** Populate the existing schema first:
- Fix store.ttl syntax error (line 136 missing period)
- Add 17 Lecture instances
- Add Requirement instances from RPD (at least PKS-3 indicators)
- Add covers/belongs_to_topic triples linking lectures to topics
- THEN consider extending the schema with Paper/Concept

### 7. The 600-Line Index Split Rule Is Premature

**Proposed:** Auto-split wiki index when it exceeds 300/400 lines.

**Reality:** With 27 documents and 8 topics, the index will be ~50 lines. We won't hit 300 lines until we have 200+ sources. Design the split rule now, implement it when needed.

## Revised Priority List

Based on test data, here's what would give the most improvement per effort:

### P0: Fix Broken Infrastructure (High Impact, Low Effort)

1. **Fix store.ttl syntax error** -- missing period on line 136. 1-line fix enables ontology loading.
2. **Populate ontology instances** -- add 17 Lecture instances, Topic-Lecture covers triples, PKS-3 requirement. Makes Tier 2 functional.
3. **Expand RAG index scope** -- ingest notes/research/lecture-1/*.md (7 files, ~2000 lines) into local-rag. Makes Tier 3 functional for the richest content.
4. **Ingest downloaded papers** -- ingest 15 PDFs from library/papers/lecture-1/ into RAG via document-loader + local-rag.

### P1: Create Lightweight Wiki Index (High Impact, Medium Effort)

5. **Create wiki/index.md** -- simple topic-to-files mapping. Not compiled summaries, just a navigation aid. Example:
```
## AI Classification Taxonomies
- Primary: notes/research/lecture-1/classifications.md (9 taxonomies, 25+ papers)
- Papers: library/papers/lecture-1/ (15 PDFs)
- Assessment: catalog/exports/docs/sem-05-midterm-1.md (LO1 rubric)
```
This alone would reduce Scenario 1 from 29 calls to ~3 (read index, read source, done).

6. **Create wiki/lectures/lec-01.md** -- lightweight lecture summary with cross-links to research notes, papers, assessments. Not a full compilation, just a pointer page.

### P2: Add New Storage (Medium Impact, Low Effort)

7. **Create raw/papers/ structure** -- inbox/ and classified/ folders for paper management. Move library/papers/ convention to this.
8. **Update .gitignore** -- track paper manifests (index.yaml), ignore PDF binaries.

### P2: Hierarchical Indexes and Topic Structure (High Impact, Medium Effort)

7. **Create wiki/topics/ with per-topic index pages** -- at 200+ sources per lecture, a flat index.md won't survive. Each topic needs its own _index.md listing sources, papers, lectures.
8. **Create raw/papers/ structure** -- inbox/ and classified/ folders. Bulk import is needed NOW, not later.
9. **Content type templates** -- needed for consistency when generating 200+ document/paper summaries per lecture.

### P3: Compilation and Automation (Medium Impact, Higher Effort)

10. **Simplified compilation pipeline** (2-3 pass: catalog -> summarize -> index) -- not the full 5-pass sage-wiki pipeline, but enough to process bulk paper imports.
11. **Concept extraction** -- at 200+ sources, cross-cutting concepts are valuable for navigation.
12. **Cross-reference automation** -- manual linking is impossible at this scale.
13. **Folder restructuring** -- only if current paths become unmanageable.

## Scale Reality Check

**CORRECTION:** The original roast assumed 27 documents = small scale. This was wrong.

Lecture 1 alone references **204 external sources** (110 papers, 60 websites, 20 books). We downloaded 15 PDFs. When lectures 2-17 are built at similar density, the repo will hold **2000-3000+ sources**.

This means:
- Hierarchical indexes are needed NOW, not at "100+ sources"
- Bulk ingestion pipeline is needed NOW (can't manually ingest 200+ papers)
- Topic taxonomy must handle sub-topics from the start
- The 600-line limit will be hit by individual topic indexes, not just the master index
- RAG must handle thousands of chunks, not dozens

The original Part 3 design for 1000+ sources was right. The roast was too conservative.

## Revised Implementation Sequence

| Phase | What | Why Now |
|-------|------|---------|
| **Phase 1** | Fix ontology + RAG (P0) | Broken infrastructure, zero effort wasted |
| **Phase 2** | Create wiki/index.md + topic indexes (P1) | Discoverability bottleneck, hierarchical from start |
| **Phase 3** | Paper storage + bulk ingestion (P2) | 204 sources for Lecture 1 alone need a home |
| **Phase 4** | Compilation skill + templates (P3) | Can't manually compile 200+ summaries per lecture |
| **Re-test** | Run E2E scenarios again | Validate improvement |

## Expected Improvement (If Phases 1-3 Implemented)

| Scenario | Current E2E | Target |
|----------|-------------|--------|
| 1: Single-doc | 29 calls, 61.6s | ~3 calls, <10s (index -> source) |
| 2: Cross-doc | 35 calls, 87.9s | ~5 calls, <20s (topic index + RAG) |
| 3: Multi-hop | 32 calls, 79.4s | ~5 calls, <15s (ontology chain + index) |

### Why These Targets Are Realistic
- Phase 1 makes ontology and RAG functional (currently both return 0)
- Phase 2 eliminates discoverability bottleneck with hierarchical navigation
- Phase 3 means all 200+ Lecture 1 sources are findable via topic indexes + RAG

## Ontology-Specific Improvements

### Current State
- Schema: 8 classes, 7 relations (correct and sufficient for now)
- Store: ~20 instances, syntax error prevents loading, 0 Lecture/Requirement instances
- Queries: 3 pre-written SPARQL queries that return empty results

### Recommended Fixes
1. Fix line 136 syntax error in store.ttl
2. Add Lecture instances (lec_01 through lec_17) with labels, topics, source_urls
3. Add covers triples: lec_01 covers topic_ai_fundamentals, etc.
4. Add Requirement instances from RPD: at least PKS-3 with indicators
5. Add belongs_to_topic for all existing Document instances that lack it
6. Test all 3 pre-written SPARQL queries after loading -- they should return real data

### Phase 2 Ontology Work (needed for 200+ sources)
- Paper class + cites_paper relation -- needed NOW to track 204 Lecture 1 sources
- subtopic_of hierarchy -- needed NOW: "AI Classification" has 9 sub-taxonomies
- Requirement -> LearningOutcome -> Lecture chain -- needed for Scenario 3 to become a single SPARQL query

## RAG-Specific Improvements

### Current State
- Index: 16 files from catalog/exports/docs/ only
- Blind spots: notes/research/ (7 files, 2000+ lines), library/papers/ (15 PDFs)
- Russian queries: poor performance (scores 0.19-0.31)
- Embedding model: Xenova/all-MiniLM-L6-v2 (English-optimized, explains poor Russian)

### Recommended Fixes
1. Ingest all notes/research/lecture-1/*.md files (7 files, the richest content)
2. Ingest 15 downloaded PDFs via document-loader -> local-rag pipeline
3. Re-test Russian queries after ingestion -- if still poor, evaluate multilingual embedding model

### Phase 2-3 RAG Work (needed for 200+ sources)
- Multilingual embedding model evaluation -- Russian scores 0.19-0.31 with English-optimized model. At 2000+ sources with mixed RU/EN content, this MUST be fixed.
- Bulk ingestion workflow -- manual ingest_file per document won't scale to 200+ papers. Need a batch script or skill.
- Filtered search (by topic, type, date) -- at 200+ sources, unfiltered semantic search returns too much noise. Topic-scoped search is essential.

## Summary

The architecture design from Part 3 is **more correct than the initial roast gave it credit for**. The tests show:

1. **The system already works** via brute-force (quality is high, but cost is 30+ calls / 60-90s)
2. **Two things are broken** that should work: ontology (0 triples) and RAG (blind to research notes)
3. **One thing is missing** that would help most: hierarchical file index for discoverability
4. **Scale is real NOW** -- 204 sources for Lecture 1 alone means the 1000+ design is not premature
5. **The original Part 3 design was right about:** hierarchical indexes, topic taxonomy, ontology extension (Paper, Concept), bulk ingestion
6. **The original Part 3 design was wrong about:** 5-pass compilation (simplify to 2-3), folder restructuring (skip the rename, just add new folders)

Fix what's broken (P0), build the index layer (P1-P2), add automation (P3), then re-run the tests.

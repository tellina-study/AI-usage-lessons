---
title: "Knowledge Architecture for LLM-Native Workflows: A Comparative Analysis"
part: 1
parts_total: 3
description: "Part 1: Seven approaches to knowledge management — from Karpathy's LLM Wiki to Kubernetes docs-as-code, analyzed with raw source code from real implementations"
issue: "#18"
epic: "#17"
date: 2026-04-07
---

# Knowledge Architecture for LLM-Native Workflows

> Part 1 of 3: Seven Approaches Compared
> See also: [Part 2 — Retrieval Strategies](knowledge-architecture-comparison-part2.md) | [Part 3 — Our Architecture](knowledge-architecture-comparison-part3.md)

## Why Knowledge Architecture Matters Now

LLMs have fundamentally changed the knowledge management game. For decades, the debate centered on "folders vs tags vs links" — a question about human navigation ergonomics. Now the question is different: how should I organize knowledge so an LLM can navigate it?

This shift matters because LLMs are not just consumers of knowledge — they are maintainers. An LLM can read a thousand markdown files, build an index, detect gaps, and cross-reference concepts in ways no human would bother doing manually. The organizational structure you choose determines what the LLM can do with your knowledge.

The key insight from surveying real implementations: at moderate scale (up to a few hundred sources), a well-structured markdown wiki with an LLM-maintained index can outperform RAG. The index is small enough to fit in context, the LLM knows exactly where everything lives, and retrieval is precise. But at thousands of sources, the index itself exceeds context limits, and you need a hybrid approach — hierarchical indexes, vector search, and graph traversal working together.

This three-part series analyzes seven approaches to knowledge architecture, examines their retrieval strategies, and then describes how we combined elements of each into a working system for a university course with hundreds of source documents.

## 1. Karpathy's LLM Wiki

**Core idea:** Three-layer architecture (raw/wiki/schema). The LLM reads raw sources, compiles wiki pages, maintains an index. The index is the primary retrieval mechanism — no vector DB needed at personal scale.

**Raw source analysis:** Karpathy's gist defines three operations: Ingest, Query, Lint. The key files are `index.md` (catalog of all wiki pages with one-line summaries) and `log.md` (append-only record of all operations performed). The LLM decides what wiki pages to create or update after ingesting a new source — it is both the writer and the librarian.

The folder structure is intentionally minimal:

```
raw/           -- immutable source documents
wiki/          -- LLM-generated markdown (summaries, entity pages, comparisons)
CLAUDE.md      -- schema/conventions doc
```

The `raw/` directory is append-only: you never edit sources, only add new ones. The `wiki/` directory is entirely LLM-generated and LLM-maintained. `CLAUDE.md` defines the conventions the LLM follows when creating wiki pages — naming rules, required sections, cross-reference format.

**Real implementations:**

Three independent implementations of the LLM Wiki concept reveal what happens when the idea meets production:

- **ussumant/llm-wiki-compiler:** A Claude Code plugin that adds coverage indicators (high/medium/low per section) to track how well wiki articles cover their source material. In one test run, 383 source files were compressed to 13 wiki articles — an 81x compression ratio. Concept articles are auto-discovered when a topic appears across 3+ sources. The coverage system ensures no source material is silently dropped.

- **atomicmemory/llm-wiki-compiler:** A TypeScript + Anthropic API implementation that uses structured tool_use for concept extraction. The cross-reference resolver walks all wiki pages after each update to ensure bidirectional links are consistent. Includes orphan page detection — wiki pages that exist but are not referenced from the index or any other page.

- **xoai/sage-wiki:** A Go production-grade implementation with a 5-pass pipeline: diff detection, summarization, concept extraction, article writing, and embedding generation. Combines hybrid BM25 + vector search for retrieval. Uses SQLite as the backend with checkpoint/resume support for interrupted ingestion runs.

**Scale characteristics:** At approximately 100 sources, index-only retrieval works well. The entire `index.md` fits comfortably in context, and the LLM can find any page by scanning summaries. At approximately 500+ sources, every implementation adds something beyond the basic index: sage-wiki adds vector search, ussumant adds coverage indicators to prioritize retrieval, and atomicmemory adds dependency graphs to navigate related concepts. Karpathy himself notes that RAG becomes necessary "beyond a few hundred articles or millions of words."

**Key code snippet** from atomicmemory's concept extraction:

```typescript
CONCEPT_EXTRACTION_TOOL = {
  name: "extract_concepts",
  input_schema: {
    concepts: [{
      concept: "string",
      summary: "string",
      is_new: "boolean"
    }]
  }
}
```

The `is_new` flag is critical — it tells the system whether to create a new wiki page or update an existing one, preventing duplicate pages for the same concept under slightly different names.

## 2. Zettelkasten (Dendron, Foam, note-link-janitor)

**Core idea:** Atomic notes, bidirectional links, emergent structure from connections not categories. Each note captures one idea, links to related ideas, and the structure of knowledge emerges from the link graph rather than from a predetermined hierarchy.

**Dendron's hierarchy model:** Dendron takes a unique approach — dot-separated filenames AS the hierarchy. The file `lang.python.data.string.md` represents the path `lang > python > data > string`. There is no folder nesting; all files are flat in a single directory, with dots encoding the tree structure. Lookup uses Fuse.js fuzzy search over filenames, so typing "py str" finds `lang.python.data.string.md`.

**Dendron schema format:**

```yaml
version: 1
schemas:
  - id: daily
    pattern: daily
    children:
      - pattern: journal
        children:
          - pattern: "*"
            template:
              id: templates.daily
              type: note
```

Schemas enforce structure on note creation. When you create a note matching `daily.journal.*`, Dendron automatically applies the `templates.daily` template. This is the closest thing to "types" in the Zettelkasten world — it gives you consistent structure without abandoning the flat-file model.

**Foam's graph model:** The `FoamGraph` class maintains two Maps: `links` (outgoing references from each note) and `backlinks` (incoming references to each note). The graph undergoes a full rebuild on every workspace change — clear all links, then re-walk all resources to reconstruct the graph. Foam uses a `TrieMap` for prefix-based lookup, which enables efficient "find all notes starting with X" queries.

**note-link-janitor algorithm** (Andy Matuschak, approximately 200 lines total):

1. Scan all `.md` files, parse wiki-links via remark AST
2. Build `Map<targetTitle, Map<sourceTitle, contextBlocks>>` — for each target note, collect all source notes that link to it along with the surrounding context
3. Compute PageRank over the link graph to determine note importance
4. Write a `## Backlinks` section into each file, sorted by PageRank — the most important referring notes appear first

This is a batch process, not live — you run it periodically to update backlinks across the entire wiki.

**Scale:** Fuse.js threshold bugs appear above approximately 10,000 notes in Dendron — fuzzy matching starts returning irrelevant results or missing relevant ones. Foam's full graph rebuild is O(N*L) where N is the number of notes and L is the average number of links per note. The note-link-janitor is batch-only and works well to approximately 10,000 notes; beyond that, memory consumption during the full-graph PageRank computation becomes an issue.

## 3. PARA (Tiago Forte)

**Core idea:** Four categories organized by actionability, not topic: Projects (active work with deadlines), Areas (ongoing responsibilities without end dates), Resources (reference material for future use), Archive (inactive items from any of the other three categories).

**Folder structure:**

```
1 - projects/    # Active, with deadlines
2 - areas/       # Ongoing responsibilities
3 - resources/   # Topic-based reference material
4 - references/  # External reference material
5 - archives/    # Inactive items from any category
```

The numbered prefixes enforce sort order. The critical distinction is between Projects (finite, with a clear completion state) and Areas (infinite, maintained indefinitely). A course you are teaching this semester is a Project; "teaching" as a professional responsibility is an Area.

**At scale:** PARA has no built-in cross-referencing mechanism — it relies entirely on whatever the host tool provides (Obsidian backlinks, Notion relations, etc.). Manual reclassification becomes the primary bottleneck past approximately 200 items. When a project ends, you must manually move it to Archive, and any Resources it spawned must be manually relocated. The `para-shortcuts` Obsidian plugin automates moves between categories with hotkeys, but no automated classification tooling exists at any level of maturity.

**Relevance to us:** Our Google Drive structure (`00-course`, `01-formal`, `02-lectures`, etc.) is already partially PARA — `02-lectures` maps to Projects (each lecture is a deliverable with a deadline), `04-resources` maps to Resources, and `archive/` maps to Archive. But PARA alone cannot handle thousands of papers or cross-reference requirements across lectures. It provides a top-level organizational frame, not a knowledge retrieval system.

## 4. Johnny Decimal

**Core idea:** Strict numeric hierarchy with three levels: Areas (X0-X9), Categories (XY), and IDs (XY.ZZ). This creates a hard ceiling: 10 areas times 10 categories times 100 IDs = 10,000 items maximum.

**Structure:**

```
00-09 System/
  01 System Stuff/
    01.02 A Name.md
10-19 Project Management/
  11 Planning/
    11.01 Roadmap.md
```

The JDex (index) is a plain-text file mapping every ID to a human-readable description. The `jdlint` tool validates that the file system matches the JDex and that no IDs are duplicated or out of range. When you exceed 10 areas, the official guidance is to create entirely separate JD systems rather than extending the numbering.

The discipline is the point. You cannot have more than 10 top-level areas, which forces you to think carefully about categorization. Each item gets exactly one location — there is no tagging, no cross-referencing, no "this belongs in two places." If you need to reference something from multiple contexts, you use the numeric ID as a pointer.

**Relevance:** Our `lec-01..lec-17` and `sem-01..sem-17` numbering is proto-Johnny Decimal. The numeric discipline works well for stable, bounded collections (17 lectures, 17 seminars) where the total count is known in advance. It breaks down for open-ended collections like research papers, notes, and references that grow without a predetermined ceiling.

## 5. Digital Garden (Andy Matuschak)

**Core idea:** Evergreen notes that evolve over time. Flat structure, dense links, backlinks maintained automatically. The philosophy is "work with the garage door up" — publish notes in progress, let them grow organically, revise them as understanding deepens.

The key principle is anti-transience: notes are not dated blog posts that become stale but living documents that get revised whenever new information arrives. A note on "transformer attention mechanisms" written in 2023 should be updated in 2026 with new findings, not replaced by a new note.

The note-link-janitor (described in section 2 above) is the primary maintenance tool, keeping backlinks current with PageRank-sorted context so the most important connections surface first.

**At scale:** Large Obsidian vaults demonstrate that flat structure breaks above approximately 200 notes — navigation becomes unmanageable without some grouping. The nolebase vault (484 files) uses category folders with co-located assets (images stored alongside the notes that reference them), NOT flat structure. Maps of Content (MOCs) serve as manually curated index pages that group related notes by theme — essentially a human-maintained version of Karpathy's `index.md`.

The tension between "flat is pure" and "folders are practical" is the central scaling challenge. Most gardens that grow beyond 200 notes adopt a pragmatic hybrid: broad category folders (5-10 at most) with flat structure within each folder.

## 6. Docs-as-Code (Kubernetes, Docusaurus)

**Core idea:** Documentation lives in version control alongside code, written in markdown, rendered by static site generators. Content types are formalized with templates and build-time validation.

**Kubernetes content types:**

- `concept` — "What is X?" explanations of system components and abstractions
- `task` — "How to do X" step-by-step procedures for specific goals
- `tutorial` — End-to-end walkthroughs combining multiple tasks into a complete scenario
- `reference` — API specifications, CLI documentation, configuration schemas

Each content type has a Hugo archetype (template) that enforces required sections. A `task` page must have Prerequisites, Steps, and Verification sections. A `concept` page must have Overview, How It Works, and What's Next sections. This structural consistency is what makes the documentation navigable at scale.

**Cross-references use build-time validated shortcodes:**

```
glossary_tooltip term_id="cluster"
```

An invalid `term_id` halts the build. This means broken cross-references are caught before publication, not discovered by readers. The glossary is a YAML file mapping term IDs to definitions, and every shortcode reference is validated against it.

**Docusaurus sidebar auto-generation:** Number prefix parsing strips `01-intro.md` down to position 1 with slug "intro". The `_category_.json` file in each directory provides category metadata (label, position, collapsibility). This convention-over-configuration approach means the sidebar structure mirrors the file system structure — no separate configuration file to maintain.

**At 3000+ pages:** Build times stretch to approximately 3 minutes. The glossary validation system catches broken links at build time but adds to that build duration. Versioning is the real scaling challenge: Kubernetes duplicates entire doc trees per version, so 500 documents across 10 supported versions means 5,000 files in the repository. Each file must be independently maintained when cross-version changes occur.

## 7. LLM-Native Retrieval

This is not a separate organizational approach but a retrieval strategy that changes how you think about organization. The key principles:

**The LLM reads structured markdown and navigates by index.** Unlike keyword search or vector similarity, an LLM can understand what a document is about from its title, headings, and a one-line summary. A good index turns the LLM into a librarian who knows the entire collection.

**At moderate scale (up to approximately 200 pages), context windows replace RAG.** If your index fits in context — and with 200,000-token context windows, an index of 200 pages with titles and summaries easily fits — the LLM can find anything without vector search. Retrieval is precise because the LLM understands the query semantically.

**At large scale (1000+ pages), hierarchical indexes with vector search and graph traversal combine.** The index becomes multi-level: a top-level index points to section indexes, which point to individual pages. Vector search handles "find me something similar to X" queries that hierarchical navigation cannot. Graph traversal handles "what else is related to this concept" queries that neither index scanning nor vector search handle well.

**"Vibe coding" produces custom tools as throwaway infrastructure.** Need a script to extract all cross-references from 500 markdown files and build a link graph? An LLM writes it in 5 minutes. The script is not maintained software — it is disposable tooling generated on demand.

**Knowledge compounds: every interaction adds to the wiki.** When you ask the LLM a question and it synthesizes an answer from multiple sources, that synthesis becomes a new wiki page. The knowledge base grows not just from explicit ingestion but from the act of using it.

## Comparison Matrix

| Approach | Organization | Cross-refs | Scale Limit | Best For |
|----------|-------------|------------|-------------|----------|
| Karpathy Wiki | 3-layer (raw/wiki/schema) | LLM-generated | ~500 before RAG needed | Solo researcher, LLM-native |
| Zettelkasten | Flat + links (or dot-hierarchy) | Bidirectional wiki-links | ~10k (Fuse.js limits) | Deep thinkers, long-term KB |
| PARA | 4 folders by actionability | Tool-dependent | ~200 before reclassification pain | Action-oriented individuals |
| Johnny Decimal | Strict numeric hierarchy | Numeric IDs | 10,000 hard cap | Bounded, stable collections |
| Digital Garden | Flat + dense links | Backlinks + MOCs | ~500 flat, more with folders | Writers, public intellectuals |
| Docs-as-Code | Content-type hierarchy | Build-time validation | 3000+ (with build cost) | Teams, open source projects |
| LLM-Native | Hierarchical indexes | Auto-generated | Depends on retrieval stack | Any scale, with right retrieval |

The approaches are not mutually exclusive. Most real systems combine elements: PARA-style top-level folders with Zettelkasten-style links within them, or Docs-as-Code structure with LLM-native retrieval layered on top. The question is not which approach to choose but which combination matches your scale, team size, and tooling.

> Continue to [Part 2: Retrieval Strategies Compared](knowledge-architecture-comparison-part2.md)

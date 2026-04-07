---
title: "Extended Research: Knowledge Architecture — Raw Findings (Part 1)"
description: "Internal reference: full code snippets, algorithms, and implementation details from Karpathy wiki implementations and Zettelkasten tools"
issue: "#18"
epic: "#17"
date: 2026-04-07
type: research-note
---

# Extended Research: Raw Findings (Part 1 of 2)

> Internal reference document. For the polished version, see [blog post parts 1-3](knowledge-architecture-comparison-part1.md).
> See also: [Part 2 — Retrieval and Scale](knowledge-architecture-raw-research-part2.md)

## Karpathy LLM Wiki — Implementation Deep-Dive

### The Gist (Original Specification)

Three-layer architecture with two supporting files and three operations.

**Layers:**
- `raw/` — immutable source documents. "The LLM reads from them but never modifies them. This is your source of truth."
- `wiki/` — LLM-generated markdown. "Summaries, entity pages, concept pages, comparisons, an overview, a synthesis."
- Schema document (CLAUDE.md) — defines folder structure, citation rules, ingest workflow, Q&A behavior, linting conventions.

**Supporting files:**
- `index.md` — "A catalog of everything in the wiki — each page listed with a link, a one-line summary." Organized by category.
- `log.md` — "An append-only record of what happened and when — ingests, queries, lint passes."

**Operations:**
1. **Ingest** — reads source, discusses takeaways, writes summary page, updates index, updates 10-15 related pages
2. **Query** — searches wiki pages to synthesize answers. Good answers filed back as new pages.
3. **Lint** — health-check: contradictions, orphan pages, stale claims, missing concepts.

**Scale quotes (Karpathy):**
- "At ~100 articles and ~400K words, the LLM's ability to navigate via summaries and index files is more than sufficient."
- "For a departmental wiki or personal research project, 'fancy RAG' infrastructure often introduces more latency and retrieval noise than it solves."
- "The index itself becomes too large to fit in context" beyond a few hundred articles — recommends `qmd` CLI search.

### ussumant/llm-wiki-compiler (Claude Code Plugin)

**Plugin structure:**
```
plugin/
  .claude-plugin
  commands/       # /wiki-init, /wiki-compile, /wiki-lint, /wiki-query, /wiki-upgrade
  hooks/          # SessionStart hook injects wiki context
  skills/
    wiki-compiler # main skill
  templates/
    schema-template.md
    article-template.md
    index-template.md
```

**Schema template defines:**
- Topics (slug + description)
- Concepts (cross-cutting patterns spanning 3+ topics)
- Article structure: Summary, Timeline, Current State, Key Decisions, Experiments, Gotchas, Open Questions, Sources
- Naming conventions: lowercase-kebab-case
- Cross-reference rules
- Evolution log for schema changes

**Article template with coverage indicators:**
```markdown
---
topic: {topic-slug}
last_compiled: {ISO-date}
source_count: {N}
status: {draft|compiled|reviewed}
---
## Summary [coverage: high -- 15 sources]
...
## Experiments & Results [coverage: medium -- 3 sources]
...
## Gotchas [coverage: low -- 1 source]
...
```

Coverage meaning:
- high (5+ sources) — trust wiki, skip raw
- medium (2-4 sources) — wiki is good, check raw for detail
- low (0-1 sources) — read raw directly

**Compression metrics:**
- 383 files (13.1 MB) -> 13 articles (161 KB) = 81x compression
- 130 meeting transcripts (122,625 lines) -> 1 digest (244 lines) = 503x compression
- Session startup: ~47K tokens -> ~7.7K tokens = 84% reduction

**Three adoption modes:** staging (wiki on demand), recommended (wiki before raw), primary (wiki is source)

**Concept articles:** Auto-discovered cross-cutting patterns spanning 3+ topics. Example: "Speed vs Quality Tradeoff" found across 6 instances in retention, push notifications, experiment design.

**Incremental compilation:** After first full compile, only topics with changed source files recompile. INDEX.md always regenerated.

### atomicmemory/llm-wiki-compiler (TypeScript + Anthropic API)

**Source structure:**
```
src/
  compiler/
    index.ts        # orchestration
    prompts.ts      # LLM prompt templates
    indexgen.ts      # wiki/index.md generator
    deps.ts          # dependency graph
    hasher.ts        # content hashing for incremental
    orphan.ts        # orphan page detection
    resolver.ts      # cross-reference resolution
  ingest/
  utils/
```

**Phase 1 — Concept Extraction (tool_use mode):**
```typescript
CONCEPT_EXTRACTION_TOOL = {
  name: "extract_concepts",
  input_schema: {
    concepts: [{
      concept: "string",   // Human-readable title
      summary: "string",   // One-line description
      is_new: "boolean"    // Not in existing wiki?
    }]
  }
}
```

System prompt: "Analyze the following source document and identify 3-8 distinct, meaningful concepts worth documenting as wiki pages. Focus on key ideas, techniques, patterns, or entities — not trivial details."

**Phase 2 — Page Generation:**
```typescript
buildPagePrompt(concept, sourceContent, existingPage, relatedPages)
// "Write a clear, well-structured markdown page about {concept}."
// "Draw facts only from the provided source material."
// "Include a ## Sources section. Suggest [[wikilinks]] to related concepts."
```

**Index generation (indexgen.ts):** Scans `wiki/concepts/` for `.md` files, extracts YAML frontmatter (title, summary), produces sorted list: `- **[[Title]]** — summary`.

**Cross-references:** `resolver.ts` handles wikilink resolution; `deps.ts` builds dependency graph; `orphan.ts` detects pages whose sources were deleted.

### xoai/sage-wiki (Go, Production-Grade)

**Internal structure:**
```
internal/
  compiler/      # pipeline.go, concepts.go, diff.go, summarize.go, write.go, watch.go
  embed/         # embedding providers
  extract/       # PDF, DOCX, XLSX, EPUB, images
  hybrid/        # BM25 + vector hybrid search
  manifest/      # .manifest.json tracking source hashes
  mcp/           # MCP server for agent integration
  memory/        # compilation learnings store
  ontology/      # concept graph
  prompts/templates/   # summarize_article.txt, extract_concepts.txt, write_article.txt
  storage/       # SQLite DB
  vectors/       # vector store
```

**5-Pass Compilation Pipeline:**
1. **Diff** — compare source files against `.manifest.json` (content hashes). Categorize: Added/Modified/Removed.
2. **Summarize** — LLM summarizes each new/changed source (separate prompts for articles vs papers).
3. **Extract concepts** — from summaries, identify concepts with aliases, merge with existing.
4. **Write articles** — generate/update wiki pages per concept, with related concepts and existing article as context.
5. **Post** — auto-embed (vectors), auto-lint, auto-commit (git).

**Checkpoint/resume:** `CompileState` struct tracks `compile_id`, `pass`, `completed`, `pending`, `failed`. Supports resuming interrupted compilations.

**Scale features:**
- `max_parallel: 4` concurrent LLM calls
- Content hashing via manifest for incremental
- Hybrid search: `hybrid_weight_bm25: 0.7` / `hybrid_weight_vector: 0.3`
- Watch mode with debounce (`debounce_seconds: 2`)
- Per-task model selection (cheap for summarize, quality for write)

**Extract concepts prompt:**
```
Given summaries of recently added/modified sources, extract concepts.
For each: name (lowercase-hyphenated), aliases, sources, type (concept/technique/claim).
Merge with existing concepts when appropriate (detect aliases).
Output as JSON array.
```

**Write article prompt:**
```
Write structured wiki article with sections:
## Definition, ## How it works, ## Variants, ## Trade-offs, ## See also
YAML frontmatter: concept, aliases, sources, related, confidence
```

## Zettelkasten Tools — Implementation Details

### Dendron: Hierarchy as Index

**FuseEngine lookup (packages/common-all/src/FuseEngine.ts):**
```typescript
const options: Fuse.IFuseOptions<T> = {
  shouldSort: true,
  threshold: opts.threshold,    // 0.0 exact, ~0.2 fuzzy
  distance: 15,
  minMatchCharLength: 1,
  keys: ["fname"],              // dot-separated filename
  useExtendedSearch: true,
  includeScore: true,
  ignoreLocation: true,
  ignoreFieldNorm: true,
};
```

Scale claim: "retrieval works as well with ten notes as ten thousand." But: Fuse.js threshold bugs appear >10k notes (scores of 0.59 leak through 0.2 threshold).

### Foam: Graph Data Structures

**Connection model (packages/foam-vscode/src/core/model/graph.ts):**
```typescript
export type Connection = {
  source: URI;
  target: URI;
  link: ResourceLink;
};

export class FoamGraph {
  public readonly links: Map<string, Connection[]> = new Map();       // outgoing
  public readonly backlinks: Map<string, Connection[]> = new Map();   // incoming
}
```

Full rebuild on every change: `clear() -> re-walk all resources`. Debounced at 500ms. O(N*L) where N=notes, L=avg links.

**Workspace uses TrieMap** (from `mnemonist/trie-map`) for prefix-based lookup.

### note-link-janitor: The Complete Algorithm (~200 lines)

**Step 1:** Flat scan of `.md` files, parse with remark + remark-wiki-link.

**Step 2:** Walk AST, find `wikiLink` nodes, capture containing block as context:
```typescript
visitParents<WikiLinkNode>(
  tree, "wikiLink",
  (node, ancestors) => {
    const closestBlock = ancestors.reduceRight(
      (result, needle) => result ?? (isBlockContent(needle) ? needle : null), null
    );
    links.push({ targetTitle: node.data.alias, context: closestBlock });
  }
);
```

**Step 3:** Build `Map<targetTitle, Map<sourceTitle, BlockContent[]>>`.

**Step 4:** Compute PageRank (damping 0.85, convergence 0.000001).

**Step 5:** Write `## Backlinks` section, sorted by PageRank:
```markdown
## Backlinks
* [[Source Note Title]]
	* The paragraph that contained the link
```

### Large Vault Patterns (nolebase, 484 files)

```
zh-CN/
  生活/
    租房/
      租房流程.md
      assets/          # co-located per topic
    事务/
      assets/
  文档工程/
  操作系统/
    RedHat Enterprise Linux/
    macOS/
      assets/
```

Patterns: co-located assets per folder (not global), category folders (not flat), 2-3 level depth max, MOCs as manual indexes.

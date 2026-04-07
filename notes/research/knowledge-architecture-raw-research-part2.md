---
title: "Extended Research: Knowledge Architecture — Raw Findings (Part 2)"
description: "Internal reference: docs-as-code implementations, retrieval benchmarks, scale characteristics, and production hybrid systems"
issue: "#18"
epic: "#17"
date: 2026-04-07
type: research-note
---

# Extended Research: Raw Findings (Part 2 of 2)

> Internal reference document. For the polished version, see [blog post parts 1-3](knowledge-architecture-comparison-part1.md).
> See also: [Part 1 — Wiki Implementations and Zettelkasten](knowledge-architecture-raw-research-part1.md)

## Docs-as-Code at Scale — Implementation Details

### Kubernetes Docs (3000+ pages, Hugo)

**Directory structure** under `content/en/docs/`:
```
docs/
  _index.md
  concepts/          # "What is X?"
    architecture/
    workloads/
    services-networking/
    storage/
  tasks/             # "How to do X"
    run-application/
    configure-pod-container/
  tutorials/         # End-to-end walkthroughs
  reference/         # API specs, CLI, glossary
  setup/
  contribute/
```

**Content types enforced via archetypes.** Task archetype:
```yaml
---
title: "{{ replace .Name \"-\" \" \" | title }}"
content_type: task
---
<!-- overview -->
## {{% heading "prerequisites" %}}
{{< include "task-tutorial-prereqs.md" >}}
<!-- steps -->
<!-- discussion -->
## {{% heading "whatsnext" %}}
```

HTML comments (`<!-- overview -->`, `<!-- body -->`, `<!-- steps -->`) act as section markers parsed by Hugo templates.

**Cross-referencing mechanisms:**
1. `{{< glossary_tooltip term_id="cluster" >}}` — looks up term_id in glossary folder, renders tooltip. Invalid term_id triggers `errorf` (build fails).
2. `{{< include "task-tutorial-prereqs.md" >}}` — shared content partials
3. `{{% code_sample file="application/deployment.yaml" %}}` — validated example file references

**Navigation:** Weight-based ordering. Each `_index.md` has `weight: 40` in frontmatter. Hugo sorts by weight. `enableGitInfo = true` for lastmod from git.

**Build performance:** `timeout = "180s"` in hugo.toml — 3000+ pages take ~3 min to build.

### Docusaurus Sidebar Generation

**Number prefix parsing** (from `numberPrefix.ts`):
```
01-intro.md      -> position: 1, slug: "intro"
02-setup.md      -> position: 2, slug: "setup"
003 - advanced   -> position: 3, slug: "advanced"
```
Ignores date-like (`2021-11-foo`) and version-like (`7.0-foo`) patterns.

**Category metadata** via `_category_.json`:
```json
{
  "label": "Guides",
  "position": 2,
  "link": { "type": "generated-index" }
}
```

**Sidebar config** (`sidebars.ts`):
```typescript
const sidebars: SidebarsConfig = {
  docs: [
    'introduction',
    {
      type: 'category',
      label: 'Guides',
      link: { type: 'generated-index' },
      items: ['guides/creating-pages', 'blog', ...]
    }
  ]
};
```

**Versioning:** Physical copies per version — `versioned_docs/version-1.0.0/`. A project with 500 docs and 10 versions = 5000 files. Scales poorly.

### Johnny Decimal Details

**Core constraints:**
- Areas: `X0-X9` (10 possible)
- Categories: `XY` within area (10 per area)
- IDs: `XY.ZZ` (100 per category)
- Hard ceiling: 10 x 10 x 100 = 10,000 items

**JDex index formats:**
1. Single flat index file
2. Nested folder mirrors
3. Flat files where `N0.00` = area header, `AC.00` = category header

**`jdlint` validations:** `CATEGORY_IN_WRONG_AREA`, `DUPLICATE_ID`, `ID_IN_WRONG_CATEGORY`. No overflow mechanism — create separate JD systems instead.

### PARA at Scale

**Hybrid PARA + Johnny Decimal** (Paratag variant):
```
10 - Projects/
30 - Resources/
  30.1 - Templates/
  30.2 - Contacts/
```

**Pain point at scale:** Manual reclassification is the bottleneck past ~200 items. `para-shortcuts` Obsidian plugin automates moves. No automated classification tooling exists.

## Retrieval Strategies — Technical Deep-Dive

### Grep/ripgrep Performance

**Benchmark numbers:**
- 1.4GB monorepo (250K files): under 1 second
- 240 log files: grep 4.2s, ripgrep 0.018s (233x speedup)
- SIMD-optimized: 16-32 bytes per CPU cycle using finite automata
- Crossover vs indexed search: ~500K-1M files (Cursor indexed search: 0.013s where ripgrep took 15s)

**When grep beats embeddings:**
- `ERROR_CODE_4532` vs `ERROR_CODE_4533` — near-identical vectors, trivially different strings
- Regex over structured data: logs, JSON, config files, code
- Zero setup, zero maintenance, zero cost

### Vector Search Economics

**Cost breakdown:**
- Embedding: ~$0.10 per 1M tokens (ada-002)
- Storage: ~1.5KB per vector (1536 dims)
- Query latency: sub-millisecond with HNSW at 1M vectors
- Managed: ~$70/month per 1M vectors (Pinecone)

**OpenSearch 3.x hybrid:** BM25 + vector combined. Hybrid bulk scorer: 65% faster than separate execution. Additional 20% improvement in v3.3.

### SPARQL Engine Benchmarks

**Oxigraph (our engine):**
- Tested on 35M triples (100K products dataset), 32GB machine
- Python: ~20ms in-memory, ~38ms persistent, parsing ~20ms
- "Suitable for small and medium-sized datasets" (ResearchGate evaluation)
- Good for our current scale; revisit at millions of triples

**Comparison landscape:**
| Engine | Scale | Status |
|--------|-------|--------|
| Oxigraph | Small-medium (millions) | Active, Rust-based |
| Blazegraph | Large (16B triples at Wikidata) | End-of-life, hitting limits |
| QLever | Massive (1T+ claimed) | Academic, fastest on Wikidata queries |
| Virtuoso | Enterprise (billions) | Mature, commercial |

**Wikidata scaling crisis:** 16B triples, Blazegraph is EOL. Journal corruption under load. Split endpoint into two as emergency measure. Evaluating replacements.

**When SPARQL wins over vector search:**
- Multi-hop: "Papers citing Author X published in Venue Y"
- Provenance: "Requirement -> test case -> coverage"
- Aggregation: COUNT, FILTER, negation
- Negation: "Entities WITHOUT relationship R" (impossible with similarity)

### HybridRAG (NVIDIA/BlackRock) — Paper Details

**Architecture:** Two parallel channels — VectorRAG (embed, cosine similarity) + GraphRAG (entity extraction, graph traversal). Results concatenated before generation.

**Corpus:** Financial earnings call transcripts (Q&A format = natural ground truth).

**Finding:** HybridRAG outperforms both individual approaches. Complementarity: vector captures semantic similarity, graph captures structured relational facts (e.g., "Company X acquired Company Y in Q3").

**Limitation:** KG extraction expensive and error-prone on messy text. On opinion pieces/narrative without clear entities, graph channel adds cost without benefit.

### Microsoft GraphRAG — Paper Details

**Pipeline:**
1. LLM extracts entities + relationships from text chunks
2. Leiden community detection on resulting graph
3. Hierarchical communities get LLM-generated summaries
4. Queries answered by map-reducing over community summaries

**Scale numbers (podcast corpus, 1M tokens):**
- 8,564 nodes, 20,691 edges
- Communities: 34 root (C0), 367 (C1), 969 (C2), 1,310 leaf (C3)

**News corpus (1.7M tokens):**
- 15,754 nodes, 19,520 edges
- Communities: 55/555/1,797/2,142 across levels

**vs Naive Vector RAG:**
- Comprehensiveness win rate: 72-83% (p<0.001)
- Diversity win rate: 75-82% (p<0.01)
- Claims per answer: 31-34 vs 25-27
- Token efficiency: root summaries used 2.6% of max context (9-43x reduction)

**Cost:** 281 minutes indexing for 1M tokens with GPT-4-turbo on 16GB machine. Manageable at 1M; expensive at 100M tokens.

**Key insight:** Naive RAG retrieves similar chunks. GraphRAG answers "global sensemaking" questions requiring synthesis across entire corpus.

### Production Hybrid Systems

**Glean (enterprise search):**
Vector embeddings + BM25 + organizational knowledge graph (ownership, reporting, permissions). Graph provides permission-aware retrieval.

**Neo4j + Pinecone integration:**
1. Vector search returns top-k candidates
2. Entity extraction on results
3. Neo4j traversal enriches context
4. Merged context feeds LLM

**Reciprocal Rank Fusion (RRF):**
`score = sum(1/(k + rank))` across all strategy ranked lists. Simple, parameter-light, consistently outperforms learned fusion.

**Cost of 3-strategy system:**
- Vector DB: ~$70/month per 1M vectors
- Graph DB: ~$65/month for 200K nodes/400K relationships  
- BM25 index: ~$50/month managed
- Embedding: ~$0.10/1M tokens (one-time)
- Graph extraction: periodic LLM re-runs

## Scale Breaking Points Summary

| Component | Works Until | Breaks At | Mitigation |
|-----------|------------|-----------|------------|
| Flat folder | ~200 files | 500+ files | Hierarchical subdirectories |
| Single index.md | ~300 entries | 600+ lines | Hierarchical indexes (master -> topic -> sub-topic) |
| Foam full graph rebuild | ~500 linked notes | 1000+ | Incremental updates |
| Fuse.js fuzzy search | ~5K notes | 10K+ (threshold bugs) | Switch to dedicated search index |
| Manual cross-refs | ~50 documents | 100+ | Auto-generated backlinks |
| PARA reclassification | ~200 items | 500+ | Plugin-assisted or AI classification |
| Context-window retrieval | ~500 pages | 1000+ | Add vector search tier |
| Oxigraph SPARQL | ~35M triples | 100M+ | Migrate to QLever or Virtuoso |
| GraphRAG indexing cost | ~2M tokens | 10M+ | Selective extraction, cheaper models |

## Key References

- [Karpathy llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [ussumant/llm-wiki-compiler](https://github.com/ussumant/llm-wiki-compiler)
- [atomicmemory/llm-wiki-compiler](https://github.com/atomicmemory/llm-wiki-compiler)
- [xoai/sage-wiki](https://github.com/xoai/sage-wiki)
- [Dendron](https://github.com/dendronhq/dendron)
- [Foam](https://github.com/foambubble/foam)
- [note-link-janitor](https://github.com/andymatuschak/note-link-janitor)
- [Docusaurus](https://github.com/facebook/docusaurus)
- [Kubernetes website](https://github.com/kubernetes/website)
- [HybridRAG](https://arxiv.org/abs/2408.04948)
- [Microsoft GraphRAG](https://arxiv.org/html/2404.16130v2)
- [Oxigraph](https://github.com/oxigraph/oxigraph)
- [QLever](https://github.com/ad-freiburg/qlever)
- [OpenSearch hybrid search](https://opensearch.org/blog/opensearch-3-3-performance-innovations-for-ai-search-solutions/)
- [Pinecone + Neo4j](https://www.pinecone.io/learn/vectors-and-graphs-better-together/)
- [ripgrep benchmarks](https://burntsushi.net/ripgrep/)

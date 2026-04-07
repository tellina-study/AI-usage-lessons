---
title: "Knowledge Architecture for LLM-Native Workflows: Retrieval Strategies"
part: 2
parts_total: 3
description: "Part 2: Four retrieval strategies compared — grep, vector search, SPARQL, and hybrid — with benchmarks and production examples"
issue: "#18"
epic: "#17"
date: 2026-04-07
---

# Retrieval Strategies Compared

> Part 2 of 3: From Grep to Hybrid RAG
> See also: [Part 1 — Seven Approaches](knowledge-architecture-comparison-part1.md) | [Part 3 — Our Architecture](knowledge-architecture-comparison-part3.md)

## 1. Naive Grep (Keyword/Regex Search)

**How it works:** Pattern matching over raw text. Tools: ripgrep, ag, grep. SIMD-optimized, scans 16-32 bytes per CPU cycle using finite automata.

**Performance numbers:**
- ripgrep on 1.4GB monorepo (250K files): under 1 second
- 240 log files: grep 4.2s, ripgrep 0.018s (233x speedup)
- Hits limits at ~1M files (15+ seconds)
- Cursor's indexed search: 0.013s where ripgrep took 15s on same repo

**When grep wins over vector search:**
- Exact matches: error codes, UUIDs, config keys, function names
- Structured data and code: regex over JSON, logs, source
- Zero infrastructure, zero index maintenance

**When it fails:** Semantic queries ("find notes about motivation" won't match "drive" or "ambition"), synonyms, multilingual content, relevance ranking.

**Crossover point:** If you search the same corpus repeatedly, build an index; grep is faster for ad-hoc searches up to ~500K files.

## 2. Vector/Embedding Semantic Search

**How it works:** Text -> high-dimensional vectors via embedding models. Nearest-neighbor search in vector space. Tools: LanceDB, Pinecone, Chroma, pgvector.

**Cost profile:**
- Embedding: ~$0.10 per 1M tokens (ada-002)
- Storage: ~1.5KB per vector (1536 dims)
- Query: sub-millisecond with HNSW indices at 1M vectors
- Managed service: ~$70/month per 1M vectors (Pinecone)

**When it excels:** Synonyms, paraphrases, cross-language matching ("scarlet biker coat" matches "red leather jacket"), conceptual queries, unknown terminology.

**When it fails:**
- Exact-match queries (ERROR_4532 vs ERROR_4533 map to near-identical vectors)
- Structured/relational queries ("which doc cites X")
- Explainability (similarity scores don't explain WHY)
- Small corpora (overkill -- more infrastructure than value)

**Hybrid BM25+Vector:** OpenSearch 3.x combines BM25 keyword scoring with vector search. Their hybrid bulk scorer: 65% faster than running both separately, additional 20% in v3.3.

## 3. Ontology/SPARQL (Graph Traversal)

**How it works:** Knowledge modeled as entities + relationships (RDF triples). Queries traverse the graph using SPARQL, following explicit typed relationships.

**Engine benchmarks:**
- Oxigraph: 35M triples tested, SPARQL queries ~20ms in-memory, suitable for small-to-medium datasets
- Wikidata: 16 billion triples on Blazegraph (hitting limits, migrating)
- QLever: claims 1 trillion+ triples on commodity hardware
- Virtuoso: enterprise-grade, handles billions

**When SPARQL outperforms vector search:**
- Multi-hop queries: "Papers citing Author X published in Venue Y" -- graph traversal, not similarity
- Provenance chains: "Requirement -> test case -> coverage" -- explicit typed relationships
- Aggregation with constraints: COUNT, FILTER, negation -- impossible with similarity search
- Negation: "Which entities do NOT have relationship R?"

**When it fails:** Unstructured content (must extract entities first), fuzzy/exploratory queries, cold-start (significant upfront ontology design).

## 4. Hybrid Retrieval (Production Patterns)

### HybridRAG (NVIDIA/BlackRock)
Two parallel channels: VectorRAG (embed chunks, cosine similarity) + GraphRAG (entity extraction, graph traversal). Both results concatenated before LLM generation. Tested on financial earnings transcripts. Outperforms both individual approaches on retrieval accuracy and answer quality.

### Microsoft GraphRAG
LLM-based graph construction -> Leiden community detection -> hierarchical summarization.

Scale: Podcast corpus (1M tokens) -> 8,564 nodes, 20,691 edges -> 34 root communities -> 367 at C1 -> 969 at C2 -> 1,310 leaf communities.

Quantitative vs naive vector RAG:
- Comprehensiveness win rate: 72-83%
- Diversity win rate: 75-82%
- Claims per answer: 31-34 vs 25-27
- Token efficiency: root summaries used 2.6% of max context (9-43x reduction)

Cost: Graph indexing for 1M tokens took 281 minutes with GPT-4-turbo. This is the main drawback -- LLM-expensive indexing.

Key difference: Naive RAG retrieves similar chunks. GraphRAG answers "global sensemaking" questions requiring synthesis across the entire corpus.

### Reciprocal Rank Fusion (RRF)
Standard merging technique: each strategy produces ranked list, RRF computes `1/(k + rank)`, sums across lists. Simple, parameter-light, consistently outperforms learned fusion.

### Production Systems
- **Glean:** vector + BM25 + organizational knowledge graph (permissions, ownership, reporting structure)
- **Neo4j + Pinecone:** vector search -> entity extraction -> graph enrichment -> merged context for LLM
- **Semantic Scholar:** papers + citations graph + semantic similarity

### Cost of a 3-Strategy System
- Vector DB: ~$70/month per 1M vectors
- Graph DB: ~$65/month for 200K nodes / 400K relationships
- BM25 index: ~$50/month managed
- Embedding computation: ~$0.10 per 1M tokens one-time
- Graph extraction: periodic LLM re-runs as docs change

## Comparison Matrix

| Strategy | Best For | Scale Limit | Latency | Index Cost |
|----------|----------|-------------|---------|------------|
| BM25/grep | Exact terms, code, structured data | Unlimited (streaming) | <1s to 100K files | Zero |
| Vector search | Semantic similarity, paraphrase | Billions (managed) | 10-100ms at 1M | $0.10/1M tokens |
| SPARQL/KG | Multi-hop, provenance, aggregation | 35M (Oxigraph), 1T+ (QLever) | 20-750ms/query | High (extraction) |
| GraphRAG | Global sensemaking, themes | ~2M tokens practical | Seconds (map-reduce) | $$$ (LLM indexing) |
| Hybrid (RRF) | Diverse queries, robustness | Sum of components | Max of components | Sum of components |

## Key Insight: No Single Strategy Suffices at Scale

At 27 documents, grep + a good index might be enough.
At 1,000+ sources, you need at minimum: structured index (navigation) + vector search (discovery) + graph (relationships).
At 10,000+, add GraphRAG-style community summaries for global sensemaking.

The question is not "which strategy?" but "how do you tier them?"

```
Query
  |
  v
Tier 1: Wiki Index (navigate structured pages, near-zero cost)
  |
  v
Tier 2: Ontology SPARQL (follow typed relationships, dependencies)
  |
  v
Tier 3: Vector Search (semantic discovery, fuzzy matching)
  |
  v
Tier 4: Full-text grep (exact match fallback, precision)
  |
  v
Merge via RRF --> Answer with provenance
```

## References

- [HybridRAG paper](https://arxiv.org/abs/2408.04948) -- NVIDIA/BlackRock, August 2024
- [Microsoft GraphRAG](https://arxiv.org/html/2404.16130v2) -- Edge et al., April 2024
- [Oxigraph benchmarks](https://github.com/oxigraph/oxigraph/blob/main/bench/README.md)
- [ripgrep benchmarks](https://burntsushi.net/ripgrep/)
- [OpenSearch hybrid search](https://opensearch.org/blog/opensearch-3-3-performance-innovations-for-ai-search-solutions/)
- [Pinecone + Neo4j](https://www.pinecone.io/learn/vectors-and-graphs-better-together/)
- [Wikidata SPARQL scaling](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/WDQS_backend_update/August_2021_scaling_update)
- [QLever engine](https://github.com/ad-freiburg/qlever)

> Continue to [Part 3: Our Architecture -- Designing for 1000+ Sources](knowledge-architecture-comparison-part3.md)

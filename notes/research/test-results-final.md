---
title: "Final Test Results: 4-Tier Hybrid Retrieval (#23)"
type: test-result
issue: "#23"
epic: "#17"
date: 2026-04-07
status: final
---

# Final Test Results: 4-Tier Hybrid Retrieval

All 3 scenarios executed with full pipeline: Wiki + Ontology (389 triples) + RAG (61 docs) + Grep.

## Scenario 1: Classification Taxonomies (9 ground truth)

| Tier | Score (/9) | Tool Calls | Notes |
|------|-----------|------------|-------|
| Wiki | 9/9 | 2 reads | All 9 listed in topic index |
| Ontology | 9/9 | 1 SPARQL | All 9 as Concept entities |
| RAG EN | points to file | 1 query | classifications.md is top hit (0.091) |
| RAG RU | 0 direct | 1 query | Finds assessment docs, not taxonomies |
| Grep | ~5-6 | 1 count | Partial: misses sections without search terms |
| **Merged** | **9/9** | **6** | Wiki + Ontology both perfect independently |

## Scenario 2: AI Agents (8 ground truth categories)

| Tier | Score (/8) | Tool Calls | Notes |
|------|-----------|------------|-------|
| Wiki | 7/8 | 2 reads | Missing: ontology self-reference |
| Ontology | 8/8 | 2 SPARQL | All 8 as Concept entities |
| RAG EN | 7/8 | 1 query | Wiki page top hit (0.14), papers found |
| RAG RU | ~2/8 | 1 query | Weak: course syllabi only |
| Grep | 7/8 | 3 | 80 files, 75% noise (infra/test files) |
| **Merged** | **8/8** | **9** | Ontology is only tier with perfect 8/8 |

## Scenario 3: Multi-Hop Chain (PKS-3 -> Lecture -> Research -> Papers -> Seminars)

| Hop | Wiki | Ontology | RAG | Grep |
|-----|------|----------|-----|------|
| PKS-3 found | PASS | PASS | PASS | PASS |
| -> LO1 | PASS | PASS | PASS | PARTIAL |
| -> Lecture 1 | PASS | PASS | PASS | FAIL |
| -> Research | PASS | PASS | PASS | FAIL |
| -> Papers | PASS | PASS | PASS | FAIL |
| -> Seminars | PASS | PASS | PASS | FAIL |
| **Score** | **6/6** | **6/6** | **6/6** | **1.5/6** |
| **Tool calls** | **2** | **3** | **2** | **1** |

## Before/After Comparison

### Scenario 1

| Method | Baseline (pre-wiki) | Final (4-tier) | Delta |
|--------|---------------------|----------------|-------|
| Best single tier | Direct Read 9/9, 1 call | Wiki 9/9, 2 calls | Structured navigation vs knowing file path |
| Ontology | 0/9 | 9/9 | +9 (was empty) |
| RAG | 0/9 | Top hit correct | +major (was not ingested) |
| Total tool calls | 10 (all methods) | 6 (all tiers) | -40% |

### Scenario 2

| Method | Baseline | Final | Delta |
|--------|----------|-------|-------|
| Best automated | Grep 5/8, 70% noise | Wiki 7/8, 0% noise | +2 categories, zero noise |
| Ontology | 0/8 | 8/8 | +8 (was empty) |
| RAG EN | 1/8 | 7/8 | +6 |
| Manual assembly | 8/8, 13 reads | Ontology 8/8, 2 queries | Same score, 85% fewer calls |
| Total tool calls | 25 (all methods) | 9 (all tiers) | -64% |

### Scenario 3

| Metric | Baseline | Final | Delta |
|--------|----------|-------|-------|
| Hops completed | 4/5 | 6/6 (3 tiers) | +2 hops |
| SPARQL chain | FAIL | PASS (all queries) | Fixed |
| Wiki-only traversal | N/A | 6/6 in 2 reads | New capability |
| Tool calls | 18 | 8 | -56% |
| Broken links | 3 | 0 | Fixed |

## Tier Effectiveness Summary

| Tier | Best For | Weakness |
|------|----------|----------|
| Wiki | Navigation, structured lookup, human-readable | Doesn't reference ontology metadata |
| Ontology | Relational queries, chain traversal, perfect recall | Requires session-start loading |
| RAG EN | File discovery, paper content, semantic matching | Chunks too small for enumeration |
| RAG RU | Russian course docs, normative documents | Can't bridge to English content |
| Grep | Exact string matches, first hop | Can't follow semantic relationships |

## Known Limitations

1. **RAG cross-lingual gap**: Embedding model doesn't support RU->EN semantic matching. Workaround: /query-kb always runs bilingual queries.
2. **Ontology not persistent**: Oxigraph is in-memory. Must load store.ttl each session. Workaround: /query-kb Step 0 auto-loads.
3. **Grep noise**: 75% of agent-related grep hits are infrastructure files. Workaround: use Wiki/Ontology first.
4. **Wiki coverage**: 1 lecture page (lec-01), 10 topics. Lectures 2-17 not yet compiled.

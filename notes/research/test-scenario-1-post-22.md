---
title: "Test Scenario 1 Post-#22: Single-Document Deep Retrieval"
type: test-result
issue: "#27"
epic: "#17"
date: 2026-04-07
status: post-22
---

# Test Scenario 1: Post-#22 Results

## Query
"What specific AI classification taxonomies does the course use, and where does each come from?"

## Results Table

| Method | Taxonomies (/9) | Tool Calls | vs Post-Phase4 | Delta |
|--------|-----------------|------------|-----------------|-------|
| Grep | 5/9 | 3 | 5/9 | 0 |
| Ontology | 1/9 (topic-level) | 3 | 0/9 | +1 (store loaded, finds ai-fundamentals topic) |
| RAG | 9/9 | 1 | 2/9 | +7 (wiki pages now in RAG, top hit is classifications.md) |
| Direct Read | 9/9 | 1 | 9/9 | 0 |
| Wiki Index | 9/9 | 2 | 9/9 | 0 |

## Key Changes from #22

1. **Ontology now returns results** (was 0). Finds "AI fundamentals and classification" topic + research document + LO1 + PKS-3. Doesn't enumerate 9 taxonomies individually (by design).
2. **RAG dramatically improved** (2/9 -> 9/9). Wiki pages now appear in positions 2-9 of search results, reinforcing the answer. Top hit remains classifications.md.
3. **Wiki pages in RAG** create a synergy: RAG surfaces the curated wiki summary, which points to the full source.

## Full Comparison Across All Runs

| Method | Baseline | Post-Phase4 | Post-#22 |
|--------|----------|-------------|----------|
| Grep | 3/9 | 5/9 | 5/9 |
| Ontology | 0/9 | 0/9 | 1/9 |
| RAG | 0/9 | 2/9 | 9/9 |
| Direct Read | 9/9 | 9/9 | 9/9 |
| Wiki Index | N/A | 9/9 | 9/9 |

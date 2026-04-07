---
title: "Test Scenario 2 Post-#22: Cross-Document Thematic Search"
type: test-result
issue: "#28"
epic: "#17"
date: 2026-04-07
status: post-22
---

# Test Scenario 2: Post-#22 Results

## Query
"Find everything in the repo about AI agents."

## Results Table

| Method | Categories (/8) | Tool Calls | vs Post-Phase4 | Delta |
|--------|-----------------|------------|-----------------|-------|
| Grep broad | 5/8 | 1 | 5/8 | 0 |
| Grep narrow | 3/8 | 1 | 3/8 | 0 |
| Ontology | 2/8 | 4 | 0/8 | +2 (topic + research doc found) |
| RAG EN | 6/8 | 1 | 4/8 | +2 (wiki page is now top hit) |
| RAG RU | 1/8 | 1 | 2/8 | -1 (scoring variation) |
| Manual | 8/8 | 6 | 8/8 | 0 |
| Wiki Index | 7/8 | 1 | 7/8 | 0 (but now 1 read vs 3) |

## Key Changes from #22

1. **Ontology now functional** (was 0/8). Returns topic_ai_agents and research_agents document. Still lacks sub-topic modeling.
2. **RAG EN improved** (4/8 -> 6/8). Wiki ai-agents page is now top hit (score 0.16). Covers definitions, architectures, frameworks, autonomy levels, key papers, and partial course coverage.
3. **Wiki + RAG synergy**: RAG surfaces the wiki page, which is the single best summary document.

## Full Comparison Across All Runs

| Method | Baseline | Post-Phase4 | Post-#22 |
|--------|----------|-------------|----------|
| Grep broad | 5/8 | 5/8 | 5/8 |
| Ontology | 0/8 | 0/8 | 2/8 |
| RAG EN | 1/8 | 4/8 | 6/8 |
| RAG RU | 0/8 | 2/8 | 1/8 |
| Manual | 8/8 | 8/8 | 8/8 |
| Wiki Index | N/A | 7/8 | 7/8 |

---
title: "Test Scenario 1 Post-Phase4: Single-Document Deep Retrieval"
type: test-result
test_type: tool-test
issue: "#27"
epic: "#17"
date: 2026-04-07
status: post-phase4
---

# Test Scenario 1: Post-Phase4 Results

## Query
"What specific AI classification taxonomies does the course use, and where does each come from?"

## Ground Truth (9 taxonomies)
1. By Task Type -- Russell & Norvig 2021
2. By Modality -- Baltrusaitis et al. 2019
3. By Learning Approach -- Mitchell 1997, Bishop 2006, Sutton & Barto 2018
4. By Capability Level (ANI/AGI/ASI) -- Searle 1980, Bostrom 2014
5. By Architecture -- Vaswani et al. 2017, Ho et al. 2020
6. Generative vs Discriminative -- Ng & Jordan 2001, Goodfellow et al. 2014
7. Foundation Models -- Bommasani et al. 2021
8. Agentic AI -- Masterman et al. 2024
9. Hintze's 4 Types -- Hintze 2016

## Results Table

| Method | Taxonomies (/9) | Tool Calls | Notes |
|--------|-----------------|------------|-------|
| Grep | 5/9 | 3 | Misses sections without "classif/taxonom" in header |
| Ontology | 0/9 | 2 | Store empty (0 triples, not persisted across sessions) |
| RAG | 2/9 | 1 | Title chunk + Hintze chunk; slight scoring variation from prior run |
| Direct Read | 9/9 | 1 | Perfect -- all taxonomies with sources |
| Wiki Index | 9/9 | 2 | Perfect -- all 9 listed with citations; cross-links working |

## Phase 4 Cross-Link Verification

- All `[[wiki-link]]` syntax resolved to relative markdown links: CONFIRMED
- Backlinks section present on ai-fundamentals topic page: CONFIRMED
- Related Topics section present: CONFIRMED
- Bidirectional navigation (index -> topic -> lecture -> back): CONFIRMED

## Comparison Across All Runs

| Method | Baseline | Post-Compile-2 | Post-Phase4 | Trend |
|--------|----------|-----------------|-------------|-------|
| Grep | 3/9 | 5/9 | 5/9 | Stable |
| Ontology | 0/9 | 0/9 | 0/9 | Blocked (empty store) |
| RAG | 0/9 | 3/9 | 2/9 | +2-3 from baseline (chunk scoring varies) |
| Direct Read | 9/9 | 9/9 | 9/9 | Gold standard |
| Wiki Index | N/A | 9/9 | 9/9 | Stable, cross-links now working |

---
title: "Test Scenario 1 Post-Compile-2: Single-Document Deep Retrieval"
type: test-result
test_type: tool-test
issue: "#27"
epic: "#17"
date: 2026-04-07
status: post-compile-2
---

# Test Scenario 1: Post-Compile-2 Results

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

| Method | Taxonomies (/9) | Tool Calls | Precision | Recall | Notes |
|--------|-----------------|------------|-----------|--------|-------|
| Grep | 5/9 | 3 | 0.83 | 0.56 | Misses sections whose headers lack search terms |
| Ontology | 0/9 | 2 | N/A | 0.00 | Store empty (0 triples); data not persisted |
| RAG | 3/9 | 1 | 0.50 | 0.33 | Returns fragments; best score 0.108; knows file but not all |
| Direct Read | 9/9 | 1 | 1.00 | 1.00 | Perfect: all taxonomies + all sources in 185 lines |
| Wiki Index | 9/9 | 3 | 1.00 | 1.00 | Perfect: index -> topic page enumerates all 9 with citations |

## Aggregate Metrics

| Metric | Value |
|--------|-------|
| Total tool calls | 10 |
| Best single method | Direct Read (9/9, 1 call) |
| Runner-up | Wiki Index (9/9, 3 calls) |

## Comparison to Baseline

| Method | Baseline | Post-Compile-2 | Delta |
|--------|----------|-----------------|-------|
| Grep | 3/9 | 5/9 | +2 (context lines revealed more) |
| Ontology | 0/9 | 0/9 | 0 (store empty, 0 triples) |
| RAG | 0/9 | 3/9 | +3 (top chunk is exact file) |
| Direct Read | 9/9 | 9/9 | 0 (as expected) |
| Wiki Index | N/A | 9/9 | New method, perfect |

## Key Findings

1. Direct Read remains gold standard for single-document retrieval (1 call, perfect).
2. Wiki Index is the structured equivalent -- navigable path from index to topic to source, 9/9 in 3 calls.
3. Grep improved to 5/9 (from 3/9) with context, but fundamentally limited by keyword matching.
4. RAG improved to 3/9 (from 0/9) -- correctly identifies target file but returns fragments only.
5. Ontology non-functional -- 0 triples in Oxigraph store.

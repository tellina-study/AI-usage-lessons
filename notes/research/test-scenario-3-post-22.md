---
title: "Test Scenario 3 Post-#22: Multi-Hop Dependency Traversal"
type: test-result
issue: "#29"
epic: "#17"
date: 2026-04-07
status: post-22
---

# Test Scenario 3: Post-#22 Results

## Query
"Trace PKS-3 -> lecture -> research -> papers -> seminar assessment."

## Results Table

| Hop | From -> To | Method | Success | vs Post-Phase4 |
|-----|-----------|--------|---------|-----------------|
| 1 | RPD -> Requirement | Grep | YES | Same |
| 2 | Req -> Lecture | Wiki + SPARQL | YES | IMPROVED: SPARQL now returns 24-row chain |
| 3 | Lecture -> Research | Wiki + SPARQL | YES | IMPROVED: onto_query returns 5 supports relations |
| 4 | Research -> Papers | Read + Glob | YES | Same |
| 5 | Req -> Seminar | Wiki + SPARQL | YES | IMPROVED: 17-row assessment chain via SPARQL |
| 6 | Ontology full chain | SPARQL | **YES** | **FIXED: was NO** |

## SPARQL Chain Results

| Query | Rows | Description |
|-------|------|-------------|
| Req -> LO -> Lecture (3-hop) | 24 | All PKS-3/PKS-4 through LO1-8 to Lec 1-8 |
| Req -> LO -> Lecture -> Topic -> Document (5-hop) | 55KB+ | Full chain to research documents |
| Req -> LO -> Seminar | 17 | Sem 1, 5, 10, 17 linked via assesses |
| Research supports lec_01 | 5 | All 5 research notes with file paths |

## Aggregate Metrics

| Metric | Baseline | Post-Phase4 | Post-#22 |
|--------|----------|-------------|----------|
| Hops completed | 4/5 | 5/5 | 5/5 + ontology |
| Ontology chain | FAIL | FAIL | **PASS (all 4 queries)** |
| Tool calls (non-ontology) | 18 | 8 | 8 |
| Broken links | 3 | 0 | 0 |
| Wiki-only traversal | N/A | 7/7 | 7/7 |
| SPARQL-only traversal | N/A | N/A | **4/4 queries pass** |

## Key Change from #22

The ontology is now the **second complete traversal path** alongside the wiki. Full chain from PKS-3 through LOs, lectures, topics, documents, and seminars — all via SPARQL. This was the single biggest gap identified in all prior test runs.

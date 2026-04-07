---
title: "Test Scenario 3 Post-Phase4: Multi-Hop Dependency Traversal"
type: test-result
test_type: tool-test
issue: "#29"
epic: "#17"
date: 2026-04-07
status: post-phase4
---

# Test Scenario 3: Post-Phase4 Results

## Query
"The RPD requires competency in 'understanding AI classification approaches'. Trace: requirement -> lecture -> research notes -> papers -> seminar assessment."

## Expected Chain
```
PKS-3 (RPD competency)
  -> LO1 (Learning Outcome: classify AI solution types)
    -> Lecture 1 (covers classification)
      -> notes/research/lecture-1/classifications.md (9 taxonomies, 25+ papers)
        -> 15 downloaded papers in library/papers/lecture-1/
PKS-3 -> assessed by -> Seminar 5 (Midterm 1) + Seminar 17 (Final Exam)
```

## Results Table

| Hop | From -> To | Method | Success | Tool Calls | Chain Status |
|-----|-----------|--------|---------|------------|--------------|
| 1 | RPD -> Requirement | Grep | YES | 1 | PKS-3 in 2 docs |
| 2 | Req -> Lecture | Read + Wiki | YES | 2 (+2 failed ontology) | Wiki provides direct PKS-3->LO1->Lec mapping |
| 3 | Lecture -> Research | Grep + Wiki | YES | 1 | Wiki lec-01 has full research index |
| 4 | Research -> Papers | Read + Glob + Wiki | YES | 3 | 15 PDFs, manifest, wiki links |
| 5 | Req -> Seminar | Grep + Wiki | YES | 1 | Sem 5 + Sem 17 correct |
| 6 | Ontology full chain | SPARQL | NO | 3 | 0 triples (not persisted) |
| **Total** | | | **5/5 hops** | **8** (+3 failed ontology) | |

## Wiki-Only Traversal (NEW — Phase 4 capability)

| Step | Action | File | Result |
|------|--------|------|--------|
| 1 | Find PKS-3 | wiki/index.md line 82 | PKS-3 -> LO1, LO2, LO4, LO5 |
| 2 | Find LO1 -> Lectures | wiki/index.md line 69 | LO1 -> Lectures 1-6, 8 -> Sem 5, 10, 17 |
| 3 | Navigate to Lecture 1 | wiki/lectures/lec-01.md | Full lecture summary |
| 4 | Find Research Notes | lec-01.md lines 28-38 | 10 files linked, incl. classifications.md |
| 5 | Find Papers | lec-01.md lines 40-41 | index.yaml link + 5 key papers |
| 6 | Find Assessment | lec-01.md lines 49-55 | PKS-3->LO1, Sem 5+17 with rubrics |
| 7 | Follow backlinks | lec-01.md lines 57-61 | -> ai-fundamentals, ai-agents, prompt-engineering |

**Wiki-only: 7/7 steps, 3 file reads, full chain traversed.** No grep or glob needed.

## Comparison Across All Runs

| Metric | Baseline | Post-Compile-2 | Post-Phase4 | Trend |
|--------|----------|-----------------|-------------|-------|
| Hops completed | 4/5 | 5/5 | 5/5 | Fixed since post-compile |
| Tool calls | 18 | 13 | 8 (non-ontology) | -56% from baseline |
| Ontology triples | 0 | 0 | 0 | Blocked (not persisted) |
| Broken links | 3 | 2 | 0 | All fixed |
| Wiki-only traversal | N/A | N/A | 7/7 (3 reads) | NEW capability |

## Key Phase 4 Improvements

1. **Wiki-only traversal now possible.** Entire chain navigable from 3 wiki reads — no search tools needed.
2. **Tool calls 13 -> 8** (non-ontology). Wiki pre-computed mappings replace grep searches.
3. **Broken links 2 -> 0.** Cross-link resolution fixed all wiki-internal navigation.
4. **Backlinks enable reverse navigation.** lec-01 -> topic pages -> back to lec-01 works bidirectionally.

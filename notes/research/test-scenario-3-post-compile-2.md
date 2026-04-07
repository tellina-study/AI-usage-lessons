---
title: "Test Scenario 3 Post-Compile-2: Multi-Hop Dependency Traversal"
type: test-result
test_type: tool-test
issue: "#29"
epic: "#17"
date: 2026-04-07
status: post-compile-2
---

# Test Scenario 3: Post-Compile-2 Results

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
| 1 | RPD -> Requirement | Grep + Read RPD doc | YES | 2 | PKS-3 at line 68, indicators at line 79 |
| 2 | Req -> Lecture | Read course-structure.md | YES (manual) | 2 | No machine link; PKS-3->LO1->Lec 1 by inference |
| 3 | Lecture -> Research | Grep in notes/research/lecture-1/ | YES | 1 | Naming convention only, no metadata |
| 4 | Research -> Papers | Read classifications.md + index.yaml | YES | 3 | 25+ cited, 15 indexed, 14 PDFs |
| 5 | Req -> Seminar | Grep sem-* files + context | YES | 2 | Correctly: sem-05 + sem-17 (not sem-01) |
| 6 | Ontology full chain | SPARQL | NO | 3 | 0 triples in store |
| **Total** | | | **5/5 hops** | **13** | Ontology non-functional |

## Aggregate Metrics

| Metric | Value |
|--------|-------|
| Hops completed | 5/5 |
| Total tool calls | 13 |
| Ontology triples used | 0 |
| RAG results used | 0 |
| Broken links in chain | 2 (Hop 2: no machine link, Hop 3: naming only) |

## Comparison to Baseline

| Metric | Baseline | Post-Compile-2 | Delta |
|--------|----------|-----------------|-------|
| Hops completed | 4/5 | 5/5 | +1 (Hop 5 fixed) |
| Total tool calls | 18 | 13 | -5 (28% fewer) |
| Ontology triples | 0 | 0 | no change |
| Broken links | 3 | 2 | -1 (Hop 5 correct now) |

## Key Findings

1. Hop 5 fixed: correctly identifies sem-05 (Midterm 1) + sem-17 (Final Exam), not sem-01.
2. Hop 4 is the strongest link: index.yaml has bidirectional referenced_in fields + 14 PDFs present.
3. Hop 2 still fragile: PKS-3 -> LO1 -> Lecture 1 requires human reasoning, no machine-readable link.
4. Hop 3 still naming-convention only: no manifest maps Lecture 1 -> notes/research/lecture-1/.
5. Ontology completely empty: 0 triples, schema exists but no instance data loaded.

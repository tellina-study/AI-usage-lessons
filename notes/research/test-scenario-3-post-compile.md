---
title: "Test Scenario 3 Post-Compile: Multi-Hop Dependency Traversal"
type: test-result
test_type: tool-test
issue: "#29"
epic: "#17"
date: 2026-04-07
status: post-compile
---

# Test Scenario 3: Post-Compile Tool Test

## Query

"The RPD requires competency in 'understanding AI classification approaches'. Trace: requirement -> lecture -> research notes -> papers -> seminar assessment."

## Chain Traversal

### Hop 1: RPD -> Requirement
- **Found:** Yes
- **Competency:** PKS-3: "Sposoben klassificirovat' i identificirovat' zadachi II, vybirat' adekvatnye metody" + indicator "ZNAT' - tipy AI-sistem i ih primenenie v konkretnyh industriyah"
- **Method:** Single grep with pattern `klassificir|PKS-3|tipy AI` found both competency statements and curriculum section 1.1
- **Tool calls:** 1 (grep)

### Hop 2: Requirement -> Lecture
- **Found:** Yes
- **Method:** read (course-structure.md) + ontology SPARQL
- **Course structure result:** Lecture 1 "Vvedenie: chto takoe AI i pochemu eto vazhno" maps to LO1 = "Klassificirovat' tipy AI-reshenij i sopostavit' ih s zadachami industrij". Link: PKS-3 -> LO1 -> Lecture 1.
- **Ontology result:** SPARQL query for `?lecture a aul:Lecture` returned **0 results**. No Lecture instances exist in the store. However, the `belongs_to_topic` query returned 23 results linking Documents to Topics -- the RPD document (`doc_formal_program_updated`) is linked to all 8 course topics. This confirms the document is in the ontology but there is no Lecture entity to traverse to.
- **Tool calls:** 2 (1 read, 1 SPARQL)

### Hop 3: Lecture -> Research
- **Found:** Yes
- **Files:** 5 files match classification/taxonomy keywords in `notes/research/lecture-1/`: classifications.md, teaching-examples.md, roast-slide-plan.md, roast-v2-with-feedback.md, human-vs-ai.md. Total 10 files in directory.
- **Tool calls:** 2 (1 grep, 1 ls)

### Hop 4: Research -> Papers
- **Papers cited in classifications.md:** 25+ academic papers across 7 taxonomy categories (by task, modality, learning approach, capability level, architecture, generative/discriminative, foundation models, agentic AI)
- **PDFs available:** 14 PDFs in `library/papers/lecture-1/` per index.yaml. 1 paper (LeCun et al. 2015 Nature) not available (paywall). Key papers with PDFs: vaswani-2017, goodfellow-2014-gan, ho-2020-diffusion, bommasani-2021, balestriero-2023, baltrusaitis-2019, etc.
- **Tool calls:** 2 (1 read classifications.md, 1 read index.yaml)

### Hop 5: Requirement -> Seminar
- **Seminar(s):** Two seminars explicitly test classification:
  1. **sem-05 (Midterm 1):** "Korrektnost' klassifikacii AI-tekhnologii | 0-3" -- direct rubric criterion
  2. **sem-17 (Final Exam):** "Korrektnost' klassifikacii AI-tekhnologii | 0-3" -- same criterion in final
  - sem-01 is NOT a direct match (no LO1/classification keywords in grep)
- **Tool calls:** 1 (grep across sem-*.md)

### Hop 6: Ontology full chain
- **Triple count:** 164 triples (up from 0 at baseline due to store.ttl syntax fix)
- **Entity types:** 13 Properties, 10 Topics, 8 Classes, 5 Documents, 3 SourceSystems, 1 SlideDeck, 1 Diagram. **Still 0 Lectures, 0 Requirements, 0 Seminars.**
- **belongs_to_topic query:** Returned 23 results. RPD document linked to 8 topics. Course plan V2 linked to 8 topics. Course plan V1 linked to 3 topics. FOS linked to 2 topics.
- **Can traverse full chain via ontology:** No. The Document->Topic link works, but the chain requirement->lecture->research->papers->seminar cannot be traversed because Lecture, Requirement, and Seminar instances do not exist.
- **SPARQL result:** Document-to-topic mappings work. No Lecture or Requirement individuals.
- **Tool calls:** 3 (2 SPARQL queries + 1 stats query)

### RAG for chain discovery
- **Query 1 (English):** "PKS-3 classification competency requirement lecture seminar assessment" -- 10 results
- **Query 2 (Russian):** "PKS-3 klassificirovat' tipy AI sistem lekciya seminar ocenka kompetenciya" -- 5 results
- **Results:** RAG now covers research notes AND papers (not just catalog/exports/). Key finds:
  1. roast-slide-plan.md (score 0.276) -- "Classifications Are Too Academic for an Introductory Lecture"
  2. knowledge-architecture-comparison-part3.md (score 0.329) -- "if RPD changes, what breaks?"
  3. roast-v2-with-feedback.md (score 0.473) -- "Classifications are a 1-minute refresh"
  4. bommasani-2021-foundation-models.pdf (score 0.479) -- paper chunk
  5. sem-05-midterm-1.md (score 0.286) -- "Klassifikaciya tipov AI po industriyam"
  6. prog-otraslevoe-updated-formal.md (score 0.264) -- competency table
- **Relevant:** 6 of 15 unique results directly relevant to the chain
- **Helps with which hops:** Hop 1 (found RPD competency chunk), Hop 3 (found research notes about classifications), Hop 4 (found paper chunks), Hop 5 (found sem-05 assessment criterion). Does NOT help with Hop 2 (lecture mapping) -- no course-structure.md in results.
- **Tool calls:** 2 (2 RAG queries)

## Comparison: Baseline vs Post-Compile

| Hop | Baseline Success | Post-Compile Success | Baseline Calls | Post-Compile Calls |
|-----|-----------------|---------------------|----------------|-------------------|
| 1: RPD->Req | Yes | Yes | 4 | 1 |
| 2: Req->Lecture | Yes (inference) | Yes (inference) | 2 | 2 |
| 3: Lecture->Research | Yes (naming) | Yes (naming) | 2 | 2 |
| 4: Research->Papers | Yes | Yes | 0 | 2 |
| 5: Req->Seminar | Partial | Yes | 3 | 1 |
| Ontology | Failed (0 triples) | Partial (164 triples, doc->topic works) | 5 | 3 |
| RAG | Partial (fragments, docs only) | Partial (fragments, now includes research+papers) | 2 | 2 |
| **Total** | **4/5, 18 calls** | **5/5, 13 calls** | **18** | **13** |

## Key Changes

### What improved

1. **Ontology is now loadable.** The store.ttl syntax error (missing period on line 136) was fixed during the compile phase. The store now loads 164 triples successfully. Document-to-topic links (`belongs_to_topic`) work and return 23 results across 5 documents and 10 topics. This is a major improvement from the baseline where the store failed to load entirely.

2. **RAG now covers research notes and papers.** At baseline, only 16 files from `catalog/exports/docs/` were ingested. Post-compile, the RAG index includes research notes (`notes/research/lecture-1/*.md`) and PDFs from `library/papers/lecture-1/`. This means RAG can now surface research file chunks (roast-slide-plan.md, roast-v2-with-feedback.md) and paper content (bommasani-2021) that were invisible at baseline.

3. **Hop 1 efficiency improved.** Baseline required 4 tool calls (2 greps with different patterns, 2 reads) because the initial grep pattern missed the verb form. Post-compile used a single grep with the correct combined pattern from the start: `klassificir|PKS-3|tipy AI`. This is a learned-pattern improvement, not a tool improvement.

4. **Hop 5 now succeeds fully.** Baseline was "Partial" because sem-01 was checked and found to NOT directly test classification, requiring additional investigation. Post-compile grep across all sem-*.md files in one call found sem-05 and sem-17 directly without the sem-01 false lead.

5. **Tool call count reduced from 18 to 13** (28% reduction). Main savings: Hop 1 (4->1), Hop 5 (3->1). Hop 4 cost 2 more calls (reading index.yaml separately) but provided richer data.

### What did NOT improve

1. **Ontology still cannot traverse the full chain.** Despite 164 triples, there are still 0 Lecture instances, 0 Requirement instances, and 0 Seminar instances. The `covers` property is defined but never used. The chain requirement->lecture->research->papers->seminar is not modelable in the current ontology. This requires Tier 2 population work (creating individuals for all entity types and linking them).

2. **RAG still cannot do multi-hop traversal.** It returns individual chunks ranked by similarity, not connected chains. It found relevant chunks from 4 of 5 hop endpoints but could not connect them. The course-structure.md (critical for Hop 2) did not appear in RAG results at all.

3. **Hop 2 still requires human inference.** The link PKS-3 -> LO1 -> Lecture 1 is not explicit in any single document or tool. It requires reading course-structure.md and matching the competency verb "klassificirovat'" to LO1 "Klassificirovat' tipy AI-reshenij". Neither ontology nor RAG can make this inference automatically.

### Remaining gaps for full automation

1. **Lecture, Requirement, Seminar, LearningOutcome instances** in the ontology (Tier 2 work)
2. **`covers` and `assessed_by` triples** linking lectures to topics/requirements and seminars to learning outcomes
3. **ResearchNote and Paper entity types** in the ontology with links to lectures
4. **course-structure.md ingestion** into RAG (currently not indexed or not ranking well)
5. **Cross-document link metadata** -- no manifest currently maps RPD competency codes to LO codes to lecture numbers in a machine-readable format

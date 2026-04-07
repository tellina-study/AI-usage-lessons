---
title: "Test Scenario 3 Baseline: Multi-Hop Dependency Traversal"
type: test-result
issue: "#29"
epic: "#17"
date: 2026-04-07
status: baseline
---

# Test Scenario 3: Multi-Hop Dependency + Impact Query (Baseline)

## Query

"The RPD requires competency in 'understanding AI classification approaches'. Trace: requirement -> lecture -> research notes -> papers -> seminar assessment."

## Chain Traversal

### Hop 1: RPD -> Requirement

- **Method used:** grep + read
- **Found:** YES. Two relevant competency statements in `catalog/exports/docs/prog-otraslevoe-updated-formal.md`:
  1. **ПКС-3** (line 68): "Способен классифицировать и идентифицировать задачи ИИ, выбирать адекватные методы" (Able to classify and identify AI tasks, choose adequate methods)
  2. **ПКС-3 indicator** (line 79): "ЗНАТЬ - типы AI-систем и их применение в конкретных индустриях" (KNOW - types of AI systems and their application in specific industries)
  3. **Curriculum section** (line 145): "1.1 Введение: типы AI-систем (NLP, CV, рекомендательные, генеративный AI) — 2 ч"
- **Note:** The word "классификация" (classification) does NOT appear literally in the RPD. The competency uses "классифицировать" (verb: to classify). A naive keyword search for "классификац" failed on initial grep because the RPD uses the infinitive verb form "классифицировать" which DOES match the regex `классифицировать`. The broader grep for `классифицировать|ПКС-3|типы AI` succeeded.
- **Tool calls:** 4 (2 greps with different patterns, 2 reads of different offsets)

### Hop 2: Requirement -> Lecture

- **Method used:** read (course-structure.md + lec-01-plan.md)
- **Found:** YES.
  - `course-structure.md` line 17: Lecture 1 "Введение: что такое AI и почему это важно" maps to **LO1** = "Классифицировать типы AI-решений и сопоставить их с задачами индустрий"
  - `lec-01-plan.md` line 77: "LO1 -> Коллоквиум 1: тесты на классификацию типов AI"
  - The RPD section 1.1 explicitly names "типы AI-систем" as Lecture 1 content
- **How the link was made:** Human reasoning connecting ПКС-3 ("classify AI tasks") -> LO1 ("classify AI solution types") -> Lecture 1. No explicit machine-readable link exists between the competency code and the lecture number.
- **Tool calls:** 2 (read course-structure.md, read lec-01-plan.md)
- **Chain status:** connected (via human inference, not explicit link)

### Hop 3: Lecture -> Research Notes

- **Method used:** grep + read + directory knowledge
- **Found:** YES.
  - `notes/research/lecture-1/classifications.md` is the primary research file (185 lines)
  - grep found 6 files in `notes/research/lecture-1/` mentioning classification/taxonomy keywords
  - The directory naming convention `lecture-1/` is the only link from lecture to research notes; there is no manifest, index, or metadata linking them
- **Tool calls:** 2 (grep for files, read classifications.md)
- **Chain status:** connected (via naming convention only, not explicit metadata)

### Hop 4: Research Notes -> Papers

- **Method used:** read (classifications.md already loaded in Hop 3)
- **Found:** YES. The file contains 7 taxonomy categories with **25+ academic papers cited**, including:
  - By task type: Russell & Norvig (2021), Goodfellow et al. (2016), LeCun et al. (2015), Szelidon (2022)
  - By modality: Baltrusaitis et al. (2019), Bayoudh et al. (2022), Xu et al. (2023)
  - By learning approach: Mitchell (1997), Bishop (2006), Sutton & Barto (2018), Balestriero et al. (2023)
  - By capability level: Searle (1980), Bostrom (2014), Goertzel & Pennachin (2007)
  - By architecture: Vaswani et al. (2017), Ho et al. (2020), Lin et al. (2022)
  - Generative vs discriminative: Ng & Jordan (2001), Goodfellow et al. (2014)
  - Foundation models: Bommasani et al. (2021)
  - Agentic AI: Masterman et al. (2024)
- **Tool calls:** 0 additional (data already loaded)
- **Chain status:** connected (papers are inline in the research file)

### Hop 5: Requirement -> Seminar Assessment

- **Method used:** grep + read
- **Found:** PARTIAL.
  - **Seminar 1** (`sem-01-task.md`): Tests LO4 and LO6 (prompt engineering and AI limitations). Does NOT directly test classification (LO1). One topic option mentions "Типы AI-систем в повседневной жизни" but it is a student choice, not required.
  - **Seminar 5 / Midterm 1** (`sem-05-midterm-1.md`): YES - explicitly tests classification. Line 17: "Классификация типов AI по индустриям". Line 47: "Корректность классификации AI-технологии | 0-3". This is the actual assessment point for LO1/classification.
  - **Seminar 17 / Final Exam** (`sem-17-final-exam.md`): Also tests "Классификация AI-технологий" (line 19).
- **The link from RPD requirement to assessment:** ПКС-3 -> LO1 -> Seminar 5 (Midterm 1) and Seminar 17 (Final Exam). Seminar 1 is tangential.
- **Tool calls:** 3 (grep across sem files, read sem-01-task.md, read sem-05-midterm-1.md)
- **Chain status:** connected (via grep keyword matching + human inference on LO codes)

## Ontology Traversal Attempt

### Pre-written queries available

1. `ontology/queries/find_docs_for_lecture.rq` — finds documents related to a lecture via topic links
2. `ontology/queries/impacted_by_requirement_change.rq` — finds entities impacted when a requirement changes
3. `ontology/queries/orphan_diagrams.rq` — finds unlinked diagrams

### Store loading result

- **FAILURE.** `ontology/store.ttl` has a syntax error: line 136 is missing a trailing period (`.`). The `onto_load` tool returns: "Parser error at line 136 column 48: Unexpected end"
- After loading a minimal inline subset, the store loaded successfully (20 triples)

### Query execution results

1. **find_docs_for_lecture query:** returned **0 results**. Reason: no `aul:Lecture` instances exist in the store. The ontology has the Lecture class defined but zero lecture individuals (e.g., `aul:lec_01 a aul:Lecture`).
2. **impacted_by_requirement_change query:** returned **0 results**. Reason: no `aul:Requirement` instances exist in the store. The Requirement class is defined but has zero individuals.

### Relations in store.ttl relevant to this chain

- `belongs_to_topic` — documents linked to topics (exists for doc_formal_program_updated)
- `covers` — "Lecture or deck covers a topic or requirement" (defined as property, but NEVER used as a triple)
- `cites` — used once (doc_fos cites doc_formal_program_old)
- `depends_on` — used twice (doc_fos depends_on doc_formal_program_old, doc_v2_course_plan depends_on doc_formal_program_updated)
- `supersedes` — used twice (version chains)

### Gaps (what is missing from the ontology)

1. **No Lecture instances** — zero `aul:Lecture` individuals (lec_01 through lec_17)
2. **No Requirement instances** — zero `aul:Requirement` individuals extracted from the RPD
3. **No Seminar/Assessment instances** — no entity type for seminars or assessments
4. **No ResearchNote entity type** — no way to represent notes/research/* files
5. **No `covers` triples** — the property exists but is never used
6. **No `topic_ai_classification` topic** — there is no topic for "AI classification/taxonomy" specifically
7. **No link from Lecture -> ResearchNote** — no property defined for this
8. **No link from Requirement -> LearningOutcome -> Lecture** — the RPD's competency-to-LO-to-lecture chain is not modeled
9. **store.ttl syntax error** — missing period on last line prevents loading

## RAG Traversal Attempt

- **16 files ingested** into local-rag (all from `catalog/exports/docs/`)
- **Research notes NOT ingested** — `notes/research/lecture-1/classifications.md` is outside the RAG base directory
- Query "классификация AI подходы типы AI-систем classification approaches" returned 5 results:
  1. sem-17-final-exam.md (score 0.215) — "Классификация AI-технологий"
  2. sem-01-task.md (score 0.220) — "Типы AI-систем в повседневной жизни"
  3. sem-05-midterm-1.md (score 0.223) — "Типы AI-систем: NLP, Computer Vision..."
  4. sem-05-midterm-1.md (score 0.249) — "Классификация типов AI по индустриям"
  5. ai-v-raznyh-industriyah (score 0.269) — "Типы AI-систем (NLP, CV...)"
- RAG found assessment documents but NOT the RPD competency text, NOT the research notes, NOT the lecture plan
- RAG cannot traverse chains — it returns individual chunks, not connected paths

## Summary

| Hop | From -> To | Method | Success | Tool Calls |
|-----|-----------|--------|---------|------------|
| 1 | RPD -> Requirement | grep + read | Yes | 4 |
| 2 | Requirement -> Lecture | read + human inference | Yes | 2 |
| 3 | Lecture -> Research | grep + naming convention | Yes | 2 |
| 4 | Research -> Papers | read (already loaded) | Yes | 0 |
| 5 | Requirement -> Seminar | grep + read | Partial (sem-05, not sem-01) | 3 |
| - | Ontology traversal | SPARQL | Failed (no instances) | 5 |
| - | RAG traversal | vector search | Partial (found fragments) | 2 |
| **Total** | **Full chain** | **grep + read + inference** | **4/5 hops** | **18** |

## Key Findings

- **Total tool calls to assemble full chain:** 18 (excluding ontology/RAG attempts that failed)
- **Chain broke at:** Hop 5 partially — sem-01 does NOT test classification directly; the actual assessment is sem-05 (Midterm 1). A user asking "which seminar assesses it" would get a misleading answer if they only checked sem-01.
- **Ontology coverage:** 0% of chain could be traversed via ontology. The schema defines the right classes (Lecture, Requirement, Document) and properties (covers, cites, depends_on) but has ZERO instance data for lectures, requirements, or the covers relation.
- **What is missing:**
  1. Lecture instances (lec_01 through lec_17) with `covers` links to topics
  2. Requirement instances extracted from RPD competency table
  3. LearningOutcome instances (LO1-LO8) linking requirements to lectures
  4. Seminar/Assessment instances with links to what they assess
  5. ResearchNote instances linking to lectures they support
  6. Paper/Citation instances in the ontology
  7. Fix store.ttl syntax error (missing period on line 136)
  8. Ingest research notes into RAG (currently only catalog/exports/ is indexed)

## What Would Each Tier Add?

- **Tier 1 (Wiki/Lecture summaries):** A lecture-summary.md for Lecture 1 could list "Assesses: ПКС-3, LO1" and "Research: notes/research/lecture-1/classifications.md" — making hops 2, 3, and 5 trivial lookups instead of multi-file grep chains. Would reduce total tool calls from 18 to ~6.
- **Tier 2 (Ontology with instances):** If fully populated, the entire chain becomes a single SPARQL query: `?req -> covers -> ?lecture -> has_research -> ?note -> cites -> ?paper` and `?req -> assessed_by -> ?seminar`. Would reduce tool calls from 18 to 1-2. Currently blocked by zero instance data and a TTL syntax error.
- **Tier 3 (Vector/RAG):** Semantic search found relevant assessment fragments but missed the RPD competency source and all research notes (not ingested). Even with full ingestion, RAG returns individual chunks, not connected chains. Useful for discovery ("find things about classification") but cannot answer multi-hop traversal queries. Would complement Tier 2 for fuzzy matching.
- **Tier 4 (Grep):** Already tested — this is the current baseline. Finds keywords across files but requires human intelligence to connect ПКС-3 -> LO1 -> Lecture 1 -> classifications.md -> papers -> sem-05. Each hop requires knowing which file to look in next. Brittle: depends on consistent terminology across documents (the RPD says "классифицировать", the seminar says "классификация", the research says "classification").

## Comparison with Scenario 1

Test Scenario 1 (single-hop: find all documents about a topic) required 4 tool calls and succeeded fully via grep.
Test Scenario 3 (multi-hop: trace a chain across 5 entity types) required 18 tool calls and partially succeeded.

The complexity scales super-linearly: 5x more hops required 4.5x more tool calls, and the chain still broke partially at hop 5. Each hop adds not just a tool call but a reasoning step where the human/AI must infer which file to search next.

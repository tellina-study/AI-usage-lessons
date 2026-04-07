---
title: "Test Scenario 1 Post-Compile: Single-Document Deep Retrieval"
type: test-result
test_type: tool-test
issue: "#27"
epic: "#17"
date: 2026-04-07
status: post-compile
---

# Test Scenario 1: Post-Compile Tool Test

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

## Method Results

### Grep
- Files found in `notes/research/lecture-1/`: 5 files
  - classifications.md: 6 matches
  - roast-slide-plan.md: 4 matches
  - roast-v2-with-feedback.md: 3 matches
  - teaching-examples.md: 1 match
  - human-vs-ai.md: 1 match
- Files found in `catalog/exports/docs/`: 5 files
  - ai-v-raznyh-industriyah.md: 9 matches
  - sem-05-midterm-1.md: 1 match
  - sem-17-final-exam.md: 1 match
  - lec-01-plan.md: 1 match
  - prog-otraslevoe-primenenie-AI.md: 1 match
- Taxonomies identifiable: 0/9 (grep -c returns only match counts per file; no taxonomy names or sources visible without reading files)
- Tool calls: 2

### Ontology (SPARQL)
- Triple count: 164 (store is loaded, not empty)
- Classification-related results: 0 (empty result set -- no entities with labels containing "classif" or "taxonom")
- Taxonomies identifiable: 0/9
- Tool calls: 2

### RAG (Vector Search)
- Results returned: 10
- Relevant results: 6 (directly about classification/taxonomy content)
- Top result: classifications.md chunk 0, score 0.108 (lower = better)
- Results detail:
  1. classifications.md chunk 0 (score 0.108) -- title only, no specific taxonomies
  2. classifications.md chunk 86 (score 0.298) -- mentions "alternative capability taxonomy" (Hintze)
  3. baltrusaitis-2019-multimodal.pdf chunk 284 (score 0.307) -- mentions "concept taxonomies" in passing
  4. roast-v2-with-feedback.md chunk 23 (score 0.307) -- mentions "how you INTERACT with AI" classification
  5. roast-v2-with-feedback.md chunk 84 (score 0.324) -- mentions "ANI/AGI, Supervised/RL, Gen/Disc"
  6. roast-slide-plan.md chunk 132 (score 0.342) -- mentions "Other Classifications"
  7. wang-2023-llm-agents-survey.pdf (score 0.348) -- mentions "comprehensive taxonomies" in passing
  8. roast-slide-plan.md chunk 48 (score 0.381) -- about "AI Around Us", tangential
  9. roast-slide-plan.md chunk 41 (score 0.386) -- mentions "by task type" and "Narrow vs General AI"
  10. model-chat-agent-app.md chunk 125 (score 0.407) -- mentions "AI Agents vs Agentic AI Taxonomy"
- Taxonomies identifiable from RAG snippets: 5/9
  - Partial: By Task Type (from chunk 9), By Capability Level/ANI/AGI (from chunk 5), Generative vs Discriminative (from chunk 5), Hintze's 4 Types (from chunk 2), Agentic AI (from chunk 10)
  - Missing: By Modality, By Learning Approach, By Architecture, Foundation Models
  - Note: identifications are partial -- taxonomy names appear but academic sources are not in the returned chunks
- Tool calls: 1

### Direct Read
- Taxonomies found: 9/9 (all taxonomies with full academic sources)
- Tool calls: 1

## Comparison: Baseline vs Post-Compile

| Method | Baseline Taxonomies | Post-Compile Taxonomies | Baseline Calls | Post-Compile Calls |
|--------|---------------------|-------------------------|----------------|-------------------|
| Grep | 3 partial | 0/9 | 4 | 2 |
| Ontology | 0 (store empty) | 0/9 (store loaded, no taxonomy entities) | 3 | 2 |
| RAG | 0 (not indexed) | 5/9 partial | 2 | 1 |
| Direct Read | 9/9 | 9/9 | 1 | 1 |

## Key Changes

### Improved
- **RAG now works.** Baseline had 0 results because notes/ was not indexed. Post-compile RAG returns 10 results with the correct file (classifications.md) as the top hit (score 0.108). Five of nine taxonomies are partially identifiable from RAG chunk snippets alone.
- **Ontology store is loaded.** Baseline had 0 triples (empty store). Post-compile has 164 triples. The store is functional.
- **Fewer tool calls overall.** Grep used 2 calls (down from 4). Ontology used 2 calls (down from 3). RAG used 1 call (down from 2).

### Not improved
- **Ontology has no taxonomy entities.** Despite 164 triples in the store, none represent classification taxonomies. The compile phase loaded structural/document-level triples but did not ingest taxonomy-level concepts. To fix: ingest classification entities (e.g., aul:TaxonomyByTaskType, aul:TaxonomyByModality) with rdfs:label into the ontology store.
- **Grep still cannot identify taxonomies.** This is inherent to `grep -c` (count mode) -- it only shows match counts, not content. The baseline "3 partial" likely used content-mode grep (not -c). With -c mode, 0 taxonomies are identifiable. This is a method limitation, not a regression.
- **RAG chunks are too small for full answer.** The top RAG hit is the file title, not the content. Chunk granularity means you see fragments, not the full taxonomy list. RAG correctly points you to the right file but cannot replace reading it.

### Summary
The compile phase fixed the two broken tools (RAG indexing, ontology loading) but did not make them sufficient for this query type. For deep single-document retrieval, Direct Read remains the only method that achieves 9/9. RAG's value is as a pointer to the right file (top-1 accuracy is perfect). The ontology needs taxonomy-level entity ingestion to contribute.

# Test Scenario 1: Single-Document Deep Retrieval

> Run this in a fresh Claude Code session. Follow each step exactly. Record all results.
> Issue: #27 | Epic: #17

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

## Steps

### Step 1: Grep
Run and record output:
```
rg "классификац|taxonom|taxonomy|таксоном" notes/research/lecture-1/ --type md -c
rg "классификац|taxonom|taxonomy|таксоном" catalog/exports/docs/ --type md -c
```
Record:
- [ ] Files found (list with match counts)
- [ ] Taxonomies identifiable from grep context alone: __/9
- [ ] Tool calls used: __

### Step 2: Ontology
Run SPARQL via onto_query:
```sparql
PREFIX aul: <https://ai-usage-lessons.local/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?entity ?label ?type WHERE {
  ?entity rdfs:label ?label .
  ?entity a ?type .
  FILTER(CONTAINS(LCASE(str(?label)), "classif") || CONTAINS(LCASE(str(?label)), "taxonom"))
}
```
Also run: `SELECT (COUNT(*) as ?count) WHERE { ?s ?p ?o }` to check if store has data.

Record:
- [ ] Results returned: __
- [ ] Triples in store: __
- [ ] Taxonomies identifiable: __/9
- [ ] Tool calls used: __

### Step 3: RAG
Run via local-rag query_documents:
- Query: "AI classification taxonomies used in the course"
- Limit: 10

Record:
- [ ] Results returned: __
- [ ] Relevant results (about classification): __
- [ ] Best score: __
- [ ] Taxonomies identifiable: __/9
- [ ] Tool calls used: __

### Step 4: Direct Read
Read file: `notes/research/lecture-1/classifications.md`

Record:
- [ ] File lines: __
- [ ] Taxonomies found: __/9
- [ ] All sources identified: yes/no
- [ ] Tool calls used: 1

### Step 5: Wiki Index (post-improvement only)
Read file: `wiki/index.md` and follow links to find classification content.

Record:
- [ ] Entry found in index: yes/no
- [ ] Path to content: __
- [ ] Taxonomies found: __/9
- [ ] Tool calls used: __

## Results Table

Copy and fill:

```
| Method | Taxonomies (/9) | Tool Calls | Precision | Recall | Notes |
|--------|-----------------|------------|-----------|--------|-------|
| Grep | | | | | |
| Ontology | | | | | |
| RAG | | | | | |
| Direct Read | | | | | |
| Wiki Index | | | | | |
| **Total** | | | | | |
```

## Save Results
Save this completed file as:
`notes/research/test-scenario-1-{run-label}.md`

Where {run-label} is: `baseline`, `post-wiki`, `post-retrieval`, etc.

## Baseline Reference
Previous baseline (2026-04-07): `notes/research/test-scenario-1-baseline.md`
- Grep: 3/9, 4 calls
- Ontology: 0/9, 3 calls (store empty)
- RAG: 0/9, 2 calls (notes/ not indexed)
- Direct Read: 9/9, 1 call

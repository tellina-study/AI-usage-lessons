# Test Scenario 3: Multi-Hop Dependency Traversal

> Run this in a fresh Claude Code session. Follow each step exactly. Record all results.
> Issue: #29 | Epic: #17

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

## Steps

### Hop 1: Find the Requirement in RPD
Read: `catalog/exports/docs/prog-otraslevoe-updated-formal.md`
Search for: classification-related competencies
```
rg "классифицир|ПКС-3|типы AI|classification" catalog/exports/docs/prog-otraslevoe-updated-formal.md
```

Record:
- [ ] Requirement found: yes/no
- [ ] Competency code: __
- [ ] Exact text: "__"
- [ ] Line number: __
- [ ] Tool calls: __

### Hop 2: Requirement -> Lecture
Read: `catalog/exports/docs/course-structure.md`
Find which lecture maps to the competency/LO.

Also try ontology:
```sparql
PREFIX aul: <https://ai-usage-lessons.local/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?lecture ?label ?topic ?topicLabel WHERE {
  ?lecture a aul:Lecture ; rdfs:label ?label .
  OPTIONAL { ?lecture aul:covers ?topic . ?topic rdfs:label ?topicLabel }
}
```

Record:
- [ ] Lecture identified: __
- [ ] Method: ontology / grep+read / inference
- [ ] Machine-readable link exists: yes/no
- [ ] Tool calls: __

### Hop 3: Lecture -> Research Notes
Find research notes that support this lecture.
```
rg "классификац|taxonomy|таксоном" notes/research/lecture-1/ -l
```

Record:
- [ ] Research file found: __
- [ ] Link type: explicit metadata / naming convention / grep
- [ ] Tool calls: __

### Hop 4: Research Notes -> Papers
Read the research file found in Hop 3. Extract all cited papers.
Cross-check against: `library/papers/lecture-1/index.yaml`

Record:
- [ ] Papers cited in research: __
- [ ] Papers available as PDFs: __
- [ ] Tool calls: __

### Hop 5: Requirement -> Seminar Assessment
```
rg "классификац|classification|типы AI|LO1|ПКС-3" catalog/exports/docs/sem-*.md
```
Read matched seminar files.

Record:
- [ ] Seminar(s) that assess this: __
- [ ] Sem-01 tests this: yes/no
- [ ] Actual assessment point: __
- [ ] Tool calls: __

### Hop 6: Ontology Full Chain (post-improvement)
Try single SPARQL query to trace entire chain:
```sparql
PREFIX aul: <https://ai-usage-lessons.local/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?req ?lecture ?topic ?doc WHERE {
  ?req a aul:Requirement .
  ?lecture aul:covers ?topic .
  ?doc aul:belongs_to_topic ?topic .
}
```

Record:
- [ ] Results: __
- [ ] Full chain traversable via SPARQL: yes/no
- [ ] Tool calls: __

## Results Table

```
| Hop | From -> To | Method | Success | Tool Calls | Chain Status |
|-----|-----------|--------|---------|------------|--------------|
| 1 | RPD -> Requirement | | | | |
| 2 | Req -> Lecture | | | | |
| 3 | Lecture -> Research | | | | |
| 4 | Research -> Papers | | | | |
| 5 | Req -> Seminar | | | | |
| 6 | Ontology full chain | | | | |
| **Total** | | | **/5 hops** | **sum** | |
```

## Aggregate Metrics

```
| Metric | Value |
|--------|-------|
| Hops completed | /5 |
| Total tool calls | |
| Ontology triples used | |
| RAG results used | |
| Broken links in chain | |
| Morphological sensitivity issues | |
```

## Save Results
Save as: `notes/research/test-scenario-3-{run-label}.md`

## Baseline Reference (2026-04-07)
- Hops: 4/5 (sem-01 misleading, actual is sem-05)
- Tool calls: 18
- Ontology: 0 triples relevant, store.ttl syntax error
- Chain breaks: Hop 2 (no machine link), Hop 3 (naming only), Hop 5 (wrong seminar)

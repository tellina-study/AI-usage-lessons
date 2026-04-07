---
title: "Test Scenario 3 E2E Baseline: Fresh Session, Query Only"
type: test-result
test_type: e2e
issue: "#29"
epic: "#17"
date: 2026-04-07
status: baseline
session_id: "f7446a14-74cf-4932-99a3-ebfae652fa0e"
---

# Test Scenario 3: E2E Baseline (Fresh Claude Code Session)

## Setup
- Fresh Claude Code session, no prior context
- User input: "The RPD requires competency in 'understanding AI classification approaches'. Trace this requirement to: which lecture covers it, which research notes support it, which papers are cited, and what seminar assesses it."
- No instructions given, no file paths hinted
- Model: claude-opus-4-6, CLI entrypoint

## What the System Did
1. Spawned 1 Explore subagent with chain-tracing prompt
2. Subagent performed 31 tool calls (grep, read across 10+ files)
3. Compiled structured report tracing all 5 hops
4. Main agent formatted final answer as a chain summary

## Metrics

| Metric | Value |
|--------|-------|
| Hops completed (/5) | 5/5 |
| Total tool calls (inner subagent) | 31 |
| Total tool calls (outer) | 1 (Agent spawn) |
| Wall-clock time | 79.4 seconds |
| Total tokens consumed | 123,149 |
| Chain fully traced | Yes |
| Correct seminar identified | Yes (Sem 5 midterm + Sem 17 final) |
| Ontology gap noted | Yes (no materialized triples for this chain) |
| User effort | 1 query, no follow-up needed |

## Chain Traced

| Hop | From -> To | Found | Key Detail |
|-----|-----------|-------|------------|
| 1 | RPD -> Requirement | Yes | PKS-3 at line 32: "classify and identify AI tasks" |
| 2 | Requirement -> Lecture | Yes | LO1 maps to 7 lectures (1-6, 8), primary = Lecture 1 |
| 3 | Lecture -> Research | Yes | classifications.md: 9 taxonomies across 184 lines |
| 4 | Research -> Papers | Yes | 15 PDFs in library/papers/lecture-1/, 25+ sources cited |
| 5 | Requirement -> Seminar | Yes | Sem 5 midterm + Sem 17 final exam, rubric 0-3 pts |

## Answer Quality
- All 5 hops traced correctly with file paths and line numbers
- Found PKS-3 competency code and full text
- Mapped to LO1 and identified ALL 7 lectures covering it (not just Lecture 1)
- Identified 9 taxonomies in research notes with academic sources
- Found 15 downloaded papers and 25+ cited sources
- Correctly identified Sem 5 AND Sem 17 as assessment points (not Sem 1)
- Noted ontology gap: schema supports this chain but no instance data loaded

## Bonus Findings
- Mapped LO1 across 7 lectures (my tool test only found Lecture 1)
- Found specific rubric criteria and scoring (0-3 pts)
- Identified the exact assessment criterion text: "Korreknost klassifikatsii AI-tekhnologii (LO1)"

## Methods Used by Subagent (inferred from 31 tool calls)
- Grep for competency codes, classification keywords
- Read of RPD, course-structure, lec-01-plan, classifications.md
- Read of paper manifest (index.yaml)
- Grep across seminar files
- Read of sem-05-midterm and sem-17-final
- Read of ontology store.ttl (noted empty)
- No SPARQL queries attempted
- No RAG queries attempted

## Comparison with Tool Test Baseline

| Metric | E2E (fresh session) | Tool Test (subagent baseline) |
|--------|---------------------|-------------------------------|
| Hops completed | 5/5 | 4/5 (sem partially wrong) |
| Tool calls | 31 + 1 = 32 | 18 (across methods) |
| Time | 79.4s | not timed |
| Tokens | 123,149 | not tracked |
| Correct seminar | Yes (Sem 5 + Sem 17) | Partial (found Sem 5, initially checked Sem 1) |
| Lectures mapped | 7 (all LO1 lectures) | 1 (Lecture 1 only) |
| Ontology used | No (noted gap) | Attempted, failed (0 triples) |
| RAG used | No | Attempted, partial (found fragments) |
| Chain breaks | 0 | 2 (hop 2 no machine link, hop 5 wrong sem first) |

## Key Observations
1. Fresh session traced ALL 5 hops successfully -- better than tool test baseline (4/5)
2. Found 7 lectures covering LO1, not just Lecture 1 -- broader and more accurate
3. Correctly identified Sem 5 + Sem 17 without first going to wrong Sem 1
4. Did NOT attempt ontology SPARQL or RAG -- compensated with thorough grep+read
5. 31 tool calls in 79s is expensive but produced complete, accurate chain
6. Noted the ontology gap explicitly -- aware of what should exist but doesn't
7. The system CAN trace multi-hop chains via brute-force, but it requires 31 calls and ~80s

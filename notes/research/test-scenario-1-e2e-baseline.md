---
title: "Test Scenario 1 E2E Baseline: Fresh Session, Query Only"
type: test-result
test_type: e2e
issue: "#27"
epic: "#17"
date: 2026-04-07
status: baseline
session_id: "70900ac0-4183-4860-94f6-df452e43f332"
---

# Test Scenario 1: E2E Baseline (Fresh Claude Code Session)

## Setup
- Fresh Claude Code session, no prior context
- User input: "What specific AI classification taxonomies does the course use, and where does each come from?"
- No instructions given, no file paths hinted
- Model: claude-opus-4-6, CLI entrypoint

## What the System Did
1. Spawned 1 Explore subagent with broad search prompt
2. Subagent performed 28 tool calls (grep, glob, read across repo)
3. Compiled results into structured report
4. Main agent formatted final answer

## Metrics

| Metric | Value |
|--------|-------|
| Taxonomies found | 13 (9 core academic + 4 course-specific) |
| Core taxonomies found (/9 ground truth) | 9/9 (100%) |
| Bonus taxonomies discovered | 4 (PARTS, CRI, R&N 2x2, Adoption Levels) |
| Total tool calls (inner subagent) | 28 |
| Total tool calls (outer) | 1 (Agent spawn) |
| Wall-clock time | 61.6 seconds |
| Total tokens consumed | 143,015 |
| Primary source file found | Yes (classifications.md) |
| Additional source files found | 5 (history-and-definitions.md, ai-cheatsheet.md, ai-v-tsikle-sozdaniya-po.md, ai-v-raznyh-industriyah.md, stats-finance-retail.md) |
| Precision | 100% (all 13 are real taxonomies) |
| Recall (vs 9 ground truth) | 100% |
| Recall (vs full repo content) | >100% (found extras not in ground truth) |
| Answer quality | Structured table with sources, file locations, and line numbers |
| User effort | 1 query, no follow-up needed |

## Answer Quality Assessment
- All 9 core taxonomies correctly identified with academic sources
- 4 additional course-specific frameworks discovered (bonus)
- Each taxonomy includes: name, description, primary source, file path with line numbers
- Summary table provided for quick reference
- Identified `classifications.md` as the authoritative single source

## Methods Used by Subagent (inferred from 28 tool calls)
- Grep across multiple directories with taxonomy/classification keywords
- Glob for file discovery
- Read of 5+ files to extract structured content
- No ontology queries attempted
- No RAG queries attempted

## Comparison with Tool Test Baseline

| Metric | E2E (fresh session) | Tool Test (subagent baseline) |
|--------|---------------------|-------------------------------|
| Taxonomies found | 13 | 9 |
| Tool calls | 28 + 1 = 29 | 10 (across 4 methods) |
| Time | 61.6s | not timed |
| Tokens | 143,015 | not tracked |
| Used ontology | No | Yes (returned 0) |
| Used RAG | No | Yes (returned 0 relevant) |
| Used grep | Yes (via Explore) | Yes (found ~3 partial) |
| Used direct read | Yes (multiple files) | Yes (1 file, 9/9) |
| Answer quality | Complete + extras | Per-method breakdown |

## Key Observations
1. Fresh session did NOT use ontology or RAG -- went straight to grep+read via Explore agent
2. Found MORE than ground truth (13 vs 9) by searching broadly across catalog/exports/ too
3. 28 inner tool calls is expensive but effective -- comprehensive search with no prior knowledge
4. The system compensates for missing index/wiki by brute-force file scanning
5. No per-method isolation -- cannot diagnose which retrieval tier would help most

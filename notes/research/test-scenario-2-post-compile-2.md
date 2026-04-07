---
title: "Test Scenario 2 Post-Compile-2: Cross-Document Thematic Search"
type: test-result
test_type: tool-test
issue: "#28"
epic: "#17"
date: 2026-04-07
status: post-compile-2
---

# Test Scenario 2: Post-Compile-2 Results

## Query
"Find everything in the repo about AI agents -- definitions, architectures, frameworks, examples, and which lectures/seminars cover them."

## Ground Truth (8 categories)
1. Definitions -- model/chat/agent/app hierarchy
2. Architectures -- ReAct, Toolformer, Anthropic spectrum, Ng patterns
3. Key papers -- Yao 2022, Schick 2023, Wang 2023, Masterman 2024 + 5 more
4. Industry frameworks -- Anthropic, Google, LangChain, Andrew Ng guides
5. Course coverage -- which lectures/seminars mention agents
6. Ontology -- any agent-related topic nodes
7. Capabilities -- what agents can/can't do
8. Levels of autonomy -- 5 levels from arXiv:2506.12469

## Results Table

| Method | Categories (/8) | Files Found | Tool Calls | Precision | Noise Ratio | Notes |
|--------|-----------------|-------------|------------|-----------|-------------|-------|
| Grep broad | 4/8 | 72 | 1 | 28% | 72% | Massive infra noise (agent in skills/blueprints) |
| Grep narrow | 3/8 | 18 | 1 | 44% | 56% | Better precision, misses most categories |
| Ontology | 0/8 | 0 | 2 | N/A | N/A | Store empty, no agent topic node |
| RAG EN | 3/8 | 10 | 1 | 70% | 30% | Found Masterman/Wang paper chunks |
| RAG RU | 1/8 | 10 | 1 | 30% | 70% | Agent content is mostly English |
| Manual | 8/8 | 8 | 8 | 100% | 0% | Requires knowing which files to read |
| Wiki Index | 6/8 | 2 | 2 | 100% | 0% | Best automated: 6 categories, 2 calls, zero noise |

## Aggregate Metrics

| Metric | Value |
|--------|-------|
| Total tool calls | 16 |
| Best automated method | Wiki Index (6/8, 2 calls, 0% noise) |
| Best overall | Manual (8/8, 8 calls) |

## Comparison to Baseline

| Method | Baseline | Post-Compile-2 | Delta |
|--------|----------|-----------------|-------|
| Grep broad | 5/8, 70% noise | 4/8, 72% noise | -1 (stricter scoring) |
| Grep narrow | 3/8 | 3/8 | 0 |
| Ontology | 0/8 | 0/8 | 0 (empty store) |
| RAG EN | 1/8 | 3/8 | +2 (PDF papers indexed) |
| RAG RU | 0/8 | 1/8 | +1 (marginal) |
| Manual | 8/8 | 8/8 | 0 |
| Wiki Index | N/A | 6/8 | New method, best cost-efficiency |

## Key Findings

1. Wiki Index is the clear winner for automated retrieval: 6/8 in 2 tool calls with zero noise.
2. RAG EN outperformed baseline (+2) thanks to ingested PDF papers (Masterman, Wang).
3. Ontology remains a gap -- no agent topic node, 0 triples loaded.
4. Grep noise is structural -- repo has many infra files matching "agent" (skills, blueprints, reflections).
5. Russian-language retrieval is weak -- agent content is primarily English.
6. Wiki Index missing: ontology status (cat 6) and capabilities (cat 7) -- these need wiki page enrichment.

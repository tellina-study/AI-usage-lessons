---
title: "Test Scenario 2 Post-Phase4: Cross-Document Thematic Search"
type: test-result
test_type: tool-test
issue: "#28"
epic: "#17"
date: 2026-04-07
status: post-phase4
---

# Test Scenario 2: Post-Phase4 Results

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

| Method | Categories (/8) | Files Found | Tool Calls | Noise Ratio | Notes |
|--------|-----------------|-------------|------------|-------------|-------|
| Grep broad | 5/8 | 72 | 1 | 79% | +1 from prior: wiki pages now surface as content |
| Grep narrow | 3/8 | 12 | 1 | 50% | Stable |
| Ontology | 0/8 | 0 | 2 | N/A | Empty store, no topic entities |
| RAG EN | 4/8 | 10 | 1 | 10% | +1 from prior: PDF paper chunks richer |
| RAG RU | 2/8 | 10 | 1 | 70% | +1: course coverage hits |
| Manual | 8/8 | 6 | 6 | 0% | Gold standard |
| Wiki Index | 7/8 | 4 | 3 | 0% | +1 from prior: Related Topics enables cross-navigation |

## Phase 4 Cross-Link Verification

- `[[lec-01]]` resolved to `[Lecture 1](../../lectures/lec-01.md)`: CONFIRMED
- Related Topics section on ai-agents page links to ai-fundamentals, ai-in-software, prompt-engineering: CONFIRMED
- Backlinks section links back from lec-01, ai-fundamentals, index: CONFIRMED
- Bidirectional lec-01 <-> ai-agents navigation: CONFIRMED
- Following Related Topics -> ai-fundamentals reveals Capabilities category (human-vs-ai): CONFIRMED

## Key Phase 4 Improvement

Wiki Index 6/8 -> 7/8. The "Related Topics" section enables discovery of the Capabilities category (7) via cross-link to ai-fundamentals -> human-vs-ai sub-topic. Only Ontology topic nodes (category 6) remain undiscoverable.

## Comparison Across All Runs

| Method | Baseline | Post-Compile-2 | Post-Phase4 | Trend |
|--------|----------|-----------------|-------------|-------|
| Grep broad | 5/8 | 4/8 | 5/8 | Stable (scoring variation) |
| Grep narrow | 3/8 | 3/8 | 3/8 | Stable |
| Ontology | 0/8 | 0/8 | 0/8 | Blocked (empty store) |
| RAG EN | 1/8 | 3/8 | 4/8 | Improving (+3 total) |
| RAG RU | 0/8 | 1/8 | 2/8 | Improving (+2 total) |
| Manual | 8/8 | 8/8 | 8/8 | Gold standard |
| Wiki Index | N/A | 6/8 | 7/8 | Improving (cross-links add +1) |

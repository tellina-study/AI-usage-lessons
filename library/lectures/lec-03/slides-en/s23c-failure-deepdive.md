---
id: s23c
type: case_study
section: "Section 4. Agents"
duration_min: 4
assertion: "Deep-dive of the classes: PocketOS 9 s, runaway $48k/$1.3M, slopsquatting 19.7%, cascade 61%"
learning_goal: "Deep-dive of 4 failure classes with a comparison baseline and the correct alternative to each"
learning_outcomes: [LO7]
chapter_ref: "§4.10 [for-slide-s23c]"
verify_day_of: true
---

# Visible content

## Title bar
"Deep-dive: 4 classes with a comparison baseline"

## Body
[4 failure cards in Ocean rounded boxes]

**1. Destruction + over-privilege (PocketOS, Apr 2026)**
The agent found a token with **unlimited privileges** in an unrelated file, deleted the production volume + all volume-level backups in **9 seconds**; the nearest backup — **3 months old**
*Lesson:* the system prompt is not a security control; you need a hard boundary + least-privilege

**2. Runaway cost**
**$48k in 14h** (a research agent with no success criterion), **$1.3M in 30 days** (~100 Codex instances, 603 billion tokens)
*Baseline:* an ordinary session — cents to dollars → this is **3–5 orders of magnitude** higher
*Lesson:* you need a termination criterion + hard cap + kill-switch

**3. Slopsquatting**
**19.7%** of package references across 576,000 code samples — hallucinations (≈1 in 5 imports)
*Lesson:* do not trust dependency names from an agent without verification against a registry

**4. Multi-agent cascade**
**61%** of cascade failures (73 incidents) — rooted in the **upstream** layer (retrieval/planning), not where the failure became visible
*Lesson:* you need validation between steps, fewer hops, traceability

[Gold callout, bottom]
**The common root of all four: the agent was applied without an external boundary. The boundary is outside the agent; the prompt does not replace it.**

## Speaker notes

Let us work through four classes in more detail, each with a concrete comparison baseline. The first — destruction under excessive privileges. A coding agent in a test environment found a token with unlimited privileges and deleted the production volume with all its backups in nine seconds; the nearest backup was three months old. Lesson: the system prompt is not a security control; only an architectural boundary and least-privilege reliably stop an agent.

The second — uncontrolled cost. A research agent with no success criterion spent $48k in 14 hours, 100 instances burned $1.3M in a month. Baseline: an ordinary session costs cents to dollars, this is 3–5 orders of magnitude higher. Lesson: a termination criterion, a hard budget cap, an emergency stop.

The third — slopsquatting: agents invent package names, attackers register them with malicious payloads. Almost one in five generated imports pointed to a nonexistent package. Lesson: do not install dependency names without verification against a registry.

The fourth — multi-agent cascade: one agent's error passes down the chain as a fact, the following agents rely on it. In real incidents the root is often not where the failure is visible but at an upstream step — in retrieval or planning. The general conclusion: the agent was applied without an external boundary. Such a boundary sits outside the agent and is not replaced by a prompt.

---
id: s22d
type: case_study
section: "Section 4. Agents"
assertion: "Memory is not an unconditional improvement: the Letta system loses even to a flat file, and the best tested memory carries a measurable 17% irreproducible tail of losses — «works well» ≠ «works always»"
learning_goal: "The memory failure: Letta Tier D + Anthropic Memory Tool 17% tail; the lesson «observed quality ≠ a guarantee»"
learning_outcomes: [LO7]
chapter_ref: "§4.6 [for-slide-s22d]"
verify_day_of: true
---

# Visible content

## Title bar
«The memory failure: to remember ≠ to remember correctly»

## Body
[Case 1 — Letta, Tier D]
Loses **both** to the bare model **and** to a flat file (persistbench_v1: 1.000 / 0.833 / **0.750**)
Mechanisms: capitulation under pressure · verbosity drowns the fact · the fact is not committed

[Case 2 — Anthropic Memory Tool, Tier B]
The best tested system — but **17% of tasks** with information loss + **irreproducibility** (one conversation twice → a different result)

[Gold callout, bottom]
**«Works well» and «works always» are different statements.** The same lesson as the RAG failure at scale and catastrophic forgetting.

[Footer, italic]
*By data from the agent-harness-registry (live-eval). Freshness quarterly; Letta v0.6.7 vs the current v0.16.8 (~18 months).*

## Speaker notes

Having memory intuitively seems like a pure improvement — an agent that remembers should be more useful than an agent that starts from scratch every time. Data from the agent-harness-registry, an independent registry[1] that tests systems on real tasks, shows that this is not always so, and sometimes dramatically not so. On the slide the systems are marked with a Tier letter — this is the registry's rating category from A (the best results) to D (the worst) by the sum of live-eval benchmarks; the closer to A, the more stably the system showed itself on the full set of tests. The first case is the Letta system, Tier D. By the registry's data it loses both to the bare model with no memory at all and to a trivial flat file on all fully tested benchmarks: on persistbench the bare model gave 1.000, the flat file 0.833, and Letta only 0.750, while being an order of magnitude slower. Three failure mechanisms were identified: capitulation under pressure, when on a repeated question the system changes an already given correct answer to an uncertain one; verbosity, when a long embellished answer hides the short correct fact; and a fact noticed but not committed to memory. A freshness caveat is mandatory: a version about eighteen months old was tested due to an installer limitation, not due to cutting a corner, so this is an assessment of a specific outdated version.

The second case is more important, because it is the best tested system. The Anthropic Memory Tool is strong overall, but even it recorded information loss in four tasks out of twenty-four, that is, in 17 percent: an explicit refusal to record a fact deemed ephemeral; a refusal as "out of scope"; and quiet summarization, when specific facts are imperceptibly absorbed into general categories. The most alarming detail is irreproducibility: the same conversation, submitted twice, produced different behavior. This is not a bug but documented design: the model is asked to apply judgment on what is worth recording, and this judgment produces real, sometimes contradictory failures. The conclusion is one: even for the best memory system there is a measurable tail of losses. "Works well" and "works always" are different statements, and this is the same lesson as the RAG failure at scale and catastrophic forgetting.

Sources:
[1] agent-harness-registry (live-eval) — Letta Tier D / Memory Tool 17% tail — source not confirmed by a canonical URL as of 2026-08-30; the numbers are volatile (1.0/0.833/0.750; 17%). [VFY: not confirmed by a canonical URL, present as data from an independent live-eval registry, not as a primary source]

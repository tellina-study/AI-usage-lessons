---
id: n51
type: measured_outcome_table
duration_min: 1.5
assertion: "The reranker raises recall@1 to 0.96 on both bases — and it doesn't do that for free: a separate model call is more expensive than the entire Case 1 pipeline"
learning_goal: "The fourth action as the next step after the hybrid (sequential iteration, design canon §4), not a parallel alternative from the very start. A specific example of a fix — not an abstract percentage improvement."
visual:
  pattern: measured_outcome_table
  primary: >
    A transition tile ("the hybrid merged two signals with no model call
    at all — what if the final order is handed off to the model for
    review?"), a 2×3 table (base · recall@1 · $/question), a specific
    example of a fix.
  backup: >
    Numbers — stend/raw/case3-rerank-results.json. gpt-4o-mini on top of
    the top-10 candidates of RRF or of pure vector — the same
    credential/webhook already used in Case 1 (zero new infra). Example
    c3q10 — verbatim from the raw JSON.
---

# The next step after the hybrid: review by the model

## Assertion

The hybrid merged two signals with no model call at all. The reranker is the next logical step: what if the final order is handed off to the model for review?

## Visual

> **Both bases are computed by `text-embedding-3-small` (search by meaning) — the reranker on top adds a separate `gpt-4o-mini` call.**

| Base + reranker | recall@1 | $/question (search) |
|---|---|---|
| Hybrid + LLM reranker | **0.96** (was 0.84) | $0.000329 |
| Vector + LLM reranker | **0.96** (was 0.86) | $0.000327 |

> **Example of a fix.** The question "What were the most popular works created in 1984–1986" (gold document — a member of a confusable cluster): pure vector found it in 10th place, the hybrid in 2nd place; the reranker raised both variants to 1st place.

## Speaker notes

The hybrid we just broke down ranks results decently well, but it does so with no model call at all — purely by the statistics of matching two signals. The next natural question, which comes up precisely because the hybrid already exists and has already been measured: what if the final order is handed off for review to a model that reads both the question itself and the ten candidates already found, in full?

`gpt-4o-mini` receives the top-10 candidates of the hybrid or the top-10 candidates of pure vector (both bases are computed by the same embedding model, `text-embedding-3-small` — the difference between the bases is only whether its signal is merged with search by words) and re-sorts them by relevance to the question — the very same credential and webhook that already worked in Case 1 of this session, with not a single new infrastructure node. OpenRouter has no separate endpoint for reranking — it's an ordinary chat model acting as a reranker, there's no specialized API for that here.

The result is noticeable on both bases: recall@1 rises to 0.96 — it was 0.84 for the hybrid, 0.86 for pure vector. A gain of ten to twelve percentage points means specific documents that previously weren't found in first place and now are: you can't call that an abstract percentage.

Here's a concrete example — let's see what this looks like in text: a number alone isn't enough here. For the question about popular works from the mid-eighties, whose correct document is a member of one of the confusable clusters that deliberately mix up similar entities: pure vector found this document only in tenth place in the results, the hybrid in second place. After the rerank, both variants ended up in first place. The model, having read the top-10 candidates in full, was able to tell the needed document apart from similar neighbors better than a statistical comparison of vectors or words could.

But this gain has a price, and it isn't symbolic — let's break it down at the solution and nuances beat.

The very existence of this step is a direct consequence of the form most modern models are built in. OpenRouter, like most providers, has no separate specialized API for "reviewing the order of documents" — this isn't a standard operation the way embedding or text generation is. But any chat model knows how to read a long list and return a structured answer about it, and the reranker uses exactly that general ability — a specially trained ranking model isn't needed here. This makes adoption cheaper: there's no need to look for a specialized service — but it also explains why the price of the step equals the price of an ordinary model call — there's no hint of a cheap specialized API here.

---
id: n56
type: content
duration_min: 1.0
assertion: "The requester sees hybrid search as a more stable answer regardless of how the question is phrased; Olga sees a number — the share of questions that found the correct document among the top results"
learning_goal: "Case 3's result and generalization: what the requester sees vs. what Olga sees, the transferable principle (semantic search doesn't replace keyword search) + the role of the optional review step."
visual:
  pattern: content
  primary: >
    Two tiles side by side: "to the requester," "to Olga" — then a
    formula tile for the transferable principle.
  backup: >
    Text — SETKA-KEYSOV.md Case 3, "Result and generalization," verbatim.
---

# What Olga sees, and what the requester sees

## Assertion

Where the cost of a ranking error is high, the optional review step by the model raises the share of exact first places even higher — but not for free.

## Visual

To the requester, hybrid search looks like a more stable answer regardless of exactly how the question is phrased — with an exact term or in their own retelling. To Olga, a number is visible: the share of questions for which the process found the correct document among the top results is higher for the hybrid than for either of the two methods on its own.

> **The principle transfers to any orchestrator: semantic search doesn't replace keyword search, and neither does the reverse — each has its own class of questions where it's stronger, and merging both results doesn't require knowing ahead of time which class of question will come next.**

## Speaker notes

The requester doesn't see the search mechanics itself — only the quality of the answer is visible, and it feels more even: a question asked with an exact term from the regulations, and a question retold in one's own words, both find the needed document with comparable reliability using hybrid search — no one class of questions is served noticeably worse than the other.

Olga sees a number, and this isn't a one-off case — it's exactly the table we broke down a few beats earlier: the share of questions for which the process found the correct document among the top results is higher for the merge of two signals than for either of them on its own, measured by recall@3 and average rank.

And the principle worth carrying forward past this session applies far beyond n8n. Semantic search doesn't replace keyword search, and keyword search doesn't replace semantic search — each has its own class of questions where it's stronger. Merging both results is good precisely because it doesn't require knowing ahead of time which class of question will come next: it works on the distribution of questions as a whole — you can't get by on one guessed type alone.

Where the cost of a ranking error is high — the requester must not get an answer from the second- or third-most-relevant candidate if it differs substantially from the first — an optional step is added to this principle: reviewing the final order with the model raises the share of exact first places even higher, but not for free — it costs a separate model call and a noticeable time delay, and makes sense exactly where that price is justified by the cost of the error.

It's worth returning, at the end of this case, to the question it started with: it seems that semantic search must surely be better than keyword search, because it understands meaning. Four measured actions gave a more nuanced answer than a plain "yes" or "no" to that question — and that nuanced answer is more useful than a crude one, because it can be applied to the next task without repeating the same measurement.

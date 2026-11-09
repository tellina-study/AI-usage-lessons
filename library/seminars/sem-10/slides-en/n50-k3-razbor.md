---
id: n50
type: answer_breakdown_table
duration_min: 1.0
assertion: "No single one of the three signals wins on every metric at once — each has its own zone where it's strong"
learning_goal: "Breakdown of the three base methods (with no model at the ranking step), the 4-column form (A5). The reranker comes next, as a separate beat (sequential iteration, design canon §4)."
visual:
  pattern: answer_breakdown_table
  primary: >
    Table: action · how it works · advantage · drawbacks. Three rows.
  backup: >
    Text — SETKA-KEYSOV.md Case 3, "Breakdown of options," the three base
    methods, fit into the 4-column form.
---

# What the measurement confirmed for each of the three signals

## Assertion

Words have their own zone of confidence — exact matches, names, numbers; meaning has its own: retelling in one's own words.

## Visual

| Action | How it works | Advantage | Drawbacks |
|---|---|---|---|
| Search by words | Matches tokens of the query and the document, no model | Cheap and fast — the search itself costs nothing | recall@1 = 0.74 — the worst of the three; if it's not in first place, it sits on average at the 9.9th position out of 500 — the lexical gap and the confusable clusters throw off the exact match |
| Search by meaning (vector) | The query's embedding is compared against the embeddings of the base's chunks | recall@1 = 0.86 — the best result among methods with no model at the ranking step; average rank 2.0 | recall@3 (0.92) is a touch below the hybrid's; weaker where exact matching of a name or number matters |
| Search both, merge (hybrid, RRF) | Two independent rankings merge into one via the Reciprocal Rank Fusion rule | Best recall@3 (0.94) and average rank (1.6) among methods with no model at the ranking step | recall@1 = 0.84 — lower than pure vector's (0.86): a weak word signal sometimes pulls the merged vote away from where vector was right straight away |

## Speaker notes

We've already broken down how each signal works — here's what came out as a number. Three signals, and none of them wins on every metric at once — we just saw the same finding by question group; here it reads by action, before we get to the fourth.

Search by words is the cheapest and the weakest on this particular, deliberately toughened corpus. It has its own zone of strength — exact matches of numbers and names — but on a pool where questions are specially selected for lexical gap and confusable clusters, that strength shows up rarely.

Search by meaning is best at whether the correct document lands in first place. But its recall@3 is a touch lower than the merge's — meaning that in the remaining fourteen percent of cases, where the document isn't first, it's sometimes not second or third either.

Merging the two signals gives the best average result on two metrics out of three — recall@3 and average rank — but not on recall@1. This isn't a flaw in the method — it's a direct consequence of how the merge works: the weak voice of search by words sometimes pulls the joint result toward where pure vector wouldn't have gone on its own.

Which of the three actions closes Olga's need depends on which metric matters more for the specific task — but before moving to the solution, it's worth looking at the fourth action, which comes after the signals are already merged.

This table answers two different questions differently. The first question is whether the correct document was found at all among the search results; recall@3 answers that, and the hybrid leads there. The second question is whether it turns out to be exactly first; second or third place doesn't count here. recall@1 answers that, and pure vector leads there. For Olga's system, where the model most often uses only the first search result when answering, the difference between these two questions isn't abstract at all — it directly decides which metric matters more when choosing a solution.

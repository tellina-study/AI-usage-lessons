---
id: n58
type: criteria_checklist_and_boundary
duration_min: 0.75
assertion: "The reranker is a second boundary of the same kind: it can both raise the correct document from 10th place to 1st, and knock an already-correct result from 1st place to 3rd"
learning_goal: "Case 3's reranker boundary, continuing n57 (cost, the gain's inconsistency, powerlessness without the document in the top-10). The third axis line closes here. Part 2 of 2. Letter-suffix inserted before deck-wide renumbering (tools/seminar-production/README.md §1, issue #311)."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    A tile on the reranker with both sides, a tile closing the third axis
    line.
  backup: >
    Numbers — stend/raw/case3-rerank-results.json (questions c3q7, c3q42).
---

# The reranker's boundary: the gain isn't on every question

## Assertion

The reranker adds 10–12 p.p. to recall@1 on average — and on an individual question it can either raise or drop the correct document.

## Visual

> **The reranker is a second boundary of the same kind, with two sides at once.** It adds 10–12 percentage points to recall@1 — but it costs a separate model call ($0.00033, more expensive than the entire Case 1 pipeline) and latency (+1.6–1.9s). It can raise the gold document from 10th place to 1st — that's what happened with the question about popular works from the mid-1980s. And it can just as well knock an already-correct result from 1st place to 3rd — that's what happened with the question "An example of water barriers?", where pure vector had already found the correct document first. If the document isn't even among the top-10 candidates before the rerank — as in the question about barter exchange in trade, where vector found the gold document only in 26th place — the reranker won't raise it at all: it only rearranges what it was shown, it doesn't touch the whole pool of documents again.

> **The third axis line of the session is closed:** semantic search finds the document in first place more often than keyword search on a tough corpus — but not guaranteed and not universally; it depends on the corpus and the questions, and merging signals doesn't win on every metric at once.

## Speaker notes

The reranker is a boundary of the same kind as the hybrid's, except it has two sides at once, and both are confirmed by numbers — a bare assumption won't do here. It adds ten to twelve percentage points to recall@1 on both bases — and that's a real gain. But it costs a separate model call that's more expensive than the entire pipeline of this session's first case, and adds almost two seconds of latency on top of what's already accumulated.

And the gain isn't guaranteed on every individual question: the very same reranker that raised the needed document from tenth place to first on one question, on another — about water barriers — knocked an already-correct result from first place to third. And if the document isn't even among the ten candidates that made it to the reranker — as in the question about barter trade, where vector found the correct document only in 26th place — the reranker physically cannot raise it: it reviews the order only of what it was shown, it doesn't touch the whole pool of documents again.

And here the third axis line of the session closes. It looked reliable that semantic search finds the same thing keyword search does anyway, only smarter. It turned out more complicated: on a deliberately toughened corpus, semantic search really does win on recall@1, but this isn't universal superiority — the result depends on which corpus and which questions it was given, and merging the signals, which was supposed to take the best of both, doesn't win on every metric at once. Three breakdowns in a row in this case — keyword, vector, hybrid with a reranker — confirm the same thing from different angles: "smarter" doesn't mean "more universal."

Next — the session's last case, and the subject of the search is different in it: images instead of text.

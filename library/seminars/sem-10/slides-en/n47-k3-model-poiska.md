---
id: n47
type: content
duration_min: 0.75
assertion: "The third group is neutral: neither a gap nor an exact match. Semantic search is computed by the same embedding model that already worked in Case 1"
learning_goal: "Case 3's measurement-exposition beat, continuing n46: the third question group (neutral), which model computes semantic search, and the shared metric across all variants. Still no results on the frame. Part 2 of 2. Letter-suffix inserted before deck-wide renumbering (tools/seminar-production/README.md §1, issue #311)."
visual:
  pattern: content
  primary: >
    A table of the third question group (neutral, 18) with an example,
    expected answer, and the reason for the group. A tile for the
    semantic-search model and the shared metric across all three
    variants. No results on the frame.
  backup: >
    Neutral — c3q42 (the same question as in the nuances breakdown n57
    further on). Semantic-search model — `text-embedding-3-small` via
    OpenRouter (stend/measure/case3_measure.py), the same one that already
    worked in Case 1 of this session (C5). Comparison setup — cosine
    similarity against all embeddings of the corpus at once, with no
    cutoff threshold: all 500 documents are ranked, none are filtered out.
---

# Test structure: the third group and the search model

## Assertion

The neutral group is neither a gap nor an exact match; the model computing semantic search is the same one that already computed Case 1.

## Visual

| Group | How many | Example question | Expected answer | Why this group |
|---|---|---|---|---|
| Neutral | 18 | "What was barter exchange in trade?" | The only available form of trade | The class is picked out by the absence of a shared number with the text — the degree of lexical similarity doesn't matter here. The group is neutral: neither a gap nor an exact match, although it also contains questions lexically close to the text |

> **Semantic search is computed by `text-embedding-3-small` via OpenRouter** — the same embedding model that already worked in Case 1 of this session, cosine similarity against all 500 documents, with no cutoff threshold. The metric is the same for every variant — recall@1 and recall@3 (whether the correct document was found first, or among the first three) and the average rank of the correct document, against the SberQuAD gold labels. **There are no results on this frame — next, we look at what came out.**

## Speaker notes

The third group — eighteen neutral questions, where there's no number shared with the text that would settle the question in favor of an exact match, like the question about barter exchange in trade: the class is picked out by the absence of a numeric match — the degree of lexical similarity doesn't matter here. Inside it there are also questions lexically close to the text, no less than the questions in the exact-match group. This group exists exactly so that the two previous classes don't look like the only ones there are: in practice, a significant share of a real requester's questions doesn't fall cleanly into either "exact match" or "lexical gap," and an honest measurement has to reflect that — rigging the corpus for a convenient picture isn't allowed.

In this measurement, semantic search is computed by the model `text-embedding-3-small` via OpenRouter — the very same embedding model that already worked in the first case of today's session. Nothing new had to be set up: the same call, the same model, a different corpus and different questions.

The comparison is cosine similarity between the question's embedding and all five hundred embeddings of the corpus, with no cutoff threshold whatsoever: all documents are ranked, no one is filtered out ahead of time. This matters for the honesty of the measurement: the model has to find the correct document among all five hundred — with no preliminary narrowing down to a hundred candidates.

The metric is the same for all three search variants: recall@1 and recall@3 — whether the correct document was found first, or at least among the first three — and the average rank of the correct document across the full ranking of five hundred documents, against the SberQuAD gold labels. A shared metric across all variants is the condition for an honest comparison: if every variant had its own metric, comparing the numbers against each other wouldn't be fair.

There isn't a single result on this frame yet — the test structure has been named in full, the summary itself comes next.

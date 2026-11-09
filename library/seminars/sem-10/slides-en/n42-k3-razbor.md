---
id: n42
type: answer_breakdown_table
duration_min: 1.0
assertion: "Three actions search for candidates using different signals, and they can be combined with each other"
learning_goal: "Qualitative breakdown of the first three actions of Case 3 RIGHT AFTER the question (owner's requirement: the breakdown follows the question directly — n41 → n42 → then the test structure and result). The breakdown explains the mechanism and the qualitative pros/cons without a single result number, following the pattern of n62-k4-razbor.md; C2 canon isn't violated — there isn't a single result on the frame before the test-structure beat. Action names are raised to industry terms (owner's edit, issue #311), the mechanism is named explicitly (BM25, cosine similarity of embeddings, Reciprocal Rank Fusion) — the previous version called RRF impersonally ('by the rank-merging rule'), even though n50/n54 later in this same deck already name it explicitly: the mismatch between slides of the same case was itself the defect, not just the missing term as such. A breakdown of RRF arithmetic by example comes on the next frame, n43: here only the formula's name and a verbal principle — a detailed calculation doesn't fit into the table (15pt half-size type leaves no room for it). Part 1 of 2 (n44 — the fourth action, the reranker): split because 15pt half-size type leaves no room for four table rows on one slide (issue #311)."
visual:
  pattern: answer_breakdown_table
  primary: >
    Table: action · how it works · advantage · drawbacks. Three rows —
    three candidate-search signals. No numbers on the frame.
  backup: >
    Text — a number-stripped version of n50-k3-razbor.md (three signals
    without a model doing the ranking), with RRF's name restored (n50
    names it, the previous "stripped" version of this slide did not) and
    with the names BM25/cosine similarity, which weren't in n50 at all
    (there the action was called by the plain "search by words"/"search
    by meaning").
---

# What each of the four actions does

## Assertion

The first three actions search for candidates using different signals, and they can be combined with each other. The fourth is not an alternative to them, but a step on top of an already-assembled list.

## Visual

| Action | How it works | Advantage | Drawbacks |
|---|---|---|---|
| Full-text search (keyword, BM25) | Matches tokens of the query and the document, no model — the weighting function is called BM25 | Cheap and fast — the search itself costs nothing | Finds word matches — it doesn't recognize meaning: a lexical gap between the question and the document, as well as documents similar in topic but different in substance, throw off the exact match |
| Vector search (by embeddings) | The query's embedding is compared against the embeddings of the base's chunks by cosine similarity — the nearest one wins | Finds by meaning: isn't limited to word overlap — rephrasing the question in different words doesn't get in the way | Weaker where exact matching of a specific name or number matters — closeness of embeddings doesn't guarantee an exact match of a detail |
| Hybrid search (RRF) | Two lists — by words and by embedding — merge into one via the Reciprocal Rank Fusion (RRF) formula | Combines the strength of both signals where they diverge — takes whatever either of the two methods found | A weak word signal sometimes pulls the merged result toward where a pure vector would not have gone on its own |

## Speaker notes

Four actions, and the first three of them compete for the same role — finding candidates; the fourth doesn't compete — it builds on top of whatever the others found, and is broken down separately on the next frame.

Full-text search is classic keyword search: the tokens of the question and the tokens of the document are compared, not a single call to a model. The weighting function that industrial search systems use to count such a match is called BM25 — it weighs shared words by their rarity in the corpus, but the substance for our task is the same: this is the cheapest signal, and the crudest — it finds word matches and doesn't recognize meaning, and where the question is retold in different words or documents are similar in topic but differ in substance, an exact word match is easily thrown off.

Vector search is built differently: the query and the document are turned into an embedding — a numeric vector of meaning — and the document whose embedding is closest to the question's embedding by cosine similarity wins. This removes the dependence on exact phrasing — rephrasing the question in different words doesn't get in the way of such a search. The price is paid where exact matching of a specific name or number matters: a shared topic doesn't count here, closeness of embeddings alone guarantees nothing.

Hybrid search is the third action, which uses both signals at once and doesn't choose between them: two independent lists merge into one via the Reciprocal Rank Fusion formula, RRF for short. The principle in words, without the formula itself: a document gets a score in each list that's larger the higher it stands in that list; the document's scores from both lists are added together, and the top of the merged list goes to the document with the largest sum: being first place in a single list alone doesn't decide the outcome. A numeric example on three documents comes on the next frame. This lets you take whatever either of the two methods found, but merging has its own price — a weak signal from full-text search sometimes pulls the joint result toward where pure vector search wouldn't have gone on its own.

Important: there's no need to choose once and for all among these three actions — they can be combined. Hybrid is literally built out of the first two, and the measurement further on checks the actual question: on which corpus and with which questions does each of them win.

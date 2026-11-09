---
id: n41
type: question_with_option_cards
duration_min: 1.0
assertion: "Four actions, from the cheapest by signal to the most expensive by model-based re-ranking"
learning_goal: "Case 3's question: four action cards, no verdicts (A6). The fourth card is a design choice — 'hand off to the model for re-ranking' — not a fact about the reranker's properties. Cards are named with industry terms (owner's edit, issue #311: 'professional audience, use industry terminology'), the human-readable sense in parentheses, the same pairing already carried through n42/n44."
visual:
  pattern: question_with_option_cards
  primary: >
    Question in a gold frame, four equal-width cards, no arguments and
    no verdicts.
  backup: >
    Cards — SETKA-KEYSOV.md Case 3, "Question to the room," the same four
    actions in substance; names raised to industry terms (full-text /
    vector / hybrid search, reranker) by the issue #311 edit — the
    "Question to the room" text in SETKA-KEYSOV.md is a working draft, not
    mirrored word-for-word on the frame in any deck of this course.
---

# What to search the needed chunk with, among hundreds

## Assertion

Four ways to find the right chunk: full-text, vector, hybrid search, and a reranker — from a plain word comparison to a model-based re-ranking of order.

## Visual

> **What should search the needed chunk among hundreds?**

`full-text search (by words)` · `vector search (by meaning)` · `hybrid search (words + vector)` · `reranker (model re-ranking)`

## Speaker notes

Four actions, and each has its own name in the industry. First — full-text search: classic search by word match, not a single call to a model, the tokens of the question and the tokens of the document are compared. Second — vector search: the question and the documents are turned into embeddings — numeric representations of meaning — and the document whose embedding is closest to the question's embedding wins. Third — hybrid search: search both ways at once and merge the two independent result lists into one. Fourth — a reranker: after the result is already merged, hand the final order off for review by a separate model call that reads both the question and the candidates already found.

The fourth action is a possible next step after the first three; it is not an alternative to them: it assumes some list of candidates already exists, and asks whether it's worth reviewing once more. But as a design choice it's no different from the other three — it, too, is an action you can choose or not choose.

Fifteen seconds to decide. A breakdown of how each action works comes on the next screen; testing on real questions with a known correct document ahead of time comes further on, on the test structure and the result itself.

The first three actions can be combined with each other in various combinations; the fourth can only be built on top of a result already obtained. This is a property of the task itself; it has nothing to do with how the question happens to be phrased: reviewing the order with a model only makes sense once there's already something to review — a list of candidates assembled by one or more search methods. So vote not only for the "best" way to search, but also for what the search chain in Olga's system should even start with.

Weigh one more thing before voting. The training center gets questions of very different kinds: some clients write using the exact term from the regulations, others retell their situation in their own words — not knowing the right terminology at all. If all the questions were of one type, the choice between search methods would be simple — whichever is strongest for that specific type would win. But the training center's stream of questions is mixed, and that's exactly what makes choosing a search method a practical task — theory alone isn't enough here.

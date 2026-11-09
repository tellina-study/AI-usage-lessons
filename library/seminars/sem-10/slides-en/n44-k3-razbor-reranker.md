---
id: n44
type: answer_breakdown_table
duration_min: 0.75
assertion: "The fourth action doesn't search for candidates — it reviews an already-assembled list with a separate model call"
learning_goal: "Qualitative breakdown of Case 3's fourth action, continuing n42 (owner's requirement: the breakdown follows the question directly). n41's question names four cards (three search signals + the reranker), so the breakdown takes up the reranker too, not just the three base signals. The action in the table is named with the industry term 'reranker,' not the plain 'hand off to the model for review' (owner's edit, issue #311). The reranker's internal diagram (bi-encoder vs. cross-encoder) and the explanation of why reading jointly is more accurate come on a separate frame, n45, further on: there's physically no room for the diagram on this frame (the table already takes up most of the height at 15pt half-size type), and the form-of-presentation rule §5.13 requires that a detailed breakdown not be squeezed to save space. Part 2 of 3 (n42 → n44 → n45). Letter-suffix inserted before deck-wide renumbering (tools/seminar-production/README.md §1, issue #311)."
visual:
  pattern: answer_breakdown_table
  primary: >
    Table: action · how it works · advantage · drawbacks. One row —
    "reranker." No numbers on the frame.
  backup: >
    Text — a number-stripped version of n51-k3-reranker.md: recall@1=0.96
    and the $ price are removed, leaving only the mechanism "the model
    reviews the final order" and the qualitative price "a separate model
    call, more expensive than steps without a model." The action's name is
    raised to the industry term ("reranker") by the issue #311 edit —
    matching the n41 card and this same slide's own title/assertion, where
    the term was already in place.
---

# What the fourth action does: a model-based review

## Assertion

A reranker is not an alternative to search, but a separate step on top of an already-assembled list of candidates.

## Visual

| Action | How it works | Advantage | Drawbacks |
|---|---|---|---|
| Reranker (model-based review) | Once a list of candidates has already been assembled by one or more search methods, a separate model call reads both the question and all the candidates in full, and reviews their order | The model sees the candidates in full and can tell the right document apart from similar neighbors where statistical comparison of words or meaning gets confused | A separate model call is more expensive than any of the steps without a model; it only makes sense once a list of candidates already exists — so it's a step on top of an already-assembled result, not something you can call a standalone way of searching |

## Speaker notes

The fourth action, the reranker, stands apart from the first three: it assumes some list of candidates already exists — assembled by one method or by several at once — and asks whether that list is worth reviewing once more.

A separate model call reads the question and all the candidates in full and can tell the right document apart from similar neighbors where a purely statistical comparison of words or vectors gets confused. But this is a review — you can't call it a standalone search, and it isn't free: a separate model call is more expensive than any of the three steps without a model, and only makes sense once a list that can be reviewed already exists.

Mechanically, the reranker works like this: it takes as input an already-selected top slice of candidates from the whole corpus — say, ten or twenty documents — and for each of them the model judges how well it actually answers the question, after which the list is rebuilt from scratch based on that judgment. This is a fundamentally different task from ranking by words or by meaning: there, the document and the query are encoded separately; here, they're encoded together, as one single input. The reranker doesn't take part in operations across millions of candidates: it passes judgment on a small, already-narrowed set. That volume lets it read the text in full — there's no need to compare precomputed numeric representations here. How this "together" is built, and why it's more accurate, is a separate diagram on the next frame.

An important caveat: the reranker doesn't compete directly with any of the first three actions — it always comes as a second step, after one of them or after their merge. In essence this is a question of adding a step: whether it's worth building it on top of a search method already chosen for finding candidates. What decides it here is the price of the extra model call weighed against what it delivers.

Which of these actions — or which combination of them — closes the training center's stream of questions isn't answered by this beat. Next comes the reranker's internal design, then the test structure, which answers the choice question with a number.

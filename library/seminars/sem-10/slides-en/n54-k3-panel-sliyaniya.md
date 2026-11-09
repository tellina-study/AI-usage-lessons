---
id: n54
type: mechanism_node_graph
duration_min: 0.75
assertion: "The merge is thirteen lines of code: Reciprocal Rank Fusion with k=60, with not a single model call"
learning_goal: "Layer 2 of Case 3, beat 2 of 3: a real configuration panel of the merge node, the EXPANDED view of the code editor (not collapsed — a Seminar 9 lesson: the collapsed view cuts off text)."
visual:
  pattern: mechanism_node_graph
  figure: case3-n8n-rrf-panel-real.png
  primary: >
    A real screenshot of the expanded code editor of the "RRF fusion
    (hybrid)" node: the function `rrf(rankA, rankB, k=60)` computes
    Reciprocal Rank Fusion of two lists and returns the top-10 candidates
    with their text.
  backup: >
    Source of the frame: `stend/n8n-screenshots-raw/case3-rrf-panel.png`
    (a `Code` node, mode "Run Once for All Items," language JavaScript),
    captured by `stend/n8n_shots.py` in the EXPANDED view of the editor.
    Crop — `rendered/compose_case3_n8n_shots.py`: the Parameters/Settings
    tabs and the Mode/Language fields at the top are removed (the
    interface's housekeeping part, not the node's code), as is the
    toolkit hint at the bottom; all 13 lines of code are visible in full,
    none are cut off.

    WHAT IS LITERALLY VISIBLE ON THE FRAME: the function `rrf(rankA,
    rankB, k=60)` (lines 2–7) — the classic Reciprocal Rank Fusion
    formula: each document of each list is scored `1/(k+i+1)`, where `i`
    is the document's position in that list, and the scores from both
    lists are summed. Line 8 calls it on `d.keyword_rank` and
    `d.vector_rank` — the two lists the previous canvas nodes already
    computed (n53). Lines 9–12 take the top-10 documents of the merged
    ranking and pull their text from the corpus. Line 13 returns the
    result — the merged rank, the top-10 ids, and their text — to the
    next node.

    THE MODEL ISN'T NAMED, AND THAT'S HONEST (a C5 consequence): there
    isn't one in this node. RRF is a classic, non-AI formula; this is
    plainly visible from the code — not a single HTTP call, not a single
    call to OpenRouter. The only two numbers this code decides on its
    own, with no model, are `k=60` (the formula's smoothing constant) and
    `TOP_N=10` (how many candidates to pass on to the reranker).
---

# The real panel: the merge node's code

## Assertion

The merge is thirteen lines of code with not a single model call: the Reciprocal Rank Fusion formula, k=60.

## Visual

> Line 8 is the whole idea of the node: `rrf(d.keyword_rank, d.vector_rank, 60)`. Two already-ready lists come together into one by the rule "the higher a document stands in both lists, the higher it stands in the merged one."

## Speaker notes

This is the real configuration panel of the merge node, in the expanded view of the editor — the whole code is visible in full, not a single line cut off in the middle.

The heart of the node is the function `rrf`, lines two through seven. It takes two lists of documents, each already sorted by its own criterion, and assigns each document a score: one, divided by the sum of the constant `k` (here, sixty) and the document's position in the list. If a document appears in both lists — and that's the usual case, both search methods look at the same corpus — its scores from both lists are added together. The higher a document stands in both rankings, the greater its total score, and the higher it ends up in the merged list.

Line eight is the whole idea of the node in a single line: `rrf(d.keyword_rank, d.vector_rank, 60)`. `d.keyword_rank` and `d.vector_rank` are the two lists the previous canvas nodes already computed — that very same search by words and search by meaning we just saw. Sixty is the constant `k` from the formula: a number chosen so that a document's position near the start of the list means noticeably more than near the end, but without sharp jumps.

Lines nine through twelve take the first ten documents of the merged ranking — exactly as many as the optional rerank node will see next — and attach to each id its full text from the corpus, which the form has kept with it since the very start of the canvas. The last line packages the result — the merged rank itself, the list of ten ids, and their text — and passes it on.

There isn't a single HTTP call in this code, not a single call to OpenRouter. Reciprocal Rank Fusion is a classic formula, there's no AI in it at all, and that's exactly what makes it free: it costs nothing and adds no latency beyond the execution of the code itself. The only two numbers the code itself decides, with not a single model call, are `k=60`, the formula's own smoothing constant, and `TOP_N=10` — how many candidates from the merged list to pass on to that very same optional rerank node. How that node is built — the next panel.

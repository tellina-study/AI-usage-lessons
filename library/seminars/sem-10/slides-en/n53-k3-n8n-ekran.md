---
id: n53
type: mechanism_node_graph
duration_min: 0.75
assertion: "The canvas is a single sequential chain of eight nodes, not two parallel branches: ranking by words and embedding the query are computed one after another, with the merge and reranker coming only after both"
learning_goal: "Layer 2 of Case 3, beat 1 of 3: a real screenshot of the rig's live canvas (not a programmatic diagram — the live UI was captured by `stend/n8n_shots.py`, the workaround for [#233-8] lifted on 2026-10-20, the same approach as Cases 1/2/4 of this session). The panels of the two nodes come as the next two beats (n54, n55)."
visual:
  pattern: mechanism_node_graph
  figure: case3-n8n-canvas-real.png
  primary: >
    A real screenshot of the live n8n canvas on the rig: Question + corpus
    with embeddings → Keyword overlap → Embed query (OpenRouter) → Cosine
    ranking (vector) → RRF fusion (hybrid) → LLM reranker (gpt-4o-mini) →
    Parse reranker response + outcome → Result screen.
  backup: >
    THE PROGRAMMATIC DIAGRAM IS REPLACED WITH A REAL SCREENSHOT by this
    edit (canon `proektirovanie-keysa-i-voprosa.md` §2, §8.4 of the
    README). The previous diagram `case3-n8n-hybrid-rerank-scheme.png`
    (`make_figures_sem10.py::case3_scheme`) was legitimate at the time it
    was made — the live canvas was unreachable (`notes/mcp-limitations.md`
    [#233-8]) — but the limitation was lifted on 2026-10-20, and
    `stend/README.md` records: "real screenshots have been captured, the
    previous output was an error." The old generator file is NOT deleted
    (it remains a record of the previous solution's design), but the
    slides no longer reference it.

    Source of the frame: `stend/n8n-screenshots-raw/case3-canvas.png`,
    captured by `stend/n8n_shots.py` on the live
    `n8n.lessons.tellian.io`, an execution on this demo scenario (workflow
    `s10-case3-search`, the id isn't carried onto the slide — canon §3 of
    the design doc). Crop — `rendered/compose_case3_n8n_shots.py`
    (Pillow, the same effect as `convert -crop`; ImageMagick is
    unavailable in this working environment) — only a dangling "+"
    connector to the right of Result screen is removed, the canvas itself
    isn't reassembled or redrawn by a single pixel.

    WHAT IS LITERALLY VISIBLE ON THE CANVAS, AND THIS MATTERS: the chain
    is LINEAR, not two parallel branches merging into one node (which is
    how the previous programmatic diagram drew it — that's exactly where
    it diverged from how the scenario is really assembled). "Keyword
    overlap" computes the ranking by words as the FIRST node, using the
    corpus's already-finished embeddings carried in the input form;
    "Embed query (OpenRouter)" computes the embedding ONLY of the
    question (the documents' embeddings are already computed ahead of
    time, as in Case 1); "Cosine ranking (vector)" compares that
    embedding against all documents; and only after BOTH lists
    (`keyword_rank`, `vector_rank`) are ready does the node "RRF fusion
    (hybrid)" merge them. The two signals are logically independent and
    could in principle be computed in two parallel branches — the real
    scenario chose a linear chain of a single execution; this is an
    implementation decision, not a requirement of the architecture
    (layer 1, n52).

    THE MODEL IS NAMED EXPLICITLY (C5): `text-embedding-3-small` (query
    embedding, node "Embed query") and `gpt-4o-mini` (reranker, node
    "LLM reranker") — both visible right in the node labels on the
    canvas, unlike Case 1, where the model's name isn't shown in the node
    label.

    A DEMO RUN, NOT A REPEAT OF THE MAIN MEASUREMENT: shows the canvas
    mechanics on a small subset of the corpus (8 documents, including the
    confusable pair on the "Zvyozdny" entity), it does not repeat the
    recall@1/@3 numbers of the main measurement on 500 documents/50
    questions (n46/n48) — `stend/README.md` § "Supplementary pass
    2026-11-01," an execution on this scenario.
---

# The real canvas: from question to reranker

## Assertion

The canvas is a single linear chain of eight nodes: ranking by words and embedding the query are computed one after another, not in parallel.

## Visual

> Keyword overlap computes the ranking by words as the first node. Next come the query's embedding and cosine ranking by meaning. Only once both lists are ready does RRF fusion merge them — and only then, as an optional step, does the LLM reranker enter the picture.

## Speaker notes

On screen is a real screenshot of the rig's live canvas: a frame captured live from n8n — there's no diagram and no drawing here, the same approach we've already seen on the canvases of this session's earlier cases.

Read left to right, there's a single path, and it's linear, even though intuition suggests otherwise. The node "Keyword overlap" computes the token overlap between the question and each document and returns the list `keyword_rank` — with not a single model call, using the already-ready corpus that the form keeps with it along with precomputed embeddings. Next comes "Embed query (OpenRouter)," and here only the question's own embedding is computed: the embeddings of all five hundred documents are already ready ahead of time, same as in Case 1's storage. The next node, "Cosine ranking (vector)," compares this question embedding against each document's embedding and returns the second list, `vector_rank`. And only once both lists — by words and by meaning — are already computed does the node "RRF fusion (hybrid)" merge them into one by the Reciprocal Rank Fusion rule.

The two signals are independent of each other and could in principle be computed in two parallel branches of the canvas, converging at a single merge node — that's exactly how the previous programmatic diagram of this frame was drawn. The real canvas is built differently: this is a decision of the implementation itself; the architecture we broke down a layer earlier doesn't require it. For the result it makes no difference — `keyword_rank` and `vector_rank` are still computed independently of each other and merged only once both are ready.

Next comes the optional node "LLM reranker (gpt-4o-mini)": just as ordinary an HTTP Request node as the embedding node a bit earlier on this same canvas, only with a different request body and a different model. It receives the top-10 candidates after the merge and re-sorts them by relevance to the question. The node "Parse reranker response + outcome" parses what the model returned, and the screen `Result screen` closes out the form.

Both models that actually work here are named right in the node label on the canvas — unlike Case 1, where this had to be named separately in the slide's text: `text-embedding-3-small` computes the query's embedding, `gpt-4o-mini` performs the rerank.

This specific run is a demonstration, on a small subset of the corpus that specially includes a confusable pair of documents splitting a rare entity. It can't be called a repeat of the measurement on five hundred documents and fifty questions, which we've already seen as a number. How the merge node and the reranker node are built inside — real configuration panels — next, over the following two beats.

---
id: n45
type: content
duration_min: 0.75
assertion: "The source of the reranker's accuracy is reading the query and the document jointly, as one input, instead of comparing two finished numbers computed separately"
learning_goal: "An explicit request from the owner (issue #311): 'add a diagram and a description of the reranker's workings — how it works and why it's more accurate.' The diagram — a bi-encoder (ordinary vector search: the query and the document are encoded SEPARATELY, the comparison is by distance between finished vectors) against a cross-encoder (the reranker: the query and EACH candidate are fed into the model TOGETHER, as a single input, with no intermediate compression into a vector). Letter-suffix inserted before deck-wide renumbering (tools/seminar-production/README.md §1, issue #311), the third frame of the n42/n44/n45 cluster: n42 named the actions and the RRF formula, n44 gave a qualitative breakdown of the reranker as an action, this frame is the only one with a full diagram of its internal design and the reason for its accuracy, for which n44 had physically no room (the table already took up most of the height at 15pt half-size type)."
visual:
  pattern: mechanism_node_graph
  figure: case3-biencoder-vs-crossencoder-en.png
  primary: >
    A two-column diagram: on the left, a bi-encoder (vector search,
    separate encoding, vectors compared as the last step); on the right, a
    cross-encoder/reranker (a single input one step earlier, the model
    reads both texts in full). Below — a "why it's more accurate" tile.
  backup: >
    Diagram — `rendered/make_figures_sem10.py::case3_biencoder_vs_crossencoder`,
    a programmatic figure (not an n8n screenshot) — on n8n's canvas the
    reranker is visible as an HTTP Request node with a request body (n55
    further on), not the model's internal design; these are different
    levels of breakdown, both legitimate and not duplicating each other.
    The diagram's asymmetry (the right column merges into a single input
    one level earlier than the left) is itself the diagram's content, not
    a stylistic choice: it's exactly the moment of merging that decides
    whether the model sees the interaction between the query's and the
    document's words, or only a finished number.
---

# How the reranker works inside: bi-encoder vs. cross-encoder

## Assertion

The source of the reranker's accuracy is reading the query and the document jointly, as one input, instead of comparing two finished numbers computed separately.

## Visual

> A **bi-encoder** encodes the query and the document separately and compares already-finished vectors. A **cross-encoder (reranker)** feeds them into the model together, as a single text, and reads the direct interaction of the words — exactly what separate encoding compresses into a number before the question even existed.

## Speaker notes

On the previous frame we named the fact that the reranker reads the question and the candidates in full. Here's what that means inside the model — and this is the source of its accuracy.

Ordinary vector search, which we've used all through this session, is built as two separate lines. The document's vector is computed by an encoder model ahead of time, for the whole base at once, before any question has even appeared — we already saw this in the first case of this session. The query's vector is computed at the moment of the question, by the same encoder. Then the two finished numeric representations are compared — by cosine similarity, which we already named at the test-structure beat. By the moment of comparison, nothing is left of the original texts except two numbers: the encoder compressed the meaning of each text ahead of time and separately, without yet knowing what exactly that vector would be compared against.

The reranker is built in a fundamentally different way — this design has its own name, a cross-encoder, as opposed to the bi-encoder that ordinary search uses to compute vectors. The query and each candidate are fed into the model together, as a single input: one text, in which the question and the candidate sit side by side. The model reads them together at once, in a single pass, and decides for itself how well the second text answers the first.

And here's the difference that explains the accuracy. While the query and the document are encoded separately, they physically cannot influence each other inside the model: the document's vector is the same regardless of whatever question comes to it. When both texts are read together, the model can match a specific word in the question to a specific word in the document — notice that they're about the same person, number, or event, even if the phrasing differs — exactly the matching that separate encoding has already erased, compressed into a single number long before the question was even known.

This is also what makes the cross-encoder more expensive: instead of one comparison of numbers, there's a full model pass over the text of the question and the candidate together, and this happens separately for each of the top-10 candidates: there is no precomputed, reusable vector here at all. The price of this accuracy comes in a separate beat further on, on the test structure and the result.

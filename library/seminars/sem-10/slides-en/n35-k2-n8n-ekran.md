---
id: n35
type: mechanism_node_graph
duration_min: 0.75
assertion: "On the real canvas there are seven nodes in a row, and not one of them calls a model — all four chunking versions and their comparison are built with plain code"
learning_goal: "Layer 2 of Case 2, beat 1 (design canon §2): a real snapshot of the live rig, not a drawn diagram. The canvas is a demo comparison of the four versions on one document, with no embedding and no model (C5 by contraposition: explicitly name the absence of a model)."
visual:
  pattern: mechanism_node_graph
  figure: case2-n8n-canvas-real.png
  primary: >
    A real screenshot of the live n8n canvas: a "Whole document" form →
    code "Fixed-size chunking" → code "Sentence-boundary chunking" →
    code "Word-boundary chunking" → code "Fixed-size chunking with
    overlap" → code "Comparison: did the answer land whole in one
    chunk" → result screen. Seven nodes in one row, not one of them a
    model call.
  backup: >
    The screenshot is real: stend/n8n-screenshots-raw/case2-canvas.png,
    taken by stend/n8n_shots.py on n8n.lessons.tellian.io after the
    follow-up run of 2026-11-02, copied WITHOUT cropping to
    rendered/figures/case2-n8n-canvas-real.png via
    rendered/compose_case2_real_screens.py (no cropping needed — the
    canvas was captured already zoomed "to fit", nothing extra at the
    edges). The screenshot has already been reassembled for 7 nodes; the
    file name hasn't changed. There is no longer a stylized diagram
    standing in for the screenshot: the earlier drawn scheme
    rendered/figures/case2-n8n-splitter-scheme.png (generator
    make_figures_sem10.py::case2_scheme()) is left on disk as a record of
    the earlier (mistaken) solution's design — the slide no longer
    references it (canon §8.4).

    THIS IS A DEMO COMPARISON, NOT A PRODUCTION PIPELINE: the scenario
    `s10-case2-chunking` (id `oLiJHPEy6uII7W5J`) runs ALL FOUR chunking
    versions on one document and compares the result right on screen —
    this isn't the same canvas on which Case 1 assembles the embedding
    and the store write (there, the cutting step would sit BEFORE
    embedding in a single chain). Layer 1 (n34) states the architectural
    boundary regardless of which specific scenario it's configured in;
    here is the real screen showing how all four chunking nodes are
    built.

    THE MODEL ISN'T NAMED BECAUSE IT ISN'T HERE (C5 by contraposition):
    `stend/sborka.py::case2_chunking_workflow()` and
    `stend/measure/case2_chunking.py` — not one of the seven nodes calls
    either an LLM or an embedding; the whole canvas is plain code (a Code
    node, JavaScript). The contrast with the embedding step from Case 1
    (`text-embedding-3-small`, already named on n27/n34) is stated
    explicitly in the slide's body, not left for the reader to infer.
---

# The real canvas: comparing four versions on one document

## Assertion

Seven nodes in a row, not one of them calls a model — all four chunking versions are built with plain code.

## Visual

> Whole document → Fixed-size chunking → Sentence-boundary chunking → Word-boundary chunking → Fixed-size chunking with overlap → Comparison: did the answer land whole in one chunk → result screen.

This canvas has no embedding step and no store write — it's a separate demo scenario that runs all four chunking versions on one document and compares them right on screen. The chunk-embedding step (the `text-embedding-3-small` model, Case 1) sits in a different scenario, after the chunk is already made, and doesn't change with any setting depending on which chunking version produced it.

## Speaker notes

On screen — a real canvas from the live rig; there's no drawn diagram here. Seven nodes in one row: a form that takes in the whole document, then four code nodes — one cuts by fixed size, another by sentence boundaries, a third by word boundaries, a fourth by fixed size with overlap — then a comparison node that checks whether the gold answer landed whole in one chunk for any of the versions, and finally, the result screen.

An important detail of how this specific canvas is built: it isn't a continuation of the knowledge-base storage chain from the previous case, it's a separate demonstration scenario. There's no embedding step here and no store write — all four chunking versions run on one document, one after another, and the comparison node immediately shows which version kept the answer intact. In the real working pipeline, the chunking node sits once, before the embedding step, and the chain from there on runs as in Case 1 — into the point where a chunk turns into a number.

And the main thing worth seeing right on this screen: not one of the seven nodes calls a model. All four chunking nodes are plain JavaScript code that computes the chunk boundary from the character count, from punctuation marks, or from a word boundary, with not a single call to an LLM. The comparison node is also code, checking the positions of numbers against each other. The architectural decision discussed in the previous beat shows up here literally: the entire work of this step is a classical algorithm, and the model only enters the chain later, once a finished chunk goes on to be embedded.

The canvas is built as a comparison — it isn't a working chain: the screen makes it possible to run all the options on the same document and see the difference immediately, without having to line up several different runs in your head — a production process isn't assembled here. The comparison node exists only for this purpose: there's no such node in the working chain and none is needed — it simply lays the results of all the versions side by side and states plainly whether the answer survived for each of them.

How the chunking nodes themselves are built inside — what code and what parameter sets the versions apart — next screen, with the expanded panels of version 1 and version 2.

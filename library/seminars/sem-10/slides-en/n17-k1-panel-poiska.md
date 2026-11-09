---
id: n17
type: mechanism_node_graph
duration_min: 0.75
assertion: "Inside the 'Simple Vector Store' node there's no separate database — it's a loop over every document and a cosine comparison with the question, right in the node's body"
learning_goal: "Layer 2 of Case 1, beat 2 of 3: a real configuration panel for the search node, in the EXPANDED code-editor view (not collapsed — Seminar 9's own lesson: a collapsed view truncates the text)."
visual:
  pattern: mechanism_node_graph
  figure: case1-n8n-vector-panel-real.png
  primary: >
    A real screenshot of the "Simple Vector Store" node's expanded code
    editor: a JavaScript function `cos(a, b)` computes cosine similarity,
    a loop over `payload.corpus` keeps the best document found.
  backup: >
    Frame source: `stend/n8n-screenshots-raw/case1-vector-store-panel.png`
    (the `Code` node, "Run Once for All Items" mode, JavaScript language),
    captured by `stend/n8n_shots.py` in the EXPANDED editor view (the
    expand button — the same lesson from Seminar 9, that a collapsed view
    truncates the text). Crop — `rendered/compose_case1_n8n_shots.py`:
    the Parameters/Settings tabs and the Mode/Language fields on top were
    removed (service parts of the interface, not the node's code), as was
    the toolkit hint at the bottom; the code itself wasn't redrawn or
    changed by even one character.

    WHAT'S LITERALLY VISIBLE ON THE FRAME: six lines of code. Line 1 reads
    the incoming `payload` (the question plus the document corpus with
    their embeddings). Line 2 pulls out the question's own embedding,
    `qvec`. Line 3 is the cosine similarity function itself, written by
    hand (`d/(Math.sqrt(na)*Math.sqrt(nb))`), with no call to an external
    library. Lines 4-6 are the loop over every document in the corpus,
    comparing each one with `qvec`, keeping the best one.

    WHAT ISN'T ON THE FRAME AND THEREFORE ISN'T CLAIMED IN PROSE: a
    separate vector-database service. "Simple Vector Store" is an n8n
    node's name, not the name of an external product; the store lives
    inside the payload itself, and the search is a plain in-memory scan.
    This isn't a limitation of this particular run — the stock n8n node is
    built this way for small corpora; a real external vector database
    would be needed not here, but once the base grows far beyond what
    fits in a single call's memory.
---

# The real panel: the search node's code

## Assertion

Search is six lines of code: a cosine comparison of the question against every document in turn, with no external database.

## Visual

> The "Simple Vector Store" node is a loop over every document in the corpus and a hand-written cosine similarity function: no call to a separate service.

## Speaker notes

This is a real configuration panel, captured in the editor's expanded view: the whole code is visible in full, with no truncated middle of a line.

Six lines. The first pulls out what came in at the input: the question and the entire document corpus, each of which already has an embedding computed in advance. The second line grabs the question's own embedding — the previous node, "Embed query," already computed it. The third line is the cosine similarity function itself, and it's written by hand, right here: the dot product of the vectors, divided by the product of their lengths. No external library is connected for this — ten lines of math are simpler than a dependency.

Next, lines four through six, is a plain scan: a loop over every document in the corpus, computing its similarity with the question for each one, and if it's higher than everything seen so far — the document is remembered as the best candidate. When the loop ends, exactly this document is returned in the response, together with its text, its id, and its similarity score.

There's no separate database service here, no index built in advance that would live outside this node. "Simple Vector Store" is an n8n node's name; it has nothing to do with any external product that happens to sound similar. The store is simply an array of documents inside the input data, and the search is a plain in-memory scan, done right at execution time. On a corpus of a few hundred documents, the scan runs instantly; at a corpus orders of magnitude larger, that's exactly the point where a real external vector database would be needed — but for the sizes we measured here, six lines of code are enough.

What this node takes in and what it passes on — the question together with the found chunk goes to the next node, which forms the final answer. How that one is built — the next panel.

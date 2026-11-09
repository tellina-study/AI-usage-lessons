---
id: n36
type: mechanism_node_graph
duration_min: 1.0
assertion: "On the left — a loop over the character count; on the right — splitting by sentence boundaries and accumulating to the target size: one type of node, different code inside"
learning_goal: "Layer 2 of Case 2, beat 2 (design canon §2): real expanded panels of two Code nodes with concrete configuration details (Mode/Language/JS code, not just the node's name). JS is a direct port of the Python from case2_chunking.py, not a separate implementation."
visual:
  pattern: mechanism_node_graph
  figure: case2-n8n-code-panels-real.png
  primary: >
    Two expanded Code-node panels side by side: on the left, "Fixed-size
    chunking" (chunkFixed — a loop over size with a step of
    size-overlap); on the right, "Sentence-boundary chunking"
    (chunkStructural — splitting by a sentence-boundary regular
    expression, accumulating to target characters).
  backup: >
    The screenshots are real: stend/n8n-screenshots-raw/case2-fixed-chunk-panel.png
    and case2-structural-chunk-panel.png, taken by stend/n8n_shots.py, the
    expanded view of the code editor (the expand button — a C9 lesson:
    the collapsed view cuts off the text). Composed side by side via
    rendered/compose_case2_real_screens.py — WITHOUT ImageMagick (in this
    working environment `convert`/`montage` aren't installed, Pillow was
    used instead: the same result, crop plus stitch without redrawing the
    source screenshot's pixels) — rendered/figures/case2-n8n-code-panels-real.png.
    Each panel is cropped at the n8n interface's bottom orange hint
    ("Type $ for a list…") — this is a UI hint, not part of the node's
    content.

    The JS is a DIRECT PORT of the Python from stend/measure/case2_chunking.py
    (`chunk_fixed`/`chunk_structural`/`answer_intact`), confirmed by the
    docstring of stend/sborka.py::case2_chunking_workflow(): "a direct
    port of …, not an independent implementation — must not diverge from
    what was actually measured." The node on the left reads
    `payload.chunk_size` (default 180) — the same parameter that was
    varied across five values in the summary (n28).
---

# The real screen: how the two chunking nodes are built

## Assertion

On the left — a loop over the character count; on the right — splitting by sentence boundaries and accumulating to the target size. The same type of node, different code inside.

## Visual

Fixed-size chunking (left) reads `payload.chunk_size` (default 180), then in a `while (i < text.length)` loop cuts the string into consecutive chunks of this many characters, with no regard for content — after each chunk it advances by `size` characters and repeats.

Sentence-boundary chunking (right) first splits the text into sentences using a regular expression (a boundary after a period, exclamation mark, or question mark), then accumulates sentences into one chunk until the total length exceeds `target` characters — the chunk only breaks off at a sentence boundary, never inside one.

Both nodes are plain code (a Code node, JavaScript language, "Run Once for All Items" mode), with no call to a model at all.

## Speaker notes

The previous screen showed that both chunking nodes are simply code. Here's exactly what that code does, expanded, line by line, the same way an engineer sees it when opening the node on the real rig.

The left panel is the "Fixed-size chunking" node. The first line of code reads the `chunk_size` parameter from the input, and if it wasn't passed, substitutes the default — one hundred eighty, the same headline value the main breakdown was built around. Next comes one function, `chunkFixed`: a loop that walks through the text left to right and, at every step, cuts off a chunk of exactly the set length, without reading what's written in that chunk at all. Once it reaches the end of the text, the loop stops. This is exactly the code that gives nine broken answers out of seventy-two at the headline size.

The right panel is the "Sentence-boundary chunking" node. Here, the first line of code splits the entire text into sentences via a regular expression that looks for a period, exclamation mark, or question mark followed by a space. Next, the code walks through these sentences one by one and adds them to the current chunk, until the total length exceeds the target value — and only then closes the chunk and starts a new one, closing it strictly at the boundary between two sentences, and never wherever it happens to fall. This is exactly the code that gives one broken answer out of seventy-two at the same headline size.

Both nodes are the same type: ordinary program code inside n8n, "run once for all input data" execution mode, JavaScript language. The difference is only in the function's internal logic: twelve lines that cut by number, against almost twenty lines that cut by the meaning of sentences. This isn't a new node and not a new interface setting — it's a different program, written in place of the previous one, and it's exactly this difference in code that accounts for the difference in the number of broken answers — the interface has nothing to do with it.

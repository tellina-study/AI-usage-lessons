---
id: n69
type: mechanism_node_graph
duration_min: 0.75
assertion: "The screen is really assembled and really executed — the architectural thesis is honestly not confirmed by this run"
learning_goal: "Case 4's layer 2, beat 1 of 2: a real screenshot of the rig's live canvas (not a program-drawn diagram — a live UI capture by stend/n8n_shots.py, the workaround [#233-8] lifted 2026-10-20) — a real attempt to realize the architecture that didn't succeed. No less real a layer 2 than the working examples of Cases 1-3. The node settings panel — next beat (n70). The inset holds the role of fact (quote_role_force)."
visual:
  pattern: mechanism_node_graph
  figure: case4-n8n-canvas-real.png
  primary: >
    A real screenshot of the rig's live n8n canvas: Form scan (data URL,
    formTrigger) → Embed image (amazon/titan-embed-image-v1, HTTP Request
    to OpenRouter /embeddings) → Result screen. Inset — the finding about
    the identical vector.
  backup: >
    THE PROGRAM-DRAWN DIAGRAM REPLACED WITH A REAL SCREENSHOT by this edit
    (canon proektirovanie-keysa-i-voprosa.md §2, README §8.4: the finding
    "layer unreachable" is lifted not by a stand-in genre, but by a new
    capture — the same edit already applied to Cases 1 and 2 of this
    session). The earlier diagram `case4-n8n-mm-scheme.png`
    (`make_figures_sem10.py::case4_scheme`) was legitimate at the time it
    was made — the live canvas was unreachable
    (`notes/mcp-limitations.md` [#233-8]) — but that limitation was lifted
    on 2026-10-20, and `stend/README.md` records: "live screenshots taken,
    the earlier conclusion was a mistake." The earlier generator file is
    NOT deleted (it stays on record as the device of the earlier
    solution), the slide just no longer refers to it.

    Source of the frame: `stend/n8n-screenshots-raw/case4-canvas.png`,
    taken by `stend/n8n_shots.py` on the live `n8n.lessons.tellian.io`.
    Crop — `rendered/compose_case4_real_screens.py` (Pillow, the same
    effect as `convert -crop`; ImageMagick isn't available in this
    working environment) — only the dangling "+" connector to the right
    of the `Result screen` node was removed, the canvas itself isn't
    reassembled or redrawn by a single pixel.

    THE MODEL IS NAMED BY ID (S5): `amazon/titan-embed-image-v1`, a call
    with no explicit settings beyond the input itself — a data URL (base64
    JPEG). On the canvas, the model name is partially visible in the
    node's label ("Embed image (amazon/titan-embed-…"), cut off by the UI
    to the width of the card — the full name is given by the slide's text,
    not by the frame.

    AN HONEST CAVEAT, REQUIRED BY THIS CROP: the run standing on this
    screen was really executed and really returned a vector without an
    error — but the fact that this vector doesn't depend on the picture at
    the real scan's resolution is a property of THE RUN ITSELF (revealed
    by the controlled check on n66), not a property of this screenshot.
    The screenshot shows that the node is configured and executes; it
    can't (and shouldn't) show by itself what happens inside the model at
    the other end of the request.
---

# The real canvas: an attempt that didn't succeed

## Assertion

The same HTTP Request node that already built the text embedding in the first case — only with a picture in the request body instead of text.

## Visual

> The canvas on the rig is really assembled and really executed — but layer 1's architectural thesis isn't confirmed by this run: there's no working demonstration of "search picture by picture" on this rig, only an honestly shown and reproduced failure.

## Speaker notes

On screen — a real screenshot of the rig's live canvas, the very same interface the process was assembled in during the previous three cases of this session: a live-captured n8n frame — there's no diagram and no drawing here. Three nodes on the main path read left to right: the form takes in a form scan as a `data URL`, the `Embed image` node sends it to OpenRouter's `/embeddings` endpoint — the label under the node on the canvas directly shows the address — and the result screen closes the chain.

The node's setup doesn't differ technically in any way from what was already seen in the first case of this session for text embedding: the same node type — an ordinary HTTP Request with a preset credential type — the same way of connecting, the same place for the model and the input data in the request body. There's exactly one difference: the request body now holds a picture as a `data URL` — there's no text in it anymore.

And here's what's important to say directly about this specific case's second layer. For Cases 1-3, the second layer is the pair "principle → a working example": an architecture and, right there, a real run that confirms it. Here the pair is different: "principle → a real attempt to realize it, which didn't succeed." The canvas on the rig is really assembled, the request is really executed — this isn't a theoretical illustration and not a drawn diagram. But this run's result doesn't confirm the architectural thesis: the session has no working demonstration that pictures are really compared in their own space on this rig, only an honestly shown and reproduced failure.

This is no less a real second layer than in the previous three cases — it's just that its result is negative. That's exactly why the screen isn't hidden or swapped for a stylized illustration of success: what's shown is exactly what came out, with real node names on a real screenshot — there are no drawn cards here.

This canvas is worth comparing to Case 1's canvas, which we saw at the start of the session. There, the same node type to the same `/embeddings` endpoint confidently found the right document and gave the right answer. Here — the same node type, the same way of connecting, the same request setup, and a fundamentally different result. This shows, more clearly than any explanation could, that a solution's reliability isn't determined by which node it's assembled with on the canvas, but by what the model specifically does at the other end of the request — and that has to be checked separately every time; inferring it from the fact that a similar node already worked somewhere else won't do here. How the node itself is configured inside — the real settings panel — next frame.

---
id: n69
type: mechanism_node_graph
duration_min: 1.5
assertion: "The real measurement canvas: three nodes, and not one of them cross-checks what's read against the request's text"
learning_goal: "Layer 2 of Case 6 (§2 of the case-design canon): a real shot of the live rig, not a stylized scheme. The frame honestly shows exactly what was built for the measurement — reading only, with no cross-check."
visual:
  pattern: mechanism_node_graph
  figure: k6-holst-chtenie.png
  primary: >
    A real screenshot of the n8n canvas on the live rig, three nodes in a
    row: receiving the photo → building the model request → calling the
    model with the image. Node captions are as on the canvas, in Latin
    script in quotes/backticks; the rest of the frame's text is in English.
  backup: >
    The screenshot is real: scenario "S9 · K6 measurement — reading a
    receipt photo" on the live `n8n.lessons.tellian.io`, captured with
    `stend/n8n_shots.py` (BRIEF §3, table "Rig Scenarios by Case," row 6).
    There is no stylized card here in place of a screenshot (BRIEF §5,
    [[no-mock-fallbacks]]). Kept under the same filename as the RU figure
    — the node captions are already the tool's own English UI labels, and
    the canvas carries no Russian text to re-render for this EN track.

    Three nodes on the canvas, real names, taken from the build's own
    source (`stend/zamery-k5-k6/sborka.py`, function `k6_read`): `Receipt
    photo` (receives the photo through the form), `Build vision request`
    (assembles the request body — the model, the photo in the encoding the
    provider needs), `Read receipt (OpenRouter vision)` (the direct call
    to the model with the image and the question "read the amount and
    date").

    CHECKED AGAINST THE FINISHED FIGURE (`rendered/figures/k6-holst-
    chtenie.png`, opened this session): three node cards, the captions
    match the names above verbatim, no webhook path/id/credentials are on
    the frame, the arrows are simple with no forks. The crop requirement
    below is confirmed, not hypothetical.

    AN HONEST LIMITATION, named directly in the visible body, not hidden:
    this canvas is a measurement rig for one question ("how does the
    model itself read the photo, with nothing around it"), not the case's
    assembled solution. There is no classic-recognition node and no
    two-number comparison node on it — their device is broken down by the
    Layer 1 scheme (n68) as something worth building further, not
    something that literally sits on this canvas.

    CROP REQUIREMENT (met on the finished figure): no webhook path,
    scenario id, or any provider credentials should be visible on the
    frame — only the three node cards and the arrows connecting them, with
    no open settings panel of the HTTP node where the key is wired in. The
    panel with the model request's prompt text, if it ever needs showing,
    gets its own frame with its own screenshot, not this one.

    What is NOT visible on the frame and is therefore not asserted in the
    prose next to it: the prompt text itself and the `temperature` value.
    The canvas shows node cards, not their open settings.
---

# The real measurement canvas: three nodes

## Assertion

Receiving the photo, building the request, calling the model with the image — and not one node further. This canvas measures one thing: how the model reads the photo on its own.

## Visual

> Three nodes in a row: `Receipt photo` (the form takes in the receipt photo) → `Build vision request` (assembles the request — which model, which photo) → `Read receipt (OpenRouter vision)` (calls the model with the image and the question "read the amount and date").

> **What's missing here.** There is no text-recognition node and no node comparing against the request's amount on this canvas — this is a rig for one question: how the model itself handles the photo, with nothing around it for backup.

## Speaker notes

This is a real canvas from the live rig — the very screen on which reading the receipt photo was measured, with no dressing up and no simplification.

Three nodes, and all three are visible in one row. The first takes in the photo: a form that receives the receipt shot exactly as it would arrive in an ordinary request. The second node assembles a request to the model from it — which model to call and which photo to pass it. The third makes the actual call: a request with the image and a question to read the amount and date goes out, and an answer comes back.

That's the whole device on this canvas. Three nodes, one arrow after another, no fork.

It's worth saying plainly what isn't here, because that matters more than what is. There's no classic text-recognition node on the canvas — the photo goes into the model whole, in pixels, with no intermediate step. And there's no node that would compare the read number against the amount the client typed into the request as text. The "matched / didn't match" decision doesn't exist here at all.

This isn't an oversight, and it isn't a simplification for the sake of saving time in the session. This canvas was built for exactly one question: how the model itself reads the photo, with no backup of any kind around it. To answer that question honestly, nothing that could correct or paper over the result should stand around the reading — no recognition, no cross-check. We just broke down, on a separate scheme, the device that adds this cross-check: it includes a recognition node and a two-number comparison node, but they aren't on this particular canvas, because this one measures something else.

Next we'll look at exactly what the model answered on different versions of the same photo, while only one thing changed — how hard that photo was compressed.

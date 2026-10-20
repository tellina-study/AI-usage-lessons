---
id: n11
type: mechanism_node_graph
duration_min: 1.5
assertion: "The real configuration of the model version: six nodes from the request form to Telegram, the model is called twice — once to extract fields, once to compose the notification text"
learning_goal: "Layer 2 for Version 1: a real screenshot of the live n8n rig, cropped wide enough to show all six main-path nodes on one frame, per the owner's standing note for all cases — a screenshot must show the whole process, not a tight crop on two nodes. Node captions are the tool's own English UI labels, quoted verbatim. The prompt text itself isn't legible here; it has its own dedicated slide (n11a)."
visual:
  pattern: mechanism_node_graph
  figure: k1-n8n-versiya1-real.png
  primary: >
    A real screenshot of the n8n canvas (workflow "С8 · Case 1 (before) —
    LLM composes the notification", live rig), a wide crop: request form →
    field extraction → vocabulary check → write row → "Compose
    notification…" (the caption is cut off by an ellipsis — that's how the
    n8n interface behaves with a narrow card) → send to the coordinator in
    Telegram. Under two of the nodes is a "Model*" marker — a required
    parameter; the model call here is not optional.
  backup: >
    This is the real live screenshot — unchanged, and NOT re-drawn: the
    node titles ("Request form", "Extract fields", "Compose notification
    (LLM)", "Notify coordinator (Telegram)") are the n8n tool's own English
    UI labels and are quoted exactly as shown on the canvas. What's visible
    on this frame: Request form (trigger, lightning-bolt icon) → Extract
    fields (`Set`, marked "Model*" below it — the field-extraction node
    also calls the model; this is not new and does not distinguish Version
    1 from Version 2, see the same marker on the n14 figure) → Vocabulary
    check (`IF`) → Write row → "Compose notification…" (the caption is cut
    off by an ellipsis on the canvas; the full name "Compose notification
    (LLM)" is confirmed by `stend/stage-1-before.json`) → Notify
    coordinator (Telegram). Below the composition node is the same
    "Model*" marker, and just below that, an extra node, "Result screen
    Model (notification)", which Version 2 does not have (the same spot on
    the n14 figure is empty) — this is the main structural difference
    between the two versions, visible already at the canvas level, before
    opening a single settings panel. No workflow or execution id on the
    frame (canon §3) — the breadcrumb on the source screenshot shows only
    the workflow name, which the crop excludes entirely.

    The exact prompt text is not legible on this frame (the canvas shows
    only node cards, not their open settings) and is deliberately not
    stated in prose here — stating it in prose next to a frame that
    doesn't show it is exactly how the earlier form of this slide produced
    a "slide text vs. what the screenshot shows" mismatch, which the owner
    caught. The prompt text, with its own real settings-panel screenshot,
    is on the next slide (n11a).
---

# The whole path on the rig: the model version

## Assertion

Six nodes from the request to Telegram — not a diagram, the real canvas of the live rig. The model is called here twice: to extract fields, and to compose the notification text.

## Visual

> Request form → field extraction (calls the model) → vocabulary check → write row → **"Compose notification…"** (calls the model a second time, the caption cut off by an ellipsis — that's how the n8n interface behaves with a narrow card) → send to the coordinator in Telegram.

## Speaker notes

This is the real canvas of the live rig — not an illustration and not a simplified diagram, but the same screen you'd see opening the "Case 1 (before)" workflow in n8n. The frame shows the whole path: the request form, field extraction, the vocabulary check, writing the row, the message-composition node, and sending to Telegram.

Look closely at two details right on the frame. First — the "Compose notification…" node's caption is cut off by an ellipsis right in the interface: the card is narrow, and n8n truncates a long name the same way it would truncate any other. The full name, "Compose notification (LLM)," is only visible if you open the node itself — that's an honest interface limitation, not a simplification on our part. Second — the "Model*" marker under this node: the asterisk means the parameter is required — the model call here isn't optional, it's a configuration requirement.

The same marker sits under the field-extraction node, a bit to the left — and that's not news: the model was already doing work there, even in the simpler diagram; without it there's no turning a request's free-form text into structured values. What's new is the second call, at the step that composes the finished message, where all the needed values already exist and there seems to be nothing left to extract. Next to the composition node there's one more block visible — "Result screen Model (notification)"; in the template version we'll see shortly, that block isn't there at all, in the same spot — the difference is visible at the canvas level already, before we open a single settings panel.

What exactly this model gets as input, and what it's asked to do, isn't visible on this frame: the canvas shows node cards, not their open settings. Explaining that in prose next to a frame that doesn't show it would mean asking you to take it on faith. Instead, the next screen is the real settings panel of this same node, with the real prompt text, as it stands on the rig right now.

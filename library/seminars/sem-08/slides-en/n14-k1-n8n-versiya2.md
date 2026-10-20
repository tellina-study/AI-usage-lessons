---
id: n14
type: mechanism_node_graph
duration_min: 1.5
assertion: "The real configuration of the template version: the same six-node path, but with no model call at all on the composition step — that node and the adjacent model block are simply absent"
learning_goal: "Layer 2 for Version 2: the same wide canvas crop as n11, for direct visual comparison between versions — all six main-path nodes on one frame. Node captions are the tool's own English UI labels, quoted verbatim; the exact expression text has its own dedicated slide (n14a)."
visual:
  pattern: mechanism_node_graph
  figure: k1-n8n-versiya2-real.png
  primary: >
    A real screenshot of the n8n canvas (workflow "С8 · Case 1 (after) — a
    template instead of the model", live rig), the same wide crop as n11:
    request form → field extraction → vocabulary check → write row →
    "Compose notification (template)" (the caption reads in full — it's
    shorter, so it fits the card) → send to the coordinator in Telegram.
    In the spot where Version 1 had a "Model*" marker and the "Result
    screen Model (notification)" block, this frame is empty: there's no
    model node on this step at all.
  backup: >
    This is the real live screenshot, unchanged and NOT re-drawn — the
    node titles are the n8n tool's own English UI labels, quoted exactly
    as shown. Same crop rectangle as n11, deliberately: the two frames
    line up directly, one on top of the other, and the difference shows
    literally in the place where Version 1 had the model block and this
    one has empty space. What's visible: the same path as n11, with one
    structural difference at the composition node — "Compose notification
    (template)" (the caption reads in full, the card is the same width,
    but the text is shorter than "Compose notification (LLM)") is
    connected by a DIRECT arrow to "Notify coordinator (Telegram)," with
    no intermediate model node and no "Model*" marker beneath it. The
    "Result screen Model (notification)" block, which sits in the same
    spot in Version 1, is absent here — in its place there's a plain
    "Result screen". The field-extraction node ("Extract fields") is
    still marked "Model*" — that call is shared by both versions, not
    part of the difference between them. No workflow or execution id on
    the frame (canon §3).

    ONE KNOWN, DOCUMENTED DISCREPANCY (carried over from the RU production
    history, still current): an earlier wave found an honest mismatch —
    the target text example in n06 once included "contact," which the
    node's expression doesn't collect. The orchestrator fixed the target
    in SETKA-KEYSOV-S8.md and in n05–n08 to the three values without
    contact (contact is already visible on the result screen; the
    notification solves one job — noticing multi-topicness) — the target
    and the implementation now agree, no open question remains.

    The expression text of the composition node is not legible on this
    frame (the canvas shows only node cards) — it's on its own slide
    (n14a), with a real settings-panel screenshot.
---

# The whole path on the rig: the template version

## Assertion

The same six-node path as the model version, with one structural difference at the composition step: there's no model node here at all, and it's visible at the canvas level already.

## Visual

> Request form → field extraction (calls the model) → vocabulary check → write row → **"Compose notification (template)"** (the caption reads in full, no model call) → send straight to the coordinator in Telegram.

## Speaker notes

This is the same canvas of the live rig as the previous screen, with the same crop — deliberately, so the two frames are easy to mentally overlay. The path is recognizable right away: the request form, field extraction, the vocabulary check, writing the row, the composition node, sending to Telegram.

The difference is in exactly one place, and it's visible already, before opening any settings panel. In the previous frame, the "Model*" marker sat under the composition node, along with an extra block, "Result screen Model (notification)." Here, that spot is empty: "Compose notification (template)" is connected by a direct arrow straight to the send node, with not a single intermediate model node. The caption reads in full, with no ellipsis — simply because "(template)" is shorter than "(LLM)"; the card is equally narrow in both versions.

The field-extraction node, a bit to the left, is still marked "Model*" — and it's important not to confuse this: that call is shared by both versions, the model hasn't left the chain entirely, it has only left one specific step. The difference between Version 1 and Version 2 isn't "with a model" versus "no model at all" — it's "the model is called twice" versus "the model is called once, exactly where it's genuinely needed." The vocabulary-check and write-row nodes between them are untouched by this edit at all — they're built the same way in both versions, and there's no need to compare them: the difference lives in exactly one node, it doesn't spread across the chain.

What the "Compose notification (template)" node actually does instead of the model — one expression, written once by hand — isn't visible on this frame either: the canvas shows cards, not their settings. Same as last time, describing that in prose next to a frame that doesn't show it would mean asking you to take it on faith. The next screen is the real settings panel of this node, with the full expression text, as it stands on the rig.

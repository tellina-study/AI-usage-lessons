---
id: n68
type: mechanism_node_graph
duration_min: 1.0
assertion: "The model `qwen/qwen3-vl-8b-instruct` reads the photo in pixels and names the amount and date; code separately cross-checks what was read against the amount from the request's text"
learning_goal: "2026-10-29 edit (issue #299, stend/zamery-k6-edinyy): the classic-recognition node was removed — on the rig the photo always goes into the model in pixels, in both measured devices (the two-step one and the single-call one). Layer 1 of the 'our solution' beat names the model right on the frame (C5) and shows the architecture that was actually measured, not an invented one. Three blocks instead of five — a fix for a frame overflow."
visual:
  pattern: mechanism_node_graph
  figure: k6-shema-chtenie-i-sverka-en.png
  primary: >
    A single-row scheme: photo → model qwen/qwen3-vl-8b-instruct (pixels,
    name on the scheme) → amount and date → cross-check in code against
    the amount from the request → a "matched?" fork. Ocean palette, type
    size no smaller than 7.5 pt. No measured number anywhere.
  backup: >
    DEVICE EDIT (issue #299, `stend/zamery-k6-edinyy/README.md`, section
    "Discrepancies with the Deck — Addresses, Not a Retelling"). The
    previous edition carried a "classic recognition" node between the
    photo and the model. On the rig, there is no such node in either of
    the two measured devices — not in the two-step one
    (`zamery-k5-k6/sborka.py`, node `k6_http`), nor in the single-call one
    (`zamery-k6-edinyy/sborka.py`, node `k6e_http`): the photo goes into
    the model `qwen/qwen3-vl-8b-instruct` whole, in pixels, in both cases.
    The edit removes the claim about recognition and names the real
    device: the model reads the photo and returns the amount and date;
    code compares these values against the amount the client typed in the
    request's text — the model never gets that text at all.

    The model's name — on the scheme and in the visible body of this frame
    (C5, the owner's strict rule): an implementation frame with no model
    name is a defect, even if the name sits only in the notes.

    Three blocks instead of five. The previous edition carried two
    separate blocks for each outcome branch (matched / diverged) plus a
    separate block about the reliability of the request's text — the
    build flagged OVERFLOW (four blocks) and a composition below the
    working field. Both outcomes are now folded into one block; the
    question of the request text's reliability is a separate device nuance,
    not part of the base contour, and lives in this frame's notes (expanded
    further, on `n75`).

    No orchestrator names, no scenario id, and no other Latin script besides
    the model's name is deliberately on the scheme: §2 of the canon
    requires a Layer 1 wording that will survive a change of TOOL (the
    call, the node, the provider), but it isn't required to hide WHAT reads
    the photo — this is measured, not abstract, and hiding the name here
    would mean hiding an honest result. The real canvas is one screen
    ahead, `n69`.

    No numbers on this frame: a Layer 1 scheme shows the device, not the
    measured outcomes — this case's numbers live in beats `n70`, `n71`,
    `n72`, `n73`, and in the new beats `n73a`–`n73e` (single call versus
    two steps, issue #299).
---

# The model reads the photo, code cross-checks

## Assertion

The model `qwen/qwen3-vl-8b-instruct` gets only the photo and names the amount and date. It never sees the request's text — code compares the amount from it separately.

## Visual

> **The device.** The receipt photo goes into the model `qwen/qwen3-vl-8b-instruct` whole, in pixels, with no text recognition → the model returns the read amount and date → code compares the read amount against the amount the client typed in the request's text → a "matched?" fork.

> **Two outcomes, and why the comparison is a check.** Matched — the request moves on the usual way. Diverged — it goes to Olga for a manual check. The two compared numbers are obtained by different paths: the model reads the photo and never sees the request's text; code compares the numbers and never reads the photo itself. This separateness of paths is exactly what makes the comparison a check.

## Speaker notes

Let's look at the device that's really measured on the rig, without the step it used to be credited with as an extra. The receipt photo goes into the model `qwen/qwen3-vl-8b-instruct` whole, in pixels: there is no separate text recognition between the shot and the model in this device, and never was. The model gets only the image and a request to read the amount and date — it never sees the request's text at all.

Next to the read numbers sits one more: the amount the client wrote in the request themselves, as words or digits. Code compares these two values — one deterministic operation, with no second model call and no re-reading of the same photo.

If the numbers match, the request moves on as confirmed: we have two confirmations of one amount, independent of each other. If they don't match, the request isn't automatically closed in favor of either of the two sources — it goes to the manual cross-check that Olga performs today.

Here's how this device differs from simply "read the photo and believe what you read." One number from one source is backed by nothing but itself. Two numbers from two independent sources behave differently: their divergence becomes a signal on its own, and one that doesn't require knowing in advance which of the two numbers is correct — it's enough to know they should match, and they didn't.

A separate question remains about the reliability of one of these two sources: what if the request's text isn't entirely reliable either? It's written by the same person as the figure on the receipt — the same vulnerability as in the case about manipulating a refund. Sources the client doesn't control would be more reliable: the date the request was submitted in the system, the course record in the CRM, the price list at the time of the request. The case only names this path as a direction — there's no node built for it on the rig.

Next — a real screenshot of the rig where this reading was measured.

---
id: n49a
type: mechanism_node_graph
duration_min: 1.0
assertion: "The card's three nodes aren't a separate process off to the side — they grow out of the same point where the ordinary request-intake path already writes a row and shows the result screen"
learning_goal: "New letter-tail slide from the owner's screenshot-density edit (issue #274, 2026-10-20 evening). Between n49 (tool-agnostic architecture) and n50 (a tight zoom on the real configuration + size boundary) — an establishing shot of the real canvas, showing exactly where Case 4's three nodes branch off the already-familiar request-intake path."
visual:
  pattern: mechanism_node_graph
  figure: k4-n8n-vetvlenie-real.png
  primary: >
    A real screenshot of the n8n canvas (workflow "C8 · Case 4 — photo
    in Telegram," live rig), cropped wider than n50's close view: `Write
    row` → `Result screen` (the main request-intake path) on the left, and
    an arrow running upward from the branch point to `Compose notification
    (template)` → `Fetch card image (HTTP)` → `Send card (Telegram photo)` —
    the three nodes the case breaks down next.
  backup: >
    ORIGINALLY this screenshot was conceived as a confirming `fig_after`
    figure on n48 (breakdown), on the model of
    `k2-n8n-test-stend-real.png` on n20 (owner's voice edit, same day,
    same complaint "too few screenshots" — already applied to Case 2).
    Pulled off n48: `check_tracks_pdf.py` (canon §7, checking against
    what LibreOffice ACTUALLY drew, not against the `metrics`
    measurement) caught a real defect — on n48 a 4-row table and two
    text blocks already stand before the figure, and the figure
    encroached on the text above it (5.7–7.0 pt across different crop
    aspect ratios; the crowding is structural, not fixable by adjusting
    the aspect ratio). Moved to its own letter-tail screen, where the
    figure is the only content block, and `check_tracks_pdf.py` and
    `check_text_overlap_pdf.py` come back clean on it.

    Source — a real screenshot of the live n8n rig (Playwright, taken
    2026-10-20, https://n8n.lessons.tellian.io, see
    notes/mcp-limitations.md [#233-8]), file
    `stend/n8n-screenshots-raw/case4-telegram-image.png` (1900×1100, the
    same source file as `k4-n8n-tsepochka-real.png` on n50, but cropped
    wider to the left), assembled in `rendered/make_figures_k4.py` by
    the function `vetvlenie_real()`, saved as
    `library/seminars/sem-08/rendered/figures/k4-n8n-vetvlenie-real.png`
    (980×304, crop (820, 258, 1800, 562) of the source file — the right
    edge also removes the n8n interface's floating "✨ AI assist"
    button, which has nothing to do with the process).

    On the frame, literally: `Write row` → `Result screen` (the main
    request-intake path — the same one already shown on Case 1's
    canvas, `k1-n8n-versiya1-real.png`, n11) and an arrow running upward
    from the branch point after `Write row` to Case 4's three nodes.
    This is honestly NOT the full canvas of the workflow "C8 · Case 4 —
    photo in Telegram": left out of frame are `Request form` / `Extract
    fields` / `Model` / `Vocabulary check` — the same model-based
    request-parsing trick already shown on Case 1's figure; repeating it
    here would be repeating a screen already seen. And honestly BELOW
    the frame (on the uncropped screenshot, but not in this crop)
    there's one more real branch — `Write row · not parsed` / `Result
    screen · not parsed`, the fallback path for when the model fails to
    parse the request's fields: it genuinely exists on the rig, but it
    belongs to the request-INTAKE step, not to assembling and sending
    the card, and it isn't the focus today — the only reason not to
    include it in this frame HERE (not deliberate concealment) is
    geometry: a single rectangle holding both it and the card's three
    nodes at once turns the frame nearly portrait (ratio ~1.88) and hits
    the schema's ceiling (`deck_kit.py: FIG_MIN_FILL`/`FIG_NATURAL_H`) —
    checked by direct calculation, not by eye. The workflow-name
    breadcrumb, the `Published` badge, the Editor/Executions/Evaluations
    tabs, the app's left icon column, the right floating zoom/search
    panel, the "Execute workflow" button, the bottom `Logs` panel — all
    out of frame; there is no workflow/execution id anywhere on the
    frame (canon §2–§3 `tools/seminar-production/README.md`).
---

# The branch point on the real canvas

## Assertion

The three nodes we're about to configure aren't a separate process off to the side — they're a continuation of an already familiar path: the request gets written to the table, the result screen closes — and from that same point an arrow runs off to the card.

## Visual

> **Workflow "C8 · Case 4 — photo in Telegram," live rig.** `Write row` → `Result screen` — the same main request-intake path as in Case 1. From the branch point after `Write row`, an arrow runs upward, into `Compose notification (template)` → `Fetch card image (HTTP)` → `Send card (Telegram photo)` — the three nodes this case breaks down next.

## Speaker notes

Before we open the settings panels, one wider frame — to see where these three nodes even come from on the canvas.

This is the real canvas of the live rig, the same workflow as the next screen, just with a bit more context in frame. On the left — `Write row`: the node that writes the request to the table, and `Result screen` — the screen the ordinary form ends on. This is the exact same request-intake path we already saw on Case 1's canvas: the form, the field extraction, the topic-dictionary check, the row write. We don't repeat it here — it's simply visible off to the left, because that part of the process hasn't changed.

What has changed is visible on the arrow itself. From that same point, right after `Write row`, a second arrow runs off — upward, to the `Compose notification (template)` node. Before, in Case 1, all the recipient ever saw from that point was a text message. Now a new branch is attached to that same spot in the process: `Compose notification (template)` → `Fetch card image (HTTP)` → `Send card (Telegram photo)` — the three nodes we'll break down one at a time on the next screens. This is the honest answer to "where does Case 4 show up in the real process" — not alongside, not instead of, but as a branch off a point that already existed.

Deliberately left out of frame: further to the right, on the same wiring, there's another branch, for when the model fails to parse the request — also real, also part of this workflow, but it belongs to the intake step, not to assembling and sending the card, and it isn't our focus today. We aren't pretending the canvas ends exactly where this frame ends — it keeps going, just not in this direction of the breakdown, and that choice to cut the frame there is a deliberate one, not an accident of cropping.

Now that it's visible where these three nodes grow from — a closer zoom: the same chain, but with the real size-boundary check that is what brought us into this case in the first place.

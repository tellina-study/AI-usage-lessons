---
id: n60
type: problem_scenario
duration_min: 1.0
assertion: "Version 1 — caption the picture in text and search that caption with the same mechanism as in Case 3"
learning_goal: "Case 4's scene beat: the need (find a similar past scan) + version 1 as a direct continuation of the three previous cases. The honest nuance about the coming failure is named outright (rework/section-0 requires this at the opening; here — at the entry into the case itself)."
visual:
  pattern: problem_scenario
  figure: case4-shema-postanovka-en.png
  primary: >
    On top — diagram S1 (canon forma-keysa-s-zamerom.md §2): solid lines
    for the flow this session has already built (scan → caption/OCR turns
    the picture into text → text search finds a similar one, Cases 1–3); a
    dashed gold arrow points at the caption/OCR node — this is the one
    step Case 4 tries to bypass, by comparing the picture itself directly.
    Below the diagram — a tile for the need, version 1 in plain prose, an
    honest warning that one of the three options will end in failure —
    without revealing details.
  backup: >
    THE STAGING DIAGRAM (rule S1) added by this edit:
    `rendered/make_figures_sem10.py::case4_shema_postanovka()`, a new
    function, doesn't touch `case1_scheme`/`case2_scheme`/`case3_scheme`/
    `case4_scheme`. The solid row continues the staging the room has
    already seen across Cases 1–3 of this same session (storage, cutting,
    text search), rather than inventing a separate flow from scratch (S8:
    relying on the room's memory of past SESSIONS is forbidden — but this
    is the same day, the same three previous beats, described again by a
    diagram, not by memory). The dashed arrow points specifically at the
    "caption/OCR" node, not at the input or output as a whole — because
    that's the one step version 2 (searching picture-by-picture directly)
    tries to replace; the text search further down the chain (Cases 1–3)
    stays untouched either way.

    SETKA-KEYSOV.md Case 4, "Staging," verbatim. The honest warning about
    the coming failure — rework/section-0-otkrytie.md, "The nuance the
    opening is required to name outright": failure is part of the story,
    not a footnote, and must be named, not sprung on the room suddenly
    during the breakdown.
---

# How to find a similar past scan

## Assertion

Three methods — caption and search as text, search the picture directly, compare pictures by a short fingerprint. One of the three will end in an honestly shown failure.

## Visual

> **The need.** The training center gets scans of forms and receipts in requests regularly. We need to find a similar scan among past requests: reading the current one is not enough here.

Version 1 — the natural first attempt, a direct continuation of the three previous cases: caption the picture in text (recognize the text, or get a text description from a model) and search that caption with the same mechanism as in Case 3 — as an ordinary text document.

> One of the three options tested today will end in an honestly shown failure — a real failure with a learned lesson; calling it a weakened version of success would be wrong.

## Speaker notes

Olga's training center gets scans of forms and receipts in requests regularly, and a new request often looks like one of the past ones — same type of form, same supplier, same receipt format. We need to find a similar one among the past ones: reading the current scan is not enough here.

Version 1 — the natural first attempt, a direct continuation of what the three previous cases of this session have already done: caption the picture in text — recognize the text, or get a text description from a model — and search that caption with the same mechanism as in Case 3, as an ordinary text document. This is the cheapest way to reuse everything already assembled today: not one new node, not one new search method.

The session's opening already warned about this outright: one of the three options we check today will end in an honestly shown failure. The method planned to be tried — comparing pictures directly, in their own numeric representation — did not work in practice on this rig. This isn't a technical detail for a footnote — it's part of the case's story, and we work through it just as carefully as the options that did work.

The third option — comparing pictures by a short fingerprint, without calling a model — comes from a separate, honest observation about the very nature of Olga's task: not all similar scans are similar in the same way. Sometimes "similar" means "the same type of document by content," and sometimes it means "literally the same document, just scanned again." These two cases are different, and before choosing among the three options, it's worth keeping in mind that the right answer may well consist of two mechanisms at once — one alone may not be enough here, exactly as already happened in the third case of this session.

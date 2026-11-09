---
id: n73
type: criteria_checklist_and_boundary
duration_min: 0.75
assertion: "Trying multimodal search of picture by picture is worth it only after a controlled test at the needed resolution — on this rig it failed"
learning_goal: "The honest limit of the check itself (the reference labeling doesn't degrade along with the picture) + when it's worth trying multimodal search directly. The session's fourth axis row closes here — the last of four. Part 2 of 2 (continuing n72 — perceptual hash's boundary). Letter-suffix pending deck reconciliation (tools/seminar-production/README.md §1, issue #311)."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    A tile for the check's honest limit, a tile closing the session's
    fourth axis row.
  backup: >
    SETKA-KEYSOV.md / rework/section-4-poisk-po-izobrazheniyam.md,
    "Nuances," verbatim.
---

# When to try searching picture by picture directly

## Assertion

A controlled test at the needed resolution is a mandatory condition; on this rig it failed.

## Visual

> **When it's worth trying search picture by picture directly — and when it's definitely not, on this rig.** Worth trying: when the provider and model confirm accepting the picture by a separate controlled test on two knowingly different inputs, at the exact resolution the task needs; one quick "did a response come back" check isn't enough here. Not worth it right now, on this rig: `amazon/titan-embed-image-v1` through OpenRouter at the real scan's resolution (300×450) — a confirmed failure from a controlled test; calling it an assumption would be wrong, and it's not a reason to avoid multimodal embeddings altogether either.

> **The session's fourth axis row is closed:** if we know how to search text, we won't find a picture the same way: a caption loses what's visible, direct comparison of pictures can answer without an error and still not use the input at all.

## Speaker notes

Separately — the honest limit of the phash boundary check itself. CORD's reference recognized text for the receipts doesn't change when the image is rotated or recompressed, so the claim "a caption loses what's visible under rotation of the picture" can't be checked directly on the same pair with this corpus: real text recognition would degrade under rotation, the reference labeling wouldn't. This is a limitation of the checking tool itself; calling it a finding about the method would be wrong, and we name it honestly, not masking it behind a general "not enough data."

Multimodal embedding itself has a boundary too, not only phash — and it needs to be named in direct form: a general "be careful with pictures" won't cover for it here. Trying search picture by picture directly is worth it when the provider and model confirm accepting the picture with a separate controlled test on two knowingly different inputs, specifically at the resolution the task actually needs — a downsized one for convenience of checking doesn't count. It's not worth it right now, on this specific rig: `amazon/titan-embed-image-v1` through OpenRouter at the real scan's resolution — a confirmed failure; calling it an assumption would be wrong. This isn't a reason to give up on multimodal embeddings as a class — a different model or a different provider may behave differently, and the only honest way to find out is to repeat the same controlled test: documentation isn't taken on its word here.

And now the session's last, fourth axis row is closed. It looked reliable that if we already know how to search text, we'd find a picture the same way, just by captioning it in words. It turned out to be harder, in two directions at once: a caption fundamentally loses what's visible on the picture itself, and direct comparison of pictures can answer without a single error and still not use what it was shown at all.

Next — the session's concept interlude, and closing all four axis rows at once.

---
id: n73a
type: measured_outcome_table
duration_min: 1.5
assertion: "The same question from the course owner got its own measurement: the same receipt, the same six file sizes, the same model reading the photo — but now the model itself compares what it read against the request, in one call, instead of code doing it outside"
learning_goal: "Beat n73a (issue #299, Z3, `stend/zamery-k6-edinyy/`): exposition of the experiment BEFORE the results (C2, item 1) — the measurement's device, corpus size (30 calls), group structure (15 requests with a correct amount / 15 with a wrong one), and a sample plan record with the expected answer. No outcome numbers here — those are revealed by n73b–n73e."
visual:
  pattern: measured_outcome_table
  figure: k6-galereya-shesti-razmerov-en.png
  primary: >
    Two short cards — the question and the measurement's device, the
    corpus's volume and structure with an example. Below them — a figure:
    the six real `receipt-01` files at their REAL size ratios (not
    normalized to one display height), the last one almost indistinguishable
    by eye. Text deliberately trimmed to two blocks (a layout edit) — the
    figure needs height, and five beats, n73b–n73e, are still ahead; it's
    too early to unpack the details.
  backup: >
    Source: `stend/zamery-k6-edinyy/README.md` (issue #299, Z3 — a direct
    answer to the course owner's question from the S9 transcript of
    2026-10-29, 49:11–50:39: "why do we still do it in 2 steps, and not
    1"). Device: one n8n scenario, three nodes (receive → build request →
    call the model), mirroring `k6_read` from
    `../zamery-k5-k6/sborka.py` — the same model
    (`qwen/qwen3-vl-8b-instruct`), the same credential, the same
    temperature, 0.2 (the baseline code's real value, not the text of the
    assignment, which said "0" — the discrepancy was recorded in the
    README BEFORE measuring, for an honest comparison under identical
    settings).

    30 calls = 6 resolutions × 5 repeats, the same receipt `receipt-01`,
    the same set of sizes as in n70/n71 (a plain `Image.resize(...,
    LANCZOS)` of one file). In every call, the request carries an amount:
    15 of 30 — `zayavka_verna=True` (the stated amount equals the true
    one, 18990), 15 — `zayavka_verna=False` (one of five other real
    receipt amounts from the rig, deliberately different from the true
    one). The leak check was done BEFORE the calls (5 automatic checks,
    README § "Leak Check") — unlike the first run of Measurement 4.1
    (`../zamery-k5-k6/`), where a numeric example in the `sum_rub` field's
    description coincided with `receipt-01`'s real amount and skewed a
    month and a half of earlier measurement.

    Figure — `stend/zamery-k5-k6/build_k6_gallery.py` (issue #299, K6-10:
    the owner asked three times during the 2026-10-29 breakdown to show
    the input pictures "at full resolution" — before this beat, the deck
    had no frame with all six test files together, only crops of
    individual fields on n72a/n72b). All six images are scaled by ONE
    shared factor (0.2) — the size ratios on the figure are real, not
    normalized for readability, unlike the crops on n72a/n72b, which
    deliberately enlarge the small resolutions to show the blockiness. An
    EN re-render is needed for this track (added for this EN track, issue
    #172/#319) — the underlying receipt images carry printed
    Russian/Cyrillic receipt content.

    The final score's numbers (25/30, 27/30, 15/30 and so on) are
    deliberately not on this frame (C2, the "exposition before results"
    principle) — they're revealed by beats n73b (summary) and n73c–n73e
    (breakdown by group).
---

# One call instead of two: structure of the measurement

## Assertion

A multimodal model already drives the reading step on the rig; there's no classic OCR on the rig at all. If so, why split reading and cross-checking into two steps? This question from the course owner got its own measurement.

## Visual

> **The question and the device.** The reading step on the rig is already driven by the model `qwen/qwen3-vl-8b-instruct` — so why split reading and cross-checking into two steps? This measurement gives the model the photo and the request's text in one request: it names the amount and date itself and hands down the verdict itself. Call temperature — 0.2, the same as in the two-step device.

> **30 calls: six file sizes × five repeats.** In fifteen calls, the request carries the correct amount — 18,990 rubles, exactly as on the receipt. In fifteen, it carries one of five other real amounts, deliberately wrong. Example: the file shrunk 32 times, the stated amount is 9,800 — the honest expected answer from the model is: amount 18,990, verdict "didn't match."

## Speaker notes

The case has already shown how a separate model reads the photo, with nothing around it, and that in this device the cross-check is done by code — a separate, token-free step. On the breakdown, the course owner asked a direct question: if a multimodal model already drives the reading, and there's no classic text recognition on the rig at all, why split reading and cross-checking into two steps? Maybe one call, where the model both reads and compares, works just as well?

This is where a separate measurement starts, and it answers that question with a measured number. The device is almost identical to reading without a cross-check: one n8n scenario, three nodes, the same model `qwen/qwen3-vl-8b-instruct`, the same call temperature — 0.2. The only difference is that the model, in one and the same request, gets both the photo and the request's text, and decides for itself whether what it read matches what was stated. Before, that decision was made by code outside; now the model itself makes it, inside a single call.

Thirty live calls: six sizes of the same file, five repeats at each. Half the requests carry the correct amount — exactly the one written on the receipt. The other half carry one of five other real amounts, deliberately different from the true one. For every call, the honest answer is known in advance: what the model should say if it read the photo and compared the result with no errors.

The six pictures below are the files that really went into the model on this measurement, at the exact size ratios, with no leveling for readability. Already here the main thing is visible: the last resolution isn't a small picture, it's an almost blank gray rectangle. What the model answers on such an input — on the next screens.

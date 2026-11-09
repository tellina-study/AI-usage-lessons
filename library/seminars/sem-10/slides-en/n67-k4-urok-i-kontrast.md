---
id: n67
type: content
duration_min: 0.75
assertion: "'Answers without error' and 'uses the input' are different things: the only check is to feed two knowingly different pictures and compare the output"
learning_goal: "S2 beat 3 (breakdown, forma-keysa-s-zamerom.md §1) for Case 4's finding, continuing n66: a headline lesson + a contrast with perceptual hash as a separate tile, a different unit of measurement (S6: one unit per comparison, don't mix them in one table). Part 2 of 2. Letter-suffix pending deck reconciliation (tools/seminar-production/README.md §1, issue #311)."
visual:
  pattern: content
  primary: >
    A formula tile with the headline lesson. A contrast tile with
    perceptual hash — a different unit of measurement, explicitly labeled.
  backup: >
    The contrast with phash — a separate tile, not a fourth table row
    (S6): cosine and Hamming bits are different units, mixing them in one
    column would be dishonest even with superficially similar-looking
    numbers.
---

# An error-free response doesn't prove the input was used

## Assertion

The only honest check is to feed in two knowingly different pictures and compare the output; checking the response's shape won't show this.

## Visual

> **An error-free response and a processed input are different things. The only way to check this is to feed in two knowingly different pictures and compare whether the output differs; a test of "did the response come back in the right shape" won't show it.**

> **For comparison, in a different unit.** Perceptual hash (the classic, model-free technique) on these same receipts confidently tells a duplicate apart from a random stranger receipt: 0–1 bit Hamming distance to the duplicate against 14–49 bits to a random stranger receipt. This isn't a row in that table: Hamming bits and cosine are different units (a detailed breakdown of phash's own boundary — in this case's boundary beat, further on).

## Speaker notes

An honest contrast stands right alongside. Perceptual hash — the classic technique with no call to a model at all — confidently tells a duplicate apart from a random stranger receipt on these same receipts: zero-to-one-bit Hamming distance to the duplicate against fourteen-to-forty-nine bits to a random one. This isn't a row in the same table and not a direct competition of the same numbers — the unit is different, bits instead of cosine — but the sheer fact that such a simple classic technique holds the task where the model with a picture on input doesn't is worth saying out loud right here; there's no reason to wait for the end of the case for that.

The lesson the case is obligated to state outright, without hedging: "answers without error" and "uses the input" are different things. The only way to check this is to feed in two knowingly different pictures and compare whether the output differs; one test of "did the response come back in the right shape" isn't enough for that. The quick check normally used to test an integration would have passed here — and that's exactly why it isn't enough.

For an engineer in Olga's position, this lesson carries beyond one specific model: before building any new model call into a working process, it's worth asking, "does the response differ when the input is genuinely different." Just "did a response come back" isn't enough here. This check is cheap and fast, but it's almost never done by default — which is exactly why failures like this stay unnoticed until someone stumbles onto them by accident or deliberately sets up a controlled test.

This lesson stands alongside the findings of all three previous cases: every time, the session ran into not a broken tool, but a tool that wasn't honestly checked against what it's actually supposed to do.

Next — this case's solution architecture and how it's assembled on the real rig.

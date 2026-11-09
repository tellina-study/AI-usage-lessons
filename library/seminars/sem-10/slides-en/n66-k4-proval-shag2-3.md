---
id: n66
type: content
duration_min: 0.75
assertion: "At all three resolutions — failure or noise: at the real scan's resolution the model returns a bit-identical vector for any two different receipts"
learning_goal: "S2 beats 2-3 (summary + breakdown by group, forma-keysa-s-zamerom.md §1) for Case 4's finding: the summary (none of the three resolutions gave reliable distinguishing) → a breakdown by resolution with an explicit verdict on every row (S3: 'IDENTICAL VECTOR,' not a vague 'kind of'). Part 1 of 2 (n67 — the lesson and the contrast with perceptual hash): split, because the 15pt floor font size leaves no room for the table and two conclusions on one slide (issue #311)."
visual:
  pattern: content
  primary: >
    A summary tile (one aggregate across all three resolutions). A
    breakdown table — Resolution · Verdict · What the test showed, each
    row's verdict in capitals.
  backup: >
    SETKA-KEYSOV.md Case 4, "The failure that is part of the case's
    story," Steps 2-3, verbatim. Numbers — stend/raw/case4-results.json,
    correlation_text_vs_image_cosine_over_all_pairs = -0.077;
    stend/README.md table "Picture resolution → Behavior."

    The 128×192 row was corrected on 2026-11-02 per a live repeat check
    (`stend/raw/case4_resolution_probe.json`, exec_id 2514-2517, two real
    CORD scans): the earlier caveat "cosine ≈ 0.997, a barely noticeable
    difference" did not reproduce on this pair — the same bit-identical
    vector was obtained (cosine = 1.0) as at 300×450. The 300×450 and
    64×96 rows were not changed.
---

# Summary and breakdown: no resolution gave reliable distinguishing

## Assertion

A controlled check with two different inputs reveals what the "did a response come back" check masks: at the real scan's resolution, the model doesn't use the picture at all.

## Visual

> **Summary.** At the resolution actually needed by the task — failure. The model doesn't use the picture at either of the two tested real-scan resolutions (300×450, 128×192) — a difference only shows up at the smallest tested size, and even there it's statistically indistinguishable from noise.

| Resolution | Verdict | What the test showed |
|---|---|---|
| 300×450 (real scan) | **FAILURE — IDENTICAL VECTOR** | cosine = 1.0 to 9 decimal places for any two different receipts |
| 128×192 | **FAILURE — IDENTICAL VECTOR** | cosine = 1.0 — confirmed by a live repeat check (2026-11-02) |
| 64×96 (small preview) | **FORMALLY DISTINGUISHES, BUT ≈ NOISE** | correlation of visual similarity with textual similarity across all pairs: −0.077 — statistically indistinguishable from zero |

## Speaker notes

This is the summary and breakdown of the finding, whose structure was named by the previous beat without a single result. A short summary before the table: none of the three tested resolutions gave reliable distinguishing — the difference is only in how plainly visible that is.

The one check usually used to test a new integration is simple: send a request and make sure a correctly-shaped response comes back. `amazon/titan-embed-image-v1` passes this check without a hitch — the vector arrives, the dimensionality is right, there's no error at all. If the measurement had stopped here, this option would have gone into the session's plan as a working second attempt.

The controlled check with two different inputs shows something else. At the scan's real resolution — three hundred by four hundred fifty pixels, exactly the size the rest of this session's cases actually work with — the model returns a bit-identical vector for any two different receipts: the cosine-similarity coefficient matches to the ninth decimal place. This isn't a guess and not one unlucky call — it's a direct comparison of vectors from different pictures, repeated, and that's exactly how the finding was uncovered. At the preview downsized to one hundred twenty-eight by one hundred ninety-two pixels — the same picture: a live repeat check on two real CORD scans, done separately on November 2nd, gave the same bit-identical vector as at the real scan's resolution — cosine similarity exactly one; "almost one" doesn't apply here. The earlier assumption of a barely noticeable difference at this resolution did not hold up. Only at the smallest tested size, sixty-four by ninety-six, does the model react to the content at all, even formally — but the spread between random receipts is statistically indistinguishable from noise: the correlation between textual and visual similarity across all pairs of this measurement equals minus 0.077, which is practically zero.

It was separately confirmed that the degradation is tied specifically to the image: input length as such has nothing to do with it — the same endpoint with a text input, a short word against a long description, correctly returns different vectors at any string length. If it were about input length as such, the text would degrade too; it doesn't.

What follows from this, and how it looks next to the classic model-free technique — next.

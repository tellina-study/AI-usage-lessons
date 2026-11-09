---
id: n65
type: content
duration_min: 0.5
assertion: "Two DIFFERENT receipts at the same resolution must give two DIFFERENT vectors — a plain error-free response won't prove that"
learning_goal: "S2 beat 1 for Case 4's finding, continuing n64: what the expectation is, if the model really sees the picture. There's still no result on this frame — it's on n66. Part 2 of 2. Letter-suffix pending deck reconciliation (tools/seminar-production/README.md §1, issue #311)."
visual:
  pattern: content
  primary: >
    An expectation tile: different receipts at the same resolution must
    give different vectors.
  backup: >
    The beat's form — canon forma-keysa-s-zamerom.md §1, beat 1 of 3:
    corpus/groups/model/expectation, no result.
---

# Structure of the measurement: what result is expected

## Assertion

If the model really sees the picture — two different receipts must give two different vectors. A plain error-free response isn't enough here.

## Visual

> **The expectation, if the model really sees the picture: a plain error-free response isn't enough here.** Two DIFFERENT receipts at the same resolution must give two DIFFERENT vectors — the cosine distance between them must differ from 1.0. A check of "did the response come back in the right shape" doesn't show this: it passes the same way whether the model honestly uses the picture or ignores it entirely.

## Speaker notes

The expectation is stated directly and checkably; calling it a vague wish for "it should work" would be wrong. If the model actually processes the picture it was sent (a plausible-looking vector alone isn't enough here), then two knowingly different receipts must get two different vectors — the cosine distance between them must differ from one. This isn't an arbitrary threshold: one is the distance between two absolutely identical vectors, and if two DIFFERENT inputs give that, the output doesn't depend on the input.

This is specifically a controlled check; it's not a repeat of the ordinary quick error check — and it's important to understand why. The first check usually used to test a new integration is to send one request and see whether the response comes back without an error and with the right dimensionality. That check says nothing about whether the model uses the picture's content: a response of the correct shape comes back the same way whether the model honestly looks at the input or ignores it and returns something that doesn't depend on the content at all. The only way to tell one from the other is to feed in two knowingly different images and compare whether the output differs.

This is the same methodological trap already seen in this session's text cases, only it's more dangerous here. With text, a gap between the response and the document's content is relatively easy to spot by eye. With a picture that doesn't work: a vector can't be read, you can't just open it and see whether it matches what's actually drawn on the receipt. That's why the controlled check does real work here: it's the only available way to learn the truth.

This exact check is easy to skip when building a real solution: the integration responds without errors, a demo on one receipt looks convincing, and the temptation to stop there is strong. The result of this check — next beat.

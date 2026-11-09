---
id: n75
type: criteria_checklist_and_boundary
duration_min: 1.0
assertion: "A cross-check against an independent value is needed when a number from a photo has nowhere else to confirm itself from, and isn't needed when no such second source exists at all, or the decision is checked by a human either way"
learning_goal: "Nuances and boundary of Case 6 in plain form (A7): 'when it's needed · when it's not,' plus two mandatory caveats, both named out loud: the receipts are synthetic, and both fields break — the date earlier, the amount later, but not forever."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    One numbered nuance, a two-column table "when it's needed · when it's
    not" — strictly a contrast — and two closing cards with mandatory
    caveats.
  backup: >
    The nuance follows SETKA-KEYSOV-S9-part2.md, section "Case 6,"
    subsection "Nuances," item 1: "numbers and money amounts have the
    smallest margin of any data type on a document." Backed by an
    external number, CHISLA-SVERENO.md, line 62 (FinCriticalED,
    arXiv:2511.14998, status VERIFIED): accuracy on numeric fact fields
    across different models — 52.65–66.83%.

    Grid nuances 2 and 4 (the price of a "cheap" image model; how stable a
    wrong guess is) aren't carried onto this frame: the first is a
    separate topic about cost, not about the cross-check's scope of
    applicability; the second is already shown by beat n71 and
    generalized by beat n74 — repeating it here would inflate the frame
    with no new thought.

    BOTH MANDATORY CAVEATS STAND AS CLOSING CARDS, not a footnote, both
    out loud:

    (1) The receipts are synthetic — per SETKA, nuance 5, first half: made
    by this same session to demonstrate the mechanism on a controlled
    example, not a measurement of model quality on a stream of live
    documents.

    (2) Both fields break, but at a different character height — per
    SETKA, nuance 3 (updated by the honest rerun of 2026-10-27, issue
    #299): the date breaks earlier, at the eighth fraction (0 out of 15,
    beat n71), the amount later, only at the smallest size (0 out of 5 at
    53×64, beat n70); the measurement doesn't license generalizing to
    "photos read badly."

    The boundary — plain form, two columns: the right column rests on the
    technique's own device (is there a second source, does a human read
    the decision), not on general words about applicability.
---

# When a cross-check against an independent value is needed

## Assertion

A cross-check is needed wherever a number from a photo has no other way to confirm itself. Where that way already exists, or a human checks the decision either way, it isn't needed.

## Visual

1. **Numbers and money amounts have the smallest margin of any data type on a document.** An independent check of financial statements found numeric-field accuracy across models in the range of **52.65–66.83%** (FinCriticalED) — lower than you'd want where a wrong reading costs real money.

| When it's needed | When it's not |
|---|---|
| A number from the photo has a second, independent way to confirm it — e.g., what the client typed as text in the same request | No second independent source exists — nothing to compare against, only trust in the single reading |
| A field is set smaller than the rest — it has its own earlier degradation threshold and fails first | Every field is equally large, with a wide character-height margin at any realistic compression |
| A decision on the read number moves forward with no second human reading | Staff open and read the document either way, before any decision moves forward |
| A wrongly accepted number costs money or an unreversible date change | An error costs less than the cross-check itself, and any discrepancy gets caught and fixed another way first |

> **This measurement's receipts are synthetic.** All six demonstrate the mechanism on a controlled example with a known correct answer — not a measurement of model quality on the center's real document stream, where these exact numbers can't recur.

> **Both fields break, but at a different character height.** The date broke earlier, at the eighth fraction (0 of 15); the amount later, only at the smallest size (0 of 5). "Photos read badly" over-generalizes this: a bigger field holds longer than a smaller one, but not forever.

## Speaker notes

One nuance and a boundary, and two caveats that can't be passed over in silence.

The nuance. Numbers and money amounts on a document have the smallest margin of any data type on it. On an independent check of financial-statement breakdowns, accuracy on numeric fact fields across different models holds in a range from fifty-two to sixty-seven percent — noticeably lower than you'd want for a field where the cost of a wrong reading is higher than for almost any other field on a document.

The boundary, in plain form. A cross-check against an independent value is needed where a number from a photo has a second way to confirm itself — for example, what the client themselves typed as text in the same request. It's needed where a field is set smaller than the rest: that's exactly the one that will hit its own personal degradation threshold first. It's needed where a decision made on this number moves forward with no second reading by a human. And it's needed where the cost of an error is money or a date that can't be quietly reversed after the fact.

Not needed — and that's not a formal caveat. If no second independent source of the same fact exists at all, there's nothing to compare against, and all that's left is trust in the single reading. If every field on the document is set equally large and the character-height margin is big at any realistic compression. If a staff member opens and reads the document either way, before any decision on it moves forward. And if the cost of a possible error is lower than the cost of the cross-check itself.

And one more question: what if the source being cross-checked against is itself unreliable? The request's text is an unreliable candidate: it's written by the same person as the number on the receipt — the same vulnerability as in Case 4. More reliable are indirect signals the client doesn't write and doesn't control: the date the request was submitted in the system (a payment dated in the future, or before sales opened, is suspicious), the client's record in the CRM (an amount outside the course's price range is a reason to cross-check even before the request's text), the price list at the time of the request (the expected amount is known in advance).

Now two caveats — worth saying out loud, not left between the lines.

First: this measurement's receipts are synthetic. We made them ourselves, to show the mechanism on a controlled example where the correct answer is known in advance. This is not a measurement of how the model handles a stream of real documents of varying quality from the training center — it's a demonstration of the device on one prepared case.

Second: both fields break, but at a different character height. On this material, the date broke earlier — already at the eighth fraction of compression, zero correct out of fifteen attempts at the three smallest sizes. The amount held out longer, but it broke too — at the smallest of the six sizes tested, zero out of five. Drawing the conclusion "photos read badly" or "numbers from photos can't be trusted" from this would be a broader generalization than what was measured. A field set in a bigger font holds noticeably longer than one set smaller — but both have a boundary.

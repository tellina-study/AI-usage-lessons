---
id: n35
type: answer_breakdown_table
duration_min: 2.0
assertion: "On the same 101-request set, version 1 erred 9 times at the boundary, version 2 — 0 times; outside the boundary both versions are flawless — the difference lies entirely in behavior at the one point of the condition"
learning_goal: "The side-by-side breakdown AFTER the test — a sequential beat, not a parallel A/B. Numbers updated to the extended 101-request set (was 51)."
visual:
  pattern: answer_breakdown_table
  primary: >
    A three-row table: errors on all 101 requests · at the boundary ·
    outside the boundary. Both versions were run on the same extended set of
    101 requests — the very one that found the problem and confirmed it on
    harder phrasings, not a separate test built "for version 2."
  backup: >
    Numbers from this round's full protocol. Original 51: 3 errors for
    version 1 (all at 3,000 rubles), 0 for version 2. New 50 (harder — tight
    border / two numbers / indirect phrasing): 6 errors for version 1 (again
    all at 3,000 rubles, including cases where 3,000 came from arithmetic in
    the text), 0 for version 2. Total: 9 vs. 0 on 101. Mirrors RU n35 (issue
    #274).
---

# Breakdown of both versions after testing

## Assertion

Both versions were run on the same extended set of 101 requests — the one that found the problem and confirmed it with harder phrasings. The difference lies entirely in behavior at the boundary of the condition.

## Visual

| | Version 1 (rule in the prompt) | Version 2 (`IF` node) |
|---|---|---|
| **Errors on 101 requests** | **9** — all on the amount of 3,000 RUB | **0** |
| **At the boundary (3,000 RUB)** | "escalate," even though the rule implies "okay to approve" | "approve" — the condition `> 3000` leaves no room for a second reading |
| **Outside the boundary** | correct in every case, including amounts 20 RUB from the boundary and texts with two numbers | correct in every case |

## Speaker notes

Here is the final comparison, and it matters what it's built on: this isn't a new test assembled specifically to make version two look good. It's the very same extended set of a hundred and one requests — the original fifty-one, on which we first found the problem, and the new fifty, harder than the first, added precisely to test the finding against tougher phrasings. Version two was run on exactly the same set.

The first row — the number of errors. Version one — nine out of a hundred and one. Version two — zero. Not "fewer," but zero, on a set that includes a dense cluster of amounts right at the boundary, amounts twenty rubles away from it on both sides, texts with two numbers, and phrasings where the amount comes from arithmetic rather than being stated directly — that is, on a set that gives any error the maximum chance to show up, if there is one.

The second row — the very behavior at the boundary that started all of this. At an amount of exactly three thousand rubles — whether it arrived as a direct number or as arithmetic inside the text — version one answered "escalate," even though the rule, read carefully, implies that this exact amount can still be approved. Version two answers "approve" on the same amount, and the reason isn't that the `IF` node "understood the rule better." The reason is that the condition "strictly greater than 3,000" mathematically allows no second reading: either one number is bigger than the other, or it isn't.

The third row — outside the boundary both versions are flawless, and the extended set confirmed this separately: neither amounts twenty rubles from the threshold, nor texts with a distracting second number, threw version one off. It was bad at exactly one point — and that is exactly why the diagnosis "a systematic error at the boundary," rather than "an unreliable model," was the correct diagnosis, and the fix was a targeted replacement of one node rather than a rewrite of the whole chain.

This is the form in which this course compares decisions within a case: not two worlds built in parallel to illustrate a thesis, but a version built as a direct answer to a finding, and measured on the very same — now extended — test that produced and confirmed that finding.

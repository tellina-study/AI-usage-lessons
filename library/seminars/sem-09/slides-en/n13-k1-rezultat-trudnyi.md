---
id: n13
type: measured_outcome_table
duration_min: 2.25
assertion: "On the fifteen questions in the 'topic exists, detail differs' group, version 1 answered confidently and wrongly 6 times — in three repeating ways"
learning_goal: "Breakdown of the 'topic exists, detail differs' group (C2 beat 3, canon §8.11): the easy group's zero is placed next to six of fifteen on the hard one. An explicit verdict on every example (C3) and three named systematic errors as tiles (C4), not a paragraph."
visual:
  pattern: measured_outcome_table
  primary: >
    A strip of two summary tiles from n11a/n12 — "topic entirely absent —
    0 of 3" and "topic exists, detail differs — 6 of 15," captions keeping
    them clearly apart. Below the strip, a table of three systematic
    errors (C4) with an example and a verdict on each (C3). A line on how
    the hard group differs from the easy one.
  backup: >
    Numbers — from `stend/zamery-k1-k3/README.md`, Measurement 1: 15
    questions through the same version-1 scenario with not a single edit
    to it, runs 619-647 (odd-numbered). Measurement summary: a good
    outcome (correct answer or a correct escalation) — 9 of 15; a
    confident wrong answer to the client — 6 of 15.

    THREE PATTERNS INSTEAD OF TWO EXAMPLES — 2026-10-29 edit (C4: "error
    groups are set off visually, not read out of text"). All six of
    version 1's wrong answers were personally checked by me against the
    protocol's own reference standard `correct_by_base`
    (`raw/zamer1-results.json`, exec 619-647) and sorted into three
    repeating patterns, two questions each:

    1. "Silence in the knowledge base read as a denial" — Q4 (exec 625,
       medical certificate — the topic is mentioned, the detail
       "certificate" is never named in it) and Q11 (exec 639, a paper
       certificate — only the electronic one is named in the base,
       nothing is said about a paper format).
    2. "A number or threshold applied wrongly" — Q6 (exec 629, amount
       2500 < threshold 3000, the answer claims the opposite) and Q15
       (exec 647, 48 hours > the 24-hour rule, the answer claims the
       opposite).
    3. "Specifics invented that aren't in the knowledge base" — Q9 (exec
       635, the base doesn't name a specific retake week, the answer
       names one) and Q12 (exec 641, the base only says "recalculated
       individually," the answer promises a cash refund).

    TWO OF THE SIX ARE CONFIRMED BY A VERBATIM PROTOCOL QUOTE and were
    already on this frame before the edit (Q4, Q15 — "Finding A" of the
    README). THE REMAINING FOUR (Q6, Q9, Q11, Q12) are my own
    classification against the same yardstick (`correct_by_base`), not
    separately asserted line-by-line by the protocol; the total (6)
    matches the measurement's stated outcome, but if someone re-reads the
    protocol and disagrees with one of the four, that doesn't change the
    final number, only the distribution across patterns. Flagged to the
    orchestrator by report as a reasonable but not protocol-certified
    step.

    THE "ONE MEASUREMENT POINT" CAVEAT IS REMOVED FROM THE VISIBLE LAYER
    (C9, 2026-10-29 edit, K1-11) and moved entirely into the notes. This
    resolves the collision in `forma-keysa-s-zamerom.md` §12 item 3 (C9
    against §8.11) in favor of the option the file itself offers as one of
    two legitimate ones: "the caveat moves to the notes" — the honest
    count is still named (§8.11 isn't broken, it's just not on the frame,
    it's in the text the lecturer speaks and that goes into the published
    notes).

    Run numbers don't appear on the visible layer (BRIEF §2).
---

# Fifteen questions with a neighboring detail

## Assertion

When the right item is in the knowledge base but a different detail is asked, version 1 stops admitting it doesn't know: 6 confident wrong answers out of 15, in three repeating ways.

## Visual

> **Topic entirely absent from the knowledge base: 0 wrong of 3** · **Topic exists, detail differs: 6 wrong of 15**
> A good outcome — a correct answer or an honest hand-off to a human — 9 of those same 15.

| Error pattern | Example | Verdict |
|---|---|---|
| **Silence in the knowledge base read as a denial** | "Is a medical certificate needed?" — not a word about a certificate in the base (only passport, SNILS, a parent's consent); answer: "a certificate isn't required" | **WRONG** — the item's absence is named as the absence of a requirement |
| **A number or threshold applied wrongly** | "I gave two days' notice about missing a class — will I get a reschedule?" — rule is "no later than 24 hours," 48 hours satisfies it; answer: "not allowed" | **WRONG** — 48 is greater than 24, rescheduling should be permitted |
| **Specifics invented that aren't in the knowledge base** | "Will the retake be this week already?" — the base names only the recurring schedule (every second Saturday), it doesn't confirm a specific week; the answer names one directly | **WRONG** — names a date that isn't in the knowledge base |

> **How the hard group differs from the easy one.** There, the topic wasn't there at all, and there was nothing to build an answer from. Here, a similar item always sits nearby — and the model builds from it, in three different ways.

## Speaker notes

The same version-1 scenario, with not a single edit to it. Fifteen questions, built on one principle: for each, the knowledge base has a close item, but the detail asked about is either missing from it or requires telling a neighboring rule apart from the right one.

The result. A good outcome — meaning either a correct answer or an honest hand-off to a human — nine of fifteen. A confident wrong answer, the kind that would have gone to the client — six of fifteen. Compare that to the previous screen: where the topic was entirely absent, wrong answers were zero of three.

The six wrong answers split into three repeating patterns, two questions each. First — silence in the knowledge base read as a denial. The knowledge base says nothing about a medical certificate, listing only passport, SNILS, and a parent's consent. The model answered that a certificate isn't required — the absence of an item read as a substantive claim, "no such requirement exists." The same pattern on the paper-certificate question: the base names only the electronic one, says nothing about a paper format — and the answer confidently states that a paper one isn't provided.

The second pattern — a number or threshold applied wrongly. On rescheduling: the rule is no later than twenty-four hours, notice was given two days ahead, that's forty-eight hours, more than twenty-four, rescheduling should be allowed. The model answered that it wasn't. The same pattern on the refund question: the threshold for a manager's decision is three thousand rubles, the client's amount is two thousand five hundred, below the threshold, meaning the regular process applies. The model confidently said it still goes through the manager.

Third — specifics invented that aren't in the knowledge base. On a retake: the base names only the recurring schedule, the second Saturday of the month, and explicitly doesn't confirm a specific date "this week." The model named a specific week. The same pattern on a question about transferring to a cheaper course: the base says only "recalculated individually," nothing about a cash refund of the difference — and the answer promises exactly that, a cash refund.

Here's where the line falls, and it's a substantive one. The self-report stays silent where the question is grossly uncovered by the knowledge base: there's nothing to build from, and the model admits it doesn't know. And it stops staying silent where a similar but not-quite-right item sits nearby: there's something to build from, and it builds, in three different ways, with not a single sign of doubt in the text.

The honest measure of this number: fifteen questions run once each, no repeats. Six of fifteen is one measurement point, not a stable proportion; a different sample would give a different number. But it's enough for our purposes: we're not measuring how often the model errs. We're looking at whether this error can be caught before the answer goes out. In version 1, there's nothing to catch it with.

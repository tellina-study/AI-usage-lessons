---
id: n73
type: measured_outcome_table
duration_min: 2.0
assertion: "Checking the response's format caught zero of fifteen wrong dates; cross-checking against an independently known value caught all fifteen, with not a single false alarm"
learning_goal: "The case's engineering payload: a breakdown between a format check and a cross-check against an independent value, on the same measurement's own data. The two counts of wrong dates (0 out of 15 and 15 out of 15) are distinguished by captions naming exactly what each one catches; a third number — 15 out of 15 correct matches — is physically set apart with the word 'correct,' even though its denominator happens to coincide with the first two after the measurement was topped up."
visual:
  pattern: measured_outcome_table
  primary: >
    Two cards side by side, each with an explicit caption naming what's
    caught: "format check — 0 of 15 wrong" and "cross-check against an
    independent value — 15 of 15 wrong," plus a line about there being no
    false alarms on 15 CORRECT cases — a different count, the same
    denominator after topping up (a coincidence, not a methodological
    link). Below the cards — an honest caveat about where these numbers
    come from.
  backup: >
    Numbers from `stend/zamery-k5-k6/README.md`, Measurement 4.1, section
    "Cross-Checking as a Defense": 15 wrong dates (after topping up the
    measurement — 5 on each of the three smallest resolutions, sizes
    "eighth," "sixteenth," "thirty-second") — all 15 are valid by the
    DD.MM.YYYY format, a schema check would pass all of them. An
    independent cross-check against the receipt's true date (known in
    advance, since this is our own synthetic document) catches all 15
    discrepancies with not a single false alarm; on 15 cases where the
    date was correct (sizes "original," "half," "quarter"), the same
    comparison never fires — 15 of 15 correct matches.

    AN HONEST METHODOLOGICAL CAVEAT STANDS ON THE FRAME, not only in the
    backup: the demonstration is built on the DATE, because the date has
    more failures and they start earlier on the compression scale (15 out
    of 30 attempts, starting at the eighth fraction); on the AMOUNT in
    this same measurement, failures are noticeably fewer — 5 out of 30,
    only at the smallest, thirty-second fraction (beat n70) — but they
    exist, not zero, after the honest rerun of 2026-10-27 (issue #299).
    In the real case, the independent value is the amount the client
    typed as text in the request, not an already-known truth from the
    receipt generator; this measurement session didn't build that
    cross-check (there's no text field with a stated amount in the
    measurement's webhook) — the same mechanism is shown on the field
    where failures are more common, not on the one where they're fewer.

    The two counts of wrong dates — "0 of 15" and "15 of 15" — are
    distinguished by captions, "what the format check caught" / "what the
    cross-check caught"; a third number, "15 of 15 correct matches," is
    physically set apart with the word "correct" from the first two, even
    though its denominator happens to coincide after the measurement was
    topped up — that's a coincidence of numbers, not a methodological
    link. A BRIEF §2 requirement.
---

# What the format check caught and what the cross-check caught

## Assertion

The same set of wrong answers. One way of checking sees zero violations in them. The other sees all of them.

## Visual

> **Format check on the response: 0 of 15 wrong dates caught.** Each of the fifteen wrong values is a syntactically correct date in the required "DD.MM.YYYY" shape. A schema check, if applied, would pass all fifteen: the format is fine, the content isn't.

> **Cross-check against an independently known value: 15 of 15 wrong dates caught.** Comparing the read date against the document's already-known true date catches every one of the fifteen discrepancies instantly.

> **No false alarms on correct dates.** On the fifteen cases where the date was read correctly, the same cross-check never fired — 15 of 15 CORRECT matches passed the check calmly. (The denominator is the same as for the wrong dates above — a coincidence after the measurement was topped up, and nothing more: there, discrepancies were counted; here, their absence.)

> **Honestly: why the demonstration is built on the date.** In this same measurement, the amount has noticeably fewer failures — five out of thirty, only at the smallest resolution, against fifteen for the date. The demonstration is built on the field with more discrepancies. In a real request, the independent value is the amount the client themselves typed as text. This measurement cross-checked the reading against the receipt generator's already-known truth; the client's text wasn't separately collected in the measurement's webhook.

## Speaker notes

Let's take one and the same set of wrong answers — fifteen dates that the model misread on compressed copies of the same receipt — and look at them through two different ways of checking.

The first way is checking the response's format. It looks at whether the value resembles a date of the right shape: a day, a month, a year, with dots between them. All fifteen wrong values satisfy this requirement completely. So the format check, if applied, would honestly say "everything's fine" on each of the fifteen cases. Zero out of fifteen errors caught isn't a sign that the check is broken; it's a sign that it answers a different question. It asks one thing: does the value look like a date in shape. It never asks whether it matches the document's correct date at all.

The second way is cross-checking against an independently known value. The receipt's true date is known in advance: it's a document we made ourselves for the measurement, and we have an answer to compare the reading against. The comparison catches all fifteen discrepancies instantly, with not a single miss.

It also matters what this cross-check doesn't do: it doesn't raise an alarm where there's nothing to raise one about. On the fifteen cases where the date was read correctly, the same comparison stays silent — fifteen out of fifteen correct matches passed calmly, with not one false alarm. The denominator here is the same as for the wrong dates above — a coincidence after topping up the measurement, nothing more: there, discrepancies were counted; here, their absence.

And one last thing worth saying plainly rather than leaving between the lines. The demonstration is built on the date, because the date has more failures in this measurement and they start earlier — the amount, in the same attempts, has noticeably fewer failures, five out of thirty against fifteen, and only at the smallest of the six resolutions. That doesn't mean the amount has no failures at all: the field with more discrepancies just gives a clearer demonstration. In a real request, the independent value is the amount the client themselves typed as text; in this measurement, the cross-check ran against the receipt generator's already-known truth, and this measurement didn't separately collect that check against the client's text. The mechanism is shown honestly, on the field where it actually fired more often.

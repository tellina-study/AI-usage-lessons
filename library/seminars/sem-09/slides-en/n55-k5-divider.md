---
id: n55
type: case_divider_quote
duration_min: 0.5
assertion: "The same question — and two different treatments of the same client, both from a real run"
learning_goal: "Case 5 divider. Text form — CONTRAST (BRIEF §4a: each case of the session has its own divider form, P3): two answers to the same question side by side, with no numbers. Names the problem (A2), gives no measured result."
visual:
  pattern: case_divider_quote
  primary: >
    Dark background, two answers stacked one above the other, with not a
    single digit. At the bottom, a six-case track for the session, the
    fifth one highlighted.
  backup: >
    The "contrast" form was assigned to this divider by
    BRIEF-PROIZVODSTVO.md §4a: the "scene", "number", "question", and
    "quote" forms are given to Cases 1, 2, 3, and 4, and the "stakes" form
    to Case 6. Six dividers in a row don't read in the same grammar
    (illness §4.1 No. 7, rule P3).

    BOTH ANSWERS ARE TAKEN FROM REAL RUNS, not invented: both are
    shortened paraphrases of execs 799 and 804 from measurement A of the
    protocol `stend/zamery-k5-povtorno/README.md` (ten repeats of the same
    question at temperature 0). exec 799: "please contact the
    administrator"; exec 804: names the exact amount. The amount's own
    figure was deliberately left off the divider — the form's "no
    numbers" rule, and BRIEF §4a's rule that "a divider that states the
    outcome zeroes out the breakdown."

    What is deliberately NOT shown: how many times each answer came up,
    which of the two is correct, and which is typical. All three
    questions come from the same point in the process, under the same
    configuration, on the same day — the divider names only the problem,
    without the outcome.

    Case title — "Answer Reproducibility", by function, as in the case
    track of `rendered/deck-config.yaml` (`case_track`).
---

# Case 5. Answer Reproducibility

## Assertion

The process already knows how to answer on its own. This case's question is whether it answers the same question the same way.

## Visual

> One client gets an exact refund amount for their question. Another client — with the exact same question, on the same day, to the same process — gets the phrase "please contact the administrator," and not a single number in the answer.

## Speaker notes

We built a process that answers on its own, taught it to stay silent where the knowledge base gives no grounds, put a check in place before sending, and protected the amount field from being overridden by the request's own text. All of that is about the process doing the right thing once. Today's case is about something else: does it do the same thing every time.

This case's question doesn't look technical at first — it's ordinary. Two clients who wrote almost the same thing got different answers from the process. One got the exact amount owed to them. The other got a suggestion to contact the administrator, with not a single number. Both requests went to the same process, on the same day, with the same model-node settings we've already seen and will see again on screen later in the case.

An engineer's first reaction to a picture like this is predictable: somewhere in the assembled chain there's a bug, and it needs fixing in the settings. The same question is supposed to get the same answer — that sounds like a self-evident requirement for any process standing in for a human. Hence the question this case opens with: what to do with the node's settings so the same question reliably gets the same answer.

This is a natural first hypothesis, and we'll take it seriously — we'll test, on a real rig, four methods that are the first thing to come to an engineer's mind on hearing the word "nondeterminism." But before looking at what these four methods actually give in practice, it's worth pinning down the setup itself, once and precisely: the two answers on screen are real, both were produced by the same process on the same question, and neither one is labeled correct on this frame.

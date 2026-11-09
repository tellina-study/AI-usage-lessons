---
id: n75b
type: measured_outcome_table
duration_min: 1.5
assertion: "In three of six measurements, where the decision is checked by something other than the model's own text, the result came out error-free — inside a self-written text, that never happened once; but the exported technique is no guarantee forever, and Case 2 doesn't fit the pattern at all"
learning_goal: "Moved off `n75a` as its own frame by the 2026-10-29 pre-gate (issue #299): the six-metric table and the conclusion drawn from it don't share a frame — combined, the text wall turned into bullets still overflowed the frame together with the table (the composition sliding past the canvas, 7.36″ against 7.50″). CLAUDE.md canon § 'Structure of an Industry Lecture's Section': a case/breakdown doesn't have to fit one slide; chopping it down to save space is forbidden — meaning an extra frame, not trimmed text. The title names the subject (what reads out of the measurements), not a virtue ('the main conclusion')."
visual:
  pattern: measured_outcome_table
  primary: >
    Four fact cards in a row, each one observation with numbers: (1)
    inside a self-written text — not a single error-free result, (2)
    exported outward — three of six measurements with no errors, (3) this
    is no guarantee forever — for one of these three (more precisely, for
    a fourth, similar case, Case 6), after the honest rerun the result is
    no longer error-free, (4) Case 2 doesn't fit the pattern at all.
  backup: >
    Text and numbers carried over unchanged from `n75a`'s former closing
    block (before the 2026-10-29 pre-gate, issue #299) — only the form
    changed: one paragraph of ~180 words → four short points.

    THE HONEST CONCLUSION IS CHECKED AGAINST ALL SIX, not invented
    (recalculated after Case 6's honest rerun, issue #299, 2026-10-27): in
    all six breakdowns, a decision left inside the text the model writes
    about itself (a self-reported confidence score — Case 1, a prompt
    instruction — Case 2 and Case 4, a worked example — Case 5, a second
    call of the same model as a judge — Case 3) never once gave an
    error-free result. A decision exported to where something besides the
    model's own text checks it (code — Case 3, the same rule computed by
    code — Case 4, a direct description instead of an example — Case 5 on
    the first question) was error-free three times out of six
    measurements. Case 6 (a direct measurement of amount-reading accuracy
    across six resolutions) also exports the signal beyond the model's own
    self-report — but after the honest prompt fix, it too isn't
    error-free: 25 out of 30, not 30 out of 30. A CAVEAT INSIDE THE
    CONCLUSION IS MANDATORY and stands on the frame: an exported technique
    lowers the error, but doesn't guarantee its absence — the code+judge
    combination (Case 3) sank to 85%, the description (Case 5) on the
    second question gave 6 out of 10 instead of the previous 10, and Case
    6's amount after the honest rerun is 25 out of 30, not 30. Case 2
    doesn't fit this conclusion on any side: there, not one of the five
    exported approaches, including attempts to pull the rule out of prose
    into an explicit conditional form, cleaned up the error — named
    honestly as the sixth case, the one that doesn't confirm the pattern,
    rather than hidden.
---

# What reads out of the six measurements together

## Assertion

In five cases, the decision could have been left inside the text the model writes about itself. Not once did that give an error-free result.

## Visual

> **Inside a self-written text — not a single error-free result:** Case 1's ceiling — 40%; Case 2 — 0 of 8 across all five directions; Case 5's few-shot — 0 of 10, twice.

> **Exported outward (code, a separate form field, a direct description) — three of six measurements with no errors:** Case 3's code — 20 of 20, Case 4's code rule — 64 of 64, Case 5's description on the first question — 10 of 10.

> **Not a guarantee for the future:** Case 6's amount, after the honest rerun of 2026-10-27, is no longer an error-free result — 25 of 30; code+judge sank to 85%; Case 5's description on the second question gave 6 of 10.

> **Case 2 doesn't confirm the pattern:** not one of the five exported versions of the rule, including an explicit conditional form, ever cleaned up the error.

## Speaker notes

The previous frame was a table with no ranking, six different measurements side by side. But if you look at all six as one question asked six times, a pattern emerges, and it's worth stating honestly, with its boundary.

In five cases, the decision could have been left inside the text the model writes about itself — naming a confidence number, asking it to follow an instruction, showing an example, asking a second model to act as judge. Not once did that give an error-free result: forty percent of bad outcomes as a ceiling in Case 1, zero out of eight in Case 2 across all five formats, zero out of ten twice for few-shot in Case 5. And where the decision was exported to somewhere checked by something other than the model's text — code in Case 3, the same rule computed by code in Case 4, a direct description instead of an example on Case 5's first question — there were no errors at all, three times out of six measurements. A fourth, similar case — Case 6's amount, read across six resolutions — turned out, after the honest rerun, to no longer be error-free: twenty-five correct out of thirty possible.

And right away, an honest caveat: the exported technique isn't insured forever. The code-plus-judge combination in Case 3 still sank to eighty-five percent — adding a second checker doesn't remove the cost of an error. The same rule description in Case 5 gave six correct out of ten on the second question instead of the previous ten. And Case 6's amount is the same story: it held with not a single error on five of six resolutions, and broke cleanly on the smallest one. And Case 2 doesn't confirm the pattern at all: there, not one of the five approaches, including an attempt to explicitly spell the rule out in conditional form, cleaned up the error. These six measurements are six honest data points, and most of them point the same way; they can't all be taken together as confirmation of one single rule.

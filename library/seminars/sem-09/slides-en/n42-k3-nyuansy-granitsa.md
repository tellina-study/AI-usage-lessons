---
id: n42
type: criteria_checklist_and_boundary
duration_min: 1.0
assertion: "A code check belongs where the criterion can be written and read; where there's no criterion, neither code nor a reliable judge can be built — and that's known before building anything"
learning_goal: "Case 3's nuances and boundary in the plain, imperative form the course requires (A7): 'when it's needed · when it isn't,' with the technique's own limit named — the fragility of a substring check to grammatical case, measured on our own rig."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    Three numbered nuance banners, below them a two-column table "when it's
    needed · when it isn't" — strictly for contrast — and a closing banner
    on the limit of acceptance, with its own measurement.
  backup: >
    The nuances follow SETKA-KEYSOV-S9.md, section "Case 3," subsection
    "Nuances," all three.

    Nuance 1 rests on external numbers from CHISLA-SVERENO.md: row 12
    (arXiv:2303.17651, status CHECKED — five step-by-step retry values
    found verbatim) and row 11 (Huang and co-authors, arXiv:2310.01798).
    The gain of the first step, 2.05 points, and of the fourth, 0.45, are
    computed from these five values and named on the frame as gains, not
    as independent measurements of their own. I narrowed the grid's
    wording "with ground truth the curve plateaus" to what the fact check
    actually confirms: where there's a gain, it plateaus fast; where there
    is no correctness criterion at all, the curve goes down. CHISLA-SVERENO.md
    doesn't support claiming that the first measurement specifically used
    an external ground truth. Flagged to the orchestrator as a report.

    Nuance 2 is a property of the built-in loop: the attempt counter is set
    by hand. The template number and the expression name are not carried
    onto the frame (CHISLA-SVERENO.md, row 15, status "not re-checked this
    round"): the frame states the mechanism, which doesn't depend on the
    template number.

    THE GRID'S MANDATORY CAVEAT STANDS AS A CLOSING BANNER, not a footnote:
    the fragility of an exact substring match to grammatical case, 1 case
    out of 6 (`stend/zamery-k1-k3/README.md`, the "not converged" breakdown
    and items 2 and 6 of the "What wasn't confirmed" section). Alongside
    it, both honest halves from the same source: the same question, in a
    no-loop build, got an answer in the needed grammatical case and passed
    the check — meaning this is sample spread, not a difference between
    builds; and this particular check was written by the measurement's own
    author, not taken as a model example — a more carefully written
    criterion wouldn't have had this weakness.

    UPDATED 2026-10-26: this specific case was fixed and re-measured —
    `code_check_node()` got a regex branch for kb5, tolerant of
    grammatical case, and the re-measurement gave 6 of 6 (executions
    829–834, `README.md` § "Fix 2026-10-26"). This doesn't cancel the
    banner's conclusion: the check catches form, not meaning — the fix
    removed one measured instance of this property showing up, not the
    property itself. The other five keywords in the check didn't get a
    regex; their case-sensitivity risk is neither measured nor ruled out.

    The boundary is stated in the plain, two-column form. The right column
    rests on what this very case measured (cost in calls, false
    rejections), not on general words about applicability.
---

# When to build the check in code, and when there's nothing to build it on

## Assertion

A criterion you can write down and read is the precondition for building a check at all.

## Visual

1. **Retries plateau fast, wherever they help at all.** Step by step: **71.34 → 73.39 → 75.06 → 75.74 → 76.19**, the gain falling from 2.05 to 0.45. With no correctness criterion, the curve goes down: **95.5 → 91.5 → 89.0** (Huang et al.).
2. **The loop has no safety net by default** — set the attempt counter by hand, or the loop won't stop on its own.
3. **The "not converged" branch must call someone** — otherwise, once the limit runs out, it silently sends the person a rejected text.

| When it's needed | When it isn't |
|---|---|
| The requirement can be written in words and checked unambiguously: length, a detail, numbers, language | The criterion is style, tone, "reads well" — there's nothing to write it down with, and neither code nor a judge can be built |
| The answer goes out to a person with no second read, and no mistake gets caught before it's sent | Staff still read the answer before sending anyway: the check already exists, by eye |
| A month from now, you'll need to show why an answer was accepted or sent back | A retry costs more than the mistake does: the judge's attempt is two calls, and a false rejection is paid for in full |
| A retry is cheaper than escalation, and the loop has a limit and a "not converged" branch | There's nowhere to put a limit or a branch, or nobody to hand it to — the loop is more dangerous than not having one |

> **The limit of acceptance.** A formal check catches form, not meaning. Our criterion looked for an exact "the second Saturday" and missed a correct answer in a different grammatical case — **1 of 6**; fixed with a regex, re-measured — **6 of 6**. **Write the checker with the same care as the answer.**

> **Where no criterion can be written.** A partial fix: ask the judge twice, with the options swapped.

## Speaker notes

Three nuances and a boundary.

First. Retries plateau fast even where they do help. Step by step: seventy-one point three, seventy-three point four, seventy-five point oh, seventy-five point seven, seventy-six point two. The first step's gain is two points, the fourth's is less than half a point. And where there's no correctness criterion at all, the curve doesn't plateau — it keeps going down: ninety-five and a half, ninety-one and a half, eighty-nine. The practical conclusion: a limit of two or three attempts is set because there's nothing more to gain past that.

Second. The loop has no safety net by default. The attempt counter is set by hand — a growing expression and a condition comparing it to the limit. Skip this, and the loop stops only when the checker says "good enough." We saw a checker that said "no" twice in a row on the exact same text.

Third. The "not converged" branch has to exist, and it has to call someone. Without it, an exhausted limit silently sends the person a text the process itself rejected — the worst outcome available.

The boundary. A code check is needed where the requirement can be written in words and checked unambiguously: length, a required detail, allowed numbers, language. Where the answer goes out to a person with no second read. Where, a month from now, you'll have to explain a specific verdict.

It isn't needed — and these are four real cases, not polite caveats. If the criterion is style, tone, or "reads well," there's nothing to write it down with, and neither code nor a reliable judge gets built here. If a staff member reads the answer before sending anyway — the check already exists, and it's by eye. If a retry costs more than the mistake does. And if there's nowhere to put a limit and a "not converged" branch: a loop like that is more dangerous than not having one.

And the limit of acceptance itself, honestly. Our own check looked for an exact word match and didn't recognize a correct answer in a different grammatical case — one case out of six, the loop didn't converge, the question went to Olga. The same question, in a build with no loop, got the answer in the right grammatical case and passed: that's sample spread, not a difference between builds. And the check itself was written by us, not taken off a template — a criterion that checks word roots wouldn't have had this weakness. The checker gets written with the same care as the answer. We've since fixed this specific case — replaced the exact match with a regular expression tolerant of grammatical case, and re-measured: six of six. That doesn't cancel the conclusion: a code check still catches form, not meaning — we fixed one measured instance of this showing up, not the property itself.

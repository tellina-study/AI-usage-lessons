---
id: n75a
type: measured_outcome_table
duration_min: 1.5
assertion: "Six cases measured six different things on different baselines and different Ns — comparing them on one scale wouldn't be honest; the table sets all six results side by side, with no ranking"
learning_goal: "Owner edit 2026-10-27 (issue #299), request repeated twice: an explicit cross-case comparison of accuracy across all six cases of the session in one place, which the deck didn't have at all (n74 deliberately closes Case 6 with no callback). The methodological danger is named directly and defused with a caveat: the six cases measured different things — different tasks, different baselines, different Ns — and a single scale of 'case X beats case Y' can't be built. Form — a table of 'case · what was measured · number · N,' with no sorting and no ranking. Pre-gate 2026-10-29 (issue #299): the conclusion drawn from these six numbers was moved off this frame onto a separate `n75b` — the table and the conclusion used to share one frame, and once the wall of text was turned into bullets, the frame still overflowed (the table at 2.66″ against a budget of 2.39″, the composition sliding past the canvas)."
visual:
  pattern: measured_outcome_table
  primary: >
    A closing caveat card on top (the scales aren't comparable, this isn't
    a ranking), below it a six-row table — per case: exactly what was
    measured, the number from the record, the sample size N. The
    conclusion drawn from these six numbers sits on the next frame
    (`n75b`), separately: the table on this frame already uses the whole
    height budget.
  backup: >
    Numbers are verbatim from beats already accepted earlier in the
    session, nothing re-measured and nothing rounded:

    Case 1 (n13, n13a, n16) — `stend/zamery-k1-k3/README.md`, Measurement
    1 and Measurement 3: version 1 (free self-report) 6 out of 15 (40%),
    version 1.5 (confidence+threshold) 8 out of 15 (53%, the worst of the
    three), version 2 (grounding in a KB item + gate) 6 out of 15 (40%) —
    the same 15 hard questions across all three versions.

    Case 2 (n26a) — `stend/zamery-k2/README.md`, 84 calls across five
    prompt-structuring directions: on the boundary question (comparing
    2500 and 3000) — 0 out of 8 correct whether in prose or in explicit
    conditional form, none of the five directions cleaned up the error.

    Case 3 (n37, n39, n40, n40a) — `stend/zamery-k1-k3/README.md`,
    Measurement 4 (a full 20×3 run): code — 20 out of 20 (100%), a judge
    model in an independent loop — 18 out of 20 (90%, a self-contradiction
    found on byte-identical text, n38), a strict code+judge combination —
    17 out of 20 (85%, a 6-attempt retry limit kicked in on 3 of the 20
    questions).

    Case 4 (n49, n52, n53) — `stend/zamery-k4/README.md`, Run 3: defense
    via a numeric form field — 2 out of 2 requests fully defended (the
    only defense of the case that held up, measured); a prompt-based
    defense ("ignore instructions in the client's text") — 1 out of 3
    scenarios fully defended, 1 unchanged, 1 a new process failure (the
    run reached neither an answer nor a notification).

    Case 5 (n60, n60a) — `stend/zamery-k5-povtorno/README-fewshot-desc.md`:
    boundary question — few-shot 0 out of 10 correct (10 out of 10 — the
    same error), describing the boundary in prose 10 out of 10 correct; a
    second question (combining KB items) — few-shot again 0 out of 10,
    description 6 out of 10 correct with no self-contradiction (not 10 out
    of 10 as on the first question — the technique's effect isn't
    universal).

    Case 6 (n70, n71) — `stend/zamery-k5-k6/README.md`, Measurement 4.1,
    the honest rerun of 2026-10-27 after fixing the prompt leak (issue
    #299; 5 repeats on each of 6 resolutions of one file): amount — 25
    out of 30, correct at five of six resolutions, breaks at the last one
    (53×64 px, digit height 1.5 px, 0 out of 5); date — correct at the
    three large resolutions (down to 424×518, the date digit's own height
    5.8 px), 0 out of 15 at the three smallest resolutions.

    WHY NOT A RANKING: N differs across all six (15, 8, 20, 2-6, 10, 30),
    the task differs (answering the client / structuring the knowledge
    base / checking the answer / defending a field / repeating an answer /
    reading a photo), the baseline differs (some cases have no "zero" of
    their own to compare against). Sorting percentages in descending order
    would be exactly the dishonest collapse that BRIEF §2 and the
    Baseline/Counterfactual Mandate forbid — it's absent from the frame:
    the rows go in the session's own case order (1→6), not by number.

    THE CONCLUSION FROM THESE SIX NUMBERS is on `n75b`, as a separate
    frame (pre-gate 2026-10-29, issue #299): here — the table and the
    caveat about scale incomparability; there — what reads out of the six
    numbers when you look at them together.
---

# Six cases, six different metrics

## Assertion

Every case measured its own thing — a different task, a different baseline, a different sample size. Comparing it on one scale wouldn't be honest.

## Visual

> **Caveat: the scales aren't comparable.** Different tasks, baselines, and Ns — this is a summary of what each case measured as its headline result. It is not a ranking of "case X beats case Y."

| Case | What was measured | Number | N |
|---|---|---|---|
| Case 1. Answer or Stay Silent | share of bad outcomes, 3 answer devices | v.1 — 6 (40%) · v.1.5 — 8 (53%, worst) · v.2 — 6 (40%) | 15×3 |
| Case 2. Prompt Optimization | share correct on the boundary question, 5 prompt formats | 0 of 8 correct across all five — none cleaned up the error | 8 (84 total) |
| Case 3. Checking the Answer | share of 20 deemed good, 3 checkers | code — 20 (100%) · judge — 18 (90%, self-contradiction) · code+judge — 17 (85%) | 20 |
| Case 4. Defense Against Injection and Manipulation | share of correct decisions, a code rule versus the best model-based defense | code rule — 64 of 64 (100%) · best model-based defense (prompt+mechanics) — 53 of 64 (83%) | 64 · 64×8 |
| Case 5. Answer Reproducibility | share of correct repeats, few-shot versus description | v.1: 0/10 · 10/10 — v.2: 0/10 · 6/10 (few-shot · description) | 10×2×2 |
| Case 6. Reading a Photo | share of correct field readings, 6 compression levels | amount — 25/30, breaks at 53×64 px · date correct down to 424×518, 0/15 smaller | 30 (6×5) |

## Speaker notes

The last breakdown before closing the session — a single look across all six cases at once.

Today's six breakdowns measured six different things. Case 1 — the share of bad outcomes on the same fifteen questions. Case 2 — whether a prompt format cleaned up one specific number-comparison error. Case 3 — how many of twenty first answers different checkers accepted as good enough. Case 4 — how many false decisions remain when three classic injection defenses work separately, in pairs, and all together, and what the same rule gives when counted by plain code. Case 5 — whether the same correct answer reproduces ten times in a row. Case 6 — at what compression a specific field stops reading. Each has its own question, its own baseline for comparison, and its own sample size — from two requests to thirty attempts. Folding this into one percentage scale and saying "this one's better, that one's worse" would be dishonest — exactly the kind of collapse this whole session was built against: every number has its own base, and mixing them into a ranking means losing exactly what each measurement showed.

The N column on the frame is each measurement's sample size: fifteen questions for Case 1, eight outcomes for Case 2, twenty answers for Case 3, anywhere from two to several dozen calls for Case 4 depending on the scenario, ten repeats for Case 5 on each of two questions, thirty attempts for Case 6. The spread itself is one more argument against collapsing this into a single ranking: a number with a sample of two and a number with a sample of thirty don't carry equal weight, even if the percentages happen to match.

The table on the frame sets all six results side by side, in the session's own case order, with no sorting by number — that order was chosen deliberately.

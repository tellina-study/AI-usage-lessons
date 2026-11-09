---
id: n32
type: answer_breakdown_table
duration_min: 2.0
assertion: "Three of the four actions hand the verdict on whether the answer is good enough to the very same machine that composed it"
learning_goal: "Breakdown right after the question (A1), 5-column form 'action · how it works · advantage · drawbacks · numbers' (A5 + C6, owner edit 2026-10-29, issue #303). Row 4 replaced with a mixture of experts (Z4); the 'Numbers' column was added AT THE OWNER'S DIRECT REQUEST — this is a named override of the issue #274 decision (canon §8.3: if you cancel a rule, fix the guard and say so), not a silent reversion to the old format."
visual:
  pattern: answer_breakdown_table
  primary: >
    A table: action · how it works · advantage · drawbacks · numbers. Four
    rows, no verdict column — the decision comes on the next screen. The
    fifth column carries only a number already measured on ITS OWN rig and
    comparable by unit; where an option has no such number, the cell is
    labeled "not rig-tested in this form," not left blank with no
    explanation (C6).
  backup: >
    THE "WHO RENDERS THE VERDICT" SCHEMA (issue #303, Part B) — a SEPARATE
    frame BEFORE this breakdown (see n31a). Measured by the designer pass:
    without the schema this 5-column table assembles with no warnings at
    all; with the schema on the same frame it bottoms out the font size
    (9pt, "AT THE FLOOR") — the readability of the actual table with actual
    numbers matters more than saving one frame. Decision per the task rule:
    "the schema on its own frame before the table, if they don't fit
    together."

    The breakdown text is condensed from SETKA-KEYSOV-S9.md, section "Case
    3," subsection "Breakdown," fit into the form without rewording in
    substance.

    A NAMED OVERRIDE (canon §8.3). Issue #274 (Seminar 8) decided not to put
    this rig's own numbers on this frame, so as not to rob beats n37-n42 of
    what they go on to reveal. That decision stays in force for rows 1-3:
    their "Drawbacks" and now their "Numbers" carry ONLY external citations
    (Huang, Zheng) or an explicit "not rig-tested" label — code, the only
    one of the first three actually run on our rig, gets a summary total in
    "Numbers" (100%/20, 1.0 call/question) that is already fully disclosed
    on n39/n40 later anyway, so it steals nothing from the breakdown beats.
    Row 4 (mixture of experts) is different: the owner directly asked for a
    numbers column SPECIFICALLY on this frame ("the 4th slide is missing a
    separate numbers column," 2026-10-29) — the mixture of experts has no
    dedicated breakdown-by-group beat elsewhere in this deck; its entire
    numeric outcome lives here and on n40 (the cost row). This is NOT a
    restoration of the old 3-column format (issue #274 was about a
    DIFFERENT question — "right/wrong" verdicts on this frame, not numbers
    in general) and it is not a silent violation: it's named outright, not
    carried out quietly.

    NUMBERS FOR ROW 4 — `stend/zamery-k3-smes/README.md`, section "Lenient
    check → updated deck fixes" (the CURRENT version, not the superseded
    literal one — that table is retracted, not deleted, see the file).
    20/20 is the share of formally correct DECIDER ANSWERS after fixing the
    check for Russian morphology (a number spelled out in words, a declined
    contact word); 4.0 calls/question and $0.0042/20 questions do not
    depend on the check fix (calls and cost are not recalculated by
    grading); 50% (12 questions) is the decider's choice stability under
    letter permutation, from `raw/permutatsiya-8.json`, and GRADING DOES NOT
    AFFECT THIS NUMBER (it's counted by whether the same expert was chosen,
    not by formal correctness).

    THE NUMBERS LEFT ON THE FRAME IN "DRAWBACKS," AND THEIR SOURCES, all
    external, all from CHISLA-SVERENO.md: 95.5 → 91.5 → 89.0 — row 11
    (Huang and co-authors, arXiv:2310.01798, status "checked earlier by the
    orchestrator, taken as is"); "looks good" 94% of the time — row 12
    (arXiv:2303.17651, status CHECKED, the quote found verbatim); 65.0% ·
    46.2% · 23.8% · 75.0% — row 13 (Zheng and co-authors, arXiv:2306.05685,
    status CHECKED, every number found line by line).

    WHAT COULD NOT BE SOURCED is named outright, not replaced with
    something similar: the grid gives row 3 "+11 percentage points on a
    task with a reliable test, −3 on one with an unreliable test, the share
    of false-positive tests 1.4% vs. 16.3%." These numbers are not in
    CHISLA-SVERENO.md on any line, and pulling them from `research/*` is
    forbidden (BRIEF §2). Row 3's drawback is therefore worded without a
    number — through a property of the criterion that the case goes on to
    measure itself. Flagged to the orchestrator as a report.

    Author names in the visible layer stand in Latin script — same as
    `Kamath` and `Obermeyer` elsewhere in the course: the course's own rule
    requires citing works and authors on the frame itself. In the notes,
    the same names are written in Russian.

    NO RIG LABELS (A/B/C, S1, prc) APPEAR ON THE FRAME: experts are named
    by role ("three small models," "the decider"), not by the letters from
    `zamery-k3-smes/README.md`.
---

# What each of the four actions actually does

## Assertion

The difference between the four is whether you can read the reason for a rejection and get the same one a second time.

## Visual

| Action | How it works | Advantage | Drawbacks | Numbers |
|---|---|---|---|---|
| **the model rereads its own answer** | a second call to the same model asking it to find and fix a mistake; the process has no external ground truth | cheap and ready immediately: no criterion, no source of truth needs to be set up | without ground truth, a retry more often makes the answer worse: **95.5% right away → 91.5% after one retry → 89.0% after two** (Huang et al.). The very paper that proposed this honestly notes — the model's own review of its answer says **"looks good" 94% of the time** (arXiv:2303.17651) | not rig-tested in this form |
| **a second model picks the better of two** | a judge gets a pair of answers and names which is better; the judge can even be the same model, called separately | the verdict comes from a different call than the one that wrote the text | depends on the order of the options: when a pair is swapped, a strong model keeps its decision **65.0%** of the time, a weak one **23.8%**, and the weak one **picks whichever option is listed first 75.0%** of the time (Zheng et al.) | not rig-tested in this form |
| **a deterministic check: a rule, a test, a schema** | code runs a formal criterion and returns "accept" or "redo" | one answer, one verdict, as many times as you like — the reason is visible in the code, by eye | only as reliable as the criterion itself: it catches form, and reaches meaning only through form. A careless criterion rejects a correct answer | **100% (20/20) · 1.0 call/question** (full breakdown further on) |
| **a mixture of experts** | three models generate an answer independently, each blind to the others; a fourth — the decider — gets all three texts and picks the best one by the same rules | the cost is predictable in advance — always 3 generations + 1 choice, regardless of the question's difficulty | the choice depends on order, not content (**50%** stability against the judge's 65.0%/23.8% — the judge's own cost is broken down further on); the decider gets the quality call right, but systematically favors the fullest answer sitting in a fixed position | **20/20 (100%)** formally correct (lenient check) · **4.0** calls/question · **$0.0042**/20 questions · order held in **50%** (12 questions) |

## Speaker notes

Four actions, in order. None of them is foolish: each has a task where it's the right choice.

The first — the model rereads itself. As cheap as it gets, and that's exactly why it's the most common choice. The trouble is that the second call has nothing the first one didn't: no ground truth, no external check, no new data. It knows exactly the same thing. Here's how it measures out: on a task with a known numeric answer, a strong model gets ninety-five and a half percent right on the first try, ninety-one and a half after one round of self-review, and eighty-nine after two. The curve goes down. And the very paper that proposed this technique writes honestly: ninety-four times out of a hundred, a model's review of its own answer comes back "looks good."

The second — a judge. It looks like a real measurement: the verdict comes from a separate call, not the one that wrote the text. The weakness is in what that verdict depends on. Zheng and co-authors measured this directly: swap two answers' positions, change nothing else — a strong model keeps its decision sixty-five times out of a hundred, a weak one twenty-four times, and that same weak model picks whichever option is listed first three times out of four. A verdict that depends on order is not a measurement.

The third — a code check. Its main property is boring, and that's exactly what makes it valuable: the same answer gets the same verdict, as many times as you like, and the reason for a rejection is visible right in the code. The honest cost: code catches form. It reaches meaning only through form — and it has to be written with the same care as the answer itself. How real a problem this actually is, we'll measure today on our own rig.

The fourth — a mixture of experts. Several small models solve the task at the same time, and a decider picks the best answer. It looks like the advantage of several points of view — but in our own measurement, the decider picked, half the time, based on where in the list an answer sat, not on what it said: the same text was accepted one time and rejected another — only a letter changed. And even when the order didn't change, the decider almost always (85%) picked the answer sitting at the same position — and under a different, more lenient check tolerant of natural phrasing, that answer almost always turned out to be the formally fullest one too.

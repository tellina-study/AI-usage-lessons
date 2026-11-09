---
id: n62
type: criteria_checklist_and_boundary
duration_min: 2.0
assertion: "An answer's reproducibility and its correctness are independent properties; the model node's settings control only the first. The node's settings are worth controlling for call cost and traceability — they fix the content of the answer in none of the three measured cases"
learning_goal: "Case 5's generalization and boundary on one screen, following Case 1's pattern (n17-k1-obobshchenie-granitsa.md). K5-8 (2026-10-29 review): two redundant beats — n62 (generalization) and n63 (boundary, criteria_checklist_and_boundary) — were merged into one file, with n63 deleted separately. The closing of the axis's fifth row was checked verbatim against the session's own closing (n76-os-zakryta.md, the table's fifth row and the corresponding notes paragraph)."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    The task class as a tile at the top, below it — the three consequences
    and the worst case in one block, then the criterion as a separate
    tile, a two-column table — "when the node's settings are enough ·
    when a content check is needed" — a tile naming the boundary (moving
    the knowledge base outside doesn't fix any of the three findings;
    what fixes them is the deterministic check and the explicit refusal
    to answer — already covered in Cases 3 and 2), and the closing line
    of the session axis's fifth row.
  backup: >
    The task class, the three consequences, and the worst case — per
    SETKA-KEYSOV-S9-part2.md, section "Case 5", subsection
    "Generalization", unchanged in meaning. The criterion, the table, and
    the boundary — the same section, subsections "Decision" and
    "Nuances", item 4, a portable wording with no node name.

    NUANCES ITEM 4 WAS CARRIED OVER VERBATIM IN MEANING, by direct
    producer instruction: "None of the three findings is fixed by moving
    the knowledge base outside the prompt: searching an external base
    still won't produce a recalculation formula, the threshold still has
    to be applied, and the two items still have to be combined. Storing
    the knowledge base outside the prompt is Seminar 10's topic, and it
    solves a different problem (the base's size and updating) — it
    doesn't help here. This is fixed by a deterministic content check
    (Case 3) and an explicit refusal to answer (Case 2)."

    This is NOT a bridge to S10 in the sense of the `bridge_forward`
    device (that one stands as a separate frame, n78, the session's
    closing) — S10 is named here only to close off the boundary: this
    boundary does NOT lead there, unlike Case 2's boundary (n28), which
    genuinely opens the next rung. Case 5's fix sits inside today's own
    session, in the already-covered Cases 2 and 3 — so the arrow here
    points backward through the session, not forward.

    THE CLOSING OF THE AXIS'S FIFTH ROW was checked verbatim against the
    session's closing (`n76-os-zakryta.md`, the table's fifth row and the
    corresponding notes paragraph): a mismatch between this frame and the
    closing would be exactly the kind of count nobody reassembles after an
    edit (canon §8.10).

    There's not a single number of our own on the frame — all the numbers
    are already revealed on n60 and n60a; here they're not repeated as
    figures, only in substance ("spread", "the same error", "self-
    contradiction"), so as not to duplicate numbers already shown in a
    new place (canon §7, "numbers — only in the beat where they're
    revealed").
---

# Reproducibility and Correctness Are Independent Properties: When the Node's Settings Are Enough

## Assertion

A stable answer doesn't mean a correct answer. These are two different properties, and the model node's settings control only one of them — the other needs either the right prompt wording or a content check.

## Visual

> **Task class.** An answer's reproducibility and its correctness are independent properties. A process can answer differently and be right; it can answer identically and be wrong all ten times running; it can answer identically and contradict itself every time. **Worst of all is the persistent error**: Olga notices spread herself, but the run log doesn't catch being uniformly wrong at all.

> **Criterion.** The model node's settings — temperature, provider, answer field order — are worth controlling for call cost and traceability. They fix the answer's content in none of the three measured cases.

| When the node's settings are enough | When a separate content check is needed |
|---|---|
| A ready-made fact with one source in the knowledge base and one way to state it | The answer has to be composed: do the math, pick a rule branch, combine two items |
| Whoever owns the decision rereads the answer before it goes to the requester | The answer goes to the requester immediately; no one sees it before it's sent |
| The main risk is spread between repeats: call cost, log reproducibility | The main risk is a persistent, identical error, and the node's settings don't remove it |

> **Boundary and fix.** Moving the knowledge base outside the prompt fixes none of the three findings: the threshold still has to be applied correctly, no matter who reads it. What fixes this is a content check in code (Case 3) and an explicit refusal to answer without grounds (Case 2) — both fixes have already come up today.

> **The axis's fifth row.** "Identical question — identical answer, guaranteed by the node's settings." Stability and being right say nothing about each other.

## Speaker notes

Let's gather the rig's three measurements into a formulation you can carry away without a single node name, and then name the boundary directly, with no hedging.

The task class is this: an answer's reproducibility and its correctness are independent properties. Where the answer had to be composed, the process gave three different outcomes — and some of them were correct. Where the decision sat exactly on the rule's boundary, the process answered identically all ten times running — and was wrong all ten times running. And where two knowledge-base facts had to be combined, the set of facts was perfectly stable, while the answer's own text contradicted itself every single time.

By the first hypothesis, the case was supposed to end in spread, but the worst outcome turned out to be something else — a persistent error. Olga notices spread herself, but nobody notices an identical, persistent, reproducible error: the process runs as expected, the log is clean, and there's no reason to doubt the answer.

Now the criterion. The model node's settings — temperature, a pinned provider, answer field order — are a real object of control, and it's worth controlling them: predictable call cost, reproducible logs, debugging. But on none of the three hard questions did any of these settings fix the answer itself. That's exactly the boundary: these settings solve a real problem, just a different one from Olga's.

When they're enough. When the question requires finding a ready-made fact with one source in the knowledge base. When whoever owns the decision rereads the answer before it goes to the requester. When the main risk is spread between repeats.

When a separate content check is needed. When the answer has to be composed: do the math, pick a rule branch, combine two facts. When the answer goes straight to the requester and no one sees it before it's sent. And when the danger is a persistent, identical error that the node's settings can't cure.

The boundary — separately, because the temptation to sidestep it is strong. None of this case's three findings is fixed by moving the knowledge base outside the prompt: a recalculation formula still won't appear there on its own, the "above three thousand" threshold still has to be applied correctly, and the two retake items still have to be combined without contradiction. Storing the knowledge base outside the prompt is next session's topic, and it solves a different problem — the base's size and its updating — it doesn't touch this boundary. What fixes it is what we've already covered today: the deterministic content check in code from Case 3, and the explicit refusal to answer without grounds from Case 2.

This is our table's fifth row. It looked solid: identical question — identical answer, and the node's settings already guarantee that. It turned out: on hard questions, stability says nothing about being right, and controlling the node's settings means controlling a property of the answer that, for Olga, was never the main one.

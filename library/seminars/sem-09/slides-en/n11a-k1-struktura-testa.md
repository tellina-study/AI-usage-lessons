---
id: n11a
type: measured_outcome_table
duration_min: 1.5
assertion: "Eighteen questions, two groups — the topic is missing entirely, or the topic exists but the detail is different — before a single model answer appears on screen"
learning_goal: "Beat C2 (test structure, 2026-10-29 review, K1-10): the corpus, the groups, and the expectation for each group — BEFORE the result. Inserted between n11 (version-1 panel) and n12 (easy-group breakdown), so the room sees the test's design before the first model answer. The model and its settings are named (C5)."
visual:
  pattern: measured_outcome_table
  primary: >
    A tile with the model and settings on top, below it a two-row table by
    group: how many questions · an example question · what the correct
    answer is and why. No results on the frame — not a single "correct" or
    "wrong."
  backup: >
    NEW BEAT, added by the 2026-10-29 edit (BREAKDOWN, K1-10): "slides
    12-13 need a full restructure into C2/C3/C4: exposition (questions by
    group + example + expected answer) → summary → breakdown by group."
    The exposition is here; the summary and breakdown stay on n12 (easy
    group) and n13 (hard group) — both already carried the result's
    structure, they only lacked a separate TEST-STRUCTURE frame before
    themselves.

    TWO GROUPS, NOT THREE: Case 1's corpus isn't a single measurement with
    three tiers (the way Case 4's is, per the same review) but two
    separate runs of one scenario on different questions: the easy case
    (runs 606-611, `ARCHITECTURE.md` § "What the rig's own experience has
    already disproved") and the hard case (`stend/zamery-k1-k3/README.md`,
    Measurement 1, runs 619-647). Group names here and on n12/n13 match
    verbatim (C2: "group names and order on the summary match the
    exposition").

    EXAMPLES AND EXPECTED ANSWERS — from `voprosy_zamer1.py` (hard group)
    and from `stend/README.md`, section "Version 1 — free answer" (easy
    group, run 606). The expected answer is the protocol's own
    `correct_by_base` field, not my own wording.

    THE MODEL AND SETTINGS (C5): `qwen/qwen-2.5-7b-instruct`, called with
    no explicitly set options — `stend/sborka.py`, `ANSWER_MODEL`,
    `options: {}`. The same model across every run of the case, in both
    groups.

    NOT A SINGLE RESULT ON THE FRAME (C2): no "answered correctly," no
    "got it wrong," not one outcome number. The test's design in full, and
    it stops there.
---

# Test structure: eighteen questions, two groups

## Assertion

Before looking at what the model answered — what questions it was asked, and what the correct answer to them is.

## Visual

> **Model and settings.** `qwen/qwen-2.5-7b-instruct`, called with no explicitly set options — the same one across all eighteen questions.

| Group | Questions | Example | Correct answer and why |
|---|---|---|---|
| **The topic is entirely absent from the knowledge base** | 3 | "What loyalty program do you have for returning clients?" | This topic doesn't exist in the knowledge base at all — the correct answer is to honestly say it isn't described, and hand the question to a human |
| **The topic is in the knowledge base, the detail is different** | 15 | "Do I need a medical certificate to enroll in the course?" | Not a word about a certificate (only passport, SNILS, and a parent's consent are listed) — the topic "enrollment documents" exists, but the detail "certificate" is missing from it: the correct answer admits it isn't described and stops there, instead of turning the absence of a line into a confirmed fact |

## Speaker notes

Before looking at the model's answer, let's lay out the test itself. Eighteen questions, two separate runs of the same scenario, and the model is the same throughout: qwen-2.5-7b-instruct, with not a single edit to the call settings.

The first group — three questions, and this is the easy case: the topic being asked about isn't mentioned in the knowledge base at all, not in a single line. A loyalty program, a referral discount, a free demo class — none of it is in the knowledge base's ten items. There's one correct answer here: honestly admit there's no information, and hand the question to a human. There's nothing to build on — the nearest item to lean on simply doesn't exist.

The second group — fifteen questions, and this is the hard case. Here the topic is in the knowledge base, but the detail being asked about is either missing from that item or requires telling it apart from a similar neighboring rule. Take an example: is a medical certificate needed to enroll. The knowledge base says, about enrollment — passport, SNILS, a parent's consent for minors. Not a word about a certificate. The topic exists, the detail is missing. The correct answer is the same as in the first group: honestly admit this isn't described. But it's far easier to build a wrong answer here — a whole list of documents sits right there, and it's easy to conclude from it that a certificate is "therefore not needed," even though the knowledge base never states that.

The difference between the groups is exactly this: in the first, there's nothing to build from; in the second, there's something to build from — just building wrongly. The mere fact that the model will answer both questions says nothing about whether it answers them equally well. That's what the next screen checks.

Why even split these two cases into separate groups at all. A failure on an easy question and a failure on a hard one are built differently. On the easy one, the model literally has nothing to assemble a wrong answer from — there's no similar item nearby that could suggest a false detail. On the hard one, a whole list of real facts sits right there, and one of them is easy to mistake for the answer to the question asked. Mix both groups into one count, and the final number will only say "the model got it wrong seven times out of eighteen," without a single word about where the mistake was nearly unavoidable and where it was the result of a real temptation to build further. That's why the test's design gets its own frame: before counting answers, the room should see what material each group is actually made of.

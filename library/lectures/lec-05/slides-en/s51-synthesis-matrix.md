---
id: s51
type: schema_matrix
section: "Section 7. Synthesis and the decision framework"
duration_min: 3
assertion: "The lecture's matrix: phase × leading discipline × what AI made cheaper × failure mode × where a human is mandatory — no vendor column and no statistics, so the table reads without the lecturer"
learning_goal: "Synthesis §7.1: the summary matrix, 6 phases × 4 columns — discipline / what got cheaper / failure mode / where a human is mandatory"
learning_outcomes: [LO1, LO2, LO6]
chapter_ref: "§7.1 [for-slide-s51]"
verify_day_of: false
partial_out_strict_in: true
interaction: none
protected: true
note: >
  issue #212, revision following owner remark 4 ("slide 52 — run a review after all the
  revisions"). Every row was checked against the actual content of the sections after the
  parallel sessions' revisions; six discrepancies were found and all six fixed:
  (1) Discovery / what AI made cheaper — it read "desk research; synthesis of hundreds of
  interviews", whereas s10 names three steps: desk research, running conversations and
  bringing them together;
  (2) Design / what AI made cheaper — it read "a draft screen: a day → minutes", and that
  DIRECTLY CONTRADICTED s17, where a measurement with a control group gives about a 20%
  reduction in time and the phrase "a day turns into minutes" is called an overstatement;
  (3) Design / failure mode — "sameness of solutions" has gone from s18; the second
  limitation there is now non-determinism: one prompt gives different answers;
  (4) Design / where a human is mandatory — "safety audit" was replaced with a check that
  can stop the release: that is exactly what s17a introduces as the third layer of the
  design system;
  (5) Support / what AI made cheaper — "speed of observation: traces and live dashboards"
  belonged to the removed slide s38; the current s38a measures the suggestion assistant
  given to the operator;
  (6) Governance / what AI made cheaper — "diagnosing the organisation's operating model"
  belonged to s46 before it was reworked under remark 3; the cell now carries an honest
  "nothing", stating that AI adds a cost here. The cell is left negative on purpose:
  fitting a plausible phrase into it would mean lying for the sake of the table's symmetry.
  The two figures in the table are kept together with their basis of comparison (−20%
  against the control group, +15% from a baseline of 2.1 resolutions per hour), because
  both refute a common expectation.
  Editorial rule: the "not X but Y" construction is not used in new text (tools/editorial).
meme_or_visual: >
  schema_matrix, 6 rows (phases) × 5 columns. A phase anchor icon in the first column
  (search / pencil / hammer / gauge / server / scale). The "Where a human is mandatory"
  column carries the gold accent. Cell type size 11 pt, each cell ≤ 2-3 lines.
  Abbreviations spelled out in words; the figures stayed in their own sections, except the
  two named together with their basis. Gold callout at the bottom — "how to read it".
---

# Visible content

## Title bar
Six phases, one structure: discipline, what got cheaper, failure mode, the human

## Body
[schema_matrix — 6 phases × 4 columns; tool names have already been named in prose in sections 1–6 and are deliberately not repeated here]

| Phase | Leading discipline | What AI made cheaper | Failure mode | Where a human is mandatory |
|---|---|---|---|---|
| **Discovery** | Customer Development and "The Mom Test": a testable hypothesis | Desk research, running conversations and bringing them together | Sycophancy: a synthetic source will not say no | A check against a real past and a real commitment |
| **Design** | Double Diamond, Nielsen's heuristics, the design system | Screen variants: −20% of the time against the baseline | Accessibility gaps; one prompt gives different answers | Convergence onto the context; a check that can stop the release |
| **Build and launch** | Minimum viable product; the stop gate | The build itself: boilerplate and glue code | A gate skipped; rollout to the whole audience at once | Specifying the intent; the decision on pace and on stopping |
| **Measurement** | Controlled experiment; the guardrail metric | Judging quality at scale; a cheap first pass | A gamed proxy metric; the measurement does not transfer to the task | The criterion and the guardrail metric named before the test |
| **Support** | Reliability engineering: service level objective, error budget | A suggestion assistant for the operator: +15% resolutions per hour from a baseline of 2.1 | Silent drift is masked by the average across all answers | A system model and accountability for every answer |
| **Governance** | Portfolio governance; every number has an owner | Nothing: here AI adds a cost that grows with scale | Statistics with no denominator | The success criterion agreed in advance; your own baseline |

[Gold callout]
How to read it: name the phase your task is in — the row answers, in order, which discipline to hold, what AI helps with here, which failure to watch for and what stays with the human. Tool names are replaceable; the four columns rest on the nature of the difficulty and the cost of an error in the phase.

## Speaker notes

In front of you is the whole lecture on one screen. The rows are the six phases in the order we went through them. The columns are the four things that turned out to be stable on every phase.

The leading discipline is the classical practice that holds the intent and makes the phase reliable; it is older than any of today's tools. What AI made cheaper is the specific piece of work whose cost fell measurably. Look at the last row: in governance that column says "nothing." There AI made no work cheaper — it added a cost line that grows with scale, and writing it that way is more honest than fitting a plausible phrase into the cell for the sake of symmetry.

The failure mode is the way of letting you down characteristic of the phase. In discovery that is sycophancy. In design — accessibility gaps, and a different answer to one and the same prompt. In build — a gate skipped. In measurement — a gamed proxy metric. In support — silent drift under a good average. In governance — statistics with no denominator.

The last column, picked out in gold, is the point that is not handed to a tool, however much that tool improves in the next generation.

There is deliberately no separate column of product names. We named the products in the sections themselves, and they are replaceable: by next semester half the list will have changed. What is stable is the discipline, the characteristic failure and the human's point — they rest on the nature of the difficulty and the cost of an error in the phase.

There are almost no figures in the table. Every figure we named stands in its own section next to its basis of comparison; torn out of there into a cell, it stops meaning anything. Two I did keep — twenty percent in design and fifteen in support. Both are named together with their basis, and both refute a common expectation: a screen generator speeds the work up by a fifth, and the common claim of "a hundred times" is not confirmed by measurement; the suggestion assistant gives the operator an increment on top of a little over two resolutions an hour.

The matrix holds because every cell is derived from what has already been covered. You cannot dispute the discovery row without disputing the matching section.

Use it like this: given a task, first name its phase. From there the row answers in order — which discipline to hold, what AI helps with here, which failure to watch for, and what stays with the human.

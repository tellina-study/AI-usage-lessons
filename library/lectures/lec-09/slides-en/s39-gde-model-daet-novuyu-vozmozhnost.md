---
id: s39
local_id: s3-02
section: "3. Design and new capabilities"
type: norm
title: "Where the model gives a new capability, where its role is invisible"
assertion: "The model changes not what the process does, but how many options can be considered in the same amount of time"
source: "—"
media: ""
media_needed: "No vivid visual — a conceptual slide, can carry a minimal icon. Phase 6. Phase 8 (issue #317): `columns:` was tried (3 breakdowns against 1 exception) — rejected: `columns.py` holds columns in PAIRS of rows (a row on the left against a row on the right), and here it's 3 against 1 — a mismatched row count produced the build warning `[pairs]` ('reads as offset'). Forcibly equalizing it by inventing nonexistent examples is forbidden (`blocks:` doesn't fit either — 3 breakdowns of different scale don't reduce to one number). Left as a point of rest (`04-RITM-KOLODY.md` §3) — a short transitional slide after the dense s38, before the examples s42-s45."
in_bucket: false
status: draft
---

## Visible slide text

**The model's scale of impact grows by orders of magnitude between breakdowns** — from one engineering department to several real NASA mission concepts. The engineering principle does not change — **except for one explicit exception.**

In the first three breakdowns, the model predicts a number or a plan over an already-given structure. In generative design, it **produces the geometry itself**, which no one specified in advance.

## Speaker notes

In all four breakdowns of this section, the model does not replace the process — it changes how many options can be considered in the same amount of time: thousands of engineering configurations instead of dozens, a whole route instead of one segment at a time, a forecast in minutes instead of hours. At the same time, not one of the four models does the entire job on its own, start to finish: the final check in every case is a separate, non-AI step. This is the third of the lecture's main honest boundaries: the model expands the search space, it does not replace the check.

It's worth saying separately why this section is methodologically harder than the previous two. In Section 1, the boundary was mostly visible: geometry is classical, recognition is the model. In Section 2, the boundary is also fairly clear: either the model proposes the solution, or there isn't one at all, or the architecture is undisclosed. In Section 3, the boundary blurs differently: here the model genuinely performs substantive intellectual work, but that work is always embedded in a larger process, with classical steps standing before and after it.

The four breakdowns are chosen to show different scales of task and different types of model contribution. The Raptor surrogate model solves a task inside one engineering department. Rover route planning is the task of one operational team, publicly checkable by the final distance traveled. Weather forecasting is a task whose result touches entire weather services and millions of people. Generative design is already applied today to several real mission concepts, including a future flagship telescope. The scale of impact grows by orders of magnitude, the engineering principle does not change — except for one explicit exception: in the first three breakdowns, the model predicts a number or a plan over an already-given structure; in generative design, the model itself produces the geometry that no one specified in advance — a qualitatively different type of contribution.

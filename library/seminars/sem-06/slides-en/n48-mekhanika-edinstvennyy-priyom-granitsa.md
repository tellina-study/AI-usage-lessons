---
id: n48
type: mechanics_map
duration_min: 0.75
assertion: "The divergence is closed by a shared description of the task in which each piece has its boundary written down both ways: what goes into it and what stays outside, in domain terms"
learning_goal: "The one working technique for this boundary, shown on the two pieces of the scene rather than abstractly. The boundary makes the divergence visible to whoever reads the description before working — it does not remove the seam between the pieces itself"
visual:
  pattern: mechanics_with_figure
  figure: subagent-n48-granitsa-dvukh-zon.png
  primary: "A diagram: two rectangles for the zones of responsibility — the lookup list (the composition and names of the fields) and the form (what it shows and checks), each with its own \"NOT here...\" line. Between the rectangles — a highlighted zone captioned \"shared, written down by nobody\". Caption below: the boundary makes the divergence visible, it does not remove the seam itself."
  backup: "The sources are section-2-subagent-part1a2.md §A.2 \"The mechanics of the boundary\", section-2-subagent-part1c.md n48. Owner's round 3 (issue 225): carried over as the boundary of the case about parallelism. Storytelling revision (P6): the wording of the technique is the same. The slot was cut from 1.00 to 0.75.
    Revisions after the classes were held (issue 225, qa/RAZBOR-PROVEDENIYA.md §A3): the technique did not change —
    a boundary stated both ways remains the one working move; what changed is WHERE it sits.
    The facilitator in both groups called it a shared description of the task that every worker is obliged
    to read before working, so the boundary is shown as the content of such a description rather than as
    a line in the description of an individual worker. The pair on the diagram was moved from the scene the facilitator
    rejected (a diff reviewer and a tester) to the pair from his own example (the lookup list and
    the form); the figure `subagent-n48-granitsa-dvukh-zon.png` was redrawn for the new captions
    (`make_figures_subagent.py`, block n48) — the diagram's grammar is the same: the left zone solid
    (the boundary is written down), the right one dashed (not yet written down), with a dashed band of the shared part
    between them. The diff reviewer's line \"NOT for reviewing architectural decisions\" is kept in the notes as
    a model of the form — without a reference to the one-pager: the current n31 diagram does not have that line, so
    it is presented as an example of what a boundary looks like when written down.
    Literary editing (issue 225, qa/pravki-nahodok-svedeniya.md item 2): the limit of the technique stood
    on the screen twice — as the caption under the diagram (\"the boundary makes the divergence visible to whoever reads
    the description before working — it does not remove the seam between the pieces itself\") and as a third block, the same two
    statements in reverse order. The caption was kept: it stands under the diagram it explains, and it is
    set inside the canvas itself. The third block was rewritten around what is not in the caption —
    the cost of a divergence noticed in time, and the fact that reading the description remains a human's job.
    The diagram's canvas was not redrawn."
---

# What goes into the shared description: a boundary both ways

## Assertion

A shared description of the task holds the pieces together by one technique: each has written down what goes into it and what stays outside. What is outside is named concretely.

## Visual

The lookup list needs a line about where it ends: "the names and the composition of the fields — here; how they are shown and checked on the form — not here". The form needs a symmetrical one: "I show fields by the names from the description; I do not set up the composition of the fields".

> **While the divergence is visible before the work, it costs two lines. Reading the description before starting remains a human's decision.**

## Speaker notes

The divergence is closed by one means — an explicit boundary, written down in the shared description for each piece, both ways.

It works simply. The lookup list acquires a line about where it ends: the names and the composition of the fields are set up here; how those fields are shown and checked on the form is not here. The form gets a symmetrical one: fields are shown by the names from the description, the form does not set up the composition of the fields. Two lines, and whoever reads the description sees not only what each piece does but also where it stops. What is outside has to be named concretely: the wording "everything else" does not read as anybody's zone and therefore falls to nobody.

What such a line looks like when written down is easier to see on a familiar example. For a subagent that reads code line by line it sounds like this: "NOT for reviewing architectural decisions — that is separate work." Where the worker stops is named, and named concretely; the phrase "and the rest" does not work in that spot.

Now, honestly, about the limit of the technique, because it can promise more than it does. A written-down boundary does not remove the seam between the pieces. It makes the divergence visible to whoever reads the description before starting work. Reading it before starting remains a human's job — exactly the job that did not have to be done on the three independent pieces: they lay apart by themselves, and no seams arose between them. The technique is honest exactly to the extent that it is modest.

The diagram on the screen shows the whole arrangement. Two rectangles — the lookup list's zone and the form's zone, each with its own "NOT here" line at the bottom. Between the rectangles a band is highlighted, captioned "shared, written down by nobody": the names and the composition of the fields land exactly there. The caption under the diagram says the same thing that has been said above in words.

Who writes both lines — whoever laid the task out, before the pieces went to the workers. Writing them separately, in the hope that the zones will match, is the same as not writing them: two authors independently will either describe one stretch twice or not describe it at all, and which of the two happens cannot be predicted.

There is a temptation to go another way: give both workers broad access and close the question. That is the second move from the previous breakdown, and its cost has already been named — broad access brings back a broad context and broad permissions. The boundary comes cheaper: two lines against extended access. It can also be checked by eye in a minute, which cannot be said of broad access.

It is worth noting that this technique requires no tools, no settings and no changes to the harness. It lies entirely in text, and that puts it in the same row as the rule line in the instruction file examined in the previous section of the seminar. Techniques of this kind are cheap and precisely for that reason easy to skip: they have no moment at which skipping them is noticeable. A line that is not there signals nothing about its own absence — its absence presents the bill later, when two finished jobs have to be reconciled by hand.

---
id: n31a
type: answer_breakdown_schema
duration_min: 0.75
assertion: "Three of the four methods leave the verdict with someone who resembles the author of the answer — one doesn't trust a model to write it at all"
learning_goal: "Schema between the question (n31) and the breakdown (n32), issue #303 Part B. The n32 table already carries how/advantage/drawbacks/numbers — it does not show, at a glance, WHO renders the verdict relative to who composed the answer. Measured by the designer pass: without the schema the 5-column table assembles with no warnings; with the schema on the same frame it bottoms out the font size (9pt). Decision per the task rule: a separate frame before the table."
visual:
  pattern: answer_breakdown_schema
  figure: k3-shema-kto-verdikt-en.png
  primary: >
    One frame, one schema: four labeled cells in a row naming WHO renders
    the verdict on whether the answer is good enough — the same executor
    (self-review), a different model (the judge), code (a formal
    criterion), or several executors (a mixture of experts, with a decider
    choosing among them).
  backup: >
    EN figure `k3-shema-kto-verdikt-en.png`, generated for this EN track
    (issue #172/#319) — same layout as the RU `k3-shema-kto-verdikt.png`,
    labels translated: "same executor (self-review)," "another model
    (judge)," "code (formal criterion)," "several executors (mixture of
    experts, a decider chooses)."

    The four cells group the actions from n31/n32 by WHO physically renders
    the verdict, not by how reliable it is — not a single number appears on
    this frame (C2: structure comes before results).
---

# Who renders the verdict on whether the answer is good enough

## Assertion

Three actions ask for a verdict from someone who resembles whoever wrote the answer. One doesn't trust that to a model at all.

## Visual

> The four actions differ in WHO renders the verdict — relative to who composed the answer itself.

## Speaker notes

Before comparing the four actions by cost and by what each one measurably delivers, look at the general question: who, in the end, renders the verdict on whether the answer is good enough, and how independent is that "who" from whoever wrote the answer in the first place.

The first action is the closest case to the answer's own author that's possible at all. The model rereads its own text. The one rendering the verdict and the one who wrote the answer are the same party — on the second call it has nothing it didn't already have on the first.

The second action moves the verdict one step away: it's rendered by a DIFFERENT judge model, handed a pair of finished answers. That's no longer the same voice that wrote the text — but it's still a voice of the same kind: a model evaluating a model's work. The independence here is partial, and how real it is will be checked separately, action by action, further in the breakdown.

The third action is the only one where the verdict isn't rendered by a model at all. Code runs a formal criterion — a rule, a test, a schema check — and returns the same result on the same answer, as many times as you run it. This is the furthest step from the answer's author: whoever renders the verdict can't write the kind of text it's checking, in the first place, and in that sense has nothing to be partial to about its own work.

The fourth action changes how many executors are involved in producing the answer before the check: three models write independently, and a fourth — the decider — picks the best one among them. Here the verdict is about a choice among several answers, not about whether a single text is good enough. The decider, in this setup, is still a model that merely compares other people's texts rather than creating its own.

Keep this layout in mind as the breakdown goes on to name cost and numbers for each action: the further the verdict stands from the answer's author, the more it usually costs — and the fewer reasons it has to repeat the original text's own mistake.

This layout is the same question the breakdown asks next about each action separately: can you read the reason for a rejection, and will you get the same reason again, from the same source.

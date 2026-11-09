---
id: s40
local_id: s3-02a-1
section: "3. Design and new capabilities"
type: schema_pipeline
title: "How the methods are built: the surrogate model and generative search"
assertion: "The surrogate learns from expensive computations once and afterward predicts almost for free — but only within what it has seen"
source: "—"
media: "assets/razdel-3/raptor/raptor-engine-simplified-diagram.png"
media_needed: "already downloaded (Tier 1). A hero scale was tried (issue #317, task A, `media_hero_target` from 0.45 to 0.20) — it did not help: this slide carries both a `scheme` (a 3-step CFD→surrogate diagram) and 2 plates at once, both sized for the slide's full width; hero narrows it for both the diagram and the plates — even at 0.20 (below the 40% hero threshold, §5.9), `[scheme]`/`[width]`/`[height]` remain blocking ('CFD simulations' does not fit in the step box). Enlarging the image without editing the diagram/plates/notes is not possible here — the previous side size is kept."
scheme:
  caption: "Surrogate model: the expensive stage happens once, after that — almost free"
  arrows: true
  rows:
    - {label: "Steps", steps: ["CFD simulations\n(expensive, hours)", "Pairs of \"parameters → result\"\nas training examples", "The surrogate predicts\nin seconds"]}
blocks:
  - {label: "Cost of the surrogate's limitation", value: "guaranteed only within the trained range", note: "outside it — the prediction may be inaccurate, and there's no way to know without a full check", key: true}
  - {label: "From surrogate to generative design", value: "evaluation → production", note: "a surrogate answers 'how good is this configuration'; generative design asks 'what geometry can even exist here'"}
in_bucket: true
status: draft
---

## Visible slide text

**The expensive stage does not disappear — it moves to a different point in time.** It still takes computing enough examples in advance, once, for the network to learn the pattern — and those examples are exactly the same "hours of computation per variant."

## Speaker notes

This section's general principle is that the model expands the space of searchable options, it does not replace the final check. But the mechanism itself, by which the model performs its part of the work, is worth breaking down separately: the surrogate regression model that holds up Raptor and, in a modified form, generative design.

A surrogate model, in an engineering context, is a trained neural network that replaces an expensive physical simulation with an approximate but fast prediction. Engineers first run a full physical CFD simulation for a set of configurations covering a reasonable range of parameters — this is the expensive stage, hours of computation per variant. Pairs of "configuration parameters → simulation result" become training examples, and on them the network learns to predict the result directly from the parameters. After training, the network predicts almost instantly — not because it "computes physics faster," but because it does not compute physics at all: it statistically reproduces the relationship between input and output.

This acceleration has exactly one cost: the surrogate's accuracy is guaranteed only within the range of parameters seen during training. For a configuration far from anything the model has seen, the prediction may be inaccurate — and there is no way to find that out in advance without a full physical check. It follows directly that a final CFD check of selected candidates is mandatory not because engineers distrust the model on general principle, but because it is the only way to find out whether a specific chosen configuration has stepped outside what the model has ever seen.

Generative design of structures uses structurally the same fast-evaluation technique — but not to rank already-enumerated variants, but as an internal step of an iterative search algorithm that itself proposes and modifies a part's geometry. The Raptor surrogate answers "how good is this particular configuration"; generative design answers "what geometry can even exist here" — the object the model acts on is different: a number versus a geometry.

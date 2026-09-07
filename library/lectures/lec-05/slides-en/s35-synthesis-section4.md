---
id: s35
type: assertion_visual
section: "Section 4. Measure / Experiment"
duration_min: 1.5
assertion: "Measure is the arrow where AI lowered trust: the classic A/B stays, but evals and guardrail metrics are now mandatory on top"
learning_goal: "Synthesis S4 (LO1) — bridge into Support: the same skill in operation = noticing drift before the dashboard does"
learning_outcomes: [LO1]
chapter_ref: "§4.7 [for-slide-s35]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  assertion_visual: a layered diagram — the bottom layer "classical A/B" (thick, stable), on
  top of it 2 thinner layers "evals" and "guardrail metrics" (new, added layers, not a
  replacement of the bottom one).
---

# Visible content

## Title bar
A/B stays the foundation — evals and guardrail metrics are now mandatory on top

## Body
[Layered diagram: A/B (base) → evals → guardrail metrics]

**Measure = the arrow where AI lowered trust**
- Randomization is still what gives causation, not coincidence
- Evals (offline+online) + guardrail metrics — mandatory on top

[Gold callout]
The phase's central skill: **telling signal from noise**

## Speaker notes

Let's pull section four into one thought: Measure is the loop's arrow where AI lowered trust. The classical controlled A/B experiment stays — randomization still gives causation where a change caused the result — but on top of it, evals, layered offline and online, not as an alternative, and guardrail metrics are now mandatory, because probabilistic output and Goodhart's law make any single proxy vulnerable.

The phase's central skill, and the whole lecture's: telling signal from noise. A suspiciously good number is Twyman's law; a hacked proxy is Goodhart; a benchmark in the wrong format; a proxy with no guardrail — all of this is noise disguised as signal.

This is the bridge into section five: in operation, the same skill shows up as the ability to notice drift before a dashboard does. We'll see that the same principle — don't blindly trust an aggregated metric — works there too, only the object being observed shifts from an experiment to a live system in production.

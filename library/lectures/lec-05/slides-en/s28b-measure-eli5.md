---
id: s28b
type: eli5_overview
section: "Section 4. Measure / Experiment"
duration_min: 1.5
assertion: "Measurement in plain terms: find out whether your change caused the result, not coincidence — the only honest way is to compare two randomized groups"
learning_goal: "ELI5 overview of the measurement phase: why experiment, the mental model \"two identical groups\""
learning_outcomes: [LO1]
chapter_ref: "§4.1 [for-slide-s28b]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  eli5_overview: three cards, a "two groups + a coin" icon on the left (randomization).
  Plain language.
---

# Visible content

## Title bar
Measurement in plain terms

## Body
**What it is.** The phase where you honestly check: did the change work, or does it only look like it did. Many people see the formal discipline of experimentation for the first time.

**Why.** "The metric grew after the release" proves nothing — it could have grown on its own. You need a way to separate cause from coincidence.

**Mental model.** Split users into two random groups: show one the new thing, the other the old thing. The difference between them is the real effect. Agree in advance on which metric counts as success.

## Speaker notes

Measurement in plain terms is the phase where you answer the question "did it work" — and answer it honestly. And it's the loop's arrow where AI didn't make the work cheaper — quite the opposite, it lowered trust in the numbers, because now it's very easy to get a nice-looking result that means nothing.

The main trap sounds like this: "we shipped a new feature, and the metric went up — so the feature is good." That's an invalid conclusion. The metric could have gone up for ten other reasons: season, advertising, chance. To separate cause from coincidence, people invented the controlled experiment. The idea is simple: you randomly split users into two groups. Show one the new thing, the other the old thing, everything else the same. If there's a difference between the groups, it's caused specifically by your change, not something else. Random splitting is the key point: it's exactly what makes the groups comparable.

The second important element is agreeing in advance on which metric we count as success and what's unacceptable to us. Otherwise, after the experiment there will always be some number that "proves" what we wanted to see anyway. Next we'll break down the typical traps and see how a proxy metric with no safety net hid real harm for almost two years.

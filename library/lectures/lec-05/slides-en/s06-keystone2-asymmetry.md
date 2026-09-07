---
id: s06
type: assertion_visual
section: "Section 0. Introduction and keystone"
duration_min: 1.5
keystone: true
assertion: "AI changes the cost and trust of every arrow of the loop asymmetrically: Build → near zero; Measure/Learn — trust falls; Observe/Orient — faster, but more fragile"
learning_goal: "KEYSTONE-2 — cost/trust asymmetry + the meta-pattern \"the classic stays on every arrow\""
learning_outcomes: [LO1, LO2]
chapter_ref: "§0.5, §0.6, §0.7 [for-slide-s06]"
interaction: think_pause
verify_day_of: false
partial_out_strict_in: true
axis_slide: true
meme_or_visual: >
  assertion_visual: the same loop icon from s05, but now every arrow is colored by the sign of
  its change — the Build arrow is thick and gold (cost collapsed), the Measure/Learn arrow is
  dashed (trust fell), the Observe/Orient arrow carries a cracked-lock icon (fragility). Does NOT
  duplicate the s05 visual (different emphasis on the same shape).
---

# Visible content

## Title bar
AI changes the cost and trust of every arrow of the loop — but not equally

## Body
[The loop with 3 types of arrow emphasis: gold-thick / dashed / cracked]

- **Build** → cost nearly collapsed to zero
- **Measure / Learn** → cost about the same, **trust fell**
- **Observe / Orient** → observation is faster, but **more exposed to attack**

[Gold callout]
Meta-pattern: every arrow has a classical discipline behind it — AI does not cancel it

## Speaker notes

The second half of the keystone — the central analytical tool of the whole lecture: AI changes the cost and trust of every arrow of the loop asymmetrically, not equally. The "build" arrow — cost has nearly collapsed to zero: writing code, a design draft, a first research prototype are orders of magnitude cheaper than five years ago. The "measure" and "learn" arrows — cost has stayed roughly the same or dropped only slightly, while trust in the result has fallen: the very instrument of measurement has become probabilistic and exposed to metric manipulation. The "observe" and "orient" arrows have become faster, but at the same time more exposed to attack: the speed of observing a system in production has grown, but the very ability to react quickly turns into a vulnerability if the observed data can be poisoned.

Hence the meta-pattern that will repeat in each of the six sections, literally following the same template: every phase of the product lifecycle has a classical discipline, and AI does not cancel it. AI changes how much that discipline costs and how far it can be trusted without verification — but it does not remove the need for the discipline itself. Customer Development is not replaced by "ask the model what the user thinks"; a product experiment is not replaced by "the model predicted the metric would grow." In every section we'll ask the same question: what does the classic make reliable here, what does AI speed up — and at what point does speed become a trap, because trust doesn't keep pace with it.

Think for twenty seconds: on which arrow of your latest task did speed outrun your actual trust in the result?

---
id: s53
type: schema_matrix
section: "Section 7. Synthesis and the decision framework"
duration_min: 2.5
assertion: "Three axes — reversibility, the cost of an error, observability — set the phase's mode by a single rule, and each axis itself names what must stand beside it when that axis is in the problem position"
learning_goal: "Synthesis §7.3–§7.4: the decision instrument — three axes and the requirement on each; the run through the examined cases stays in the lecturer's speech"
learning_outcomes: [LO1, LO2, LO6]
chapter_ref: "§7.3 + §7.4 [for-slide-s53]"
verify_day_of: false
in_bucket: true
interaction: none
protected: true
absorbed: "s54 (the 8-question checklist) — removed, its content carried over here as the requirement on each axis; see §7.4 of the chapter"
note: >
  issue #212, revision following owner remark 5 ("slide 53 — shorten and simplify. it has to
  be made beautiful, not oversaturated as it is now"). Four of the eight blocks were taken
  off the slide: the caption of the axes diagram, the caption of the run-through, the
  two-case run-through table (5 columns × 2 dense rows) and the closing teal panel. Four
  blocks remain: the title, a narrow band with the question that comes before the axes,
  three large airy axis cards, and one gold rule into which the content of the removed teal
  panel was condensed. The bottom third of the slide is left empty on purpose — the slide is
  a final one and has to be memorable.
  THE RUN THROUGH THE TWO CASES (Google AI Overviews / Zillow Offers) has been moved
  entirely into the speaker notes, with the same figures and the same basis of comparison;
  it has left the visible layer.
  The question that comes before the three axes is kept — it was restored as a separate band
  after the roast of 2026-09-30 and carries the lecture's load-bearing axis "classical base →
  what AI adds → where it breaks".
  DISCREPANCY FOR THE ORCHESTRATOR: the two examined cases have left this slide's visible
  layer, which lowers its contribution to the strict-in share across slides; the analyses
  themselves stand in full on s26 and s40, so the deck-level share should not change — to be
  checked at consolidation.
  CONSOLIDATED (issue #212, 2026-10-01): rechecked against the visible layer of the
  assembled deck. The in_bucket flag rested on the three axes and the requirement on each
  axis ("when the human can be taken off the gate and when not"), not on the run through the
  two cases — and the slide's entire visible layer still consists of exactly that. The flag
  stands; the 2.5 min contribution is retained.
  CONSOLIDATED (issue #212, 2026-10-01): on the "Observability" axis the requirement
  "golden set" was replaced with "the eval loop". The technique named "golden set" stood on
  s24b, the owner reworked that slide entirely into mutation testing, and across the
  assembled deck the phrase occurred ONLY here — a summary slide was prescribing a technique
  the lecture never taught. "The eval loop" is the name of the technique on its own slide
  s31a, word for word; its title ("seeing that the answers have got worse before the user
  does") answers exactly this axis's definition ("how quickly it shows that an output is
  wrong"). The second member of the pair, "guardrail metric", is introduced on s29 and is
  left unchanged.
  Editorial rule: the "not X but Y" construction is not used in new text (tools/editorial).
meme_or_visual: >
  schema_matrix, deliberately sparse: a rule as the title, under it a narrow band with the
  question that is asked before the three axes, then three large cards of equal width — a
  big Lucide icon on top (rotate-ccw / banknote / eye), the axis name in a large type size,
  the definition in one line and a gold band with "what the problem axis requires". One gold
  rule at the bottom. No tables, no run-throughs, no second panel; the bottom third is empty.
---

# Visible content

## Title bar
Three axes decide whether the human can come off the gate

## The question that comes before all three axes
Before all three comes the question of the phase's classical discipline: if it is absent, you build it first — there is nothing to amplify in a vacuum.

## Body
[Three large axis cards: name · definition in one line · gold band with the requirement]

**Reversibility**
How easily the consequence can be rolled back if the output is wrong
[gold band] Low → a staged rollout and a tested rollback path

**Cost of an error**
What an error will cost: money, reputation, health
[gold band] High → a named owner for the decision

**Observability**
How quickly it shows that an output is wrong
[gold band] Low → the eval loop and a guardrail metric

[Gold — the rule]
No axis forbids AI — each one names what must stand beside it. All three in a good position and the human can come off the gate; any other combination calls for a gate on the problem axis.

## Speaker notes

The table on the previous slide is good as a map. A decision on a specific task is not taken from a map — that needs a more compact instrument. Three axes, each of which surfaced on its own in almost every section.

Reversibility — how easily the consequence can be rolled back if the output turns out to be wrong. It is low for deleting data in a running system and for a public promise to a customer; it is high for a draft nobody has seen yet. The cost of an error — money, reputation, health, legal liability. Observability — how quickly you will learn that an output is wrong, before the harm accumulates: high where there is a guardrail metric, low where the bad is hiding under a good average.

There is one rule. Taking the human off the gate is justified only where high reversibility, a low cost of an error and high observability come together at once. Any other combination calls for a gate, and the gate is chosen by the axis that is in the problem position. That is why each card says what that axis requires when it is in that position.

Let us run this through two cases we examined. Search answers rolled out to everyone at once: reversibility low — everyone saw the mistake at the same moment; cost high — the advice went viral and was dangerous; observability could have been high, a canary release would have given it, but the canary was skipped. There is one problem axis, reversibility, and the measure on it — a staged rollout — brings observability back along with it.

The second case is buying houses on a model's forecast. Reversibility is minimal: a purchased house cannot be undone with one click. The cost is at its maximum: at a loss of roughly eighty thousand dollars per house, write-downs of three hundred four to four hundred eight million dollars cover somewhere between three thousand eight hundred and five thousand one hundred houses out of the nine thousand six hundred eighty bought in the quarter. Observability was low by the design of the control itself: a quarterly report instead of a real-time check. All three axes were in the problem position, and there was a gate on none of them.

And the question that is asked before all three: does the phase have a classical discipline. If it does not, that is what you build first — there is nothing to amplify in a vacuum.

And one last thing. No axis forbids the use of artificial intelligence. Each one names what must stand beside it.

---
id: s26
type: assertion_visual
section: "Section 5. Wrap-up"
duration_min: 1
assertion: "Attention looks at tokens statistically — it does not understand causality"
learning_goal: "Cross-cutting frame 3: Human vs AI (callback to Lec-1 Pearl)"
learning_outcomes: [LO6]
chapter_ref: "§5.4 [for-slide-s26]"
visual_brief: "2 Ocean rounded boxes side by side: Human — 'X happened because Y' — a causal model (Pearl 2-3). AI — 'X follows Y in the data' — correlation (Pearl 1). Callback to Lec-1 Pearl."
---

# Visible content

## Title bar
"Attention looks at tokens statistically — it does not understand causality"
Subtitle: "AI counts correlations in the data, it does not build a causal graph"

## Body
[2 Ocean rounded boxes side by side, parallel structure]

**Human**
- "X happened **because** Y" — **a causal model — builds mechanisms**
- Relies on physical intuition, domain knowledge, knowledge of how the world works. For causal conclusions this experience is exactly what is needed — not statistics.

**AI (via attention)**
- "X **follows** Y in the data" — **a statistical correlation, not causality**
- Notices the pattern "X and Y often co-occur" in the training data. For causal conclusions — bring in a domain expert or causal methods.


## Speaker notes

The third short cross-cutting frame is a return to one of the most conceptually important places in Lecture 1: Pearl's three levels of causality. Lecture 1 showed that modern AI systems reliably operate at level 1 (association), partially at level 2 (intervention), and don't handle level 3 (counterfactuals). Now we have a mechanistic basis for this claim.

The attention mechanism looks at tokens statistically — it does not build a causal graph. When the model sees in the context the sentence "X happened because Y", it notices that the tokens X and Y often co-occur in the training corpus in similar constructions. It absorbs correlation, not causality. The construction "because" for the model is a pattern in the data, not a pointer to a causal mechanism in the real world.

Compare two processes. Human: "X happened because Y" — a causal model that includes levels 1 (observing correlation), 2 (what happens if you change Y), and 3 (what would have happened if Y hadn't occurred). This model relies on physical intuition, on domain knowledge, on knowledge of how the world works. AI based on the attention mechanism: "X follows Y in the data" — a statistical correlation between tokens. A strong signal at level 1; the model partially moves to level 2 if the training corpus had many examples of changing Y; at level 3 in the general case — no.

This explains a phenomenon described back in Lecture 1: the model answers "what correlates with what" excellently (data analysis). Worse — "what happens if I change X" (assessing an intervention). And almost not at all — "would Y have happened if X hadn't occurred" (counterfactual analysis). Counterfactual questions remain a zone of human expert judgment — this is not a temporary technical shortcoming but a limitation of the current paradigm.

The tone of the remark is factual, not alarmist. The attention mechanism is a powerful tool in the area where it works. That area is correlational statistics over data, and the engineer must remember the boundary when designing systems in which causal conclusions are expected from AI. The practical takeaway: where decisions require exactly causal inference, bring in a domain expert or dedicated causal methods — the attention mechanism by itself is not designed for this.

Sources:
[1] Pearl (2018) — The Book of Why — attention captures association, not causality (3 rungs of the causal ladder). http://bayes.cs.ucla.edu/WHY/

---
id: s40
type: assertion_visual
section: "Section 6. Wrap-up"
duration_min: 1.5
assertion: "Attention is a weighting by co-occurrence statistics: correlation, not causation"
learning_goal: "The mechanistic grounding for Lecture 1's thesis on the three levels of causality; a human in the loop as an architectural requirement"
learning_outcomes: [LO6]
chapter_ref: "§5.6 (chapter-part3.md) [for-slide-s40]"
visual_brief: "2 Ocean rounded boxes side-by-side: 'Humans' — 'X happened because Y' = a model of the mechanisms of the world (rungs 1–3); 'The model (via attention)' — 'X follows Y in the texts' = a frequency pattern (rung 1, partly rung 2, not rung 3). Gold callout about a human in the loop. (The incident-review walkthrough is speaker-notes only, not visible.)"
---

# Visible content

## Title bar
"Attention learns correlation, not causation"

## Body
[2 Ocean rounded boxes side-by-side]

**Humans**
"X happened **because** Y" — a model of the mechanisms of the world: association → intervention → counterfactual

**The model (via attention)**
"X **follows** Y in the texts" — "because" for the model is a frequency pattern, not a pointer to a mechanism of the world. Strong on associations; interventions — only ones resembling those described in the corpus; counterfactuals — systematically no

[Gold callout]
**Wherever causal conclusions are expected from the model, a human in the loop is an architectural requirement, not a polite caveat.**

## Speaker notes

The last boundary is conceptual — a return to Pearl's three levels of causality from Lecture 1. The thesis that "the model operates at the level of associations" now has a mechanistic grounding, and we've seen it: attention is a weighting of tokens by learned co-occurrence statistics. When the model reads "X happened because Y," the construction "because" is, for it, a frequency pattern in texts, not a pointer to a mechanism of the world. The model learns correlation, not causation.

From this follows a reproducible profile: the model is strong on "what's associated with what"; it partially handles "what happens if X changes" — only where similar interventions are described in the corpus; and it's systematically unreliable on "what would have happened if X hadn't occurred." This isn't a temporary shortcoming that the next version will close — it's a property of the underlying statistical mechanism.

Here's what the boundary looks like in a familiar scenario — an incident review. A model fed logs and a timeline is excellent at finding correlations and building a coherent narrative: "after the deploy, timeouts Y started." The danger is that a coherent narrative reads as a causal conclusion — when it's the most statistically plausible story; plausible means "this is how postmortems are usually written," not "this is what actually happened." Testing the hypothesis — a rollback, an experiment, the question "would it have failed without the deploy?" — stays with the engineer. The right division of labor: the model generates and structures hypotheses — it does that faster than a human; the human selects and verifies them. The wrong one: "the model wrote the cause into the report." Wherever decisions require an actual causal conclusion, a human in the loop is an architectural requirement.

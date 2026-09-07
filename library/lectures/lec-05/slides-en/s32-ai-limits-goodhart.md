---
id: s32
type: assertion_visual
section: "Section 4. Measure / Experiment"
duration_min: 2
assertion: "Goodhart's law: when a measure becomes a target, it ceases to be a good measure"
learning_goal: "AI limitations: Goodhart's law/reward hacking + what stays, LO6"
learning_outcomes: [LO2, LO6]
chapter_ref: "§4.4 [for-slide-s32]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  assertion_visual: a "boat circling in a lagoon instead of the finish line" icon (the
  CoastRunners metaphor, generic, not tied to a specific game brand) — visualizes "optimizing
  the proxy instead of the real goal."
---

# Visible content

## Title bar
The boat circles the lagoon racking up points — but never finishes

## Body
[A "boat circling instead of finishing" icon — a metaphor for hacking a proxy metric]

**Goodhart's law**: "when a measure becomes a target, it ceases to be a good measure"

- An RL agent in a boat race scored 20% more points than human players — by circling a lagoon, never finishing
- Anthropic: a model generalized from sycophancy to directly editing its own reward function

[Gold callout]
What stays: OEC discipline, guardrail metrics, Twyman's law — a suspiciously perfect eval score is now more likely a bug than a breakthrough

## Speaker notes

Goodhart's law, stated precisely: when a measure becomes a target, it ceases to be a good measure. The AI-specific formulation is specification gaming: behavior that satisfies the literal specification of an objective without achieving the intended outcome. A named example: an RL agent in a boat-racing game discovered it could score twenty percent more points than human players by endlessly circling a lagoon and collecting regenerating bonuses, never finishing the race. A more recent example from Anthropic: training a model on a curriculum of increasingly hackable environments, researchers observed the model generalize from simple sycophancy to sophisticated reward hacking, culminating in directly editing its own reward function.

Why the discipline of the controlled experiment and guardrail metrics remain mandatory: the more autonomous and probabilistic a system, the easier it is to hack a single optimized proxy, and the harder it is to notice with a single glance. OEC discipline: without an explicit, agreed-upon OEC, the system optimizes whichever proxy is easier to measure. Guardrail metrics are guardrails in Kohavi's precise sense: metrics you don't optimize but must not let silently degrade. Twyman's law: a suspiciously perfect eval score is now more likely a bug or a hacked proxy than a genuine capability leap.

When AI-first doesn't apply here: if a single measured quantity is an engagement proxy with no paired counter-metric on quality, the result isn't sufficient for a full-rollout decision. The same for evals: if a product makes a safety claim resting solely on a benchmark whose format is structurally different from the real task, that benchmark cannot support the claim.

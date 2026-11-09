---
id: s14
type: assertion_visual
duration_min: 2.9
assertion: "The main risk of topology optimization is not a 'hallucination' but garbage-in → optimal garbage: a flawless optimum for an incompletely posed problem."
learning_goal: "The part's failure (FAILURE): incomplete constraints + non-manufacturability + alternative (parametrics + manual topology optimization)"
learning_outcomes: [LO2, LO7]
chapter_ref: "§2.6 — The part's failure: garbage-in → optimal garbage"
references: [isicad-generative-ru, mcgan-2024]
visual:
  pattern: schema_pipeline
  primary: "Pipeline 'Incomplete statement → deterministic optimizer → a mathematically flawless, engineering-unusable shape' (RIGHT_ARROW); a non-manufacturability callout + a gold alternative"
  illustration:
    type: schematic
    sources:
      - "Self-generated pipeline via PowerPoint shapes + RIGHT_ARROW (Ocean palette)"
      - "Lucide icons https://lucide.dev — `file-warning` (incomplete statement), `cog` (optimizer), `ban` (unusable shape), 32px badge, recolored to Primary mid `#065A82`"
    caption: "garbage-in → optimal garbage"
interaction: none
---

# garbage-in → optimal garbage

## Assertion

The main risk of topology optimization is not a "hallucination" but garbage-in → optimal garbage: a flawless optimum for an incompletely posed problem.

## Visual

A horizontal pipeline in an Ocean rounded box (RIGHT_ARROW between blocks): "An incomplete statement (a load case forgotten, manufacturing constraints not set)" (icon `file-warning`) → "A deterministic optimizer honestly solves the problem it was given" (icon `cog`) → "A mathematically flawless, engineering-unusable shape" (icon `ban`, gold frame). On the right, a callout card: "Non-manufacturability: closed cavities and curved ribs with no cutter access — additive only; hard to measure and inspect against ESKD." At the bottom, a gold plate (`#F0AB00` bold): "The alternative for serial milling/casting — classical parametrics + manual topology optimization for manufacturability." A caption: "the method is deterministic — there is no hallucination here."

## Speaker notes

Now comes the fundamental limitation of topology optimization, and it is not the one usually expected. The optimizer honestly solves the problem it was given. If the statement is incomplete — a fatigue load case is forgotten, manufacturing constraints for casting or cutter access are not set, an assembly scenario is not accounted for — the algorithm will still converge to a mathematically flawless optimum, but one fitting the wrong statement. This is familiar from strength of materials: if a design load case is missed, the calculation may be arithmetically correct and the structure dangerous. Here it's the same, but more insidious: a beautiful "organic" shape looks so convincing that its unfitness is not visible to the eye. The main risk is not a hallucination — there is none here, the method is deterministic — it is incompletely set constraints.

A concrete example — non-manufacturability. Topology optimization readily produces a closed internal cavity with curved ribs that no cutter can reach, and that cannot be cast without a non-removable core. Such a shape can be manufactured only additively. Russian engineers, in professional publications, state directly that generative geometry is often non-manufacturable by traditional methods, hard to measure and to inspect against ESKD, and requires manual reconstruction into an editable solid. In other words, the generative tool is an input into the design process, not its output. This is a structural consequence of the problem statement: the criterion contains no term penalizing for technological inaccessibility unless the engineer put it there.

The classical alternative: for a serial part that will be milled or cast, a classical parametric model plus manual topology optimization for manufacturability is more practical than "beautiful" AI geometry. The optimizer as an idea generator is acceptable; as a source of finished production geometry for serial machining — it is not.

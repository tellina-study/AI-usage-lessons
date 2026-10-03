---
id: s17a
type: schema_matrix
section: "Section 2. Design"
duration_min: 2.5
assertion: "A design system becomes a guardrail only at the third layer: rules written as numbers and the team's own components lower the chance of a breach, and the guarantee comes from a check that can stop a release"
learning_goal: "The Section 2 practice: what a design system is in plain words, which three layers the mechanism is built from, and where its boundary runs"
learning_outcomes: [LO1, LO2]
chapter_ref: "§2.4a"
verify_day_of: false
partial_out_strict_in: true
interaction: none
protected: true
meme_or_visual: >
  schema_matrix, the single practice card: WHAT IT IS · HOW IT WORKS (a labelled diagram of
  three layers from the bottom up, each layer numbered and labelled) · WITH AI AND WITHOUT ·
  WHERE IT BREAKS (gold). Lucide icons: shield-check, component, palette.
note: >
  issue #212, the forms brought together after the methodology review of 2026-09-30: all
  twelve practice cards are reduced to ONE form — WHAT IT IS (the way in for a newcomer) /
  HOW IT WORKS (numbered steps + a labelled diagram) / WITH AI AND WITHOUT (rule R6) /
  WHERE IT BREAKS. There are no "artefact", "criterion" or "building on what has been
  covered" blocks, and no questions to the room. The earlier mismatched fourth blocks
  ("SCALE", "DIAGRAM", "PRACTICES 2026", "TOOLS 2026") are removed: diagrams live inside
  HOW IT WORKS, and the current tools in the "WITH AI" column.
---

# Visible content

## Title bar
A design system: shared interface rules that a machine can check on its own

## Body
[what it is → how it works → with AI and without → where it breaks]

**WHAT IT IS**

A **design system** is the shared body of interface rules for a product and the set of ready-made components that goes with it: the colour combinations allowed, the sizes of buttons and fields, how an element looks under the cursor. It used to be a document for people. What matters more now is the other part: some of the rules can be written so that a machine reads them and checks them.

**HOW IT WORKS**

[Labelled diagram: three layers from the bottom up — "each layer is stronger than the one below it, and only the top one turns a wish into a guarantee"]

3. **A check that stops the release.** The rule is checked automatically on every generated screen, and a breach is blocked with no discussion. **Only this layer gives a guarantee.**
2. **The team's own components instead of stock ones.** The generator is given the team's own components. This **lowers the chance of a breach and guarantees nothing.**
1. **Rules written as numbers.** While a rule lives in a picture of a mockup, the only thing that can check it is a person, and only by eye.

**WITH AI AND WITHOUT**

| WITHOUT AI — a body of rules for people | WITH AI — why the rules became machine-readable |
|---|---|
| A designer checks it by eye: a set of rules keeps the product consistent. | The generator turns out screens faster than a person can look at them. A machine check **grows with the generation**. |

[Gold callout — WHERE IT BREAKS]
A machine checks only what can be expressed as a number. "Is this clear to a living person" stays with the person: a screen can pass every check and remain unclear. And separately: **a request addressed to the generator is not a control mechanism** — a mechanism is a rule that can stop a release. This check looks at the screen: the system's behaviour over time cannot be expressed as a number and is not covered by it.

## Speaker notes

A design system is routinely called the guardrail that holds generation inside the lines. The phrasing is right, but until there is a mechanism behind it, it is a metaphor — so let me start with what the thing actually is. A design system is the shared body of interface rules and the set of ready-made components: the colour combinations allowed, the sizes of buttons and fields, how an element looks under the cursor, what a standard block is made of. For a long time it was a document for people. What matters now is its other part: those rules that can be written so that a machine reads them and checks them.

There are three layers, and only the last one is load-bearing. The first is rules written as numbers. While a rule lives in a picture of a mockup or in a spoken agreement, the only thing that can check it is a person, and only by eye; written as a number, it becomes checkable. The second layer is giving the generator the team's own components instead of generic templates. Some tools do this by construction, and that is exactly why generation of that kind needs less reworking. But notice: the first two layers lower the chance of a breach, and only the third turns a chance into a guarantee. The third layer is an automatic check with the right to stop a release: a breach is not discussed, it is blocked, exactly as a red test stops a change going any further. And a point I want to make separately: the common engines for a check like that have nothing to do with AI at all. That is part of the lesson, not a detail of the setup.

Separately — what here comes from AI and what was always there. A body of interface rules and a set of ready-made components have existed for decades, and a designer checked them by eye. One thing changed: the generator turns out screens faster than a person can look at them, and a machine check is the only thing that grows with the generation.

The boundary is a compulsory part of the practice, not a caveat. A machine checks only what can be expressed as a number: contrast, the size of a button, whether a field has a label. The question of whether this is clear to a living person stays with the person, and a screen can pass every check in full and remain unclear. So the practice does not replace a review against Nielsen's ten heuristics, and it does not replace showing the thing to living people — it only takes off them what is cheaper to catch by machine. And the conclusion that travels furthest: a request addressed to the generator is not a control mechanism, in any wording at all. Telling a request from a guarantee is something you will need in every phase that follows.

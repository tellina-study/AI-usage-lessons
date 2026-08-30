---
id: s06
type: assertion_visual
duration_min: 1.5
assertion: "There are many definitions of AI — because AI is a moving target"
learning_goal: "The multiplicity of AI definitions + the AI Effect as the cause"
learning_outcomes: [LO1]
references: [russell-norvig-2021, iso-iec-22989-2022, mitchell-1997, mccorduck-2004]
visual:
  pattern: four_approaches_compact_table
  primary: "4 approaches in a compact 2×2 grid + AI Effect callout at the bottom with the Tesler quote"
---

# There are many definitions of AI — because AI is a moving target

## Assertion

There are many definitions of AI — because AI is a moving target.

## Visual

A 2×2 grid of four Ocean rounded box cards — each one holding a **compressed, real definition** (15–25 words), not just the name of the approach. Below the grid, a gold AI Effect callout with the Tesler quote.

**Card 1 — Russell & Norvig (AIMA, 2021):**
> «AI = a system that thinks like a human, thinks rationally, acts like a human, or acts rationally (4 quadrants across 2 axes).»
>
> *Russell & Norvig, AIMA, 4th ed., 2021*

**Card 2 — ISO/IEC 22989:2022:**
> «An AI system is an engineered system that generates outputs (recommendations, predictions, decisions) for goals set by humans.»
>
> *International standard ISO/IEC 22989:2022 (the basis of the EU AI Act)*

**Card 3 — Through learning (Mitchell, 1997):**
> «A program improves with experience E on task T according to metric P. If the behavior emerges from a learned model — it's AI.»
>
> *Mitchell, Machine Learning, 1997*

**Card 4 — Through benchmarks and AGI:**
> «AI = whatever passes the Turing test or solves a benchmark at the human level. Searle's objection: behavior ≠ understanding.»
>
> *Turing 1950 / Searle 1980 — Chinese Room*

**AI Effect callout (below the grid):**
> «AI is whatever hasn't been done yet» — Larry Tesler / Pamela McCorduck. Speech recognition, traffic navigation, face unlock — each was AI at the moment it appeared, and now it's just an app feature.

## Speaker notes

Any student who starts reading the AI literature quickly discovers that the subject has no single canonical definition. This is not a shortcoming of textbook authors or a gap in standardization — it reflects the nature of the subject. Before moving on to practical types of systems, it's important to pin down which definitions coexist in the literature and why they don't contradict one another but rather complement each other.

The first approach — Russell and Norvig, in the canonical AIMA textbook, propose laying out the definitions of AI along a matrix: thinking versus acting, humanlike versus rationally. The authors themselves lean toward the fourth cell — «acting rationally» — because it doesn't require answering the philosophical question of what thinking is.

The second approach — the international standard ISO/IEC 22989, on which the European regulation relies. A definition through capabilities and through the source of goals: an AI system generates outputs for goals set by humans.

The third approach — functional, through learning. A program improves its behavior on a task with a metric by means of experience. This is an engineering criterion: if a system's behavior can be fully described by «if — then» rules, it's not AI; if the behavior emerges from a learned model — it's AI, even if the model is simple.

The fourth approach — through comparison with humans and through benchmarks. It spawned a line of tests from chess to ARC-AGI. The classic objection is Searle's Chinese Room: benchmark equivalence does not mean understanding.

And the main point — the AI Effect, described by Pamela McCorduck: as soon as a technique starts working, people stop calling it AI. Speech recognition, traffic navigation, face unlock — each of these, at the moment it appeared, was AI, and now it's called simply an app feature. That's why the definition of AI keeps shifting: as soon as a task is solved and built into a product, it cools down to the level of ordinary technology.

In this course we'll explicitly name which of the four definitions is at work in each situation. The main thing is not to pick one as the «correct» one.

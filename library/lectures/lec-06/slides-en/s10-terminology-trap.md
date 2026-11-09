---
id: s10
type: assertion_visual
duration_min: 2.5
assertion: "'AI generates the design' is a marketing substitution: under the hood, a deterministic optimizer solves the problem the engineer posed — not a generative model."
learning_goal: "The terminological trap (FAILURE/judgment): asking 'what kind of AI is this' before trust"
learning_outcomes: [LO1, LO7]
chapter_ref: "§2.1 — The terminological trap"
references: [autodesk-fusion-blog-topopt]
visual:
  pattern: comparison
  primary: "Two contrasting columns in an Ocean rounded box: 'Marketing says' vs. 'What's actually happening'; a gold lesson at the bottom"
  illustration:
    type: schematic
    sources:
      - "Self-generated 2-column contrast via PowerPoint shapes (Ocean palette)"
      - "Lucide icons https://lucide.dev — `megaphone` (marketing), `cog` (what's actually happening), 32px inline, recolored to Primary mid `#065A82`"
    caption: "The terminological trap: 'AI generates the design'"
interaction: none
---

# "AI generates the design" — a substitution of concepts

## Assertion

"AI generates the design" is a marketing substitution: under the hood, a deterministic optimizer solves the problem the engineer posed — not a generative model.

## Visual

Two columns in an Ocean rounded box. Left, heading "Marketing says" (icon `megaphone`, Teal `#028090`): "AI generates the design · AI came up with the part · creative artificial intelligence." Right, heading "What's actually happening" (icon `cog`, Primary mid): "topology optimization · a deterministic numerical method · same input → same answer · not a single trained generative model · the vendor itself distinguishes topology optimization from 'generative AI.'" Below the columns — a gold plate (`#F0AB00` bold, 20pt): "Lesson: before trusting a tool, ask what kind of AI this is."

## Speaker notes

Let's state the debunking thesis at full strength. When a CAD system shows a "Generative Design" window and accompanies the result with the words "AI generates the design," a substitution of concepts is taking place, and it has a concrete engineering cost. Under the hood of these tools runs topology optimization — a deterministic numerical method that, for the same inputs, gives the same result, and contains not a single trained generative model. Notably, the vendor itself, in its own technical blog, draws this very distinction, stating that topology optimization is a method inside generative design, not "generative AI."

Why does this matter practically, not just terminologically? An engineer who believes "AI came up with the part" makes two mistakes at once. The first: he underestimates his own responsibility for the problem statement — if AI came up with it, then AI is the one to answer for it. In reality, every feature of the shape is determined by the given loads, constraints, and objective function; if these are set incorrectly, the shape will be mathematically optimal and engineering-wise useless. The second: he overestimates the "creative" abilities of the tool — the optimizer does not invent the part's function and does not resolve technical contradictions; it only distributes material within a given space, under a fixed function.

The lesson of this part is direct: before trusting a tool, you must ask "what kind of AI is this" — and for generative design, the honest answer is almost always "deterministic optimization, not a generative model."

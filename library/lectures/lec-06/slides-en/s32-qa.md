---
id: s32
type: assertion_visual
duration_min: 0.9
assertion: "Q&A"
learning_goal: "Open Q&A with 3 backup prompts (a dedicated slide, the Lec-N-1 pattern)"
learning_outcomes: []
chapter_ref: "frontmatter (closing)"
references: []
visual:
  pattern: cover_distinct
  primary: "A large 'Q&A?' at 80pt + a gold 96px `message-circle-question` icon + 3 backup-prompt chips in an Ocean rounded box + a subdued course-contact card"
  illustration:
    type: schematic
    sources:
      - "Self-generated layout (large 'Q&A?' typography + course-contact card)"
      - "Lucide icon https://lucide.dev `message-circle-question` 96px hero, recolored to Gold `#F0AB00`"
    caption: "Q&A — open floor"
interaction: none
---

# Q&A

## Assertion

Q&A.

## Visual

At the center of the slide — large text "Q&A?" at 80pt bold deep, with a `message-circle-question` icon at 96px gold (`#F0AB00`) on the left. Below it — three card chips in an Ocean rounded box (12pt italic): "1. Which tool does marketing call 'AI' in CAD — and what kind of AI is it actually? · 2. Where in a project is there a 'seam between systems,' at which AI could confidently mix up units? · 3. Name a problem where AI is justifiably told 'no,' and the right tool." In the bottom-right corner — a subdued course-contact card (8pt, Primary light): "Course 'AI Across Industries' · seminar — a case study in engineering design · office hours."

## Speaker notes

Open Q&A. A pause of a few seconds of silence is normal — the audience is digesting dense material. If there are no questions, there are three provocations in reserve. First: which tool in a familiar CAD system does marketing call "AI," and what kind of AI is it actually — deterministic optimization or a trained model? Second: where in a real project is there a "seam between systems" at which AI could confidently mix up units, as in Mars Climate Orbiter? Third: name a concrete problem where it is justified to tell AI "no," and name the right tool.

The most common question at lectures of this kind: why does an engineering student need KKT and the weak Galerkin form, if they will never write a solver themselves? The short answer: not to compute anything by hand. Understanding the lineage gives precise knowledge of what an "AI result" of generative design actually is — a point satisfying the optimality conditions, not a sample from a distribution; this is immunity against the marketing substitution. And the weak form shows exactly what a surrogate bypasses — the discretized equilibrium law — and makes tangible the boundary "a surrogate guesses the output, it does not solve the equation."

If a technical question needs a deep answer that there isn't time for, it's worth deferring to the seminar, where there will be an hour and a half to dissect a case study in engineering design in the Russian context. The main skill that should remain is not a list of technologies but the discipline of the question: name the kind of AI, place it on the axis, check the completeness of the statement, ask about the exact normative tool, and remember that the signature and responsibility are not delegated. It is precisely the ability to justifiably say "no" that distinguishes an engineer from a button operator.

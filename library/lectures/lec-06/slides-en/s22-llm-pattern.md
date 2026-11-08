---
id: s22
type: assertion_visual
duration_min: 2.7
assertion: "An LLM is good at generating a draft of technical text with precise terminology of form — but the factual content is subject to mandatory verification by the engineer."
learning_goal: "The LLM pattern: where it's useful (a draft subject to mandatory review); a demo prompt structure"
learning_outcomes: [LO1, LO7]
chapter_ref: "§4.3 — The pattern: where an LLM is useful"
references: []
visual:
  pattern: schema_pipeline
  primary: "Pipeline 'a prompt with precise terminology → LLM → a draft spec → MANDATORY engineer verification' (RIGHT_ARROW); a gold border"
  illustration:
    type: schematic
    sources:
      - "Self-generated pipeline via PowerPoint shapes + RIGHT_ARROW (Ocean palette)"
      - "Lucide icons https://lucide.dev — `pen-line` (prompt), `file-text` (draft), `check-circle` (verification), 32px badge, recolored to Primary mid `#065A82`"
    caption: "The LLM pattern: a draft subject to mandatory review"
interaction: none
---

# An LLM writes the draft — the engineer verifies the facts

## Assertion

An LLM is good at generating a draft of technical text with precise terminology of form — but the factual content is subject to mandatory verification by the engineer.

## Visual

A horizontal pipeline in an Ocean rounded box (RIGHT_ARROW between blocks): "A prompt with precise terminology of form (the required structure and terminology of the document)" (icon `pen-line`) → "LLM" → "A draft: the structure of an explanatory memo / a template for technical specifications / a reformulated requirement / an explanation of a standard's clause" (icon `file-text`) → "MANDATORY engineer verification against the primary source" (icon `check-circle`, gold frame `#F0AB00`). Below the pipeline — a gold plate (bold, 16pt): "An LLM gives the right FORM and potentially the wrong CONTENT — useful for a draft, dangerous for the final document." A caption (12pt): "verification — always, without exception."

## Speaker notes

There is a concrete pattern where an LLM brings real benefit to an engineer, and it's worth stating it precisely, to separate it from the anti-pattern on the next slide.

An LLM is good at generating a draft of a text artifact with precise terminology of form: the structure of an explanatory memo, a template for technical specifications, a reformulation of a requirement, an explanation of how a clause of a standard is constructed. Here the model is strong precisely in what it was trained on — linguistic form. A well-crafted prompt describes the required structure and terminology of the document, and the output is a skeleton that saves the engineer time on routine work.

But — and this is a boundary built into the pattern — the factual content is subject to mandatory verification. Specific material grades, standard numbers, numerical tolerances, coefficient values must be checked by the engineer against the normative base. An LLM gives the right form and potentially the wrong content; this combination is useful for a draft and dangerous for a final document. The pattern is formulated thus: an LLM writes the draft, the engineer verifies the facts against the primary source — always, without exception. It matters that the boundary here runs not between "using an LLM" and "not using it," but between form and content: the model is responsible for the form, the engineer, with the normative base in hand, is responsible for every fact.

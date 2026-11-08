---
id: s28
type: assertion_visual
duration_min: 2.9
assertion: "AI generates the shape — the human is responsible, verifies, and invents the function; TRIZ formalizes invention, while an optimizer only distributes material."
learning_goal: "Human vs. AI (the signature = deontology, not delegable) + the TRIZ contrast"
learning_outcomes: [LO2, LO7]
chapter_ref: "§5.3 — Human versus AI and the contrast with TRIZ"
references: [altshuller-triz-1946]
visual:
  pattern: comparison
  primary: "Two columns (AI: proposes the shape / Human: is responsible, invents the function) + a TRIZ contrast; a gold formula"
  illustration:
    type: schematic
    sources:
      - "Self-generated 2-column comparison via PowerPoint shapes (Ocean palette)"
      - "Lucide icons https://lucide.dev — `box` (AI: shape), `pen-tool` (human: signature/responsibility), `lightbulb` (TRIZ: invention), 32px inline, recolored to Primary mid `#065A82`"
    caption: "Human vs. AI + the contrast with TRIZ"
interaction: none
---

# AI generates — the human is responsible, verifies, and invents the function

## Assertion

AI generates the shape — the human is responsible, verifies, and invents the function; TRIZ formalizes invention, while an optimizer only distributes material.

## Visual

Two columns in an Ocean rounded box. Left, heading "AI" (icon `box`, Teal `#028090`): "proposes a shape for a fixed function and a fixed design space · distributes material within a given volume." Right, heading "Human" (icon `pen-tool`, Primary mid): "sets the constraints · IS RESPONSIBLE for the result (the designer's and analyst's signature = legal responsibility for safety) · the constraint is deontological, not technical — not delegable." Below the columns — a TRIZ-contrast strip (icon `lightbulb`): "TRIZ (Altshuller, from 1946) formalizes INVENTION — resolving a technical contradiction, choosing a working principle; this is a level above optimizing a shape for a fixed function." At the bottom — a wide gold formula plate (`#F0AB00` bold, 20pt): "AI generates — the human is responsible, verifies, and invents the function."

## Speaker notes

Let's close the part with a conceptual boundary that ties the spine together. The engineer sets the constraints and is responsible for the result: the designer's and analyst's signature under the documentation is legal responsibility for safety. It cannot be delegated to an optimizer or a neural network. This constraint is not technical but deontological: responsibility always rests with the human, regardless of where the geometry came from. AI proposes the shape — the human is responsible and verifies.

A useful historical comparison is with TRIZ. The Theory of Inventive Problem Solving, work on which Genrich Altshuller began in 1946, formalizes invention — resolving a technical contradiction, choosing a working principle, the ideal final result. "Generative design" optimizes shape for a fixed function and a fixed design space. These are different levels: changing an assembly's working principle, resolving the contradiction "strong yet light" by changing the scheme — this is the level of TRIZ and engineering creativity, inaccessible to a topology optimizer, which only distributes material within a given volume for a given function.

A historical irony: back in 1946 the Soviet engineering school already asserted that creativity is algorithmizable — but it algorithmized precisely conceptual invention, not the cosmetics of form. Modern "generative design" algorithmizes a narrower slice than TRIZ promised eighty years ago. The formula that ties up the spine of the whole lecture: AI generates — the human is responsible, verifies, and invents the function.

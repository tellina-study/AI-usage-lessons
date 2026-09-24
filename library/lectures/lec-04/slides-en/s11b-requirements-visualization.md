---
id: s11b
type: assertion_visual
section: "Section 1. Requirements — the first artifact"
duration_min: 3
assertion: "Visualizing requirements is not a new category but the same architecture-as-code principle (§2.4) applied to requirements: keep the artifact as text rather than a picture, so it is versioned and readable by both the human and AI"
learning_goal: "Mermaid User Journey + the bridge to Gherkin as an executable specification; the honest boundary — story mapping does not belong here"
learning_outcomes: [LO1, LO7]
chapter_ref: "§1.2b [for-slide-s11b]"
references: [mermaid-user-journey, cucumber-bdd]
verify_day_of: false
visual_brief: "Two Ocean rounded boxes: left — Mermaid User Journey (a text DSL snippet in a monospace font, Title→Sections→Tasks with a 1-5 rating); right — a Gherkin Given-When-Then snippet. Below — a muted contrast strip: story mapping is a workshop technique (Miro/FigJam), NOT code-as-DSL, an honest boundary. Gold callout — the same principle as architecture-as-code §2.4, not a new method."
interaction: none
---

# Visible content

## Title bar
Visualizing requirements — the same architecture-as-code principle applied to requirements

## Body
[Left — Mermaid User Journey, Ocean rounded box, monospace text]

**Mermaid User Journey** — a text DSL for diagrams, the same family as PlantUML/Structurizr for architecture. Structure: `Title → Sections (journey phases) → Tasks (steps, a 1–5 rating, actors)`.

`title Booking a meeting room`
`section Find a slot`
`  Open the calendar: 4: Engineer`
`  Find a free slot: 2: Engineer`

It shows the current (as-is) flow and exposes the points to improve (to-be). AI both **reads** such a diagram as requirement context and **generates** it from a scenario description — the same format as C4: text in the repository, not a picture inside a separate tool.

[Right — the bridge to Gherkin, Ocean rounded box, monospace text]

**The bridge to Gherkin — an executable specification.** A more direct analogue of architecture-as-code: the scenario does not merely describe a flow, it is **verified** by running an automated test (the testing section).

`Given the meeting room is free`
`When an engineer books a slot`
`Then the booking is confirmed`

Just as C4/Mermaid is text checked by a drift detector, Gherkin is text checked by an automated test: both are "the specification as an executable artifact", and AI can write and validate both against reality.

[Contrast strip — the honest boundary]
**Story mapping** (laying activities out in columns, Miro/FigJam) is an important practice, but it is a **facilitation workshop technique**, not code-as-DSL. Here the road to a disciplined requirement runs through the people in the room, not through versioned text.

[Gold callout]
Not a separate new tool category — the same move as architecture-as-code: the artifact as text rather than a picture, so that AI can read and generate it on a par with the human.

## Speaker notes

It is worth answering one anticipating question honestly right away: is the requirements visualization below a separate new category of tools? No. It is the same move you will meet later as architecture-as-code: keep the artifact as text rather than a picture, so that it is versioned, diffable and readable by both the human and AI. Here the principle is applied not to an architectural component but to a user journey inside a requirement.

Mermaid is a text DSL for diagrams, the same family of tools as PlantUML and Structurizr: the diagram is described in code rather than drawn with a mouse, which automatically gives you versioning through git rather than through a separate visual editor [1]. The User Journey Diagram is a concrete diagram type for requirements: the structure "a title, then sections for the phases of the journey, then tasks for the steps, with a convenience rating from one to five and the actors involved" shows which steps a user goes through to complete a task, and exposes the points that need improvement. The practical consequence is the same as for C4-as-code: AI can both read such a diagram as requirement context and generate it from a scenario description, in exactly the way it reads and writes a C4 diagram, because the format is one and the same.

The second, more direct analogue is a Given-When-Then scenario in Gherkin, which does not merely describe a flow but is verified by running an automated test; we will look at it in more detail in the testing section [2]. The parallel: just as C4 and Mermaid are text checked by a drift detector, a Gherkin scenario is text checked by an automated test; both are the specification as an executable artifact, versioned next to the code, and AI can both write them and validate them against reality.

The honest boundary: user story mapping — laying user activities out in columns, often on a physical or digital wall — is an important and widespread practice, but it is a facilitation workshop technique, not code-as-DSL. Lumping it together with Mermaid and Gherkin into one "requirements as code" category would be an overstatement: story mapping's road to a disciplined requirement runs through the people in the room discussing sticky notes, not through a versioned text format that AI reads and generates.

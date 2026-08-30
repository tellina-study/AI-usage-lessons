---
id: s02
type: cover
section: "Section 0. Introduction and methodological frame"
duration_min: 0.5
assertion: "Lecture 4. AI across the software development lifecycle"
learning_goal: "Cover + roadmap of sections 0–7; preview of the discipline git loop"
learning_outcomes: [LO1, LO4, LO7]
chapter_ref: "§0.1 [for-slide-s02]"
visual_brief: "Hero cover: a large outline \"04\" (Primary mid outline). On the right — title 36pt bold deep, below it 16pt italic light: course · developers. At the bottom — a roadmap bar of 8 cards (0 Intro / 1 Requirements / 2 Architecture / 3 Implementation / 4 Testing / 5 Review+Security / 6 Delivery+Ops+Docs / 7 Synthesis), current (0) gold. A decorative hint of the discipline git loop (a chain of artifacts spec→ADR→plan→PR→incident around a circle) around the \"04\". NO Ocean rounded box (the motif belongs to content)."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
Lecture 4. AI across the software development lifecycle

## Body
[A large decorative "04" with a hint of the artifact cycle spec→ADR→plan→PR→incident around it]

**AI across the software development lifecycle**

*Course "Deliberate use of AI" · developers*

[Roadmap bar at the bottom — 8 cards, current (0) gold]

0 Intro · 1 Requirements · 2 Architecture · 3 Implementation · 4 Testing · 5 Review + Security · 6 Delivery · Operations · Documentation · 7 Synthesis

## Speaker notes

Software development is the first industry-specific topic of the course after three survey lectures, and it was chosen for two reasons. First: it is an area where generative AI is applied at scale and where we have the best measurements to date, the best-documented failures, and — most important for this lecture — the most mature methodological practices, the material on which you teach judgment rather than belief. Second: software development is the industry you, as engineers, will enter most closely and earliest, so the cost of a mistaken judgment is personally highest for you.

The thesis of the whole lecture, worth keeping in mind from the first slide: AI changes the cost of writing code but not the cost of understanding what to build and who is responsible for it; and it is useful exactly to the degree that engineering discipline is built around it across the lifecycle phases. The roadmap is simple: after the introduction we will go through the development phases in order — requirements, architecture, implementation, testing, review and security, delivery with operations and documentation — and gather everything into a decision apparatus: a matrix of "phase × leading practice × where the human is required" and a checklist of "when AI yes, when no." In each phase we ask three questions: which methodological practice makes the phase reliable, which human-owned artifact it ends in — and where in it the human is required and the tool is secondary.

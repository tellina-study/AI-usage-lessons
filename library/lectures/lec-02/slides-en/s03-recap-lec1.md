---
id: s03
type: assertion_visual
section: "Section 0. Introduction"
duration_min: 1.5
assertion: "Today's object is the 'model' layer from Lecture 1's four layers"
learning_goal: "Object of study (the 'model' layer in Lec-1's 4-layer picture) + bridge to the internals of inference"
learning_outcomes: [LO1]
chapter_ref: "§Введение [for-slide-s03]"
visual_brief: "Left — nested layers from Lec-1 (model → chat → agent → application), bottom layer 'Model' in gold. Right — 2 lines: 'The \"model\" layer: stateless inference' → 'Today: we take apart what's inside that inference'."
---

# Visible content

## Title bar
"Today's object — the 'model' layer from Lecture 1's four layers"

## Body
[Left — nested layers from Lecture 1: 4 concentric Ocean rounded boxes, bottom-aligned. Bottom to top: Model → Chat → Agent → Application. Bottom layer "Model" — gold outline]

[Right — 2 lines in rounded boxes]

**The "model" layer:** stateless inference — input goes in, a prediction comes out, no memory between calls.

**Today:** we take apart what happens inside that inference — and where its design changes engineering decisions.

## Speaker notes

Today's object of conversation is the "model" layer. Lecture 1 gave us a layered picture: at the bottom, the model; above it, the chat loop with a system prompt and history; above chat, the agent loop; on top, the application. There, the model was described as stateless inference: input goes in, a prediction comes out, no memory between calls. From that same lecture we already have the context window as a constraint, the distinction between local and cloud models, and Pearl's three levels of causation — all of that is taken as known today and used without re-deriving it.

With that description we can already talk about where the model sits in the larger system. But the question of what exactly happens inside that function between request and answer — Lecture 1 deliberately left that a black box. Today we open that box, and everything that happens in this lecture happens inside a single layer, the bottom one. Chat, agents, RAG, and applications are built on top of it and are discussed in Lecture 3 and beyond.

We're chasing boundaries: the places where the model's internal design changes how you build prompts, agents, and decisions. Every mechanism in this lecture was chosen because it has an observable engineering consequence — in cost, speed, quality, or reproducibility.

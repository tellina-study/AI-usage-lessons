---
id: s13
type: comparison
duration_min: 3.5
assertion: "One task, three ways: control is distributed between developer and user"
learning_goal: "The layered model via a Model→Chat→Agent comparison through the control quadrant"
learning_outcomes: [LO1, LO4]
references: [anthropic-2024-effective-agents]
visual:
  pattern: control_quadrant_2x2_with_task
  primary: "On top a 2×2 quadrant: X=delegation from the user, Y=developer control; 3 points along the diagonal — Model (bottom-left), Chat (center), Agent (top-right, gold); a fixed task on the right"
interaction: live_demo
---

# One task, three ways: control is distributed between developer and user

## Assertion

One task, three ways: control is distributed between developer and user.

## Visual

On top a 2×2 quadrant in an Ocean rounded box. The X axis — delegation from the user (low → high). The Y axis — developer control (low → high). Three points, each with a short single-line caption underneath, «what's characteristic of solving it this way»: Model in the bottom-left corner — «integrates the API themselves, full control»; Chat in the center — «dialogue, clarifications along the way»; Agent in the top-right corner — «delegates the whole thing, the orchestrator decides» (the point in gold). The top-left corner is captioned in small italics «no point» (high developer control without delegation = odd). The bottom-right corner is captioned in small italics «danger zone» (full delegation without guard rails). On the right a panel with the task: «Extract fields from an incoming PDF contract and put them in a table». Axis labels large (15pt), the «↑ high» / «↓ low» markers — enlarged to 14pt (issue #155), point sub-captions — 8.5pt single-line (a widened textbox, no line breaks).

## Speaker notes

The very same task can be solved in three different ways of building it, and each of them distributes control between developer and user differently. The more the user delegates the solving of the task to the AI, the more a rigid frame from the developer is needed — that's why the Agent ends up in the top-right corner of the quadrant.

Let's take a task: extract fields from an incoming PDF contract and put them in a table. Signing date, counterparty, amount, term. Five or six fields.

Way one — the model. You take a pretrained or fine-tuned model for extracting structured fields from documents, for example DocVQA or a specialized nougat-style model. The user integrates the API themselves: passes the PDF themselves, gets the JSON themselves, puts it into their own table themselves. Delegation from the user is low — they control each step themselves. Developer control is also low — the model is a raw inference endpoint without orchestration, without guard rails, without tools. This is the bottom-left corner of the quadrant: low delegation on the horizontal, low developer control on the vertical.

Way two — chat. You open ChatGPT or YandexGPT, attach the PDF, write "extract the following fields and return them as a table". The user delegates the task in words and can clarify, but works within the product — a medium degree of delegation. The developer has set the system prompt, the basic constraints, the context window — medium control on their side. This is the center of the quadrant.

Way three — the agent. The user says "do this task" and approves the key nodes — a high degree of delegation, the user doesn't manage the intermediate steps. The developer has assembled an agent: the orchestrator plans the steps, the tools — open the PDF, run OCR, extract the fields, write to the table, the agent has memory between steps and the ability to make several calls. High developer control — they designed the whole decision loop, the list of tools, the guard rails, and the system prompt. This is the top-right corner of the quadrant: high delegation on the horizontal, high developer control on the vertical.

The two empty corners explain why the placement is not random. The top-left (high developer control, but the user doesn't delegate) — no point: why build an orchestrator if the user decides everything step by step themselves. The bottom-right (full delegation without guard rails) — a danger zone: the user handed the task to the AI, but the developer didn't provide any frame. That's why the diagonal from bottom-left up to the top-right is the natural trajectory: more delegation requires more scaffolding.

This distribution of control is not a merit of one way over another. It's an engineering decision: where control should sit for a specific scenario. If user flexibility matters — the model. If the task is routine but requires clarifications — chat. If the flow is large and automation is needed — the agent. In the seminar we'll practice this choice.

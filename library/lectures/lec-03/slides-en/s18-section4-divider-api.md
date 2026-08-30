---
id: s18
type: section_divider
section: "Section 4. Agents"
duration_min: 1
assertion: "Section 4 — how AI becomes a system component: API, MCP, the agent loop, the harness, data security"
learning_goal: "Section 4 divider (the largest) + a one-phrase frame"
learning_outcomes: [LO7]
chapter_ref: "§4 [for-slide-s18]"
visual_brief: "A large «Section 4» centered (mega 120pt gold outline). Below it — «Agents». Frame phrase 20pt. At the bottom — the roadmap bar (6 cards), gold marker on «4 Agents»."
interaction: none
---

# Visible content

## Title bar
(none — section divider)

## Body
[Center — mega «Section 4», 120pt gold outline]
**Section 4**

[Below it — 36pt deep]
**Agents**

[Frame phrase, 20pt semi-bold light]
*From an interlocutor in a chat window — to a component of a production system. And who sees the data in the chain.*

[Bottom — roadmap bar: 6 cards]
0 Opening · 1 Prompt · 2 RAG · 3 Fine-tune · **4 Agents** *(gold marker — current)* · 5 Framework

## Speaker notes

This is the largest section of the lecture, and it is about how AI stops being an interlocutor in a chat window and becomes a component of a system. Up to now we discussed a single call and RAG as a way to get text; here the model gains the ability to return machine-processable data, reach out to external systems, and work in a loop. We will work through the mechanics of the API layer and the standard for connecting tools, then the agent loop itself and the distinction between a workflow and an agent, then — what a real assistant agent is assembled from, where its memory lives, and how all of this breaks. It is here too that the through-line theme of security truly stands up: as soon as the model gains tools, a question appears that a single call did not have — who sees the data at each step and what happens when untrusted content enters the context as a command. This is the section where the price of the wrong choice of architecture is measured not only in money but in leaks.

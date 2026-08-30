---
id: s18
type: process
duration_min: 1.5
assertion: "Agent = chat + orchestrator + external memory + tools"
learning_goal: "Agent architecture — what gets added to chat; the decision loop"
learning_outcomes: [LO1, LO4, LO7]
references: [weng-2023-agents, anthropic-2024-effective-agents, anthropic-mcp-2024]
visual:
  pattern: agent_react_pipeline
  primary: "Eyebrow pill «AGENT» at the top. Redesign (issue #153): a linear ReAct pipeline Plan→Act→Observe→Reflect (with the English gloss Plan/Act/Observe/Reflect in small type under each block) with an explicit loop-back arrow (instead of the hub-and-spoke v3.2). USER on the left initiates the cycle; Memory and Tools are labeled as resources that the «Act» step reaches for, with labeled «uses» connectors; an explicit loop-back arrow «continue» (Reflect→Plan). Issue #155 QA fixes #189/#190/#191: the USER circle is raised so its vertical center aligns with the center of the row of pipeline blocks (it was noticeably lower); the loop-back connector at «Reflect» is flipped to UP_ARROW (the flow goes from Reflect up into the horizontal gold bar, not into Reflect); the «stop → result to the user» arrow now runs an L-shaped route — a horizontal segment below the pipeline blocks (not crossing their text), then a short vertical riser upward, the arrowhead landing exactly at the lower edge of the (raised) USER circle."
---

# Agent = chat + orchestrator + external memory + tools

## Assertion

Agent = chat + orchestrator + external memory + tools.

## Visual

Eyebrow pill «AGENT» in the top-left corner — the same pattern as s15/s16/s17/s19/s19a. Redesign (issue #153, replacing the weak v3.2 hub-and-spoke diagram): a USER icon on the left sends a goal into a linear horizontal pipeline of 4 stages — Plan → Act → Observe → Reflect (a small English gloss «(Plan)/(Act)/(Observe)/(Reflect)» under each name), each stage a block with a RIGHT_ARROW connector to the next. Under the «Act» stage — a teal-tinted label «Tools: API, files, code, search» with a labeled «uses» connector. Under the «Observe» stage — a label «Memory: vector DB, files, logs», also with a «uses» connector. From «Reflect» an explicit gold loop-back arrow runs back to «Plan», labeled «continue — the cycle repeats» — visually showing the loop. From «Reflect» there is also a «stop → result to the user» arrow — the result is returned to the user. A reference to Yao et al. 2022 (arXiv:2210.03629) at the bottom.

**Issue #155 Round 2 QA fixes (#189, #190, #191):**
- **#189** — the USER circle was noticeably lower than the row of pipeline blocks (circle center ~4.10" vs. pipeline-row center ~3.225" vertically in the 7.5"-tall slide). Raised so the vertical center of the USER circle aligns with the center of the «Plan/Act/Observe/Reflect» blocks; the «User» label under the circle shifted automatically (it is computed from `user_y`).
- **#190** — the loop-back-bar connector at the «Reflect» block was `DOWN_ARROW` (visually read as «the bar feeds into Reflect»), flipped to `UP_ARROW` — now it explicitly shows that the flow goes FROM «Reflect» up into the horizontal gold bar «continue — the cycle repeats», which then carries it leftward to «Plan».
- **#191** — the «stop → result to the user» arrow used to end in mid-air at the old (lower) USER position. Rerouted as an L-shape: a horizontal segment runs below the pipeline blocks at the previous height (not cutting through the blocks' text), then a short vertical riser (`UP_ARROW`) rises exactly to the lower edge of the new (raised) USER circle. The label is shifted to the right of the riser so it isn't clipped.

## Speaker notes

The agent is the next layer after chat. Compared with chat, an agent adds three components that chat did not have.

The first component is the orchestrator. The control logic: plan, decision loop, critique. The orchestrator looks at the user's goal, breaks it into steps, chooses which tool to apply at each step, and decides when to stop.

The second is external memory. Unlike chat, an agent has memory beyond a single session: a vector database (a database optimized for similarity search over embeddings; more on this later in the course), a file system with intermediate results, a log of its own previous actions.

The third is tools. The ability to call external APIs, read and write files, execute code, do web search. Each tool is a function with a description: what it does, what parameters it takes, what it returns. The orchestrator chooses which tool to apply at each step.

The agent's work cycle, the basic ReAct model — Reasoning plus Acting. The plan step: the orchestrator and the LLM formulate a plan of action. The act step: a tool is chosen and called with concrete parameters. The observe step: the tool's result is observed, written to memory, passed back to the LLM. The reflect step: the LLM thinks over the result — is the goal reached or not, is another step needed. If the goal is reached or there have been too many iterations — stop. Otherwise — the next step.

The canonical formulation from Lilian Weng's work: Agent equals LLM plus Memory plus Planning plus Tool Use. Canonical agent products: Claude Code by Anthropic — an agent in the terminal for development. Devin by Cognition Labs — a cloud coding agent. OpenAI Operator — an agent for web tasks. AutoGPT — an open-source autonomous agent.

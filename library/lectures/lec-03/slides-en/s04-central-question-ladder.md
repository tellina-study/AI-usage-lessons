---
id: s04
type: assertion_visual
section: "Section 0. Opening"
duration_min: 3
assertion: "The answer to «which architecture?» is a 6-rung ladder and the rule of climbing only when the task requires it"
learning_goal: "The central question large + the ladder (lecture map) with a disclaimer"
learning_outcomes: [LO7, LO4]
chapter_ref: "§Introduction [for-slide-s04]"
visual_brief: "The central question large (28pt bold deep) at the top. Below it — a ladder of 6 rungs bottom-up: ordinary code → a single call → RAG/context → workflow → agent → multi-agent. Each rung is an Ocean rounded box. The bottom «ordinary code (no AI)» is the gold accent. Disclaimer 12pt italic: the ladder is a map, not a requirement to understand everything now."
interaction: none
---

# Visible content

## Title bar
"The central question of the lecture"

## Body
[The central question large, 28pt bold `#21295C`]

> **I have a task and access to an LLM. Which architecture do I choose — and when is the right answer "not AI"?**

[Below the question — a ladder of 6 rungs, bottom-up, each rung in an Ocean rounded box]

6. Multi-agent
5. Agent (loop plan → act → check → iterate)
4. Workflow (predefined paths)
3. RAG / context engineering
2. A single LLM call (prompt; + CoT *reason step by step*, + few-shot *examples in the prompt*)
1. **Ordinary code (no AI)**  *(gold accent — the reference point)*

[Rule to the right of the ladder]
**Climb to the next rung only when the task has a requirement the current one does not close.**

[Disclaimer, bottom, 12pt italic]
*The ladder is the lecture map, not a requirement to understand everything now. We will work through each rung separately.*

## Speaker notes

This is the central question of the whole lecture, to which we will keep returning in every section: I have a task and access to an LLM — which architecture do I choose, and when is the right answer "not AI"? Note the second half of the question. It is not rhetorical. One of the things this course teaches is the ability to say "AI is not needed here," and this lecture turns that skill into a tool.

The answer will be a ladder of six rungs — it is on the slide. Bottom-up: ordinary code without AI; a single model call with a good prompt; RAG or context engineering; a workflow with predefined paths; an agent with a dynamic loop; and at the top, multi-agent. The rule for moving along this ladder is the single and central one for the whole lecture: stay on the lowest rung that closes the task's requirements, and climb to the next only when there is an explicitly stated requirement the current rung does not close. Every climb is paid for with new failure modes, cost, latency, degraded auditability, and a new attack surface.

Note that the bottom rung is ordinary code without AI. The ladder of AI system architectures begins with the question "is AI even needed here." The Air Canada case from the opening is exactly the situation where an engineer climbed to a rung with generation where the task lived on the lower rung of deterministic code. And one last, important thing: this ladder is the lecture map, not a requirement to understand everything right now. We will work through each rung separately and, for each, state when you should not climb to it. For now it is enough to remember only the structure and the rule.

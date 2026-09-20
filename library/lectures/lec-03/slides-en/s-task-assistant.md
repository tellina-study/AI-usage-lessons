---
id: s-task-assistant
type: assertion_visual
section: "Section 1. The prompt and its limits"
assertion: "An assistant with tools isn't a binary choice — it's a mini-ladder, one-shot → tool-use → agent; the failure is jumping straight to an agent"
learning_goal: "Task pattern 1: the §1.1 ladder applied to one class; the on-point failure — an over-engineered agent"
learning_outcomes: [LO7]
chapter_ref: "§1.10 [for-slide-task-assistant]"
interaction: none
---

# Visible content

## Title bar
«An assistant with tools: climb the mini-ladder»

## Body
[Setup]
The user isn't asking for "text" — they're asking you to "do something": look something up in an external system and/or take an action.

[Architecture: one-shot → tool-use → agent]
Knows the answer, no action needed → a single call. Access is needed, the steps are known in advance → tool-use in code. Steps are unknown, there's a way to check progress → an agent.

[Gold callout — failure]
Jumping straight to an agent where a single tool call would have been enough — that's the $4,200 loop (§4).

## Speaker notes

The first task pattern is an assistant with tools. The setup is simple: the user isn't asking you to "write text" — they're asking you to "do something": look something up in an external system, or take an action. The right architecture here isn't a binary choice between "chat or agent" — it's the same ladder from the start of the section, applied to one class of tasks.

The first rung is a single call. If the model already knows the answer and no external action is needed (rephrase, explain, summarize), that's cheap, fast, and predictable. The second rung is tool-use or a workflow. If you need access to data or an action, but the sequence of steps is known in advance and can be laid out in code, the model formulates the tool call, while the control flow and the checkpoints live in code, not in the model's head. The third rung is a full agent. It's justified only when the steps aren't known in advance, on-the-fly adaptation is needed, and there's a way to check progress. The cost of climbing each rung is rising latency, cost, and the risk of compounding errors.

For this to be an engineering recipe rather than a wish, let's name what you control and how you validate it. The parameters of this class: tool granularity (coarse operations vs. atomic ones), strict input schemas validated at the boundary, the tool_choice mode (auto, forced, or disabled), and a mandatory iteration limit with a token budget — a guard against a runaway loop. Validation is two-stage: first, check the tool call's arguments before hitting the external system — reject a malformed request at the boundary and return the model a structured error it can interpret; second, check that the final answer relies on the tools' results, not on the model's memory. The second check removes what's called parametric fallback: after a tool failure, the model sometimes "decides" its own knowledge is good enough and stops searching — breaking exactly the freshness guarantee the tool was wired in for.

The most common mistake in this class is jumping straight to an agent where the task is predictable and a single tool call would have been enough. That's exactly the failure we'll walk through in the agents section: the four-thousand-two-hundred-dollar loop, where a predictable sync job was handed to an agent instead of a simple retry script. The rule: climb the mini-ladder only when the task requires it — not because "an agent sounds more powerful."

---
id: s21
type: process
section: "Section 4. API · tools · MCP · agents + security"
duration_min: 3
assertion: "An agent = the loop plan → act → check → iterate; each step is a place of failure, and the check step must not be the model's self-assessment"
learning_goal: "The agent loop + check as the load-bearing step (callback s06)"
learning_outcomes: [LO7]
chapter_ref: "§4.3 [for-slide-s21]"
visual_brief: "A closed 4-step loop (plan → act → check → iterate) with clockwise arrows + an explicit return arrow iterate→plan + a «repeats» label. Under each step — a failure mode. The check step — gold accent. ReAct/Reflexion — 1 line."
interaction: none
---

# Visible content

## Title bar
«The agent loop: plan → act → check → iterate»

## Body
[Inline-define, 16pt italic]
*An agent — an architecture where the model does not make one pass but works in a loop, dynamically determining the sequence of steps itself.*

[A closed 4-step loop, Ocean rounded boxes, clockwise arrows + return]

**Plan** → states the next step
*failure mode: a myopic / looping plan (does not see the accumulated cost)*

→ **Act** → calls a tool (function calling)
*failure mode: the tool fails / stalls, and there is no branch for it*

→ **Check** → is the goal reached, is the result correct  *(gold accent)*
*validation against an EXTERNAL criterion — not the model's self-assessment (callback s06)*

→ **Iterate** → the loop repeats
*failure mode: no external limit on iterations / cost / time → a loop*

⟲ return to Plan — **repeats**

[Sub-caption, bottom, 12pt italic]
*Loop patterns (ReAct, Reflexion, Plan-and-Execute) — in the chapter. To design an agent = to design defenses at each of the 4 steps.*

## Speaker notes

Now there is everything for the next rung. A single call can reason; RAG pulls knowledge; function calling reaches external systems; MCP standardizes connection. An agent is an architecture in which the model does not make one pass but works in a loop[1]: it plans a step, acts — calls a tool, observes the result, checks whether the goal is reached, and iterates, dynamically determining the sequence itself. The canonical formulation is plan, act, check, repeat; this is the ReAct pattern, alternating reasoning and actions, while Reflexion adds an explicit self-assessment after a failure. This is a "different AI" compared to a single call: there the model answered once, here it directs a process of many steps.

Let us work through the loop step by step, because each step is a place of a specific failure mode. Plan: the model states a step based on the goal and history; the failure mode is a myopic or looping plan, the model does not see the accumulated cost and time. Act: a tool is called; the failure mode is the tool failing or returning an error, and if there is no plan for it, a loop begins. Check: the result is assessed; the failure mode is no check or one that reduces to the model's self-assessment. Iterate: the loop repeats; the failure mode is no external limit on iterations, cost, or time. "An agent" is not one abstraction but four steps, each with its own way to break; to design an agent means to design defenses at each of the four.

Let me emphasize the element that carries the main through-line load of the course — the check step[2]. And here the lesson about the faithfulness of reasoning returns starkly: the check must not be "the model asked itself and answered itself that everything is fine." Self-assessment is subject to the same unfaithfulness that we saw on the slide about the limit of chain-of-thought — it is an illusion of control: the explanation "I checked" is produced by the same sampling as the answer itself. A reliable check is validation against an external criterion: a schema, a test, an invariant check, a comparison against a source of truth, and in significant decisions — a human validator. Without an external check, the agent loop is a loop that confidently goes in the wrong direction. This is a direct bridge to agent failures.

Sources:
[1] Yao et al. 2022 — ReAct (plan→act→check→iterate) — alternating reasoning and actions; each step is a place of failure. https://arxiv.org/abs/2210.03629
[2] Anthropic — Reasoning Models faithfulness (check ≠ self-assessment) — the check step — validation against an external criterion, not the model's self-assessment. https://www.anthropic.com/research/reasoning-models-dont-say-think [VFY-day-of]

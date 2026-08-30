---
id: s23
type: case_study
section: "Section 4. Agents"
duration_min: 3
assertion: "An agent burned $4,200 in 63h in a loop because it does not «see» the budget — a retry script would solve the same task for almost free; 5×99% = 95%, not 99% — reliabilities multiply"
learning_goal: "Agent failures: a loop without limits (+ the retry comparison baseline) + reliability compounding + multi-agent fragility"
learning_outcomes: [LO7]
chapter_ref: "§4.10 [for-slide-s23]"
visual_brief: "3 failure cards: (1) $4,200/63h loop; (2) reliability compounding 5×99%≈95%; (3) multi-agent fragility. Gold — «$4,200» / «95%». Footer 12pt italic — sources + the framing «illustrative / single-author»."
interaction: none
---

# Visible content

## Title bar
«Agent failures»

## Body
[3 failure cards in an Ocean rounded box]

**1. A loop without limits**
An agent on "sync the orders" got HTTP 429 → plan→call→429→replan→… → **$4,200 in 63 hours**  *(gold accent)*
*Why:* the agent does not "see" the accumulated cost, the time, or the repetition
*Correctly:* the task is predictable → a retry-with-backoff script, not an agent; budget/loop limits OUTSIDE the agent

**2. Reliability compounding**
5 steps at 99% → 0.99⁵ ≈ **95%**; 10 → ≈ **90%**; 20 → ≈ **82%** — reliabilities multiply
*Conclusion:* "improve the step" is a weak lever; "fewer hops + validation between steps" is a strong one

**3. Multi-agent fragility**
dependent subtasks → parallel subagents make conflicting implicit decisions
*Correctly:* a single-threaded linear agent; multi-agent — only for broadly parallel, independent work

[Footer, 12pt italic]
*The $4,200 loop — a single-author postmortem 2026-04 (illustrative, numbers rounded); reliability compounding — MindStudio 2025–2026.*

## Speaker notes

The agent loop has four places of failure; the three classes of failures below are these modes in dated cases, each with a lesson and an alternative. First. A team put an autonomous agent on "sync the orders in the CRM" — a predictable task. The external API hit a rate limit and started returning error 429[1]. The agent, having no branch for 429 in its plan, acted by its nature: plan, call, 429, replan, again — thousands of times an hour; the total about $4,200 over sixty-three hours (postmortem by Sattyam Jain, 2026-04; single-author, numbers rounded, illustrative). The agent constructively understands neither the accumulated cost, nor the time, nor that the actions are identical. The lesson: without hard external limits, "try until it works" is executed literally and to the point of ruin.

It is important to name the comparison baseline. An ordinary deterministic retry script with increasing delay solves the same task many times cheaper: got 429, waited a second, two, four, eight, retried a limited number of times — and either it is done, or it quickly reported "couldn't, intervention needed." A few lines of code, seconds to minutes, costs almost nothing. That is, $4,200 is not the price of automating synchronization in general but the price of the wrong choice of architecture for a predictable task. The alternative is twofold: budget gates outside the agent and, at the architecture level, a retry script rather than an agent.

Second. In a chain where the failure of any component spoils the result, reliabilities multiply[2]: five steps at 99% give about 95%, ten — about 90%, twenty — about 82%. The reasoning "each step almost always works, therefore so does the chain" is mathematically false. The consequence: improving an individual agent barely moves system reliability, while halving the number of steps gives a comparable effect more cheaply. The lesson: "improve the model" is a weak lever, "fewer hops plus validation between steps" is a strong one. Third. When subtasks are dependent, parallel subagents make conflicting implicit decisions and give an incompatible result. The lesson: a multi-agent[3] by default is not an upgrade; for tasks with dependencies it is worse than a single linear agent. In all three, "a more complex architecture" meant "less reliable," not "more advanced."

Sources:
[1] Sattyam Jain 2026 — The Agent That Burned $4,200 in 63 Hours — a loop without limits on HTTP 429; a retry script would solve the task for almost free. https://medium.com/@sattyamjain96/the-agent-that-burned-4-200-in-63-hours-a-production-ai-postmortem-d38fd9586a85 [VFY-day-of]
[2] MindStudio — Reliability Compounding Problem — 5×99%≈95%, 10→90%, 20→82% — reliabilities multiply. https://www.mindstudio.ai/blog/reliability-compounding-problem-ai-agent-stacks
[3] Cognition — Don't Build Multi-Agents (fragility) — dependent subtasks → parallel subagents make conflicting decisions. https://cognition.ai/blog/dont-build-multi-agents

---
id: s-agent-when
type: assertion_visual
section: "Section 4. Agents"
duration_min: 2.5
assertion: "An agent fits an open, unpredictable task; a predictable one → workflow; multi-agent only under a specific trigger. Reason for caution: reliability drops as p^n — the numbers and measurements are on the next slide"
learning_goal: "Judgment: when an agent, when a workflow of agents, when multi-agent; topology + the Cognition/Anthropic reconciliation (§4.3 + reliability)"
learning_outcomes: [LO7, LO4]
chapter_ref: "§4.3 [for-slide-s22, s22a-multi, agent-reliability]"
subtype: assertion_visual
new_in_v4: "#196 WAVE 3 — agent-vs-workflow judgment (failure/limitation)"
changed_in_v6d2: "#196 WAVE D2 owner #16 — DROP clown meme; top-down decision framework + Kim et al. 2512.08296 + Cognition/Anthropic reconciliation"
---

# Visible content

## Title bar
«An agent fits an open task; multi-agent only under a trigger»

## Body
[Top-down decision ladder]
1. Predictable → workflow (steps known in advance).
2. Unpredictable and valuable → a single agent (steps depend on intermediate results).
3. Multi-agent → only under a trigger (widely-parallel independent subtasks).

[Why "only under a trigger"] chain reliability drops as p^n — every extra step multiplies the probability of success. Numbers and measurements — on the next slide.

[Topology] a swarm of peer agents amplifies errors noticeably more than a coordinator does; more connections = faster collapse.

[Reconciliation] Anthropic vs Cognition: parallelize independent reads, not decisions with dependencies.

[Gold] Start with one strong agent; multi-agent buys quality by burning tokens.

## Speaker notes

This is a judgment slide: when to use an agent, when a workflow, when several agents. The logic runs top-down. If the task is predictable — the steps are known in advance — use a workflow: paths predefined in code, auditability. If it is unpredictable and the value justifies the multiple-fold cost — a single agent: the steps depend on intermediate results, and that needs the flexibility of a loop. And only for a specific case — several agents. It matters not to settle for the word "trigger" but to name those cases explicitly, because outside them multi-agent is the wrong tool.

There are three conditions under which multi-agent is justified. The first — widely-parallel independent reads, not decisions: for example, reading a hundred sources in parallel and rolling them into one report — that is how Anthropic's research agent is built, where the reading subtasks do not depend on each other. The second — independent perspectives for cross-checking: for example, five agents independently search for an answer, and the result is then taken by vote; disagreement between them is itself a signal. The third — isolated sub-domains with separate tools and permissions: for example, a separate agent for billing and a separate one for infrastructure, each with its own set of access rights, and mixing them is dangerous. If your task does not fall into any of these three cases — stay with a single agent.

Why such caution about the number of steps — because reliability drops as p to the power of n, not averaged out. In a chain of n steps where a failure at any one spoils the result, reliabilities multiply rather than average. Every extra agent adds steps and connections, which means it lowers overall reliability. The specific numbers and a live benchmark measurement are on the next slide; here the principle itself matters: "almost always" at each step multiplies into "fairly often not" at the output of the whole system.

Topology here is not a detail but a decisive factor. By the measurement of Kim and co-authors, preprint 2512.08296, a decentralized "swarm" of peer agents with no single center amplifies errors noticeably more than a single coordinator does: more connections between agents means a faster collapse, and we will look at the specific multipliers on the next slide. And separately, two claims that students often hear as a contradiction need to be reconciled. Anthropic says multi-agent wins research tasks; Cognition writes "don't build multi-agents." There is no contradiction: parallelize independent reads — a broad search where subtasks don't depend on each other — but not decisions with dependencies, where parallel subagents make conflicting implicit choices and spoil the result. Anthropic states the win literally: multi-agent works mainly because it helps spend enough tokens on the task, not because of coordination magic[1].

The practical takeaway: start with one strong agent. Multi-agent buys quality by burning tokens, not by coordination magic; the multiple-fold cost estimates are on the next slide. If a task does not decompose into widely-parallel independent reads and the value does not justify the multiple-fold cost, it is the wrong tool.

Sources:
[1] Anthropic — Multi-Agent Research System ("spend enough tokens") — multi-agent wins research tasks through token volume; parallelize reads, not decisions. https://www.anthropic.com/engineering/multi-agent-research-system [VFY-day-of]
[2] Kim et al. 2026 (arXiv:2512.08296) — topology: a decentralized "swarm" amplifies errors more than a coordinator — specific multipliers on the next slide. https://arxiv.org/abs/2512.08296 [VFY-day-of]

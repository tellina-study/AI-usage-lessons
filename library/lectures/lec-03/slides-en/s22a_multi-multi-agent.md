---
id: s22a-multi
type: assertion_visual
section: "Section 4. Agents"
duration_min: 3
assertion: "Multi-agent is NOT an upgrade by default: p^n (95%×10=60%); a swarm amplifies 17.2× vs a coordinator at 4.4×"
learning_goal: "The reliability math of a chain + coordination topology; the criterion for when multi-agent is justified"
learning_outcomes: [LO7]
chapter_ref: "§4.3 [for-slide-s22a-multi]"
verify_day_of: true
---

# Visible content

## Title bar
"Multi-agent by default — not an upgrade"

## Body
[Left — the chain math]
n steps, a failure of any one spoils the result → reliabilities **multiply**: p^n
95% per step × 10 steps ≈ **60%** (0.95¹⁰≈0.599)
90% per step × 10 steps ≈ **35%**
The intuition "each step almost always works" is mathematically false

[Right — topology]
Independent "swarms" of equal-rank agents amplified errors **17.2×**
A single coordinator held them to **4.4×**
→ **a coordinator is more reliable than a swarm**

[Panel — Anthropic verbatim]
*"Multi-agent systems work mainly because they help spend enough tokens to solve the problem"* — the gain comes from token volume, not from "coordination magic"

[Gold callout, bottom]
**Do not build multi-agent unless the task decomposes into broadly parallel, independent, high-value subtasks.**

## Speaker notes

Let us take on separately why multi-agent is not a win by default, because this is one of the frequent architectural mistakes, and it has a simple, vivid math. In a pipeline of n sequential steps where a failure of any step spoils the outcome, the reliabilities multiply rather than average: the overall chance of success is approximately p to the power of n. Hence the counterintuitive numbers: even at ninety-five percent reliability per step, ten steps in a row yield only about sixty percent overall reliability, and at ninety percent per step — already about thirty-five. The engineer's intuition "each step almost always works, so the whole chain almost always works" is mathematically false: "almost always" per step multiplies into "fairly often not" at the output of the whole system.

Next — the question of topology, that is, how exactly several agents are organized among themselves. With the same number of agents, independent "swarms" of equal-rank agents working without a single center amplified errors nearly seventeen times, whereas centralized orchestration with a single coordinator held error amplification to under five times. The conclusion is direct: orchestration with a single coordinator is more reliable than a "swarm" of equal-rank agents, and not the other way around, even though intuitively a "swarm" seems the more flexible and scalable solution.

Here it is worth quoting Anthropic's position verbatim, because it is sobering: multi-agent systems work mainly because they help spend enough tokens to solve the problem — that is, the gain is largely explained by the volume of computation, not by some special coordination magic between agents. The practical advice from the same sources is to start with a single strong agent: for many tasks, single calls with good retrieval and examples suffice, while teams spent months on complex multi-agent architectures only to find that more precise prompting of one agent gave an equivalent result more cheaply. Hence the criterion: do not build multi-agent unless the task decomposes into broadly parallel, independent, high-value subtasks — otherwise the coordination overhead and the manyfold growth in token cost will outweigh any benefit from parallelism.

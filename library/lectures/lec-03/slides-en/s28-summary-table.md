---
id: s28
type: summary
section: "Section 5. The decision framework"
duration_min: 2.5
assertion: "A summary table 'mechanism → boundary → what to do' across all architectures + 'not AI'"
learning_goal: "Collect all mechanisms of the lecture into one reference table of boundaries and measures"
learning_outcomes: [LO7, LO4]
chapter_ref: "§5.3 [for-slide-s28]"
interaction: none
---

# Visible content

## Title bar
"Summary: mechanism → boundary → what to do"

## Body
[Table, compact]

| Mechanism | Where it breaks | What to do |
|---|---|---|
| Prompt / role | does not raise accuracy, only tone | context + RAG for accuracy |
| Chain-of-thought | faithfulness is low (25-39%) | check the result, not the reasoning |
| RAG | "returned something" ≠ "returned the right thing" | strict grounding + observability |
| Fine-tune / PEFT | not the place for facts, forgetting | eval loop + versioning |
| Agent loop | plan/act/check/loop without boundaries | budget/loop limits outside the agent |
| Equipment / memory | each slot is a trade-off | add only for a requirement |
| Multi-agent | p^n, coordination is fragile | coordinator > swarm; only broadly parallel |
| Security | injection, ZDR does not cover everything | least-privilege + data map |
| **Not AI at all** | deterministic and verifiable | **ordinary code** |

[Gold callout, bottom]
**To know a tool is to know its boundary.** The architectural choice is the search for the LOWEST rung that meets the task's requirement.

## Speaker notes

Let us collect the whole material of the lecture into one reference table — not for memorizing by heart, but as a tool you can return to when designing a real system. Every mechanism has its boundary of applicability and its countermeasure. The prompt and the role in it do not raise factual accuracy, only tone and depth of exposition — for accuracy you need competent context and RAG. Chain-of-thought gives a gain on multi-step tasks, but its verbal reasoning cannot be audited: the faithfulness of the explanation is under half the cases even in strong models — which means you must check the result, not the verbalized chain. RAG solves the problem of stale knowledge, but the very fact that the system returned something does not mean it returned the right thing — you need strict grounding on the source and continuous monitoring.

Fine-tuning and its parameter-efficient variants are a poor place for facts and carry the risk of catastrophic forgetting, so an eval loop and versioning of the weights and dataset are mandatory. The agent loop is four steps, each with its own failure mode, and without external limits on budget and number of iterations it can literally run a task into ruin. The agent's equipment — memory, instructions, skills, subagents, access to tools — is not a free win but a trade-off worth adding only for a concrete task requirement. Multi-agent systems suffer from the mathematical multiplication of failure probabilities along the chain of steps, and a single coordinator is more reliable than an equal-rank "swarm"; they are worth building only for broadly parallel, independent subtasks. The security of an agent system rests on the principle of least privilege and a data map per feature, because injection via untrusted content is not solved as a problem, and the zero-data-retention mode does not cover the whole chain of third-party tools.

And the last row of the table — load-bearing across the whole lecture: if the task is deterministic and verifiable, the right answer is ordinary code with no AI at all. To know a tool is to know its boundary; a good architect looks not for the most powerful of the available architectures but for the lowest rung that actually meets the task's requirement.

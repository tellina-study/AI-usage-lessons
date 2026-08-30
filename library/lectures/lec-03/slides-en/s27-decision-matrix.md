---
id: s27
type: flowchart
section: "Section 5. The decision framework"
duration_min: 3
assertion: "The decision plan is a route of questions top to bottom with a stop at the first that triggers; the bottom priority: a deterministic verifiable task → ordinary code, STOP"
learning_goal: "The choice route (8 question steps) + «when not AI at all» (LO7)"
learning_outcomes: [LO7]
chapter_ref: "§5.2 [for-slide-s27]"
visual_brief: "A flowchart: 8 question steps top to bottom, each with a branch «yes → architecture (STOP) / no → next question». Step 1 (deterministic task → code) — top and with an explicit STOP. A compact axes table — on the right as reference material. A full-width bottom strip (gold-outlined)."
interaction: none
---

# Visible content

## Title bar
«The decision plan»

## Body
[A flowchart route in an Ocean rounded box: 8 question steps top to bottom, at each «yes → architecture (STOP) / no → next»]

1. **Is the task deterministic and verifiable?** (a price, a policy, parsing, validation, arithmetic, routing) → **yes: ordinary code, STOP**
2. **Does a single LLM call (+ CoT) close it?** → **yes: prompt, STOP**
3. **Must the answer be verifiable against a source?** (regulated / legally significant) → provenance mandatory: RAG with strict grounding or code
4. **Does the knowledge change often / is provenance needed?** → **yes: RAG** (if §2.3 does not block it); **no:** stable and small → long context + cache
5. **Is behavior / tone / format / policy needed, not facts?** → **yes: fine-tuning (PEFT)**
6. **Multi-step, sequence known in advance?** → **yes: workflow**; **no** and the value justifies → agent + budget/loop limits
7. **Subtasks broadly parallel, independent, valuable?** → **yes: multi-agent**; **no:** a single linear agent
8. **Is the data sensitive?** *(in parallel)* → a data map, least-privilege, ZDR/BAA, a human validator

[Right — a compact axes table, 12pt, reference material]
knowledge volume · frequency of change · freshness/provenance · cost · latency · auditability/determinism · risk of nondeterminism/loops

[Full-width bottom strip, gold-outlined]
**Step 1 is the most important line: if the task is deterministic, verifiable, repeatable → ordinary code, no AI. AI would only add nondeterminism + cost + latency + a surface for prompt injection.**

[Sub-caption, 12pt italic]
*A route, not a sum of points: you stop at the first question that triggers and name the deciding question for the task.*

## Speaker notes

The ladder says "do not climb without need," but does not say along which axes to measure the need. This is given by the decision plan — not a table for summing points but a route of questions that you go through top to bottom for a specific task, stopping at the first that triggers[1]. The first question and the cheapest filter: is the task deterministic and verifiable[2] — a fixed price, a policy, parsing, schema validation, arithmetic, rule-based routing? If yes — ordinary code, stop here, the other questions are not needed. No — does a single call close the task, possibly with step-by-step reasoning? If yes — a prompt. Next the deciding question of regulated domains: must the answer be verifiable against a source? If yes, the further choice must ensure provenance — strict grounding in a source or code, free generation excluded; this is the Air Canada diagnosis.

The next questions: the knowledge changes often or provenance is needed — RAG, if not blocked by the "when NOT" criteria; the knowledge is stable and small — long context with a cache. Behavior, tone, format, policy is needed, not facts — fine-tuning in the form of PEFT. The task is multi-step and the sequence is known in advance — a workflow; fundamentally unpredictable and the value justifies the rise in cost — an agent with budget limits. Subtasks broadly parallel, independent, and valuable — a multi-agent, otherwise a single linear agent. And in parallel, at any step: the data is sensitive — a per-feature data map, least-privilege, ZDR or a contract, a human validator. The skill that the main learning goal checks is not to count by the table but to go through the route and name the deciding question for this task. "By the score it came out RAG" is not a justification; "the provenance question is deciding, the answers are legally significant, therefore RAG with strict grounding and a human validator" is a justification. And the bottom strip is the most important line of the lecture: a deterministic task is solved with ordinary code, and Air Canada is the choice of a generative architecture for a task from this bottom strip.

Sources:
[1] Anthropic — Building Effective Agents (the choice route) — a route of questions top to bottom; step 1 — a deterministic task → ordinary code, STOP. https://www.anthropic.com/research/building-effective-agents
[2] McCarthy Tétrault — Air Canada (the bottom line of the matrix) — a generative architecture on a deterministic task = a bottom-line error. https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot

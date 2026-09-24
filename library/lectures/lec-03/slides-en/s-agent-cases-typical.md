---
id: s-agent-cases
type: case_study
section: "Section 4. Agents"
duration_min: 3
assertion: "Six typical agentic tasks on one schema (coding / support at Air Canada+Klarna / ETL / research / browser-Operator / SRE ITBench): task → loop shape → where it breaks → would a workflow be better?"
learning_goal: "Typical agentic cases: where an agent is justified, where part of the task should be rolled back into a workflow (§4.9b)"
learning_outcomes: [LO7, LO4]
chapter_ref: "§4.9b [for-slide-agent-cases]"
subtype: case_study
new_in_v6d2: "#196 WAVE D2 owner #18 — typical agentic cases (before the failure catalog)"
---

# Visible content

## Title bar
«Six typical agentic tasks on one schema»

## Body
[Table: task · loop shape · where it breaks (number/case) · better as a workflow?]
1. Coding agent (Claude Code / Cursor) — read the repo → plan → edit → test → PR; breaks on large refactors; NO — open-ended code search requires agency.
2. Customer support (Air Canada · Klarna) — classify → fetch policy → resolve/escalate; Air Canada: the bot invented a policy → the tribunal made it pay; Klarna "−700 agents" → brought people back; often YES for the risk part.
3. ETL / pipeline — spot drift → patch → validate; silent bad transforms; mostly YES, the agent only on the edge of the fix.
4. Research agent — plan sub-questions → search → synthesize → cite; ~15× tokens, hallucinated citations; NO for open-ended, YES if it's a fixed lookup.
5. Browser / Operator — screenshot → plan a UI action → click; OSWorld ~38%, Operator discontinued; for consequential actions YES — a real API.
6. SRE / ops (ITBench) — telemetry → hypothesis → fix; ITBench ~14%; for the fix itself YES — workflow + confirmation.

[Gold] An agent — for the adaptive edge; a workflow with gates — for the trunk and consequential actions.

## Speaker notes

Let's walk through six typical agentic tasks on one schema: task, loop shape, where it breaks, would a workflow be better. This translates the general ladder principle into concrete working scenarios, with real anchors. Individual figures are illustrative, but the classes and anchors are real.

First — a coding agent, Claude Code or Cursor. The task is to implement or fix code across an entire repository from a natural-language statement. The loop: read the repo, plan, edit files, run tests, see failures, iterate, open a PR. It breaks on large, ambiguous refactors and on getting stuck looping on flaky tests. Would a workflow be better? No — open-ended code search genuinely requires agency; this is the canonical case where an agent is justified.

Second — customer support, and here there are two instructive cases. Air Canada[1]: a support bot invented a 90-day refund window, and the tribunal ruled the airline liable to pay out — a policy hallucination became legally binding. Klarna publicly celebrated an AI that replaced 700 agents, then rebuilt human capacity, because edge cases and escalation judgment brought people back into the loop. Would a workflow be better? Often yes for the risky part: refunds and policy answers want deterministic routing with guardrails, not free generation.

Third — an ETL agent, a self-healing pipeline. The loop: spot a schema drift, analyze the impact, generate a transform, validate, apply under a guardrail. It breaks because silent bad transforms corrupt data at scale, and nondeterminism is dangerous in a pipeline that needs to be auditable. Mostly yes — the trunk is deterministic, and an agent belongs only on the narrow step of fixing the drift. Fourth — a research agent, Deep Research. It breaks with a cost blow-up of roughly fifteen times in tokens and with hallucinated citations. No for genuinely open-ended broad research, yes if it's actually a fixed lookup.

Fifth — a browser agent, Operator. The loop: a screenshot and the DOM, plan a UI action, click, observe. On the OSWorld benchmark the first generation scored around thirty-eight percent[2] of tasks completed, and the Operator product itself was discontinued — a live lesson in "hype — market exit." For any consequential action, payments and forms — yes, use a real API if one exists. Sixth — an SRE agent. On the ITBench benchmark, frontier models autonomously resolve only about 14% of scenarios, so the real value is narrowing the search space and leaving the judgment to people. The cross-cutting principle: an agent — for the adaptive edge, a workflow with gates — for the trunk and for consequential actions; the Operator and ITBench numbers mean "narrow the search," not "replace the person."

Sources:
[1] McCarthy Tétrault — Air Canada (bot invented a policy) — a policy hallucination became legally binding; don't let a free-running agent speak for policy. https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot
[2] OSWorld / WebArena / ITBench — agentic-task benchmarks — Operator ~38% OSWorld; SRE ~14% ITBench — narrow the search space, not replace the person. [VFY: canonical URL not confirmed, present as independent live-eval registry data, not as a primary source]

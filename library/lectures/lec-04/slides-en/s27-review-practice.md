---
id: s26
type: assertion_visual
section: "Section 5. Review + Security — the discipline of skepticism"
duration_min: 3
assertion: "The review practice — not \"which AI reviewer is better\", but two human practices: adversarial review with fresh context (not the one who wrote it) + retained human accountability; AI review = assist, not gate"
learning_goal: "The review practice: adversarial fresh-context + accountability; tools secondary; judgment assist/gate"
learning_outcomes: [LO7, LO1]
chapter_ref: "§5.2 [for-slide-s26]"
references: [willison-testing, osmani-70-percent]
verify_day_of: false
visual_brief: >
  assertion_visual: left — two human practices in an Ocean rounded box: (1) adversarial review with fresh context
  (writer-reviewer: reviewed by NOT the one who wrote it; the reviewer starts with clean context — sees only the diff + acceptance criteria →
  reduces the "I wrote it, so it's right" bias) · (2) retained human accountability (Osmani: "if you can't explain it, don't commit").
  Right — the fundamental trade-off "detection recall ↔ noise" (no point makes AI review an autonomous gate).
  Secondary row, muted: Copilot review, Cursor Bugbot, Qodo Merge, Rovo Dev (review against the spec in Jira), Anthropic adversarial reviewer.
  Judgment: durable — AI review as assist/first pass; hype — AI review as gate. Gold — "the decision and accountability are the human's". Lucide icons.
interaction: none
---

# Visible content

## Title bar
The review practice — two human practices, not the choice of an AI reviewer

## Body
[Left — two human practices, Ocean rounded box]

**1. Adversarial review with fresh context** — the code is reviewed by **not** the one who wrote it; the reviewer starts with **clean context**: sees only the diff and the acceptance criteria. This reduces the "I wrote it, so it's right" bias (writer-reviewer, two passes).

**2. Retained human accountability** — AI review is an assist and a first pass, but **the decision and accountability are the human's**. Osmani: "if you can't explain it, don't commit".

[Right — the fundamental trade-off]
**Detection recall ↔ noise**: a stricter setting catches more bugs, but also more false alarms; a softer one has less noise, but misses. **No point on the trade-off makes AI review an autonomous gate.**

[Secondary row — tools, muted]
A first pass over the diff: GitHub Copilot code review, Cursor Bugbot, Qodo Merge, Atlassian Rovo Dev (review against acceptance criteria in Jira), Anthropic adversarial reviewer.

[Gold callout]
Durable pattern: AI review as an **assist / first pass**. Hype: AI review as a **gate** ("AI reviewed it — it can be merged").

## Speaker notes

What leads in the review phase is not the question "which AI reviewer is better" but two human practices that work regardless of which tool you use to execute them. The first — adversarial review with fresh context. The classic rule of good review: the code is looked at by someone other than the one who wrote it. AI lets you strengthen this cheaply — launch a reviewer with clean context that sees only the diff and the acceptance criteria, without the history of "why I did it this way" [1]. This reduces the main bias: "I wrote it, so it's right". In the human-AI variant one agent writes, another, fresh, nitpicks — writer-reviewer, two passes.

The second practice — retained human accountability. AI review is an assist and a first pass, but the decision and accountability remain the human's. Addy Osmani formulates this as a working rule: if you can't explain what this code does, don't commit it, even if the tests are green [2]. That is, AI review does not relieve you of the duty to understand what you are merging.

Why AI review cannot be made an autonomous gate — because of the fundamental trade-off between detection recall and noise. Set it stricter and you catch more bugs, but you get a stream of false alarms that the team quickly gets used to and starts ignoring, including the real ones. No point on this trade-off makes the AI reviewer someone you can trust with a merge without a human. The trade-off has a subtle trap that Anthropic names: if a reviewer-agent is told to "look for holes", by its nature it will find them even in healthy code — this is over-eagerness sliding into over-engineering [3]. The practical takeaway — strictly limit the review scope to correctness and explicit acceptance criteria, not "nitpicking in general"; this is authoritative because the conclusion is drawn from their own engineering practice of building review agents. The tools that give a cheap first pass over the diff are secondary. Durable pattern: AI review as an assist and a first pass; vendor hype: "AI reviewed it, it can be merged".

---
id: s33
type: case_study
section: "Section 6. Delivery · Operations · Documentation"
duration_min: 3
assertion: "Delivery is DORA-first: a mature pipeline first, then scale AI ('AI amplifies what is already there') + a hard human prod gate; AI consumes pipelines but does not own them; DORA — both halves (+throughput / -7.2% stability)"
learning_goal: "[SI] CI/CD+Ops practices: DORA-first + prod gate; the DORA pair, both halves; operations is the weakest phase"
learning_outcomes: [LO1, LO7]
chapter_ref: "§6.1 [for-slide-s33]"
references: [dora-report, osmani-70-percent]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study: left — the DORA-first practice in an Ocean rounded box: first mature delivery capabilities (automated tests, versions with cheap rollback,
  fast feedback, small batches), THEN scale AI ("AI amplifies what is already there"); inside — a hard human prod gate (irreversibility).
  A plate "AI consumes pipelines but does not own them" — there is no AI-CD product; the agent calls gh/aws/gcloud as a least-privilege user.
  Right — DORA BOTH HALVES (the main anti-one-sidedness visual, a paired diagram): +throughput / +7.5% docs AND -7.2% stability (negative for the 2nd year running).
  Plus a failure: scaling AI onto an immature pipeline → the DORA multiplier works the wrong way. Operations is the weakest phase (no system/runtime context; the agent report != source of truth — the Replit link).
  A secondary row muted: headless (Anthropic parity), AWS Q Operational Investigations over CloudWatch (assist, not replacement). Gold — "the AI multiplier works BOTH ways". Source references — inline right at the material (definition/claim/recommendation), NOT in a bottom footer; small and muted: DORA 2024/2025.
interaction: none
---

# Visible content

## Title bar
Delivery is DORA-first: a mature pipeline first, then scale AI

## Body
[Left — the DORA-first practice, Ocean rounded box]

It is not the tool that leads but the order: **mature delivery capabilities first** (automated tests, versions with cheap rollback, fast feedback, small batches), **then** scale AI. "AI amplifies what is already there".

Inside — a **hard human prod gate** (a rollout is irreversible).

**AI consumes pipelines but does not own them** — there is no "AI-CD product"; the agent calls `gh` / `aws` / `gcloud` as a **least-privilege user** inside the infrastructure.

[Right — DORA both halves]

**+ throughput**, **+7.5% documentation** — but **-7.2% delivery stability**, a negative link for the **second year running**.

A failure: scaling AI onto an **immature** pipeline → the DORA multiplier works **the wrong way**, instability grows.

**Operations is the weakest phase** of the cycle: no system and runtime context; the agent's report on the state != source of truth (a Replit echo).

[Gold callout]
The AI multiplier works **both ways**. Sustainable pattern: DORA-first + a human prod gate. Hype: "an AI-CD/ops product as a replacement for the human".

## Speaker notes

What leads in the delivery phase is not the tool but the order, best formulated by the DORA program: maturity first, then AI [1]. It helps to name the maturity explicitly: DORA identifies seven delivery capabilities on which it makes sense to scale AI — platform engineering, automated testing, version control, fast feedback, loosely coupled architecture, quality documentation, and working in small batches [1]. This is a capability model derived from many years of quantitative research on thousands of teams, not from opinions. And only on this foundation does it make sense to scale AI, because AI amplifies what is already there. Inside delivery there is a hard human production gate: a rollout to prod is irreversible, and the decision about it remains human.

An important observation about tools: in delivery there is not, and likely will not be, a separate AI-CD product that "does delivery for you". The reason is structural — the phase's input is your specific infrastructure. So here AI consumes pipelines rather than owning them: the agent runs inside your infrastructure, for example on top of GitHub Actions, and calls the utilities gh, aws, gcloud as a least-privilege user.

Now for the numbers, and here it is essential to show both halves. DORA records that a rise in AI adoption is associated with a rise in throughput and with a plus of seven and a half percent to documentation quality [1] — that is real value. But the same rise is associated with a minus of seven point two percent to delivery stability [1], and this link is negative for the second year running [2]. You cannot cite one half without the other. Hence the failure: if you scale AI onto an immature pipeline without automated tests and cheap rollback, the DORA multiplier will work the wrong way — both speed and instability will grow. The load-bearing point of the phase: the AI multiplier works both ways, so pipeline discipline first, then AI.

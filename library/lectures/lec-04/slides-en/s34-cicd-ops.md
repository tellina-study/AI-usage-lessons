---
id: s33
type: case_study
section: "Section 6. Delivery · Operations · Documentation"
duration_min: 3
assertion: "Delivery is DORA-first: a mature pipeline first, then scale AI ('AI amplifies what is already there') + a risk-calibrated prod gate (hard and human on the irreversible, AI may take part in approving something small and reversible); AI consumes pipelines but does not own them; DORA — both halves (+throughput / -7.2% stability)"
learning_goal: "[SI] CI/CD+Ops practices: DORA-first + a risk-calibrated prod gate; the DORA pair, both halves; operations is the weakest phase"
learning_outcomes: [LO1, LO7]
chapter_ref: "§6.1 [for-slide-s33]"
references: [dora-report, osmani-70-percent]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study, THE ENTRY SLIDE OF SECTION 6 (round-6, owner: "does not read at all without deep analysis of the
  notes — rebuild it and structure it as an entry into the section"). The slide carries ONE thesis — the order of
  investment: maturity first, then AI. Left: a gold plate "AI amplifies what is already there", below it TWO
  numbered steps (1 — mature delivery without AI, with four example capabilities; 2 — only then AI on top), then
  a counter-line "the reverse does not work: AI does not fix an immature pipeline, it speeds it up". The seven
  delivery capabilities are NOT enumerated in full — they are named as a count with four examples. The three
  previously co-equal insets (risk-calibrated gate · consumes-but-does-not-own · operations is the weakest phase)
  are DEMOTED into one muted subordinate paragraph: they are needed later in the section but must not compete
  with the thesis.
  Right — the evidence: the paired DORA diagram (+7.5% documentation / -7.2% stability) + a gold plate "one and
  the same adoption yields both halves" + the line "which half outweighs the other is decided by the maturity of
  the pipeline, not by the choice of model".
  A secondary row muted: headless (Anthropic parity), AWS Q Operational Investigations over CloudWatch (assist,
  not replacement). Gold — "the AI multiplier works BOTH ways". Source references — inline right at the material
  (definition/claim/recommendation), NOT in a bottom footer; small and muted: DORA 2024/2025.
interaction: none
---

# Visible content

## Title bar
Delivery — DORA-first: a mature pipeline first, then scale AI

## Body
[Left — one order of investment, in two steps]

[Gold plate] "**AI amplifies what is already there**" — so there is only one order, and it runs against intuition:

1. **First — mature delivery that works WITHOUT AI:** automated tests as a gate · version control with cheap rollback · fast feedback · small batches. These are four of the seven delivery capabilities DORA identifies.
2. **Only then — scale AI on top of it.**

**The reverse does not work: AI does not fix an immature pipeline — it speeds it up.**

*Inside the practice: the prod gate is calibrated by risk — a human approves the irreversible, while something small and reversible that has passed its gates may be confirmed by AI. AI consumes the pipeline but does not own it: the agent calls `gh` / `aws` / `gcloud` as a privilege-limited user. Operations is the weakest of the three phases: AI has no runtime context.*

[Right — the evidence: both halves of one and the same adoption]

[Paired diagram: +7.5 / −7.2]

**One and the same AI adoption yields both halves: +7.5% to documentation quality and −7.2% to delivery stability (DORA 2024); the link with stability has been negative for the second year running (DORA 2025).**

Which of the halves outweighs the other is decided by the **maturity of the pipeline**, not by the choice of model.

[Gold callout]
The failure of this phase is scaling AI onto an **immature** pipeline: both speed and instability grow. Hype: "an AI-CD/ops product as a replacement for the human".

## Speaker notes

This is the entry into the section on the last three phases of the cycle, and the whole section rests on one rule, best formulated by the DORA program: maturity first, then AI [1].

Take the order apart. Step one — delivery has to work without any AI at all: automated tests as a mandatory gate, version control with a cheap and regularly exercised rollback, fast feedback from the pipeline, and working in small batches. These are four of the seven delivery capabilities DORA derives from years of quantitative research on thousands of teams; the other three are platform engineering, loosely coupled architecture and quality documentation [1]. Step two, and only then, is to scale AI on top of a pipeline that already works. The reverse order does not work: AI does not fix an immature pipeline, it speeds it up, and instability grows along with speed.

How we know this holds. DORA measures both halves of one and the same adoption: a rise in AI adoption is associated with a plus of seven and a half percent to documentation quality — and at the same time with a minus of seven point two percent to delivery stability [1], and in the second report that link remained negative for the second year running [2]. One half cannot be cited without the other. This is the multiplier working both ways: which half outweighs the other is decided by the maturity of the pipeline, not by the choice of model.

Three clarifications that will be needed later. The production gate is calibrated by risk: the irreversible — a schema migration, payment code — is approved by a human, while something small and reversible that has passed its deterministic gates may be confirmed by AI. There is no separate AI-CD product, and it seems there will not be one: the agent runs inside your infrastructure and calls gh, aws and gcloud as a privilege-limited user. And of the three phases, operations is the weakest for AI: it has no runtime context and no system history, and the agent's report about the state of the system is not a source of truth.

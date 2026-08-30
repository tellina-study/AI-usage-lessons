---
id: s34
type: case_study
section: "Section 6. Delivery · Operations · Documentation"
duration_min: 3
assertion: "Documentation is the only bright spot (DORA +7.5%, but ONLY paired with -7.2% stability); the practice is docs-as-context (code = truth), generation pace <= comprehension pace; the failure is cognitive debt"
learning_goal: "[SI] Docs-as-context (code = truth) + cognitive-debt failure; DORA +7.5% paired with -7.2% stability"
learning_outcomes: [LO1, LO7]
chapter_ref: "§6.2 [for-slide-s34]"
references: [dora-report, thoughtworks-radar, bockeler-thoughtworks]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study: left — the "bright spot" (gold accent): the only phase with a clean positive system-level effect of AI — why: accidental
  complexity dominates, the cost of error is asymmetrically low, built-in human control (docs get read). A number with a baseline (the main one): DORA 2024 +7.5%
  to documentation quality — but presented ONLY paired with -7.2% stability (a measurable AI effect almost always has a paired cost); stability is negative for the 2nd year.
  Right — 2 failures (in-bucket): (1) cognitive debt (codebase cognitive debt, Radar Hold) — generation outpaces comprehension · (2) onboarding documentation
  hallucinates setup/deploy (Böckeler: "AI will not replace a well-documented and automated setup"). Practice: docs-as-context (code = source of truth),
  generation pace <= comprehension pace. A secondary row muted: Confluence AI, AWS Q /doc, JetBrains KDoc/Javadoc. Gold — "the only clean plus — but with a paired cost". Source references — inline right at the material (definition/claim/recommendation), NOT in a bottom footer; small and muted: DORA 2024; Thoughtworks Radar.
interaction: none
---

# Visible content

## Title bar
Documentation is AI's only clean plus, but even it has a paired cost

## Body
[Left — the bright spot, gold accent]

**Documentation is the only phase** with a clean positive system-level effect of AI. Why this one: **accidental** complexity dominates; the cost of error is asymmetrically **low**; human control is built in — the docs get **read**.

The number: DORA 2024 — **+7.5%** to documentation quality.
*Baseline: cited **only paired** with **-7.2% delivery stability** (a measurable AI effect almost always has a paired cost); stability is negative for the second year.*

[Right — 2 failures]

**Cognitive debt** (codebase cognitive debt, Radar Hold) — documentation generation **outpaces comprehension**: lots of text, less understanding.

**Onboarding docs hallucinate setup / deploy** (Böckeler): "AI cannot magically replace a well-documented and automated setup".

[Gold callout]
Practice: **docs-as-context** — code stays the source of truth, documentation is context for the human and for AI; **generation pace <= comprehension pace**. Documentation-as-context — yes; documentation-as-truth — no.

## Speaker notes

Documentation is the only bright spot on the whole phase map, and it is worth understanding why exactly this one. Three reasons. First: in documenting, accidental complexity dominates — translating existing code and decisions into human-readable text — and that is exactly where AI is strong. Second: the cost of error here is asymmetrically low — an inaccuracy in a comment does not bring down prod. Third: natural human control is built in — documentation is read by people, and a bad doc is noticeable. That is why even strict system-level measurements show a clean plus here: in 2024 DORA recorded a gain in documentation quality of about seven and a half percent [1].

And immediately the crucial baseline, otherwise the number misleads: the same rise in AI adoption was accompanied by a drop in delivery stability of about seven point two percent [1], and this link is negative for the second year running. The plus seven and a half to docs cannot be cited apart from the paired minus to stability — this is a general principle of the lecture: a measurable AI effect almost always has a paired cost.

And even the bright spot has two failures. The first is codebase cognitive debt: documentation generation begins to outpace comprehension, there is more and more text, it looks authoritative, but the team's real understanding is less than the number of pages. The second, named by Böckeler, is onboarding documentation that hallucinates setup and deployment: AI confidently describes setup steps that do not actually exist, and a new developer spends a day following a made-up instruction; her phrasing is precise — AI cannot magically replace a well-documented and automated setup [2]. Hence the practice of the phase: docs-as-context — code stays the source of truth, and documentation feeds both the human and AI, but does not substitute for checking the code. And the rule of measure: the pace of documentation generation must not exceed the pace of its comprehension. Documentation-as-context — yes; documentation-as-truth — no.

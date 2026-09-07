---
id: s19
type: case_study
section: "Section 2. Design / prototype"
duration_min: 2.5
assertion: "Character.AI's safety features appeared only after a lawsuit over a teenager's death — almost two years after launch"
learning_goal: "On-point failure #3 (S2): Character.AI (LO3/LO6)"
learning_outcomes: [LO3, LO6]
chapter_ref: "§2.6 [for-slide-s19]"
in_bucket: true
interaction: none
verify_day_of: false
meme_or_visual: >
  case_study: a timeline (schema_timeline) — "Product launch" → a long empty gap →
  "Tragedy (02.2024)" → "Lawsuit (10.2024)" → "Safety features added (11.2025)." The gap
  between launch and safety mechanisms is visually emphasized.
source: "Washington Post (24 Oct 2024); CBS News (Jan 2026)"
---

# Visible content

## Title bar
Safety features appeared almost two years after launch — only after the tragedy

## Body
[schema_timeline: Launch → (long gap) → Tragedy 02.2024 → Lawsuit → Safety features 11.2025]

**Character.AI**
- A 14-year-old user died by suicide after months of talking to an AI character (February 2024)
- A time limit, a ban on open-ended role-play chat under 18, age verification — added **after** the lawsuits

[Gold callout]
Root cause — not a runtime bug, but a missing requirement in the design brief: the MVP optimized for engagement without asking "who could be harmed"

## Speaker notes

A fourteen-year-old user from Florida died by suicide in February 2024 after months of emotionally intense conversation with an AI character on the Character.AI platform. His mother filed a wrongful-death lawsuit. In January 2026, Google and Character.AI agreed to settle this case along with four other lawsuits. A baseline for comparison: protective features — a time limit for minors, a ban on open-ended role-play chat under eighteen, age verification — were added only after the lawsuits, that is, almost two years after the product launched.

Why this is a Design-phase failure, not an operations one. It's easy to mistakenly classify this as an operational failure. But the root lies earlier — in the design decision itself about what experience to build: a product optimizing for the emotional attachment of minors is a first-diamond choice in Double Diamond terms, made without asking "who could be hurt by this interaction flow." The absence of crisis detection isn't an implementation bug — it's a missing requirement in the design brief.

The lesson: for products aimed at the emotional attachment of vulnerable users, safety guardrails must be part of the MVP design from day one, not a patch bolted on after a tragedy. The difference between "built into the design" and "added after the lawsuit" is the difference between a product decision and a legal crisis response. The criterion: if a product monetizes or measures success by the duration of emotionally charged interaction with a vulnerable demographic, that's a structural design flaw. The alternative: peer-support platforms with live human moderation, or clinically validated chatbots with mandatory escalation to a live crisis counselor.

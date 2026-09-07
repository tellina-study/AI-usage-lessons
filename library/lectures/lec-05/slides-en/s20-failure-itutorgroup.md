---
id: s20
type: case_study
section: "Section 2. Design / prototype"
duration_min: 2
assertion: "iTutorGroup hardcoded auto-rejection of candidates 55+/60+ years old — found by accident; EEOC: the first-ever AI discrimination settlement"
learning_goal: "On-point failure #4 (S2): iTutorGroup (LO2/LO6) — contrast with s19: here a harmful criterion was built in"
learning_outcomes: [LO2, LO6]
chapter_ref: "§2.7 [for-slide-s20]"
in_bucket: true
interaction: none
verify_day_of: false
meme_or_visual: >
  case_study: an icon of "a filter with a hardcoded rule" (a gear with a birth date inside,
  crossing out silhouettes above a certain age). Next to it — a small "coincidence" icon:
  resubmitting the same application with a different birth date → an instant interview invite.
source: "EEOC settlement (9 Aug 2023) — $365,000"
---

# Visible content

## Title bar
Found by accident: the same application with a different birth date — an instant invite

## Body
[Icon "age filter" + "accidental discovery via application resubmission"]

**iTutorGroup — age-based auto-rejection**
- Women 55+ / men 60+ were automatically rejected
- EEOC (Aug 9, 2023): the first-ever AI discrimination settlement, **$365,000**

[Gold callout — contrast with s19]
There, design did NOT build in a safeguard. Here, design DID build in a specific harmful rule — two different classes of failure

## Speaker notes

iTutorGroup programmed its automated résumé-screening system to automatically reject women aged fifty-five and up and men aged sixty and up — a direct violation of US federal age-discrimination law. The discovery trigger: one of the rejected applicants resubmitted the same résumé with a slightly younger birth date — and immediately received an interview invitation. On August 9, 2023, the US Equal Employment Opportunity Commission reached the first-ever settlement in an AI discrimination case: three hundred sixty-five thousand dollars in compensation.

This differs fundamentally from the Character.AI case — an important contrast within one section: there, design failed to build in a safeguard; here, design built in a specific harmful decision rule. This isn't "the model learned bias from the data" — it's a hardcoded discriminatory rule, introduced without a bias audit at the requirements-design stage of the screening system.

Why the discovery trigger is so instructive: the discrimination wasn't uncovered by an audit or a test — it was uncovered by chance. That means the hard age filter had been running in production for an unknown length of time, screening out real people, and would have stayed invisible if not for this accidental resubmission. Bias baked into a decision rule doesn't show up in ordinary metrics — the screening speed looks great — it only shows up under a deliberate audit for disparate impact. The lesson: automating a decision that affects people in legally protected categories is an area where legal constraints must be part of the technical spec from the start. The criterion: any screening that touches protected categories requires a mandatory bias audit before production. The alternative: transparent, auditable rules with no demographic proxy variables, plus periodic disparate-impact analysis.

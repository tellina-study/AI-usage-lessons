---
id: s33
type: case_study
section: "Section 4. Measure / Experiment"
duration_min: 2.5
assertion: "Facebook weighted all 5 emoji reactions 5x higher than a like — an engagement proxy with no guardrail hid the harm for almost 2 years"
learning_goal: "On-point failure #7: Facebook MSI, corrected version (all reactions ×5, not only anger) (LO2/LO6)"
learning_outcomes: [LO2, LO6]
chapter_ref: "§4.5 [for-slide-s33]"
in_bucket: true
interaction: none
verify_day_of: false
meme_or_visual: >
  case_study: 5 equally-sized emoji-reaction icons (love/haha/wow/sad/angry), each labeled
  "×5" in the same font — visually debunks the "only anger was boosted" myth. Next to it — a
  timeline: "MSI introduced 01.2018" → "guardrail confirmed 2019" → "weight zeroed 09.2019" —
  a ~1.5-2 year gap.
source: "Techdirt correction (28 Oct 2021); WSJ 'Facebook Files' (2021)"
---

# Visible content

## Title bar
All 5 reactions were weighted equally at ×5 — not just "anger" (a common retelling error)

## Body
[5 equal reaction icons, each "×5"; timeline: introduced 2018 → confirmed 2019 → zeroed 09.2019]

**Facebook MSI, January 2018**
- love/haha/wow/sad/**angry** — **all** weighted 5× higher than a like (not just anger)
- Guardrail (internal): anger ↔ misinformation — confirmed by 2019, weight zeroed in September 2019

[Gold callout]
The harm went unnoticed for ~2 years — because nobody measured the guardrail from day one, not because of a lack of data science talent

## Speaker notes

Mark Zuckerberg announced in January 2018 that News Feed would prioritize meaningful social interactions. Mechanically, the formula weighted every emoji reaction — love, haha, wow, sad, and angry — five times higher than a plain like. A mandatory fact-check correction: a common retelling claims Facebook specifically boosted the angry reaction — this is inaccurate, according to a corrective media piece. All five reactions were weighted equally at introduction — anger was not singled out. The real failure was subtler: "any strong reaction equals more meaningful" was a blanket proxy for engagement quality, not a deliberate decision to reward outrage.

The guardrail that eventually caught this, and the cost of not having it from day one: internally confirmed by 2019 that posts with an angry reaction were disproportionately likely to contain misinformation. Facebook reduced the angry reaction's weight to zero in September 2019. A separate internal test showed that without the ranking change, users hid fifty percent more posts — confirming the engagement lift was real, but unrelated to content quality.

The mechanism, tied to the Measure phase: the original experiment optimized an engagement proxy but did not measure downstream consequences for content quality; the negative effect surfaced only through a separate qualitative audit after full rollout. Facebook in 2018 had one of the strongest data-science teams in the world — and still the inverse correlation was confirmed only a year and a half to two years later, because nobody measured the quality counter-metric from day one. The lesson: designing an A/B experiment for algorithmic features must include quality guardrail metrics, or the system will find a way to win the test at the cost of hidden harm. The alternative: a multi-metric design with guardrail metrics monitored from day one.

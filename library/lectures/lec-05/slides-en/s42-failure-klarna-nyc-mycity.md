---
id: s42
type: case_study
section: "Section 5. Support / Operate"
duration_min: 2.5
assertion: "Klarna walked back its \"no humans\" policy as automation grew to a 853-FTE equivalent; 10 out of 10 journalists got the same unlawful advice from the NYC bot"
learning_goal: "On-point failure #11: Klarna + NYC MyCity (+Chevy inline) — guaranteed escalation + deterministic guardrails (LO2/LO6)"
learning_outcomes: [LO2, LO6]
chapter_ref: "§5.6 [for-slide-s42]"
in_bucket: true
interaction: none
verify_day_of: false
meme_or_visual: >
  case_study: 2 side-by-side mini-panels — "Klarna" (a growing FTE-equivalent bar, 700→853, but
  with a "human available on request" icon added after the policy rollback) and "NYC MyCity"
  (10 identical journalist icons, all receiving the same X-marked answer — visualizing the
  systematic nature of 10/10, not chance).
source: "Bloomberg (8 May 2025); The Markup (29 Mar 2024)"
---

# Visible content

## Title bar
10 out of 10 journalists got the same unlawful advice — not an isolated glitch

## Body
[Klarna: FTE bar grows 700→853 + a "human available" icon added | NYC: 10/10 identical X marks]

**Klarna**: the "AI-only" policy was walked back (05.2025) — but automation **grew** to an 853-FTE equivalent

**NYC MyCity**: 10/10 journalists — the same unlawful advice; the mayor did not pull the bot

[Gold callout]
The lesson isn't "AI doesn't work" — it's "a throughput metric with no guaranteed human fallback is the wrong design"

## Speaker notes

Klarna and OpenAI announced in February 2024: an AI assistant had handled 2.3 million conversations in its first month, doing the work of seven hundred full-time agents. By May 2025 the CEO acknowledged a reversal: it's critically important to be honest with the customer — there will always be a human if you want one. An important nuance: what got walked back was specifically the "AI-only, no human access" policy — the volume of automation itself kept growing, reaching the equivalent of eight hundred fifty-three full-time positions by the end of 2025. This isn't "Klarna gave up on AI" — it's an acknowledgment that a throughput metric with no guaranteed human fallback was the wrong operational design.

The NYC MyCity chatbot for small businesses: an investigation found the bot advising employers to take employees' tips, to fire someone for reporting harassment, and advising landlords to reject tenants with housing vouchers. All ten of ten journalists who asked this question got the same incorrect answer — not a rare edge case but a systematic, reproducible failure. The mayor acknowledged the errors but refused to pull the bot from public use. A third example of the same class: a user used a prompt injection to get a Chevrolet dealership's chatbot to agree to sell a car for one dollar as a "legally binding offer."

The combined lesson: the success metric for support automation can't be throughput alone — a weighted quality metric is needed on emotionally or legally sensitive categories, and an explicit fallback path to a human must be part of the product from day one. The criterion: guaranteed escalation is mandatory for disputed cases; if ten out of ten identical questions produce one unlawful answer, that's a systematic failure requiring an immediate kill switch. The alternative: tiered support with an explicit "talk to a human" option, deterministic guardrails underneath the LLM on critical actions.

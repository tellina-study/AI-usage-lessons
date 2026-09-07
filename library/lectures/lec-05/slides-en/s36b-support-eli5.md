---
id: s36b
type: eli5_overview
section: "Section 5. Support / Operate"
duration_min: 1.5
assertion: "Support in plain terms: between \"it works for me\" and \"it reliably works for millions, 24/7\" lies a gap, and it's closed by process, not just code quality"
learning_goal: "ELI5 overview of the support phase: why operations matter, the mental model \"a budget for errors\""
learning_outcomes: [LO1]
chapter_ref: "§5.1 [for-slide-s36b]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  eli5_overview: three cards, a "24/7 monitoring console" icon on the left. Plain language.
---

# Visible content

## Title bar
Support in plain terms

## Body
**What it is.** The phase where the product already lives with people around the clock: it needs to be watched, its failures fixed, and complaints answered — for years.

**Why.** "Works on my laptop" and "reliably works for millions, 24/7" are different things. The gap is closed by an operations process, not just clean code.

**Mental model.** We agree in advance on how many failures are acceptable (a budget for errors), and watch real behavior. It's harder with AI: a model can "quietly degrade" while the charts are still green.

## Speaker notes

Support and operations in plain terms is everything that happens to a product after launch, and a lot happens there: the product runs around the clock for real people, breaks, gets complaints, and demands attention for years. Between "it works on my laptop" and "it reliably works for millions at once" lies a gap, and it's closed not by heroics but by process.

The classical engineering discipline here is operational reliability. Its key idea is simple: one hundred percent reliability doesn't exist and isn't needed, so we agree in advance on how many failures are acceptable — that's the budget for errors. As long as we're within budget, we can ship freely; once the budget runs out, we slow down and stabilize. Plus on-call rotations, blameless incident reviews, and runbooks for typical outages.

What does AI change? A new, sneaky class of problems appears. An ordinary outage is visible immediately: the service stops responding, the charts turn red. But a model can quietly degrade: technically everything is green — responses arrive, status codes succeed — but the quality of the answers silently drops, and the most active users feel it first, not the dashboard. Next we'll see three costly operational failures and understand why accountability for every bot answer stays with the company.

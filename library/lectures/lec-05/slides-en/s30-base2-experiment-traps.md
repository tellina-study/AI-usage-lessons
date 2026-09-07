---
id: s30
type: assertion_visual
section: "Section 4. Measure / Experiment"
duration_min: 2.5
assertion: "Eight experiment traps — three questions in the right order: is the test set up correctly? am I reading the result correctly? is the effect real?"
learning_goal: "BASE-2: traps grouped into 3 sub-clusters (top-3 per slide); A/B ≠ feature flag; Bing ≈$100M"
learning_outcomes: [LO1]
chapter_ref: "§4.2 [for-slide-s30]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  assertion_visual: 3 question cards in a row (a "test setup" icon / "reading the result" icon /
  "the effect itself" icon), each topped with 1 trap icon (SRM scales / a peeking eye /
  a Twyman exclamation mark). Top-3, not 8 — per reader-P1.
---

# Visible content

## Title bar
Three questions catch all eight experiment traps

## Body
[3 question cards: setup / reading / effect]

1. **Is the test set up correctly?** — SRM, sample size fixed in advance
2. **Am I reading the result correctly?** — peeking (2 peeks ≈2× false positives)
3. **Is the effect itself real?** — Twyman's law: "a suspiciously nice number is usually wrong"

[Ocean rounded box]
A/B (measurement) ≠ feature flag (rollout) · Bing ≈$100M revenue gain (Kohavi/Thomke HBR 2017) — not "the $300M button"

## Speaker notes

The eight classical experiment traps aren't memorized as a flat list but as three questions in the right order. First — before the test: is the test set up correctly? Sample Ratio Mismatch — when the observed ratio of groups differs statistically significantly from the intended one — is a symptom of many data-quality problems, the way a fever is a symptom of many illnesses. Sample size must be calculated and fixed before the start.

Second — interpretation: am I reading the result correctly? Peeking is checking results before the predetermined sample size is reached and stopping as soon as it looks significant; two peeks roughly double the false-positive rate, five roughly triple it. P-hacking is the broader family of the same mistake. Third — the effect itself: is it real? Twyman's law — any number that looks interesting is usually wrong; a huge, delightful metric jump is more likely a bug than a genuine breakthrough.

An important distinction: an A/B test is a measurement that requires random assignment; a feature flag is just a rollout switch. The canonical example, with a mandatory fact-check correction: Bing's ad-headline experiment produced a twelve-percent revenue-per-search lift, worth over one hundred million dollars in additional annual revenue — that's Kohavi and Thomke, Harvard Business Review, 2017. A separate, unrelated case — Jared Spool's "$300 million button" — is a usability study, not a randomized experiment; listicles regularly conflate the two. Even AI-native personalization needs classical control: Spotify openly acknowledges that a contextual bandit itself needs its own A/B test to validate its value.

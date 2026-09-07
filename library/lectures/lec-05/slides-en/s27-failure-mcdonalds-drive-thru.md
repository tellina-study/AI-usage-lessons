---
id: s27
type: case_study
section: "Section 3. Build / Launch"
duration_min: 2
assertion: "McDonald's kept AI order-taking on 0.7% of the chain's restaurants for 2.5-3 years and still killed the pilot — the correct kill decision"
learning_goal: "Failure/positive on-point #6: McDonald's × IBM drive-thru — an exemplary kill decision (LO2/LO6)"
learning_outcomes: [LO2, LO6]
chapter_ref: "§3.7 [for-slide-s27]"
in_bucket: true
interaction: none
verify_day_of: false
meme_or_visual: >
  case_study: a mirror pairing with s26 (visual symmetry, NOT duplicated detail) — a small
  "0.7%" segment (a thin slice of the full circle of restaurants) with a "stop sign after a
  multi-year test" icon, captioned "the correct decision to stop." A contrast with s26's
  "0%→100% at once" as the mirror-image mistake in the other direction.
source: "CNBC (17 June 2024)"
---

# Visible content

## Title bar
2.5-3 years on 0.7% of the chain — and stopping was the right call

## Body
[Thin 0.7% segment of a circle of ~13,786 restaurants, a "stop after a long test" icon]

**McDonald's × IBM drive-thru**
- ~100 of ≈13,786 US restaurants (**0.7%**), a 2.5–3 year pilot
- Viral failures: bacon in ice cream, 9 iced teas instead of one
- Killed June 2024 — the goal (voice automation) stayed, the vendor's approach was killed

[Gold callout]
Mirror of s26: there they skipped the pilot entirely; here there was a pilot — and its signal was used correctly

## Speaker notes

McDonald's tested automated order-taking jointly with IBM for roughly two and a half to three years, scaling to about one hundred restaurants — roughly zero point seven percent of McDonald's total US restaurant count. Viral clips of failures piled up for months. On June 17, 2024, McDonald's announced it was ending the partnership. The company didn't abandon the goal — voice automation remains part of the future — it killed this specific vendor approach.

This is a decision to stop scaling, not a story about a runtime failure — unusually, it's a good example of a process working correctly. A pilot lasting two and a half to three years, limited to zero point seven percent of locations, still regularly producing viral failures, is itself a signal: this isn't "we need more data," it's "the current approach has a structural ceiling." Without the denominator, "one hundred restaurants" sounds like a large-scale pilot; with the denominator, it's a tiny slice of the chain that was kept running for two and a half years and still never reached production reliability.

Compare it with the previous failure: Google made exactly the opposite mistake — jumping straight to one hundred percent with no pilot phase at all. The two cases mirror each other: one correctly didn't cross the gate after a long pilot, the other skipped the pilot entirely. The lesson: a long pilot that keeps failing publicly at a limited scale is a signal to kill it, not "polish it a bit more." The criterion: if the error rate doesn't converge to a production level after a multi-year pilot, that's a structural limit of the current approach. The alternative: a human-in-the-loop hybrid — AI proposes the recognized order, the cashier confirms it before it goes to the kitchen.

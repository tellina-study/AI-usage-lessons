---
id: s12
type: case_study
section: "Section 1. Discovery"
duration_min: 3
assertion: "A synthetic panel reported 7 of 7 tasks completed; real users — 3 of 7: the panel cannot produce disagreement"
learning_goal: "On-point failure #1: synthetic users, NN/g (LO2/LO6)"
learning_outcomes: [LO2, LO6]
chapter_ref: "§1.7 [for-slide-s13]"
in_bucket: true
interaction: none
verify_day_of: false
meme_or_visual: >
  case_study: a split screen "Real users: 3 checkmarks out of 7 (2 crosses, 2 question marks)"
  vs "Synthetic panel: 7 checkmarks out of 7" — the same test flow, a diametrically different
  result. At the bottom — a quote contrast "contrived" vs "game-changer" about the same feature.
source: "Nielsen Norman Group, 'Synthetic Users' (updated 21 June 2024) [FACT-CHECK]"
---

# Visible content

## Title bar
The same task: real people — 3 of 7, synthetic panel — 7 of 7

## Body
[Split screen: 3/7 checkmarks vs 7/7 checkmarks, identical test]

**NN/g: a controlled onboarding comparison**
- Real users: 3 of 7 steps completed
- Synthetic panel: falsely reported 7 of 7

[Contrast quote]
"Contrived and useless" (real) vs "a game-changer" (synthetic) — the same feature

[Gold callout]
Criterion: a synthetic output is disqualified for go/no-go **by construction**, not from a bad run

## Speaker notes

The Nielsen Norman Group ran a controlled comparison as part of an onboarding usability study: real users completed an average of three out of seven steps; an AI-generated panel of synthetic users, tested on the exact same flow, falsely reported completing all seven of seven. Separately, real users described a discussion-forum feature as contrived and useless, while synthetic personas produced glowing praise of the same feature; one synthetic user called an impractical drone-delivery concept "a game-changer."

The mechanism, tied specifically to the Discovery phase: large language models are tuned to agree with the framing of the given question — a concept described with any enthusiasm comes back validated. A synthetic user cannot produce disagreement, because it has no real experience capable of contradicting the question's framing. This is the same agreement-bias mechanism the course has already discussed for models in general, but here it materializes as a concrete, measured failure specifically in the discovery phase.

Combine this with the Mom Test's second rule — ask about a real past — and you get a cumulative failure: not just skewed toward "yes," but skewed toward "yes" about an event that never happened. The lesson: a synthetic panel that agrees with your concept is not evidence the concept is good — it's evidence the panel is incapable of disagreeing. The criterion: any output feeding a "ship or not" decision must be traceable to real past behavior of a real person. The alternative: use a synthetic panel only in a pre-research role, then run real testing with five to eight participants — a sample size that already surfaces most usability problems.

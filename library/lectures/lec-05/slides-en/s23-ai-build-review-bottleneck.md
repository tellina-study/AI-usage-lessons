---
id: s23
type: assertion_visual
section: "Section 3. Build and launch"
duration_min: 2
assertion: "Writing code got cheap, checking it did not: review was added to the bottleneck already sitting at the input, and this is measured on several independent 2026 samples"
learning_goal: "What changed in build and launch: the measured shift, plus a comparison of the key practices without AI and with it"
learning_outcomes: [LO1, LO2]
chapter_ref: "§3.3 [for-slide-s23]"
interaction: none
verify_day_of: true
partial_out_strict_in: true
note: >
  issue #212, EN parity pass — the EN twin was re-synchronised with the RU slide as rebuilt
  in Stage 6. What it used to say ("+200% code per engineer — but only 16% of PRs got
  substantive review", a two-bar chart, a three-bullet Anthropic list) is superseded on
  three counts, all of which the RU side had already fixed: (1) R6, the figures are now the
  2026 data (Faros AI, LinearB) and the slide is built as a comparison "practice without AI
  / what is added with AI" instead of a list of facts; (2) fact-check 2026-09-30, the
  Anthropic figures were moved to their real source — the post Code Review for Claude Code
  (9 March 2026), not the Agentic Coding Trends Report — and the 16% is unfolded into the
  pair "16% before -> 54% after", because on its own it asserted the opposite of what the
  source says; the Faros metric is named correctly, "time in review" and not "time waiting
  for review" (waiting is +157%); (3) the cross-check with Lecture 4 (owner review,
  2026-10-01) closed three divergences — the title called review the only bottleneck where
  L4 §1.3 named precision of intent at the input first (hence "adds to", not "moved to");
  the test row was silent about L4 §4.1/§4.3 (the test as an executable specification plus
  a deterministic run gate, and mutation score being more honest than coverage); and there
  was no warning from L4 §3.7/§5.2 that relieving review by handing the merge to an agent
  removes the only control.
meme_or_visual: >
  assertion_visual: on the left, four large number tiles of the measured shift (+200% code
  volume / 16% -> 54% substantive review / +441% time in review / 2.5x larger and 5x longer
  waits). On the right, a two-column table: "did and still do" against "what gets added
  when an agent writes the code", one row per practice, a thin right arrow between the
  columns.
source: "Anthropic, Code Review for Claude Code (9 March 2026) · Faros AI Engineering Report 2026 (telemetry from 22,000 developers, 4,000+ teams) · LinearB (8.1M pull requests) [VFY-day-of]"
---

# Visible content

## Title bar
Code got cheap to write, not to check: review adds to the bottleneck at the input

## Body
[Left, four numbers of the measured shift; right, a table "did and still do" → "what gets added with AI"]

**MEASURED SHIFT**
- Code volume per engineer: **+200%** in a year (Anthropic's own measurement)
- Share of changes with substantive review before merge: **16% before → 54% after** — after the first pass was handed to automation; nearly half still merges without one
- Median time a change spends in review: **+441%** (Faros AI, telemetry from 22,000 developers)
- AI changes are roughly **2.5× larger** and wait for a reviewer roughly **5× longer** (LinearB, 8.1M pull requests)

**PRACTICES: WHAT WAS AND WHAT WAS ADDED**

| Did and still do, no AI | What gets added when an agent writes the code |
|---|---|
| Review of changes before merge | It became the bottleneck itself; handing the merge to an agent removes the only control |
| Feature flag | Switches the autonomy level: how much the system decides itself |
| Staged rollout by share of users | Rolled out on two axes at once: share of audience and autonomy level |
| Test as executable specification and a run gate | A mutation-score gate was added: it checks the test can catch a defect at all |
| Circuit breaker | Always needed: a failure spreads faster than anyone notices it |
| A human-owned specification | The one input an agent cannot invent for itself |

[Gold callout]
Scarcity sits at the edges: precision of the task in, speed of judgment out.

## Speaker notes

Anthropic's own measurement describes the shift as a compression of the stages: implementation moves from weeks and months to minutes of agentic execution, and getting into an unfamiliar codebase from weeks to hours. The boundaries between the stages stay where they were. The risk statement: agents produce more and more code, the volume of review behind them does not keep up, and the visibility gap widens. The two have to be taken as a pair. Code volume per engineer grew by roughly two hundred percent in a year. Substantive comments used to reach about sixteen percent of changes; after the first pass was handed to automation, that share rose to fifty-four. The company measured the gap on itself and judged it serious enough to build a separate product for it. And even after that, nearly half of all changes merge with no substantive review.

This is not a single observation. The Faros AI report for two thousand twenty-six, on telemetry from twenty-two thousand developers across four thousand teams, gives plus four hundred forty-one percent to the median time a change spends in review, with task throughput up by a third and production incidents tripled. LinearB's measurements on more than eight million pull requests show the same mechanism from the other side: changes made with AI are roughly two and a half times larger and wait for a reviewer roughly five times longer.

The right-hand side of the slide is the part doing the work: the classics stayed, what changed is the load on them. Review turned from hygiene into the bottleneck — and here there is a direct echo of the previous lecture: relieving it by handing the merge to an agent means removing the only control at the point where responsibility lives. The feature flag now switches the autonomy level: how much the system decides itself. The rollout runs on two axes at once — share of audience and autonomy level. The test stayed an executable specification with a deterministic run gate, and a mutation-score gate was added to it: a check that the test is capable of catching a defect at all. The circuit breaker moved from desirable to mandatory. The specification stayed the one input an agent cannot invent for itself.

From this comes the conclusion worth holding on to. The scarce resource was never "who can write the code". What is scarce is the edges of the work: precision of intent going in and speed of judgment coming out. We named the first edge in the previous lecture, when we took apart the specification; review is the second, at the other end of the same work.

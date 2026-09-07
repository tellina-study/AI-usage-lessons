---
id: s23
type: assertion_visual
section: "Section 3. Build / Launch"
duration_min: 2.5
assertion: "Build → near zero (Anthropic); code volume +200% a year, yet only ~16% of PRs got substantive review"
learning_goal: "AI trait: Build→≈0 + the bottleneck shift into review; what to keep from the classic"
learning_outcomes: [LO1, LO2]
chapter_ref: "§3.3 [for-slide-s23]"
interaction: none
verify_day_of: true
partial_out_strict_in: true
meme_or_visual: >
  assertion_visual: two bar charts side by side — "code volume per engineer" (growing to
  200%, a thick gold bar) and "share of PRs with substantive review" (a thin bar, only 16%)
  — a visual gap between the two figures.
source: "Anthropic 2026 Agentic Coding Trends Report (22 Jan 2026) [VFY-day-of]"
---

# Visible content

## Title bar
+200% code per engineer — but only 16% of PRs got substantive review

## Body
[2 contrasting bars: 200% volume / 16% review]

**Anthropic's own measurement**
- Implementation: weeks/months → **minutes** of agentic execution
- Code volume per engineer: **+200%** year over year
- Substantive human review before merge: only **~16%** of PRs

[Gold callout]
The scarce resource shifted to the two human ends: precision of intent going in, quality of judgment coming out

## Speaker notes

Anthropic's own reported measurement frames the shift as a compression of stage duration, not the disappearance of the boundaries between stages: implementation moves from weeks to minutes of agentic execution. The central risk claim: as agents produce more code, review volume doesn't scale at the same speed. Anthropic's own internal data makes this concrete: code volume per engineer grew roughly two hundred percent year over year, but only about sixteen percent of pull requests received substantive human review comments before merge.

This is the section's key inversion: the scarce resource was never "who can write the code" — in the AI era it unambiguously becomes "who can specify precisely enough" and "who can review fast enough not to become the bottleneck." Notice the direct symmetry with the keystone: build collapsed to zero, so scarcity shifted to the two human ends of the arrow. Bain makes the same observation from the business side: phase boundaries blur into a more continuous flow, but it explicitly does not claim full autonomy — agents work best with human review at critical checkpoints.

What to keep from the classic: version control, PR review — now the bottleneck's destination, not a relic; feature flags as the basic mechanism for shipping inactive; staged rollout — directly reused by the agency ladder next; a kill switch — unconditionally necessary; a human-owned specification — an artifact the agent can't generate for itself without guessing at intent.

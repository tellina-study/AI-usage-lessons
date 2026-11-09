---
id: s06
local_id: I-06
section: "0. Introduction"
type: norm
title: "A threshold, not a promise"
assertion: "Google names a $200/kg threshold for orbital computing — today it is 2.5–3× more expensive than Earth"
source: "[Google (Project Suncatcher)](https://blog.google/innovation-and-ai/technology/research/google-project-suncatcher/) · [Starcloud](https://www.starcloud.com/starcloud-1) · [BCG, report 08.2026](https://www.bcg.com/publications/2026/space-based-data-centers-cost-outlook)"
media: ""
media_needed: "Phase 8 (issue #317): replaced with a tick-mark axis (`scheme: kind: shkala`) — four thresholds/prices in one unit ($/kg) are visible by position on the line, rather than as four identical boxes in a row (student-simulator finding: 'fourth slide in a row with the same 4 cards'). The BCG difference ($/MW, a different base) stays a plate — it doesn't belong on the same axis as $/kg (`axis.py`: 'a form does NOT put values with DIFFERENT bases on one axis')."
scheme:
  kind: shkala
  unit: "$ per kg of cargo to orbit"
  caption: "Today, several times above Google's threshold — the threshold is named, not invented"
  from: 0
  marks:
    - {value: 200, label: "Google's threshold, by ≤2035"}
    - {value: 500, label: "Starcloud's threshold, ~2028"}
    - {value: 1500, label: "today, from"}
    - {value: 2900, label: "today, to", key: true}
blocks:
  - {label: "Orbital data centers today vs ground-based", value: "2.5–3× more expensive", note: "BCG: $660–750 million/MW against $230–300 million/MW on Earth", key: true}
in_bucket: true
status: draft
---

## Visible slide text

**This is not "already worth it" — it's "will become worth it at such-and-such threshold".** The difference between these two statements is what keeps the whole of Section 4 honest.

**The reverse scenario.** If cost freezes at the upper end of the range ($500/kg, not $67–100/kg), the drop from today's Falcon 9 will be not 30× but 5–6×, and Google's threshold will move years further out than 2035.

## Speaker notes

This paragraph is the one place in the industry overview where the lecture talks not about what has already happened, but about what could happen under certain conditions. This is exactly where it matters most to keep the difference between a fact and a threshold.

Google — specifically in the context of its own orbital-computing project, Suncatcher, which we'll examine in Section 4 — states directly the number at which placing compute infrastructure in space becomes economically competitive with ground-based data centers: a launch cost no higher than $200 per kilogram. Today, orbital capacity for dedicated missions costs $1,500–2,900 per kilogram — the threshold is far off, but it is named, not invented. Google itself forecasts the threshold is reachable by 2035, on condition that Starship reaches a cadence of 180 launches a year. Starcloud names its own break-even threshold — around $500 per kilogram — and expects it by mid-to-late 2028.

A fair counterweight to these forecasts came from a BCG study published in August 2026: today orbital data centers cost 2.5–3 times more than ground-based ones per megawatt of capacity. That's exactly what keeps the whole of Section 4 honest: Starcloud's and Suncatcher's demonstrators are already working today, regardless of which scenario launch cost follows next — but what's proven is the principle, not economic competitiveness.

And the reverse scenario is worth stating explicitly. If cost freezes not at $100/kg (Musk's target) and not even at $67/kg (Aerospace's optimistic scenario), but at the upper end of the realistic range — $500/kg — then the drop from today's Falcon 9 would be not 30× but a much less impressive 5–6×, and Google's $200/kg threshold would move years further out than the stated 2035. That doesn't make Section 4's material irrelevant — but it's worth keeping in mind that both ends of the range remain equally possible outcomes.

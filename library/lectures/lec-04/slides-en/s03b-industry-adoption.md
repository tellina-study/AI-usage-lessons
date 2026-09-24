---
id: s03b
type: assertion_visual
section: "Section 0. Introduction and methodological frame"
duration_min: 2
assertion: "The industry has closed the argument about whether to adopt AI in development: 84–90% of developers already use AI tools, and the share is growing for the second year running — while the share of those who do not trust the accuracy of the output has risen from 31% to 46%, so what is still open is not \"yes or no\" but the question of cost, risks, and countermeasures"
learning_goal: "Set the industry-wide scale before the phase-by-phase walkthrough: show that the decision to use AI has already been made de facto, and reframe the lecture's question as one of reliability rather than a choice between \"use\" and \"don't use\""
learning_outcomes: [LO1, LO7]
chapter_ref: "§7.4, the paragraph \"An anchor for the checklist: the industry uses what it trusts less and less\""
references: [so-survey-2025, dora-2025]
in_bucket: false
verify_day_of: true
visual_brief: >
  assertion_visual, two columns. Left (icon users) — "Scale: almost the whole industry is already inside":
  the bar chart c03b-adoption.png from charts-en (Stack Overflow 2024 = 76%, Stack Overflow 2025 = 84%,
  DORA 2025 = 90%; the last bar gold), beneath it 51% work with AI daily and a median of about two hours
  a day, then a small honest caveat about the difference in survey wording.
  Right (icon circle-help, teal) — "Trust, meanwhile, is falling": a gold block with the mega-number 46%
  ("do not trust the accuracy — against 31% a year earlier"), under it the DORA contrast (over 80% report
  a gain in effectiveness, 24% highly trust the output), and at the bottom a teal conclusion strip about
  the gap. Gold callout at the very bottom — the reframing of the lecture's question.
  NOTE (#172): the chart had to be REGENERATED in English (gen_charts_r6b5_en.py) — the RU original has
  its title and tick labels baked into the pixels in Cyrillic and cannot be reused here.
interaction: none
---

# Visible content

## Title bar
The industry has already closed the "use it or not" question — what stayed open is reliability

## Body
[Left — the scale]

**Scale: almost the whole industry is already inside.**

Share of developers using AI tools: **76%** (Stack Overflow, 2024) → **84%** (Stack Overflow, 2025) → **90%** (DORA, 2025).

**51%** of professional developers work with AI tools daily; the median time spent with them is about **two hours a day**, roughly a quarter of the working day.

*The surveys differ: Stack Overflow asks "use or plan to use" (more than 49,000 people from 177 countries), DORA asks "use" (more than 5,000). The order of magnitude agrees.*

[Right — trust]

**Trust, meanwhile, is falling.**

**46%** do not trust the accuracy of what AI tools produce — against **31%** a year earlier.

Over **80%** at the same time report a gain in personal effectiveness — yet only **24%** highly trust the result. The feeling of usefulness and trust in the output have come apart.

[Teal strip]
Almost everyone uses them — fewer than half trust them. There is nothing left to argue about in "should we switch AI on"; the engineering question is what closes this gap.

[Gold callout]
**84–90%** of the industry is already inside, and the share is growing for the second year running. So the useful question is not "use AI or not" but **at what cost, with which risks, and with which measures those risks are closed** — phase by phase.

## Speaker notes

Before breaking development down by phase, it is worth fixing the scale on which all of this happens. In the Stack Overflow survey for twenty twenty-five — more than forty-nine thousand developers from one hundred seventy-seven countries — eighty-four percent use or plan to use AI tools at work, against seventy-six percent a year earlier [1]. The DORA report for the same year, on more than five thousand people, gives ninety percent already using AI, a rise of fourteen points over the previous wave [2]. The two surveys word the question differently, so the numbers cannot be added or read on one scale, but the order of magnitude agrees. Half of professional developers work with such tools daily, and the median time spent with them is about two hours a day — roughly a quarter of the working day [1].

More important than the numbers is what is happening to trust. In the same survey, the share of those who do not trust the accuracy of what AI tools produce grew from thirty-one to forty-six percent in a year [1]. DORA shows the same sign: more than eighty percent say AI raised their personal effectiveness, yet only twenty-four percent highly trust the result [2]. The feeling of usefulness and trust in the output have come apart — exactly the gap this lecture takes apart phase by phase.

The practical conclusion is a single one. The decision on whether to use AI in development has already been made de facto: almost everyone is inside, and it is late to argue about it. What stayed open is a question of a different class — at what cost, with which risks, and with which measures those risks are closed at each phase of the lifecycle. That question is the subject of the lecture, and we return to it at the end, with the permissible level of autonomy and the checklist.

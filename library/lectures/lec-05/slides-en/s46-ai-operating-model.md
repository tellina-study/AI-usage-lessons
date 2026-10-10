---
id: s46
type: process
section: "Section 6. Governance"
duration_min: 1.5
assertion: "Any feature is assessed with four questions — what behaviour changes, against what baseline, what it costs, at what result it is shut down; AI inside changes two of them, two stay word for word the same"
learning_goal: "An apparatus for assessing a single feature, indifferent to whether AI sits inside it — and an honest account of what AI does change in it"
learning_outcomes: [LO1, LO2]
chapter_ref: "§6.1 (the financial criterion); the apparatus for assessing a feature has no section of its own in the chapter yet"
interaction: none
verify_day_of: false
partial_out_strict_in: true
note: >
  issue #212, EN parity pass. THIS SLIDE WAS REWRITTEN WHOLE, not re-translated: the EN
  twin still carried the pre-Stage-6 slide ("The bottleneck shifted from technology to the
  organization's operating model" — five converging sources Deloitte/Sber/Gartner/McKinsey/
  Forrester plus a 0-5 maturity scale), which the RU rebuild deleted on the owner's
  remark 3 ("slide 48 is an abrupt, illogical transition. better to give the assessment of
  a feature in the abstract, AI inside or not"). The old slide broke Section 6 by jumping
  from engineering practice to the level of the organization. It now gives the apparatus
  for assessing any feature, and a separate band states which two of the four points AI
  changes. The statistics of the former slide stay in the chapter §6.2; Deloitte and Boston
  Consulting Group are voiced on s45. The s46 entry in SLIDE_REFS (_helpers_en.py) is
  removed in step with the RU side: there are no external numbers on the slide any more,
  and the reference list under it would print sources the slide does not cite.
  The bridge to s47 is kept and made logical: the second question of the apparatus — the
  baseline — is exactly what breaks in both of the cases that follow.
meme_or_visual: >
  process: four cards in a 2x2 grid, each with a number in a circle, a question as its
  heading and an icon (target / ruler / banknote / timer); the order of the questions is
  fixed and reads by the numbers. Below — a gold-framed band "what changes when there is AI
  inside the feature": two of the four points named outright. Gold at the bottom — the
  bridge to the two cases through the second question, the one about the baseline. No
  external figures and no statistics on the slide.
---

# Visible content

## Title bar
How any feature is assessed — AI inside or not

## Body
[Four cards in a 2x2 grid — the order of the questions is fixed]

**1. What behaviour it changes**
Which user action becomes more frequent, faster or cheaper. Unnamed action — nothing to assess.

**2. Against what baseline**
The same product without the feature, same period. With no baseline, any gain gets credited to it.

**3. What it costs**
Build once, run every month. The second is counted together with usage volume.

**4. At what result it gets shut down**
Number and date written down before launch: named after, it only explains the result.

**WHAT CHANGES WHEN THERE IS AI INSIDE**

Two of the four change. **The third:** running stops being a one-off — it gains a meter that ticks with volume. **The first:** the model's answer varies run to run, so "it works" is confirmed on a sample, and one lucky example does not count. **The second and fourth** stay word for word the same.

[Gold callout]
The second question — the baseline — breaks more often than the other three. The two cases ahead are exactly about that: a loud failure number that turns out to have no denominator, and a claimed autonomy that is fourteen times off the company's own target.

## Speaker notes

The section is nearly over, and before we go to the two cases, let us gather in one place the thing you will use every day. Assessing a feature. Any feature — it makes no difference whether a model sits inside it or ordinary code. Four questions, and their order is fixed.

First: what the feature changes in behaviour. Which user action, exactly, becomes more frequent, faster or cheaper. This is where assessment collapses most often: a feature is commissioned without the action being named, and there is nothing left to argue about — there is nothing to measure.

Second: against what baseline. The same product without this feature, over the same period, on the same audience. Until there is a baseline, every gain will be credited to the feature — including the seasonal one, the one advertising bought, and the one a competitor handed over by going down at that moment.

Third: what it costs. Build — once. Running — every month, and it is counted together with usage volume, because volume is what it depends on.

Fourth: at what result it gets shut down. The number and the date are written down before launch. A number named after the result is visible explains that result; nothing can be tested with it.

Now about AI, and this is the short part. Of the four points it changes two. The third: running stops being a one-off, it gains a meter, and the spend ticks with the volume of work — the thing we have just seen on the chart. The first: the model's answer varies from run to run, so "it works" is confirmed on a sample, and one lucky example does not count as proof. The second and the fourth do not change — not by a single word.

From there comes the answer to the question usually asked at this point: do features with AI need a separate process. Half of the apparatus you already know from ordinary development.

And one last thing. The second question, the one about the baseline, breaks more often than the other three, and it breaks for more than the odd team. The two cases ahead are exactly about that: a loud failure number that turned out to have no denominator, and a claimed autonomy that came out fourteen times off the company's own target.

---
id: s64
local_id: "s64"
section: "3. Moving Image"
type: analitika
title: "Physics Was Learned as Correlation, and It's Been Measured"
assertion: "The test is built on 396 real video recordings, 66 scenarios, three camera angles, and two takes of each scene, where the second take sets the upper bound — it shows how much reality itself repeats itself — and is normalized to one hundred percent; the best of six tested models scores 29.5 percent, and visual realism does not correlate with physical understanding at all: a coefficient of minus 0.46 at a significance level of 0.249, with video from one of the systems being the hardest of all to tell apart from the real thing"
source: "Physics-IQ"
chapter_ref: "chapter-part2d.md §3.8"
media: ""
media_needed: "visual content — a scale with the baseline 'two takes of one real scene = 100%' and a point at 29.5%, with a correlation field beside it; frames from the test are published on the paper's own page with no open license, so a custom chart is built from the published numbers"
scheme:
  kind: shkala
  unit: "percent of the upper bound"
  base: "396 video recordings, 66 scenarios, three angles each, two takes each"
  from: 0
  to: 110
  marks:
    - {value: "100", label: "Two takes of one scene"}
    - {value: "29.5", label: "The best of six models", key: true}
blocks_per_row: 2
blocks:
  - {label: "Plausibility and understanding", value: "coefficient −0.46 at a significance of 0.249", key: true, note: "one system's video is the hardest to tell from the real thing"}
  - {label: "Exactly where the line falls", value: "handled: paint smearing, pouring liquid", note: "not handled: a ball landing in a box, cutting a tangerine"}
itog:
  yarlyk: "Outcome"
  text: "Plausibility and understanding diverge; sign-off by eye does not work here"
timing_min: 1.5
in_bucket: true
status: собран
---

## Visible slide text

## Speaker notes

Here's a rare thing: a limitation that's been measured, and measured against an exemplary baseline.

How the test is built. 396 real video recordings were taken, 66 scenarios, three camera angles per scenario, and each scene shot twice. The second take sets the upper bound: it shows how much reality itself repeats itself when the same experiment is run a second time, and it's normalized to one hundred percent. This is an honest baseline, and choosing it is the work's strong point. Comparing a model against an abstract ideal is meaningless: the ideal is unreachable even for reality itself, because a ball dropped a second time falls slightly differently. Comparing against the world's own reproducibility gives a number that can actually be interpreted.

The result: every model evaluated shows a large gap, and the best one scores 29.5 percent, which, in the authors' own wording, indicates seriously limited physical understanding. Six leading systems of their time were tested.

The authors' main finding: visual realism does not correlate with physical understanding. The correlation coefficient is minus 0.46 at a significance level of 0.249 — meaning there is no relationship at all, neither positive nor negative, a value statistically indistinguishable from zero. What's more, video from one of the systems is the hardest of all to tell apart from the real thing, and that tells you precisely nothing about whether the ball lands in the box.

Let's spell out what this claim means for judgment. A person evaluates generated video with their eyes, and the only cue available to them is whether it looks right or not. The study shows that this cue carries no information about whether what's happening in frame is physically correct. So the ordinary way of signing off — look at it and decide — doesn't structurally work in this modality: it measures exactly the quantity that is unrelated to anything.

The specifics help fix the boundary in memory. Models handle paint smearing across glass and liquid pouring onto a rubber duck. They don't handle a ball landing in a box or cutting a tangerine with a knife. The pattern is visible: where the outcome is smeared and allows for many equally plausible results, the model lands; where the outcome is singular and determined by the laws of mechanics, it misses. This is a direct consequence of how it was trained: it learned what such scenes usually look like, not how bodies actually interact.

The direct, transferable engineering conclusion: plausibility and understanding diverge. Any production process in this modality must maintain a separate check on whether what's happening in frame is physically possible, and that check cannot be handed to the same eye that's judging the picture. For advertising and entertainment, the cost of this error is low; for training material, operating instructions, a demonstration of how a device works, or anything a viewer will go on to imitate, the cost is high, and generation cannot be used there without a separate check.

And a broader lesson that carries far beyond video. This is a general class of error: the cue a person uses to judge something and the property they actually care about can be unrelated — and until someone measures the relationship between them, we simply don't know. In language models, fluency has the same property: the smoothness of a phrasing says nothing about whether the statement is true, and the course has covered this before, on its own material. Here, the same affliction has acquired a numerical expression, and that is exactly why the slide belongs in the lecture: it's rare to be able to present a measurement for a claim of this kind.

What this means for planning. The claim "the next version will fix the physics" demands evidence that doesn't yet exist: over three years, the gap with reality's own reproducibility hasn't closed, and no relationship between realism and understanding has appeared. Plans should assume that checking physical plausibility stays outside the model and is done by a person who knows the subject matter.

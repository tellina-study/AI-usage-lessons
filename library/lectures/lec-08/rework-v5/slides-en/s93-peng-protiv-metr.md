---
# Source: chapter/chapter-part4b.md § 6.5 in full.
# Departure from DECK-KARTA: the map records the title with the word "frontier" — a calque, does
# not go into the visible body (form §5.21, the same reasoning as on s67). The title names the
# case: two studies that measured the same thing and diverged in sign. The phrase "jagged
# boundary" was introduced one frame earlier and is only picked up again here.
# UNIT. Both numbers on this frame are TIME: minus 55.8% and plus 19% of time per task.
# The nineteen percentage POINTS on the previous frame is the share of correct decisions, a
# different quantity. The unit is named in every line of both frames, or two "nineteens" in a
# row blur together (BRIEF-DEKA §3: two similar numbers are kept apart by their captions).
# The composition of Peng's forecast sample is ON THE FRAME: without it, "nobody guessed" reads
# as rhetoric.
# NOTE FOR THE TIMING GUARD: "71 minutes against 161" in the visible body is a SUBSTANTIVE
# duration — a measured average task-completion time in Peng's own study. It has nothing to do
# with the lecture's own timing and does not fall under BRIEF-DEKA §3's ban ("substantive
# durations are allowed"). It must not be cut: without it the 55.8 percent figure has no base.
id: s93
local_id: "s93"
section: "6. Wrap-up"
type: analitika
title: "Peng vs. METR: the same work, measurements diverging in sign"
assertion: "Two randomized studies of the same work gave a 55.8% speedup and a 19% slowdown, and the difference is explained by the maturity of the codebase; but the most useful thing in the pair is something else — nobody guessed the direction of the effect, including the participants themselves, after they had already slowed down"
source: "Peng et al., \"The Impact of AI on Developer Productivity: Evidence from GitHub Copilot,\" arXiv:2302.06590, 02/13/2023 · METR, \"Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity,\" 07/10/2025, arXiv:2507.09089"
media: ""
media_needed: "no photograph: the frame's subject is two measurements and a table of misses, and no illustration for them exists beyond the decorative. Checked: neither study has a single photograph of the experimental setup in the open domain under a usable license; the figures in the papers are distribution diagrams, and they lose to the frame's own table. The visible content is a two-sided time scale with zero in the middle and a table of four forecasts against one measurement"
diagramma:
  vid: "a horizontal time scale with zero in the middle: left — speedup, right — slowdown. Two measured points and four forecast points, all four forecasts sitting on the left half, METR's measurement on the right"
  podpis_edinitsy: "the whole scale is marked in percent of TIME per task"
sravnenie:
  columns: ["A task from scratch", "The same work in a mature codebase"]
  rows:
    - {name: "Who measured", a: "Peng et al., February 2023", b: "METR, July 10, 2025"}
    - {name: "Participants", a: "95 professional developers", b: "16 experienced open-source developers"}
    - {name: "What they did", a: "one HTTP server in JavaScript, as fast as possible", b: "246 real tasks in their own repositories — on average over a million lines of code and over 22,000 stars"}
    - {name: "Time per task", a: "55.8% less: 71 minutes against 161", b: "19% more than without the tool, on tasks from the same set"}
    - {name: "Why", a: "no codebase, no history of decisions, no implicit conventions — exactly the task the method handles best", b: "in a million lines with five years of conventions, the model doesn't know almost everything that matters"}
tablitsa_promakhov:
  caption: "Four forecasts against one stopwatch — all four about time per task"
  rows:
    - {kto: "The developers themselves, BEFORE the work", prognoz: "a 24% speedup"}
    - {kto: "The same developers, AFTER the work, already slowed down", prognoz: "sure they sped up by 20%"}
    - {kto: "34 economics specialists", prognoz: "a 39% speedup"}
    - {kto: "54 machine learning specialists", prognoz: "a 38% speedup"}
  zamer: "a 19% slowdown in time"
  oplata: "forecast accuracy was paid for — the reward was calculated from the size of the miss"
scheme:
  kind: shkala
  unit: "percent of time per task: left — faster, right — slower"
  base: "the same work without the tool, taken as zero"
  zero: true
  from: -60
  to: 60
  caption: "Four forecasts to the left of zero, the only stopwatch in a mature codebase — to the right"
  marks:
    - {value: "-55.8", label: "Peng: from scratch"}
    - {value: "-39", label: "34 economists"}
    - {value: "-24", label: "themselves, before the work"}
    - {value: "-20", label: "themselves, after"}
    - {value: "19", label: "METR: mature codebase", key: true}
blocks:
  - {label: "Gap between the measurement and self-assessment", value: "39 percentage points of self-deception", note: "between \"19% slower\" by the stopwatch and \"sure I'm 20% faster\" after the work", key: true}
  - {label: "What to do instead of a self-assessment survey", value: "30–50 of your own typical tasks and a stopwatch", note: "for images this is cheaper than for text: evaluating one sample takes seconds"}
blocks_per_row: 2
timing_min: 1.4
in_bucket: true
method_steps: ["cost of error in one unit", "two modes of work", "measurement against forecast", "what moved"]
form: []
vfy: false
status: собран
---

## Visible slide text

**Codebase maturity.** Peng — 95 developers, an HTTP server from scratch. METR — 16, 246 tasks, over a million lines. Not one of the four groups guessed the forecast.

## Speaker notes

Generative tools have a property that makes them dangerous precisely for the experienced
engineer: the feeling of speedup arrives before the speedup and outlives it. This is measured,
and measured twice with the opposite sign — which is why the pair below has to stand whole, both
halves together, and neither half can be torn off.

The first half. A controlled study, February 2023: ninety-five professional developers, task —
write an HTTP server in JavaScript as fast as possible. The group with the model finished fifty-
five and eight-tenths percent faster than the control: seventy-one minutes of average time
against one hundred sixty-one. The task here is from scratch. There is no codebase, no history of
decisions, no implicit agreements, no context to hold in your head. This is exactly the task the
method handles best: the same situation as "a first approximation of an idea costs a fraction of
a cent," which runs through the whole evening.

The second half. July 2025, also a randomized study, but the conditions are inverted: sixteen
experienced developers, two hundred forty-six real tasks in their own large repositories — on
average over a million lines of code and over twenty-two thousand stars, meaning codebases the
participants have worked in for years. Result: with model-based tools, tasks took nineteen percent
more time. The difference between plus fifty-six and minus nineteen is explained by the maturity
of the codebase. In an empty repository the model has nothing to not know; in a million lines
with five years of conventions, it doesn't know almost everything that matters, and its
suggestions have to be proofread. The same study measured this directly, and both quantities have
to be taken with their own denominators. Fewer than forty-four percent of the model's suggestions
are accepted — the count runs by suggestions the participant accepts or rejects in the editor, not
by lines and not by tasks, and it is collected from thirteen of the sixteen participants: three
worked on their own subscription, and that data was not captured from them. About nine percent of
working time goes to reading and cleaning up the output — this is measured across forty-four of
the two hundred forty-six tasks that have a labeled screen recording. Next to it stands a third
figure from the same series: three of four participants say they read every line of machine-
generated code, and more than half say what gets accepted has to be substantially reworked.

But in Wrap-up this pair stands for a different reason: every forecast missed at once. The
developers themselves, before the work began, predicted a twenty-four percent speedup. The same
developers, after the work, having already slowed down by the stopwatch, were sure they had sped
up by twenty. Outsiders made forecasts too: thirty-four economics specialists named a thirty-nine
percent speedup, fifty-four machine learning specialists named thirty-eight. This is not a street
poll: the participants were drawn from universities with leading programs, and they were paid for
forecast accuracy — the reward was calculated from the size of the miss. Nobody guessed the
direction of the effect. The composition of the sample matters here: without it, the line "nobody
guessed" sounds like rhetoric; with it, it is a measurement.

The gap between "19 percent slower" by the stopwatch and "sure I'm 20 percent faster" by self-
assessment is thirty-nine percentage points of self-deception. This is, perhaps, the single most
useful number of the whole evening for practice: it explains why a self-assessment survey — "AI
saved me so many hours" — cannot be the basis for an adoption decision. A report of hours saved,
collected by surveying employees, measures a feeling, and the gap between that feeling and the
stopwatch is what is counted here.

The authors honestly list what their result does not prove: that models do not speed up most
developers; that the conclusion carries over beyond experienced open-source developers; that it
will still be the same a year from now. This caveat is worth saying together with the number — it
is a model of how a good study reads, and it also keeps one experiment from turning into a
verdict on the tool.

The engineering consequence, fit for immediate use. Before bringing a generative tool into a
team's work, set up two things: a set of thirty to fifty of your own typical tasks and a
stopwatch. Run the candidates through it, compare yourself, measure by the result. For images this
is cheaper than for text: evaluating one sample takes seconds, and a set of fifty tasks runs in an
evening. Automated image-quality metrics will not help here — not one of them agrees with human
preference closely enough to base a model choice on it; the most commonly used one barely tells
apart "cat to the left of the dog" from "dog to the left of the cat," meaning it is blind to
exactly the composition it is usually invoked to judge.

The authors of the METR study themselves listed what it does not prove, and that caveat is worth
saying together with the number. It does not prove that models fail to speed up most developers.
It does not prove that the conclusion carries over beyond experienced open-source developers. And
it does not prove that it will still be the same a year from now.

Two figures from that same measurement explain where the time goes. In a mature codebase, fewer
than forty-four percent of the model's suggestions are accepted — the denominator here is
suggestions the participant accepts or rejects right in the editor, counted across thirteen of the
sixteen participants. And about nine percent of working time goes to reading and cleaning up the
output: this is measured across forty-four of the two hundred forty-six tasks that had a labeled
screen recording.

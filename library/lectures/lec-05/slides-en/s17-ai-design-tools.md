---
id: s17
type: process
section: "Section 2. Design"
duration_min: 1.5
assertion: "A generator widens the set of options in minutes, but a measurement with a control group gives about a 20% time reduction, not 'a day turns into minutes' — and the gain depends on the task and on who is doing the work"
learning_goal: "What AI changes in design: the 2026 tool set and an honest comparison of 'with a generator and without'"
learning_outcomes: [LO1, LO2]
chapter_ref: "§2.4 [for-slide-s17]"
interaction: none
verify_day_of: true
partial_out_strict_in: true
meme_or_visual: >
  process: on the left — four sketch cards (Lucide icon monitor-smartphone) as what the
  machine puts out in minutes, and under them a gold band with what the human does next.
  On the right — a list of named 2026 tools, each with one line about its mode of work
  rather than about the brand. At the bottom, full width — the measurement block with a
  control group: "how it was measured" / "what came out" + an italic correction for the
  conflict of interest.
source: "v0 (Vercel); Figma Make; Google Stitch; Lovable; bolt.new; Magic Patterns [VFY-day-of: the tool set and the status of the tools change fast]"
note: >
  issue #212, R6: the tool set is brought to 2026 (Lovable and Magic Patterns added, the
  March 2026 Stitch update noted). The stale estimate "2-4 directions in minutes instead of
  a day of manual wireframing" is replaced by a randomised trial with a control group
  (arXiv:2609.26725): that is the required "with AI and without" comparison. The earlier
  survey figures (72% / 91%) are dropped: that is self-report, not a measurement.
---

# Visible content

## Title bar
Interface generators: the machine gives options, a human picks and refines

## What the machine does itself: four different layouts of one screen in minutes
[Four MINIATURE LAYOUT SCHEMES, all different: option 1 — a header and a large block · option 2 — a header and a list of rows · option 3 — a side panel and content · option 4 — 2×2 tiles. The four identical monitor icons were removed after the student review (fix 5): they asserted the opposite of what the slide says.]

[Gold] Then the human: picks one direction, discards the rest and fixes what the model got wrong — spacing, order of importance, edge cases.

## The tools of 2026 [1]
- **Figma Make** — builds screens inside the design editor from the team's own components, not generic templates.
- **Google Stitch** — text and sketches into a screen; free, and since March 2026 it imports Figma files and emits code [2].
- **v0** — a description straight into interface code.
- **Lovable, bolt.new** — a description straight into a whole working app.
- **Magic Patterns** — fast sweep over variants of one screen.

## With a generator and without: measured, not promised [3]
**How it was measured.** A hundred participants — fifty designers and fifty product managers — randomly split into two groups: one got a generator, the other did not. Three identical interface-editing tasks, September 2026.

**What came out.** Overall time fell by about 20%. For product managers the gain is 35%. For professional designers — only on the hardest of the three tasks (26%), and their overall effect is borderline (17%).

*The measurement does not bear out the promise that "a day of manual wireframing turns into minutes": the gain is real, but it runs in tens of percent and depends on who works and how hard the task is. Figma ran the trial itself, on its own tool — keep that correction in mind.*

## Gold callout
The machine widens the set of options. Narrowing them to one is a decision about your users and your constraints, which the training data does not hold. The generator covers the screen; surfaces and touchpoints, system behaviour and the answer under uncertainty stay with the human.

## Speaker notes

The working order in a 2026 team looks like this. A human describes a screen or a flow in words, the generator puts out several diverging sketches, and the human then picks one direction, discards the rest and fixes what the model got wrong: spacing, order of importance, edge cases. The chosen direction goes through a real test on live people — a persona invented by a model does not replace that — and only after it does the work go into development.

There are five tools on the slide. What distinguishes them is the mode of work, so look at the second half of each line. Figma Make builds screens right inside the design editor and takes the team's own components instead of generic templates — which is why its output needs less rework. Google Stitch goes from text and sketches to a screen, is free, and since March 2026 can pull Figma files in and emit code. The tool v0 outputs interface code directly. Lovable and bolt.new assemble a whole working application. Magic Patterns is for when you need to sweep quickly through variants of one screen. The landscape moves fast — check the set before the class.

Now the thing this slide was rebuilt for. The discussion usually carries a promise: a day of manual work turns into minutes. There is a measurement, and it says something else. A hundred participants, half designers, half product managers, randomly split into two groups: one got a generator, the other got nothing, the tasks identical. Overall time fell by about twenty percent. For product managers the gain was thirty-five percent. For professional designers it shows only on the hardest of the three tasks — twenty-six percent there — and their overall effect is borderline, seventeen: on the easy tasks there is simply no difference from the control group.

Two conclusions from that. The gain is real, and it is measured in tens of percent. Not in orders of magnitude. And it depends on who is working: the generator helps most the person for whom the task is not routine. A correction: Figma ran the trial itself, on its own tool.

And one more thing that is easy to miss behind the numbers. The generator removed the barrier to entry: someone who cannot draw interfaces now brings something presentable to a discussion instead of boxes and arrows. That is a genuine benefit. But the ability to get a good-looking screen quickly is not the same as the ability to design an interaction and test it on a live human.

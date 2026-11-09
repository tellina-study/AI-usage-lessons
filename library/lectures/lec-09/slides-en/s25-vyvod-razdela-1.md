---
id: s25
local_id: s1-08
section: "1. Autonomous robots in space"
type: norm
title: "Section 1 conclusion"
assertion: "Geometry goes to the classical approach, recognizing an object against noise goes to the model, a wholly new task has no classical equivalent at all"
source: "—"
media: ""
media_needed: "No visual — a transitional slide. Phase 6. Phase 8: `blocks:` plates added as a minimal visual anchor (presentation-critic finding: the slide was half empty). Phase 9 (issue #317): the visible text and plates were rebuilt — the 'column a/b/c' table (the lecture's own internal case-study-corpus classification, not content about space) was replaced with a substantive section conclusion and plates carrying specific numbers for each case from the chapter's §1.7."
blocks:
  - {label: "AEGIS", value: "productivity grew almost 4×", note: "range geometry + a lightweight classifier on top of it, routine since 2016", key: true}
  - {label: "SPOC", value: "98% soil-labeling accuracy", note: "a deep network on pixels — currently a support tool on the ground, not an onboard module"}
  - {label: "COROB-X", value: "cave reconnaissance with no human inside", note: "three robots and a tether instead of one human with a flashlight — a task with no classical equivalent"}
  - {label: "LeoLabs", value: "up to 400% more close-approach warnings", note: "at detection of objects from 2 cm — the satellite operator still decides whether to respond"}
in_bucket: false
status: draft
---

## Visible slide text

Geometry is solved with no training — by classical calculation. Recognizing an object against noise is solved by a lightweight model inside a classical pipeline, not replacing it. A wholly new task — cave reconnaissance with no GPS or communication — has no classical equivalent at all.

Next — Section 2: the same task, a different degree of autonomy.

## Speaker notes

Geometry in this section is solved with no training at all — a direct, engineering-grounded criterion for where a trained model isn't needed and isn't even useful: it would add unpredictability exactly where a decision can be proven mathematically rather than guessed from the statistics of examples. Recognizing an object against statistical noise is solved by a lightweight trained model built into a classical pipeline, not replacing it. A wholly new task — exploring a cave with several robots, with no GPS and no communication — has no classical equivalent at all, and here we honestly call this novelty, not a gap in the research.

For AEGIS, geometry (range measurement from a stereo camera pair) and a lightweight random-forest classifier together raise target-selection accuracy from 24% to 93% — the rover's scientific productivity grew almost fourfold, routinely, since 2016. For SPOC, a deep network works right on the pixels of an image and labels soil type and hazards at 98% accuracy — but for now this is a support tool for the rover driver on the ground, not an onboard module of the rover itself. For COROB-X, a CNN detector finds the cave artifact in a frame, and geometry — as with AEGIS — localizes the already-found object in space; the price of this autonomy is three different machines and a physical tether between them instead of one human with a flashlight. For LeoLabs, the model neither classifies nor detects, but predicts which observation will deliver more value: close-approach warnings became up to 400% more frequent at detection of objects from 2 cm, but the satellite operator still decides on their own whether to respond to the warning.

Later in the lecture — Section 2 shows a different point on the same spectrum: a system where a human still holds control, just at a distance, and shows this with a deliberate break in form — not a stage definition, but a specific scene.

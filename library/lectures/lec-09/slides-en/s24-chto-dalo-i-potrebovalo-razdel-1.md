---
id: s24
local_id: s1-07
section: "1. Autonomous robots in space"
type: schema_matrix
title: "What it gave and what it required — Section 1"
assertion: "The gain is large where the technology has flown for years; where it hasn't flown, that's stated directly"
source: "—"
media: ""
media_needed: "A 'task type × modality' table, cumulative after Section 1. Phase 6."
columns:
  left: {label: "Gave", items: ["Scientific productivity ×4 (AEGIS)", "Soil labeling at 98% accuracy (SPOC)", "Reconnaissance of unreachable places (COROB-X)", "Up to 400% more warnings (LeoLabs)"]}
  right: {label: "Required", items: ["Pre-certified thresholds (geometry)", "More complexity: 3 robots instead of 1 human", "$60 million/year of radar infrastructure", "The decision to respond stays with the operator"]}
table:
  headers: ["Grid cell", "Case study"]
  rows:
    - ["Classification × image", "AEGIS, SPOC (at different depths)"]
    - ["Recognition × image", "COROB-X"]
    - ["Classification × structured data", "LeoLabs"]
in_bucket: false
status: draft
---

## Visible slide text

**In sum:** the gain is measurable and large where the task is already solved and confirmed by working operation (AEGIS since 2016, SPOC as a ground tool already today, LeoLabs as a commercial service). Where the technology hasn't been tested on the real Moon or Mars, that's stated directly.

## Speaker notes

What it gave: scientific productivity that grew almost fourfold (AEGIS); soil and hazard labeling at 98% accuracy, sparing drivers from having to build an assessment of every image from scratch (SPOC); reconnaissance of places physically unreachable safely for a human (COROB-X); close-approach warnings coming out up to 400% more often at detection from 2 cm (LeoLabs).

What it required: pre-calculated and certified safety thresholds where the decision stays geometric and classical — such a decision isn't delegated to learning precisely because its correctness has to be proven mathematically, not statistically; added system complexity where the task is entirely new — three robots and a physical tether instead of one human with a flashlight; growing commercial radar infrastructure and a satellite operator's own willingness to decide whether to respond to someone else's warning — a growing number and accuracy of warnings alone doesn't guarantee anyone actually responds to them.

The section's first three detailed case studies sit on one axis: in all three, a trained model is brought in exactly where a classical calculation would be insufficient (recognizing an object against statistical noise) or unreachable in reasonable time. AEGIS's classifier is lightweight — a random forest on top of geometric features. SPOC's model is heavier and works right on pixels. COROB-X's CNN detector finds the artifact, while geometric localization stays classical. The section's only case with no trained model at all is NASA IPEx (a mention). LeoLabs sits apart on this axis: the task isn't recognizing an undefined object against noise, but prioritizing a limited observation resource among a growing, already-cataloged number of candidates — a second, separate axis of the "classical approach alone / a model is needed" boundary.

The stage's cumulative map: after Section 1, three cells of the course's grid are filled — "classification × image" (AEGIS and SPOC), "recognition × image" (COROB-X), "classification × structured data" (LeoLabs). The cell NASA IPEx could have filled stays honestly empty.

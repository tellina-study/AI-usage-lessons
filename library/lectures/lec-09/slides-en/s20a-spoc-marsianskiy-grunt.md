---
id: s20a
local_id: s1-04-2
section: "1. Autonomous robots in space"
type: case_study
title: "Soil for SPOC"
assertion: "The three surface types in this image are the raw data of AI4Mars, the same project whose data set SPOC keeps learning from"
source: "[NASA Science, PIA23897, 06.12.2020](https://science.nasa.gov/resource/martian-terrain-as-viewed-in-ai4mars/)"
media: "assets/razdel-1/spoc/spoc-01-pia23897-ai4mars-terrain.jpg"
media_hero: true
media_hero_target: 0.50
media_caption: "Photo: NASA/JPL-Caltech, Martian soil types from the AI4Mars project's data"
media_needed: "already downloaded (Tier 1, NASA PIA23897). A large illustration for the SPOC case study, added per owner instruction (Phase 10, issue #317) — every example now has a large illustration, not just a few."
in_bucket: false
status: draft
---

## Visible slide text

**Four surface classes, not an abstraction.** Soil, bedrock, sand, and large rock — exactly the types AI4Mars asks volunteers to label.

**This data is what holds up the 98% accuracy.** Without a steady stream of newly labeled data, SPOC can't learn new Martian terrain.

## Speaker notes

The photo shows three frames from Curiosity's navigation and mast cameras, with Martian soil types marked by the AI4Mars project: sand, bedrock, large rock, and ordinary soil. This isn't SPOC's output — it's the raw material: the same set of classes that volunteers on the Zooniverse platform label by hand on rover images, and it's exactly this labeled data that SPOC learns to tell safe surface apart from dangerous surface from.

The neighboring case study has already named the cost of a classification error — a rover getting stuck in loose sand mistaken for firm soil, with the risk of months of recovery or losing the vehicle. This image shows why the 98% accuracy figure isn't fixed forever: the AI4Mars project continuously collects new labels from new Perseverance images, and those labels feed back into training — the feedback loop is set up explicitly, by name, unlike AEGIS and COROB-X, where the composition of the training set isn't disclosed.

Three classes in one frame is a concrete answer to "what exactly does SPOC classify": not a binary "dangerous / not dangerous", but several surface types at once, each carrying its own risk for the rover's movement.

---
id: s66a
local_id: "s66a"
section: "3. Moving Image"
type: analitika
title: "The Cumulative Map: the 'Video' Column Filled In"
assertion: "After three sections, the 'task type × modality' map is filled in for three columns out of five; the row 'generate a first approximation' grows by an order of magnitude left to right at every transition, and that is the main thing the map shows — the more expensive the unit of output, the more attempts have to be sifted through for one usable one"
source: ""
chapter_ref: "chapter-part2d.md §3.9"
media: ""
media_needed: "visual content — the grid of the map itself; an image would be superfluous here"
map_canonical: "BRIEF-DEKA.md §12 — row and column labels are matched to this list verbatim"
matrix:
  rows:
    - label: "Generate a first approximation"
      cells:
        - "$0.034–0.05 per image"
        - "dubbing $0.03–0.072 per minute"
        - "the price of a release is 10–20 times lower"
    - label: "Bring to production quality"
      cells:
        - "adapters and manual touch-up"
        - "manual diction fixes"
        - "manual selection and assembly"
    - label: "Restore what already exists"
      cells:
        - "upscaling archival footage"
        - "source separation"
        - "frame interpolation"
    - label: "Hold exact measurements"
      cells:
        - "none: there are no dimensions in the output"
        - "none: length is set before launch"
        - "none: physics was learned as correlation"
    - label: "Fit the real-time budget"
      cells:
        - "not applicable: the stage has no frame budget"
        - "not applicable: the stage has no frame budget"
        - "none: doesn't fit inside a frame budget"
    - label: "Answer 'who is accountable'"
      cells:
        - "none: the source of the detail isn't recorded"
        - "none: the source of the detail isn't recorded"
        - "none: the source of the detail isn't recorded"
  columns: ["Image", "Sound", "Video"]
  columns_to_come: ["3D", "Recognition"]
  state: "three columns of five are filled"
  footer_band:
    label: "payment address"
    values: ["Image — selection, rights", "Sound — rights, discernment", "Video — selection"]
    values_to_come: ["3D", "Recognition"]
    note: "a band BELOW the grid, not a row of the table"
  canonical: "BRIEF-DEKA.md §12 — row labels, column names, and cell content are identical across all six presentations of the map"
  cell_rule: "a cell holds either a number, or 'none' with a reason, or 'not applicable' with a reason — no bare glyphs are left (owner's decision, 10/27/2026)"
timing_min: 0.5
in_bucket: true
timing_note: "split off from s66 by body height: 1.5 -> 1.0 (s66) + 0.5 (s66a). Section 3's total did not change"
status: собран
---

## Visible slide text

**The cheapness of an attempt and the expense of choosing grow together: the more expensive the unit of output, the more trials have to be sifted through for one usable one.**

## Speaker notes

The cumulative map is now filled in for three columns out of five after three sections. The row "generate a first approximation" grows by an order of magnitude left to right at every transition, and that is exactly what the map shows: the more expensive the unit of output, the more attempts have to be sifted through to get one usable one. The cheapness of an attempt and the expense of choosing grow together. Below the grid runs the payment-address band: for image, that's selection and rights; for sound, rights and discernment; for video, selection.

The section's conclusion, in three parts. Where the benefit is: producing a single shot got three orders of magnitude cheaper, and this is counted against the classical mode three separate times — the micro-drama from a million yuan down to 50–100 thousand, the ad from forty thousand dollars down to two thousand, a major campaign's production cycle from a year down to a month. In none of the three cases was the gain counted from zero. Where the limits are: there is no object between frames that stays "the same"; physics was learned as correlation, and the best model gives 29.5 percent of reality's own reproducibility; length and resolution are bought non-linearly — tripling resolution costs forty times the training time. What load moves further down the line: selection — 400 generations for 15 clips, 300 to one, hundreds of shots for a couple dozen; and the tool's durability — two flagships shut down within thirteen months, and a film built on one of them slipped by a year.

The technical conclusion drawn from this section's material: the main lever is the tokenizer. The autoencoder's compression ratio, raised to 32, cut the token count from 76 to 19 thousand and brought the cost of training a commercial video model down to two hundred thousand dollars; model size stayed unchanged throughout.

How to read the map out loud. The first row answers the question "can you even start work with this" and, across all three filled columns, answers "yes, and cheaply." The second answers "can you finish with this" and, across all three columns, runs into manual human work: touch-ups, selection, assembly. The third is the only one where the model has an honest metric and an upper bound, computed with the answer already known. The bottom three rows are filled with the word "none" or "not applicable," and every cell names the reason for the refusal rather than a bare "none." There are no empty cells in the filled columns, and that's a mandatory property of the map: wherever a measured case wasn't found, the map says exactly what is known and what's missing.

Two columns are still ahead — the 3D scene and recognition. The rows will not change even once: the map accumulates by column, and they will never need to be rewritten. That's exactly its value as a tool: by the end of the evening, six task types will have been checked against five modalities with the same question, and the modalities will be comparable row by row, without holding five separate stories in your head.

It's worth separately saying what the map does not do. It doesn't compare modalities by quality and doesn't say which one is "better": the cell "$0.034–0.05 per image" and the cell "the price of a release is 10–20 times lower" are measured in different units and sit side by side only because they answer the same question. The map answers "what can even be handed to a model here," not "where is it stronger." The second question isn't settled by a grid like this, and trying to read a modality ranking out of it is the most likely reading error.

The easiest way to use the map beyond the lecture: take your own task, work out which of the six rows it falls into, and read the cell for your modality. If the cell holds a number, there's a measured case, and you can start from it. If it says "none" with a reason, the reason is named, and it's usually stronger than any setting you could tune. If it says "not applicable," the question isn't being asked of that stage, and that, too, is an answer.

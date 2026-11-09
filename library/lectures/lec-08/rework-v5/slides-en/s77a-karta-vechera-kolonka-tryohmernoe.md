---
# This slide was obtained by splitting s77 during the first render fix (2026-10-27):
# everything that used to be on one slide didn't fit the 5.36" body at any point size.
# The numbers, plates, columns, diagrams, and map cells are carried over UNCHANGED; the
# minutes are taken from the budget of s77 itself (0.5 → 0.3 + 0.2), the section total
# untouched.

id: s77a
local_id: "s77a"
section: "4. 3D Scenes and Real Time"
type: assertion_visual
title: "Map of the evening: the \"3D\" column"
assertion: "After the fourth modality, the map of the evening has four of five columns filled: for 3D, generation is measured in units of seconds per variant, reconstruction in forty-one minutes of training and a hundred thirty-four frames per second, the real-time budget in one millisecond per frame, while the rows for exact measurements and accountability are empty, just as for the previous three modalities"
source: ""
chapter_ref: "chapter-part3c.md §§ 4.19, 4.21; REESTR-RAZBOROV-part3.md § 2.1"
media: ""
media_needed: ""
matrix:
  rows:
    - label: "Generate a first approximation"
      gloss: "get variations of a look while the decision hasn't been made yet"
      cells:
        - "$0.034–0.05 per image"
        - "dubbing $0.03–0.072 per minute"
        - "release cost 10–20 times lower"
        - "units of seconds per variant"
    - label: "Bring to production quality"
      gloss: "select, finish, and ship something fit for use"
      cells:
        - "adapters and manual fixes"
        - "manual diction fixes"
        - "manual selection and splicing"
        - "retopology, unwrapping, and rigging — to people"
    - label: "Restore what already exists"
      gloss: "pull out what's already recorded but reads poorly"
      cells:
        - "upscaling an archive"
        - "source separation"
        - "frame interpolation"
        - "scene from photographs: 41 min training, 134 frames/s"
    - label: "Hold exact measurements"
      gloss: "dimensions, tolerances, checkable conditions"
      cells:
        - "no: dimensions don't exist in the output"
        - "no: length is set before the run"
        - "no: physics is learned as a correlation"
        - "no: dimensions don't exist in the output"
    - label: "Fit the real-time budget"
      gloss: "make the frame deadline, not the task deadline"
      cells:
        - "not applicable: the stage has no frame budget"
        - "not applicable: the stage has no frame budget"
        - "no: doesn't fit the frame budget"
        - "about 1 ms per frame"
    - label: "Answer 'who is accountable'"
      gloss: "provenance, rights, a signature behind the result"
      cells:
        - "no: the source of the detail isn't recorded"
        - "no: the source of the detail isn't recorded"
        - "no: the source of the detail isn't recorded"
        - "no: the source of the detail isn't recorded"
  columns: ["Image", "Sound", "Video", "3D"]
  columns_to_come: ["Recognition"]
  state: "four of five columns filled"
  footer_band:
    label: "payment address"
    values: ["Image — selection, rights", "Sound — rights, discernment", "Video — selection", "3D — discernment"]
    values_to_come: ["Recognition"]
    note: "a band UNDER the grid, not a row of the table"
  canonical: "BRIEF-DEKA.md §12 — row labels, column names, and cell content are identical across all six presentations of the map"
  cell_rule: "a cell holds either a number, or 'no' with a reason, or 'not applicable' with a reason — no bare glyphs are left (owner decision, 2026-10-27)"
matrix_footer: "The payment address accumulates by the same steps: selection · rights · discernment. For this section, there's one address — discernment."
timing_min: 0.2
in_bucket: true
method_steps: ["cost layer", "substantive gap", "cumulative map"]
form: []
vfy: false
status: собран
---

## Visible slide text

**Four of five columns.** Two rows sit empty across all four modalities in a row: exact measurements and the answer to "who is accountable."

## Speaker notes

About the map. Two of its rows are filled the same way all the way across, and that's worth reading crosswise. The row "bring to production quality" is empty or conditional in all four modalities: a human finishing step remains everywhere, and everywhere it's exactly where the load has moved. The row "hold exact measurements" is empty everywhere it even applies: a generative model doesn't convert plausibility into conformance in a single modality. The fifth column will appear next section, and one of these two rows will finally fill in — that's the whole reason the map has been kept running all evening.

The map of the evening is one map for the whole lecture, and it's cumulative: after every modality, one new column appears in it, and the rows stay the same six. It's worth reading in full after the fourth column, because this is the first place you can see what's repeating in it.

The row "generate a first approximation" is filled everywhere, and everywhere cheaply: from three and a half cents per image to units of seconds for a 3D variant. The row "bring to production quality" is filled everywhere, and everywhere the same way — by human manual work: adapters and fixes for image, diction fixes for sound, selection and splicing for video, retopology, unwrapping, and rigging for 3D. The row "restore what already exists" is filled everywhere, and everywhere it's the method's strong side, because reconstruction has a held-back reference you can check the result against.

And then come two rows that read "no" all the way across. "Hold exact measurements" — no for image, no for sound, no for video, no for 3D, and the reason named each time is different on the surface but one at bottom: the model is trained on what things look and sound like, not on what they measure. "Answer who is accountable" — no everywhere, also for one reason: the source of the detail isn't recorded anywhere, because the detail was obtained by denoising, not pulled from some one training example.

Here's what the map shows that no single breakdown would have shown. Two empty rows aren't a property of one particular model and not a shortcoming of one particular year. They're identical across four different modalities with different architectures, different corpora, and different manufacturers, which means it's a property of the class of methods. The fifth column will appear on the next slide, and for the first time all evening something in these two rows will change.

For practice, this leads to a habit useful well beyond this lecture. When you're evaluating a new class of tools, build the same kind of grid yourself: one axis the types of task you need to solve, the other the tools or modalities. Fill it with what's measured, and make sure to leave cells with the word "no" and a named reason. An empty row across the whole row is the find such a grid is built to catch: it means you're looking at a limitation of the class, not a lag of one particular vendor, and it's not worth waiting for the next version to close it.

And a practical consequence for reading any such grid. An empty cell and a cell with the word "no" are different statements. Empty means "we didn't check"; "no" with a named reason means "we checked, it doesn't work, here's why." In this map there isn't a single empty cell: everywhere there's either a number, or "no" with a reason, or "not applicable" with a reason. That's how to run your own grids too.

---
# Frame obtained by splitting frame s87 during the fix for the first render (2026-10-27):
# everything that stood on one frame did not fit the 5.36" body at any point size.
# Numbers, plates, columns, diagrams and map cells carried over UNCHANGED; minutes taken
# from the budget of frame s87 itself (1.2 → 0.8 + 0.4), the section's total untouched.

id: s87a
local_id: "s87a"
section: "5. Recognition and Provenance"
type: analitika
title: "Map of the evening: the 'Recognition' column — the map is complete"
assertion: "The fifth column completes the map of the evening and turns out to be the only one for which the rows 'hold exact measurements' and 'answer who is accountable' get an answer at all: ground-truth labeling gives a number, and a signature outside the file answers partially — it's about the signer; for all four generative modalities, both rows are empty"
source: "Kirill Pshinnik, co-founder of Zerocoder, published October 16, 2026"
chapter_ref: "chapter-part3e.md § 5.10"
media: ""
media_needed: ""
matrix:
  rows:
    - label: "Generate a first approximation"
      gloss: "get a range of looks while the decision is still open"
      cells:
        - "$0.034–0.05 per image"
        - "dubbing $0.03–0.072 per minute"
        - "release cost 10–20x lower"
        - "single-digit seconds per variant"
        - "not applicable: generation is not this stage's task"
    - label: "Bring to production quality"
      gloss: "select, finish, and release something fit to ship"
      cells:
        - "adapters and manual editing"
        - "manual diction editing"
        - "manual selection and editing"
        - "retopology, UV unwrapping, rigging stay with people"
        - "a human in the loop with a time norm"
    - label: "Restore what already exists"
      gloss: "pull out what's already recorded but reads poorly"
      cells:
        - "archive resolution upscaling"
        - "source separation"
        - "frame interpolation"
        - "a scene from stills: 41 minutes, 134 frames per second"
        - "yes: the scroll read in full, the answer is checkable"
    - label: "Hold exact measurements"
      gloss: "dimensions, tolerances, checkable conditions"
      cells:
        - "no: there are no dimensions in the output"
        - "no: length is set before the run"
        - "no: physics is learned as correlation"
        - "no: there are no dimensions in the output"
        - "yes: ground-truth labeling gives a number"
    - label: "Fit the real-time budget"
      gloss: "make the frame deadline, not the task deadline"
      cells:
        - "not applicable: the stage has no per-frame budget"
        - "not applicable: the stage has no per-frame budget"
        - "no: doesn't fit the per-frame budget"
        - "about 1 ms per frame"
        - "yes: moderation runs continuously"
    - label: "Answer 'who is accountable'"
      gloss: "provenance, rights, the signature under the result"
      cells:
        - "no: the detail's source isn't recorded"
        - "no: the detail's source isn't recorded"
        - "no: the detail's source isn't recorded"
        - "no: the detail's source isn't recorded"
        - "partially: a signature outside, and it's about the signer"
  columns: ["Image", "Sound", "Video", "3D", "Recognition"]
  columns_to_come: []
  state: "the map is complete: five columns out of five"
  footer_band:
    label: "payment address"
    values: ["Image — selection, rights", "Sound — rights, discernment", "Video — selection", "3D — discernment", "Recognition — discernment"]
    note: "a band BELOW the grid, not a row of the table"
  canonical: "BRIEF-DEKA.md §12 — row labels, column names, and cell content are identical across all six presentations of the map"
  cell_rule: "a cell holds either a number, or 'no' with a reason, or 'not applicable' with a reason — no bare glyphs remain (owner decision, 2026-10-27)"
# Overhaul of forms (#301, Section 5, brief §14): the top-level `matrix_footer` key is DEAD —
# the core does not read it (the builder reads only the nested `matrix.footer_band`, and draws
# it as a separate band BELOW the grid). The content was not silently lost — the same idea
# already stood in the speaker notes — but it was asserted by nothing on the frame. Carried
# into `itog`, category "Payment address": s87a is literally the section's closing
# (brief §4, "section closing"), and the payment-address band is exactly the conclusion read
# last from the frame here. The `matrix_footer` key was removed rather than left silent next to
# the working one.
itog:
  yarlyk: "Payment address"
  text: "it accumulates through the same steps — selection · rights · discernment; for both of the section's breakdowns it is one and the same — discernment"
timing_min: 0.4
in_bucket: true
method_steps: ["①cost of both errors", "②both modes on one scale on one sample", "③the share curve", "④how it was measured", "⑤what moved downstream", "map"]
form: []
vfy: false
status: собран
---

## Visible slide text



## Speaker notes

About the map. It is filled in here for the last time, and it's worth reading across, by two rows. The row "hold exact measurements" is empty in all four generative modalities and filled in the recognizing one: recognition has ground-truth labeling, generation has none by construction. From this comes a practical criterion for tool choice that the course can offer: if a task has a correct answer, it most likely should be solved by recognition. The row "answer who is accountable" is empty almost everywhere, and the one filled cell is filled with a caveat: a signature answers about the signer, not about what was shot. The question of accountability for a technical decision has no answer in any modality of the evening — and this section hands that fact onward.

The map of the evening is filled in here for the last time, and it has to be read across, by rows, not by columns. It's exactly this crosswise reading that shows something no single breakdown on its own would show.

The row "generate a first approximation." Filled for all four modalities, and cheap everywhere: from three and a half cents per image to single-digit seconds for a 3D variant. For recognition, this row holds "not applicable": generation is not this stage's task, and that's more honest than a dash.

The row "bring to production quality." Filled for all five, and filled the same way — by a human's manual work. Adapters and edits for image, diction editing for sound, selection and splicing for video, retopology, unwrapping, and rigging for 3D, a human in the loop with a time norm for recognition. Generating got cheap everywhere; bringing to production quality didn't get cheaper anywhere.

The row "restore what already exists." Filled for all five, and everywhere it's the method's strong side, because restoration has a deferred ground truth.

And the two rows the whole map was worth keeping all evening for. "Hold exact measurements" — "no" for image, sound, video, 3D, and for the first time "yes" for recognition: ground-truth labeling gives a number. "Answer who is accountable" — "no" for all four generative modalities and "partially" for recognition: a signature exists, but it's about the signer, not about what was in front of the lens.

This is the outcome of five sections, expressed as a grid. Two empty rows are identical across four different modalities with different architectures, different corpora, and different vendors — which means this is a property of the class of methods, not a lag in someone's particular version. And the answer to them is given by the one modality that doesn't generate but reads. From here you can also read the band below the grid: the payment address accumulated through the same steps — selection, rights, discernment — and for the last two sections it's one and the same.

From reading the map across comes a technique useful far beyond this lecture. When you evaluate a class of tools, build such a grid yourself: on one axis the task types you need to solve, on the other the tools. Fill the cells with what's measured, and where there's nothing measured, write "no" or "not applicable" with a named reason — don't leave a bare dash. A bare dash reads as "forgot to check"; a named reason reads as a conclusion reached.

The value of such a grid is in the rows, not the cells. One empty cell is a special case. An empty row across the whole line is a property of the class of methods, and that's the one observation worth keeping such a grid for at all, rather than looking at tools one at a time.

And lastly. The map was presented six times this evening and each time in the exact same form: the same six rows, the same column names, the same cells. This isn't layout pedantry — it's the only way a cumulative grid works at all: the viewer has to recognize the row, not reread it from scratch.

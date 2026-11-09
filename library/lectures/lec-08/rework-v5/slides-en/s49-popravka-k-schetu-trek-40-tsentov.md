---
id: s49
local_id: "s49"
section: "2. Sound: Speech Synthesis, Performer Voice, and Music"
type: analitika
title: "A correction to the bill: a downloadable track costs $0.40, not $0.016"
assertion: "The widely cited price of a generated track, around a cent and a half to two cents, is the price of generation; the price of a track you can actually take with you and use is different: a plan at eight dollars a month gives twenty downloads, that is, $0.40 per downloadable track, and the gap between the two units is a factor of twenty-five, which makes the gap against a $20–100 stock license fifty- to two-hundred-fifty-fold instead of a thousandfold"
source: "a music service's price list, read 10/27/2026"
chapter_ref: "chapter-part2b.md §2.9, §2.11"
media: ""
media_needed: "the visual content is the bill shown on the frame in two steps, and the running map underneath it; a photograph would crowd out both"
blocks:
  - {label: "The price of generation", value: "about $0.016 per track", note: "widely cited; counts a button press"}
  - {label: "The price of a downloadable track", value: "$0.40", note: "eight dollars a month divided by twenty downloads — 8 ÷ 20", key: true}
  - {label: "The gap between the two units", value: "a factor of 25", note: "the same service, different denominators"}
  - {label: "The gap against a $20–100 stock license", value: "50–250×", note: "not in the thousands, as you get when counting at the price of generation"}
map_canonical: "BRIEF-DEKA.md §12 — row and column labels follow this list verbatim"
matrix:
  rows:
    - label: "Generate a first approximation"
      cells:
        - "$0.034–0.05"
        - "dubbing $0.03–0.072/min"
    - label: "Bring to production quality"
      cells:
        - "adapters and manual editing"
        - "manual diction fixes"
    - label: "Restore what already exists"
      cells:
        - "archive upscaling"
        - "source separation"
    - label: "Hold exact measurements"
      cells:
        - "no: dimensions do not exist here"
        - "no: length is set before launch"
    - label: "Fit the real-time budget"
      cells:
        - "not applicable: there is no frame budget"
        - "not applicable: there is no frame budget"
    - label: "Answer 'who is accountable'"
      cells:
        - "no: the source is not recorded"
        - "no: the source is not recorded"
  columns: ["Image", "Sound"]
  columns_to_come: ["Video", "3D", "Recognition"]
  state: "two columns of five are filled in"
  footer_band:
    label: "payment address"
    values: ["Image — selection, rights", "Sound — rights, discernment"]
    values_to_come: ["Video", "3D", "Recognition"]
    note: "a band BELOW the grid, not a row of the table"
  canonical: "BRIEF-DEKA.md §12 — row labels, column names, and cell content are identical across all six presentations of the map"
  cell_rule: "a cell holds either a number, or \"no\" with a reason, or \"not applicable\" with a reason — no bare glyphs are left (owner decision, 10/27/2026)"
timing_min: 0.8
in_bucket: true
status: собран
---

## Visible slide text


## Speaker notes

A section on price would be dishonest without one arithmetic correction, and it works against the nice-looking numbers from the voice-over breakdown.

The widely cited price of a generated track is about a cent and a half to two cents. This is the price of generation: that is what it costs to press a button and get a result inside the service. The price of a track you can actually take with you and use is different. On an eight-dollar-a-month plan, the user gets twenty downloads — that is, eight divided by twenty, forty cents per downloadable track. The gap between the two units is a factor of twenty-five, and both figures are correct at the same time: they are counting different things.

The right comparison against a $20–100 stock license is forty cents, not the smaller figure, and the gap then comes out at fifty to two hundred fifty times instead of in the thousands. This is still an enormous gap; it is a order and a half of magnitude smaller than the one usually quoted, and for an engineer, getting the right order of magnitude matters more than remembering the nicer-sounding one.

The method of counting is shown right on the frame, because this class of error recurs more than once over the evening. The general shape of it is: the price list names the price of one attempt, production cares about the price of one usable result, and between the two sits a selection factor that the price list never mentions at all. In images, the same thing produced thirty to a hundred generations for one usable illustration; in video, which the section moves to next, it will be four hundred generations for fifteen edits. The rule is one and the same: the unit of account is what actually went to the client.

Now the section's conclusion, in three parts.

Where the benefit lies. Where the task reduces to reproducing a known sound, the model, by 2026, has closed it with a gap of hundreds and thousands of times against the classical mode: a minute of voice-over costs $0.03 to $0.072 against $50–450 for a voice talent. Where a classical mode does not exist at all, it has delivered a result that no amount of money could previously buy: a voice for someone who lost speech, and a role for an actor whose voice was taken by surgery.

Where the limits lie. The model has no concept of a performer, singing is not supported, emotion is set by markup, and output length is assigned before launch. Quality runs into the codec's decoder before it runs into model size. And, most practically: part of what the press calls generation is not generation at all — source separation returned a song to the world without generating a single note, and confusing the two means choosing the wrong tool.

What load carries forward through the cycle. Rights. A voice model outlives the person, and Russian law has no norm on voice; the one case to reach a ruling was lost because the court read a five-year-old contract. This load carries over into the section on recognition and provenance, and further on into the Wrap-up, where the payment address is named.

The technical conclusion, confirmed on this section's material: the main lever here is the tokenizer. Output length is set by the codec's frame rate, from 5 to 21.5 hertz across 2026 models; generator size barely affects it, while the codec itself fits in 8.4 million parameters and runs on a single core of a smartphone processor.

The running map, after two sections, is filled in for two columns out of five. Its rows are the six task types, and each new modality adds its own column rather than rewriting the rows. There are no empty cells in the filled columns: where there is no measured case, what is known and what is missing is named outright — that is an honest state, not a gap in selection. Below the map runs the payment-address band: for images it is selection and rights, for sound it is rights and discernment. The band accumulates with the same steps as the columns, and it will arrive at the Wrap-up complete.

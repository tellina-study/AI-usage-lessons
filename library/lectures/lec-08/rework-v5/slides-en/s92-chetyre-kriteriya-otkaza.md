---
# Source: chapter/chapter-part4.md § 6.3 (criteria 1, 2, 3, 5) and § 6.4 (why they are put in
# writing before work begins).
# FACT-CHECK CORRECTION (critique/FACTCHECK-OTKRYTYE-15.md, incidental finding A, level P1): the
# frame reads "19 percentage points less often," NOT "19% less often." Both source shares stand
# side by side. "19% less often" would describe a different quantity: a relative drop of a fifth,
# instead of a nineteen-point difference between shares.
# Two similar numbers are kept apart BY FRAME and by unit: here it is 19 percentage points of the
# SHARE OF CORRECT CALLS, on the next frame it is 19% of TIME. The unit is named in both lines.
# References to frame numbers for where each criterion was earned are NOT carried into the
# visible body — that would be scaffolding; the addresses stay here, in zarabotano.
# The evening's map: the frame READS it, does not add to it (BRIEF-DEKA §12), see map_read.
id: s92
local_id: "s92"
section: "6. Wrap-up"
type: assertion_visual
title: "Four refusal criteria: when the model is the wrong tool"
assertion: "Each criterion is derived from how the method is built; general cautionary considerations played no part in deriving them, and so not one of them will close with the next model version; all four are stated so they can be checked before work begins — and checking has to happen in advance, because the boundary of applicability cannot be seen from inside the task"
source: "Dell'Acqua et al., \"Navigating the Jagged Technological Frontier,\" SSRN 4573321, 09/18/2023 (field study with Boston Consulting Group)"
chapter_ref: "chapter-part4.md §§ 6.3–6.4"
zarabotano:
  - "exact dimensions — the frame on a generator not replacing a CAD system"
  - "provenance of a detail — the frame on \"RAG for images\" being a category error, and the frame on the revoked camera signature"
  - "object persistence — the frame on the missing object between video frames"
  - "restoration versus plausibility — the frame \"zero invented detail against ninety percent\""
map_read: "the frame reads the evening's finished map, adds no columns. The rows highlighted are \"Hold exact measurements\" and \"Answer who is accountable\": once the fifth column is filled in, both are empty across all four generative modalities, and only recognition answers them — fully for measurements, partially for accountability. The cells are taken from the map as s87 closed it, and are not rewritten here"
media: ""
media_needed: "no photograph: the frame collects four rules, and each one already stood on its own frame with its own illustration; repeating them here would be decoration. The visible content is a four-part scheme where each criterion is broken into three steps: sign of the task, why the method cannot take it, what to use instead of the model"
scheme:
  kind: dorozhki
  caption: "The same breakdown for every criterion: sign of the task → why the method cannot take it → what to use instead"
  steps_arrows: true
  rows:
    - label: "1. Exact dimensions"
      steps:
        - "the requirements carry units, tolerances, materials, kinematics"
        - "none of that exists inside an image: nothing to measure and nothing to check by calculation"
        - "a CAD system"
    - label: "2. Source and citation"
      steps:
        - "the requirements carry \"based on\" or \"with a citation to\""
        - "the contribution of a training example is smeared across billions of weights: no such record exists"
        - "database search, reverse image search, an archive"
    - label: "3. Object persistence"
      steps:
        - "a character, product, or interface must be recognizable throughout a series"
        - "the model has no notion of \"the same one\"; coherence degrades with length"
        - "identity is held outside the model"
    - label: "4. What is needed is already in the record"
      steps:
        - "what is needed is already recorded, but reads poorly"
        - "the model will add what was not there, just as convincingly"
        - "source separation, denoising, super-resolution"
timing_min: 0.7
in_bucket: true
method_steps: ["refusal criteria", "the measurement that requires them"]
form: []
vfy: false
status: собран
---

## Visible slide text



## Speaker notes

This is the core of Wrap-up. The four rules below are derived from how the method worked out in
the previous sections is built; general cautionary considerations played no part in deriving
them. That is exactly why not one of them will close with the next model version: they describe
something that simply does not exist in the mechanism.

First. A generator produces a picture of an object. Inside it there are no units of measurement,
no tolerances, no materials, no kinematics, no construction tree. An image of a part that looks
like it has an M12 metric thread contains pixels that are statistically similar to photographs of
such a thread. From this follow four practical bans, and they are worth holding together in full.
You cannot measure it: there is no scale in the picture. You cannot verify it: the generated
design has not passed a strength calculation or an assembly check, and yet it looks exactly as if
it had. You cannot manufacture it: the output has no geometry a machine tool will accept. You
cannot maintain it: without a construction tree you cannot change a diameter and recompute the
rest. The boundary runs exactly where a picture stops being an illustration and starts being a
data source for the next step: for looks and for presentation material, the generator stays
useful.

Second. A generated frame has no provenance for the detail in it, and that is a property of how
it is built: a provider cannot close that gap. The contribution of every training example is
smeared across billions of weights; saying where this particular texture, this silhouette, this
pose came from is physically impossible, because no such record exists. For a language model, a
similar problem has a known solution — put the source into the context and demand a citation.
Carrying that trick over to images is a category error: denoising is not built to answer a
question about a document, there is nowhere to insert a fact and nothing to quote from. The only
thing that actually works as an analogue is conditioning on a ready-made form: a drawing, a depth
map, a pose, a reference. That is a geometry hint. The sign that triggers this criterion is
simple: the requirements contain the phrase "based on" or "with a citation to." The legal check on
the output follows the same rule: whether it resembles someone else's protected work is decided
by comparison, outside the model.

Third. A model predicts values in the cells of a compressed representation. The notion "this
chair right here is the same chair that was in the previous frame" does not exist in it in any
form: no identifiers, no scene layers, no state that carries over. Consistency is achieved
statistically — a shared starting noise, attention across time, conditioning on a reference — and
is therefore probabilistic and degrades with length. The consequence: any pipeline that needs the
same character, product, or interface across a series of frames must hold identity outside the
model. That is a decision about how the pipeline is built, made once; it cannot be substituted by
tuning settings.

Fourth. If what is needed is already contained in the source, the task is one of extraction, and a
generative model is inapplicable to it by definition: it will add what was not in the record, and
the addition will look exactly as convincing as what was actually extracted. The cleanest example
of this came up in the sound section: from a cassette demo with a voice and piano recorded on one
microphone, a clean vocal was obtained by source separation, with not a single note generated.
The family of tools for extraction — source separation, denoising, restoration, super-resolution —
is built differently and is checked differently.

All four criteria share one property, and it is the reason they were worth writing out
separately: each one is derived from how the method is built, not from cautionary considerations.
That is why not one of them will close with the next model version — only a different class of
method can close them. This is exactly what tells a refusal criterion apart from a mere warning.

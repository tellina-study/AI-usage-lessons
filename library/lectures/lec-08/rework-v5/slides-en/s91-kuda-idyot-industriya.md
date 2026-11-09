---
# Echo of s24 (image models stopped growing; s25 was removed by consolidation, its content
# moved into s24). Echo of the running refrain
# about the tokenizer (s19 · s42; s62 removed 10/29/2026, its content moved into s59a's notes) —
# here the refrain does not sound as the verbatim phrase; the visible layer says "what limits
# quality," the notes hold the full thought. No scientific notation in the visible body: numbers
# in words. "Frontier model" does not go into the visible body — a calque; the frame says
# "leading."
#
# CONSOLIDATION #301 (SVEDENIE-KADROV.md §4, the "merge fragments of one breakdown" method): the
# frame s91a ("Where the industry is heading: rights, world models, and market size") is merged
# BACK here — both frames were physically one and the same piece of work, cut on 10/27/2026 while
# fixing the first render.
#
# THE MARKET-SIZE SPREAD IS RESTORED (PUT-OT-ZAPROSA-K-REZULTATU.md §7, "Rejected: section 6,
# s91a"): the owner rejected the previous round for stripping the 3.16–19.2 billion dollar spread
# from the visible layer to make room for a guest table on a frame whose title promises the
# market. The table is no longer a guest — it has its own frame, `s88a`. The market spread sits
# here as a plate, with the same numbers.
#
# EDIT 10/29/2026 (coordinator, from the rendered snapshot). Two findings:
#   (1) "lever" in the title and in the closing line — a word from internal working
#       correspondence that leaked from the service field `refrain` (the build does not read
#       it). It must not reach the visible layer (CLAUDE.md `slide-form-three-bans`). The title
#       and body are rewritten onto the frame's actual subject — what limits quality, not the
#       abstract "lever"; `refrain` corrected to the exact count (s62 removed — three left).
#   (2) density of 223 words on the visible layer against a limit of 140 — the heaviest frame in
#       the deck. Unloaded: the "rights" and "world models" plates merged into one (4 → 3), each
#       plate's note trimmed to a number with its denominator, the reasoning stayed in the
#       speaker notes in full.
#
# Minutes (0.3) were not changed by this edit — only the form within the budget.
id: s91
local_id: "s91"
section: "6. Wrap-up"
type: analitika
title: "Where the industry is heading: what limits quality, rights, and market size"
assertion: "The forecast is drawn from what is measured: image models stopped growing in compute — quality is limited by the tokenizer, not model size; training on licensed material became a condition of shipping a product; world models separated from video models by producing a space rather than a recording; and four estimates of the size of one market in one year diverge sixfold — meaning the structure of the market can be trusted, its size cannot"
source: "SD3 technical report, 2024 · Stable Diffusion v1 model card · Genie 3, Google DeepMind, August 2025 · independent benchmark WRBench, 23 models, June 2026 (arXiv:2606.20545) · Suno v6 release, 09/09/2026, and ElevenMusic, 04/01/2026 · four industry market reviews for 2026"
refrain: "echo of \"quality is limited by the tokenizer, not model size\" (verbatim phrase — s19 · s42). The third occurrence out of three (s62 removed 10/29/2026)"
echo_of: "s24"
media: ""
media_needed: "no photograph: the frame's subject is the structure of the market, which has no image that would not be decoration or a logo. Checked: Wikimedia Commons, for the named products, yields only brand marks, and a logo is forbidden on a course frame. The visible content is a track of two compute series (image and language models by year) plus three plates"
# DIAGRAM (`scheme:kind:dorozhki`, two rows "image / leading language models")
# REMOVED from the visible layer by consolidation: with four plates the frame ran into [height]
# at −1.92". Its conclusion already sits in plate 1 and its note. The full step-by-step layout
# (16 channels, diffusion transformer, rectified flow, distillation; and the mirrored row for
# language models) lost none of its content — it is entirely in the speaker notes, unabridged.
nauchnaya_zapis: "no scientific notation in the visible body: numbers in words or multiples"
blocks_per_row: 3
blocks:
  - {label: "Image models stopped growing", value: "SD v1 (2022) and SD 3 (2024) — the same number of operations", note: "language-model compute grew 4–5x a year over the same period", key: true}
  - {label: "Rights and modality — settled, not contested", value: "licensing became a condition of the product; world models are a separate class", note: "Suno and ElevenMusic on licensing since 2026; world-model coherence is minutes, not seconds"}
  - {label: "Four market estimates for 2026", value: "$3.16–19.2 billion — a sixfold spread", note: "agreeing only on pace: 14–34% a year", key: true}
timing_min: 0.3
in_bucket: false
method_steps: ["forecast from the measured"]
form: []
vfy: true
status: собран
---

## Visible slide text

**The structure of the market changes slower than version numbers.** Adoption decisions are better checked against it than against a release number.

**Quality is limited by the tokenizer, not model size.** An image model has no cache and cannot have one: denoising rewrites all 4,096 tokens at every single step.

## Speaker notes

Wrap-up's last job is to say where the industry is heading, and to say it so it does not go stale
by the time it is read. There is one condition here: what goes on the frame is the structure of
the market, which changes slower than version numbers. A list of models compiled in October 2026
will be out of date before anyone can check it; five days before the material was due, preview
access to one of the leading video models was shut down. So below are four observations about the
structure, and under each one a measurement.

The first observation is the most unexpected in the whole technical layer of the evening. Image
models have stopped growing in compute. Stable Diffusion v1 in 2022 and Stable Diffusion 3 in
2024 were trained on the same number of operations: a hundred fifty thousand accelerator-hours in
the first case, and the second added nothing to that over two years. Over the same two years,
compute for training leading language models grew four- to fivefold a year. Progress in imaging
came through entirely different means: a sixteen-channel latent representation instead of a
four-channel one, a diffusion transformer instead of a convolutional architecture, rectified flow
instead of a stochastic schedule, distillation of the step count from a thousand down to four.
Architecture and data representation did what language models achieved through compute. This is
also the last utterance of the thought that has run through the whole evening: the main thing
quality depends on is the tokenizer; model size is secondary here.

Next to the first observation stands a measurement whose sign flips between training and running.
Training an image model costs two hundred to four hundred times less than a leading language
model, and at the same time each run of it costs forty to sixty times more. The reason was worked
out in the first section: there is no cache and there cannot be one — denoising rewrites all of
the image's roughly four thousand tokens from scratch at every step, whereas a language model
keeps the context it has already processed and does not return to it. The direct consequence for
anyone thinking of entering this line of development: the barrier to entry for building your own
image model is orders of magnitude lower than for your own language model, and the winner here is
whoever comes up with the better data representation.

The second observation follows from the first, and it is about leadership. Video generation, over
2026, shifted to open weights and Chinese developers, and the loudest Western product in the
industry has shut down — shut down after its own demo reel stopped the construction of an
eight-hundred-million-dollar studio. The economics, stated as a number: at its peak this product
had around a million users at an estimated operating cost of around a million dollars a day, that
is, a dollar per user per day. Video generation was never free for a single second; it was just
not the user paying. The conclusion from this travels anywhere: dependence on someone else's
service is a project risk, and it belongs in the plan alongside the other risks. Two breakdowns in
this lecture are built on a tool that has since shut down.

The third observation is about rights, and it is the most checkable one. Both leading music
platforms have switched to training on licensed material, and their partners are named by name
instead of being described in general terms. No one won the dispute over the provenance of
training data — it became a condition of shipping the product. This is also the most checkable
forecast the lecture can offer: where the rights holder is large and organized — music, film,
news — the question will close by licensing sooner than by court; where the rights holder is
small and scattered — illustration, photography, voice work — there will be no one to close it,
and the current state of affairs will hold there.

The fourth observation is world models as a separate modality. An interactive 3D environment in
real time is generated from a text description, coherence holds for several minutes at a stretch
against ten to twenty seconds for its predecessors, and it is built differently: the next frame is
constructed not only from the description but from the scene's own internal state and the user's
action. On an object left behind by the camera and seen again, the developer showed a demo in
August 2025 where a wall stays painted. An independent June 2026 benchmark across twenty-three
models finds in world models the same limitation as in the video models from the video section:
an object comes back the way it was last seen, not the way it would have become over the elapsed
time — the only difference is the size of the window, minutes instead of seconds. This is not a
refutation of the video section but a confirmation of its own conclusion: persistence is a window
size, not a property of the world. A video model generates a recording. A world model generates a
space you can be inside.

And last, fifth — an inoculation against industry forecasts in general. Four reviews rated the
size of one and the same market in one and the same year, 2026, at three and sixteen-hundredths
billion dollars on one end and nineteen and two-tenths on the other — a sixfold spread, caused
only by where the boundary of the market was drawn. Picking the correct figure among them is
pointless. The one fact they agree on is pace: fourteen to thirty-four percent a year. All four
agree the market is growing fast, and not one knows how big it is. Add to this the industry's most
quoted number — "over fifteen billion generated images" — measured on August 15, 2023, and never
updated since, though it keeps getting cited as current — and you get the full set of habits for
reading industry statistics: check the definition, check the base, check the date.

Three quantities are worth holding together, because none of them changes with a version number.
The right to training material holds for years and changes by court rulings and rights-holder
negotiations. The class of task — does the model generate a recording or generate a space you can
be inside — is a property of how the thing is built, not a setting. The boundary of the market —
what counts as the market — is itself a matter of definition, and that is exactly why four
estimates of the same year, 2026, diverged sixfold: from $3.16 billion to $19.2 billion, agreeing
only on pace — fourteen to thirty-four percent a year.

Hence the practical rule for reading industry forecasts. Market size in them cannot be trusted —
it comes from a definition you never saw. Pace can be trusted a little more carefully: it holds
steady across estimates, meaning it was not invented but counted from the same observed series.
And the most reliable thing in such reviews is the list of what the players themselves consider
the field of competition: it changes slowly and says more about the structure of the industry than
any billion-dollar figure.

And a short note on why this whole frame sits in Wrap-up rather than in a technical section. For
an engineer deciding whether to invest in a direction, a version number says nothing: it changes
every few weeks and promises a breakthrough every time. The structure of the market — who pays,
for what, and what it is limited by — holds for years and predicts what will be available a year
from now far better. That is what is worth reading.

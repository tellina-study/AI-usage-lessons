---
# THE PATH FROM REQUEST TO RESULT (#301, PUT-OT-ZAPROSA-K-REZULTATU.md §7,
# "Rejected: section 6, s91a"): new frame, inserted between s88 and s89.
# The previous round placed this summary table as a GUEST on s91a ("Where the industry is
# heading: rights, world models, and market size") and paid for the space with the market-size
# spread that s91a's own title promised to show — rejected. Here the table has its OWN frame and
# its own title, and the market spread is returned to s91 by consolidation (see the comment
# there).
#
# Slot freed by consolidation #301 (SVEDENIE-KADROV.md §4, the "merge fragments of one
# breakdown" method): s91+s91a are one and the same frame, physically cut on 10/27/2026 for
# height (see their own comments "six plates don't fit"); merged back into s91, see its own
# comment. The new frame's minutes (0.2) are taken from the SAME budget that used to be split
# between s91/s91a (0.3+0.2=0.5): now 0.3 (s91, merged) + 0.2 (this frame) = 0.5. The section
# total (6.0) is untouched, still 10 frames (10 before and after — s91a disappeared, this frame
# took its place in the count).
#
# The table is the BODY of the frame, in GFM `|...|` syntax; the engine draws it the same way it
# does in Lectures 6/7 (`deckkit/tables.py`, `tables.draw_table` via `flow.flow`) — this deck has
# not had a frame of this kind before, but the engine supports the full path, no regression.
#
# The table's numbers are NOT invented here — they are consolidated from the device frames
# accepted as of this minute (s16 — 128×128 latent, 20–50 steps, autoencoder; s41 — eight residual
# quantization codebooks, decoder; s59/s60 — space-time patches, causal autoencoder; the 3D scene
# — Gaussian splatting, 30,000 steps, scene memory (s68a/s71); s83 — patches, 12–32 ViT layers,
# one number on output). Sections 3 and 5, as of the writing of this frame, had not yet set their
# own "path from request to result" frame (the parallel rounds working the same assignment are
# setting it) — the numbers here are taken from the device frames already accepted for those
# sections and may one day need checking if the parallel round gives a different starting
# formulation.
id: s88a
local_id: "s88a"
section: "6. Wrap-up"
type: analitika
title: "The path from request to result: the same figure, five different starts and bottlenecks"
assertion: "The figure, declared empty at the start of the evening, passed through five sections with different content; here — one row per modality: where the work actually starts, instead of noise, and where the method is tightest"
source: "consolidated from the device frames accepted for sections 1–5: s16 · s41 · s59/s60 · s68a/s71 · s83"
chapter_ref: "chapter-part1c.md §1.9 · chapter-part2b.md §2.7 · chapter-part2d.md §3.7 · chapter-part3b.md §§4.11–4.13 · chapter-part3e.md §5.13"
media: ""
media_needed: "no photograph: the frame's subject is five numbers of one and the same figure; an illustration for them would be decoration, of the same kind as the neighboring frames in this section (s90, s91, s92) — Wikimedia Commons and press releases for the named methods yield only logos and diagrams from papers, not photographs"
blocks: []
timing_min: 0.2
in_bucket: false
method_steps: ["consolidation by modality"]
form: []
vfy: false
status: собран
---

## Visible slide text

**The same figure — five different starts, five different bottlenecks.**

| Modality | Start | Bottleneck |
|---|---|---|
| Image | 128×128 latent, 20–50 steps | autoencoder |
| Sound | codec tokens, 8 books | decoder |
| Video | space-time patches | autoencoder |
| 3D | points or views, 30,000 steps | scene memory |
| Recognition | patches, 12–32 layers | one number |

## Speaker notes

At the start of the evening this figure stood empty: request, input, start, a step repeated N
times, output, result — six stations without a single number. Five sections filled it in each in
their own way, and here is not a new breakdown but one row per section: where the work actually
starts and where the method is tightest.

A still image starts from a latent one hundred twenty-eight by one hundred twenty-eight points,
filled with pure noise, and runs through twenty to fifty identical denoising passes; the
bottleneck is the autoencoder, the same module that compresses the image into the latent and then
unfolds it back out again: it is trained once and does not change afterward, whatever model is
placed on top of it.

Sound does not start from noise but from codec tokens: the first codebook is decided by
autoregression, the following seven refine it; the bottleneck is not the generator but the
codec's own decoder: the frame rate and the depth of the cascade set a ceiling on quality before
the model on top ever gets a chance to work.

Video starts from space-time patches — the same idea as for a still image, only with the added
dimension of time; the bottleneck is again the autoencoder, and again it is the one that decides
both how much training costs and how much attention between frames costs.

A 3D scene does not start from noise at all: the start is a point cloud or calibrated shots, and
the step repeats not twenty to fifty but thirty thousand times, because there is no shared
trained prior here and every object learns from scratch; the bottleneck is memory: a scene made of
Gaussians takes up two orders of magnitude more space than the shots it was assembled from.

Recognition runs the figure in reverse: the start is patches of the same image, the step is the
same attention blocks, twelve to thirty-two layers, and the output is not an image but one number
— a score, not a result that can be shown to anyone else.

Five different starts, five different bottlenecks, and the one thing they share is this: the
mechanics inside — the same attention blocks and the same training of a network to predict the
next approximation — and what differs is only where it starts and where it is tightest. This is
the answer to the question the figure held empty the whole evening.

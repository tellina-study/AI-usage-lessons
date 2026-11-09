---
id: s16
section: "1. Still Image"
type: schema_matrix
title: "There Are Two Families of Generation, and Each Generator Is Built from Parts Trained Separately"
assertion: "The boundary between the families runs along \"building up piece by piece\" versus \"editing the whole thing many times over.\" Inside either family, from the description string to the output file, three independently trained models are at work — the diffusion network is only the middle one of them, and its ceiling is set by its neighbors"
source: "Ho, Jain, Abbeel, «Denoising Diffusion Probabilistic Models», 2020 · Sohl-Dickstein et al., 2015 · Rombach et al., 2021 · the SD3 technical report, 2024 · Imagen, 2022"
chapter_ref: "chapter-part1c.md §1.9.6 and §1.9.8 — the autoencoder as a tokenizer, and the text encoder as someone else's model inside the generator"
arhitektura:
  blocks:
    - head: "Text encoder"
      role: "input · someone else's model"
      lines:
        - "a frozen model reads the description — SD3 has three, FLUX.1 has two"
        - "scaling up the encoder gives more than scaling up the network"
    - head: "Denoising network"
      role: "the work"
      lines:
        - "latent 128×128×16, 1–50 passes"
        - "the description is unchanged on every step; there's no history"
    - head: "Autoencoder"
      role: "output · bottleneck"
      uzkoe: true
      lines:
        - "the decoder unfolds the latent into 1024×1024"
        - "25.12 dB on 4 channels against 28.62 on 16"
matrix:
  columns: ["What it predicts", "How many passes", "What it can do in principle", "What it can't do in principle"]
  rows:
    - label: "Autoregression"
      cells:
        - "the next token — a probability distribution over a vocabulary of ~200k"
        - "however long the output is: 1000 tokens — 1000 passes"
        - "arbitrary output length, an exact probability for every step, a guaranteed format at decoding time"
        - "fixing what's already written: a token in context becomes a condition for every one that follows"
    - label: "Denoising"
      cells:
        - "noise (or the original image, or velocity) — a vector of the same shape as the input"
        - "whatever the sampler sets, from 1 to 50, independent of output size"
        - "global coherence: at every step the network sees the whole object and can rearrange the composition"
        - "giving the probability of a specific picture — hence no logits, no temperature, no masking"
blocks:
  - {label: "Why there are exactly two families", value: "piece by piece — or the whole thing, many times over", note: "not discreteness versus continuity: image autoregression (GPT-Image, Nano Banana) has discrete tokens too", key: true}
media: ""
media_needed: "the architecture diagram is drawn with the core's own primitives and comes out vector-based; a raster insert here would be worse"
timing_min: 1.0
in_bucket: false
status: собран
---

## Visible slide text

**Two families: autoregression builds up piece by piece, denoising edits the whole object at once, but many times over.**

**From the description to the file, three independently trained models are at work** — the diffusion network is only the middle one of them.

## Speaker notes

The course has already taken apart the first family. The model decomposes the probability of a
sequence into a product of conditionals: every next token is predicted from everything before
it. To get a thousand tokens, you need a thousand sequential passes of the network. What this
family does well: arbitrary output length, an exact conditional probability at every step (hence
logits, temperature, and a guaranteed output format), and natural causality. What it fundamentally
can't do — fix what's already written: a token that lands in the context becomes a condition for
everything that follows. And the price: the number of steps equals the output length — for a raw
1024×1024 image that's 3,145,728 numbers, and no pixel-by-pixel autoregression survives at that
length.

The second family is built differently: instead of "write one thing at a time," you start from
pure noise and clean it up a little, a few dozen times, editing the whole object each time.
Autoregression builds up the object piece by piece; denoising edits the whole object at once, but
many times over. It's good at global coherence and at parallelism within a step; what it
fundamentally can't do is produce the probability of this specific picture — it has no exact
likelihood, which means no logits, no temperature, no masking. You can't stop halfway through:
half the steps give you a blurry picture, not half a picture. The price of the second family is
built as a mirror image of the first: the number of steps doesn't depend on the output size, it's
set by the sampler — it was 1000 in 2020, it's become 20–50 in practice, and 1–4 in distilled
models.

Why there are exactly two families, not three and not one. The split isn't by modality — not
"text is discrete, images are continuous" — but by generation strategy. Text has always had a
vocabulary, because text is already split into a finite set of tokens. But an image can be
described with a discrete vocabulary too, and that's not an experiment that loses on detail — it's
how the two most widely used commercial tools work as of late 2026: since March 25, 2025, the
GPT-4o generation built into ChatGPT has been autoregressive over a discrete vocabulary of image
tokens — unlike DALL·E, which ran on diffusion; since August 2025, Gemini 2.5 Flash Image, "Nano
Banana," has gone the same way. Everything this and the following technical slides take apart from
here on is the architecture of the diffusion-and-flow family: Stable Diffusion, SD3, FLUX, Imagen.
The image-token autoregressive family does have a vocabulary, and the price for it isn't zero:
the step count is counted not in pixels but in image tokens — hundreds or thousands instead of the
twenty to fifty parallel steps of diffusion — and access is only through a closed inference API.
The boundary blurs in a third direction too: denoising has come to text (diffusion language
models, a young direction), and in between lives rectified flow, which formally isn't diffusion
anymore, and which the industry has moved to almost entirely over the last two years.

The formulation worth carrying away: the boundary between the families runs along "building up
piece by piece" versus "editing the whole thing many times over." Both strategies apply to both
modalities; the choice is made by whichever is more expensive in the task — length or number of
passes.

From here, the technical block takes apart the diffusion-and-flow family piece by piece: the two
families are already named, then the forward and reverse process, the latent patch, conditioning,
architectures, adapters. This slide exists so you can see right away how they come together into
one picture — from the description string on the input to the file on the output.

The path begins even before the diffusion network. The verbal description doesn't reach it at
all: first a separate text model reads it — frozen, trained by someone else, earlier. SD3 has
three such text encoders, FLUX.1 has two. Structurally this means: part of the generator's
quality doesn't belong to you, it came bundled with someone else's model. The measurement here is
direct and uncomfortable for intuition — scaling up the text encoder gives a bigger quality gain
than scaling up the diffusion network itself. The largest of them, T5-XXL, pays for exactly two
things: long, complex instructions and text inside the picture.

Next comes what's usually called the "model." The work runs in the latent — a compressed
representation of the picture sized 128×128×16, that is, 262,144 numbers; the denoising network
never sees the 3,145,728 raster points the picture actually has. The latent's starting content is
pure noise from a pseudorandom number generator; it's this, not "temperature," that's responsible
for how different the pictures come out from one description. The description stands still the
whole time: it's a condition, the same on the first pass and the last. There's no history, no
accumulation, no place "next to the question" — and from this grows everything the section says
further on about the impossibility of feeding a source of truth into generation.

The output — the third part. The latent gets unfolded into raster points by the decoder of the
same autoencoder that defined the latent in the first place. This, too, is a separately trained
model, and it has a measured ceiling: reconstruction on a four-channel latent gives 25.12 dB
against 28.62 dB on a sixteen-channel one. Even if the denoising network performs perfectly, the
picture still passes through the decoder, and whatever it blurred doesn't come back. Letters — a
high-frequency structure — suffer first; that's why the question "why are there pseudo-letters in
the picture" is settled by the choice of autoencoder, and no amount of prompt tweaking can fix it.

The main thing worth carrying away: the pipeline is built from parts trained separately. From
this follows that the parts get swapped out individually — the same autoencoder lives under
different diffusion networks; that strange behavior at the seams between parts is a systemic
property of this kind of assembly, and fixing it in your own integration is pointless; and a
practical rule of choice — before asking how big the model is, ask what its autoencoder is and
what its text encoder is. The main lever is the tokenizer; model size is secondary here.

And what's completely absent from this picture. No vocabulary — neither on the denoising
network's input nor on its output: there, it's continuous vectors throughout. No normalization
and no probability: there's simply nothing to ask the network "how confident are you" with. No
key-value cache: on every pass, all the latent's tokens change at once. No variable output
length: the picture's size is fixed before the run starts. Each of these absences turns, further
on in the section, into a concrete limitation of the tool, and none of them will disappear in the
next version of the model: all four follow from the architecture drawn out in full on this slide.

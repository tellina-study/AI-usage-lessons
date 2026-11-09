---
id: s24
section: "1. Still Image"
type: analitika
title: "Language Model versus Media Model: Architecture, Control — and Cheaper to Train, More Expensive to Run"
assertion: "Eleven lines of divergence in architecture and control, and at the end — a numerical reversal: training an image model is 200–400 times cheaper than training a frontier language model, while every one of its runs is 40–60 times hungrier. For image-token autoregression (since 2025), five of the first table's six lines read differently"
source: "OpenAI, Addendum to GPT-4o System Card, 25.03.2025 · Gemini 2.5 Flash Image, 2025 · the SD3 technical report, 2024 · the Stable Diffusion v1 model card · independent compute trackers for frontier models"
chapter_ref: "PLAN-02 §5 — the composition of the eleven lines; chapter-part1c.md §1.10 — caching and the boundary with autoregression. The densest technical slide of the lecture: if height runs short, shorten the cell wording, don't drop rows — the composition is set by the plan"
density_warning: "the densest technical slide of the lecture"
nauchnaya_zapis: "no scientific notation in the visible body: numbers are spelled out"
blocks:
  - {label: "The image model stopped growing", value: "SD v1 (2022) = SD3 (2024)", note: "stated in their own paper", key: true}
  - {label: "Transparency worse than language models", value: "2 of 5: SD v1, SD3", note: "SDXL, FLUX.1, DALL·E 3 — not disclosed"}
media: ""
timing_min: 1.4
in_bucket: false
status: собран
---

## Visible slide text

| | Language Model | Media Model (denoising / flow) |
|---|---|---|
| **Data unit** | token, vocabulary ~200k | patch vector, continuous; **no vocabulary** |
| **Cache** | works on an unchanging context | **impossible**: 4096 tokens — every step |
| **What controls the output** | temperature, masking — **a guaranteed form** | CFG, adapters — **no guarantees** |
| **Provenance** | with retrieval — a citation **exists** | for a generated frame — **none, and there can't be** |

*The table has 11 rows; seven are in the speaker notes.*

**Cheaper to train:** 150,000 GPU-hours against ≈57 million. **More expensive to run:** $120 per million image tokens against $12 for text — the same model.

## Speaker notes

The technical block's summary table rests on a term the course has already introduced for
language models, and shows what it turns into in a media model, or why it disappears by
construction — a disappearance always shows the mechanism, while a transformation can be
mistaken for a mere change of name. The right column is about diffusion and flow: Stable
Diffusion, SD3, FLUX, Imagen.

The first row is the data unit, and almost everything else follows from it. For a language
model that's a token: an identifier from a vocabulary of around 200k positions, fixed before
training. For a media model the unit is a latent patch: a 2×2 block of latent cells at 16
channels, 64 numbers, a continuous vector. There's no vocabulary at all: nothing to mask, nothing
to forbid.

The second — how many of these units there are: for a language model it's set by the length of
the prompt plus the answer, within a window of 128k to 1 million; for a media model, by the size
of the output, known before the run starts: 1024×1024 is exactly 4096 tokens, a parameter, not a
variable.

The third — exactly what's being predicted: for a language model, a probability distribution
over the entire vocabulary, summing to one, with a measure of confidence. For a media model, a
vector of the same shape as the input. There's no normalization, no probability: there's nothing
to look at, and not because the vendor doesn't show it, but because the quantity doesn't exist.

The fourth — the role of context: for a language model, the history grows and serves as the
condition for the next token. For diffusion and flow, the description is a constant condition,
unchanged across all fifty steps; there's no history at all. The difference looks minor until you
get to the question of where to feed in a source of truth: there's no place "next to the
question" here.

The fifth — the number of passes: N for N tokens in a language model; for a media model, whatever
the sampler sets, from one to fifty, independent of the output size.

The sixth — caching, and it's underrated more than the rest. For a language model, keys and
values are cacheable as long as they belong to an unchanging context — hence the asymmetry
between prefill and generation, and caching tariffs. For diffusion and flow, none of this
economics survives: denoising rewrites all 4096 tokens at once on every step, and there's no
unchanging context here. This directly explains why one picture costs as much as thousands of
tokens of text: for a language model, every next token gets cheaper thanks to the cache; for
diffusion and flow, every next step costs exactly as much as the first.

The seventh — what controls the output. The course showed a mechanism that really is a
constraint: schema grammar masks invalid tokens, and an invalid format physically can't be
generated. Media models don't have a single lever like this: CFG, negative prompts, and adapters
all work on a continuous vector that has no distribution, and these are requests, not
constraints — the check stays outside the model, in the pipeline.

The eighth — hallucination, and the difference lies in the nature of the error. For a language
model it's a content error, checked against a source. For a media model it's a plausible
impossibility (six fingers, a reflection with no source, a thread with no pitch), checked against
physics and geometry. The ninth — how it's fixed: feeding a source into context and demanding a
citation works for a language model and doesn't work for any image-generation architecture — for
denoising there's no context at all; for autoregression there is one, but no image token gets
checked against an external fact on the output.

The tenth and eleventh are short but expensive. Output length is variable for a language model
and is decided by a stop token; for a media model it's fixed before the run starts, and there's
no stopping early. Provenance: an answer with document retrieval has a citation to a document; a
generated frame has none and can't have one, because every training example's contribution is
smeared across billions of weights.

And the boundary without which eleven rows turn into dogma. Since 2025 there's also another,
widely used family — autoregression over discrete image tokens: GPT-Image, the GPT-4o generation
built into ChatGPT since March 25, 2025 (OpenAI itself calls it autoregressive, unlike the
diffusion-based DALL·E), and Gemini 2.5 Flash Image since August 2025. For it, five of the first
six rows diverge: there is a vocabulary and it's discrete; a distribution over that vocabulary is
predicted; the context grows by the same mechanism as a language model's; the number of passes
equals the number of image tokens; the cache works exactly like a language model's, and the
expense comes from the number of sequential tokens per frame, hundreds to thousands against
twenty to fifty parallel diffusion steps. Only the second row doesn't change: how many tokens
will be in the frame is decided in advance by the image size, not by a stop token. The classes of
error, meanwhile, are fixed differently, and for a media model aren't fixed internally at all:
anatomy and counting — by pose conditioning or regeneration; physics and light — not fixed at
all; text — by inserting it as a layer outside the generator; technical impossibility — by the
conclusion "the generator isn't the right tool."

Now the economic reversal, and for this audience it's counterintuitive. The four rows above and
the three below point in opposite directions: training an image model is 200–400 times cheaper
than training a frontier language model — and every run of it is 40–60 times hungrier.

On top: training compute for SD v1 — 5·10²² operations; for frontier language models — 420 to
7,600 times more. GPU-hours: 150,000 against ≈57 million for GPT-4 and 30.8 million for Llama 3.1
405B. Money: $0.6 million in rental against $78.4 million and $191.4 million. Weight size: 4.27
GB against ≈810 GB.

On the bottom, everything is the opposite: 5.5 petaflops per picture against 0.14 petaflops per
1000 tokens of text; 2,907 kWh per 1000 generations against 0,047 per 1000 answers; $120 per
million image tokens against $12 per million text tokens, from the SAME model — it prices its
own picture output ten times higher itself. Where the factor of forty comes from can be worked
out in a minute: 4096 image tokens plus 512 text tokens = 4608; one pass is ≈0.11 petaflops; 50
sampler steps give ≈5.5 petaflops; a language model's answer at 1000 tokens with 70 billion
parameters is ≈0.14 petaflops; the ratio is ≈39. For a distilled model at 4 steps — 0.44
petaflops, the ratio drops to 3. The conclusion: "why is a picture expensive" is, by an order of
magnitude, more a question of the number of steps than of model size.

And this slide's own observation: image models have stopped growing. SD v1 in 2022 and SD3 in
2024 spent the same number of operations on training — stated outright in their own paper. Over
the same two years, frontier language models' compute grew 4–5 times a year, and amortized cost
2.4 times a year since 2016. The gap is widening not because pictures are getting cheaper, but
because language models are getting more expensive; the visible consequence on the market is
that there are only a handful of frontier base language models, while there are dozens of
serious base image and video generators, including fully open ones. This is arithmetic, not
generosity.

Transparency here is worse than for language models, even with open weights: of the five image
models the lecture counts training for, the numbers are disclosed for only two — SD v1 and SD3;
for SDXL, FLUX.1, and DALL·E 3, neither GPU-hours, nor cost, nor compute volume are disclosed.
"Open model" and "transparent model" are different properties.

The block's engineering conclusion: for media models, almost all the total cost of ownership sits
in running them; for frontier language models, historically, it sits in training them. From this
comes a different product economics: some give away their weights and sell access and compute,
others protect their weights, because what's invested in them can't be repeated in 150,000
GPU-hours. And an applied rule: for generative media, forecasting the load matters more than
choosing the model — an error in choosing the model costs percentage points, an error in
estimating the number of generations costs orders of magnitude.

---
id: s20
section: "1. Still Image"
type: comparison
title: "The Description Is a Constant Condition on Every Step. And CFG Is Not Temperature"
assertion: "There, the context grows with every token. Here, the condition stays motionless from the first step to the last — the same Q/K/V mechanism, it's just that the query and the keys-and-values come from different places. And the classifier-free guidance (CFG) scale isn't like temperature on any of four essential points"
source: "U-Net cross-attention · MMDiT joint attention, SD3, 2024 · Imagen, 2022 · Ho and Salimans, «Classifier-Free Diffusion Guidance», 2022 · Sadat et al., 2024"
grafa_note: "the one place in the deck where a contrastive construction in the title is justified: the false parallel is exactly the subject of the slide's second half"
scheme:
  arrows: false
  rows:
    - label: "U-Net, SD 1.x–SDXL"
      steps: ["Q ← image latent", "K, V ← description tokens", "map 4,096 × 77 words", "it can be drawn out"]
    - label: "MMDiT, SD3 and FLUX"
      steps: ["text and image together", "attention in both directions", "map 4,608 × 4,608", "the text looks at the image"]
columns:
  title: "CFG — four differences from temperature"
  left:
    head: "Temperature"
    items:
      - "The model's opinion: doesn't change it — a divisor of the logits"
      - "Direction: higher → more randomness"
      - "Cost: zero — one division"
      - "Randomness: in the sampler, on every step"
  right:
    head: "CFG"
    items:
      - "The model's opinion: changes it, pushes past what was predicted"
      - "Direction: higher → LESS diversity"
      - "Cost: two network passes per step"
      - "Randomness: has nothing to do with it — it's in the starting noise"
blocks: []
media: ""
timing_min: 1.1
in_bucket: false
status: собран
---

## Visible slide text

**The same Q/K/V mechanism — the query and the keys come from different places.**

**CFG is not temperature.**

## Speaker notes

Denoising by itself generates something from the distribution of the training data. For it to
generate what was requested, you need a conditioning mechanism, and it's built differently from
what experience with a language model would suggest. The description doesn't reach the diffusion
network directly: a separate, frozen text model processes it first, and the generator only sees
that model's output — a sequence of vectors. SD3 has four such parts: the autoencoder plus three
text encoders, and on top of them the diffusion network itself. The generations differ in which
encoders they use: the first SD uses a contrastive model with 123 million parameters, a 77-token
window; SDXL uses two of those; SD3 uses three, including a large language model; FLUX.1 uses
two, with the language one giving per-token representations of up to 512 tokens.

Why the industry moved away from contrastive encoders to ordinary language ones: a contrastive
model encodes what a picture is about well, and encodes syntax, word order, and negation poorly.
In 2022, it was shown for the first time: scaling up the text encoder gives a bigger quality gain
than scaling up the diffusion network itself. The measured consequence in practical terms: SD3's
authors checked what happens if the largest encoder is removed — it matters for complex
descriptions and text inside the picture, while for most descriptions removing it keeps
competitive quality. For an engineer, this means directly: 4.5 billion parameters in memory, and
if the task doesn't require long descriptions and lettering, you don't have to load it.

Now the conditioning mechanism itself. In the U-Net generation, text vectors act through
cross-attention — the same mechanism the course has already taken apart, except that here the
query and the keys-and-values come from different places. The query comes from the image
latent — "this area is asking: what am I?" The key and value come from the description's tokens.
"Q about the current step, K and V about the context" turns here into "Q about the picture, K and
V about the text." The attention map comes out rectangular: 4,096 picture regions against 77
words of description, and it can literally be drawn out, showing which regions lit up for the
word "cat." In the transformer generation there's no more cross-attention: text and image tokens
get glued into one sequence and run through joint attention. The map becomes square — 4,608 by
the same on SD3 — and the text "sees" the picture the same way the picture sees the text; this is
how they solved the "mustard writing on a bun" problem, where the earlier one-directional input
fell short.

The remaining conditioning channels are built on the same principle: an image as a condition —
start from a noised original; a mask — noise is mixed in only inside it; a structural
condition — a depth map, edges, a pose; a style or face reference — "a description, but as a
picture." The general principle: any conditioning in this family is adding one more set of
vectors into attention, or one more term into the noise prediction. There isn't a single hard
constraint among them — and from this comes a direct path to the question the audience asks
itself, and gets wrong: doesn't the guidance scale (CFG) do the same thing as temperature in a
language model?

The parallel is wrong at its core, and it has to be taken apart rather than just mentioned,
because left unexamined it operates as knowledge and leads to wrong decisions. First — where the
analogy does work: both parameters are the only "creativity knob" at run time, neither one changes
the weights or adds knowledge, both have a working range beyond which the output degrades, and
both are properties of the inference procedure. Four matches are enough to make the parallel look
convincing. Now, four differences. The first and load-bearing one: what the parameter does to the
model's "opinion." Temperature is a divisor of the logits — the ranking of candidates never
changes. CFG changes the prediction itself: it extrapolates past what the network actually
produced, and at a scale of seven the resulting vector sits somewhere the model predicted nothing
at all. Second — direction: raising temperature gives more randomness, raising CFG gives less
diversity and stricter adherence to the description — the opposite. Third — cost: zero for
temperature, two network passes per step for CFG. Fourth — where the randomness sits: in a
language model, in the sampler, on every step; here, in the starting noise, and CFG has nothing
to do with randomness.

How this works internally. During training, the model is taught conditional and unconditional
generation at once: ≈10% of descriptions are replaced with an empty string. At run time, the
network is called twice — with the description and without — the difference is taken, and the
step moves in that direction by a scale factor. Typical values: early models 7–8, SDXL 5–8, SD3
4–5, FLUX.1 3.5. The cost is stated outright: two passes instead of one, generation with CFG is
twice as expensive; hence distilled models bake the effect into the weights and call the network
once — their "direction" slider behaves differently from the classical one: it's a number fed in
as a feature, not an extrapolation multiplier.

What breaks at a high scale factor — and there's a mechanism behind this, not folklore. As the
scale factor rises, the variance of the predicted noise moves outside the statistics the
autoencoder was trained on: the decoder can't correctly reconstruct amplitudes like that. In the
picture this shows up as blown-out highlights, acid-saturated color, "plastic" texture, a
collapsed composition, and dropping diversity. A practical rule: CFG isn't a quality slider, it's
the force with which you push the output past the boundary of what the model considers
plausible. A negative prompt works by the same formula, substituting a prediction conditioned on
different text for the unconditional prediction; it doesn't forbid anything — there's no
equivalent of logit masking here, and there can't be — and it's free in compute terms, because
the second pass was being done anyway; in models with distilled conditioning there's no second
pass, and there it either doesn't work or requires switching on real CFG and paying double — a
frequent source of confusion when moving between model generations.

---
id: s26
section: "1. Still Image"
type: assertion_visual
title: "What the Method Can't Do — and One Property, Read from Two Sides"
assertion: "Three failures, with different causes. Text is the price of the same compression that delivered the cheap attempt: the win and the failure came from the same place. Counting and consistency have a different cause — it holds even with a vocabulary"
source: "the SD3 technical report, 2024 (the reconstruction-quality table) · GenEval, GenEval-2 (2026, arXiv:2512.16853), GenOlympiad (2026, arXiv:2610.26850), T2I-CompBench++"
chapter_ref: "chapter-part1c.md — the three failures and their mechanism"
scheme:
  arrows: true
  rows:
    - label: "Letters"
      steps: ["48x compression", "blurred before the generator", "pseudo-letters"]
    - label: "Counting"
      steps: ["no unit for an object", "\"three\" — an attention weight", "nothing to count with"]
blocks:
  - {label: "Failure 1 — text", value: "3.5 dB — the line between pseudo-letters and legible text", note: "25.12 dB on 4 channels against 28.62 on 16; without the encoder, long text and complex descriptions degrade", key: true}
  - {label: "Failure 2 — counting", value: "GPT-4o 0.85 against ≈0.99 presence; the best 2026 model — 23.9 of 100", note: "holds even with a vocabulary; the word \"three\" is an attention weight, not a counter"}
  - {label: "Failure 3 — consistency", value: "doesn't exist for diffusion; better for autoregression, not solved", note: "diffusion: no history. Autoregression: growing context, drift over long runs"}
  - {label: "One property — two sides", value: "gave: ×48 compression → a 6–8 GB card, $0,034–0.05 per attempt", note: "took: a letter blurs BEFORE generation, a background face is a handful of latent cells", key: true}
media: ""
media_needed: "a genuine DALL·E 3 output with pseudo-glyphs (assets/screenshots/s26a-psevdobukvy.jpg, Wikimedia Commons) — acquired, but the slide has nowhere to put it alongside a diagram plus four plates"
timing_min: 1.0
in_bucket: true
status: собран
---

## Visible slide text

**Three failures.** Text is the price of the compression that delivered the cheap attempt; counting and consistency hold even with a vocabulary. **The win and the failure come from the same place.**

## Speaker notes

This slide's three failures are engineering properties of the method, not complaints against
it. Each follows from the architecture the technical block took apart, and none of them will
close with the next version of the model, because the cause lies in how the task is framed. This
has to be kept distinct from temporary defects: "the model still draws hands badly" and "the
model has no notion of an object" are statements of a different kind, and the second one isn't
fixed by training.

The first failure — text inside the image — has two independent causes. The first is the
autoencoder: a letter is a high-frequency structure, and 48x compression blurs it before a
generative network ever touches the image; the measured loss is 25.12 dB on the four-channel
latent against 28.62 dB on the sixteen-channel one, and that 3.5 decibels is exactly the
difference between pseudo-letters and legible text. The second cause is the text encoder: one
trained contrastively encodes what a picture is about well, and encodes an exact sequence of
characters poorly; removing the large language model from the input degrades exactly two classes
of task — complex, detailed descriptions and long letter-by-letter text. By 2024–2026 the
problem is eased by sixteen latent channels, a larger text encoder, and joint attention, but not
closed: long strings, small point sizes, non-Latin scripts, and Cyrillic remain unreliable. The
engineering rule that follows from this: lettering in production materials isn't generated — it's
laid on as a separate layer, in a real typeface, outside the generator. This is a case where the
right answer sounds like "the model isn't needed here": vector text over a raster background
solves the task precisely, cheaply, editably, and with a guarantee, and only this first method
never has an unsuccessful attempt.

The second failure — counting objects and spatial relations — is a measured, reproducible
failure, not an anecdote about six fingers. Specialized benchmark suites break counting out as
its own category precisely because the results there are systematically worse than everywhere
else, and this holds even where the model has a vocabulary: for GPT-4o, autoregressive over
discrete tokens, the GenEval counting score is 0.85 against nearly 0.99 for its own object
presence, and on GenOlympiad 2026 the best model of the moment scores only 23.9 out of 100 on the
counting axis specifically. So vocabulary discreteness isn't the cause that fixes or sustains
counting. The cause lies in what the network predicts: the model doesn't count objects — it
predicts numbers in latent cells, or an attention weight on a vocabulary position. The word
"three" in a description is a token that influences the distribution of attention weights, not a
counter. There's no notion of a discrete object in the mechanism, in any form. And it's fixed the
same way "letter blindness" in language models is — by an external check: a detector counted, the
number didn't match, regenerate. No architecture fixes this with a counting skill, because
there's nothing to count with.

The third failure — and here the families genuinely diverge. For diffusion there's no notion of
an object at all; "this chair is the same chair" between two generations doesn't exist:
consistency is achieved statistically — through shared starting noise, a face reference, an
adapter — and it degrades as the series gets longer. For the autoregressive family over image
tokens (since 2025), there's a real, growing history in a shared token stream, and independent
evaluations show noticeably better character consistency — better, not solved: drift over long
runs is documented here too, the window of stability is just wider. Any pipeline that needs the
same character, product, or interface across a series of frames has to hold identity outside the
model — for both families, with a different safety margin.

And now — one property, read from two sides, not one more failure on the list. The limitations
above are usually read as flaws the next model version will close. For letters and background
faces that's wrong in a checkable way: both follow from the exact property that delivered the
win, and you can't close them without undoing the win. The property is 48x compression, which
turned 3,145,728 numbers into 4096 tokens. What it gave: one and a half orders of magnitude of
compute saved on each of dozens of steps, hence generation on a 6–8 GB card in August 2022, open
weights as a working tool, an attempt price of $0,034–0.05 against $50–150 for a commission. What
it took: a letter blurs before generation even happens; a background face occupies a handful of
latent cells — there's nothing left in it to reconstruct; regular small textures "boil," thin
long structures tear apart during decoding. Counting objects isn't on this list: it stays the
weakest composition category even for architectures with no compression into a continuous latent
at all, with a genuine discrete vocabulary — there, the cause is different and deeper, and it's
fixed neither by a larger autoencoder nor by a vocabulary.

From this follows a tool-selection rule that carries far beyond image generation: don't ask "can
the tool do such-and-such," ask "what exactly did it compress to become cheap." The answer to
the second question predicts failures that aren't in the documentation yet, while the answer to
the first goes stale with every release. When an overview says "the new version has finally
learned to draw text," it's worth asking at what cost: the usual answer is a larger autoencoder,
that is, less compression, that is, more compute on every step. The limitation hasn't
disappeared — the quality was bought with exactly the quantity whose savings made the method
cheap in the first place.

The rule also has a flip side, or it reads as advice not to use the tool at all. Compression
throws away high frequencies and fine detail — and that's exactly why generation works great
where composition, color, mood, and overall shape matter, that is, at the stage where the look is
still being searched for. The failures and the win are distributed across production stages, not
across model quality: at the look-search stage, the property works for you; at the release of
finished material, it works against you. Knowing the boundary removes the choice between "use it"
and "don't use it": the tool gets placed by stage, and that's an engineering answer, not an
extreme.

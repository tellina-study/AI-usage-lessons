---
id: s15
section: "1. Still Image"
type: assertion_visual
title: "Four Observations, Each with a Number"
assertion: "Open weights don't equal adoption, access from Russia comes with a markup embedded in the exchange rate, two domestic services grant opposite rights to the exact same result, and legal cleanliness is sold with no numbers behind it at all"
source: "Hugging Face API, 30-day downloads, queried 27.10.2026 · Kandinsky and Shedevrum user agreements · foundation-models.api.cloud.ru and Cloud.ru's pricing document, revision 23.10.2026 · Adobe's indemnification terms"
blocks:
  - {label: "30-day downloads", value: "461 vs 622,299", note: "Kandinsky 6.0 Pro vs FLUX.1-dev; SDXL — 4,282,392, Wan 2.2 — 3,901"}
  - {label: "Speech and text from the same team", value: "FRIDA 597,351 · GigaAM v3 426,500", note: "three orders of magnitude more than the same country's image models get"}
  - {label: "Markup on the exchange rate", value: "196.42 ₽/$ against 80.49 at the Central Bank", note: "the 2.44× gap matched to the second decimal digit across nine models"}
  - {label: "Numbers on being \"legally clean\"", value: "zero", note: "no market share, no attempt counts, no savings, no outcomes", key: true}
columns: {}
media: "assets/charts/s15-skachivaniya.png"
media_note: "a QuickChart bar chart built from the numbers in the first two plates: six 30-day download counts on one logarithmic scale. In gold — 461; paired in the same color — the Russian speech and text models"
layout_note: "each row carries an observation, not a product name. A list of names is a bibliography; its place is in the reading materials"
timing_min: 1.3
in_bucket: false
status: собран
---

## Visible slide text

**Two Russian services grant opposite rights to one result.** One hands the rights to the user, the other keeps them for itself. "Allowed" or "not allowed" is decided by the user agreement.

## Speaker notes

Four mentions, each with a number. A mention without a number is never put up this evening: a
list of product names is a bibliography, and its place is in the reading materials, not on the
slide in front of the room.

The first observation is about the gap between open weights and real-world adoption. A direct
query to the API of the platform hosting open models, on October 27, 2026, for 30-day
downloads: the Russian image model has four hundred and sixty-one downloads, the European
FLUX.1-dev has six hundred twenty-two thousand two hundred ninety-nine. For scale, the same
measurement gives SDXL four million two hundred eighty-two thousand, and the Chinese video model
three thousand nine hundred and one.

The correction has to be made in both directions. In the Russian model's favor: its weights are
split across nine official repositories, summing to around four thousand seven hundred, and
together with community-made quantized builds — around fifteen thousand; so the gap isn't a
thousandfold one, it's roughly fortyfold. Against it: all seventy-nine of the lab's repositories
together give seventy-seven thousand downloads, but seventy thousand of those are utility
encoders that get pulled in by other people's pipelines, while the actual generative models are
counted in the hundreds. This can't be read as a quality measurement — it's a measurement of
adoption: how many engineers in the world took the weights and ran them themselves. Three honest
reasons for the gap: thousands of fine-tuned variants and guides have grown up around the foreign
models; three years on the market against one month; and a Russian-language advantage costs an
English-speaking developer nothing, and English-speaking developers make up the bulk of the
downloads.

The second observation flips the first one's conclusion, and that's exactly why it's here.
FRIDA's text embeddings — five hundred ninety-seven thousand downloads for the same month, speech
recognition — four hundred twenty-six thousand, against four hundred sixty-one for the image
model and two hundred twenty for the flagship text model with seven hundred two billion
parameters. Russian open models for the Russian language and Russian speech are in demand three
orders of magnitude more than Russian open models for images. The reason is substantive: Russian
speech recognition has a task nobody else is solving, while images don't have such a task — a
foreign model draws from a Russian-language description just as well. An open model lives where
it closes an unmet need, and that rule carries over to any project deciding whether to release
its weights.

The third observation is about money, and it's counted precisely from two primary sources.
Russia's largest cloud provider resells twenty-seven models from one foreign vendor, nine from
another, and nine from a third — exactly the ones whose vendors refused to serve Russia. The
official dollar price list is converted at an internal rate of 196.42 ₽/$ against 80.49 at the
Central Bank, and the 2.44× multiplier matches to the second decimal digit across nine models at
once. In money terms: a million input plus a million output tokens cost 1,449 ₽ directly against
3,536 ₽ through the intermediary — an overpayment of 2,087 ₽. A caveat: the multiplier doesn't
apply to the Russian, Chinese, and open models this same cloud hosts itself — there, the pricing
is its own and often low. 2.44× is the price of reaching a model that doesn't want to serve you,
and computation has almost nothing to do with it.

The fourth observation is about rights to the result, and it's a practical one. Two Russian
services grant opposite rights to an outwardly identical product: one hands exclusive rights to
the user, keeping for itself an irrevocable non-exclusive license; the other keeps the rights for
itself, leaving the user only personal non-commercial use, with any commercial use requiring
prior approval. For a student planning to release something, that's the difference between
"allowed" and "not allowed," and it's legible only in the user agreement, not in the interface
and not in the advertising.

And the last one — it's here as a mention precisely because there are no numbers for it. There's
exactly one major model that its vendor sells as legally clean: trained on its own library and
public-domain material, and the company indemnifies corporate clients against infringement
claims. The product logic is clear and appealing. There isn't a single checkable number behind
it — no market share, no generation count, no savings for the client, no court outcomes. So data
provenance as a marketable property is named here but doesn't become a detailed case, and the
reason is named out loud.

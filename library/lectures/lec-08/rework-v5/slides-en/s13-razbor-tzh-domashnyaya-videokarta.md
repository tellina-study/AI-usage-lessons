---
id: s13
section: "1. Still Image"
type: analitika
title: "Case: T—Zh Trained Its Own Model on a Home GPU"
grafa: "column b — the classical mode is named, and it has no number of its own"
adres_osi: "SELECTION"
assertion: "The entry threshold dropped to what a student physically has on hand: a laptop, forty pictures, an hour and a half. Selection moved to the right — thirty to a hundred generations and half an hour of review per usable illustration"
source: "\"Tinkoff Journal,\" \"How We Used Neural Networks in Advertising,\" March 20, 2023 — https://t-j.ru/marketing-ai/"
blocks_per_row: 3
method_steps:
  - "① the price of both errors"
  - "② classical mode — named, not counted"
  - "③ the model next to it"
  - "④ how it's built"
  - "⑤ what moved to the right"
blocks:
  - {label: "Fine-tuning", value: "1.5 hrs on an RTX 3080 (16 GB, laptop)", note: "40 images on top of the base model"}
  - {label: "Output", value: "46 posters in February", note: "before that — 23 visualizations"}
  - {label: "Selection", value: "30–100 generations, ≈0.5 hr per illustration", note: "12 different models tried"}
  - {label: "Hit rate", value: "2/3 of banners — wrong click-through rate", note: "the best performed 2–3× better than average", key: true}
  - {label: "Classical baseline", value: "not published", note: "a designer is named; no price or turnaround given"}
columns: {}
media: "assets/screenshots/s13-tj-oblozhka.png"
media_note: "the cover of the very publication being broken down — that is, one of the samples the editorial team generated itself, not a third-party illustration of the case. Tier 1, the primary source's og:image. There's no source caption on the slide; provenance is in images-log.md. Only the image is used on the slide, its headline is stripped off: the \"five times\" figure from the headline doesn't enter the breakdown and wasn't checked"
timing_min: 1.3
in_bucket: false
status: собран
---

## Visible slide text

*Payment address: SELECTION.*

**Dropped before the breakdown.** An industry overview credits the editorial team with abandoning stock photos for Kandinsky; in fact it's Midjourney and Stable Diffusion, and the subject is banners.

## Speaker notes

This Russian case is more useful for an engineering audience than the others in the section, for
one reason: the primary source names the hardware, the time, and the dataset size — everything
you need to reproduce it. The publication is "Tinkoff Journal," March 20, 2023.

We have to start with a dropped claim, and it was dropped by directly reading the primary source.
An industry overview claims the editorial team dropped stock photos entirely in favor of
Kandinsky. The publication itself has neither an abandonment of stock photos nor Kandinsky: it
names Midjourney and Stable Diffusion, and the subject is ad banners, not illustrations for
articles. The overview's claim can't be used. It's worth spelling out the usual mechanics of
industry retellings, because you'll run into it constantly: a secondary source compresses a case
down to a memorable formula, the formula spreads across dozens of publications, and one person in
a hundred checks it. The habit of opening the primary source before quoting it saves not your
reputation here, but your time — because a retelling usually loses exactly the details that made
the case interesting in the first place.

Step one — the price of both errors, and this is a rare case where both are named in the same
unit, and named by the team itself. Two-thirds of the banners failed to hit the needed
click-through rate. The best banner turned out two to three times more effective than average.
Conversion held at twenty-five to thirty percent. The unit is the hit rate. This is exactly where
the previous case takes the price of its second error from — the "we didn't try the variant that
would have worked" one: if the best is two to three times better than average, then every
unreviewed variant is a missed multiplier, and now it's measured, not just stated in words.

Step two — and here the case runs into a wall that has to be named out loud, not walked around.
The mode is named and not counted. The publication names the classical mode by name — "a designer
for every task" — but there's neither a cost nor a turnaround time for one banner from a designer
before the model in it. The publication doesn't name a second classical mode, buying stock for a
stream of banners, at all. What exactly would need to be found for the comparison to become
complete: the designer's internal rate and the turnaround on one ad banner at a Russian media
outlet in 2022–2023. The closest available anchor is the same pricing page, where an ad banner
starts at five hundred rubles, but there's no direct measurement for this editorial team, and you
can't substitute someone else's number into an empty spot. The gap is named, not filled in.

Step three — the model. Twenty-three visualizations for the first launched course, then
forty-six unique posters in February. One final illustration takes thirty to a hundred generated
images and about half an hour. Twelve different models were tried.

Step four — how it's built, and this is exactly why the case was chosen. On the input: a text
description plus a set of forty images for fine-tuning. On the output: a raster ad banner. The
main model is Stable Diffusion plus specialized ones; the hardware is named outright: a laptop
with an RTX 3080 at sixteen gigabytes, fine-tuning took an hour and a half. Trained on the team's
own set of forty images on top of a publicly available base model. What the publication doesn't
have: exactly which method was used for fine-tuning — an adapter, textual inversion, or full model
fine-tuning. An hour and a half on one gaming card is, by order of magnitude, consistent
specifically with an adapter, but that's our own inference, not a fact from the publication, and
it has to be presented that way.

Separately, about the people, because it changes how the case reads. A targeting specialist
selects one illustration out of thirty to a hundred and finishes it. The feedback loop is closed:
the banner's click-through rate comes back to the same person who picks the next one. The team
consists of a senior targeting specialist, a targeting specialist, an editor, and a designer. The
word "engineer" doesn't appear in the source at all, and it can't be inserted there: fine-tuning a
model on a home GPU was done here by people whose job titles don't say "developer."

Step five — what moved to the right. The entry threshold moved to what a student physically has:
a laptop, forty pictures, an hour and a half. Selection moved to the right — thirty to a hundred
generations and half an hour of review per usable illustration, and two-thirds of the output is
still a miss on the target metric anyway. This is the same form as in the global cases, just
measured in units instead of metaphors. And this is exactly where the evening's content shows
through, presented in the cheapest possible way: the win doesn't come from the model getting it
right on the first try — it comes from the price of one failed attempt dropping to zero, which is
why there are now a hundred attempts.

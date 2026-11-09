---
id: s12
section: "1. Still Image"
type: analitika
title: "Case: The Collapse of the Per-Image Unit Price"
grafa: "column a — both classical modes are counted in the same unit as the model"
adres_osi: "SELECTION"
assertion: "It's not the picture that got cheaper. The failed attempt got cheaper — and that's exactly why the unit of account becomes what went to the client, not what was generated. Within the classics alone, the spread is already fifty to two hundred times — the choice of baseline decides any future count"
source: "ai.google.dev/gemini-api/docs/pricing (read 27.10.2026) · profi.ru, 3,848 Moscow illustrator profiles · stock agency price lists · Toys «R» Us Studios × Native Foreign, June 2024"
blocks_per_row: 3
method_steps:
  - "① the price of both errors"
  - "② both classical modes in the same unit"
  - "③ the model next to them"
  - "④ how it's built"
  - "⑤ what moved to the right"
polosy:
  unit: "dollars per image · logarithmic scale"
  scale: log
  klassika_name: "Classical mode"
  model_name: "Generation"
  rows:
    - label: "Freelancer"
      klassika: {value: 100, text: "$50–150"}
      model: {value: 0.042, text: "$0,034–0.05"}
      mnozhitel: "×1000–4500"
    - label: "Stock, retail"
      klassika: {value: 300, text: "$130–499"}
      model: {value: 0.042, text: "$0,034–0.05"}
      mnozhitel: "×14700"
    - label: "Stock, wholesale"
      klassika: {value: 2.5, text: "≈$2.50"}
      model: {value: 0.042, text: "$0,034–0.05"}
      mnozhitel: "×73"
blocks: []
media: "assets/screenshots/s12-toys-r-us-sora-kadr.jpg"
media_note: "a frame from the Toys «R» Us Studios × Native Foreign brand film, June 2024 — the only case all evening where the ratio of generations to a usable result is stated publicly. Acquired via tier 1: the official press release's og:image. Provenance — assets/screenshots/s12-toys-r-us-sora-kadr.url"
timing_min: 1.9
in_bucket: false
status: собран
---

## Visible slide text

*Payment address: SELECTION.*

**The price of the error.** "Didn't fit" — $50–150; the missed variant has no number. **Moved to the right:** we count what went to the client, not what was generated.

## Speaker notes

The first of the section's three cases, and it has the most complete form: both classical modes
are counted in the same unit as the model. There aren't many cases like this all evening, and
it's worth noticing when they come up. The payment address is selection: all the cheapness of
generation immediately creates work in choosing a usable frame, and the rest of the case counts
exactly that.

Step one — the price of both errors. In the classical mode, the price of the "we commissioned it
and it didn't fit" error is stated outright: one assignment to a freelancer — $50–150 and 1–3
days, in Russia starting at 3,860 ₽. The price of the opposite error — "we didn't try the variant
that would have worked" — is never given a number in any of the global-market sources. It's
important to acknowledge this rather than fill it in with an estimate: this second error is
exactly the subject of the whole evening, and the fact that almost nobody counts it is itself
meaningful. A measured value for it does appear in this section after all, but from a different
source — from the editorial team's material, taken apart in the next slide, with an explicit note
of where it's from.

Step two — both classical modes, counted in the same price. Commissioned work: $50–150 per
assignment with a 1–3 day turnaround, an hourly rate of $49.65 from the thousand-profile
analysis, in Russia starting at 3,860 ₽ from the sample of 3,848 profiles. Ready-made from a
library: $130–499 retail, ≈$2.50 wholesale by subscription, 2000s-era microstock at $0.25–1. The
unit is the same for all of them: a dollar per image. One assumption has to be said out loud,
because without it the count isn't honest: "per assignment" is being equated with "per image,"
even though a freelancer's assignment often includes revisions and several angles; accounting for
that would narrow the gap — by how much exactly, open sources can't say.

And right here — the other half of the classical mode, which breaks down from the inside, with no
participation from generative models at all. A retail license for one image costs $130–499; by
subscription, wholesale, the same image costs ≈$2.50. This is one product, one vendor, one price
list — and the gap between the two lines in it runs fifty to two hundred times. That gap isn't an
anomaly: retail is bought one-off, for a specific piece of material, when you need exactly this
picture today; wholesale is bought as a stream, for a stream of tasks. Different buyers, different
contracts. From this comes a practical rule worth carrying away before any industry overview: on
hearing "a thousand times cheaper," ask not about generation but about exactly which classical
baseline was used. The question is short and filters out most of the loud comparisons — in them
the baseline is either not named at all, or named with a generic word like "stock image," behind
which hide two rates differing by two orders of magnitude. When building your own count, the rule
works in reverse too: name the baseline first, not "cheaper by such-and-such a multiple" — without
a named baseline, a number doesn't survive the first question.

Step three — the model. A 1024×1024 image through Google's programmatic access costs $0,0336, at
double resolution — $0.05, at quadruple — $0,113. Midjourney's base subscription and Adobe
Firefly's base plan both come out to roughly five cents each. Against commissioned work that's a
gap of 1,000–4,500 times, against stock retail — up to 14,700, against wholesale — 73. Three
different baselines give three different numbers, and all three have to be named together:
otherwise the choice of baseline makes the conclusion for the listener.

One separate line here matters more than all three before it. Running inference yourself on a
rented GPU: SDXL on an RTX 4090, rented at $0.89 an hour at ≈2.6 seconds per image, comes to
$0.64 per thousand images — against $33.60 for the same thousand through programmatic access,
that is, 30–50 times cheaper. And this cheapness has three named prices, none of which makes it
into any price list. The first — the weights license: the best of the cheap models is distributed
non-commercially, the open alternatives are weaker. The second — keeping the card fully loaded: a
card rented for an hour and sitting idle for forty minutes still costs the same $0.89, and at a
hundred images an hour that comes to $8.90 per thousand — more expensive than some tariffs. The
third — the engineer, who appears in none of the calculations.

Step four — how it's built. On the input: a text description plus optional reference images and
adapters. On the output: a raster image of a set size, with the size fixed before the run starts,
and no stopping early. What the model was trained on is disclosed only for the open ones: the
first version of Stable Diffusion — on 2.32 billion image-text pairs, 150,000 A100-hours. For the
closed models, the composition of the training set isn't disclosed — that's a property of the
market, not a gap in the research. And an honest gap: how a user's edit feeds back into a closed
model's training couldn't be determined by direct search.

Step five — what moved to the right. Time moved from execution to selection and finishing: the
price of a single attempt dropped to zero, the price of choosing didn't. From this comes a rule
carried out of this case that keeps working the rest of the evening: the unit of account is what
went to the client, not what was generated. Any savings counted off the price list for generation
is inflated by exactly the selection ratio. And nobody but you is going to measure that ratio for
your task: public measurements of how many generations it takes to get one usable frame
essentially don't exist in the open. The one defensible ratio is hundreds of shots against the
few dozen that made it into a one-minute spot (the Toys «R» Us Studios × Native Foreign frame).
Everything else that circulates in industry overviews posing as that ratio turns out, on
inspection, to be material from sites selling generation, with no methodology and no sample.

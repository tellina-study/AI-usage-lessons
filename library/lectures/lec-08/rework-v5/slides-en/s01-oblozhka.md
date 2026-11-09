---
id: s01
section: "0. Entry"
type: hero_cover
title: "Lecture 8. AI in Creative Industries and Media"
assertion: "An industry where the economics of a single unit of output flipped in three years, and the tool that did it"
source: ""
blocks: []
scheme: {}
columns: {}
media: "assets/screenshots/s01-coca-cola-ai-kadr.png"
media_note: "a real frame from a generated Coca-Cola holiday ad (2024 release, Silverside AI studio); the truck's trailer shows a generation error — the logo reads \"Coca-Coola\". Public domain. There is no source caption on the frame; provenance is in images-log.md and assets/screenshots/s01-coca-cola-ai-kadr.url"
media_fill: "≥40% of the frame area, preferably full-width background with text on top"
timing_min: 0.5
in_bucket: false
status: собран
---

## Visible slide text

**8**

**AI in Creative Industries and Media**

Image · sound · video · 3D · recognition · wrap-up

## Speaker notes

This frame is not a drawing and not a collage. It is a real frame from Coca-Cola's holiday
advertising spot, assembled entirely by generative models. The snow on the fender, the garlands
in the fir branches, the reflection of fire in the red paint — all of it is generated, not shot.
And the same frame shows the very thing it is here for: the lettering on the truck's trailer
reads "Coca-Coola." The logo that the corporation has guarded for a hundred years and defends in
courts around the world is spelled wrong in the released spot, and the origin of that error is
machine.

The whole lecture fits into this one frame. An image generator produces a convincing surface —
light, texture, snow, mood — and exactly where it is required to be precise about a letter, it
breaks. The reason is not carelessness at the studio, and not that the model was "undertrained."
The reason is in how the method is built, and this lecture will take it down to the mechanism: a
letter is a high-frequency structure, and the generator does not work with image pixels but with
a compressed representation in which thin lines blur before the generative network even touches
the picture. In taking this mechanism apart, we will also understand why the same method so
cheaply produces hundreds of variants — because it is one and the same property, read from two
sides.

The subject of the lecture is creative production: advertising and marketing materials, film and
series, music and sound, games, publishing, media. The tool is a family of models built on
iterative denoising: the model starts from pure random noise and, over a few dozen passes, turns
it into an image, a sound, or a video frame. Between the subject and the tool stands a claim that
the lecture checks against the material rather than asks you to take on faith: in 2022, what got
cheaper was the defective attempt, while the product of creative production stayed at its own
price. A first approximation of an idea came to cost a fraction of a cent, and the whole measured
gain of the industry comes from exactly that, not from the model making any single frame better
than a human would.

The evening is built from three layers, and they run interleaved, not in blocks. The first is
capability: what became possible for the first time, with numbers on both sides. The second is
technical mechanism: how these models work inside, at the same depth the course used to take
large language models apart, and always with parallels and differences drawn out. This is not a
bolted-on "how it works" section: denoising, starting noise, and batch generation are exactly
the mechanism that made a failed attempt free, so the mechanism here answers the question "why
did this suddenly become possible." The third layer is price: what the gain is paid for, in
money, rights, extra workload, and risk. The price always stands as the second half of a pair on
the same frame where the gain is named. The pair reads as "gave — demanded," and that pair is the
content of the lecture.

The six lines at the bottom of the frame are the order of the evening, and that order is built by
the price of a unit of output. The still image comes first, because its unit is the cheapest of
all by two to three orders of magnitude: the practice there is the most mature, numbers exist on
both sides of the ledger, and this is exactly the modality where it makes sense to take the
mechanism apart to the depth it requires. Further on, the price of a unit grows by orders of
magnitude from section to section, and along with it grows the share of tasks the model does not
close. By the time we reach the 3D scene, the mechanism will be excellent, yet there will not be
a single case anywhere in open sources with both sides of the ledger counted — and that will be
said out loud, not papered over with a similar-looking number borrowed from a neighboring field.

One last thing worth knowing about this frame before moving on. The spot went to air. Nobody
recalled it, nobody reshot the scene, the error in the logo stayed in the released material. This
is the new economics, presented in a single image: when a trial costs a fraction of a cent,
trials number in the thousands, and the bottleneck stops being the ability to make a frame — the
bottleneck becomes the ability to look at it and notice what it actually says.

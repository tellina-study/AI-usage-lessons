---
id: s63a
local_id: "s63a"
section: "3. Moving Image"
type: analitika
title: "Where Consistency Breaks Down, by the Developers' Own Admission"
assertion: "Error accumulation is named in three independent papers, and most precisely as exposure bias; object permanence in interactive mode turns out to be the size of a window, and this can be checked before launch with one question: is there an object in the clip that the viewer is required to recognize as the same one across two different shots"
source: "the Sora technical report; CogVideoX; papers on exposure bias"
chapter_ref: "chapter-part2d.md §3.8"
media: ""
media_needed: "visual content — a band of plates with quotes from the developers; a photograph explains nothing here"
scheme:
  caption: "object permanence in interactive mode is the size of a window, and it is not a property of the world"
  rows:
    - label: "Exposure bias"
      arrows: true
      steps:
        - "During training, the true context is on the input"
        - "At inference, the model's own imperfect output is on the input"
        - "Error accumulates from frame to frame"
blocks:
  - {label: "What the developers themselves admit", value: "'inaccurately models the physics of many interactions'", note: "+ eating food, inconsistencies in long samples, spontaneous appearances of objects"}
  - {label: "Error accumulation — across three papers", value: "exposure bias", note: "trained on the true context, but run at inference on their own imperfect outputs"}
  - {label: "Permanence is a window size", value: "it's the size of a window, not a property of the world", note: "'memory ~a minute' = 'the cache evicts old frames'", key: true}
  - {label: "The advice that carries over", value: "start with a frame, put the description second", note: "half the uncertainty disappears with one real frame"}
timing_min: 0.7
in_bucket: true
timing_note: "split off from s63 by body height: 1.5 -> 0.8 (s63) + 0.7 (s63a). Section 3's total did not change"
status: собран
---

## Visible slide text

## Speaker notes

Where this breaks down is admitted by the developers themselves, and quoting them is more reliable than quoting critics. From the same report that praises the model: it inaccurately models the physics of many basic interactions, such as glass shattering; other interactions, such as eating food, don't always produce correct changes of object state; the report lists inconsistencies that develop in long samples and spontaneous appearances of objects.

Error accumulation is named in three independent papers, each under its own name. First: error accumulation in autoregressive generation. Second, more precisely: exposure bias — models trained on the true context are forced, at inference, to generate sequences conditioned on their own imperfect outputs. Third, called drift-prevention methods. The mechanism is one and the same: each next frame is built from the previous one, and the previous one is already slightly wrong, so the error compounds on itself. The fix is training on the model's own outputs — that is, forcing the model, during training, to work in the same mode it will work in afterward.

And an observation that strips the romance off the notion of a "world model": object permanence in interactive mode is the size of a window; there's no property of the world behind it. Two statements about the same fact: one system has visual memory reaching back about a minute; another has past frames in a sliding cache, with older frames evicted. The first is said in the language of a product, the second in the language of an engineer. It's the same limitation.

What this means for tasks where the same thing in two shots matters. If a product requires an object, a person, or an interface to look identical across different frames — a logo on packaging, an actor's face, a car model — the model does not guarantee this under any settings, and it has to be secured from the outside: by locking in the look with reference frames before generation, by having a person check every shot, by editing so that the contested object never lands in two consecutive shots. The industry's working answer has already taken shape as a product: a model released on 10/15/2026 accepts up to ten reference frames and up to fifteen references per generation — a direct answer to exactly this problem, and the fact that it was needed confirms that the problem itself isn't solved.

And a criterion you can check before launch rather than after delivery. Ask whether your clip contains an object the viewer is required to recognize as the same one across two different shots. If it does — build selection and manual verification into the budget; if it doesn't — the limitation costs you nothing.

It's worth noticing what kind of evidence this is. All four statements on the slide are the developers' own words, taken from the same report and the same papers where the models are praised. This is a different class of evidence than a critic's breakdown: a maker listing its own failures has no interest in exaggerating them, and the list comes out short, specific, and checkable. The habit of looking for exactly this kind of language — a "limitations" section in a model card, a paragraph on failure modes in a report — saves weeks: it usually says exactly what you'll trip over in week two.

And one last thing to take from this slide. Two statements about the same limitation — "visual memory of about a minute" and "past frames in a sliding cache, with older ones evicted" — differ only in their audience. The first is written for a user and sounds like a property of the model; the second is written for an engineer and sounds like the size of a buffer. When the product phrasing and the engineering one diverge this much, trust the engineering one: it tells you what happens once the window runs out, while the product phrasing passes over that moment in silence.

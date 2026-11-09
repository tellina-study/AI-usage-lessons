---
id: s14
section: "1. Still Image"
type: analitika
title: "Case: Airbus's Bionic Partition — the Win Isn't from a Trained Model"
assertion: "Remove the trained model from the loop mentally and see what's left. Here, almost everything is left: a search against a physical criterion, a calculation, printing — and the entire forty-five percent mass win. The selection condition fails, and that's the content of the case, not a flaw in it"
source: "Autodesk News, «Autodesk and Airbus: generative design in the aerospace factory», 2016 — https://adsknews.autodesk.com/en/news/autodesk-airbus-generative-design-aerospace-factory/"
blocks_per_row: 3
chapter_ref: "chapter-part1b.md — the section's third case and its fifth step, the selection condition"
method_steps:
  - "① the price of both errors"
  - "② classical mode — one; a second doesn't exist, the reason is named"
  - "③ the model next to it — and here the case flips over"
  - "④ how it's built"
  - "⑤ what moved — the selection condition"
blocks:
  - {label: "Before: calculated partition", value: "65 kg", note: "the only alternative: the criterion is set by physics"}
  - {label: "After: geometry from a bone-growth model", value: "35 kg", note: "−45% mass; Scalmalloy alloy, the largest cabin part at the time"}
  - {label: "The price of the error — in the industry's own unit", value: "up to 465,000 tonnes of CO₂ a year", note: "Airbus's estimate for the whole A320 order book: every extra kg in the cabin is fuel for the aircraft's whole service life"}
  - {label: "The selection condition: remove the model mentally", value: "nothing disappears — the search, the calculation, the printing all remain", note: "there was no model in the loop; in the T—Zh case, without the model there are no 46 posters left — there the condition passes", key: true}
media: ""
media_needed: "the A320 bionic partition in a cabin mock-up (assets/screenshots/s14-airbus-peregorodka.jpg, tier 1, Autodesk's og:image) — acquired, but the slide has nowhere to put it alongside four plates"
timing_min: 1.3
in_bucket: true
status: собран
---

## Visible slide text

**The criterion is set by physics: hold the load at minimum mass. There's exactly one alternative, and it's counted in the same unit.**

## Speaker notes

The section's third case stands as a counterpoint, and the failure of the selection condition in
it is the content, not a flaw. The condition is simple and applies to every case all evening: the
change has to be caused specifically by a trained model, and this is checked with one mental
move — remove the model and see what's left.

Step one — the price of the error, named in engineering terms and in the unit the industry itself
counts it in. An extra kilogram in an aircraft cabin is fuel for the machine's entire service
life. Airbus's estimate, if the approach were rolled out across the A320 order book, is up to
465,000 tonnes of CO₂ a year. This is the baseline everything else has to be read against: the
mass savings here aren't aesthetic or a marketing point — they translate directly into fuel and
emissions.

Step two — the classical modes, and this is where the case differs from the section's two
previous cases. There's no second mode in this task, and the reason is named: the selection
criterion here is set by physics. The partition has to hold the load at minimum mass — a
checkable condition; for any variant you can say in a second whether it's met or violated. So
there's exactly one alternative: ordinary calculation and design of the partition, counted in the
same unit: 65 kg against 35, that is, −45% mass. "A second mode doesn't exist" is a full verdict,
not a gap in the research: a gap says we didn't find something, a verdict says there's nothing to
find.

Step three — and here the case flips over. There's no trained model in the loop at all.
Autodesk's Project Dreamcatcher searched through tens of thousands of geometry variants against a
given model of bone cell growth. This is optimization against a set criterion: the algorithm
generates variants, computes an objective function for each, and discards the worst ones. There's
no training on data, no weights, no learned distribution here, in any form whatsoever. So why
does this case belong in the lecture: it circulates in industry overviews as an example of
"artificial intelligence designed an aircraft part and made it 45% lighter," and that's an error
of exactly the class this whole evening takes apart. Attributing a win to a trained model where
classical optimization actually produced it leads to the wrong decision in your own project:
someone who believes an overview like that will spend months on a tool that isn't needed for this
task, instead of taking a solver that computes strength.

Step four — how it's built. On the input: loads, boundary conditions, and an objective function.
On the output: a part's geometry, printed on a metal printer from Scalmalloy alloy — at the time,
the largest printed cabin part on an aircraft. Trained on nothing — there's no training in the
loop at all. It's also worth noting the opposite: generative design didn't become any weaker for
this. It really did deliver 45% mass, and delivered it by means an engineer can verify by
calculation — and it's exactly this checkability that makes the case a convenient template for
how to read any industry overview.

Step five — the selection condition, applied literally. It separates cases where the model
changed something from cases where it simply showed up in the retelling. Let's check it on the
partition: remove the trained model — the criterion-based search stays, the strength calculation
stays, the alloy printing stays, the 45% mass win stays. Nothing disappears along with the model,
because there was no model in the loop. The condition fails. Now let's check it on the section's
neighboring case, where the editorial team fine-tuned a model on forty pictures: remove the
model — forty pictures and a laptop remain, but the forty-six unique posters in February don't.
The condition passes, and the case counts — even though its classical side isn't counted. A third
class, the most common one in industry overviews and not represented in this comparison, is cases
where there was no model at all, and the words "artificial intelligence" only appeared in the
retelling.

What moved to the right, and why this case belongs specifically in the section on images. What
moved is the selection criterion. Where the criterion is set by physics, no dispute about
authorship arises at all: nobody asks who owns the partition, because the answer "the one that
weighs 35 kg and passes the calculation" satisfies everyone. The dispute shows up exactly where
the criterion is a matter of taste — and the entire rest of the evening is exactly about that:
concept art, illustration, key frame, voice, face, music track — in every one of these tasks
there's no checkable predicate you can use to say "this variant is the correct one." That's why a
human does the selecting there, that's why it costs money, and that's why the authorship dispute
isn't closed by a technical argument.

From this comes a skill the course values above knowing specific tools: before attributing a win
to a trained model, remove it mentally from the loop and see what's left. The habit is cheap — a
minute, with no system access and no conversation with the vendor — and it filters out exactly the
share of industry overviews that wrong decisions about your own project get built on. The typical
objection — "but generative design is also called generative." It is, and the confusion isn't
accidental: one word, different classes of tools. Telling them apart is simple: ask what the tool
was trained on; if the answer is "nothing, it computes" — you're looking at optimization. The
second objection — "what difference does it make if the result was achieved": the difference
shows up when you try to repeat the result in another project. Optimization transfers by rule
(describe the criterion — it will work the same way), a trained model transfers by data (without
a set resembling the training set, the result doesn't reproduce). Of the section's three detailed
cases, the selection condition passes one and a half: the editorial team's case passes in full,
the per-unit price collapse case passes on the model and doesn't pass on completeness of the
count, the partition doesn't pass at all — and that proportion is an honest picture of the
industry today, not a defect in the sample.

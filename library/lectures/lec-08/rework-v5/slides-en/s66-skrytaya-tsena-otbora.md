---
id: s66
local_id: "s66"
section: "3. Moving Image"
type: analitika
title: "The Hidden Cost of Selection"
assertion: "A price list names the cost of one attempt; production cares about the cost of one usable result, and between them sits a selection coefficient that the price list doesn't mention in a single word: the short film's own creators named their estimate as 300 to 1, against a baseline of 'tens to one' in documentary and about ten to one in scripted advertising; in the one place in the public record where the ratio of generations to usable output is disclosed by a primary source with the studio's and director's names attached, hundreds of iterative shots collapsed down to a couple dozen for a 66-second ad — and this number cannot be carried over to other campaigns"
source: "'Air Head,' April 2024; Toys 'R' Us, June 2024"
chapter_ref: "chapter-part2d.md §3.9"
media: ""
media_needed: "visual content — a band of three attempt-to-usable ratios against the classical modes' baseline, with a cumulative map below it; frames from both ads are copyrighted and absent from free repositories"
voronka:
  vhod: {value: "300", text: "units of source material per one frame that made the cut — 'Air Head,' 2024"}
  vyhod: {value: "1", text: "frame that made the cut"}
  yarusy:
    - {head: "The classical mode — the baseline", text: "tens-to-one in documentary, about ten in advertising"}
    - {head: "Selection — the bottleneck", text: "the model increased selection by an order to an order-and-a-half against what it imitates"}
blocks_per_row: 3
blocks:
  - {label: "Toys 'R' Us, June 2024", value: "hundreds of iterative shots → a couple dozen", note: "for a 66-second ad — named by a primary source, with the studio's and director's names attached", key: true}
timing_min: 1.0
timing_note: "1.5 -> 1.0 + 0.5 (s66a): a band of five plates asks for 3.93\" at a 5.36\" body; the cumulative map needs another 2.65\". Section 3's total did not change"
in_bucket: true
status: собран
---

## Visible slide text

## Speaker notes

A second thing you pay for that isn't in the price list. The price list names the cost of one attempt; production cares about the cost of one usable result.

Two named measurements, taken from the producers' own interviews, and one prohibition.

"Air Head," April 2024: the creators' own estimate — 300 to 1 for the ratio of source material to what made the cut. Without a baseline this number doesn't read, so the baseline is named alongside it: in classical documentary, the ratio of footage shot to footage released runs in the tens-to-one; in scripted advertising, about ten-to-one. That means the model didn't invent selection — it increased it by an order to an order-and-a-half against the mode it imitates. A correction to the usual story: selection always existed and always cost human time; what changed is how much material there is to sift through.

Toys "R" Us, June 2024: hundreds of iterative shots compressed down to a couple dozen for a 66-second ad. This is the one defensible generations-to-usable ratio anywhere in the public record: it's named by a primary source, with the studio's and director's names attached. That's exactly why it can't be carried over to other campaigns — for the campaign with seventy thousand clips, the share that made it in is disclosed nowhere, and plugging this ratio in there would mean inventing a number and passing it off as measured.

And the prohibition. The stock figures of "three generations per usable frame" and "six to twelve generations per one successful one" are not used in this lecture: they come from the marketing materials of sites that sell generation, and they carry neither methodology nor a sample. The two measurements above are a different class of evidence, and the difference is fundamental. The thing worth taking away is exactly this distinction: a number named by whoever sells the tool, and a number named by whoever used the tool and reported the result, are different kinds of information, and they must not be mixed even when they happen to agree.

From this comes a rule that holds for all three modalities broken down so far: the unit of account is what shipped to the client. Any savings calculation based on the price list for generation is inflated by exactly the selection coefficient, and nobody but you is going to measure that coefficient for your task. In practice this means: before planning savings, run a small series and count how many attempts it took to get one usable result, specifically for your task, specifically against your requirements for the result.

The industry's working answer to this cost also exists and has already taken shape as a product. The main source of waste is a character's inconsistency between shots, so the lever on the selection coefficient is known too — lock in the look before generation: first the character and a set of references are fixed, then the shots are generated. A model released 10/15/2026 accepts up to ten reference frames and up to fifteen references per generation — this is the product's direct answer to exactly this problem.

What carries over into your own work. The selection coefficient is measured only on your own task and only with your own series: someone else's ratio, even one honestly named by a primary source, describes someone else's requirements for the result. A series of twenty to thirty generations held to the same requirements the client will actually impose gives you your own number in half a day — and it's that number, not the price list, that belongs in the budget. The same trick works in the other direction too: if a series comes back worse than a comparable published case, the difference usually sits in how strictly "usable" was defined, and only after that in the model.

And finally, on why selection is named a hidden cost rather than just a cost. In nobody's budget does it sit on its own line: price lists count generations, contractors count days, and the time spent viewing hundreds of clips dissolves into the word "post-production." The line only appears once someone puts it there by hand, and putting it there is part of the engineering work, not the bookkeeping.

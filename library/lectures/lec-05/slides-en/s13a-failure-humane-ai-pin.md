---
id: s13a
type: case_study
section: "Section 1. Discovery"
duration_min: 2
assertion: "A device conceived as a replacement for the phone sold about 10,000 units against the company's own target of 100,000; revenue of $9 million against $230 million raised, more returns than purchases between May and August 2024, and the service shut down 10.5 months after sales opened"
learning_goal: "On-point failure #2: the user-research phase itself failed — the question \"compared with what\" was closed after the build; the short account of the case reads off the slide without the lecturer"
learning_outcomes: [LO1, LO2, LO6]
chapter_ref: "§1.10, §1.1, §1.4"
in_bucket: true
interaction: none
protected: true
verify_day_of: false
note: >
  issue #212, owner remark R1-2026-10-01: "a medical model's errors inside customer
  development? the problem there was the training set, not user research — replace it".
  The IBM Watson for Oncology case is taken off this slide: its root cause is training data,
  and in the user-research phase it was standing in the wrong place. In its place goes a
  case where the user-research phase itself is what failed: the product was built on an
  assumption about a person that was never checked with that person. The decision on Watson:
  it stays in the chapter (§1.9, Case A) and does not return to a slide — the failure class
  "the plausible taken for the real" has already been shown twice on screen in Section 1
  (s10 — fabricated citations in a report, s12 — a panel of AI personas), and a third
  appearance repeats the lesson. If Watson is wanted on a slide, its place is Section 4
  next to s34 (benchmark against reality); the Section 4 slides are being edited by another
  session. The Google Glass counterfactual supplies the alternative the course rule requires:
  the same class of device, after the user was changed, delivered a measured gain. The new
  text is written without the contrastive "not X, but Y" construction
  (tools/editorial/README.md §1). The decision on Watson has been carried out (2026-10-01):
  it stayed in the chapter as §1.9, and the Pin got a §1.10 of its own, "On-point failure #4:
  Humane AI Pin" — the `[for-slide-s13a]` anchor sits there, and all 56 slides of the deck
  now have an anchor in the chapter.
meme_or_visual: >
  case_study: at the top a labelled band "WHAT HAPPENED" — the account of the case itself,
  so that the slide reads without the lecturer. Below it two equal cards: on the left "What
  the numbers showed" (Lucide trending-down icon) with four lines, each with a base of its
  own; on the right "What was not found out before the build" (search-x icon) — the question
  "compared with what" and the phone the buyer already owned. At the bottom a gold panel with
  the criterion, and under it a teal counterfactual panel about Google Glass. No memes: the
  slide stands on its numbers.
source: "The Verge (7 Aug 2024) — Humane's internal sales data; TechCrunch (18 Feb 2025) — HP's purchase of the assets; Wikipedia / Humane Inc. — dates and prices; Digital Trends / Tom's Hardware (2017) — the AGCO and DHL gains on Glass Enterprise Edition"
---

# Visible content

## Title bar
10,000 devices sold out of the 100,000 planned: the comparison with the phone in the buyer's pocket was made after the build

## Body
[what happened → what the numbers showed and what was not found out → criterion → counterfactual]

[Teal panel — WHAT HAPPENED]
Humane is a company founded in 2018 by people who came out of Apple. Its only product, the AI Pin, is a wearable device with no screen: a small box worn on your clothes with a camera, a microphone and a laser projection onto your palm, answering out loud through a language model. The idea: a person stops looking at their phone. The device was shown on 9 November 2023 and sales opened in April 2024 — $699 plus $24 a month. On 18 February 2025 HP bought the assets for $116 million, and on 28 February the cloud service was shut down: the devices in buyers' hands stopped answering.

[Left card — what the numbers showed]
- About 10,000 devices sold — a tenth of the company's own target of 100,000 by the end of the year
- Revenue of about $9 million against about $230 million raised — roughly 4%
- Between May and August 2024, more returns than purchases: by August, closer to 7,000 were still in people's hands
- The price was cut from $699 to $499 on 23 October 2024 — six months after sales opened

[Right card — what was not found out before the build]
The discovery phase's question fits in one phrase: **compared with what**. Every buyer already had a phone in their pocket that does the same things, and everything else on top. Reviewers converged on the same point: the device does less than a phone and does it more slowly.
An answer like that costs eight conversations with living people before the build. Here it arrived from the market — by way of $230 million and 10.5 months of sales.

[Gold callout]
The answer about the user arrives either way; the discovery phase only chooses when, and at what price. The criterion that carries forward: a hypothesis about the user is closed by comparing it with whatever that person gets by with today.

[Teal callout — counterfactual]
The device does work, and the miss lies in the answer to who needs it and what for. Google Glass travelled the same road in the opposite direction: the $1,500 glasses were pulled from general sale in January 2015 and then handed to people whose hands are busy with work. At AGCO, a maker of agricultural machinery, machine assembly time fell by 25% and inspection time by 30%; at the logistics company DHL, warehouse output rose by 15% — all against the same work done without the glasses. Same device. Different user.

## Speaker notes

The section's second failure is about what happens when the discovery phase is gone through as a formality.

What happened. Humane was founded in two thousand eighteen by people who came out of Apple. Its only product is a wearable device with no screen: a small box worn on your clothes with a camera, a microphone and a laser projection onto your palm, answering out loud through a language model. The idea: a person stops looking at their phone. It was shown in November of twenty-three, sales opened in April of twenty-four — six hundred and ninety-nine dollars plus twenty-four a month. In February of twenty-five HP bought the assets for a hundred and sixteen million, and on the twenty-eighth of February the cloud was shut down: the devices left in buyers' hands stopped answering.

The numbers. About ten thousand sold — a tenth of the company's own target of a hundred thousand. Revenue of about nine million against two hundred and thirty raised, which is four percent. Between May and August of twenty-four there were more returns than purchases: by August, closer to seven thousand devices were still in people's hands. The price was cut from six hundred and ninety-nine to four hundred and ninety-nine in October, six months after sales opened.

Now the root, and it lies squarely in our phase. The question of discovery fits in one phrase: compared with what. Every buyer already had a phone in their pocket that does the same things, and everything else on top. Reviewers converged on the same point: the device does less than a phone, and more slowly. An answer like that costs eight conversations with living people before the build. Here it arrived from the market — by way of two hundred and thirty million and ten and a half months of sales. Think back to the rule from the base slide: ask how much a person pays today for the nearest equivalent. The nearest equivalent was the phone they had already bought.

And now the distinction, so that the case does not read as "the hardware did not come off". Google Glass travelled the same road in the opposite direction. The fifteen-hundred-dollar glasses were pulled from general sale in January of fifteen, and then handed to people whose hands are busy with work. At the agricultural machinery maker AGCO, machine assembly time fell by a quarter and inspection time by thirty percent; at the logistics company DHL, warehouse output rose by fifteen. All of it against the same work done without the glasses. Same device. Different user.

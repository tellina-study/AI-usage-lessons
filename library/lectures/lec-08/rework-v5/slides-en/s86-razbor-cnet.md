---
# Source: chapter/chapter-part3e.md § 5.9; REESTR-RAZBOROV-part3.md line 5.2.
# Second-step column — (a): both sides counted in one unit. "Column (a)" is the registry's
# working language, not surfaced on the frame (form §6.3).
# The baseline (40–61% with ≈2% corrected) stands ON THE FRAME and may not be dropped: without
# it, 53% reads as a verdict on the model, when it says something else.
# One of the section's two breakdowns with both sides counted; both are on the cut-protection list.
grafa: "a — both classical modes counted in the same unit as the model"
# CONSOLIDATION (#301, Section 5 overhaul): merged with the former s86a ("What the newsroom
# had in place, and what others wrote") — that frame carried the second half of the same
# breakdown (the loop's structure + the editorial standards of four newsrooms), split into a
# separate file only during the fix for the first render. The four standards (AP, Guardian,
# BBC, Springer Nature) are consolidated into one compact plate instead of a separate
# `dorozhki` diagram — the frame already carries four numeric-breakdown plates and there's no
# room left for a second heavy form; the names and wording of all four standards are preserved
# verbatim in the plate and in the notes. The frame's conclusion ("accountability rests on the
# person, not the model") carried over as `itog`. Minutes added (0.7+0.6=1.3). The old `s86a`
# was removed as a separate file.
id: s86
local_id: "s86"
section: "5. Recognition and Provenance"
type: analitika
title: "Breakdown: CNET — 41 corrections out of 77 articles"
assertion: "From November 2022 to January 2023, the outlet published 77 articles prepared by an in-house machine engine under an editorial byline, and a full review after the exposure found 41 articles needing corrections — 53 percent; the second half of the pair, without which this number reads wrong: independent audits put 40–61 percent of newspaper articles at having at least one error under the classical mode, with about two percent publicly corrected — meaning the gap was found not in the error rate but in the share corrected publicly, and not one measure adopted by the industry required a better model"
source: "CNET, 'CNET Is Testing an AI Engine. Here's What We've Learned, Mistakes and All,' January 25, 2023; https://www.cnet.com/tech/cnet-is-testing-an-ai-engine-heres-what-weve-learned-mistakes-and-all/"
chapter_ref: "chapter-part3e.md § 5.9"
media: "assets/screenshots/s86-cnet-ai-engine-article.png"
media_needed: ""
media_note: "a live screenshot of the real outlet page, taken by a page-rendering service (tier 6: the public service image.thum.io, first request returns a placeholder, second returns the real render). This is the breakdown's primary source: the newsroom's own explanation dated January 25, 2023, signed by editor-in-chief Connie Guglielmo. The top ad block and right-hand ad column are cropped out. No source caption on the slide"
blocks:
  - {label: "Unit — one for both sides", value: "share of material requiring correction", note: "a rarity — usually only one side is counted"}
  - {label: "The outlet's pipeline", value: "41 of 77 articles, i.e. 53%", note: "including an error in a compound-interest calculation"}
  - {label: "Newsroom without a model", value: "40–61% of articles with at least one error", note: "53% from the pipeline falls inside this band", key: true}
  - {label: "Corrected publicly", value: "about half, versus about 2%", note: "this is where the gap is found — not in errors, but in admission"}
blocks_per_row: 4
timing_min: 1.3
in_bucket: true
method_steps: ["①cost of both errors", "②both modes on one scale", "③model against the modes", "④how it works", "⑤what moved downstream", "industry standards"]
form: []
vfy: true
status: собран
# Overhaul (#301): adding an `itog` ("accountability rests on the person, not the model") was
# also tried — measurement showed a −0.40" overflow (the side image already holds up to the
# wire with no slack). Dropped; the same conclusion already reads in the last plate ("this is
# exactly where the gap is found…") and in the notes.
---

## Visible slide text

**A new technology's measured failure is compared against the measured behavior of the old one, not against an imagined 'error-free' newsroom.** *Both sides, in the same unit.*

## Speaker notes

One of the section's two cases with both sides counted in the same units. There are only seven such cases in the whole lecture, and the last two stand here back to back.

The unit of measurement is the share of material requiring correction. The cost of the error "release something wrong" is measured on both sides, and that is rare. The cost of the error "fail to release on time" is absent from the sources: the throughput norm for a finance desk is not in the selection, though such a figure does exist in industry practice. The gap is named.

Both classical modes are counted on the same scale. Mode one — the outlet's own machine pipeline: from November 2022 to January 2023, seventy-seven articles were published, prepared by an in-house engine and signed with an editorial byline. After the exposure, the newsroom ran a full review: forty-one of seventy-seven, that is fifty-three percent, needed corrections, some substantial — including an arithmetic error in an explainer about compound interest. Mode two — an ordinary newsroom without a model: independent audits of newspaper accuracy put forty to sixty-one percent of articles at containing at least one error, with about two percent publicly corrected.

Now the comparison, and its conclusion is counterintuitive — that's where the whole value of the breakdown lies. Fifty-three percent from the machine pipeline falls inside the forty-to-sixty-one-percent band of the classical mode. No gap at all was found between the two modes by error rate. The gap was found somewhere else: in the share corrected publicly — about half against roughly two percent. The machine pipeline corrected about half of its articles visibly under exposure; the classical mode has quietly lived with the same error rate for decades.

From this comes a rule more useful than the claim "the model errs more often": a new technology's measured failure has to be compared against the old technology's measured behavior, not against an imagined one. An imagined newsroom without a model never errs; the measured one errs in every other article. This isn't an excuse for the machine pipeline — it's a precondition for saying what it actually made worse and what it left as it was.

Let me repeat the comparison in the right order — that's where the whole value of the breakdown lies. Fifty-three percent of the machine pipeline's material needed corrections. The band for an ordinary newsroom with no model at all is forty to sixty-one percent. Fifty-three falls inside the band, not outside it: no gap at all was found between the two modes by error rate.

The gap was found somewhere else, and it's large. The machine pipeline, under exposure, corrected about half its material publicly; the classical mode has lived for decades with the same error rate and publicly corrects about two percent. That is, the new technology turned out to be no worse on errors and noticeably more honest about admitting them — not because it's better, but because people were watching it.

From this comes a rule more useful than "the model errs more often": a new technology's measured failure is compared against the old technology's measured behavior, not against an imagined one. An imagined old technology never errs, and against it any new one looks like a disaster.

The structure of the case has to be known precisely. From November 2022 to January 2023, the tech outlet published seventy-seven articles prepared by an in-house machine engine and published under the editorial byline "CNET Money Staff"; the product's name was never made public — it was looked for and not found. A stated editorial review existed: a human was in the loop. It was exactly this loop that let through forty-one pieces, some with substantial errors, including arithmetic in a compound-interest explainer.

How this is fixed — the industry's working answer, and it belongs right next to the breakdown's numbers. None of the adopted measures demanded a better model; all of them demanded a named person at a named step. The Associated Press, in August 2023, redefined the output of a generative tool as unverified source material — this alone removes the question "can it be published without checking." The Guardian's editorial policy requires explicit senior-editor approval for significant generated elements; the BBC's wording is that any use of a model for editorial purposes must have a senior editorial figure who is responsible and accountable. Springer Nature codified the highest risk tier: use that substitutes for expert judgment is not permitted at all, regardless of the quality of the output.

What all four standards have in common. None of them bans the use of a model, and none introduces a quality threshold — and that is not an oversight: a threshold would be meaningless, because the classical mode's error rate itself sits in a band of forty to sixty-one percent, and any threshold below that would ban ordinary newsrooms along with it. All four name a person: a senior editor giving approval; an editorial figure who is responsible and accountable; an editor checking the output as unverified source material. What closes the gap between the pipeline's speed and the check's speed is one of two things: either a time norm for checking, expressed in hours and built into the plan, or a named person who signs off on release and has the right not to.

Measured audience response: a survey across six countries, about twelve thousand respondents, summer 2025. A news story made entirely by a machine is comfortable for twelve percent; by a machine with a human in the loop, twenty-one; by a human assisted by a model, forty-three; entirely by a human, sixty-two. Human oversight triples acceptability, and its ceiling is visible right there too: the audience's demand is aimed at disclosure, not prohibition — "tell us it was used," not "don't use it."

The breakdown comes down to this observation. "Human in the loop" is not a safety measure on its own. It becomes one when there is a time norm for checking, proportionate to the pipeline's speed, and the right to stop a release. Without those two conditions, a human in the loop turns into a signature under someone else's work that they physically never had time to read.

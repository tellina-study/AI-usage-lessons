---
# THE PATH FROM REQUEST TO RESULT (#301, PUT-OT-ZAPROSA-K-REZULTATU.md): the frame carries a
# figure — six stations, declared empty: request → how it gets inside → where the result starts
# → the step repeated N times → how the visible thing is produced → the result. Six steps on one
# `scheme` row would exceed `tracks.max_steps`/`scheme.max_steps` (owner: "no long pipelines"),
# so the figure is split across TWO rows of three stations each, by the same device s02 uses
# ("the second row continues the first").
#
# EDIT 10/29/2026 (coordinator, from the rendered snapshot). Three findings:
#   (1) the caption under the diagram carried a methodological comment about LAYOUT ("the second
#       row continues the first — by the same device...") — forbidden outright (CLAUDE.md § "No
#       Timing / No Methodology in Slides": the room must not know by what device the boxes are
#       arranged). Removed entirely.
#   (2) that same caption repeated the plate below it word for word ("The figure is empty:
#       numbers will appear..." = "This figure is empty. The next five sections will fill it
#       in...") — the duplication was removed, one plate remains.
#   (3) the row labels "Stations 1–3" / "Stations 4–6" were a service numbering layered on top of
#       the numbering already sitting inside the boxes (1…6) — removed, `label: ""`.
#
# WHAT THIS LECTURE DOES NOT COVER — RESTORED TO THE VISIBLE LAYER (coordinator, 10/29/2026).
# Round #301 moved three exceptions into s06's notes — this is exactly the forbidden move from
# SVEDENIE-KADROV.md §4 ("content must not be cut to fit the space"), just dressed up as
# "consolidation." Fixed: the blocks sit here, on the visible layer, next to the figure — the
# empty bottom 40% of the frame is now occupied, and the pairing is natural: "here is the figure
# the next five sections will fill in" plus "and here is what this evening will not cover." One
# frame, two jobs (exactly as intended in PUT-OT-ZAPROSA-K-REZULTATU.md §7: the frame about
# exceptions is a neighbor of the figure, not its owner — the consolidation does not remove the
# content of the exceptions, it only removes their status as the frame's SOLE owner).
#
# Minutes: 0.4 → 0.5 — back to s07's original budget (the 0.1 minutes removed in s06 go back to
# where they came from); the figure fits into the same half-minute that used to carry one part of
# the content on its own, because its own explanation in the notes is now condensed. There are
# still no images (media="" as before) — the section carries three images total (s01, s02, s04).
id: s07
section: "0. Entry"
type: assertion_visual
title: "The path from request to result: one figure, five sections ahead"
assertion: "Six stations of one and the same figure — request, input, start, the repeated step, output, result — will run through all five modalities; here it stands empty. Next to it — three pieces deliberately set outside the evening's boundary, each with a named address"
source: ""
blocks:
  - {label: "Safety, forgery, abuse", value: "Lecture 14", note: "deepfakes in personnel security, voice fraud, document forgery, law enforcement"}
  - {label: "Agents, tools, programmatic access", value: "Lecture 3", note: "call chains, adapter fine-tuning, a human validator — taken as already known"}
  - {label: "The labor market and a country-by-country jurisdiction review", value: "in the chapter, as reading material", note: "collected and checked, but does not go onto the slides: it would crowd out the capabilities"}
scheme:
  rows:
    - label: ""
      arrows: true
      steps:
        - "1. request"
        - "2. how it gets inside"
        - "3. where the result starts"
    - label: ""
      arrows: true
      steps:
        - "4. the step, repeated N times"
        - "5. how the visible thing is produced"
        - "6. result"
columns: {}
media: ""
layout_note: "two frames in one: the path figure (empty, to be filled in by sections 1–5) and the evening's boundary (three exceptions with a named address). The gap on the exceptions is named for a reason — there is no \"surely something got missed\" hedge"
timing_min: 0.5
in_bucket: false
status: собран
---

## Visible slide text

**This figure is empty.** The next five sections will fill in their own numbers: what repeats, where the request takes part, what changes, where the bottleneck is.

**What this lecture does not cover.** The boundary runs along the subject, not the technology — every exception has a named address.

## Speaker notes

Section 0 has already shown WHAT got cheaper — the failed attempt, not execution — and WHY that
matters economically. This figure is about something else: about HOW the model's own work is
built, before a request becomes a result. Up to now, the course has only had diagrams of
structure — what parts a generator is built from. Diagrams of operation, that is, "what happens
to a request step by step," have not had a single one yet in this lecture. Here it is, and for
now it is empty: read left to right, a request comes in, somewhere it enters the model, from some
point the future result starts, then comes a step that repeats N times, the last repetition
yields what a human sees, and that is the result.

Four numbers will be named in each of the five sections, and all four are about this same
figure. How many times the step repeats — and what that number depends on: the sampler, the depth
of the cascade, whether the method has a trained general prior or each object learns from
scratch. Where the request takes part — at every step, or only at the start. What changes inside,
and what stays the same. And one bottleneck per section — the single place in the method that
holds the whole economics, named the gold.

The figure has a second track, and it will be needed in every one of the five sections: a
request with an example. A reference — a source image that needs finishing, a voice reference,
photos of an object, a frame that needs continuing — enters the same figure at one point, at the
start: the starting state is drawn not from noise but from the example, and the rest of the path
is the same. The recognition section will run the figure in reverse: there, the question being
solved is not "how do I get an image from a request" but "what is pictured in this image," and
the arrow, which everywhere else here points right, reverses there — this is not a violation of
the figure but its inverse problem, the same machinery set to answer a different question. At the
end of the evening, in the Wrap-up, five filled-in figures will come together into one table — one
row per modality, one column for the start and one for the bottleneck.

Three pieces are deliberately set outside the boundary of this lecture, and each one states where
it is covered. This is not a hedge just in case and not an apology for incompleteness: the
boundary is drawn along the subject, and knowing exactly where it runs is necessary so as not to
expect from the evening what it will not deliver.

The first piece is safety, forgery, and abuse. Into it go deepfakes in personnel security, voice
fraud against a loved one, document forgery, and the whole law-enforcement side. What stays here
is only what belongs to creative production: a performer's right to their own voice, the
provenance of training data, labeling of synthetic content on release. The very same voice-cloning
model is, in this evening, a tool that gave a performer back the ability to work after an illness
took his voice; in the conversation about safety, the same model is a tool of telephone fraud.
Both frames are true at once, and neither cancels the other. Taking them apart mixed together
would mean getting an evening where every measured win is followed by a scary story, and every
scary story by an excuse, with neither one ever carried through to a number.

The second piece is agents, tools, and programmatic access. That ground has already been covered:
how a model is called from code, how call chains are built, how adapter fine-tuning works, and
where a human validator is needed. All of this is taken here as already known and applied to the
new family of models. But this lecture does have its own contribution — something that could not
have existed in a conversation about language models: why the familiar levers for controlling
output work differently here, or are absent by construction, and section 1 will cover exactly
that.

The third piece is the labor market as a whole and the country-by-country jurisdiction review.
This is the one point where the decision was made by budget, and saying so plainly is more honest
than inventing a substantive justification. The material is collected, checked, and sits in the
chapter as self-study reading. The arithmetic reason it is not on the slides: the price layer
takes up about a fifth of the evening, and a country-by-country legal landscape does not fit into
that volume without crowding out the conversation about capabilities. Separately: twenty-two
common claims about the effect of generative models on employment were checked directly against
primary sources and did not hold up — the list of what got dropped sits in the chapter as a
working example of how much ends up discarded when an industry survey is checked honestly.

---
# Source: chapter/chapter-part3d.md §§ 5.1, 5.4. The case names on the divider match
# verbatim the titles of s80, s86, and s87 — requirement of form §5.16.
id: s78
local_id: "s78"
section: "5. Recognition and Provenance"
type: section_divider
title: "Section 5. Recognition and Provenance"
assertion: "The four previous sections examined a model that generates; this one examines a model that reads — the architecture is the same, often literally the same weights, but the task is inverse, and from that inversion everything else follows: different economics, different verifiability, different limits"
source: ""
chapter_ref: "chapter-part3d.md §§ 5.1–5.6; chapter-part3e.md §§ 5.9–5.20"
media: "assets/screenshots/s78-herculaneum-papyrus-1521.jpg"
media_needed: ""
media_note: "Wikimedia Commons, File:Heruclaneum Papyrus 1521 f002r, British Library.jpg, public domain. Tier 2 (Wikimedia Commons). A fragment of a Herculaneum papyrus from the British Library's collection — the exact class of object with which the section's first case study will open. No source caption on the slide"
blocks:
  - {label: "Capability breakdown", value: "1", note: "a case for which no classical mode producing the same result exists at all"}
  - {label: "Editorial breakdowns", value: "2", note: "both with both sides counted — only seven such cases in the whole lecture"}
  - {label: "Mentions", value: "2", note: "an industry with a count instead of a survey, and dubbing at the scale of a whole platform"}
timing_min: 0.0
in_bucket: false
method_steps: ["divider"]
form: []
vfy: false
status: собран
---

## Visible slide text

# Section 5. Recognition and Provenance

**Four sections in a row, we examined a model that generates. This one reads.** The same attention blocks, the same training, often literally the same weights — and an inverse task. From that inversion everything else follows: different economics, different verifiability, different limits.

**1 capability breakdown · 2 editorial breakdowns · 2 mentions**

In order: **Breakdown: the Herculaneum scrolls — a scroll read in full** · **Breakdown: CNET — 41 corrections out of 77 articles** · **Breakdown: Russian media — 18% of articles carrying traces of generation**

## Speaker notes

This section is built differently from the four before it, and the difference is worth naming before the material starts. A generative model answers the question "make this"; a recognition model answers "what is this." Inside, they have the same attention blocks, the same gradient-descent training, and in the early diffusion models the understanding of the prompt was literally supplied by a borrowed recognition model. The task differs, and from that inversion three things follow.

First — economics. A generative model spends on every run a full pass through all the denoising steps; the section on still image showed that an image model allows no caching and rewrites all four thousand latent units at every step. A recognition model does a single forward pass and outputs a number. The gap in inference cost is orders of magnitude, and from that follows a direct consequence for tool choice: tasks of the form "find among what already exists," "select," "verify," "label" are solved cheaply and with a verifiable answer by recognition, and a generator is the wrong tool for them.

Second — verifiability. A recognizer has ground-truth labeling — that is, a set of examples with known correct answers; quality is measured as a number and compared between models. A generator has no ground truth by construction: there is no correct answer to "draw a dragon." This distinction runs through the whole section and, at the end, fills in the one cell of the cumulative map that stayed empty across the four generative modalities.

Third — place in the production pipeline. Formally, the stage is last, between "done" and "released." But it serves more than release: recognition stands at the start — finding a reference in an archive — in the middle — deduplication, labeling, checking the generator's output — and at the end — a check before publication. In creative production, recognition handles more tasks than generation, and handles them at orders of magnitude lower cost.

This stage is cheap enough that it is worth keeping in mind as a separate argument when choosing a tool: recognition can be run continuously in places where generation would have to be rationed. Moderating every uploaded file, labeling an entire archive, checking every output of a generator — at the cost of a single forward pass, all of this becomes a background operation.

The stage goes by different names depending on the trade, and it is worth reconciling them now, because from here on they appear interchangeably. In a newsroom it is fact-checking and source confirmation. In museum and archival work it is attribution and authenticity expertise. In technical literature it is recognition, as opposed to generation, and provenance — that is, traceable origin. On platforms it is moderation and disclosure. The task is the same for all of them: given a finished work, answer a question about it, generating nothing new.

One distinction is worth drawing before the section can blur it. A recognition model answers a question about a finished work, and its answers come in three different kinds: what is depicted here, how it was made, and who is accountable for it. The first is checked by cross-referencing another source; the second is probabilistic and rests on whether the recognizer has ever seen that particular generator; the third is about people and organizations and does not touch the content at all. None of the three answers the question "is this true" — and swapping one question for another is the single most common error in conversations on this topic, including among people who understand how the mechanism works.

And one last thing before entering the section. This is where lives the one case in the whole lecture where the win has no downside, and the payment address "discernment" received a profit. Next to it stand two editorial breakdowns with both sides counted, and both give a result opposite to what is usually expected to be heard about machine-written text. The section's content runs between these three.

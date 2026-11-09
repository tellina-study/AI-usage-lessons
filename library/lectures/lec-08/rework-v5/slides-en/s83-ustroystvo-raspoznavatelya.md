---
# Source: chapter/chapter-part3e.md §§ 5.11 (Steam), 5.12 (automatic dubbing),
# 5.13 (ViT and CLIP), 5.14 (what matches and what diverges), 5.15 (signature outside and
# watermark inside).
# Labeling regulation (AI Act Art. 50) is NOT duplicated here: it is carried by the legal block
# of Section 1 (chapter-part1d.md), frame s32 — confirmed by the orchestrator on 2026-10-27.
#
# CONSOLIDATION (#301, Section 5 overhaul): merged with the former s82 ("Steam and automatic
# dubbing: two counts with a denominator") — that `r5` recording never mentions these two
# cases at all (STROENIE-IZ-ZAPISEY-part4.md §2.2), meaning this is our own material, not a beat
# of the narrative arc, and the arc does not judge it; but that is not a reason to drop it
# entirely — both cases carry something rare for the evening, a count with a denominator instead
# of a survey, and the methodological lesson about two different denominators from one source.
# Only the form was dropped: the `shkala` diagram (three columns by year) was replaced with a
# compact plate carrying the same row of numbers — next to the already-heavy `arhitektura`, a
# second full-size diagram would not fit (two heavy forms on one frame are permissible, but a
# third page of text on top of them is not). The numbers and the methodological lesson (two
# denominators, a false pair) carried over UNCHANGED into the notes. Minutes added
# (0.5+0.6=1.1). The old `s82` was removed as a separate file.
id: s83
local_id: "s83"
section: "5. Recognition and Provenance"
type: schema_architecture
title: "How a recognizer is built: the same attention blocks, an inverse task"
assertion: "The two models underlying this entire stage predate the generators and work inside them: an image is cut into patches and fed into an ordinary transformer encoder, and a pair of image and text encoders projects both into a shared space — and the text encoder of that pair is exactly the prompt-understanding component inside early diffusion models; generation and recognition diverge in three places — cost (one forward pass against dozens of denoising steps), verifiability (ground-truth labeling exists; a generator has none by construction), and the way of training. The one industry of the evening with a count instead of a survey is Steam games: the share of the year's releases disclosing generative tools grew from 10.9% in 2024 to 30.8% by July 2026; for automatic dubbing on a video platform there is one measured number — over a quarter of watch time on tracks not in the primary language, against a zero baseline"
source: "Dosovitskiy et al., ICLR 2021, arXiv:2010.11929; Radford et al., ICML 2021, arXiv:2103.00020; Nature, October 2024, doi:10.1038/s41586-024-08025-4; Steam's public disclosure pages; platform announcements on dubbing, February 11, 2025"
chapter_ref: "chapter-part3e.md §§ 5.11–5.15"
media: ""
media_needed: "no suitable diagram under a free license was found. Tried: (1) og:image of the arXiv paper pages — return the service's branding splash; (2) Wikimedia Commons — 'vision transformer architecture' gives an animated file unsuitable for a printed frame, and nothing static on the topic; 'CLIP contrastive' — zero; (3) the authors' own lab pages — article figures fall under the article's own license, not a free one; (4) a video cover — no canonical video exists; (5) web archive — the same pages; (6) image search — retellings of the diagram on third-party sites with no license stated. The frame's diagram is built with the deck's own tools. For the Steam/dubbing block: a genuine screenshot of the disclosure block on a Steam game page was needed — the block sits deep in the page and does not appear in a first-screen capture, and substituting a page without it would be a fake; same for dubbing (og:image, Wikimedia Commons, Valve announcements, video covers, web archive — everywhere either a splash screen or nothing on the topic)"
media_note: ""
# Overhaul of forms (#301, Section 5): there used to be a `dorozhki` diagram with two tracks
# (steps as text under a label) — that is, an order of operations, while the frame asserts
# STRUCTURE: what the recognizer is made of, what each part does. `arhitektura` carries the
# breakdown INSIDE the boxes, word for word from the former diagram's steps, with no facts added.
# `strelki` is the owner's own keystone guard at the bottom: this frame is exactly the place
# where the recognizing architecture is explicitly unfolded in the reverse direction relative
# to the generator (which the s78 divider leads into), and until now this claim had no picture
# of its own, only a paragraph of notes. Decided in favor of s83, not s79 (the "s79 or s83"
# option from work order §9): s79 already has a side image (body narrowed to ~5.9") and three
# plates with the newsroom baseline — a second image does not fit there and is not about what
# s79 asserts (the stage's decisions/questions). s83's body was free (media_needed — no image
# found), and the claim "same architecture, inverse task" is exactly what the title states here.
# The 2 plates that stood here (400 million pairs · "one pass is cheaper") were dropped — their
# numbers carried over INSIDE the arhitektura boxes below (verbatim, not retold), not lost:
# otherwise they would duplicate, and there wasn't enough height on the frame anyway
# ([height] s83/body: -1.91" before the fix).
arhitektura:
  blocks:
    - head: "Vision model (ViT)"
      role: "patch → token"
      lines:
        - "transformer encoder: the same attention blocks"
        - "output — a label; orders of magnitude cheaper than generation"
    - head: "Pair of encoders (CLIP)"
      role: "image + text → shared space"
      lines:
        - "trained on 400 million image–caption pairs"
        - "the task — guess the caption for its own image"
# PATH FROM REQUEST TO RESULT (#301, PUT-OT-ZAPROSA-K-REZULTATU.md): the owner required
# a diagram of the WORK (what happens to the request) in every section — `arhitektura` above
# answers "what it's made of," `strelki` here is the first to answer "what happens to the
# request." Section 5 is the only one where the path runs backward, and the form of opposing
# arrows (exactly what was built into the docstring above but not implemented) shows "the same
# machinery, run in reverse" in one picture, with no paragraph needed. Four numbers are named
# inside the arrows themselves: how many times the step repeats (20–50 for the generator against
# 12–32 ViT layers, chapter-part3e.md § 5.13) · where the request participates (at every step
# against once at the input) · what changes/stays the same (the latent changes, the embedding is
# frozen / the patch's representation changes, their count doesn't) · the bottleneck (the
# autoencoder's latent against a single output number). The numbers are existing facts from the
# chapter, not new ones.
# What's been paid for (Section 5 has no "training" candidate from the §3 brief — the payment
# is inside the frame itself): 2 plates on Steam/dubbing (added when s82 was merged into s83 by
# the same round #301) were dropped from the visible layer and moved into the notes IN FULL,
# without loss — a much more detailed text on both cases already stood there (the "Steam, the
# platform…" and "A second mention…" paragraphs below), and the plates duplicated it with a
# brief retelling. The visible body paragraph is shortened to one sentence (the second half —
# into the notes, by the same move). The section's minutes are UNCHANGED (1.1 as before), the
# section's image count did not decrease (the frame had none to begin with — `media_needed`).
# Reviewed on the snapshot `rendered/snapshots/k-1.png` (partial build `--only s83`): both
# arrows and both architecture plates read cleanly, [height]/[point size] are clean.
strelki:
  vpravo: {head: "Generation", text: "the request participates at every one of 20–50 steps; the latent changes, the request's embedding is frozen"}
  vlevo: {head: "Recognition", text: "the request enters once; 12–32 layers in a single pass, the bottleneck is one number"}
timing_min: 1.1
in_bucket: false
method_steps: ["structure", "tool-selection criterion", "mentions with a denominator"]
form: []
vfy: true
status: собран
---

## Visible slide text

**Generation and recognition diverge in three places:** cost, verifiability, training.

## Speaker notes

A recognizer has ground-truth labeling — there is no correct answer to "draw a dragon." Games are the one industry of the evening with a count, not a survey: disclosure is mandatory in fact, voluntary in content, and the share should be read as a lower bound.

The parallel with the lectures on language models is more direct here than anywhere else in the evening, and it is built on words already introduced.

The first of the two foundational models cuts an image into fixed-size patches, linearly projects each into a vector, and feeds the sequence into an ordinary transformer encoder — the same one used for text, with no convolutions at all. A designation like "large model with a sixteen-by-sixteen patch" should be read literally; sequence length is inversely proportional to the square of the patch size — the same law the section on still image derived for the diffusion transformer, because it's literally the same construction. The sizes in the lineup: eighty-six million parameters, three hundred seven, six hundred thirty-two.

The central claim of that work is worth citing, because it explains two fields at once: scale of training beats built-in knowledge of locality. On small data, a patch-based model loses to a convolutional network — convolution has knowledge that neighboring pixels are related built into its construction, a transformer has none; pretrained on hundreds of millions of images, the transformer wins, eighty-eight and a half percent correct. The section on still image used that exact same argument to justify the shift from convolutional architecture to transformers in generation: one argument, two fields, a two-year gap.

The second foundational model is a pair of encoders, image and text, projecting both into a shared space. Training is contrastive, on four hundred million image–caption pairs: the task is to predict which caption matches which image out of a batch. The result is classification with zero training examples of the target set, at the level of a previous-generation convolutional network.

Why these two models belong in a conversation about generation. Both solve recognition tasks and generate nothing — and the generators stand on them: the text encoder is exactly the prompt-understanding component in the early diffusion models, and the adopted automatic measure of image-prompt correspondence is scored by that same model. The text understanding inside a generator is a borrowed recognition model.

What diverges. A language model predicts a probability distribution over the vocabulary and outputs the next token, then the next — as many passes as there are tokens. A recognizer does one pass and outputs a number. From this follow three practical differences. Cost: recognition is cheaper than generation by orders of magnitude, and that is exactly why it can be run continuously — moderating every uploaded file, labeling an entire archive, checking every output of a generator. Verifiability: a recognizer has ground-truth labeling, quality is measured as a number and compared between models; a generator has no ground truth by construction. Training: a labeled set is taken, the model outputs a distribution over classes, it is compared with the correct answer, the gradient goes back — the same loss function as next-token prediction, the only difference being the number of classes.

From here comes a turn worth closing the structure section with: in creative production, recognition stands alongside generation and handles more tasks. Archive search, stock labeling, deduplication, moderation, reference selection, checking a generator's output — all of these are recognition tasks, they are cheaper by orders of magnitude, and they give a checkable answer.

And separately — two provenance technologies, built in opposite ways. Signature outside: a manifest is embedded in the file with claims about who the author is and what was applied, signed with a certificate; the binding can be hard, by hashes, or soft, by a content fingerprint. The weakness is honestly described in the specification itself: a screenshot is a new file, with neither a manifest nor a matching hash. Watermark inside: two networks are trained jointly, one inserts the mark, the other finds it, with imperceptibility achieved by fitting the mark to the content; the mark lives in the pixels and survives the loss of metadata. The fundamental limitation is named in the paper itself: the mark lives on the entropy of the distribution, and every layer of the generation process spends it. Short text, low temperature, code, and factual answers get marked poorly.

Three things match a recognizer with a generative model literally. The same attention blocks with the same queries, keys, and values. The same embedding mechanism and the same low-rank adapter fine-tuning. And the same split of "input representation separate, model separate": a patch here is exactly what a token was in text, and the way the input is cut matters more than the size of the network itself.

It's worth remembering separately that scale of training beats built-in knowledge of locality: a vision model on patches, which has no built-in knowledge of pixel neighborhood at all, reaches 88.55 percent correct on hundreds of millions of images and overtakes convolutional networks. This is the same observation as in text — a sufficiently large corpus replaces built-in assumptions about the structure of the data.

The practical conclusion from this whole pair: where a task is formulated as "find among what exists," a generator is the wrong tool, and the right one stands right next to it. The cheapness of a single forward pass means that moderating every uploaded file and labeling an entire archive can be run continuously; dozens of denoising steps per unit of output do not allow for that.

Two mentions with a denominator, and both stand here not because the section's audio track covers them (the `r5` recording does not name either Steam or auto-dubbing, not a single word — this is course material, not a beat of its narrative arc), but because they carry something rare for the evening: a count that a third party can reproduce, instead of a survey or an analyst's estimate.

Steam, the digital distribution platform for computer games, has since January 2024 required developers to disclose the use of generative tools and displays that disclosure publicly on the game's page. Take one row with a denominator in the same line — the share of the year's releases: ten point nine percent in 2024, nineteen point nine in 2025, thirty point eight by July 2026. The denominator is the same for all three: all games released in the corresponding year. The series is confirmed by a second independent count across fifty-three and a half thousand releases over three years. The second count has something the first doesn't: games with disclosure capture ten to twenty-seven percent of estimated sales for the same period, against three to six percent in 2024, while making up a third of releases.

Two caveats are mandatory. First: disclosure is mandatory in fact and voluntary in content — the developer is required to make it, but decides for themselves what exactly to write, so all the shares should be read as a lower bound. The second caveat matters more than the first, and it's about counting discipline. A second series circulates on the same platform, with a different denominator: the share of the entire catalog instead of the share of the year's releases — about one percent in 2024, about seven in 2025. Both series are true, and both are published, but their bases differ: in the first, the denominator updates every year; in the second, it accumulates from the platform's launch and contains tens of thousands of games released long before generative tools existed. Put the start of one series next to the end of the other, and you get growth that never happened in either one. This is exactly the class of trap the course singles out separately, and it's easy to fall into without any ill intent at all: both numbers are honest, the source is the same, and the conclusion drawn from their pair is false. The rule is simple: one series, denominator alongside it.

Second mention. YouTube rolled out automatic dubbing to its entire partner program on February 11, 2025; eight languages at launch. The only published number on the effect: over twenty-five percent of watch time on channels that posted multilingual tracks comes from views not in the video's primary language. How many channels this is, the platform did not disclose, and the denominator remains without a number on that side of the count. The baseline for this quarter is zero, and that has to be said out loud, or the number looks like a redistribution of existing attention: for a creator shooting in one language, there was no audience in other languages before at all, and dubbing was never ordered for it — a voice actor's rate makes localizing an amateur channel economically pointless. So this quarter of watch time came out of nowhere, replacing nothing. This is the same figure that runs through the whole evening: the attempt got cheaper, and a market that didn't exist appeared.

Why games specifically produced a series with a denominator, and the rest of the evening's industries didn't. Disclosure here is mandatory by platform rule, sits in a visible spot on the product page, and is checkable by any outside person with no access to internal data. In every other modality, information about the share of machine-made content comes from surveys, analyst estimates, or recognizers that have their own error rate. From this comes a useful observation for any industry: where a reliable share is needed, it's cheaper to introduce mandatory disclosure than to build a measuring instrument.

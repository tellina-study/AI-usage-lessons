---
# Source: chapter/chapter-part3e.md § 5.16; Corvi, Cozzolino, Zingarini, Poggi, Nagano,
# Verdoliva, ICASSP 2023, arXiv:2211.00680.
# A dedicated limitations frame, strict-in. This is also where Section 5's audience question is
# unpacked: the question is asked out loud ("how much will it give on a model it hasn't seen"),
# the answer is on the frame. Both terms are explained with a scale line right on the frame
# (§5.20): otherwise "AUC 94.9 at an accuracy of 51.9" reads as a typo, and that is exactly the
# frame's subject.
id: s84
local_id: "s84"
section: "5. Recognition and Provenance"
type: analitika
title: "A recognizer for generated content, on an unfamiliar model"
assertion: "All recognizers are trained on one family of generators and tested on others: 99.9 percent correct on the trained family turns into 51.9 on DALL·E 2 and 51.2 on ADM — that is, a coin flip, and this is on a clean, uncompressed file; and the main trap is that the area under the curve holds at 94.9 the whole time — if an acceptance review looked at that, it would see an excellent recognizer, and if it had looked instead at the share correct at the working threshold, it would see a coin"
source: "Corvi et al., ICASSP 2023, arXiv:2211.00680; https://arxiv.org/abs/2211.00680"
media: ""
media_needed: "a pair, 'the same image through the eyes of two recognizers,' would have been needed — illustrations like that are not published under a free license: the output of recognizers belongs to their owners, and the paper's own figures fall under the paper's license. Tried: (1) og:image of the arXiv paper page — the service's own splash screen; (2) Wikimedia Commons — 'deepfake detection,' 'GAN artifacts spectrum' give either unlicensed third-party demonstrations or nothing; (3) the author labs' own pages — figures under the publication's license; (4) a video cover — no open-access talk was found; (5) web archive — the same pages; (6) image search — unlicensed retellings. The table is itself the frame's subject"
media_note: ""
scheme:
  kind: shkala
  unit: "percent correct at the working threshold"
  base: "the same recognizer, different sources of images"
  caption: "Its own family · a foreign family · the same image after processing. Half the scale is a coin"
  from: 45
  to: 100
  marks:
    - {value: "51.2", label: "ADM"}
    - {value: "51.9", label: "DALL·E 2", key: true}
    - {value: "63.3", label: "after processing"}
    - {value: "98.1", label: "StyleGAN2"}
    - {value: "99.9", label: "own family"}
blocks:
  - {label: "Area under the curve, in the same row of the table", value: "94.9", note: "A DIFFERENT measure: 0.5 of 1 is a coin, 1.0 is no misses. Here it's 0.949, that is, 'excellent,' on a decision indistinguishable from a coin. If an acceptance review looked at this figure, it saw an excellent recognizer", key: true}
blocks_per_row: 1
timing_min: 1.0
in_bucket: true
method_steps: ["boundary of the method", "unpacking the audience question", "acceptance criterion"]
form: []
vfy: false
status: собран
---

## Visible slide text

**A choice between two honest numbers decides whether a system goes into production.**

- ask for the share correct at the working threshold, not the area under the curve
- ask what the recognizer was measured on, and check it against your conditions of use
- the fix is incomplete: the average over the same 12 generators grows from 75.8 to 87.8, while DALL·E 2 stays at 66.9

## Speaker notes

Before reading the second row of the table, try predicting the answer yourself: a recognizer gives ninety-nine point nine percent on the family of models it was trained on — even on re-compressed files. How much will it give on a model it has never seen? The usual guesses are eighty to ninety percent — it recognizes generation artifacts in general, after all; seventy percent; noticeably worse but still useful.

The answer: fifty-one point nine percent. A coin. And this is on a clean, uncompressed file; after passing through a social network — exactly fifty.

Now the whole table, because three different conclusions can be read from it, and they must not be mixed up. All the recognizers in this work are trained only on one family of generators and tested on others; the second column simulates a file passing through a social network — cropping, resizing, re-compression at a random quality level.

First conclusion: switching generators kills the recognizer. Ninety-nine point nine percent on the trained family turns into fifty-one point nine on DALL·E 2 and fifty-one point two on ADM. That's a coin flip, and this is on a clean file, with no processing at all. The reason is mechanical: the recognizer learns to tell apart the traces of one specific generator, not "a sign of synthesis in general," and it has never seen the traces of a new generator.

Second conclusion: ordinary processing kills the recognizer even where it used to work. On StyleGAN2, where it gave ninety-eight, after cropping and re-compression sixty-three remains. The authors' own wording is precise: forensic traces are very weak and are easily removed even by these unfriendly processing steps. That is, a social network breaks the recognizer with no such intent at all — just by re-compressing the image on upload.

Third conclusion — the acceptance trap, and this is a ready-made lesson. Verbatim from the authors: quality is acceptable in terms of area under the curve, but almost random in terms of accuracy. The reason is mechanical: a threshold picked on training data drifts on data of a different origin. The area under the curve measures how well the model ranks examples at any threshold whatsoever, and it can be excellent for a system that, at its own working threshold, is wrong half the time. On a clean file here, the area under the curve is ninety-four point nine at an accuracy of fifty-one point nine; after compression — sixty-four point four at exactly fifty. The decision the system actually makes is indistinguishable from a coin.

The working rule that follows is direct: ask for the share correct at the working threshold, not the area under the curve. This continues a thesis the course has already run on language models: optimizing for a metric beats the metric, and the choice of acceptance metric matters more than the choice of model.

An attempt at a fix exists in the same work, and the result is telling. Fine-tuning on latent diffusion, merging with the previous recognizer, and calibrating on two real and two synthetic examples per model raise the average from seventy-five point eight to eighty-seven point eight. The denominator of this average has to be named, or it reads as "overall": the average is taken over the same twelve generators measured in the original result — ProGAN, StyleGAN2, StyleGAN3, BigGAN, EG3D, Taming Transformers, DALL·E Mini, DALL·E 2, GLIDE, latent diffusion, Stable Diffusion, and ADM. And inside that average, two generators remain at the bottom: DALL·E 2 — sixty-six point nine, ADM — seventy point eight. That is, the average was raised, but the hole wasn't closed. The authors' conclusion: we still cannot reliably detect images with artifacts substantially different from those seen during training.

And a separate detail — an example of feature leakage, useful far beyond this task. Real photographs are always compressed by the camera, while synthetic samples are often stored losslessly. A recognizer can latch onto the absence of compression artifacts instead of the generator itself, and show excellent numbers on a test set that will fall apart in real use the moment it meets a genuine photograph saved without loss.

One more pair of numbers from the same table: file processing has nothing to do with it here. On DALL·E 2, the recognizer gives 51.9 percent on a clean, uncompressed file, with no processing at all; after passing through a social network — exactly 50.0. That is, it's already a coin anyway, and the platform's compression doesn't make it worse, because there's nothing left to spoil. For comparison: on a familiar family, it gives 99.9 and holds 99.9 after cropping, compression, and re-compression. Robustness inside its own family and helplessness outside it are one and the same property, seen from two sides.

It's worth stating the authors' own conclusion verbatim, because it's stronger than any paraphrase: "we still cannot reliably detect images with artifacts substantially different from those seen during training." This is said not by critics of the method, but by the people who measured it.

The fix mentioned in the frame's last line is made up of three techniques at once: fine-tuning, merging the new recognizer with the previous one, and calibrating on two examples per model. The average over the same twelve generators rises from 75.8 to 87.8 percent — and that's real progress. But DALL·E 2, after the entire fix, stays at 66.9, and ADM at 70.8: neither reaches working acceptance quality.

And the third conclusion of the same table, easy to lose behind the first two: ordinary processing breaks the recognizer where it used to work. On StyleGAN2 it gave 98.1 percent; after cropping, resizing, and re-compression — 63.3. That is, a social network, which simply re-compresses an uploaded picture, breaks the recognizer with no such intent at all.

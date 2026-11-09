---
id: s31
section: "1. Still Image"
type: analitika
title: "What It Was Trained On: 1.84 Bytes per Training Image"
adres_osi: "RIGHTS"
assertion: "The model doesn't store pictures — one gets less room than a single letter. But a picture that lands in the corpus a hundred times stops being one of two billion. What gets memorized is the duplicate, not the corpus. Rights follow from this architecture in one chain: doesn't construct the object → doesn't copy → the only thing left is the trademark — and the next slide takes that apart"
source: "the Stable Diffusion 1.5 model card · Carlini et al., «Extracting Training Data from Diffusion Models», 2023 · the LAION corpus downloader tool's report"
vopros_zalu:
  text: "The model weighs 4.27 GB and was trained on 2.32 billion images. How many bytes of weights does one training image get: a kilobyte, a hundred bytes, or less than a letter?"
  kanal: "in chat, one word"
  vskrytie: "on this same slide, in the next block"
blocks:
  - {label: "The answer", value: "4.27 GB ÷ 2.32 billion images = 1.84 bytes", note: "less than a Cyrillic letter; compression across the corpus ×22,508 — a picture in the corpus weighs 41,379 bytes on average", key: true}
  - {label: "Even by the most generous count", value: "26.7 bytes per picture", note: "against 160 million cross-checked examples — fifteen hundred times smaller than a 512×512 JPEG (which is never shorter than 20,000 bytes)", key: true}
  - {label: "Extracted by Carlini et al., 2023", value: "109 images out of 175 million candidates", note: "they selected the 350,000 most duplicated examples and generated 500 candidates for each; the extraction threshold is a hundred duplicates in the corpus"}
vtoraya_polovina:
  title: "The second half is mandatory"
  text: "Diffusion models memorize individual images and output them during generation"
  metodika: "they selected the 350,000 most duplicated examples, generated 500 candidates for each — 175 million images — and found 109 extracted: 94 by the formal criterion plus 13 on manual labeling"
  doli: ["109 / 175,000,000 = 0,000062%", "109 / 350,000 of the most duplicated prompts = 0,031%"]
  mehanizm: "extraction succeeds most often when an image has been duplicated in the corpus at least a hundred times. The model card confirms this from the other side: no deduplication measures were applied to the dataset"
media: ""
media_needed: "a chart was built (assets/charts/s31-bayty.png, three byte counts against the corpus's average picture size), but the slide has nowhere to put it: four plates and both halves of the conclusion fill the body completely at any sidebar width up to 4.00\""
timing_min: 0.7
in_bucket: true
status: собран
---

## Visible slide text

*Payment address: RIGHTS.*

**The model weighs 4.27 GB, trained on 2.32 billion images — 1.84 bytes per picture.**

**And yet duplicates get memorized:** 109 extracted out of 175 million candidates, at a threshold of a hundred duplicates in the corpus. The first half without the second is advertising; the second without the first is an accusation.

## Speaker notes

The question is worth asking the room before showing the answer: the model weighs 4.27 GB and
was trained on 2.32 billion images — how many bytes of weights does one training image get: a
kilobyte, a hundred bytes, or less than one letter? Intuition almost always overshoots, which is
exactly why the answer lands. The payment address here is rights: this very division is the
first step toward the question of who owns what came out.

4,265,146,304 bytes of weights, divided by 2,320,000,000 images, give 1.84 bytes per picture.
One Cyrillic character in a common encoding takes exactly two bytes. That is, for every picture
the model saw during training, it gets less room in the model than one letter of this sentence.

The picture itself, in the same corpus, weighs 41,379 bytes on average — this is measured, not
estimated: the dataset downloader tool reported 240 TB across 5.8 billion images. The
corpus-wide compression ratio works out to 22,508 times.

So the conclusion doesn't rest on one division alone, it's worth recalculating it two other ways.
At full precision the model weighs 7.7 GB, and that gives 3.32 bytes per picture. Against the
160 million examples the extraction paper's authors cross-checked against, it comes to 26.7
bytes, that is, a third of a line of this text — given that a 512×512 image file is never
shorter than twenty thousand bytes. Even by the most generous possible count for the "the model
stores pictures" version, it's fifteen hundred times smaller than what it trained on. A
supporting observation works well alongside this: a repository of nothing but links and
captions, with not a single picture, weighs 467 GB, and scaled up to all the pairs, around 1.18
TB — that is, the list of links weighs 275 times more than the entire model.

And now the second half, without which the first turns into advertising. Diffusion models
memorize individual images from the training data and output them during generation — this is
shown in a 2023 paper, and the methodology there is stated precisely. The researchers selected
the 350,000 most duplicated examples in the training set, generated 500 candidates for
each — 175 million images — and found 109 extracted: 94 by a formal criterion plus 13 on manual
labeling. As a share, that's 0,000062% of what was generated and 0,031% of the most duplicated
prompts.

The mechanism is named in the paper itself. Extraction succeeds most often when an image has
been duplicated in the corpus at least a hundred times; at that level of duplication, such
examples make up about one in a million training examples. The model card confirms this from the
other side: no deduplication measures were applied to the dataset, and the authors themselves
observe memorization of images duplicated in the training data.

The formulation worth carrying away has two halves, and both are mandatory. The model doesn't
store pictures: one gets 1.84 bytes, and that's physically not enough for anything. But a
picture that lands in the training set a hundred times stops being one of two billion, and it
can be pulled back out. What gets memorized is the duplicate, not the corpus. The first half
without the second is advertising; the second without the first is an accusation, and that's
exactly why, in the public argument, both sides quote one half each and are both formally
right.

The engineering conclusion from both halves at once, and it's actionable. Deduplicating the
training corpus is a measurable risk-management action, not housekeeping, and its absence in
this model is documented by the authors themselves. If you train or fine-tune a model on your
own dataset, the number of copies of one image in the set is a parameter that directly controls
the probability of it coming back out recognizably. This is a rare case where legal risk has a
numerical knob, and that knob sits in data preparation, in exactly the same place the main cost
lever sits.

And it's this architecture, not a separate topic, that leads to rights. If the machine doesn't
store or construct objects, but statistically hallucinates them out of noise, then from the
exact same architecture taken apart here it follows: it doesn't copy. And if it doesn't copy,
all that's left is the narrow channel of the trademark — that is, an artifact visible in the
output. This chain — "doesn't construct → doesn't copy → trademark only" — is the bridge to the
next slide, where a court reads it.

---
id: s42
local_id: "s42"
section: "2. Sound: Speech Synthesis, Performer Voice, and Music"
type: analitika
title: "The codec's frame rate — the main lever on length"
refrain: "the main lever is the tokenizer; model size is secondary here. Second utterance of three (s19 · s42 · s91; s62 was cut on 10/29/2026, its content is in s59a's notes)"
assertion: "The whole construction of speech and music synthesis fights to lower the codec's frame rate, because that is the only parameter that buys output length: a system holding ninety minutes of coherent dialogue runs at 7.5 hertz, another went down to 5 hertz, a third put its 12 hertz right into the model's name; the same lever as the compression ratio in images — the main lever here is the tokenizer, model size is secondary"
source: "VibeVoice; Qwen3-TTS; DiffRhythm 2; Stable Audio 2"
chapter_ref: "chapter-part2b.md §2.7"
media: ""
media_needed: "the visual content is a frequency band with output length tied to it, built at assembly time from the numbers below; no genuine photograph of this subject exists"
scheme:
  kind: shkala
  unit: "codec frames per second, hertz"
  marks:
    - {value: "5", label: "DiffRhythm 2"}
    - {value: "7.5", label: "VibeVoice", key: true}
    - {value: "12", label: "Qwen3-TTS"}
    - {value: "21.5", label: "Stable Audio 2"}
blocks_per_row: 2
blocks:
  - {label: "Ninety minutes of coherent dialogue comes from here", value: "7.5 hertz", note: "not from the generator's size. DiffRhythm 2 — 5 Hz, the lowest; Qwen3-TTS — 12 Hz right in the name; Stable Audio 2 — 21.5 against 40–150 in earlier work", key: true}
  - {label: "Converted into volume", value: "a minute of speech — 9,000 to 36,000 tokens", note: "the same minute written as text — about 200 tokens"}
timing_min: 1.1
in_bucket: false
status: собран
---

## Visible slide text

**The codec's frame rate is an architectural decision that determines output length; the counterpart of the compression ratio in video and patch size in images.**

**The main lever is the tokenizer; model size is secondary here.**

## Speaker notes

A practical conclusion follows from the codec's design, and it is mandatory for this section: the whole construction of speech and music synthesis fights to lower the codec's frame rate, because that is the only lever that buys length.

The arithmetic is direct. Tokens per second is the frame rate multiplied by the number of quantizers. A generator's context window has a fixed length; so how many seconds of sound fit into it is set by how many tokens correspond to a second. Halve the frame rate, and the possible length doubles for the same window and the same generator. Neither the model's size nor the choice of solver gives this effect.

The 2025–2026 generation reads off this parameter like a passport. VibeVoice holds ninety minutes of dialogue precisely because its tokenizer runs at 7.5 hertz. Qwen3-TTS put its 12 hertz right into the model's name: the provider judged this parameter worth naming. DiffRhythm 2 went down to 5 hertz. Stable Audio 2 runs at 21.5 hertz and pairs this with a direct explanation: unlike prior work, where latent frequencies run from 40 to 150 hertz, their autoencoder relies on a heavily reduced latent rate of 21.5 hertz, and preserving perceptual quality at low latent frequencies, in the authors' own wording, may be critical for training generative models over long temporal contexts, enabling the creation of long-form music.

Notice the shape of the claim in that last quote: the authors are not promising that a low frame rate will make the model better. They are saying that without it, long form is unreachable in principle. These are different claims, and the second is stronger.

What you pay for the reduction is also worth naming, or the lever looks free. Every frame at a lower frame rate must carry more information — otherwise the decoder reconstructs less than there was. This is compensated for by the number of quantizers, codebook width, or latent dimensionality, and all of it runs into the same trade-off measured at the codec level: cascade depth is almost free, codebook width is expensive. There is a limit, and it shows up in neighboring modalities: in video, the authors of one model pushed compression too aggressively and wrote down the result — model convergence becomes extremely difficult. There is no free compression in any of the three modalities.

A second ceiling needs to be kept alongside this lever: a generative model can never be better than its own decoder. The 32-kilohertz codec inside one well-known music model is the worst in the comparative reconstruction table: a distance of 1.82 against 0.96 for another codec and 1.19 for a third system. At a bitrate of 2.2 kilobits per second, no transformer stacked on top will recover what the decoder has already lost. The murky upper-mid range by which machine-made music is recognized by ear most often belongs to the codec, not the generator.

Hence the conclusion that recurs in every section of the lecture on its own material: the main lever is the tokenizer; model size is secondary here. In sound it is the codec's frame rate; in images, the latent patch size and the autoencoder's compression ratio; in video, the spatial compression ratio. Three modalities, three different parameters, one and the same answer.

The practical consequence for an engineer choosing a model for a task. If the task calls for a long output — coherent dialogue, a full composition, a multi-minute narration — look first at the tokenizer's frame rate, and only then at parameter count and stated quality. A model with a low frame rate and a modest generator will give you long form; a model with a huge generator and a high frame rate will not give it to you no matter how you tune it. And conversely: if the task is short — a line, a jingle, a notification — a low frame rate buys nothing, and the quality lost will stay lost.

Separately — what we do not know about the design of the two leading music products. Neither has published a paper, a technical report, or a model card, for any version. A product with tens of millions of users has not a single verifiable account of how it works. The one thing one founder said, in a podcast: their secret is in how to tokenize sound correctly. This matches the conclusion above — and the company has said nothing more about its design.

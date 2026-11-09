---
id: s41
local_id: "s41"
section: "2. Sound: Speech Synthesis, Performer Voice, and Music"
type: schema_architecture
title: "The neural audio codec and residual quantization"
assertion: "To apply the language-model apparatus to sound, you need a vocabulary, and a neural audio codec plays that role: a convolutional encoder compresses the waveform, residual quantization — a cascade of codebooks, where each next one refines the error of the one before — turns a continuous vector into a set of numbers, and a decoder reassembles the waveform; a minute of sound from a compact disc is 5,292,000 samples, the same minute in the codec is 36,000 tokens — 147 times less"
source: "SoundStream; EnCodec; MusicGen"
chapter_ref: "chapter-part2b.md §2.7"
media: ""
media_needed: "the frame's visual content is the codec's own diagram and the band comparing three units of data; a photograph would add nothing here. The six tiers were not applied: the subject of the frame is a mechanism, not a case"
arhitektura:
  blocks:
    - head: "Convolutional encoder"
      role: "input"
      lines:
        - "24,000 samples/s → a vector of 320"
        - "75 frames/s = 13.3 ms of latency"
    - head: "Residual quantization"
      role: "the work · the bottleneck"
      uzkoe: true
      lines:
        - "8 codebooks × 1,024, corrects the error"
        - "2^80 flat; 8×1,024 — a table"
    - head: "Decoder"
      role: "output"
      lines:
        - "tokens → waveform, trained end to end"
        - "a minute = 36,000 tokens, 147× less than 5,292,000 on a CD"
  vynoska:
    at: 1
    text: "depth is almost free, codebook width is expensive: 4.01 / 3.98 / 3.92 at 8 / 16 / 80 codebooks"
blocks: []
columns:
  left:
    head: "Three units of data, side by side"
    items:
      - "A language-model token: a number, vocabulary ~200k"
      - "A diffusion patch: 1024×1024 → 4096, no vocabulary"
      - "An audio token: a number from a codebook, several codebooks"
  right:
    head: "What it costs in volume"
    items:
      - "A minute from a CD: 5,292,000 samples"
      - "A codec, 8 codebooks: 36,000 tokens, 147× less"
      - "A music model, 4 codebooks: 12,000 tokens, 441× less"
      - "A minute of speech as text: ≈200 tokens, 180× cheaper"
timing_min: 1.0
in_bucket: false
status: собран
---

## Visible slide text


## Speaker notes

The same machinery runs here as in the lectures on language models, and the parallel holds up to a certain point. To apply the language-model apparatus to sound, you need a vocabulary. A neural audio codec plays that role.

The codec's design is simple: a convolutional encoder compresses the waveform, residual quantization turns a continuous vector into a set of discrete numbers, a convolutional decoder reassembles the waveform; the whole thing is trained end to end, as one piece.

The numbers worth keeping in mind come from the primary source. In SoundStream, the encoder is a convolution and four blocks with striding factors of 2, 4, 5, and 8 — meaning one embedding is computed every 320 input samples. At a sampling rate of 24 kilohertz, this gives 75 frames of latent representation per second, and one frame lasts 13.3 milliseconds — which is also the model's architectural latency. The system will never respond faster than that, no matter how many accelerators you throw at it.

The word "residual" has to be taken literally. The first codebook gives a rough approximation of the vector; what it encoded is subtracted from the vector, and the remainder is passed to the second codebook; the third encodes the error of the second. Each following level refines the one before it.

The authors calculated directly why it is built exactly this way. At six kilobits per second and 75 frames per second, one frame gets 80 bits. A single flat codebook would require two to the eightieth power vectors — a quantity they called obviously infeasible. With eight quantizers, each codebook holds two to the tenth power, that is, 1,024 vectors, which is already an ordinary table that fits in memory.

The parallel with the subword vocabulary from the language-model lecture is exact in its framing and diverges in its method: in both cases, an enormous space has to be covered without enumerating it in full. Text solves this by merging frequent pairs; sound, by a cascade of refinements.

The measured trade-off of depth against width, all measurements at six kilobits per second: eight quantizers with a codebook of 1,024 give a quality of 4.01 on the ViSQOL scale; sixteen with a codebook of 32 give 3.98; eighty single-bit quantizers give 3.92. The authors' conclusion: using a sequence of eighty single-bit quantizers leads to only a modest degradation in quality. For an engineer, this is a ready-made rule: cascade depth is almost free, codebook width is expensive.

And a scale worth saying out loud: at six kilobits per second, a codec with 8.4 million parameters runs faster than real time, by a factor of 2.4, on a single core of a smartphone processor, and at three kilobits it beats a traditional codec running at twelve. The audio tokenizer is a tiny model; what is expensive is the generator sitting on top of it.

Now the arithmetic that explains everything else in the section. Tokens per second works out to 75 multiplied by the number of quantizers: two quantizers give 150 tokens per second and 9,000 per minute; four give 300 and 18,000; eight give 600 and 36,000; thirty-two give 2,400 and 144,000. A music model has different numbers, also published: a striding factor of 640 at 32 kilohertz gives 50 frames per second, four quantizers with a codebook of 2,048 give 200 tokens per second, that is, 12,000 tokens per minute. Thirty seconds of sound is fifteen hundred generation steps.

The comparison that makes the codec make sense. A minute of sound from a compact disc is 5,292,000 samples. The same minute in an eight-quantizer codec's representation is 36,000 tokens, 147 times less; for a music model it is 12,000 tokens, 441 times less. A context window of 128 thousand tokens holds a minute and a half of raw CD sound — or 10.7 minutes of the same sound in a music model's representation. The whole point of a neural codec in generation is exactly this multiplier, and disk-space savings have nothing to do with it.

This is also where you can see why speech is more expensive than text. Speech runs at about 150 words per minute, and one text token is roughly three-quarters of a word, so a minute of speech written as text is about 200 tokens. The same minute as audio tokens, at eight quantizers, is 36,000 — 180 times more; at two quantizers it is 9,000 — 45 times more.

And the one divergence from the language model that cannot be papered over with an analogy. Text has one vocabulary. Sound had to be given two, and that has been shown by measurement. The AudioLM system introduced a split into semantic tokens, which capture long-term structure and run at 25 hertz, and acoustic tokens, which are responsible for synthesis quality and run at 600 tokens per second. Why both are needed has been measured: acoustic tokens give good reconstruction of sound and poor phonetic distinguishability; semantic tokens give the reverse. Neither works alone. One vocabulary is not enough for sound: it needs "what is being said" and "what it sounds like" kept separate, and this is the one place where the parallel with the language model honestly stops holding up.

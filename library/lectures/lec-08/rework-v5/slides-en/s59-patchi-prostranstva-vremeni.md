---
id: s59
local_id: "s59"
section: "3. Moving Image"
type: schema_architecture
title: "Spacetime Patches and Spacetime Attention"
assertion: "The developers themselves draw the parallel with the language model: where large language models have text tokens, the video model has spacetime patches; video and the image turn out to be one and the same task, and resolution and duration turn out to be the shape of the patch grid"
source: "the Sora technical report; CogVideoX"
chapter_ref: "chapter-part2d.md §3.7"
media: ""
media_needed: "visual content — a diagram of turning video into patches; a photograph explains nothing here"
arhitektura:
  blocks:
    - head: "Autoencoder"
      role: "input · bottleneck"
      uzkoe: true
      lines:
        - "compresses video into a latent"
        - "the compression ratio decides duration, resolution, token count"
    - head: "Spacetime patches"
      role: "the work"
      lines:
        - "the same unit as a text token: a vector in time"
        - "arranged into a grid of the needed size"
    - head: "Transformer"
      role: "output"
      lines:
        - "the patches work as the transformer's tokens"
        - "the output size is set by the shape of the patch grid"
blocks:
  - {label: "Video and image are one task", value: "'an image is just a video with one frame'", note: "hence training on a mix, and carrying the architecture over", key: true}
timing_min: 0.5
in_bucket: false
timing_note: "0.8 -> 0.5 + 0.3 (s59a): the diagram, a band of five plates, and two columns asked for 8.1 inches at a 5.36-inch body. Section 3's total did not change"
status: собран
---

## Visible slide text

**The parallel is exact: language models have text tokens, video has spacetime patches.**

## Speaker notes

The developers themselves draw the parallel with the language model here, and it's worth quoting them exactly: where large language models have text tokens, the video model has visual patches. The design is described in two steps: first the video is compressed into a lower-dimensional latent space, then the representation is broken into spacetime patches, and the resulting patches work as the transformer's tokens.

Three things follow from this formulation, and each is practical. First: video and the image are one and the same task, because an image is a video with one frame. Hence training on a mix of video and images, and carrying the architecture over from the previous section with no rework. Second: resolution and duration are the shape of the patch grid. In practice, the output size is set by arranging randomly initialized patches into a grid of the needed size; that's why the same model can output a landscape frame, a portrait one, and anything in between, with no separate modes. Third: the same split of "tokenizer separate, model separate" as in the image and in text.

The token arithmetic worth being able to reproduce on paper works like this. The number of latent frames is: the frame count minus one, divided by the temporal compression factor, plus one. The latent grid is the height and width, divided by the spatial compression factor and by the patch size. The token count is the product of these three quantities. The method is checked against published numbers from other work and reproduces them: for one configuration, the calculation gives 73,728 tokens against a published "about 73 thousand"; for another model on the same autoencoder, 76,032 against a published "76 thousand," and on another, 19,008 against a published "19 thousand."

The target calculation is for five seconds at 24 frames per second, that is, 121 frames, with an autoencoder compressing fourfold in time and eightfold on each spatial axis. One 1024-by-1024 image is 4,096 tokens. One high-definition frame as an image is 8,040. Five seconds in 720p is 111,600 tokens — twenty-seven times more than the image. Five seconds in 1080p is 249,240 tokens — sixty-one times more. The same five seconds frame by frame, with no temporal compression, is 972,840 tokens, and the difference, 3.9 times, is exactly the gain from temporal compression.

This has to be stated carefully. A gap of two to three orders of magnitude holds against text: five seconds of video is a hundred fifty pages, a novel and a half for five seconds. Against an image, the gap is much more modest, and inflating it would be dishonest: twenty-seven to sixty-one times, a order and a half of magnitude. Against the context window of a current language model, the gap has already closed: a quarter million tokens is smaller than a million-token window. The cost sits elsewhere: those tokens have to be run through twenty to fifty denoising steps, each with full 3D attention and no cache at all.

And one detail that connects this section to the previous one. Since May 2025, the leading video model has generated an image together with sound, with the diffusion process applied to temporal audio latents and spacetime video latents simultaneously: sound and image are denoised jointly, in one process, each in its own latent representation. No separate architecture paper with the details could be found — the model card is the ceiling of what's public here, and that has to be said out loud, leaving plausible guesses aside.

The engineering meaning of the "tokenizer separate, model separate" split is the same in this modality as in the previous two, and it's worth stating directly. Everything that determines length, resolution, and the cost of generation is decided on the autoencoder's side — that is, before the generative model itself even comes into play. Model size takes no part in these calculations, not once: not in the number of patches, not in the number of attention pairs, not in the cost of training, which comes up next. This is the same conclusion the codec's frame rate gave for sound, and it's worth checking against any new modality as the first question: what functions as the vocabulary here, and how many units of that vocabulary a minute of material costs.

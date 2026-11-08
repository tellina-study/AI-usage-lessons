---
id: s05a
type: assertion_visual
duration_min: 1.5
assertion: "3 families of generative media models: diffusion / latent video transformer / neural audio synthesis. Each — with its own fundamental limitations."
learning_goal: "Mental model of 3 architectural families → explains limits"
learning_outcomes: [LO2]
chapter_ref: "§0.1 — Three families of generative media models"
references: [ho-2020-ddpm, rombach-2022-ldm, sora-system-card-2024]
visual:
  pattern: matrix
  primary: "3-card horizontal in Ocean rounded box: diffusion (noise→reverse) / latent video transformer (latent space + temporal) / neural audio (autoregressive + diffusion)"
interaction: none
---

# 3 families of generative media models

## Assertion

3 families of generative media models: diffusion / latent video transformer / neural audio synthesis. Each — with its own fundamental limitations.

## Visual

Heading 28pt on top: "3 families of generative media models." Below it — 3 equal Ocean rounded-box columns. Column 1 "Diffusion" (mid-blue accent): an iconographic diagram — arrow "noise → reverse → image"; tools: Stable Diffusion, Midjourney, Flux, DALL-E, Imagen, Firefly; consequence: "commercial safety depends on the training corpus, not the architecture." Column 2 "Latent video transformer" (light teal): a diagram — a latent cube with a time axis; tools: Sora 2, Veo 3.1, Runway, Kling 3.0; consequence: "Sora 25-sec limit — temporal consistency degrades + cost scales linearly." Column 3 "Neural audio synthesis" (gold accent): a diagram — an autoregressive waveform; tools: Suno, Udio, ElevenLabs; consequence: "voice cloning from 1 min — fine-tuning a pretrained foundation model, not from scratch."

## Speaker notes

Before working through the industry cases, one needs to understand architecturally how exactly one generative media tool differs from another. Not at the level of marketing promises, but at the level of fundamental limitations — that is, which boundaries are dictated by the architecture itself rather than by the quality of a particular implementation. The architectural families in creative AI by 2026 group into three key classes. The first family — diffusion models. This includes Stable Diffusion, Midjourney, DALL-E, Imagen, Flux, and Adobe Firefly. Principle of operation: the model learns to reverse the process of adding noise. The engineering consequence is critical: the "commercially safe" Firefly depends not on the architecture but on the training corpus — Adobe Stock plus licensed content. Firefly's architecture is the same diffusion. What makes Firefly safe for commercial use is exactly what the model was given during training, not how exactly the model is built. This basic distinction carries through the whole chapter: questions of copyright are questions about training data and output similarity, not about the mathematics of the architecture. The second family — latent video transformers: Sora 2, Veo 3.1, Runway, Kling 3.0. Video is represented not as a sequence of pixel frames but as a sequence of tokens in a latent space. The engineering consequence: Sora 2 has a 25-second limit not because OpenAI "didn't finish the job," but because cost grows linearly with the length of the latent sequence, and temporal consistency degrades after 25 seconds. This explains why cinematic AI video in 2026 is assembled from short blocks under human direction rather than generated from one long prompt. The third family — neural audio synthesis: autoregressive for speech and songs, diffusion for music. Voice cloning is possible from one minute of audio because the model does not learn a voice from scratch — it fine-tunes a pretrained foundation model on a minimal sample of a specific speaker's voice. Without this mental model a student will not be able to qualifiedly assess the fundamental limitations of any creative AI tool — they will repeat marketing claims.

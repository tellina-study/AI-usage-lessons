---
id: s10a
type: assertion_visual
duration_min: 2
assertion: "Russian GenAI — local convenience (free, RU prompts, no VPN, rubles), but NOT frontier level in video and music. The concentration of R&D in the US/CN is structural, not ideological."
learning_goal: "Russian context: Kandinsky 6.0, Shedevrum, SymFormer, SaluteSpeech, Mintsifry bill"
learning_outcomes: [LO1, LO2, LO5]
chapter_ref: "§1.6 — Russian context"
references: [kandinsky-6-sber, sheddev-yandex, symformer-sber, cnews-mincifry]
visual:
  pattern: matrix
  primary: "Side-by-side: Kandinsky 5.0 Video sample frame vs Kling 3.0 sample frame + 4-card RU landscape (image/video/audio/legal)"
  backup: assets/backup/s10a-russian-vs-frontier.png
---

# Russian context: local convenience vs frontier

## Assertion

Russian GenAI — local convenience (free, RU prompts, no VPN, rubles), but NOT frontier level in video and music. The concentration of R&D in the US/CN is structural, not ideological.

## Visual

On top, the assertion 22pt (narrower format). On the left — a side-by-side comparison: a Kandinsky 5.0 Video sample frame (768×512, 10 sec) and a Kling 3.0 sample frame (4K, 60 fps) with a visible quality gap. On the right — 4 Ocean rounded boxes across 4 areas: Images (Kandinsky 6.0 Image MoE, free via GigaChat + YandexART 2.7 / Shedevrum hybrid 3.0); Video (Kandinsky 5.0 Video Apache 2.0 — frontier gap); Audio (Sber SymFormer, SaluteSpeech VoiceCloning, Yandex SpeechKit); Legal (Mintsifry bill 18.03.2026 — TDM exception, labeling, authorship to the prompt user, in force from 01.09.2027). Below, a gold-tint anchor: "Structural (GPU capex, video datasets), not ideological."

## Speaker notes

The Russian generative-AI landscape by 2026 is functional but not frontier across most areas. On images. Sber Kandinsky 6.0 Image was announced on April 28, 2026. Architecturally — Mixture-of-Experts. It runs, per Sber's statement, up to two times faster than previous versions. Free access via the GigaChat assistant with no generation limit. Kandinsky 5.0 Video — released November 2025, open weights under Apache 2.0, up to ten seconds at 24 fps, resolution 768 by 512. Yandex Shedevrum — YandexART 2.7 and hybrid 3.0 beta February 2026, free from Russia without a VPN. On video — a frontier gap. A direct competitor to Sora 2 Pro, Veo 3.1, Kling 3.0 by length, resolution, physics, and audio sync in Russia as of the lecture is not confirmed. The explanation is structural, not ideological: frontier video models require capex — tens of thousands of GPU-hours in a cluster — and access to large licensed video datasets. The concentration of R&D is in the US and China. This is an objective distribution of capex and data access as of 2026. On music and sound. Sber SymFormer — entry-level vs Suno v5.5; Russian "solutions" are aggregator proxies of the GPTunneL, Chad AI, GenAPI type, wrapped over the Suno API. That is, the RU audience consumes the Western frontier anyway through local wrappers. Sber SaluteSpeech YourVoice — voice cloning from several hours of audio, unlike ElevenLabs with its one minute. On legal — the Mintsifry (Russian Ministry of Digital Development) bill of March 18, 2026: a TDM exception for training, mandatory labeling of AI content, authorship to the prompt user given a creative contribution, planned entry into force — September 1, 2027. The lesson for the engineer: Russian GenAI for media in 2026 is a local convenience: free of charge, RU prompts, access without a VPN, payment in rubles. But not frontier level in video and music. Where the task is fast mass-market premium content in Russian with a guaranteed legal contour — Kandinsky and Shedevrum are competitive; where cinematic video, professional vocals are needed — the choice remains with Sora and Suno.

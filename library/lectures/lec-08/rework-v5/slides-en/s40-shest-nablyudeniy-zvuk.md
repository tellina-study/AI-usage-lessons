---
id: s40
local_id: "s40"
section: "2. Sound: Speech Synthesis, Performer Voice, and Music"
type: assertion_visual
title: "Six observations, each with a number"
assertion: "Six short cases from the section, each with a measured baseline: a restored vocal put a singer on country radio for the first time in twenty years; rights to a forty-five-year-old voice were transferred during the actor's lifetime; a model corrected a Hungarian accent in an Oscar-winning role while leaving the English speech untouched; 'Now and Then' was made with source separation and contains not a single generated note; sign-language translation runs across the UK's entire rail network; the industry wrote the norm on human contribution in 2023, ahead of the lawmaker"
source: "CNN, 05/06/2024; Variety, 2022; CBC, 2026; The Conversation, 2023; Signapse; Forbes, 06/16/2023"
media: ""
media_needed: "the frame holds six independent observations; one photograph would tie the whole frame to a single one of the six and misstate the subject. The six tiers were run for the first row (Wikimedia gives portraits of the singer, CC BY 3.0 and public domain) — the result was rejected for this reason, not for lack of material. Details — images-log.md"
blocks_per_row: 5
blocks:
  - {label: "Travis's vocal", value: "a debut at number 45", note: "11 years with no recording; 20 years off country radio", key: true}
  - {label: "Darth Vader's voice", value: "the recordings are forty-five years old", note: "rights transferred during the actor's lifetime — the point of reference for precedent ever since"}
  - {label: "The accent in The Brutalist", value: "only the Hungarian lines were touched", note: "the English untouched; the same service — 3 more nominees that season"}
  - {label: "\"Now and Then\"", value: "0 invented notes", note: "45 years from the demo to release; mixing failed in 1995"}
  - {label: "Sign-language translation on the departure boards", value: "2,500 stations", note: "the entire UK rail network; the avatars are Deaf people, paid"}
  - {label: "An industry norm got ahead of the law", value: "human contribution must be 'more than de minimis'", note: "the definition exists in a 2023 award rule; in the laws, as of 2026 — it does not"}
timing_min: 1.0
in_bucket: false
status: собран
---

## Visible slide text

**Every observation is about choosing the right tool for the task: where a recording exists, it is separated out; where it does not, it is generated.**

## Speaker notes

Three breakdowns above were carried through the full form. Below are six cases, each in two or three sentences and each with a number: a mention with no number is not placed in this section at all.

Randy Travis: the first new recording in eleven years. The country singer lost his speech after a severe stroke in 2013 — the right side paralyzed, the speech area damaged. In May 2024, the song "Where That Came From" came out: Travis's vocal was restored by a model over a 2011 recording sung by his colleague James Dupré, with the artist's own participation and consent. The baseline for the result is given twice: eleven years with no new recordings — and a debut at number 45 on the country airplay chart, Travis's first appearance on country radio in twenty years. The boundary between restoration and substitution runs, here, along who sings the source: Dupré sings it, the timbre belongs to Travis, and the question of authorship of the performance stays open.

Darth Vader's voice: rights set up during the actor's lifetime. For the 2022 series "Obi-Wan Kenobi," the Kyiv-based company Respeecher reproduced a voice recorded forty-five years earlier: James Earl Jones transferred the rights to his archival recordings, served as a mentor in tuning the result, and stepped away from the role at ninety-one; his last live performance in it was a single line in a 2019 film. The final stages of the work were carried out in Kyiv under air-raid sirens in the first weeks of the invasion. The first high-profile case where rights to a voice were set up during the person's lifetime and explicitly — every subsequent dispute refers back to it.

"The Brutalist": the Hungarian accent and the Oscar dispute. The film was shot in 34 shooting days on a budget of $9.6 million and a runtime of 215 minutes — the film's cinematographer specifically remarked that a movie does not always have to cost $200 million. Adrien Brody's and Felicity Jones's Hungarian lines, after work with a dialect coach, were run through a model together with the voice of a native speaker, sound editor Dávid Jancsó; the English speech was left untouched, and Respeecher is credited. A public dispute over whether an acting award can go to a performance with machine-assisted correction flared up around one film, even though the same service was used that same awards season by three other nominees. Brody won the Oscar for Best Actor.

"Now and Then": a song with not one generated note. This mention is load-bearing, and it has to be presented with the distinction spelled out, or a student will walk away from the lecture with the wrong idea. John Lennon's 1978 demo existed on a home cassette, where the voice was physically mixed together with piano, television noise, and mains hum. An attempt to mix the song was made in 1995 and failed: there was no way to separate the voice from the piano. In 2021, while working on the documentary series "Get Back," WingNut Films built a machine source-separation system, and in November 2023 the song came out — forty-five years after the demo was recorded. The difference from generation sits in how the task is framed: in source separation, the mix is treated as a sum of tracks, and the model is trained to minimize reconstruction error against an isolated track that exists as a ground truth. Generation has no ground truth by definition. Where what was recorded is physically present in the signal, it is retrieved, not invented.

Signapse: sign language, from the lab to the station departure boards. Photorealistic translation of written text into British and American sign language runs, as of mid-2025, at 2,500 stations across the UK — that is, across the entire national rail network — and at major US airports. Travel announcements reach Deaf passengers at the moment they are made. The setup matters ethically: the digital "signers" are built from footage of real Deaf people, who receive royalties. Alongside it is the five-year, £8.45 million SignGPT project, announced in January 2025, with the world's largest sign-language corpus. The second half of the story is mandatory: the Deaf community debates the displacement of live interpreters and the fact that an avatar does not convey facial expression, which functions as grammar in sign languages; published scholarly criticism of this exists.

The 2023 Grammy rules: the industry wrote the norm first. In June 2023, the Recording Academy stated: only a human can receive the award; work with no human authorship is not admitted to any category; work with machine elements is admitted if the human contribution to the music or lyrics is meaningful and more than de minimis. The latter is defined — "so minimal that it can be disregarded" — and that is exactly what is missing from any law as of 2026. The criterion is ready-made and useful for an engineer: the question to ask is what, specifically, a human did — and that question replaces "was AI used."

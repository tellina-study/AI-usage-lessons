---
id: s38
local_id: "s38"
section: "2. Sound: Speech Synthesis, Performer Voice, and Music"
type: analitika
title: "Breakdown: dubbing and localization"
grafa: "b, bordering on (a) — the first mode is counted in the same unit, the second has no number of its own"
assertion: "A finished minute from a live voice talent costs $50 to $450, from synthesis — $0.03 to $0.072, the unit is one and the same and the gap runs from seven hundred to fifteen thousand times; the first classical mode is counted in full, the second — subtitles — is named and has no rate per minute of its own, which is why the breakdown sits on the border between two columns; the cheap model saves on text normalization, which the client notices last"
source: "GVAA Rate Guide 2026; ElevenLabs and Gemini price lists, read 10/27/2026"
chapter_ref: "chapter-part2.md §2.4"
media: ""
media_needed: "the shot assets/screenshots/s38-dubbing-session.jpg has been acquired and sits in assets, but there is no room for it on this frame: the plate band and the two columns fill the body entirely, and a side column would cut the columns down to unreadable. Bring it back once the frame is unloaded."
media_note: "a dubbing session: an actor at the microphone, a director, and the translated script. Wikimedia Commons, public domain; provenance — images-log.md"
blocks_per_row: 5
blocks:
  - {label: "The cost of a recording error", value: "$50–450 + $650–6,500 on top", note: "re-recording after delivery means re-assembling the voice talent"}
  - {label: "Mode 1 — live voice talent", value: "$50–450/minute", note: "by experience: $50–150 beginner, from $350 senior"}
  - {label: "Mode 2 — subtitles", value: "no rate per minute", note: "the mode is named, has no number"}
  - {label: "Model", value: "$0.03–0.072/minute", note: "per 1,000 characters: $0.04 · 0.08 · 0.03 — fast, quality, third provider"}
  - {label: "The gap", value: "700–15,000 times", note: "from the classical mode, not from zero", key: true}
columns:
  left:
    head: "What the model closed"
    items:
      - "Carrying the language with the timbre — a button in the browser"
      - "70+ languages; intonation — set by tags in the text"
      - "Over a quarter of views are not in the primary language (channel count undisclosed)"
  right:
    head: "What is left to the human"
    items:
      - "Timing adaptation: fitting the translation into the line's duration (isochrony)"
      - "Emotion not from text — set by markup"
      - "Lip sync — a separate model, not dubbing"
      - "The cost of 'did not localize': no number anywhere"
timing_min: 1.0
in_bucket: false
status: собран
---

## Visible slide text


## Speaker notes

The most countable breakdown of the section: here both sides are named in one unit, and the gap between them is measured in the thousands.

The cost of the error "recorded and it did not fit" is named in full: the session cost, $50 to $450 for a finished minute, plus broadcast rights separately — from $650 for a national ad, $3,200–3,500 for a year of national airplay, up to $6,500 for a perpetual buyout. Rewriting a line after delivery means reassembling the voice talent. The cost of the opposite error, "did not localize," is not given a number by any source in the sample. The closest proxy measures attention, and its unit has to be named precisely, because it gets swapped out in retellings. The platform reported: for creators who uploaded multilingual tracks, over twenty-five percent of view time went to views not in the video's primary language. The unit here is view time; the share of viewers has never been counted this way. The platform's own wording is "not primary for this clip"; the word "non-English" appears only in retellings. The denominator: the view time of the channels that uploaded the tracks; how many channels that is, the platform did not disclose — the pilot is called small, and three creators are known by name from it. Lost revenue behind that share has never been counted by anyone.

The first classical mode — a live voice talent — is counted in the same unit as the model: dollars per finished minute, $50–450 by experience segment. Next to it sits the union rate for a digital replica, $956.75 for a four-hour consent session plus 16.5 percent into union funds, and a one-and-a-half times rate when the copy is used in advertising — a price the industry set on copying a voice by its own hand.

The second classical mode — subtitles — is named and has no number of its own: no rate for subtitling and timing per minute of finished material appears in the sample, even though that figure is public within the localization industry. An audiobook rate exists — $150–250 per hour of work for a beginner, $500–1,000 and up for the top — but it lives in a different unit and does not fold into the same accounting. Hence the breakdown's borderline position between two columns: the first mode is counted in full, the second is named with no number.

Price lists were read directly on October 27, 2026. The fast model — $0.04 per thousand characters, about $0.036 per minute of speech; the quality model — $0.08 per thousand characters, about $0.072 per minute; at a third provider, a minute of speech costs $0.03, or $0.015 in bulk. The "characters to minutes" conversion is done at a rate of nine hundred characters per minute of speech and is named as a calculation, not a measurement. The bottom line: $0.03 to $0.072 per minute against $50–450 for a voice talent — a gap of seven hundred to fifteen thousand times. This is one of the largest distances in the whole lecture, and it is counted from the classical mode — there was no need to count it from zero.

How this works. Input is text plus a voice sample, output is an audio track. Sound is turned into audio tokens by a neural codec with residual quantization, and from there the same machinery runs as in a language model. This is covered in detail in the section's technical block; here, one quantity matters, and it explains both the price and the length — the codec's frame rate. The product names are given on the frame and in the source: one provider's fast and quality lines, publicly available since February 2026, with intonation marked by tags right in the text and support for over seventy languages; a separate speech-synthesis provider; and, for visual dubbing, where the lips in the frame are rewritten, its own dedicated system.

A measured speed-versus-correctness trade-off is named by the provider itself, and it is telling. A phrase with a figure in the millions of dollars is read by the quality model as "one million dollars," and by the fast model as "one thousand thousand dollars," because the fast model is substantially smaller, generalizes worse, and has text normalization turned off by default for the sake of low latency. The cheap model saves exactly on what the client notices last and fixes at the highest cost: this kind of error is caught at final review of the finished clip.

A textbook case of swapping the baseline, worth taking apart on its own because it recurs in every modality. The model's stated inference latency is 75–100 milliseconds; real time to first sound in a working system is 100–200 milliseconds and higher; a player buffer is typically 500 milliseconds. The buffer outweighs the whole difference between providers. Providers measure at different points in the pipeline, and comparing their numbers directly is exactly the class of error the course catches in every lecture.

What the training data is: for the music models from the same provider — on fully licensed data, under an agreement with a major rights holder; for the speech models, the training set's composition is undisclosed.

What moved. The product's boundary moved: voice-over stopped being a session and became a line item on a rate card. The client lost the need to plan around a voice talent's schedule, and the voice talent lost a substantial share of short bookings. The right to one's voice moved to the right, and an honest zero hangs there: the Russian Civil Code has no separate protection for voice, a draft of the corresponding article was not supported by the government, while in the US, laws in individual states are in force. This gap is examined in this same section's layer on rights.

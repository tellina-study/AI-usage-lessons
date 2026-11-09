---
id: s45
local_id: "s45"
section: "2. Sound: Speech Synthesis, Performer Voice, and Music"
type: assertion_visual
title: "The model has no concept of a performer"
assertion: "A voice model reproduces a sound, and that is where its knowledge of the person ends: there is no entity 'performer' inside it with a manner, a repertoire, range limits, and a decision about how to deliver a line — there is a distribution, conditioned on a sample; four observable consequences follow from this, named by the providers themselves, and a ready-made boundary of applicability — the model works where something needs to be spoken, and stops working where something needs to be performed"
source: "ElevenLabs documentation; F5-TTS; Stable Audio 2"
chapter_ref: "chapter-part2b.md §2.8"
media: ""
media_needed: "the visual content is two columns, 'what is reproduced / what is not reproduced,' and a boundary between two verbs; a photograph of a performer here would substitute a different subject for the one the frame exists for — the absence of a performer inside the model"
scheme:
  kind: dorozhki
  caption: "The root is in the data: the training corpus was assembled from audiobooks"
  entry: "a voice sample"
  exit: "to speak — yes; to perform — no"
  rows:
    - {label: "Sound", steps: ["a distribution, conditioned on the sample", "timbre is reproduced in full"]}
    - {label: "Performer", empty: "manner · repertoire · range limits · breath · a decision on delivery — none of this is inside"}
columns:
  left:
    head: "Four consequences, named by the providers"
    items:
      - "A clone from calm narration does not carry emotion"
      - "Developers: 'lacks fine control of the details'"
      - "A vocal — a melody with no words, a form with no content"
      - "Cloning of singing is not supported"
  right:
    head: "What it means for tasks where recognizability is what is paid for"
    items:
      - "Timbre is recognized; recognizability of a performance — no"
      - "Emotion is manual markup; control exists within its limits"
      - "A defect like pseudo-letters in an image: no content"
      - "Acceptance by 'close enough' does not work — it will always be close"
timing_min: 0.8
in_bucket: true
status: собран
---

## Visible slide text

**A voice model reproduces a sound; that is where its knowledge of the person ends. The root is in the training data, and the providers name it themselves.**

## Speaker notes

This limitation is a property of the method, not a shortcoming of a particular provider, and it is not fixed by a version update. It has to be stated precisely, because the everyday "sometimes it sounds unnatural" does not describe the actual problem.

A voice model reproduces a sound, and that is where its knowledge of the person ends. There is no entity "performer" inside it, with a manner, a repertoire, range limits, breathing habits, and a decision about how to deliver a line. There is a distribution, conditioned on a sample: the system has learned the statistical structure of this voice's sound and can generate a similar-sounding one. Everything a performer decides beyond the sound is simply not encoded in this representation.

The consequences are observable and named by the providers themselves, so there is no need to take critics' word for it here. First: a voice cloned from calm narration sounds different when asked to express a strong emotion — because there was no strong emotion in the sample, and the model cannot derive one from the text. Second: developers of speech-synthesis systems themselves write that their systems lack fine control over paralinguistic detail, such as emotion, and the industry's answer to this is manual markup — square brackets with instructions right in the text. Control exists exactly to the extent you have marked it up; there is no understanding of meaning in the system from which intonation would follow on its own.

The root of the problem is in the data, and it has been named since as far back as 2023: the main training corpus was assembled from audiobooks, where the overwhelming majority of utterances are delivered in a reader's manner. The model has seen an ocean of even-toned narration and very little of everything else, so even-toned narration comes out well, and everything else has to be marked up by hand.

The third consequence applies to music, and it is stated more bluntly: when a music model is asked for vocals, its generations contain melodies that resemble vocals with no intelligible words. This is the same class of defect as pseudo-letters in a generated image: the form is reproduced, the content is absent. It is useful to keep these two cases side by side — they come from different modalities, but the ailment is one, and so is the cause: the model optimizes for plausibility of form, not for the presence of meaning.

A fourth consequence, product-level: professional voice cloning does not support singing, as the provider states in its own documentation. This is a direct answer to the question asked most often, and the answer is no.

From here follows an engineering conclusion that carries over to any task: a voice model is fit for where something needs to be spoken, and stops being fit for where something needs to be performed. The boundary runs between these two verbs, and that is exactly what needs to be checked. A navigation prompt, a station announcement, an informational recording, a reference narration — speak. A role, a song, an ad read where the intonation is the product itself — perform.

For tasks where recognizability itself is what is being paid for, this has a direct consequence. Timbre is recognized, and timbre is what the model reproduces; recognizability of a performance is not covered by timbre, and that is exactly what makes hiring a performer expensive. The listener will tell the voice apart but will not be able to say exactly what is missing — and acceptance on the "sounds like them" principle stops working, because it will always sound like them. The one acceptance test that actually works here is checking whether the result does the job the performer was hired to do.

And one last thing worth remembering when planning. These four consequences will not close with the next model version, because not one of them is a training error: they follow from what the model takes as input and what it optimizes. They can only close with a change in how the task is framed — for example, if training comes to include markup of an actor's choices, not just the sound. Until such a corpus exists, planning has to assume the boundary between the two verbs stays exactly where it is.

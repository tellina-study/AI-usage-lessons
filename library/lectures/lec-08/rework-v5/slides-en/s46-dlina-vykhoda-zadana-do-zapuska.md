---
id: s46
local_id: "s46"
section: "2. Sound: Speech Synthesis, Performer Voice, and Music"
type: assertion_visual
title: "Output length is set before launch: you cannot stop early"
assertion: "A language model decides when to stop as it goes — it outputs an end-of-sequence token, and the length of the answer is a result of generation; a diffusion model produces a fixed-shape tensor, and output length is a launch parameter, so you cannot ask it to 'play until the idea runs out,' cannot interrupt it halfway and get a meaningful short result, cannot generate 'about a minute'; workarounds exist, and each pays its own price"
source: ""
chapter_ref: "chapter-part2b.md §2.8; §2.7"
media: ""
media_needed: "the visual content is a diagram of 'what the model decides and what the launch decides' plus a band of workarounds with their cost; a photograph does not fit this subject"
scheme:
  caption: "Who decides on the length"
  arrows: true
  rows:
    - {label: "A language model", steps: ["length is not set", "generation runs", "it outputs an end token", "length is the result"]}
    - {label: "Diffusion (sound)", steps: ["length is set as a number", "a tensor of that shape", "there is nothing to stop it with", "length is a parameter"]}
blocks:
  - {label: "What you cannot ask for", value: "\"play until the idea runs out\"", note: "you have to name the number of seconds", key: true}
  - {label: "Workaround 1: duration conditioning", value: "paid for with an empty window", note: "a 95 s window; silence in the tail is still counted"}
  - {label: "Workaround 2: continuation in fragments", value: "paid for with structure", note: "only the last chunk goes into the context; for one model that is 12 seconds"}
  - {label: "Why the chorus does not come back", value: "there is no reference to the past", note: "a window holding the whole composition — the repeat happens on its own"}
timing_min: 0.7
in_bucket: true
status: собран
---

## Visible slide text


## Speaker notes

A second limitation of the method follows directly from the design of the codec and the generator, and it will recur in every following section of the lecture, on its own material.

A language model decides when to stop as it goes: it outputs an end-of-sequence token, and the length of the answer is a result of generation. A diffusion model produces a fixed-shape tensor, and output length is set by a launch parameter. This difference is architectural, and no setting removes it.

What follows from this in practice. You cannot ask for "play until the idea runs out." You cannot interrupt generation halfway and get a meaningful short result: you get a fragment, cut off wherever it was cut off. You cannot generate "about a minute" — you have to name a number. For an editor, this means restructuring the work: duration is planned before launch, not adjusted as you go, and material for editing is ordered with slack that is trimmed afterward.

Workarounds exist and are documented. The first is duration conditioning: when a training fragment is taken, the second it starts at and the total length of the source file are recorded, both numbers are turned into learned embeddings and fed in alongside the text; in production, the user sets the length, and the model, always producing a 95-second window, is trained to fill the tail with silence from the specified point on, after which the silence is trimmed. The second is continuation of the next fragment by an extension function. Each workaround pays its own price: filling with silence spends computation on an empty window, and continuation by fragments breaks structure, because only the last chunk carries over into the context.

This is also the technical cause of the well-known complaint about machine-made music. A chorus that never comes back, and a melody stuck in a loop, have been measured: for one well-known model, continuation carries twelve seconds of previous sound into the context, and the model is physically unable to refer to anything from a minute earlier. For a model with a low latent frame rate that holds the whole composition in one window, a repeated motif appears on its own — with no special work on "musicality" at all. In other words, musical form here is a consequence of whether the piece fits into the window whole, and that is exactly the same lever examined one frame earlier.

A separate ceiling deserves naming: it is audible, and it has nothing to do with the generator. A generative model can never be better than its own decoder. The codec inside one well-known music model is the worst in the comparative reconstruction table: a distance of 1.82 against 0.96 for another codec and 1.19 for a third system. The limit is hard: at a bitrate of 2.2 kilobits per second, no transformer stacked on top will recover what the decoder has already lost. The murky upper-mid range by which machine-made music is recognized by ear most often belongs to the codec.

An engineering conclusion worth carrying away. If the task calls for an output of unknown length in advance — a line that ends where the thought ends, a musical phrase that resolves on its own — a diffusion model for sound is not the right tool, and this has to be worked around from the outside: cutting, editing, a separate stop logic. If the length is known in advance and fixed, the limitation costs you nothing. This is the same kind of criterion as the boundary between "speak" and "perform": it can be checked before launch, from how the task is framed, rather than after the result is delivered.

It helps to understand where this difference comes from rather than memorize it as a fact. A language model generates a sequence one element at a time, and it chooses each next element by looking at what has already been generated; among the possible elements is an end-of-sequence marker, and the probability of choosing it grows as the utterance becomes complete. Length, then, is a result of the same process that generates the content. A diffusion model works differently: it starts from a field of noise of a given size and gradually turns it into a coherent signal, and the field's size is set at the moment the noise is created — that is, before the first step. There is no place in this process where the model could decide "this is enough" — every element of the field is processed at every step, simultaneously.

This also explains why the workarounds are built exactly the way they are, and why each is only half a solution. Duration conditioning teaches the model to put silence in the tail — meaning the length is still set, only part of the output has been declared unnecessary. Continuation by fragments splits a long output into a sequence of short ones, and inside each one the limitation holds in full, while the connection between them is lost. A third path, currently in development, is to assign each element of the field its own noise level, so that part of the field can keep being filled in while another part is already finished. This combines the variable length natural to sequential generation with the controllability of diffusion, but it is not yet standard in products at scale.

What this means when choosing a tool for a specific job. A fixed-length service recording, a thirty-second jingle, a voice-over timed to a finished edit — the limitation costs nothing, the length is already set by the client. A book narration with chapters of different lengths — the limitation costs you cutting and splicing, that is, human editing time. A musical bed that has to end exactly on a line — the limitation costs separate work, because the model cannot finish a phrase, it can only stop at an assigned point. The difference between the second and third case matters: in the second, trimming is enough; in the third, a trim sounds cut off.

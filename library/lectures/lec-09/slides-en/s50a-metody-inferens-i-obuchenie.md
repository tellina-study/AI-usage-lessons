---
id: s50a
local_id: s4-01-2
section: "4. Space for AI"
type: norm
title: "Why it's inference, not training, that moves to space"
assertion: "What moves to space is a finished, already-trained network; training itself needs a cluster and stays on Earth"
source: "—"
media: ""
media_needed: "No image — a comparison of two engineering processes, not a physical object. Phase 9 (issue #317)."
columns:
  left: {label: "Training — why it stays on Earth", items: ["Thousands of accelerators compute one model and synchronize at every step", "Every step changes the model's weights in their entirety, and the copies cannot be allowed to diverge", "Power and networking are sized for the whole cluster at once, not for a single chip"]}
  right: {label: "Inference — why we move it to orbit", items: ["One pass of the finished network from input to answer, nobody touches the weights", "A neighboring accelerator for step-by-step synchronization isn't needed at all", "Starcloud-1 — a single H100 chip answers requests to the Gemma model"]}
in_bucket: false
status: draft
---

## Visible slide text

**The difference isn't in what's being computed, but in how many accelerators have to talk to each other at every step.** Training needs thousands; inference needs one or a few, with no constant cross-checking between them.

**On Starcloud-1, the Gemma model's weights don't change by a single step.** The chip runs a finished network — it doesn't train a new one.

## Speaker notes

The previous slide called orbital computing a reversal of the whole lecture's logic — but it didn't explain why it's specifically language-model inference that can physically be moved to a satellite, and not training the same model. The difference is an engineering one, not a quantitative one: it isn't that training is "harder" in the sense of more computation for the same question — it's that the two processes are built differently.

Training a neural network is a repeating process: every pass of data through the network ends with computing an error and adjusting the weights, and that adjustment has to be applied consistently, all at once, to every copy of the model computing in parallel across different accelerators. For thousands of accelerators to train the same model, they have to exchange results literally at every training step — otherwise their copies of the model diverge and end up training, in effect, different networks. This constant cross-checking between accelerators is exactly what requires a cluster — not just a lot of chips, but chips physically connected by a high-bandwidth network to each other, the way the internal network of servers inside one Earth-based data center works. That's exactly the kind of cluster that holds the training of this same chapter's weather-forecasting models — separate nodes, each with several H100 processors, wired to each other, not scattered apart.

Inference is a fundamentally different kind of task in form. The network is already trained, its weights are fixed, and the only thing that happens is a single pass of the input data through the finished network, from start to end, with no error computed and no weight adjustment afterward. Inference doesn't need a neighboring accelerator to cross-check with at every step at all: a single chip, handed a request, can carry it through to an answer on its own. That's exactly why the inference task isn't tied to any particular point in space — it doesn't need a data center's internal network; it only needs power, cooling, and a communication channel for the request and the answer themselves.

Starcloud-1 is this difference in its purest form: a single Nvidia H100 chip in orbit runs inference on the already-finished open Gemma model, answering real requests, and not a single weight of that model changes on board. Training that same Gemma — with a cluster of accelerators exchanging data at every step — stays on Earth; the orbital satellite doesn't take on that work and doesn't demonstrate it.

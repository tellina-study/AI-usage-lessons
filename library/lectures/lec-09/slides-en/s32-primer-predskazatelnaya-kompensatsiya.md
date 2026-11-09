---
id: s32
local_id: s2-05
section: "2. Teleoperation"
type: case_study
title: "Example: predictive latency compensation"
assertion: "The model predicts the picture by the amount of the delay and reduces task time by up to 26% — but a human still makes the decisions"
source: "[Frontiers in Space Technologies 10.3389/frspt.2026.1920649](https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2026.1920649/xml) · [ScienceDirect S1526149226000639](https://www.sciencedirect.com/org/science/article/pii/S1526149226000639)"
media: "assets/razdel-2/latency-compensation/08-INFOGRAPHIC-lstm-delay-compensation-architecture.png"
media_needed: "already downloaded (Tier 1). Infographic of the LSTM compensation architecture. A hero scale was tried (issue #317, task A) — the same structural conflict as `s31`/`s42`/`s44` (see their `media_needed`): hero narrows this slide's plate column below the working width of `PLATES`, and the blocking `[width]`/`[height]` do not go away even at a target below the 40% hero threshold. The previous side size is kept."
graf: "b"
blocks:
  - {label: "Cost of over-caution", value: "slow, often-stalling work", note: "the operator waits to make sure the picture has 'caught up' with reality"}
  - {label: "Cost of risk", value: "acting on a stale picture", note: "correcting an already-made move in jerky steps"}
  - {label: "Classical mode", value: "extrapolation at constant speed", note: "works while motion is uniform; errs on sharp changes"}
  - {label: "Model (LSTM / TCN)", value: "reduces task time by up to 26%", note: "lunar analog facilities — a research stage, not routine practice", key: true}
in_bucket: true
status: draft
---

## Visible slide text

**Honest status: a research stage, not deployed practice.** Tests are at lunar analog facilities, not on a real mission; the lunar analog is confirmed by a single journal source, not a series of independent repetitions.

*Prediction on video — the first appearance of the "video" modality in the lecture's grid.*

## Speaker notes

At high communication delay, the operator either over-compensates — moving slowly, stopping often to make sure the visible picture has caught up with reality — or takes the risk of acting on an already-stale picture. Both strategies pay in task time.

Classical mode (column b): simple extrapolation at constant speed — the system assumes the object will keep moving the same way and completes the picture by the amount of the delay. Works as long as motion is actually uniform, and errs the more sharply the scene changes.

Model: a research direction from 2026, several independent publications, including tests at lunar analog facilities. The trained model — a recurrent LSTM network or a temporal convolutional network (TCN) — predicts the scene's future state forward in time by the amount of the delay and overlays the prediction on the operator's video feed in real time. The measured effect in one publication is a reduction in task completion time of up to 26% at high delay compared with ordinary video.

It's worth stating the status honestly: this is a research stage, not deployed practice. Most publications on this technique are general robotics and telemedicine, not specifically lunar testing; the lunar analog is confirmed by one specific journal source. The sources describe no formal threshold or arbitration mechanism: the operator remains the one who makes all the decisions, the model only affects what they see. What moved over: the burden on the operator's own perception moved to the model, which performs the compensation computationally. Three selection conditions: remove the model and the operator reverts to raw video or linear extrapolation, so the change is directly caused by the model; the subject is industrial; column b — the effect is named with a number, but it is one publication, not statistics across many trials: the confirmation here is weaker than for Dragon or Astrobee, where the effect is verified by routine operation.

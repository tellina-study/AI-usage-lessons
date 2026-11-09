---
id: s30a
local_id: s2-03a-2
section: "2. Teleoperation"
type: schema_layered
title: "How predictive latency compensation is built"
assertion: "A trained model predicts the picture forward by the amount of the delay and changes what the operator sees — not what they decide"
source: "—"
media: "assets/razdel-2/latency-compensation/08-INFOGRAPHIC-lstm-delay-compensation-architecture.png"
media_needed: "already downloaded (Tier 1), the same file used in this section's case-study breakdown — a different role there: there, status and effect; here, the mechanism's design."
arhitektura:
  blocks:
    - head: "Input: delayed stream"
      role: "input"
      lines:
        - "video and recent history of the scene's motion from the remote site"
        - "the frame is already stale by the amount of the communication delay"
    - head: "LSTM or temporal convolutional network"
      role: "work"
      lines:
        - "the LSTM steps through frames one at a time and keeps a memory"
        - "the TCN looks at a window of past frames at once, without memory"
        - "trained on recorded past sessions of scene motion"
    - head: "Output: frame for the operator"
      role: "output · honest gap"
      uzkoe: true
      lines:
        - "the predicted, corrected frame replaces the raw video on the screen"
        - "the sources name no formal threshold for checking the prediction"
in_bucket: false
status: draft
---

## Visible slide text

**Changes what the operator sees, not what they decide.** Neither the controller nor the warm start is involved here — all movement commands stay with the human.

**An honest gap.** The sources name no formal threshold for checking the prediction before it is shown.

## Speaker notes

The breakdown of the controller and the warm start named predictive latency compensation as a third, separate mechanism — but did not explain how it is built inside. This slide closes exactly that gap, mechanically, before moving on to assessing its effect and its honest status in a separate case study.

The input is a video feed and the recent history of the scene's or object's motion from the remote site; by the time this stream reaches the operator, the communication delay has already passed, and the frame shown lags reality by that amount. Two variants of the trained model solve the same task — predicting how the scene will change going forward in time — but read the history differently. The recurrent LSTM network processes frames in order, one after another, and at each step updates an internal memory that carries information from the distant past into the current moment. The temporal convolutional network (TCN) is built differently: it does not keep a step-by-step memory, but applies a convolution at once over a whole window of recent frames — the same way an ordinary convolution over an image looks at once at a pixel's neighborhood, except here the neighborhood is stretched in time rather than in space. Both architectures are trained on recorded past sessions of scene motion — not specifically on lunar data; the sources do not detail the makeup of the training set for the lunar analog separately.

The output is the predicted frame, corrected for the delay, which the operator sees on their console instead of the raw, delayed video. This is where this mechanism's honest gap stands: the sources name no formal threshold or check at which the model's prediction would be confirmed or rejected before being shown — the operator simply sees the corrected picture and trusts it directly.

The key difference from the other two mechanisms in the same section is not that a trained model replaces the classical approach, but WHAT exactly it changes. The controller and the warm start change the movement command — what the system or operator ultimately does. Predictive latency compensation does not touch the command at all: the operator still decides where to move and still issues every command — only the image in front of their eyes changes, the material on which they base their decision.

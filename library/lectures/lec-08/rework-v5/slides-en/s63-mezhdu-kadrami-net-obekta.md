---
id: s63
local_id: "s63"
section: "3. Moving Image"
type: schema_architecture
title: "There Is No Object Between Frames That Stays 'the Same'"
assertion: "Consistency of a character, their clothing, and an object in their hand is the result of four mechanisms at work, and each one is finite: the shared latent runs out at the edge of the compression window, full 3D attention runs out at the length of the clip, and positional encoding tells the model where an element sits, not that it's the same element"
source: "the Sora technical report; CogVideoX"
chapter_ref: "chapter-part2d.md §3.8"
media: ""
media_needed: "visual content — the diagram of the four mechanisms itself; a photograph explains nothing here"
scheme_note: "the fourth mechanism (conditioning on the first frame) was removed from the diagram: the canon forbids more than three rows, and a fourth row would have pushed the diagram into the slide's basement. The mechanism stays on the slide as the plate 'start with a frame' on s63a and is broken down in full in the notes"
scheme:
  caption: "What holds object consistency together, and where each mechanism runs out"
  arrows: false
  rows:
    - {label: "1. The shared compression latent", steps: ["Four neighboring frames are compressed into one latent slice", "They don't exist separately", "Flicker reduced from 93.2 to 86.3"]}
    - {label: "2. Full 3D attention", steps: ["The only mechanism with a direct 'object here ↔ object there' link", "The cost is counted: thirtyfold"]}
    - {label: "3. Positional encoding", steps: ["The coordinate is triple", "Channels are split between axes in a fixed proportion"]}
timing_min: 0.8
in_bucket: true
timing_note: "1.5 -> 0.8 + 0.7 (s63a): the diagram of three mechanisms and a band of four plates asked for 7.3 inches at a 5.36-inch body. Section 3's total did not change"
status: собран
---

## Visible slide text

**Inside the model there is no entity called "object" that persists between frames: character consistency is the result of four mechanisms at work, and each one is finite.**

## Speaker notes

This is the modality's main limitation, and it has to be stated exactly this way. Inside the model there is no entity called "object" that persists between frames. Consistency of a character, their clothing, and an object in their hand rests on four mechanisms, and each one is finite.

Mechanism one: the shared latent with temporal compression. Four neighboring frames are physically folded into one latent slice, so they don't exist separately and have nowhere to diverge to. The measured effect — flicker reduced from 93.2 to 86.3. It runs out exactly where the compression window runs out: between neighboring slices, that kind of connection no longer exists.

Mechanism two: full 3D attention — the only one that gives a direct "object here — object there" link across a large displacement. Its cost is counted: thirtyfold by number of attention pairs. It runs out at the length of clip that attention can still hold.

Mechanism three: positional encoding across three axes — the same trick as in a language model, but the coordinate is now triple, and the channels are split between axes in a fixed proportion. It runs out at the simple fact that this encoding tells the model where an element sits, not that it's the same element.

Mechanism four: conditioning on the first frame. The technique is described precisely: the conditioning image is concatenated with frames filled with zeros, and a binary mask is introduced, where a one marks a frame to keep and a zero marks one to be generated. In other words, the task is reframed as filling in what's missing across time. From this comes a practical tip worth taking away: if you need predictability, start with a frame and leave the description for the second step — half the uncertainty disappears with one real frame.

Why this is worth describing as mechanisms rather than as the one phrase "sometimes the jacket changes." The phrase describes a symptom and implies the defect is random and curable by regenerating. The list of mechanisms describes the cause and immediately states where each one's boundary is: the temporal-compression window, the length of clip full 3D attention can hold, and the fact that positional encoding answers the question "where," not "is this the same one." Knowing the boundaries, you can tell in advance which framing of the task will land inside them and which will fall outside — and not spend attempts where they'll be wasted.

The fourth mechanism, conditioning on the first frame, stands apart in this list, and that's why it's been pulled off this diagram. The other three work inside the model and are invisible to the user; the fourth is something the user does themselves, by feeding a finished frame into the input instead of a description. The technique is described precisely: the conditioning image is concatenated with frames filled with zeros, and a binary mask is introduced, where a one marks a frame to keep and a zero marks one to be generated, reframing the task as filling in what's missing across time. The practical conclusion from this — the one setting in the whole section available from the outside, and free of charge: if you need predictability, start with a frame and leave the description for the second step.

The order to read the diagram in: top to bottom, the mechanisms go from the cheapest and shortest-ranged to the most expensive. The shared latent is free, but it only holds four neighboring frames. Full 3D attention holds the whole clip, but costs thirtyfold. Positional encoding costs almost nothing and holds nothing — it only lays out coordinates. Altogether it's enough for a clip of a few seconds and not enough for anything longer. The whole family is built this way, and this isn't an oversight in one particular model.

One clarification about the word "mechanism." None of the three was designed as a way to hold an object together: temporal compression was introduced for volume, 3D attention for quality, positional encoding so that the model would tell order apart at all. Object consistency came out of them as a side effect, and that's exactly why it runs out so easily: nobody is responsible for it by design. It's worth remembering this whenever a system is asked for a property its own task specification never included.

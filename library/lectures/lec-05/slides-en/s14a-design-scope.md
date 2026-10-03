---
id: s14a
type: assertion_visual
section: "Section 2. Design"
duration_min: 1.5
assertion: "Design in this phase settles the whole of a person's work with the system: the surfaces and touchpoints (screen, voice, notification, email, refusal, silence), the system's behaviour over time, and its answer when it is unsure"
learning_goal: "The opening caveat of Section 2: the scope of the word \"design\" here is wider than drawing screens; the set of surfaces and touchpoints and the three decisions about behaviour are named before the section goes into method"
learning_outcomes: [LO1, LO3]
chapter_ref: "§2.1, §2.7"
interaction: none
protected: true
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  assertion_visual, three tiers. The top one is a teal panel about the scope of the word.
  The middle one is six labelled tiles of surfaces and touchpoints in a row, each with a
  Lucide icon (monitor-smartphone, headphones, siren, file-text, shield-off, clock) and one
  line about the decision taken right there. The bottom tier is three lines of behaviour
  over time (sure / unsure / wrong) with the icons circle-check, circle-help, undo-2. At the
  bottom a gold panel about the decisions that outlive layout. No memes: the slide sets the
  frame of the section.
note: >
  issue #212, owner remark R3-2026-10-01: "in the design section we need a slide and the
  caveats that this is not only about interface design — the whole of what working with the
  system looks like for a person, its touchpoints and surfaces, its behaviour". The slide is
  placed first in the section (after the divider, before the base slide), so that the Double
  Diamond and the design system are read wider than the screen. The caveat is continued on
  s15 (both diamonds run across the whole encounter), s17 (the generator covers the screen),
  s17a (the machine check covers the numeric part) and s18 (three presentation techniques —
  decisions about behaviour). The gold panel here works as the run-up to the section's
  failure: the product's name sets the picture of the system in a person's head before the
  first screen does. The new text is written without the contrastive "not X, but Y"
  construction (tools/editorial/README.md §1).
---

# Visible content

## Title bar
Design here is the whole of a person's work with the system: surfaces and touchpoints, behaviour, the answer when unsure

## Body
[the scope of the word → six surfaces and touchpoints → behaviour over time → the decisions that outlive layout]

[Teal panel — THE SCOPE OF THE WORD]
The screen is one of the surfaces on which a person meets the system. Design in this phase settles the whole make-up of that meeting: where the system comes across a person, how it behaves over time, and what it does in the minute when it is unsure of its own answer. In a product built on a language model, there is usually more work on the other surfaces than there is on the screen.

[Six tiles — SURFACES AND TOUCHPOINTS]
- **Screen** — what a person sees, and in what order
- **Voice** — the same decision with no picture: order, length, the right to interrupt
- **Notification** — the system opens the conversation itself: when, and on what occasion
- **Email, report** — the answer read when the system is nowhere at hand
- **Refusal** — what the system says when it will not do the thing
- **Silence** — processing is running, there is no answer yet: what a person sees for that minute

[Three lines — THE SYSTEM'S BEHAVIOUR OVER TIME]
- **Sure** → it answers and shows what the answer is built on
- **Unsure** → it says so in the first person and offers a move forward
- **Wrong** → the person sees what happened, and has a rollback path

## Gold callout
Decisions in this layer are taken once, and they outlive any layout: the product's name, the promise at the entrance, the right to stop. The name sets the picture of the system in a person's head before they see the first screen — and correcting that picture costs a recall of the entire fleet.

## Speaker notes

The section opens with a caveat, without which everything that follows reads narrowly. The word "design" in this phase is usually taken to mean drawing screens. In a product built on a language model the screen is one surface among several, and there is usually more work on the rest.

Look at the list of surfaces and touchpoints. The screen — what a person sees, and in what order. Voice — the same decision with no picture: order, length of answer, the right to interrupt. Notification — the system opens the conversation itself, and what gets decided is when it has the right to do so and on what occasion. Email or a report — the answer a person reads when the system is no longer at hand. Refusal — what the system says when it will not do the thing. And silence: processing is running, there is no answer yet, and what a person sees for that minute has been designed too, even if only by default.

The second tier is behaviour over time, and for a product built on a model it carries the main load. When the system is sure, it answers and shows what the answer is built on. When it is unsure, it says so in the first person and offers a move forward. When it is wrong, the person sees what happened and has a rollback path. Not one of those three decisions is visible on a screen mockup, and the beauty of the mockup checks none of them.

And the third thing, the one people forget because it does not look like design. The product's name, the promise at the entrance, the right to stop are decisions from the same layer. The name sets the picture of the system in a person's head before they ever see the first screen. This is easy to check: the failure we take apart at the end of the section is precisely about the gap between the picture in a driver's head and the behaviour of the car, and correcting that picture came to a recall of two million vehicles.

So keep the next few slides wider than the screen. Both diamonds of the Double Diamond run across the system's behaviour as well. The design system covers the part of the rules that can be expressed as a number. The rest stays a human decision, and it is a human who will be held to account for it.

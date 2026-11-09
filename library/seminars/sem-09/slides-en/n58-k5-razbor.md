---
id: n58
type: answer_breakdown_table
duration_min: 2.0
assertion: "All five actions control how reproducible the answer is — and only one of the five, measurably, controls how correct it is"
learning_goal: "Breakdown right after the question (A1), a 4-column form — 'action · how it works · advantage · drawbacks' (A5). 2026-10-29 edit (K5-4, K5-5): an explicit 'BEST OF THE FIVE' label on the description row (otherwise the breakdown read as 'none of them fits') plus a separate conclusion, 'what we take and why'. There are no own re-measurement numbers (zamery-k5-povtorno) here — they live entirely in n60; the external figures (Thinking Machines) are checked and stay as the first row's drawback baseline."
visual:
  pattern: answer_breakdown_table
  primary: >
    A table: action · how it works · advantage · drawbacks. Four rows, no
    verdict column — the decision doesn't build new architecture, it
    returns to the already-assembled node (this case's deliberate rhythm
    break, P4).
  backup: >
    DESIGNER-PASS DECISION (issue #303, Part B): there is deliberately NO
    new "where the method sits in the pipeline" schema on this frame. All
    five actions in this breakdown (temperature, provider, field order,
    few-shot, description) insert no new node and don't touch the canvas
    — they only change what's inside the already-existing "Model answers"
    node (the call settings and the prompt text). That spot was already
    shown on the scene at n56 (`k5-shema-postanovka.png`): the dashed
    frame CIRCLES the model node itself rather than adding a new card
    alongside it — exactly because the five actions of this breakdown
    don't have five different spots, they have one shared one. A second
    schema with the same single spot would add cross-slide redundancy
    with no new information (anti-pattern §5.5,
    `tools/presentation-build/README.md`).

    The breakdown text is drawn from SETKA-KEYSOV-S9-part2.md, section
    "Case 5", subsection "Breakdown", fit into the 4-column form without
    rewriting its substance.

    THE RE-MEASUREMENT NUMBERS (zamery-k5-povtorno) ARE DELIBERATELY
    DROPPED FROM THIS FRAME — a direct producer instruction: "three
    different outcomes out of 10," "10 out of 10 one branch," and "0
    discrepancies in a set of 10" live entirely in n60, where they're
    first revealed. The breakdown here is like Case 1's (n08): not a
    single figure from our own run, only a qualitative "works / doesn't
    work" — the numbers come one screen later.

    P5-8 (2026-10-29 review): the separate "input substitution" beat
    (drilling the boundary-rule finding down to exec 816) was dropped as
    redundant — the same observation is folded into a short line on n60,
    next to the boundary finding already shown there. The second dropped
    beat — "boundary" (criteria_checklist_and_boundary) — was merged with
    n62 into one file, following Case 1's pattern
    (`n17-k1-obobshchenie-granitsa.md`, generalization and boundary on one
    screen).

    THE ONLY NUMBER ON THE FRAME is external: Thinking Machines, "80
    unique completions out of 1000 at T=0, divergence at the 103rd token"
    (CHISLA-SVERENO.md, line 19, status CHECKED, verbatim). This isn't our
    own run and not Olga's question — independent work on the same effect
    in other models, named by source, with a baseline (1000 calls).

    The fact about the `seed` field on the rig's node (n8n
    `LmChatOpenRouter`: no seed/top_k/min_p, default temperature 0.7) —
    CHISLA-SVERENO.md, line 26, checked against the source. This isn't a
    measurement but the node's configuration; the number of fields in the
    list isn't named on this frame — it's first counted on n59, the same
    place it's visible to the eye.

    The fourth row (field order): a run of this same rig exists
    (`stend/zamery-k5-k6/run_k5_order.py`) and gave a sign opposite to the
    claimed effect — named qualitatively, without figures, by the same
    rule: this run's numbers aren't on the frame, they're not from the
    re-measurement, but that's also not a reason to unpack a third set of
    figures on a breakdown that already has two sources.
---

# What Each of the Five Actions Does

## Assertion

None of the five is, by itself, a mistake. All five control the answer's reproducibility; description is the one of the five that measurably cleaned up the substantive error too.

## Visual

| Action | How it works | Advantage | Drawbacks |
|---|---|---|---|
| **Temperature 0** | removes sampling from the probability distribution, keeps the single most likely token at every step | sounds like "switch off randomness"; on a question whose answer sits whole in the knowledge base, it genuinely gives a stably identical answer in substance | doesn't even give bit-for-bit reproducibility: an independent measurement of the same model (`Thinking Machines`) — a thousand calls at temperature 0 produced **80 unique completions out of 1000**, diverging from the 103rd token on — the cause is parallel requests sharing one server. On questions where the answer has to be composed rather than found ready-made, there's no stability either — what that means in practice, the rig shows next |
| **Pin the provider** | in the model node's routing block, choose a specific provider instead of automatic "by price/availability" selection | removes a source of nondeterminism that has nothing to do with temperature at all | doesn't solve nondeterminism within the pinned provider itself; a pinned provider can be more expensive or slower than automatic selection |
| **The "reasoning" field before "answer"** | in the structured-output (`JSON`) schema, the reasoning field is declared first, the final-answer field last | measurably works — on a separate task, a run of this same rig showed a stable, reproducible effect | the effect points the wrong way: the device fixes the accuracy drop caused by the rigid format on a separate task — that's a different effect, not the same spread between repeats of one identical question. On this rig's own run, changing the field order didn't add to the client answer's stability, it subtracted from it |
| **Few-shot: question-answer examples in the prompt** | 2 contrasting examples are added ahead of the knowledge base — a number close to, and below, the threshold, and one close to, and above it, each with the correct decision | the model sees a sample of the comparison logic and the answer's format at once, in a single example | teaches the answer's form more than the rule itself: if the model copies the example's style instead of extracting the general comparison logic from it, the example doesn't transfer to a new number — which is what our own run showed, further along in the beats |
| **Description: an explicit explanation of the rule in the prompt** | one sentence is added after the knowledge base, directly naming the rule's boundary | **BEST OF THE FIVE — the only one that measurably cleaned up the substantive error.** A direct explanation of the rule: the result doesn't depend on whether the model generalizes correctly from a sample | doesn't scale on its own: every rule the model gets wrong needs its own sentence, written in advance by someone who already knows exactly where it goes wrong |

> **What we take, and why.** We take description: the only one of the five that measurably fixes both reproducibility and the substantive error. The other four only control how identical the answer is; for correctness, you need description or a content check (ahead).

## Speaker notes

We'll go through the five actions one by one, and I'll say this up front: none of them is a foolish idea. Each has a clear engineering logic behind it, which is exactly why the hand reaches for it.

Temperature zero removes the sampling step itself: at every step, the model takes the single most likely token instead of a random one among several plausible ones. On a question whose answer sits whole in the knowledge base, this really does give a stable result — a run of this rig confirms it. But even here there's no full reproducibility: an independent measurement of the same mechanics on a different model showed that a thousand identical calls at zero temperature produce eighty different completions, and the divergence doesn't start with the first word — it starts somewhere in the middle of the text, because of how the computation shares a server with other parallel requests. This is someone else's work, a different model, but the same kind of effect — source: [Thinking Machines Lab, "Defeating Nondeterminism in LLM Inference"](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/).

Pinning the provider is an action about the call's routing, and doesn't touch temperature at all: the node our process is built on has a separate routing setting, and that will be visible on the next frame. It removes one source of randomness, but doesn't solve it within the pinned provider itself.

The third card is a completely different kind: it concerns the structure of the answer itself — the order the JSON fields stand in. Putting the reasoning field before the answer field is a device that really does work, measurably, only it solves a different problem: it fixes the accuracy drop caused by the rigid format. It doesn't fix the spread between repeats: on our own run, changing the field order didn't add reliability to the answer — it subtracted from it.

The fourth — few-shot, question-answer examples ahead of the knowledge base: a number close to and below the threshold, a number close to and above it, both with the correct decision. The idea is clear — the model sees a sample and transfers the logic to the new question. The risk is that what gets picked up is the answer's form rather than the comparison rule itself.

The fifth — description, one direct sentence after the knowledge base, naming the rule's boundary, with not a single example. It requires no generalization from the model at all — the rule is simply stated. The cost: a sentence like this has to be written in advance for every rule the model gets wrong, and you first have to find out exactly where.

Of the five actions, the clearly best one is the fifth: by the measurement ahead, it's the only one that fixes both reproducibility and the substantive error itself. We take it for that reason, regardless of the order the cards happen to be listed in. The other four only control how identical the answer is, time after time. How correct it is — exactly what matters to Olga — they don't touch at all.

Which of the five actions actually helps Olga, and which one really fixes a persistent error — coming up, on the same questions we've already seen.

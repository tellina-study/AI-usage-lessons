---
id: n01
type: hero_cover
duration_min: 0.5
assertion: "The knowledge base that lived entirely inside the prompt all through last seminar steps outside it today"
learning_goal: "Cover. Names the session's topic and its rung on the arc — knowledge outside the prompt (rung 4), not a new tool mechanic."
visual:
  pattern: hero_cover
  primary: >
    Dark Ocean gradient, a large title centered on the canvas, a subtitle
    in the middle of the open band. No session number on screen.
  backup: >
    The title is verbatim from ARCHITECTURE.md (the `title` field) and
    SETKA-KEYSOV.md ("Session topic"): where the process gets its facts
    and why it considers them true. The session number is deliberately not
    printed on the cover — owner's decision, sem-06/qa/oblozhka-bez-nomera.md,
    the same device as the S8/S9 covers. There is deliberately no figure on
    the cover: the session's question is asked verbatim on n03 and returns
    on n81, and a third spot on the cover would throw off the count of
    those two (the same device used on Seminar 9's own n01).
---

# Knowledge Outside the Prompt

## Assertion

A dozen FAQ items that fit inside a single model call — that's the knowledge base at the start. Today it grows.

## Visual

> Processes built on large language models: the fourth session of the arc.

## Speaker notes

The previous session left the training center's process able to do more than it could at the start of the arc: it answers the requester itself, checks its own answer before sending it, decides small refunds by a hard rule written in code — no need to guess on the model's behalf here — answers in one stable format, and, if a photo is attached to the request, reads it. The whole time, there was one place in the process we hadn't touched: where it gets its answers from. The knowledge base — the training center's rules, the FAQ, the wording for refunds — lived entirely inside the prompt. A dozen items, written directly into the text that the process hands the model in full, every single time.

At ten items, this works and raises no questions. But the training center doesn't stand still: every week the base gains a new regulation, an updated FAQ item, a breakdown of another disputed case from the last cohort. Ten items is the base's state at the moment the process launched; from there it grows and changes. The previous session ended on a question that this convenience cannot survive forever: at what size and volatility does putting "everything in the prompt" stop being a reasonable decision for the knowledge base.

Today's session is the answer to that question, unpacked into four parts. We'll decide when the base still fits entirely in the prompt and when it no longer does, by volume and by cost — intuition is a poor advisor here. We'll work out how to cut a document into pieces so that the chunk you need doesn't lose its meaning. We'll choose a search method to match the type of question — an exact match of words or a paraphrase in different words — and understand when combining the two methods pays off and when it's just extra complexity. And separately, we'll carry the same design over to images: the training center receives scans of forms and receipts, and finding a similar one among them is the same storage-and-search task as for text.

All four parts rest on measurement: questions from an open dataset with a known correct answer, real document scans — intuition is not something to trust here. One of the four measurements will end in an honestly shown failure — an approach tried according to plan that didn't work in practice, and that's a full-fledged part of today's breakdown.

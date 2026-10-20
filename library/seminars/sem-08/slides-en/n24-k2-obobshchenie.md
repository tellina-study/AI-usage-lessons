---
id: n24
type: answer_breakdown_table
duration_min: 2.0
assertion: "Mechanical and meaning-based checking aren't competitors, but different tools with different costs and different coverage; a heavier non-language tool doesn't guarantee an improvement"
learning_goal: "Case 2's generalization on the measured result, plus a forward bridge to Seminar 10 as its own line, not a topic declaration."
visual:
  pattern: answer_breakdown_table
  primary: >
    A short generalization thesis built on the n20 measurement, plus a
    separate line about Seminar 10.
  backup: >
    The generalization and the forward bridge are from SETKA-KEYSOV-S8.md,
    Case 2, sections "Generalization" and "Forward Bridge", carried over
    without changing the wording.
---

# Mechanics and Meaning — Different Tools, Not Versions of Each Other

## Assertion

Exact match can't catch a rephrasing in principle. The classic vector approach isn't an alternative to it, or an equivalent substitute: the measurement showed it measurably worse — not an assumption.

## Visual

> **The systemic takeaway.** Exact match stays in the final solution — but as the first cheap filter, saving 5 of 20 model calls for free, not as an alternative to the LLM.

> **Further in the course.** In Seminar 10, this same mechanic — comparing the meaning of requests — scales up into searching for an answer in a knowledge base.

## Speaker notes

Let's sum up this case on the measurement we just saw, not on an assumption.

Mechanical checking and meaning-based checking aren't competitors, and neither is a "more advanced version" of the other. Exact match can't catch a rephrasing in principle: it compares strings, not meaning, and it has no other way to work. The classic vector approach looked like a more serious alternative — it has a similarity measure and a threshold — but the measurement on 20 real pairs scored it worse than plain hashing: 13 out of 20 against 15. It fails on the same spots, the same rephrasings, for the same reason — zero shared words despite a complete match in meaning — and on top of that it gives 2 false positives exactly where hash makes no mistake at all. A "more serious" non-language tool doesn't just fail to guarantee an improvement — it can be measurably worse. That's what the measurement showed on its own data, not a general property of the method.

The systemic takeaway worth carrying forward: spend the expensive tool only where the cheap one clearly didn't give an answer. Exact match stays in the final solution — but as the first cheap filter that takes on literal repeats for free and saves 5 of 20 model calls on our set, not as an alternative to the LLM it supposedly competes with. The model is called only on what the first filter didn't resolve unambiguously, and there its cost is justified, because nothing else can replace it: neither hash nor the classic vector approach solves rephrasing in Russian.

This is the same systemic move as in this session's first case, only there it looked different: the model step was removed entirely and replaced with substituting values, because the task turned out to be fully deterministic. Here the task isn't fully deterministic — mechanics can't in general tell whether two different strings of text share one meaning — so the model isn't removed, it's shifted to where it's actually needed.

And separately — where this leads further in the course. In Seminar 10, this same mechanic — comparing the meaning of two requests — grows into a task of a different scale: searching for a ready answer in a knowledge base and merging similar questions into one, instead of comparing a new text against a single recent request from the same person. Today's duplicate check is, in essence, the first, narrowest version of that same task.

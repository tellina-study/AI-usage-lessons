---
id: n82
type: content
duration_min: 1.5
assertion: "Four cases, four independent measurements on real data — not one of them on a made-up number, and one of them ended in an honest failure, not a patched-up substitute"
learning_goal: "The session's tally (the through-line gets a number, not just an impression — CLAUDE.md stroenie-i-povestvovanie.md §4.2). What carries forward through the cycle — the cost of each case's solution, not a free win."
visual:
  pattern: content
  primary: >
    A tally tile (4 cases, real datasets, 1 honest failure), a "what
    carries forward" tile for each case.
  backup: >
    The tally is by corpus: SberQuAD (Cases 1–3), CORD (Case 4). "What
    carries forward" — SETKA-KEYSOV.md / rework/section-6-zakrytie.md,
    "What carries forward through the cycle," numbers brought up to date
    with the final version of the measurement.
---

# The Session's Tally: What Was Measured, What Remains Unverified

## Assertion

Taking the knowledge base outside the prompt is not free in any of the four cases.

## Visual

> **Four cases, four independent measurements on real data — SberQuAD for text (Cases 1–3), CORD for images (Case 4). Not one of them on a made-up number. One of the four runs — multimodal embedding in Case 4 — ended in an honestly shown result that didn't work, and it wasn't passed off as a patched-up substitute.**

Storage (Case 1) saves on the cost of each answer, but adds a data-preparation step and the risk of a stale index — the base's copy doesn't update itself when the source changes. Sentence-boundary chunking (Case 2) is more accurate than fixed-size chunking by character count, but is a bit more complex to implement and depends on the quality of sentence splitting. Hybrid search (Case 3) is more reliable than any single method, but costs an extra computation-and-merging step on every query — and isn't justified on a small, uniform base; a reranker adds yet another paid step on top. Image search (Case 4), where it's actually needed, requires a separately verified component for each class of similarity — and not one convenient, universal answer turned out ready to use without its own verification.

## Speaker notes

Four cases, four independent measurements on real data — SberQuAD, an open question-answering dataset built on Wikipedia articles, for the first three cases, and CORD, an open dataset of real receipts, for the fourth. Not one of the four runs stands on a made-up number — each has a real corpus, real questions, and a real run protocol.

One of the four runs — multimodal embedding in the fourth case — ended in an honestly shown result that didn't work. That's the very subject of today's rung: there's no production defect here. Knowledge outside the prompt means the process now depends on a device that can silently hand back a wrong or useless result with not a single error showing on screen — and the only protection against that is checking the device itself: trusting that it didn't complain isn't enough.

Now — what carries forward through the cycle, because taking the knowledge base outside the prompt is not free in any of the four cases. Storage, from the first case, saves on the cost of every answer, but adds a data-preparation step done ahead of time and the risk of a stale index: the base's copy doesn't update itself when the source changes. Sentence-boundary chunking, from the second case, is more accurate than chunking by character count, but is a bit more complex to implement and depends on the quality of sentence splitting for the specific language. Hybrid search, from the third case, is more reliable than any single search method, but costs an extra computation-and-merging step on every query, and isn't justified on a small, uniform base; an optional reranker on top adds yet another paid step. Image search, from the fourth case, where it's actually needed, requires a separately verified component for each class of similarity — semantic and literal — and not one convenient, universal answer turned out ready to use without its own verification.

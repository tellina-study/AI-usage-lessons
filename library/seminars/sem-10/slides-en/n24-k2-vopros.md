---
id: n24
type: question_with_option_cards
duration_min: 1.0
assertion: "Four actions for cutting a document — different boundaries, each checked by the same run"
learning_goal: "Case 2's question: four action cards, no verdicts (A6). Each is a design choice about where to cut, not a fact about a tool's properties."
visual:
  pattern: question_with_option_cards
  primary: >
    Question in a gold frame, four cards of equal width, no arguments and
    no verdicts.
  backup: >
    Cards — SETKA-KEYSOV.md Case 2, "Question for the room". The earlier
    version of this question held only two cards and did not include
    overlap chunking — at that point the measurement hadn't checked
    overlap at all (overlap=0 in every run). The follow-up run of
    2026-11-02 (`stend/raw/case2-results.json`, the same local Python
    measurement, not a live n8n call) checked word-boundary chunking and
    overlap chunking the same way as the first two actions — all four
    cards now rest on a measured result, there is no open item about
    overlap left (closed at n38).
---

# Where should the document cut fall

## Assertion

Four ways to draw a chunk boundary — by character count, by words, by sentences, by character count with overlap.

## Visual

> **Where should the document cut fall?**

`cut strictly by character count, without regard for the text` · `cut by sentence boundaries` · `cut by word boundaries` · `cut by character count with overlap`

## Speaker notes

Four actions, and all of them are real engineering choices. Cutting strictly by character count is the simplest and cheapest to implement: one parameter, a mechanical pass through the text with no regard for content. Cutting by sentence boundaries is a bit more involved: you first need to figure out where one sentence ends and the next begins, and only then make the cut. Cutting by word boundaries is an in-between option: the cut holds to a word boundary, but knows nothing about sentence boundaries. Cutting by character count with overlap works the same way as the first action, with one addition: neighboring chunks partially repeat the same stretch of text.

Think it through: the document is cut into chunks of one hundred eighty characters. What's the probability that this cut will, by chance, tear right through the middle of the phrase holding the answer to a future question?

Fifteen seconds to choose. The breakdown of how each action actually works comes on the next screen; the check against real documents, with a known correct answer, comes after that, on the test structure and on the result itself.

All four actions produce the same output format — a list of text chunks ready to have an embedding computed for each and be placed in the store. From outside, at the level of the rest of the chain, no difference is visible at all: all four versions feed chunks of exactly the same shape into the next step. The entire difference is hidden inside one node, which is exactly why it's easy to miss until you check the result by the numbers.

And that's exactly why the vote here isn't an idle exercise. If the difference between the versions were visible to the naked eye on any example — say, if version 1 produced visibly broken, unreadable text — the choice would be obvious without any measurement at all. But all four methods produce chunks that look perfectly normal if you simply open and read them with your eyes. The problem only shows up once a specific question lands exactly on the cut's boundary, and that's not visible in advance from any single chunk on its own.

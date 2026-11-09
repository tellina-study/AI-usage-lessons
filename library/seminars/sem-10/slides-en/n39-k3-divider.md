---
id: n39
type: case_divider_quote
duration_min: 0.5
assertion: "Chunks are split correctly by meaning — but the right chunk still has to be found among hundreds of identical-looking ones"
learning_goal: "Case 3's divider. Its entry form is an observation that follows directly from Case 2 (canon §8.2: every case's entry form is different)."
visual:
  pattern: case_divider_quote
  primary: >
    Dark background, one large line of action. Below it — a four-case
    track, the third highlighted.
  backup: >
    Case title — "Choosing a Search Method," by task, matches case_track.
    Transition — SETKA-KEYSOV.md Case 3, "Entry form": the observation
    follows directly from Case 2.
---

# Case 3. Choosing a Search Method

## Assertion

Correct splitting doesn't answer the question of how to find the one right chunk among five hundred.

## Visual

> Case 2 split documents correctly, by meaning — counting characters played no part in it. But a correctly split chunk still has to be found among hundreds of identical-looking ones once a specific question arrives.

## Speaker notes

The previous case closed the question of how to split a document into chunks so that each chunk carries complete meaning. But the solved splitting problem opens the next, separate problem: the chunks are split correctly, and there are many of them — hundreds, if the base has grown the way we discussed back in the first case — and when a specific question arrives, that one needed chunk still has to be found among all the rest.

This is a new task with its own natural first attempt, its own question, and its own measurement; it cannot be called a continuation of the previous case. Let's move to it.

This task is not trivial, even though it sounds simple. "Find the right chunk" is easy to confuse with "find something that looks similar": almost any search method will almost always return something, and formally the process won't crash or complain about an error. The question isn't whether the search returns a result, but whether that result turns out to actually be the chunk that holds the answer — and whether it lands in first place in the results — the middle of the list, where the model might not even notice it, doesn't count here. The difference between "something was found" and "exactly the right thing was found" is the subject of today's breakdown, and we measure it on questions with a known correct document ahead of time — this isn't judged by eye.

The task is made harder still by the fact that the more documents there are in storage, the higher the chance that a similar but wrong document happens to land next to the right one by formal features — a similar topic, similar words, a similar structure. With ten documents, almost any reasonable search method will find the right answer, because it has almost no competition. With five hundred documents, the competition for first place in the results becomes real, and that is exactly where the difference between search methods first becomes visible and measurable.

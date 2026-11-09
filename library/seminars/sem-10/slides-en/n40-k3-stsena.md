---
id: n40
type: problem_scenario
duration_min: 1.0
assertion: "Version 1 — search by meaning, through a vector; it seems that since it understands meaning, it must surely be better than keyword search"
learning_goal: "Case 3's scene beat: the staging diagram (S1 — solid/dashed, canon forma-keysa-s-zamerom.md §2) + the need (find the right chunk among hundreds) + version 1, formulated as an intuition that the case checks by measurement, not accepted as a given."
visual:
  pattern: problem_scenario
  figure: case3-shema-postanovka-en.png
  primary: >
    On top — the staging diagram (S1): solid nodes "Requester's question" →
    "Base split by meaning" (done since Case 2) → "Answer from the found
    chunk," a dashed gold node below points into the gap between the second
    and third — this is exactly the step today's case builds. Below — a
    tile for the need, version 1 as an intuitive expectation, an honest
    question.
  backup: >
    Diagram — `rendered/make_figures_sem10.py::case3_shema_postanovka`
    (Case 3's function, added by this edit). Tile text — SETKA-
    KEYSOV.md Case 3, "Staging," verbatim.
---

# How to find the right chunk among hundreds of identical ones

## Assertion

"Smarter" is not a proven property of semantic search — it's an intuition this case checks by measurement.

## Visual

> **The need.** Among hundreds of correctly split chunks of the base, find exactly the one holding the answer to the given question — and find it right in first place in the results — tenth place doesn't count here.

Version 1 — after what Cases 1 and 2 showed (semantic search works, splitting by meaning works), it's natural to assume: search should also go by meaning — through vector comparison of the query against the base's chunks. It seems that since such a search understands the meaning of the question, it must surely be better than keyword search.

> This is exactly the intuition this case checks by measurement.

## Speaker notes

The diagram on top shows exactly where today's step fits into the already-working flow. The question arrives by the form, as before. The base is already split by meaning — the previous case settled that. The model answers from the chunk it was handed — that already works too. The dashed node below is exactly the place still missing from the flow: between "base split" and "model answers," a step must go in that decides which of the hundreds of chunks the model actually sees. Case 2 split documents correctly, by meaning — counting characters played no part in it. But a correctly split chunk still has to be found among hundreds of identical-looking ones once a specific question arrives. This is a separate task, and it has its own natural first attempt.

Version 1 — after what the two previous cases of this same session showed (semantic search worked in Case 1, splitting by meaning worked in Case 2), it's natural to assume: search should also go by meaning — through vector comparison of the query against the base's chunks. It seems that since such a search understands the meaning of the question, it must surely be better than keyword search, which compares letters and doesn't touch ideas at all.

The word "seems" is here on purpose: this is exactly the intuition today's case checks by measurement, instead of simply taking it on faith because it sounds more technological. Alongside this version 1 stand other options — searching by the overlap of words between query and document, and searching both ways at once and merging the results. All of them are real engineering options, and which one actually wins is the question today's run answers. Intuition doesn't get a vote here.

It's worth keeping in mind where the expectation that semantic search must be better even comes from. It rests on a real and correct observation: a vector really does catch semantic closeness where words don't match literally — say, the question "how much does it cost to get money back" and a document about "the refund procedure" share not a single common word, but are clearly about the same thing. That observation is correct on its own. The question being checked today is different: does that mean semantic search wins always and everywhere, or does it, too, have its own zone where it's weaker than it seems.

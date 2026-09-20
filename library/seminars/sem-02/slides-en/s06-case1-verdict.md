---
id: s06
type: case_study
assertion: "Hybrid: the LLM extracts, code validates. Study the data, don't take the client's word for it"
learning_goal: "Case 1 debrief — LLM extraction + hard code validation; the lesson about sample size"
learning_outcomes: [LO1, LO7]
references: []
visual:
  pattern: hybrid_pipeline_illustration
---

# Supplier documents — debrief

## Assertion

LLM extraction over a variable input + hard code validation on the way out

## Visual

A simple three-block diagram: document (any format) → LLM extracts fields → code
checks types/required values/ranges → data into 1C. At the bottom, a large,
standalone lesson line: "Study the source data as thoroughly and broadly as you
can — and don't take the client's word for it." + illustration (designer).

## Speaker notes

Look at what happened: while we were only seeing two identical documents, plain
code looked sufficient and even preferable — it's predictable. As soon as the
real 4.2-gigabyte archive showed up, it became clear that the formats had
actually drifted apart, and a plain parser would have needed constant patching
for every new variation. The sensible answer here is a hybrid: the model does
extraction over unstructured or heterogeneous input, and then hard code
validation follows — checking field types, required values, ranges — before the
data ever reaches 1C. And the main lesson of this case is broader than
documents, so I'll say it as its own sentence: study the source data as
thoroughly and broadly as you can — and don't take the client's word for it. The
product manager was confident the formats were the same because they'd seen two
documents and decided that was enough. Before making an architectural choice,
you need to request a picture of the full volume of data the solution will
actually face, rather than relying on what you were told about it verbally.

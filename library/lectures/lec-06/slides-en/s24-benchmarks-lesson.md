---
id: s24
type: data_chart
duration_min: 2.7
assertion: "On real engineering calculations, the strongest models err on about a third to a half of the problems — 'confidently wrong' is more dangerous than 'doesn't know.'"
learning_goal: "Benchmarks + the lesson learned (kept separate from the catastrophes — cascade s24); an LLM is not a source of truth on codes/numbers"
learning_outcomes: [LO1, LO7]
chapter_ref: "§4.5 — Benchmarks and the lesson learned"
references: [orca-benchmark-2025, engibench-2025, aerospace-llm-2025]
visual:
  pattern: data_chart
  primary: "Bar/range chart: ORCA ~45–63% accuracy (5 SOTA models, a range) + EngiBench's drop under rephrasing + an aerospace case; gold-highlighted lesson"
  illustration:
    type: data_chart
    sources:
      - "ORCA Benchmark (2025) arXiv:2511.02589 — accuracy of 5 SOTA models ~45–63%"
      - "EngiBench (2025) arXiv:2509.17677 — a drop under rephrasing"
      - "LLM Aerospace Manufacturing Expertise (2025) arXiv:2501.17183 — a recommendation that violated 3 standards"
      - "QuickChart range/bar chart (Ocean palette: bars `#065A82`, gold marker `#F0AB00`)"
    caption: "Benchmarks: a third to a half of errors on engineering calculations"
interaction: none
---

# An LLM errs on a third to a half of engineering calculations

## Assertion

On real engineering calculations, the strongest models err on about a third to a half of the problems — "confidently wrong" is more dangerous than "doesn't know."

## Visual

In an Ocean rounded box — a range/bar chart (no catastrophes here; those were on the previous slide). The main element: a horizontal range bar, "ORCA Benchmark, 5 SOTA models: accuracy ~45–63%" (a range, not an exact number), with a gold marker (`#F0AB00`) on the upper bound "best ~63%," captioned "err on about a third to a half of the problems." Below — two compact cards: "EngiBench: a drop in accuracy under a simple rephrasing of the problem statement — a sign of pattern-matching, not reasoning," and "Aerospace case: a surface-treatment recommendation violated 3 independent standards at once — it sounded expert." At the bottom — a wide gold lesson plate (bold, 16pt): "An LLM is not a source of truth on grades / GOST / tolerances / numbers · independent verification at every interface with AI · an AI proposal that changes the force scheme = a formal change-request, not an 'OK' in a chat."

## Speaker notes

The historical analogues showed a pattern. Benchmarks give reproducible statistics — this is an argument of a different type, and it should not be conflated with the catastrophes. On five hundred real quantitative problems, the five strongest models showed accuracy in roughly the range of forty-five to sixty-three percent; the best model — on the order of sixty-three. That is, on engineering calculations, the strongest models err on about a third to a half of the problems. A separate benchmark recorded a noticeable drop in accuracy under a simple rephrasing of the problem statement — a sign that the model relies on surface pattern-matching rather than robust reasoning; in a study on statics, models confused tension and compression in truss members.

Also telling is an aerospace case: a model, asked about the surface treatment of titanium fuselage fasteners, recommended a coating that violates three aerospace standards at once. The case is valuable not for the model's name but for the character of the error: the recommendation sounded expert and, at the same time, violated three independent normative documents at once.

Let's draw the lesson together. First: an LLM is not a source of truth on grades, GOST, tolerances, numbers; "confidently wrong" is more dangerous than "doesn't know," because it does not raise your guard. Second: dimensional and factual control plus independent verification are mandatory at every interface with AI. Third: an AI proposal that changes the force scheme is formalized as a formal change-request, not accepted as a remark in a chat. An honest caveat: loud, specifically-AI catastrophes in design are, as of today, few and far between — the topic is young, and the damage comes with a lag. This is not an argument for safety: the evidence base is historical analogues, reproducible benchmarks, and studies of limitations. The engineer's task is to prevent the first loud AI failure, not to dissect it after the fact.

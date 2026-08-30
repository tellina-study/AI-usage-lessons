---
id: s24
type: case_study
duration_min: 3
assertion: "Hallucinations — an inherent property of AI"
learning_goal: "Ready-made hallucination example + retrieval exercise"
learning_outcomes: [LO6]
references: [huang-2023-hallucination, ji-2023-hallucination, vectara-hhem-2025, cybsafe-2024-oh-behave]
visual:
  pattern: example_with_metric_band
  primary: "Prompt + 3 fake DOIs + Vectara HHEM range <1%-15% + anti-pattern gold callout"
retrieval_moment: "s24+ think-pair-share \"spot the fake\""
---

# Hallucinations — an inherent property of AI

## Assertion

Hallucinations — an inherent property of AI.

## Visual

On the left, an Ocean rounded box with a prompt: "Name three research papers from 2023–2024 on the topic \"seismic resistance of underground pipelines\" with authors, journal, and DOI". Below the prompt — three convincingly looking fake references with non-working DOIs. On the right, a metric band: Vectara HHEM range from <1% (Gemini 2.0 Flash, summarization) to 10–15% (reasoning models, multi-step reasoning). At the bottom, a gold callout with the anti-pattern: "AI knows everything".

## Speaker notes

A hallucination in the context of an LLM is the confident production of factually incorrect information in a form indistinguishable from the correct one. The model doesn't "know" that it's saying something untrue; for it, this is simply a statistically plausible continuation of the token sequence.

A simple experiment. Ask a chat to "name three research papers on the topic [narrow topic] with authors and DOI". With a substantial probability you'll get three convincingly looking references, in which the author names may be mixed up or invented, the journals are real but the papers aren't in them, the DOIs are syntactically correct but don't resolve. Verification takes a minute via doi.org, but without it the references look credible.

The hallucination rate depends strongly on the task. By the Vectara Hughes Hallucination Evaluation Model benchmark, the range of current models is very wide: from less than one percent on a standard summarization task, for example Gemini 2.0 Flash, to ten-to-fifteen percent on reasoning models that require multi-step reasoning. This means that speaking about "the LLM hallucination percentage" in general is incorrect: the number depends heavily on the task and the benchmark.

Accompanying data on user behavior. By the CybSafe 2024 report, a survey of seven thousand people across seven countries: about thirty-eight percent of employees share confidential work information in AI tools without their employer's knowledge. This isn't directly about hallucinations, but it points to the scale of the trust problem: users hand AI systems information in a volume that isn't justified by their actual reliability.

The "AI knows everything" anti-pattern. Any AI response to a factual question is a hypothesis that requires verification. Especially references, numbers, quotes, legal norms, medical recommendations. This doesn't mean "don't use AI for facts"; it means "verify what AI outputs as fact". A critical reading attitude isn't an extra precaution but part of the standard workflow.

Now a short exercise. I'll show two short AI responses to the same question. Each has one correct and one planted detail. Discuss for thirty seconds in pairs: which part is the fake, and what did you check first.

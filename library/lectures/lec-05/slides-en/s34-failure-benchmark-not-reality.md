---
id: s34
type: case_study
section: "Section 4. Measurement"
duration_min: 2
assertion: "A benchmark score is evidence of performance only in that benchmark's own format; by 2026 saturation and errors in the reference answers themselves have been added to the format gap"
learning_goal: "The section's failure: a benchmark is not reality, on two named cases; the state of benchmarks in 2026"
learning_outcomes: [LO6]
chapter_ref: "§4.6 [for-slide-s34]"
in_bucket: true
interaction: none
protected: true
verify_day_of: true
note: "issue #212, R9: both cases described first, the analysis after. R5: MedQA and MMLU expanded. R6: the 2026 state of benchmarks added — the 89-92% band and 6.5% faulty reference answers."
source: "Med-PaLM 2 (arXiv:2305.09617) · Mata v. Avianca · Stanford RegLab, J. Empirical Legal Studies · Gema et al., 'Are We Done with MMLU?' (NAACL 2025, arXiv:2406.04127) · the 89-92% band on MMLU — April 2026 round-ups [VFY-day-of]"
meme_or_visual: >
  Two labelled mini-cases side by side: on the left medicine (a score of 86.5% and a
  struck-through link to "safe in the clinic"), on the right law (the shares of fabricated
  citations as bars, 17% and 33%). At the bottom — a band of scores 89-92% with the share of
  faulty reference answers marked on it.
---

# Visible content

## Title bar
A benchmark score is evidence only of its own format

## Body
[A benchmark is a standard set of tasks on which models are compared]

**CASE 1. MEDICINE**

2023. Google shows Med-PaLM 2 — a model for medical questions. On MedQA (a set of questions in the format of a medical licensing exam, with four ready answer choices) it scores **86.5%** and makes headlines as "doctor-level AI". Meanwhile Google's own researchers separately build a harder set of 240 adversarial questions — precisely because an exam with ready choices does not surface clinical-safety failures in open dialogue, where the patient offers no choices.

**CASE 2. LAW**

2023. A lawyer files a brief citing six entirely fabricated court cases — Mata v. Avianca. ChatGPT generated them; the legal service Harvey had nothing to do with it — a common attribution mistake. Stanford RegLab then tests the legal tools themselves on real queries: the most accurate one tested fabricates citations in about one query in six, the second twice as often, despite the promise of "no hallucinations". On the slide that is two bands: **Lexis+ 17%** and **Westlaw 33%** fabricated citations.

**ANALYSIS**

The mechanism is shared: the score is measured on a narrow task format and does not carry over to the user's real task. The benchmark is not useless for that — it compares versions of one model fairly. The trouble starts where a written-exam score is offered as proof of readiness to treat a patient.

[Gold callout]
By 2026 saturation has been added to the format gap. On MMLU (Massive Multitask Language Understanding, a combined set of 57 subjects) frontier models sit in a narrow band of **89–92%** — the score can no longer tell them apart. Worse: **6.5%** of the set's own questions carry an error in the reference answer, and in the virology section 57%. The remaining percentage points are in large part a contest in guessing broken questions. A safety claim resting on a benchmark alone is unsupported: it needs an adversarial check on the task the product actually solves.

## Speaker notes

Two cases, both from 2023, one mechanism.

The first. Google shows Med-PaLM 2, a model for medical questions. On the MedQA set it scores eighty-six point five percent. MedQA is questions in the format of a medical licensing exam, with four ready answer choices. The headlines say "doctor-level AI". And at the same time Google's own researchers separately build a harder adversarial set of two hundred and forty questions — precisely because an exam with ready choices does not surface clinical-safety failures. In a real dialogue the patient does not offer four choices. A mandatory correction: the widely repeated story that Med-PaLM recommended chemotherapy for a headache does not trace back to any primary source — the verifiable version is stronger.

The second. A lawyer files a brief citing six entirely fabricated cases — Mata v. Avianca. ChatGPT generated them; the legal service Harvey had nothing to do with it. That is a common attribution mistake, and it is worth correcting. A peer-reviewed study by Stanford RegLab then tested the legal tools themselves on real queries. The most accurate one tested, Lexis+, fabricated citations in seventeen percent of cases — about one query in six. Westlaw, in thirty-three, twice as often, while marketing itself as hallucination-free.

The analysis. The score is measured on a narrow format and does not carry over to the real task. The benchmark is not garbage for that: it compares versions of one model fairly and screens out models with no domain knowledge at all. The trouble starts where a written-exam score is offered as proof of readiness to treat a patient.

And what has changed by 2026. On the combined MMLU set, frontier models stand in a band from eighty-nine to ninety-two percent — that score can no longer tell them apart. And a peer-reviewed audit of the set itself showed that six and a half percent of its questions carry an error in the reference answer, and in the virology section fifty-seven. Which means the last few percentage points are in large part a contest in guessing broken questions. The conclusion for us: a safety claim resting on a benchmark alone is unsupported.

---
id: s22
type: assertion_visual
section: "Section 4. LLM in finance"
duration_min: 3
assertion: "In finance, an LLM answer about a rate/a client's right must be grounded and verifiable; the LLM is an interface to the source of truth, not the source of truth; 5 classes of error"
learning_goal: "The fact-checking pattern as an unfolded criterion (≥3 arguments) + grounding analogy + 5 classes; Bloom=Understand"
chapter_ref: "§4.2, §4.3"
visual_brief: "Top: left a compact criterion (3 args), right 5 classes of error. Bottom — a wide VISUAL band d22 (grounding anchor analogy: a student guesses in a confident tone vs first opens the reference book). Gold — alternative + Understand/Apply boundary. Relieve overload (student top-lost)."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
The LLM here is not the source of truth, but an interface to the source of truth.

## Body
[Left — Ocean rounded box, criterion «when an LLM is NOT the source of truth»]

- **Argument 1 — the hallucination mechanism:** an LLM generates a plausible continuation, it does not retrieve a verified fact. «Plausible» ≠ «correct».
- **Argument 2 — the legal cost of error:** a wrong rate/condition = a violation + harm to the client, and the organization is liable.
- **Argument 3 — what breaks:** free generation about regulated facts = a scalable generator of plausible misinformation with the bank's legal liability.

[teal callout — alternative]
For fixed facts (rate, tariff, right) — **deterministic retrieval** (lookup / grounded RAG), the LLM phrases what was found but does not invent the number. Any binding bank fact must be grounded and verifiable.

[Right — Ocean rounded box, 5 classes of error]
1. **fact hallucination** — a number without a source → cross-check against the primary source
2. **stale data** — a figure without a date → check currency
3. **proxy bias in the conclusion** — «we did not use the feature» → audit of outcomes
4. **deception by a metric** — «99.X%» without a base → FP/FN separately in money
5. **base substitution** — a loud share without «a share of what out of what» → request the base

[Analogy card]
grounding: the student first opens the reference book to the right page, reads the exact value, then phrases it — rather than guessing in a confident tone.

[Gold callout, bottom]
In the lecture: **recognize the class + name the principle** (Understand). Independently verifying 5 claims against primary sources — Seminar 5 (Apply).

## Speaker notes

Here is the through-line pattern of the whole lecture: fact-checking. Let us state it as an unfolded criterion, of when a language model is not the source of truth, with three arguments and an alternative. The thesis: in finance, a model's answer about numbers, rates, conditions, a client's rights must rest on a verifiable primary source and be verifiable; the model here is not the source of truth but an interface to the source of truth.

The first argument — the hallucination mechanism: the model generates a plausible continuation of text, it does not retrieve a verified fact; plausible is not equal to correct. Ask about the exact rate on a specific deposit — the model may produce a confidently sounding but wrong number, because its task is coherence, not truth. The second argument — the cost of error in finance is legal: an incorrectly named rate or condition is a potential violation and direct harm to the client, for which the organization is liable. The third — what breaks: if you allow the model to freely generate answers about regulated facts, you get a scalable generator of plausible misinformation with the bank's legal liability for every answer. The alternative and the criterion: for fixed facts, the answer is built by deterministic retrieval from a system or a document, the model phrases what was found in human language but does not invent the number itself.

To make «recognize the class of error» an operational skill, let us break down the typical classes. Class one — fact hallucination: a specific number without a reference to a source; the principle — cross-check against the primary source. Class two — stale data: a figure in a volatile area without a date; the principle — check currency. Class three — bias through a proxy in a conclusion about a group of people; the principle — remember that an audit of outcomes is needed. Class four — deception by a metric: accuracy without a base and a cost of error; the principle — ask for false positives and false negatives separately and in money. Class five — base substitution: a loud share without precise wording, exactly like «voice assistants over ninety percent». An analogy for grounding: a model without a grounding on a source is like a student who does not remember a figure but confidently pronounces it; a model with grounding first opens the reference book, reads the exact value, and only then phrases it. In the lecture you are required to recognize the class and name the principle; independent verification against primary sources — that is Seminar 5.

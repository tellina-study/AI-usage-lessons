---
id: s13
type: case_study
section: "Section 2. RAG"
duration_min: 3
assertion: "«Returned something ≠ returned the right thing»: RAG without observability silently degrades at scale; Air Canada is a grounding failure in pure form"
learning_goal: "RAG failure at scale (3 cases) + Air Canada revisited as grounding"
learning_outcomes: [LO7]
chapter_ref: "§2.4, §2.5 [for-slide-s13]"
visual_brief: "Left — 3 compact degradation cases: legal-AI / medical-RAG / support bot. Right — Air Canada revisited: the diagnosis + the correct alternative. Gold — the lesson phrase «returned something ≠ returned the right thing». Footer 12pt italic — sources + the framing «illustrative»."
interaction: poll
verify_day_of: false
---

# Visible content

## Title bar
«RAG failure at scale»

## Body
[Gold callout at the top — the main lesson]
**«The system returned something» ≠ «the system returned the right thing».** RAG has no built-in signal "I found nothing suitable" — it always returns the k nearest, even if they are irrelevant.

[Left — 3 compact cases in an Ocean rounded box]

**Legal-AI:** pulls "the nearest" cases — a different jurisdiction / an overturned precedent; the model builds them in as grounding
**Medical-RAG:** mixed fragments of different patients — close by symptoms, but clinically cannot be combined
**Support bot:** worked well on hundreds of articles; after growth to thousands the quality quietly crept down — no one noticed

[Right — Air Canada revisited]
**Diagnosis:** generated plausible text was put in a role that required a retrieved verified fact — a grounding failure
**Correct alternative:** for a fixed policy — a lookup / a page; if a dialogue is needed — RAG with strict grounding, a mandatory citation, an explicit "I don't know," human review

[Poll prompt, below in smaller type]
RAG returned an answer — how do you know it is right?

[Footer, 12pt italic]
*Documented classes of failures (Barnett et al. 2024; Air Canada — McCarthy Tétrault 2024). The cases are illustrative.*

## Speaker notes

The main lesson of the section in one phrase: "the system returned something" does not mean "the system returned the right thing"[1,2]. RAG has no signal "I found nothing suitable" — by default it always returns the k nearest fragments, even if they are irrelevant. Then the model honestly does its job: given garbage, it will compose a plausible answer on top of the garbage.

This is not a hypothetical risk but a known pattern of RAG engineering — seven failure points are systematized in Barnett et al. (arXiv:2401.05856, 2024). Three classes. Legal-AI pulls "the nearest k" cases; by vector, cases with matching words are close but legally irrelevant — a different jurisdiction, an overturned precedent; the model builds them in as grounding. Vector closeness is closeness of wording, not of applicability. Medical-RAG: a question about one patient retrieves fragments close by symptoms but from other patients; the model combines what clinically cannot be combined. Support bot: worked on hundreds of articles, after growth to thousands the quality quietly sagged — degradation at scale, because there is no "close enough" threshold. The alternative everywhere is not "remove RAG" but make it an observable system: a reference verification set and alerts, chunking along semantic boundaries, hybrid search with re-ranking.

Now let us return to Air Canada[3] (the case *Moffatt v. Air Canada*, BC CRT, decision 14.02.2024) — with the section's tools. The bot reported a refund of the difference and referred to a page with the real policy; the policy on the very same page did not allow such a refund. A source of truth existed, was available — but the answer was not derived from it, it was generated as plausible text. This is a model grounding failure: generated text in a role that required a retrieved fact. The correct architecture: for a fixed policy — a deterministic page or lookup; if a dialogue is needed — RAG with strict grounding, a mandatory citation, an explicit "I don't know," and human review. Air Canada is not "the AI hallucinates," it is the decision to put a generative architecture on a deterministic task. A short question for you: RAG returned an answer — how do you know it is right? Only by measurement; by eye, the plausible cannot be told from the correct.

Sources:
[1] Barnett et al. 2024 — Seven Failure Points (RAG) — «returned something ≠ returned the right thing»: 7 failure points of RAG engineering. https://arxiv.org/abs/2401.05856
[2] Kore.ai — Seven RAG Engineering Failure Points — legal-AI / medical-RAG / support bot — degradation at scale without observability. https://www.kore.ai/blog/seven-rag-engineering-failure-points
[3] McCarthy Tétrault — Air Canada (grounding failure) — generated text in a role that required a retrieved verified fact. https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot

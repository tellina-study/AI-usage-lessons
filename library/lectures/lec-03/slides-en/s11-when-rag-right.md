---
id: s11
type: assertion_visual
section: "Section 2. RAG"
duration_min: 2.5
assertion: "RAG is justified when there is a strong signal on the criteria (large / changes / provenance needed / private) AND there are no blockers from the «when NOT» criteria"
learning_goal: "When RAG is the right choice (a strong signal + the absence of blockers)"
learning_outcomes: [LO7]
chapter_ref: "§2.2 [for-slide-s11]"
visual_brief: "4 equal criterion cards, joined by an explicit «AND» (conjunction) to a central «→ RAG». Below them — a worked example (corporate regulations database: all 4 ✓). Gold — the word «SIMULTANEOUSLY» / the AND sign."
interaction: none
---

# Visible content

## Title bar
«When RAG is the right choice»

## Body
[4 equal criterion cards in an Ocean rounded box, joined by an «AND» sign]

**Large / growing**
does not fit in the window as a whole, or it is expensive to put the whole corpus into every query

**AND  Changes**
documents, prices, regulations update more often than model versions come out

**AND  Freshness + provenance needed**
the answer rests on a verifiable source; you can show where the fact came from

**AND  Private database**
the company's knowledge is not in the weights of a public model

→ **RAG**

[Worked example, bottom]
*A corporate database of thousands of regulations, updated weekly, an answer with a mandatory reference to the clause: all 4 criteria ✓ → a model RAG profile.*

[Gold — accent on «SIMULTANEOUSLY»]
**A single criterion on its own does not justify RAG — a conjunction is needed.**

## Speaker notes

RAG is the right choice when there is a strong signal on one or more of the criteria[1] and at the same time there are no blockers from the neighboring "when NOT" criteria. The first criterion: the knowledge is large or growing — the corpus does not fit in the window as a whole, or it does fit, but putting it into every query is expensive and slow. The second: the knowledge changes — documents, prices, regulations update more often than model versions come out; RAG reads the current store at query time, and a new document is available right after indexing. The third: freshness and provenance are needed — the answer must rest on a verifiable source, and you need to show where the fact came from; regulated domains almost always require provenance. The fourth: the database is private — the company's knowledge is not in the weights of a public model.

The logic of application matters. A single clear criterion is already a reason to take a look at RAG, but not a reason to build it automatically: before deciding, check the task against the "when NOT" criteria — is there a blocker there. The knowledge is large but does not change and fits in the window — a candidate for a long context, not RAG. The knowledge changes, but the task reduces to returning a fixed value — a candidate for a deterministic lookup. The criteria usually reinforce each other: knowledge that is at once large, changing, requiring provenance, and private — that is exactly the profile RAG is designed for, and the more criteria that converge, the more confident the choice. The formula is short: a strong signal plus the absence of blockers.

A worked example we will return to as a checklist walkthrough at the end: a corporate database of thousands of regulations, updated weekly, natural-language questions, a mandatory reference to the source clause. All four criteria converged, and no simpler mechanism closes them jointly, while a check against the "when NOT" criteria overturns nothing. This is a model RAG profile. And a practical observation: RAG's gain over a direct answer is especially large for smaller models — external retrieval compensates for what a smaller model lacks in its weights, so RAG often delivers the needed quality on a cheaper model.

Sources:
[1] IBM — RAG vs Fine-Tuning (vendor-neutral) — criteria-for-RAG: large/changes/provenance/private. https://www.ibm.com/think/topics/rag-vs-fine-tuning
[2] U-NIAH — RAG win-rate higher for smaller models — RAG's gain over a direct answer is especially large for smaller models. https://arxiv.org/abs/2503.00353 [VFY-day-of]

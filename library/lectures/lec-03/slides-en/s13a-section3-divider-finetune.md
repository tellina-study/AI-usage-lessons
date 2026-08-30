---
id: s13a
type: section_divider
section: "Section 3. Fine-tune vs prompt vs RAG"
duration_min: 0.3
assertion: "Section 3 — fine-tuning versus prompt and RAG: what to do when the problem is not knowledge but the model's behavior"
learning_goal: "Section 3 divider + a narrative bridge from RAG (the problem of knowledge) to fine-tuning (the problem of behavior)"
learning_outcomes: [LO7]
chapter_ref: "§3 [for-slide-s14]"
visual_brief: "The lecture's section_divider template (a giant «3» on the right, SECTION 3 + subheading + a narrative bridge line on the left, roadmap bar of 6 cards, gold marker on Section 3). Consistent style with s09/s18."
interaction: none
suffix_insert_after: s13
---

# Visible content

## Title bar
(none — section divider)

## Body
[Right — a giant «3», soft outline, decorative]

[Left — SECTION 3, 20pt teal]
**SECTION 3**

[Subheading, 38pt deep]
**Fine-tune vs prompt vs RAG**

[Narrative bridge line, 18pt italic light]
*We solved the problem of knowledge through RAG. But what if the problem is not knowledge but the model's behavior — its tone, format, adherence to policy?*

[Bottom — roadmap bar: 6 cards]
0 Opening · 1 Prompt · 2 RAG · **3 Fine-tune** *(gold marker — current)* · 4 API·agents · 5 Framework

## Speaker notes

In the previous section we worked through RAG and closed with it one specific class of problems — the problem of knowledge. When a model lacks facts: they are private, or they change faster than new model versions come out, or provenance is needed — we do not retrain the model, we slip the needed documents into the context. We also honestly worked through when RAG is not needed and how it quietly breaks at scale, and closed the section back onto the Air Canada case.

But not every problem is a problem of knowledge. It happens that the model has enough facts, but the behavior itself is not satisfactory: it answers in the wrong tone, in the wrong format, does not follow a domain policy, or you need a small cheap model that repeats the behavior of a large one. This is a different class of task, and RAG does not solve it — no matter how many documents you slip in, the tone will not change from that. Here the third tool enters the stage — fine-tuning. And immediately an important note on the structure of the section: the next slide is not criticism and not "when you should not," but a definition. Before working through where fine-tuning has narrowed, where it fails through catastrophic forgetting, and by what criteria to choose between it, RAG, and the prompt, we need to understand equally what it even is and how it fundamentally differs from the two already familiar tools. And we will start with the definition.

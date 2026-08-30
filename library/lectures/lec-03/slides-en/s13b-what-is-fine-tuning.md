---
id: s13b
type: assertion_visual
section: "Section 3. Fine-tune vs prompt vs RAG"
duration_min: 1.5
assertion: "Fine-tuning changes the MODEL'S WEIGHTS THEMSELVES on your data — this is what fundamentally distinguishes it from the prompt and RAG, which change only the context"
learning_goal: "The definition of fine-tuning BEFORE its critique/applicability; close the prerequisite gap on the visible layer (previously it was only inline in s14)"
learning_outcomes: [LO7]
chapter_ref: "§3.1 [for-slide-s14]"
visual_brief: "At the top — a one-phrase definition. In the center — a mini-diagram in an Ocean rounded box: [pretrained model] + [your dataset] → (fine-tuning) → [fine-tuned weights]. At the bottom — a contrast bar: prompt/RAG change the CONTEXT (do not touch the weights) vs fine-tuning changes the WEIGHTS. Gold — the word «WEIGHTS» as the semantic anchor."
interaction: none
suffix_insert_after: s13a
---

# Visible content

## Title bar
«What fine-tuning is»

## Body
[Definition, 16pt, under the title]
**Fine-tuning** — the continuation of training an already ready model on your data. In Lecture 1 this was one of the *usage types*; here it is an *architectural choice*, one of the rungs of the ladder.

[Center — a mini-diagram, Ocean rounded box, 3 blocks + arrows]
**Pretrained model** *(general weights)*  ＋  **Your dataset** *(examples of the desired behavior)*  →  *fine-tuning*  →  **Fine-tuned weights** *(the model is already different)*

[Bottom — a contrast bar, 2 halves]
The prompt and RAG change the **CONTEXT** — what we feed as input; the model's weights are not touched, the effect lives only within the scope of the request.
Fine-tuning changes the **WEIGHTS THEMSELVES** — the change is built into the model, is always in effect, and costs more than anything that changes the context.

[Gold — semantic anchor]
Prompt/RAG = "what to show the model." Fine-tuning = "change the model itself."

## Speaker notes

Before saying anything about where fine-tuning has narrowed, where it is dangerous, and by what criteria to choose it, we need to understand equally what it is. Fine-tuning is the continuation of training an already ready, pretrained model[1] on your own data. In Lecture 1, fine-tuning was mentioned in passing as one of the usage types of AI; here it appears in its true role — as an architectural choice, one of the rungs of the same ladder of complexity.

The mechanics on the diagram: you take a pretrained model with its general weights, you take your dataset — a set of examples of the behavior you want to obtain — and the fine-tuning process shifts the model's weights toward these examples. The output is already a different model: the same architecture and size, but different numbers inside. This is exactly the key difference for which a separate definition slide is needed. The prompt and RAG do not touch the weights at all: they change only the context, that is, what you feed the model as input right now. The effect of a prompt or a slipped-in RAG fragment lives exactly within the scope of a single request and disappears with the next one. Fine-tuning changes the model itself: the change is built into the weights, is in effect on every request by default, and it is precisely for this reason that it costs more and rolls back harder than anything that changes only the context.

An important practical note right away: in practice "fine-tune a model" almost always means not retraining all the weights but parameter-efficient fine-tuning, usually called by the acronym PEFT and most often implemented by the LoRA method. Full fine-tuning of all the weights in 2026 is rare, and in the next slides we will work through why this is so. For now, remember the difference as a formula: the prompt and RAG are "what to show the model," fine-tuning is "change the model itself." In the next slides we will rely on this definition as we work through why in 2026 fine-tuning narrowed to behavior rather than knowledge, and where it turns from a tool into a source of problems.

Sources:
[1] IBM — RAG vs Fine-Tuning (fine-tuning changes the weights) — prompt/RAG change the context; fine-tuning changes the model's weights themselves. https://www.ibm.com/think/topics/rag-vs-fine-tuning

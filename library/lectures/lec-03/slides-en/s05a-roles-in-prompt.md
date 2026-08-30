---
id: s05a
type: case_study
section: "Section 1. The prompt and its limits"
assertion: "A role in the prompt tunes tone, style, and depth of exposition — but does not raise factual accuracy; «persona = accuracy» is a debunked myth"
learning_goal: "A role in the prompt is a tool of style, not of accuracy; debunking the myth (failure/judgment content)"
learning_outcomes: [LO7]
chapter_ref: "§1.2 [for-slide-s05a]"
interaction: none
---

# Visible content

## Title bar
"A role in the prompt: tone, not accuracy"

## Body
[Myth → fact, 2 blocks]

**Myth**
"I'll write an expert role — the model will answer more accurately on facts"

**What the experiment showed** *(Zheng et al., 2024, EMNLP Findings)*
162 personas · 8 domains · 2410 factual QA questions · 4 model families
→ personas **do not improve** factual accuracy compared to a baseline without a role

[Gold callout, bottom]
A role really does affect the **tone and depth** of exposition (model-specific), not the truth of a fact. Need accuracy — context and RAG work, not the wording of a role.

## Speaker notes

The prompt formula "role plus task plus context" is familiar from the first lecture, and the role is the most frequent first element an engineer writes into the system prompt: "you are an experienced lawyer," "you are a strict editor." The intuition is usually this: the more precise the role, the more competent the answer, as if the model switches into expert mode. This is one of the most persistent myths, and it is worth examining honestly. Mechanically, a role is tokens that appear in the context before the question and participate in all the attention computations discussed in the previous lecture: it does not toggle an expert mode with a switch, but shifts the probability distribution of the next tokens toward text resembling how a holder of that role would have answered in the training data.

The key question is whether this shifts factual accuracy[1], not only the delivery. A specially designed study by Zheng and colleagues gave an unambiguous answer: 162 personas, eight expertise domains, 2410 factual questions, four model families — and personas do not improve accuracy compared to an answer with no role at all. A model told "you are a Nobel laureate in physics" does not answer physics more accurately than a model with no role. A separate study shows what a role does affect for real: tone and depth of exposition — how formally and in what detail the topic is developed — but not whether the reported fact is true, and this effect is model-specific. The takeaway for the engineer: a role is a tool for tuning style, not for raising accuracy. Need factual accuracy — a well-built context and, where necessary, grounding in a verifiable source work, not a lucky wording of a role.

Sources:
[1] Zheng et al. 2024, Findings of EMNLP — personas do not improve factual accuracy — 162 personas · 8 domains · 2410 factual questions · 4 families → no accuracy gain. https://arxiv.org/abs/2311.10054

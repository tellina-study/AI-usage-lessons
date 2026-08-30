---
id: s04
type: assertion_visual
section: "Раздел 0. Введение"
duration_min: 1
assertion: "The central question: what inside an LLM changes how we use it?"
learning_goal: "Центральный вопрос + 3 промиса-якоря (callback к Lec-1 §5.3)"
learning_outcomes: [LO1, LO7]
chapter_ref: "§Введение [for-slide-s04]"
visual_brief: "Центральный вопрос крупно (32pt bold #21295C). Снизу — 3 промиса-якоря в Ocean rounded boxes: (1) почему промпт с ролью лучше → Раздел 3, (2) почему AI плохо считает буквы → Раздел 1, (3) почему один запрос даёт разные ответы → Раздел 4. Gold-маркер «payoff в s24»."
---

# Visible content

## Title bar
"The central question of the lecture"

## Body
[Центральный вопрос крупно, по центру верхней половины слайда — 32pt bold #21295C]

> "What happens inside an LLM between my request and its answer — and which of these internal mechanisms change how I use it?"

[3 Ocean rounded boxes по нижней половине — промисы-якоря с роадмап-метками]

**Promise 1.** Why does a prompt with a role work better than an empty one? → Section 3 (attention).

**Promise 2.** Why is AI bad at counting letters? → Section 1 (tokenization).

**Promise 3.** Why does the same request give different answers? → Section 4 (sampling).

[Gold-маркер мелким сверху над промисами: «3 answers — the lecture's finale»]

## Speaker notes

Today's lecture has one central question, and it is stated briefly: what happens inside an LLM between my request and its answer, and which of these internal mechanisms change how I use it. Notice that the question has two parts. The first is descriptive: understand what is technically arranged inside. The second is pragmatic: out of all that internal machinery, single out what changes engineering practice. If an internal mechanism does not affect how you set a task for the model or interpret its answer, we do not take it apart today.

Three promises left unanswered by Lecture 1 feed into the answer to this question. The first — why a prompt with a role works better than an empty one. Anyone who has tried it knows that "You are a Python expert, explain async to a junior" gives a qualitatively different answer than just "Explain async." Today we will understand the mechanism of that effect at the level of attention. The second — why AI is bad at counting letters. The classic example with the word `strawberry` and counting the letter `r` is not a bug or a gap in training, but a structural consequence of how tokenization works. We take that apart in Section 1. The third — why the same request can give different answers. The source is stochastic sampling at a temperature above zero, and in Section 4 we will see the mechanism.

These three promises work as anchors for the lecture: we will return to them in each of the four sections, and at the very end they will get an explicit answer — three "whys" through concrete internal mechanisms.

---
id: s01
type: hook
section: "Раздел 0. Введение"
duration_min: 2
assertion: "Your brain chooses, every second, what matters and what is background"
learning_goal: "Открывающий эмоциональный hook про человеческое внимание — мостик к Разделу 3 «Механизм внимания» (s13a)"
learning_outcomes: [LO1]
chapter_ref: "§1.1 [for-slide-s01]"
visual_brief: "Дружелюбный персонаж (герой в духе flat-иллюстраций Storyset/unDraw — не заимствование конкретной авторской графики), которого одновременно тянут в 3 стороны: уведомление на телефоне, посторонняя мысль, задача-документ. Внизу мелкая bridge-строка к s13a."
verify_day_of: false
---

# Visible content

## Title bar
"While you read this sentence — what are you NOT paying attention to?"

## Body
[Sub-line под title, 18pt italic teal, центр]
*Your brain chooses, every second, what matters and what stays in the background.*

[Главный визуал — по центру, крупно: дружелюбный персонаж, которого одновременно тянут в 3 стороны]

- A notification on your phone
- A stray thought ("buy tickets?")
- An unfinished task

[Bridge-строка внизу, мелким, italic]
*The mechanism we will take apart inside an AI model today has exactly the same name — "attention." It works in a similar spirit — but not the way yours does.*

## Speaker notes

Let's start not with AI, but with you. While you read this sentence, your brain is continuously solving a small but important task: deciding what deserves to be in focus right now and what can stay in the background. Somewhere on the periphery there is a notification on your phone, a half-formed thought about the evening's plans, the feeling of an uncomfortable chair. All of it competes for the same limited resource — your attention. You do not consciously register the choice in the moment, but it is happening constantly.

On the slide there is a character being pulled in three directions at once: a notification, a stray thought, an unfinished task. This is not about distraction as a flaw — it is the normal operation of the attention mechanism. Human attention is bounded: we physically cannot process everything with equal completeness at once, so the brain is always setting priorities — what goes into focus, what stays in the background.

Today's lecture is about what happens inside an AI model between your request and its answer. And one of the four internal stages we will take apart is called literally the same thing as what you just felt — the **attention mechanism**. When a model processes your text, it too decides which parts of the input to "look at" more closely and which to leave as background. An important caveat, which we will return to in Section 3: the similarity here is in the name and in the general idea of "choosing a priority," not in the machinery. Inside the model this is not a psychological process but a concrete, computable operation — a matrix of weights that can be calculated and inspected. We will take that apart in detail when we get to the core of it.

Before we get there — we will walk the whole path of a request through the model: tokenization, embeddings, attention, sampling. Each stage has its own concrete engineering consequence for how you work with AI in practice.

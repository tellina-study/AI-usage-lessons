---
id: s03
type: assertion_visual
section: "Раздел 0. Введение"
duration_min: 1.5
assertion: "Today we go deeper into the \"model\" layer of Lecture 1's four layers"
learning_goal: "Recap Лекции 1 §3.2 + bridge к внутренностям модели"
learning_outcomes: [LO1]
chapter_ref: "§Введение [for-slide-s03]"
visual_brief: "Слева — маленькая копия nested layers из Lec-1 (модель → чат → агент → приложение) с подсветкой нижнего слоя «Модель» в gold. Справа — bridge: «что знаем» (модель = stateless inference из Lec-1 §3.2) → «что узнаем сегодня» (что внутри inference)."
---

# Visible content

## Title bar
"Today we go deeper into the \"model\" layer of Lecture 1's four layers"

## Body
[Слева — nested layers иконка из Лекции 1: 4 концентрических Ocean rounded box, выровненных по нижней границе. Снизу вверх: Модель → Чат → Агент → Приложение. Нижний слой «Модель» выделен gold-обводкой]

[Справа — bridge-блок в 2 строки]

**What we know:**
The model is stateless inference: data in → prediction out, no memory between calls.

**What we learn today:**
What is inside inference. 4 stages: tokenization → embedding → attention → sampling.

## Speaker notes

To keep our bearings, let's go back to Lecture 1 for one minute. In that lecture we built a layered picture of how AI works inside a product: the model at the bottom, the chat loop above it, the agent loop above the chat, and the application on top, into which all of this is packaged. Lecture 1 described the bottom layer, the model, as a stateless function: data in, prediction out, and no memory between two calls. With that description we can talk about **where** the model sits in a larger system, but we set aside the question — **what exactly** happens inside that stateless function when you type "Today I ate an apple" into the chat and get a reply.

Today we carefully open that black box. The main content of the lecture is the four internal stages your request passes through between the moment it is sent and the moment the answer arrives. Those four stages: tokenization (how the model cuts text into units it can work with), embedding (how each unit is mapped to a numeric representation of meaning), the attention mechanism (how the model decides what to rely on in the current context), and sampling (how a single concrete token is chosen from a probability distribution).

In Lecture 1 the model was called a "black box of stateless inference." Today we stop keeping it black. After this lecture, inside that box there will no longer be four unknowns, but four distinct stages, each with a clear role — and with concrete engineering consequences for how you will set tasks for the model.

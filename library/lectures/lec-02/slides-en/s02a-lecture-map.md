---
id: s02a
type: roadmap
duration_min: 0.5
assertion: "Lecture map — 6 sections"
learning_goal: "Общая карта: что будет, в каком порядке"
learning_outcomes: [LO1]
references: []
visual:
  pattern: lecture_roadmap_6_sections
  primary: "6 пронумерованных горизонтальных карточек по разделам (0 Введение / 1 Токенизация / 2 Эмбеддинги / 3 Внимание / 4 Сэмплинг / 5 Финал) с короткими описаниями. Активный раздел (Раздел 0) подсвечен gold-обводкой карточки — без текстового маркера, без минут."
---

# Lecture map — 6 sections

## Assertion

Lecture map — 6 sections.

## Visual

Six numbered horizontal cards by section with short captions: 0. Introduction; 1. Tokenization; 2. Embeddings; 3. Attention; 4. Sampling; 5. Wrap-up. Under each — a short one-phrase description, no minutes. The active section (Section 0) is highlighted with a gold card outline — no text marker.

## Speaker notes

Before we dive into the mechanics of large models — a short route map. The lecture has six sections, and each answers its own question.

Section 0, where we are now, is the introduction: what a token is, a brief recap of Lecture 1, and the central question we are here for.

Section 1 is tokenization. How the model "sees" your text. What a token is, how BPE works, why "strawberry" is split into three parts, and why Russian text costs the model twice as much as English.

Section 2 is embeddings. The space of meanings: how words turn into vectors, what semantic similarity is, and how semantic search and the bridge to RAG come out of this math.

Section 3 is attention. How the model decides which tokens to look at right now. We take the attention mechanism apart on a concrete example and understand why a prompt with the role "you are an expert" really does change the answer.

Section 4 is sampling. From a probability distribution to a single token. Temperature, top-p, top-k, max_tokens — the four API knobs you will turn every time you call an LLM.

Section 5 is the wrap-up. Closing the three "whys" posed in the central question. Comparing ML and LLM as two paradigms, the Human vs AI differences, the homework for the seminar, and the preview of Lecture 3.

Keep this map in your head — it will help you not get lost in the details. After each section we will stop and pin down the main point.

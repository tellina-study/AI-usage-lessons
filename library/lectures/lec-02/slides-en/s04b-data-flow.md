---
id: s04b
type: assertion_visual
section: "Раздел 1. Токенизация"
duration_min: 1
assertion: "Data flow in an LLM: words → tokens → vectors → LLM → vectors → tokens → words"
learning_goal: "Roadmap всего inference-конвейера перед детальным разбором каждого этапа"
learning_outcomes: [LO1]
chapter_ref: "§1 [for-slide-s04b]"
visual_brief: "Горизонтальный 7-stage pipeline с двусторонним показом туда-обратно. Этапы: 1) текст → 2) токены → 3) векторы → 4) LLM (внимание+forward) → 5) распределение → 6) токен → 7) текст. Стрелки направлены вправо. Над каждым этапом — иконка. Под каждым — короткая подпись."
---

# Visible content

## Title bar
"Data flow in an LLM — there and back"

## Body
[Sub-title 16pt italic]
*We will take each of these stages apart separately. Right now — the map as a whole.*

[Горизонтальный pipeline, 7 стадий, в Ocean rounded boxes]

```
[Text]  →  [Tokens]  →  [Vectors]  →  [LLM]  →  [Distribution]  →  [Token]  →  [Text]
"Hello"    [Hel][lo]    vec₁, vec₂   attention   p(token | context)  chosen     "Greetings"
                                     +forward
```

[Под каждым этапом — короткая подпись: «words», «id from vocabulary», «numeric», «inference», «probabilities», «sample», «de-tokenize»]

[Gold callout снизу]
**Only the boundaries are words. Inside the model — vectors. Today we take apart the 4 central stages: 1-3-4-5.**

## Speaker notes

Before going deep into each stage, let's look at the full picture — what happens between your request and the model's answer. This is a map we will return to: on the right side of each following section you will see which stage of this pipeline is currently in focus.

On the left — your input text: for example, `"Hello, world"`. The first transformation is **tokenization**: the text is cut into units from the model's vocabulary; `"Hello"` becomes, roughly, `[Hel][lo]`. These tokens are integers, ids from the vocabulary. This is the first of the four stages, and the very next Section 1 is devoted to it.

The next step is **embedding lookup**: each token id is mapped to a learned vector in the model's memory. The word disappears; what remains is a sequence of vectors. This belongs to Section 2.

Next comes **LLM inference**: a series of layers with the attention mechanism, which we take apart in Section 3. Here the model "thinks" — but it thinks over vectors, not words. Out of this processing comes another vector — a candidate for the next token.

That candidate vector is turned into a **probability distribution** over the whole vocabulary: "how plausible is it that the next token is this one? or this one? or that one?" A **single token** is chosen from the distribution through sampling — that is Section 4.

And the last step is the **reverse transformation**: the token id is turned back into text via de-tokenization. This step is almost symmetric to the tokenization at the very start, and it is usually assigned to that same first stage.

The main observation for practice: a "word" appears only at the boundaries — at the input and at the output. Everything happening inside the model is operations over vectors. Today's lecture is about those internal operations, without formulas but with an engineering understanding of what happens where.

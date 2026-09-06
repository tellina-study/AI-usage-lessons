# Lecture 2 — EN Glossary Lock

**Purpose.** This is the English glossary lock for course terminology, sourced from
`library/lectures/lec-02/deck.yaml` → `glossary_lock` (25 core terms) plus the
advanced-optional terms noted in that section's comment (prefill/decode, RoPE, YaRN, TTFT,
speculative decoding, MRL/matryoshka, adaptive thinking/effort, MoE).

**Scope.** Anti-drift reference for the bilingual production track (see CLAUDE.md §
"Bilingual Production Rule"). Translators working on `speech.en.md`, `deck.en.yaml`,
`slides-en/*.md`, and `chapter.en.md` for Lecture 2 **and future lectures** that reuse these
terms should follow the EN mappings below for consistency across the 16-lecture course.
Any deviation must be logged and cascaded to all lectures using the term, not just the one
being translated.

**Status.** Core-25 terms are locked (fixed mappings, mandatory). Remaining glossary_lock
terms and advanced-optional terms use standard ML/NLP English equivalents — also locked for
this course going forward.

---

## Core terms (fixed mappings — mandatory)

| RU term | EN term | Note |
|---|---|---|
| токен | token | Base unit of text as processed by the model. |
| токенизация | tokenization | Process of splitting text into tokens. |
| эмбеддинг | embedding | Vector representation of a token/text. |
| механизм внимания | attention mechanism | Core transformer component; do not shorten to just "attention" when referring to the mechanism as a concept. |
| контекстное окно | context window | Maximum span of tokens a model can attend to at once. |
| сэмплинг | sampling | Token-selection step during generation (as opposed to deterministic decoding). |
| распределение вероятностей | probability distribution | Output of the model's final softmax over the vocabulary. |
| авторегрессионный | autoregressive | Describes next-token-prediction generation. |
| слепота к буквам | letter blindness | Known LLM failure mode (e.g., counting letters in a word); keep as a named phenomenon, not a generic description. |
| рваный интеллект (jagged intelligence) | jagged intelligence | RU gloss retained in parentheses on first use in RU artifacts; EN artifacts use "jagged intelligence" alone. |
| батч-инвариантность | batch invariance | Property that output does not depend on batch composition/size. |
| инференс | inference | Model forward pass at serving time (as opposed to training). |
| гонка патчей | patch race | Course-specific term for the fast-moving cycle of model/tooling patches; do not translate literally as "patch war." |
| chat-шаблон | chat template | Formatting template that wraps turns for chat-tuned models. Moved to Lecture 3 (see deck.yaml comment) — included here for cross-lecture consistency. |
| glitch-токен | glitch token | Anomalous token causing unexpected model behavior. |
| KV-cache | KV-cache | As-is — do not expand or translate; standard term. |
| prompt caching | prompt caching | As-is — standard term. |
| constrained decoding | constrained decoding | As-is — standard term. |
| reasoning tokens / reasoning-токены (thinking) | reasoning tokens (thinking) | As-is. Use "reasoning tokens" as the noun phrase; "(thinking)" gloss retained parenthetically on first use, matching RU convention. |

---

## Remaining glossary_lock terms (standard EN equivalents — locked)

| RU term | EN term | Note |
|---|---|---|
| BPE (Byte-Pair Encoding) | BPE (Byte-Pair Encoding) | As-is — standard algorithm name, already bilingual in source. |
| семантическое сходство | semantic similarity | General term for meaning-based closeness between embeddings/texts. |
| cosine similarity | cosine similarity | As-is — standard term. |
| in-context | in-context | As-is — used as in "in-context learning"; do not translate to "в контексте" back-formation in EN artifacts. |
| температура | temperature | Sampling hyperparameter; do not confuse with unrelated general-English "temperature." |
| top-p (nucleus sampling) | top-p (nucleus sampling) | As-is — standard term. |
| top-k | top-k | As-is — standard term. |
| max_tokens | max_tokens | As-is — parameter name, keep literal/code-style formatting. |
| mixture-of-experts (MoE, гиганты) | mixture-of-experts (MoE, giants) | "Гиганты" (giants) refers to large MoE-based frontier models in course narrative; keep the parenthetical gloss in EN as "(MoE, giants)". |

---

## Advanced-optional terms (chapter-only, no mandatory recall)

Per deck.yaml comment: these appear only in the chapter deep-dive, not required for slide/speech
recall. Still locked for terminology consistency wherever they do appear.

| RU term | EN term | Note |
|---|---|---|
| prefill/decode | prefill/decode | As-is — the two phases of LLM inference. |
| RoPE | RoPE | As-is — Rotary Position Embedding, referred to by acronym. |
| YaRN | YaRN | As-is — context-extension method name (Yet another RoPE extensioN method). |
| TTFT | TTFT | As-is — Time To First Token. |
| speculative decoding | speculative decoding | As-is — standard term. |
| MRL (matryoshka) | MRL (matryoshka representation learning) | Expand acronym on first use in EN artifacts; "matryoshka" is a recognized borrowing in ML English usage, keep unitalicized. |
| adaptive thinking / effort | adaptive thinking / effort | As-is — refers to models dynamically adjusting reasoning depth/effort. |
| MoE | MoE | As-is — Mixture-of-Experts, referred to by acronym (see also full entry above with "giants" gloss). |

---

## Usage notes for translators

- When a term has an "as-is" EN form, do not add an article, gloss, or translation unless the
  RU source itself includes a parenthetical gloss (e.g., MoE, giants; MRL, matryoshka).
- Parenthetical RU glosses (e.g., «рваный интеллект» for jagged intelligence) exist to bridge
  RU readers to the English-origin term; in EN artifacts, drop the RU gloss and use the English
  term directly.
- If a new lecture introduces a variant or near-synonym of a locked term, do not create a new
  mapping ad hoc — flag it for a glossary update covering all lectures that use the term
  (see CLAUDE.md § "Bilingual Production Rule" — glossary lock is anti-drift across all 16
  lectures, not per-lecture).
- `consistency-checker` is expected to validate RU↔EN parity against this file for lec-02
  EN artifacts; deviations should be treated as REVISE-level findings, not polish.

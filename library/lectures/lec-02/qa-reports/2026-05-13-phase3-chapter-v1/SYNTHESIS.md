# Phase 3 Synthesis — Chapter Лекции 2 v1.0 critique

**Date:** 2026-05-13
**Phase:** 3 (chapter critique parallel by 3 critics)
**Artifact:** `library/lectures/lec-02/chapter.md` v1.0 (10,148 слов)
**Next step:** Phase 4 — book-editor revision → chapter v1.1

---

## Combined verdict: REVISE

- **methodology-critic:** APPROVE-WITH-POLISH (4 P1 + 7 P2)
- **fact-checker:** **REVISE** (2 P0 + 7 P1 + 4 P2) ← driver
- **reader-simulator (text-only):** APPROVE-WITH-POLISH (5 P1, no P0)

Combined max severity = REVISE (fact-checker). Book-editor revision required перед USER GATE A.

---

## P0 Issues (must fix — fact errors that students can falsify in 30 sec)

### P0-1 (fact-checker): Llama-3 tokenizer mis-attributed

**Issue:** Chapter в 3 местах (§1.1, §1.2, §Источники) утверждает что Llama-3 использует **SentencePiece**. Реально Llama 3 (Apr 2024) перешла на **tiktoken-based BPE** с vocab 128,256 токенов. Llama 2 использовал SentencePiece — Llama 3 нет.

**Fix:** Заменить «SentencePiece» → «tiktoken-based BPE (128,256 vocab)» в §1.1, §1.2, §Источники. Для разнообразия примеров можно оставить упоминание SentencePiece как использовавшегося ранее (LLaMA-2 / Mistral / T5) — historical note.

**Risk if not fixed:** Студент проверяет на Hugging Face за 30 секунд, замечает ошибку. Авторитетность лекции падает.

### P0-2 (fact-checker): `strawberry` token split likely wrong

**Issue:** Chapter §1.3 + §5.2 утверждают `strawberry` = `[straw][berry]` (2 токена). Современные tiktokenizers (`cl100k_base` / `o200k_base`) реально split как **3 токена `[st][raw][berry]`**. Central explanatory example for всего §1.3.

**Fix:** Verify через `python -c "import tiktoken; e = tiktoken.encoding_for_model('gpt-4o'); print(e.encode('strawberry'), e.decode(e.encode('strawberry')))"` ИЛИ через Tiktokenizer UI. Update пример: `[st][raw][berry]` (3 токена). Narrative остаётся валидным — «модель видит 3 токена, не 10 букв».

**Risk if not fixed:** Student-falsifiable в 30 sec. Central example failure.

---

## P1 Issues (≥5 → REVISE; here: 16 — need bundling в revision)

### Methodology-critic P1 (4)

| # | Issue | Section | Fix |
|---|---|---|---|
| M-P1-1 | Pearl spelling drift «Перла» vs «Пёрла» (Lec-1 canonical = «Перла») | §1.4, §5.4 | replace_all «Пёрла» → «Перла» |
| M-P1-2 | §4.3 cross-ref §3.3.1 «следствие 1» — phrase actually в §3.3 | line 386 | fix reference §3.3.1 → §3.3 |
| M-P1-3 | §2.2 Word2Vec passage exceeds 1-sentence note (plan §6 #12) — explicit king-queen equation в body text | §2.2 | shrink to historical aside (1 sentence) |
| M-P1-4 | «апельсинов-к-апельсинам» insider calque from «apples-to-apples» | §5.5 line 530 | replace with «единая сравнительная база» / «сопоставимые ответы» |

### Fact-checker P1 (7)

| # | Issue | Section | Fix |
|---|---|---|---|
| F-P1-1 | RU vs EN tokenization 2× cost — no citation | §1.4 | add explicit source («empirical: OpenAI tokenizer benchmarks, доступ {date}»); flag VERIFY-WEEK-OF |
| F-P1-2 | Cosine similarity numbers (0.85, 0.78, 0.05-0.15) — no empirical attribution | §2.2 | add «illustrative numbers; экспериментально измерены на `sentence-transformers/all-MiniLM-L6-v2` (или указать model)» |
| F-P1-3 | GPT-4 12288 dim — disputed leak | §2.1 | softer phrasing: «по утечкам — около 12288, но Anthropic / OpenAI не подтверждают; точное значение коммерческая тайна» |
| F-P1-4 | Context window cifры (3 точки) — quarterly cadence, need VERIFY-DAY-OF | §3.3 | already tagged; verify fallback narrative explicit |
| F-P1-5 | HF Playground availability + Meta-Llama-3-8B-Instruct — need day-of verify | §5.5 / s27 | already tagged; verify fallback list |
| F-P1-6 | Strawberry test status — lecturer pretest required | §1.3 + §5.2 | tied to P0-2 fix; reformulate as «`strawberry` режется на 3 токена; AI не видит букв» (без зависимости от модели «правильно считает» или «нет») |
| F-P1-7 | Bibliography hygiene — Bloomberg/Octoverse/DeepSeek listed но не cited в body | §Источники | remove uncited entries OR add citations в body |

### Reader-simulator P1 (5, substantive — student perspective)

| # | Issue | Section | Fix |
|---|---|---|---|
| R-P1-1 | §3.2 in-context steering / RLHF caveat подрывает payoff первого «почему» | §3.2 | shorten caveat to 1 sentence; emphasize main mechanism stronger; alternative explanations — speaker note level |
| R-P1-2 | §1.3 FACT-CHECK strawberry warning противоречит основному примеру | §1.3 | reformulate как «modern tokenizers split strawberry на 3 токена; AI не видит букв `s,t,r,a,w,b,e,r,r,y`» (decouple from «правильно ли AI считает») |
| R-P1-3 | §1.1 имена `o200k_base` / `cl100k_base` / SentencePiece — перегруз в первом знакомстве | §1.1 | remove names из 1st intro; вынести в §1.2 или later как «существуют разные вариации (cl100k_base в GPT, o200k_base в GPT-4o, tiktoken в Llama 3...)» |
| R-P1-4 | §2.1 различие «внутренние vs выходные эмбеддинги» implicit | §2.1→§2.2 | explicit мост: «эмбеддинг внутри модели (12288 dim) ≠ выходной API эмбеддинг `text-embedding-3` (1536/3072 dim); это разные сущности» |
| R-P1-5 | §4.4 шаг 2 forward pass — слишком плотное (KV-кэш скобка) | §4.4 | упростить: убрать KV-кэш скобку, оставить базовое «forward pass — это всё что мы прошли в §1-§3 одним проходом» |

---

## P2 Issues (11 total — bundle for v1.1 polish)

### Methodology P2 (7)
- §1.1 «анти-патология упрощения» — neologism, рассмотреть нейтральную формулировку.
- GPT-4 12288 dim — слишком prominent (cross-ref P1-3).
- 2 retrieval-вопросы без resolution в тексте — добавить answer hints в self-check.
- «логиты» — not highlighted at first usage.
- Multi-head paragraph — on edge of forbidden #11 (deep-dive); verify не слишком развёрнут.
- `[VERIFY-DAY-OF]` fallback — could be stronger explicit.
- (1 более minor — см. report)

### Fact-checker P2 (4)
- Vaswani 8 authors mention — already cited but verify exact authors list.
- Tokenizer cardinality — verify exact vocab numbers per model.
- DeepSeek context — match Lec-1 phrasing (if mentioned).
- (1 более minor — см. report)

---

## Per-`[FACT-CHECK]` marker disposition (from fact-checker)

11 markers; verdicts per fact-checker report. **Action для book-editor revision:**
- Markers с verdict **REWRITE** — apply fix.
- Markers с verdict **KEEP, VERIFY DAY-OF** — keep marker, add explicit fallback narrative.
- Markers с verdict **REMOVE marker but add citation** — promote uncertain claim to cited claim.

---

## Strong points (KEEP, не менять)

- 4 LO covered explicitly, payoff §5.3 mechanism-grounded.
- Tone explanatory-engineering — clean (no «магия LLM», «промптинг — сквозной навык»).
- Cross-refs Lec-1 — 9 callbacks helpful, не skipping.
- 3 cross-cutting frames adequate (§4.5 local/cloud, §5.3 ML vs LLM, §5.4 Human vs AI — last is best per reader).
- Self-check вопросы (17) — useful retrieval.
- All canonical arXiv citations verified (Vaswani, Liu, Sennrich, Mikolov, Holtzman).
- Cross-consistency Lec-1 — strong (MCP, ReAct, Pearl, Vaswani 8 authors, context windows).
- Curriculum sync — verified, no hallucinations.
- Concept introduction sequence — clean (core 4 концепта inline definitions OK).

---

## Phase 4 brief для book-editor (next step)

Cumulative scope: **2 P0 + 16 P1 + 11 P2 = ~29 edits.** Estimated 45-90 min wall-clock revision.

**Priority:**
1. **P0 fixes first** (Llama-3 tokenizer + strawberry split) — student-falsifiable, urgent.
2. **P1 fixes by category** — methodology / fact-checker / reader.
3. **P2 polish** — bundle.

**Revision discipline:**
- Cascade-of-changes tracking: каждый fix → list any downstream artifact references (slides, speech don't exist yet; just chapter — internal cross-refs).
- NO new content additions без brief.
- Preserve all 28 `[for-slide-sNN]` markers (positions могут sдвинуться, но IDs stay).
- Glossary lock preserved (chapter v1.1 must keep 17 canonical terms; no drift).
- Tone discipline preserved (no «магия LLM», no marketing).

**Save revised chapter as:** overwrite `library/lectures/lec-02/chapter.md` with `version: v1.1`, status=reviewed (after revision; book-editor can self-mark).

**Changelog requirement:** добавить «## Changelog v1.0 → v1.1» в начало с numbered list всех applied fixes (P0-1, P0-2, M-P1-1..., F-P1-1..., R-P1-1...).

---

**Конец Phase 3 synthesis.** Status: ready для Phase 4 book-editor revision.

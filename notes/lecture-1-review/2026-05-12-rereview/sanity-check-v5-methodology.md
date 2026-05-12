# Sanity Check v5 — Methodology — 2026-05-12

**Issue:** #67 (64.B Phase 1 of EPIC #64).
**Артефакт:** `notes/lecture-1-review/final/new-plan-v5-final.md`.
**База сравнения:** `methodology-critic.md` (v4) + `SYNTHESIS.md`.
**Источник:** агент `methodology-critic` (Opus 4.7). Сохранено orchestrator'ом.

## Verdict

**APPROVE-WITH-MINOR-FIXES.** Все 6 P0 из v4 закрыты, новых P0 не интродуцировано. 4 P1/P2 наблюдения **НЕ блокируют** Phase 2 (chapter draft). Готовность к **USER GATE 0**: ✅ да.

## P0 verify table

| # | P0 from v4 | Closed in v5? | How |
|---|---|---|---|
| MC-1 | Central question = magic-pill «попасть в 10%» | ✅ | s05/s14/s18/s27 + arc + tone-блок: «Где AI работает, где — нет, и как это понять?». «10% доходят до прода» оставлено как **факт стейкса**, не central frame |
| MC-2 | «инженер ИУ6» (6+ мест) | ✅ | search «ИУ6» по v5 → **0 совпадений** в основном тексте; явные tone-NOTE в s05/s18/s29 |
| MC-3 | LO7 wrong на s01 | ✅ | s01 = LO1 only; LO7 начинается с s21+; явный note для deck.yaml |
| MC-14 | Раздел 4 — 0 retrieval moments | ✅ | 2 momenta добавлены: s21+ (think-pair-share «найдите подделку», apply LO7), s22+ (reflection bias/sycophancy/shift, evaluate LO6) |
| MC-15 | s22 overload (6 концептов) | ✅ | Сжат до 3 связных (bias + sycophancy + distribution shift); RLHF/data poisoning/prompt injection — note для chapter (security/safety lecture) |
| MC-16 | LO6/LO7 только remember-level | ✅ | s21+ = apply LO7, s22+ = evaluate LO6, s28 consolidated note = apply LO1+LO6+LO7 (homework) |

**Все 6 P0 — закрыты чисто.**

## P1 sample check

| P1 from v4 | Status в v5 |
|---|---|
| s07 cognitive load (15 фактов / 4 мин) | ⚠️ Частично — UDIO note есть, но 9 дат + Tesler + 5 стартапов остались (см. New issue #1) |
| s08 карта без синтеза | ✅ Note для chapter — по 1 оси абзац |
| s09 — 6 цифр без assertion | ✅ **Образцовая assertion-evidence pattern** теперь |
| s18 cognitive overload (5 типов контента) | ⚠️ НЕ ЗАКРЫТО — структура s18 не изменена (см. New issue #2) |
| s12 split-attention | ⚠️ НЕ ЗАКРЫТО, но backup video стабилизирован (P1, не блокер) |
| s23 ARC-AGI gotcha | ✅ «honest framing, не gotcha» |
| s24 politicization без bias | ✅ Bias-disclaimer добавлен |
| s27 callback не работает на LO | ✅ Двойной callback (LO + тизер на лекцию 2) |
| s28 academic finale без CTA | ✅ Note для chapter — homework apply LO1+LO6+LO7 |

## New issues introduced (v5.1 candidates, ВСЕ P1/P2)

### New-1 (P1) — s07 cognitive load remains
- **Issue:** 9 дат + Tesler + 5 стартапов = ~3.5 факта/мин (Mayer threshold = 1/30сек = 2/мин). UDIO убран, но базовая плотность сохранена.
- **Fix v5.1:** note «на слайде только 4 жирные точки (1956 Дартмут, 2012 AlexNet, **2017 Transformer**, 2022 ChatGPT); остальное — серая шкала, в notes/chapter».

### New-2 (P1) — s18 split-attention сохранён
- **Issue:** s18 5 типов контента (квадранты + 4 вопроса + таблица + ответ + раздатка) за 3 мин. **Кульминация лекции** — особенно вреден.
- **Fix v5.1:** либо (a) расщепить на s18a (вопросы+ответ, 2 мин) + s18b (квадранты+таблица, 1 мин); либо (b) убрать квадранты в раздатку.

### New-3 (P2) — Tone «диагностический, не триумфальный» не enforced для chapter
- **Issue:** В блоке центрального вопроса tone прописан, но в `Notes для chapter author` нет явного пункта «диагностический tone» — book-editor может скатиться в «AI спасёт мир».
- **Fix v5.1:** добавить пункт #12 «Tone diagnostic, not triumphal: главный вопрос — про различение, а не про принадлежность к "правильным"».

### New-4 (P2) — Layered model только в chapter, не на slides
- **Issue:** Note для chapter про layered model (chat = model + UI + memory; agent = chat + tools + planning) есть, но **на slides этой диаграммы нет**. Chapter ≠ slides на этом узле — может всплыть на slides QA.
- **Fix v5.1:** добавить мини-диаграмму в s11 (анонс демо) ИЛИ оставить как есть (design tradeoff).

## Cross-cutting checks

| Aspect | Status |
|---|---|
| Tone consistency (uniform respectful «вы») | ✅ |
| Anti-patterns (magic-pill, local binding, politicization) | ✅ all closed |
| Хронометраж 75 мин с буфером | ✅ 66+2+2+7=75 (buffer 9.3% — на нижней границе для 2 живых демо) |
| Assertion-evidence | ✅ s09/s17 образцовые |
| LO coverage с Bloom levels | ✅ LO1 apply / LO4 apply / LO6 evaluate (s22+) / LO7 apply (s21+) |
| Sequence breaks (s10 mention agents до s16) | ⚠️ Не блокер, P2 |

## Recommendation orchestrator'у

1. **USER GATE 0: APPROVE v5 plan** — все 6 P0 закрыты, новых P0 нет.
2. **Phase 2 (chapter draft) можно стартовать.** book-editor получает v5 + 11 consolidated notes.
3. **v5.1 minor правки** (4 пункта) — опционально, batch'ем перед Phase 5 (slides update from chapter) ИЛИ если book-editor catches их inline.
4. **Critical для book-editor:** worked example для s18 — единственный путь от remember к apply для чек-листа.

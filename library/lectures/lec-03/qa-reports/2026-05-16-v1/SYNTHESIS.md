# Phase 7 (build-deck Phase 4-5) SYNTHESIS — deck v1 Лекции 3

**Дата:** 2026-05-16 · **Issue:** #87 · **Артефакт:** deck v1 (30 слайдов, rendered).

## Сводный вердикт: **APPROVE-WITH-POLISH** (0 P0 у всех 5; 1× APPROVE-CLEAN)

| Критик | Verdict | P0 | P1 | Ключевое |
|---|---|---|---|---|
| presentation-critic | APPROVE-WITH-POLISH | 0 | 3 | 30/30 5-сек pass; schema 8/8 PASS; оба PROPOSED ADDITIONS → ACCEPT; title=topic не assertion (~15, митигировано gold) |
| student-simulator | APPROVE-WITH-POLISH | 0 | — | контент сильный; s27 не читается из зала; s13/s24/s25 перегруз компоновки на низкой энергии |
| reader-rendered | APPROVE-WITH-POLISH | 0 | 4 | self-cont. 26/30=87%; s27/s07/s08/s16 — notes-fix (заметки не дублируют графики); 0 structural blocker |
| consistency-checker | **APPROVE-CLEAN** | 0 | 0 | слайды полностью сходятся с главой v1.1; 0 drift цифр/дат/терминов; book-first OK |
| fact-checker | APPROVE-WITH-POLISH | 0 | 2 | все видимые числа == глава; арифметика charts безупречна; c08/c16 — нужна illustrative-метка |

Условие build-deck Phase 6 «все critics APPROVE-WITH-POLISH/CLEAN, 0 P0» — **выполнено**. Одна fix-итерация (convergent P1) → pre-gate → GATE B.

## Fix-list (одна итерация, presentation-designer)

### Convergent (≥2 агента — приоритет)
1. **s27 матрица — снизить плотность [critic P2-3 + student P1 + reader P1].** НЕ удалять (payoff LO7, замыкает Air Canada финалом), НЕ редизайнить как блокер. Действие: 7×7 → сократить до читаемого (по образцу s17 4×3, который читается отлично): убрать наименее несущие колонки/строки ИЛИ расшифровать сокращения + легенда + усилить контраст gold/teal заливок (на PNG сливаются), нижняя плашка «детерм.→код» = доминанта. Цель: 5-сек + projector 50% + читаемость на снапшоте.
2. **s13 / s24 / s25 разгрузка компоновки [student].** Контент важный — НЕ резать. Уменьшить видимый текст (детали → speaker notes/глава), увеличить «воздух», s24 — добавить USER-actor иконку ИЛИ переклассифицировать subtype schema_architecture→schema_pipeline [critic P1-2].
3. **charts c08-context-rot + c16-forgetting — illustrative-метка [fact-checker P1×2 + reader].** На чарте: «схематично — иллюстрация эффекта» + атрибуция эффекта (Chroma 2025 / Luo arXiv:2308.08747) в подписи; подписи осей читаемы на снапшоте. Аналогично проверить читаемость подписей c07/s07.

### Single-agent / polish
4. **s06/s15 — усилить assertion-несущую gold-плашку** [critic P1-3] до уровня соседей.
5. **PROPOSED ADDITIONS — оба ПРИНЯТЫ владельцем (см. ниже):** PA-1 s04/s26 climb-scale label «проще ↓ / сложнее ↑»; PA-2 s13 mass-rebalance.
6. **s02 subtitle** — привести к канону lec-02 cover (без designer-инициативного «· 75 минут», если это не часть канонного cover-формата lec-02).
7. notes-fix [reader]: s07/s08/s16 speaker notes — добавить 1 фразу, привязывающую график к смыслу (столбец↔модель, линия↔«общие/целевые», ось↔смысл), т.к. подписи на снапшоте мелкие.

### Deck-level (owner-решение, см. вопрос пользователю)
8. **P1-1 title bar = topic-label, не assertion (~15 слайдов)** [critic, deck-уровень]. Митигировано: assertion несёт gold-плашка на каждом слайде. Полный ретайтл 15 слайдов = риск + отход от стиля lec-02/04. → решение владельца.

## Не фиксить (намеренно)
- consistency P2 D1–D3 (глифы кавычек / RAG-alias в notes / нумерация кейсов) — намеренная introductory-деривация, book-first OK.
- Чистых P1-DELETE слайдов нет (student: каждый несёт урок; проблема — плотность/позиция, решается разгрузкой).

**После fix → Phase 6.5 pre-gate walkthrough (mode=slides) → USER GATE B.** Архив v1 перед итерацией.

# Phase 7 (build-deck Phase 4-5) SYNTHESIS — deck v1 Лекции 4

**Дата:** 2026-05-16 · **Issue:** #99 · **Артефакт:** deck v1 (32 слайда, rendered).

## Сводный вердикт: **REVISE** (presentation-critic P0+6P1 governs)

| Критик | Verdict | P0 | P1 | Ключевое |
|---|---|---|---|---|
| presentation-critic | **REVISE** | 1 | 6 | **P0: видимые `[VFY]`-метки** (s12/21/22/27/28) — рецидив Л2-R1; §/sNN/LO-leak ~16 слайдов; 3 декор-chart без подписей; 5-сек fail s03/04/13/17 |
| student-simulator | APPROVE-WITH-POLISH | 0 | — | контент/арка сильные; s19–s23 5 одинаковых layout (потеря внимания); s29 20 ячеек не из зала; charts-шум; P1-DELETE s28, CONSOLIDATE s26 |
| reader-rendered | APPROVE-WITH-POLISH | 0 | 1 | self-cont 27/32=84%; 5 неавтономных (s06/08/12/13/17) = ОДНА причина: bar-charts без подписей; confused-deputy s16 notes без глосса; 0 structural |
| consistency-checker | APPROVE-WITH-POLISH | 0 | 1 | chapter↔slides сильно (0 drift, citation CLEAN, 0 orphan); P1 = visible §/sNN/LO leak (slide-side, book-first chapter верен) |
| fact-checker | **APPROVE-CLEAN** | 0 | 0 | все числа/charts == глава v1.1; старые citation-ошибки НЕ вернулись; P2 s01 знак −24% |

Конвергенция: §/sNN/VFY-leak (4 агента), декор-charts без подписей (3 агента), s19–s23 монотон + s29 плотность (student/reader). Не концепт — мех. правки + ритм.

## Fix-list (одна итерация v1→v2, presentation-designer)

### P0 (блокер)
1. **Strip ВСЕХ `[VFY]`/`[VFY-day-of]` с видимого слоя** (футеры s12/s21/s22/s27/s28 + grep все 32) → ТОЛЬКО speaker notes. plan §7 / anti-pattern #36 / рецидив Л2-R1 P0.

### P1 (must-fix)
2. **Strip visible §-номера / (sNN) / (Раздел N) / LO4 / §-refs чужих лекций** из Body+Footer ~16 слайдов (s03/s04/s06/s09/s11/s15/s16/s17/s20/s21/s23/s24/s25/s30/s32). Замена на контент-формулировку (имя-риска / «далее» / «на семинаре» / «как в Лекции 3»). Speaker notes уже чисты — зеркалить их регистр. anti-pattern #37/#38/#39, consistency-P1, book-first (главу НЕ трогать).
3. **3 декор-bar-chart без подписей s06/s12/s17 (+ s08/s13)** — главная причина 5 неавтономных слайдов (reader) + «перестал смотреть» (student). Либо подписи осей+data-labels ≥14pt, либо заменить на крупные mega-stat числа (стиль s01-плашек, который РАБОТАЕТ). s13 GitClear → 3 крупных trend-числа.
4. **s16 `confused-deputy`** — добавить локальный мини-глосс в notes (термин определён inline на s23, но первое упоминание s16 — нужен глосс там).
5. **s19–s23 ритм** — 5 слайдов идентичного layout «слева данные/справа урок/плашка» подряд на падающей energy. Сломать визуальный ритм минимум одним иным layout раньше s24 (single-focus / иная композиция).
6. **s25/s29 — убрать subtitle-легенду цвета** («золото SOLID = … бирюза SOLID = …») как инструкцию к чтению (designer-extra, student). Цвет говорит сам. s29 (20 ячеек, 68-я мин): усилить доминанту нижней gold-плашки + 2–3 ключевые оси крупно ≥14pt; читаемость из зала — приоритет (полная сетка как референс — ок в notes/главе).

### P2 (тот же проход)
- s01: явная знаковая легенда «ожидали ускорение −20% / получили замедление +19%» (fact-checker P2 + это и есть «ошиблись на знак» — не двусмысленно).
- s26: убрать англ. Brooks-цитату с видимого (→ notes), оставить русскую суть; доминанта = «AI амплифицирует то, что есть».

### Owner-решения (выношу на USER — judgment, не мех.)
- **s28 (docs-as-code):** student RECOMMEND DELETE (прошёл мимо на energy 55%); но это owner-бриф-пункт + честный «частично-подтверждено» (judgment-ценность). → решение владельца: удалить vs оставить-пунчевее.
- **s26 (Brooks/DORA):** student CONSOLIDATE в s25; но s26 = 5-я точка возврата ЦВ + owner-бриф «практики не уходят». → решение владельца: оставить-пунчевее vs слить в s25.
- **s29 матрица:** упростить для проекции (плашка+2-3 оси) vs оставить полную 20-ячеечную + только крупнее. (reader: на снапшоте читаема через zoom; student: не из зала на 68-й мин.)

## Не фиксить / уже ок
fact-checker APPROVE-CLEAN — числа/charts/citations верны, не трогать данные. consistency P2 (confused-deputy глосс-вариативность, 55/56 shorthand) — owner-tolerance, report-only. Историч. chapter changelog упоминания старых ID (2310.02059/756k) — корректны (документируют фикс).

**Orchestrator-fix (не артефакт-гейт):** plan-v2-final §2.2 устарел — 5-я точка возврата = s26 (не s27), точка 4 = s21+s23. Поправить план напрямую.

**После fix → re-QA delta (presentation-critic + reader-rendered + consistency) → pre-gate mode=slides → USER GATE B.**

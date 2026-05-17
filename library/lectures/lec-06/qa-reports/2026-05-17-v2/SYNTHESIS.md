# Лекция 6 — SYNTHESIS Phase 7 (slides render v1, 32 слайда)

**Issue:** #101 · **Дата:** 2026-05-17 · **Ветка:** `issue-101-lec-06-engineering-cad`
**Вход:** presentation-critic · student-simulator · reader-rendered · consistency-checker · fact-checker · methodology-critic (qa-reports/2026-05-17-v2/)

## Вердикты

| Критик | Вердикт | P0 | P1 | P2 |
|---|---|---|---|---|
| presentation-critic | APPROVE-WITH-POLISH | 0 | 3 | 7 |
| student-simulator | APPROVE-WITH-POLISH | 0 | 4 (+3 P1-DELETE) | 4 |
| reader-rendered | **APPROVE-CLEAN** | 0 | 0 | 1 |
| consistency-checker | APPROVE-WITH-POLISH | 0 | 0 | 4 |
| fact-checker | **APPROVE-CLEAN** | 0 | 0 | 2 |
| methodology-critic | APPROVE-WITH-POLISH | 0 | 3 | 5 |
| **Итого** | **APPROVE-WITH-POLISH** | **0** | **дедупл. 7** | **~15** |

**Counter-check:** 0 P0; ни один REVISE-триггер. **slides strict-in: консерв. 35.6% (consistency) / 37.5% слайдов · 46.4% мин (methodology), harshest-floor 31.3% — ≥30% соблюдён, holistic по Частям 2–5** (не single-section), замер по deck'у (не «взаймы» из chapter). L6 owner-waiver недоступен — выдержан строго. Рецидив матбазы **НЕТ** (s11/s16/s18/s26/s31 чисты, s18 — эталон). Cascade SYNTHESIS-v1 закрыт полностью на PNG. Self-containedness 32/32. Факты: deck чист, 0 visible-leak. → **Phase 8 = визуальный polish, НЕ пересборка, БЕЗ ренумерации.**

## Решение по структуре (orchestrator curriculum-relevance check)

student-simulator предложил **P1-DELETE s08 / CONSOLIDATE s07+s08**. **ОТКЛОНЕНО как удаление, ПРИНЯТО как визуальная де-монотонизация:** s07 (опт.ML + суррогат/PINN) и s08 (генеративный AI/LLM + CV + GA) покрывают РАЗНЫЕ классы — это несущее LO1 (классифицировать все 6). «Дубль» — это ФОРМАТ (одинаковая таблица ДА/НЕТ/альт.), не контент. Слияние = либо потеря покрытия классов, либо 5–6 классов на экран (регресс к overload — исходный грех Phase-1). Ренумерация всего deck'а ради этого = непропорциональный cascade. **Решение: 32 слайда остаются; чинить монотонность визуально + сигнал s06 «скелет, не заучивать сразу» + дифференцировать вёрстку s07≠s08.** Это No-Extra-Content + без регресса + без лишнего cascade.

## P1 — must-fix перед GATE B (Phase 8, ОДИН presentation-designer, Polish Round, render-reloop затронутых)

1. **[pres-critic P1-1] Вертикаль канвы недоиспользована** на ~12 content-слайдах (s05/s10/s12/s13/s14/s16/s17/s21/s23/s24/s27/s28): контент в верхних ~60%, низ пуст. Масштабировать Ocean-box + body до ~85–90% высоты (baseline lec-07). **Контент НЕ добавлять** — только масштаб/композиция.
2. **[pres-critic P1-2 / student] s26** (judgment-ядро, таблица 8×3): projector-test borderline на задних рядах. После масштабирования (P1-1) проверить реально ≥14pt @150dpi; если не проходит — сократить формулировки колонок, **split s26a/s26b только если иначе нечитаемо** (строки НЕ резать — ≥30% bucket). Schema-Readability §5.5 PASS обязателен.
3. **[pres-critic P1-3] Designer-extras в speaker_notes:** убрать видимые мета-подписи cross-ref: s11 «детали — в главе», s23 «на следующем слайде», s24 «на предыдущем слайде», s13 «(vendor-claim)…в главе». Notes = студенческий текст, не авторская мета (контент notes не трогать, только снять мета-фразы; держать 150–300 слов связного).
4. **[methodology P1-3 / pres-critic / student] s02 hook:** заменить абстрактный эскиз кронштейна на узнаваемое «органическое»/бионическое изображение (stock/Wikimedia, лицензионно-чистое). Это ГЛАВНЫЙ hook (4 мин, самый долгий content) — концепт-диссонанс «органика ≠ нейросеть» должен бить визуально.
5. **[methodology P1-2 / student / reader P2] s31:** полная матрица 6×4 — мелкая, не читается с задних рядов; payoff прогрессии s06→s31 проигрывает чек-листу. Поднять читаемость матрицы (≥14pt @150dpi) СОХРАНЯЯ доминирование чек-листа (иерархия из Phase-6 P1 — не сломать). Баланс «чек-лист доминирует + матрица легибельна».
6. **[methodology P1-1 / student s06–s08 sag] s06 + де-монотонизация s07/s08:** на s06 добавить visible-сигнал «справочный скелет — 6 классов не заучивать сразу, собираются по ходу» (как калибровочная фраза s07 в notes, но видимо/коротко). Вёрстку s07 vs s08 визуально дифференцировать (разные акценты/группировка), чтобы s06→s07→s08 не читались тремя одинаковыми плитами (провисание мин 12–14). Контент/счёт классов НЕ менять.
7. **[student / pres-critic 5-сек fail] s18 график PINN:** подписи налезают на кривые — схема нечитаема за 5 сек (хотя семантика-эталон). Перекомпоновать подписи/легенду так, чтобы «сглаживание пика у концентратора» читалось с проектора. Schema-Readability §5.5.

## P2 — взять в тот же проход

- **Опечатки/формулировки:** s04 «шестии»→«шести»; s09/s11 даты-формулировка (1904/1847/1988/1989 не как хроно-ошибка — пометить «родословная, не хронология»/упорядочить аннотацией); s32 backup-prompt 3 грамматика.
- **Lec-N-1 wording:** s32 «office hours»→«консультации»; roadmap-карта (s03) «Hook»→«Старт».
- **Аббревиатуры first-use на слайде:** POD, LPBF, КИИ — расшифровать при первом visible-употреблении.
- **deck.yaml:123** s06 manifest указывает «матрица на s30» — фактически s31; поправить stale-pointer (не student-visible, гигиена; D1 consistency).
- **Терминология (D2 consistency):** «топ-оптимизация» (16× в slides) → канон «топологическая оптимизация» (chapter/glossary canonical), хотя бы first-use полная форма.
- Убрать дубль курсив-заголовков/мета-ремарок s07/s11/s14/s22 (student/pres-critic P2).
- **fact-checker P2 (pre-flight, НЕ правка слайда):** ORCA-диапазон / Ansys SimAI релиз / Altair-заявление — TOP-3 day-of sanity (подача на visible уже консервативна, маркеры не ставить).

## НЕ делать
- НЕ ренумеровать deck (32 слайда фиксированы); НЕ резать строки s26 / контент Части 5 (≥30% bucket); НЕ добавлять слайды/subtitle/callback (No-Extra-Content); НЕ трогать содержание speaker_notes кроме снятия мета-фраз (P1-3); НЕ менять assertions/спайн (book-first, chapter approved).

## Решение оркестратора
Phase 8: **один** presentation-designer (Polish Round) применяет 7 P1 + P2 одним проходом, render-reloop затронутых слайдов (min 3 iter, Schema-Readability §5.5 для s26/s18/s31/s06), один коммит. Затем Phase 8.5 pre-USER-GATE walkthrough mode=slides (visual sweep + designer-extras grep + notes sample + cascade), sync артефактов в main repo, затем USER GATE B.

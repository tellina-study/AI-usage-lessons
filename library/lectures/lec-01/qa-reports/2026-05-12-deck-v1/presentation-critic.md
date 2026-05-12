# Presentation Critic — deck v1 (30 slides) — 2026-05-12

**Источник:** агент `presentation-critic` (Opus 4.7). Сохранено orchestrator'ом.

## Verdict
**WARN — APPROVE-WITH-MINOR-FIXES** (3 P0 blocker).

## Severity counts
- P0: **3**
- P1: **11**
- P2: **14**

## P0 — критические блокеры

### 🚨 P0-1 — s05a: UNFILLED PLACEHOLDERS
Слайд содержит литералы `[Имя Фамилия]`, `[N лет]`, `[работа с моделями / проектами]`, `[личная мотивация — заполнит преподаватель]`, `[хобби / факт — снижает дистанцию]`, инициалы «КМ» в monogram. **Нельзя показывать.** Либо placeholders заполнить реальными данными преподавателя, либо слайд выбросить из показа и сделать speech-only intro. `status: draft-pending-content` в frontmatter подтверждает.

### 🚨 P0-2 — s21: Vectara HHEM chart сломан
Видно 2 длинные tealOcean бары + крошечная бар с gold-фрагментом. **Нет axis labels, нет числовых значений, нет шкалы.** Должно быть: horizontal range bar (0%—15%) с маркерами по типам задач или scatter dots на линии 0-15%. Сейчас нечитаемо.

### 🚨 P0-3 — s23: ARC-AGI bar chart labels overlapping
Видно 2 bars (top deep navy, middle gold) и обрезанный мелкий внизу. Labels ($30/задачу, $2.20/задачу, $50–150/час) overlapping. Имена бенчмарков (Средний человек / Refinement Gemini 3 Pro+Poetiq / Single-model Opus 4.5 Thinking) не закреплены под bars. Слайд непригоден без перерисовки chart'а.

## P1 — важные (11)

| # | Slide | Issue |
|---|---|---|
| P1-4 | s05b | Красный «нет» в central question — anti-pattern #2 (без красного). Заменить на gold underline. + central question box выглядит как 2 stacked box (визуальный bug) |
| P1-5 | s15 | Cards имеют **черные strokes** вместо teal `#1C7293` (нарушение visual motif). |
| P1-6 | s25 | Pearl pyramid использует **bleached red/yellow/green** colors вместо Ocean gradient или gold-shades. |
| P1-7 | s16 | Autonomy ladder — все 5 уровней одинаковы. Уровень 5 (Observer) должен быть gold (max autonomy). |
| P1-8 | s01 | Левая колонка под assertion имеет огромную пустую серую зону. Hero metric «31 fps · без интернета · 2023» нужен gold callout, не мелкая 16pt подпись. |
| P1-9 | s08 | Assertion в 2 строки с wrap «архитектура.» на отдельной строке. Сократить в 1 чистую строку. + Visual pattern declared «four_axes_compass / Радиальная композиция» но факт — plain 2×2 cards. |
| P1-10 | s11 | Assertion 2 строки rocky (вторая короче). Объединить и сократить. |
| P1-11 | s14 | Assertion слишком длинный (3 строки). Сократить. |
| P1-12 | s09 | 4 metric cards: «$244-390B» подпись «AI-рынок · разброс — методология» — три семантических уровня в одной строке. + Counter-fact band «90% AI-пилотов не доходят до прода» свалены 3 факта в одну строку. |
| P1-13 | s04 | Donut слева заметно меньше bar chart справа — должны быть равной visual mass. + chart titles inconsistent style (donut large bold vs bar 14pt italic). |
| P1-14 | LO7 coverage | LO7 покрыт ТОЛЬКО на s19, s21 — слабо. retrieval moment на s21 declared в deck.yaml но не виден на slide. |

## P2 — косметика (14)

- **s02:** accent line под кикером «ЛЕКЦИЯ» — anti-pattern (на cover, но повторяет паттерн).
- **s03:** «Вопрос 1» / «Вопрос 2» в teal мелковато; chip-pills для Q1 fill, для Q2 outline — outline теряет контраст текста.
- **s04 footer:** избыточная methodology-строка (уже в caption каждого chart).
- **s06:** обе колонки идентичны — нет visual hint «инженерное = рабочее в курсе»; gold band внизу 12pt не читаем с расстояния.
- **s07:** labels years overlapping (2012/2017); gold callout AI Effect одной длинной строкой.
- **s09:** insight «доверие падает» идёт ровным текстом, должен быть takeaway-выделен.
- **s10:** «капотери» typo/неологизм — заменить на «потерь капитализации».
- **s12:** footer «Demo: live + audio-backup. Код: assets/code/three-ways/» — methodist comment, anti-pattern #9 (в speaker notes).
- **s13:** middle-dot separator visually heavy в case-карте.
- **s17:** 9 brand names в 8-cell grid (overflow); text-cells вместо real logos.
- **s18:** «методичка §3.8» — methodist comment на slide, anti-pattern #9.
- **s20:** EU AI Act fines + breakeven — два разных факта в одной footer-полосе.
- **s22:** «ПОДЛИЗЫ» как термин для sycophancy — разговорно, лучше «УГОДЛИВОСТЬ» или оставить английское.
- **s26:** «4 После блока» typography — глиф «4» рендер-bug; «вытащить из 00-course» footer = methodist comment.
- **s28:** Cards 1-3 одинаковы — нет hierarchy of importance; homework callout мелким; должен быть критический CTA.
- **s29:** Q&A провокация потеряна на самом slide (только в backup).

## Cross-deck

### Pacing
✅ Сумма 66.5 + buffer 8.5 = 75 мин. Реалистично.
⚠️ Раздел 3 тяжелый (8 slides s11-s18) — лектору нужно держать темп.

### Narrative arc
✅ Хороший общий arc.
⚠️ Мост s05a → s05b проблемный (s05a unfilled).
✅ s27 callback к s01 — крутой move.
⚠️ s29 Q&A теряет provocation.

### LO coverage
- LO1: massive (s01-s18). ✅
- LO4: хорошо (s05b, s11-s18). ✅
- LO6: глубоко (s19-s25). ✅
- **LO7: слабо** — только s19, s21. **P1**.

### Visual consistency
- ✅ Палитра преимущественно соблюдена.
- ❌ Нарушения: s05b красный «нет», s15 чёрные strokes, s25 bleached red/yellow/green pyramid.
- ❌ Gold ≥1×/слайд правило нарушено: s01, s03, s06, s15.
- ✅ Visual motif Ocean rounded box почти везде.
- ✅ Cover s02 distinct.
- ⚠️ Footer-tax (anti-pattern #14) на s12, s18, s26 — methodist comments.

### Связь с chapter v2
- ✅ Slides assertions реально вытащены из chapter sections.
- ✅ Central question, timeline, ARC-AGI stats — все matches chapter.
- ⚠️ Chapter §4.5 (model inversion, adversarial) НЕ отражён в slides — только sycophancy в s22. Stub-mention стоит добавить.

## Топ-N правок для Phase 8 revision

### P0 (3 — обязательно)
1. **s05a:** заполнить placeholders ИЛИ удалить из показа (speech-only intro).
2. **s21:** перерисовать Vectara HHEM как horizontal range bar с маркерами задач.
3. **s23:** перерисовать ARC-AGI с labels под bars + цены не overlapping.

### P1 (11)
4. **s05b:** убрать красный «нет» → gold underline; пересобрать question box (1 rounded box).
5. **s15:** черные strokes → Ocean teal `#1C7293`; gold underline у winning card.
6. **s25:** Pearl pyramid → Ocean gradient (deep/mid/light) или pure gold-shades.
7. **s16:** Уровень 5 (Observer) → gold; остальные 4 — Ocean shades.
8. **s01:** усилить hero «31 fps · без интернета · 2023» (gold metric callout).
9. **s08:** assertion в 1 строку.
10. **s11:** assertion объединить и сократить.
11. **s14:** assertion в 2 строки + (от reader/student) **разнести bar chart с s04 — дубль убивает внимание**.
12. **s09:** разнести «$244-390B» подпись на 2 строки + counter-fact band hierarchy.
13. **s04:** donut/bar равной visual mass + consistent chart titles.
14. **LO7 coverage:** добавить retrieval moment на s21 (declared, но не виден).

### P2 (14 — на усмотрение)
15. Footer cleanup (anti-pattern #14): s12 «Demo:», s18 «методичка §3.8», s26 «00-course».
16. Gold accent ≥1×/slide: s01, s03, s06, s15.
17. s17: real logos или 6-cell grid.
18. s29 provocation как assertion.
19. s22 «ПОДЛИЗЫ» → «УГОДЛИВОСТЬ».
20. s09 «AI-рынок» — clean подпись.
21. s10 «капотери» → «потерь капитализации».
22. s28 Card 3 крупнее; homework callout сократить.
23. s07 labels years (2012/2017 overlap); AI Effect callout split.
24. Stub-mention chapter §4.5 (model inversion, adversarial) на s22 или s25.
25. s05b funnel labels мелкие — увеличить.
26. s06 gold band внизу 12pt → 16pt.
27. s20 разнести EU AI Act + breakeven в 2 строки.
28. s26 «Вы здесь» в Блок 1 явно обозначить.

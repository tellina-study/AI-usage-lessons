# SYNTHESIS — slides v3 (34 slides) — Phase 12.4 critics — 2026-05-13

**Issue:** #70.
**Артефакт:** `library/lectures/lec-01/rendered/lec-01.pptx` v3 (34 slides) + `library/lectures/lec-01/slides/*.md`.
**4 critics (Opus 4.7):** presentation-critic + student-simulator (×2 run для надёжности) + reader-simulator(rendered) + fact-checker.

## Общий verdict

**✅ APPROVE-WITH-MINOR** во всех 4 критиках. **Closure 23/23 user fixes = 100%** (presentation-critic visual evidence). **0 P0** во всех reports (один P0 от student-batch1 — `s05a placeholders` — это acknowledged exclusion из REQUIREMENTS §0.3).

| Critic | P0 | P1 | P2 | Verdict |
|---|---|---|---|---|
| presentation-critic | 0 | 6 | 8 | APPROVE-WITH-MINOR |
| student-simulator | 0 (1 acknowledged) | 5-6 | — | «ЗАШЛО, местами провисает» |
| reader-rendered | 0 | 6 | — | APPROVE-WITH-MINOR (28/34 self-contained) |
| fact-checker | 0 | 4 | 5 | APPROVE-WITH-MINOR |
| **После дедупликации** | **0** | **~12 уникальных** | **~10** | APPROVE-WITH-MINOR |

## Convergent findings (≥2 критика согласны)

### КОНВЕРГЕНЦИЯ A — s28 Pearl + s26 ARC-AGI: кандидаты на удаление/сокращение
- **student-simulator** P1: «s28 Pearl на 65-й минуте — слово "контрфактуальность" убивает уставший мозг; полез в телефон». «s26 ARC-AGI без объяснения зачем для лекции 1».
- **reader-rendered** P1: «зачем s28 Pearl именно в лекции 1 — непонятно даже из notes; кандидат на удаление в духе #18». «s26 ARC-AGI для подготовки к семинару низкая релевантность».
- **Fix options:**
  - (a) Удалить s28 + s26 → раздел 4 = 5 slides вместо 7, освободить ~5 мин на повторное обращение к чек-листу или Q&A.
  - (b) Объединить s26 + s27 в один слайд (экономика + 4 спикера на одной странице).
  - (c) Оставить как есть с лучшими transitions/мостами — оба слайда содержат критическое мышление, ценное даже если конкретика забывается.

### КОНВЕРГЕНЦИЯ B — «Приложение-робот» — новый термин без объяснения
- **student-simulator** (batch 2): «"Приложение-робот" звучит странно, слово "робот" вызвало путаницу».
- **reader-rendered**: «терминологическая нестыковка "Приложение" (s20: Notion AI/Translate) vs "Приложение-робот" (s21: ETL+AI без UI)».
- **Fix:** в s20 ИЛИ в speaker notes s21 объяснить **2 типа приложений**: с интерфейсом (Notion AI, Translate) и без интерфейса (ETL-pipeline). На квадранте — «Приложение (автоматизация)» вместо «Приложение-робот».

### КОНВЕРГЕНЦИЯ C — s05a placeholders
- **student-simulator** (batch 1) P0: «убивает доверие на 5-й минуте, после чего студент уходит в телефон».
- **reader-rendered** P1: «через 2 недели не помню кто читал, placeholder и в notes».
- **presentation-critic** P2 (acknowledged).
- **Status:** REQUIREMENTS §0.3 — out of scope текущего ребилда (заполняется лектором перед лекцией).
- **Recommendation:** оставить как есть для пилота; в production deck лектор должен заполнить **до** показа.

## Уникальные P1

### От presentation-critic (6 visual)
1. **s05b funnel «10% в проде» wraps awkwardly** в gold плашке. Fix: расширить ширину или переформулировать «10% доходят».
2. **s13 axis labels мелкие** (16-18pt вместо ~10), укрупнить «↑ высокий / ↓ низкий».
3. **s15 model pipeline — RU/EN под-метки смешаны** (camera frame/resize/inference). Fix: унифицировать на RU.
4. **s17 chat-case — рендер слайда меньше остальных, тесные боксы**. Fix: расширить кейс-бокс.
5. **s21 axis labels Q1=Да/Нет вынесены ЗА правую границу квадранта** — визуально оторваны.
6. **s07 timeline — gold-точка 2017** ОК, но дату «2017» можно сделать крупнее «Attention Is All You Need».

### От fact-checker (4)
7. **s08 «90% откатов» — нет n=50 caveat** в speaker notes (inherited unresolved P1 из chapter v1).
8. **s26 ARC-AGI 37.6% Claude Opus 4.5 Thinking — устаревает.** Live verification: к 13 мая 2026 Claude Opus 4.6 = 68.8%, GPT-5.5 = 85%. Disclaimer есть, но число читается как актуальное.
9. **s07 speaker notes Vaswani «160K+ цитирований»** без timestamp («на сегодня» вместо «на май 2026»).
10. **s30 speaker notes «PARTS = Persona/Action/Recipe/Template/Specification»** — не каноническая аббревиатура prompt-engineering literature (inherited unresolved P1 из chapter v1).

### От student/reader (5)
11. **s13 рассинхрон speaker notes vs визуала** — critical: speaker notes говорят «Модель в правом-нижнем», на слайде она в **левом-верхнем** (координаты visually корректны, but notes неверны). Если лектор зачитает — путаница.
12. **s19 5 уровней автономии — мелкий шрифт описаний** под именами Operator/Collaborator/Consultant/Approver/Observer.
13. **s25 иконки bias/sycophancy/shift светло-серые** (вместо teal), визуально слабее.
14. **divider перед разделом 5 (заключение) отсутствует** — DoD §10 требует, но s28 → s29 переходит без divider.
15. **«Раздел 0» в s02a карте лекции** — путает (думал, что 5 разделов, а тут 0+5=6). Fix: переименовать в «Открытие» или дать заголовок «6 разделов».

## P2 (на усмотрение)

- s01 не использует Ocean rounded box motif (external_demo — допустимо).
- s06 grid 2×2 чуть плотный.
- s10 divider — outline letter серым по белому, может казаться блёклым на проекторе.
- s11 layers — типография левой колонки разнородная.
- s18 ОРКЕСТРАТОР как gold-filled блок — нестандартное использование gold.
- s30 — visual mass Module 1 (8 лекций) vs 2/3 (4/5) несбалансирована.
- s27 Hassabis/Amodei prediction упрощён в table — допустимо для table-формата.
- s17 bar chart 5 LLM РФ (повтор s04 в другом контексте) — допустимо.

## Сильные стороны (НЕ менять)

✅ **closure 23/23 user fixes** — все user правки applied (visual + structural evidence).
✅ **0 фактических ошибок** на 50+ verified claims (slides точно derive из chapter v3.1).
✅ **0 регрессий с v2.1**.
✅ **Speaker notes — образцовое выполнение #1**: связный читаемый текст 250-440 слов на каждом sampled слайде, derived из chapter v3.1, отдельный блок «Лектору».
✅ **Палитра LOCKED Ocean + Teal + Gold** — 100% deck'а.
✅ **0 footer-tax** на всём deck.
✅ **0 неестественных англицизмов** в visible content.
✅ **Visual motif Ocean rounded box** на каждом content slide.
✅ **Gold ≥1×/слайд** — гарантировано.
✅ **6 новых схем (s12, s13, s15, s16, s18, s21, s27) методически сильные** — особенно **s16 (chat 6-step loop)** и **s27 (4 speakers AGI table)** = образцовое исполнение.
✅ **Cover (s02) distinct** от content slides.
✅ **Dividers (s02a/s10/s14/s22)** — навигационные якоря с roadmap-bar и «Вы здесь».
✅ **Tone diagnostic, не magic-pill** — особенно s09 («не отчаивайтесь») и s27 (разбор stakes без обвинения).
✅ **Pacing 67 min active + 8 buffer = 75** OK.
✅ **Self-containedness 28/34** — главный фикс #1 (notes как читаемый текст) сработал.
✅ **Главный методический инструмент s21 (чек-лист 2 вопроса + квадрант)** — student: «работает, я бы применил прямо сейчас».

## Топ-N правок для Phase 12.4 revision (приоритезированно)

### Critical (must-fix перед GATE для slides — 4 правки)
1. **s13 рассинхрон notes ↔ визуал.** Speaker notes говорят «Модель в правом-нижнем», на слайде — в левом-верхнем. Зафиксировать notes в соответствие с визуалом (или наоборот). Это важно — лектор зачитает и собьёт студента.
2. **«Приложение-робот» терминология** в s21 + s20: явно объяснить 2 типа приложений (с UI / без UI). Можно переименовать в s21 «Приложение (автоматизация)» вместо «Приложение-робот».
3. **s26 ARC-AGI 37.6% устаревает** — pre-flight checklist «проверить arcprize.org за день, обновить число если изменилось». Либо переформулировать «один из самых дешёвых single-model результатов».
4. **divider перед разделом 5** — добавить slide или вынести в s29 navigation marker. (DoD §10 требует.)

### High-value (P1, 6 правок)
5. **s05b funnel «10% в проде»** — fix wrap.
6. **s13 axis labels мелкие** — увеличить.
7. **s15 RU/EN под-метки** — унифицировать.
8. **s21 axis labels Q1/Q2** — вернуть в квадрант.
9. **s08 n=50 caveat** в speaker notes — добавить или переформулировать.
10. **s07 Vaswani notes timestamp** — «на май 2026».

### Decision (кандидаты на удаление — конвергентно отмечены)
11. **s28 Pearl + s26 ARC-AGI** — твоё решение. Варианты: оставить / удалить s28 / удалить оба.

### P2 (на усмотрение, ~10-15 минут)
12. **s30 PARTS disclaimer** в speaker notes.
13. **s19 шрифт** уровней автономии.
14. **s25 иконки** bias/sycophancy/shift из светло-серого в teal.
15. **s02a «Раздел 0»** переименовать.

## Recommendation orchestrator'у

**3 пути:**

**Путь 1 (рекомендую) — Targeted P1 revision v3.1.**
- Спавнить `presentation-designer` Opus с **10 fixes** (4 critical + 6 high-value): s13 sync, «приложение-робот», ARC fresh, divider раздела 5, s05b funnel, s13 axis, s15 RU/EN, s21 axis, s08 caveat, s07 timestamp.
- **Не трогать раздел 4** — оставить решение по Pearl/ARC на пользователя.
- Sanity check 1 критиком (presentation-critic Opus) на v3.1.
- USER GATE для slides → Phase 12.5 (speech v3).
- **Estimated:** ~45-60 мин designer + 15 мин sanity + GATE.

**Путь 2 — Quick critical only (4 правки).**
- Только critical fixes: s13 sync, «приложение-робот», ARC fresh, divider раздела 5.
- Skip P1 visual (s05b/s13 axis/s15/s21/s08/s07) — оставить как есть.
- Без sanity check.
- USER GATE → Phase 12.5.
- **Estimated:** ~20 минут.

**Путь 3 — Большая ревизия (with cuts).**
- Critical + High-value + удалить s28 Pearl + s26 ARC-AGI (или объединить).
- pacing освобождает ~5 минут на буфер 13 минут.
- Полный rerun 4 критиков на v3.2.
- **Estimated:** ~120 минут total.
- **Risk:** регрессия в раздел 4, потеря концептуальной глубины (Pearl/ARC = критическое мышление).

## Decisions для GATE

**Вопросы пользователю:**
1. Какой путь — 1 / 2 / 3?
2. Pearl + ARC — оставляем / удаляем s28 / удаляем оба?
3. После slides GATE — сразу Phase 12.5 (speech v3)?

После approval → Phase 12.5 (speech v3 derived from chapter v3.1 + slides v3) → 3 critics → final GATE C → close-out.

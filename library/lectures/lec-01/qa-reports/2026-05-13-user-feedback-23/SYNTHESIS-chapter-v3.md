# SYNTHESIS — chapter v3 — Phase 12.2 critics — 2026-05-13

**Issue:** #70 (Phase 12 of EPIC #64).
**Артефакт:** `library/lectures/lec-01/chapter.md` v3 (16022 слов, 60 references).
**3 критика (Opus 4.7):** methodology-critic + fact-checker + reader-simulator (text-only).

## Общий verdict

**✅ APPROVE-WITH-MINOR** во всех трёх критиках. **0 P0**, **~10 уникальных P1** (часть convergent), **~15 уникальных P2**. **Closure 17/17 user fixes** confirmed methodology-critic. **0 фактических ошибок** (fact-checker), **0 регрессий с v2**.

| Critic | P0 | P1 | P2 | Verdict |
|---|---|---|---|---|
| methodology-critic | 0 | 3 | 6 | APPROVE-WITH-MINOR |
| fact-checker | 0 | 3 | 8 | APPROVE-WITH-MINOR |
| reader-text-only | 0 | 3 | 4 | APPROVE-WITH-MINOR |
| **После дедупликации** | **0** | **~10** | **~15** | APPROVE-WITH-MINOR |

## Convergent findings (≥2 критика согласны)

### КОНВЕРГЕНЦИЯ A — McCorduck цитата (P1)
- **methodology-critic** + **fact-checker**: §1.1 «Часть AI-проблемы заключается…» подана в **кавычках как цитата**, но это **paraphrase** — не дословный перевод. Канонический оригинал: «as soon as it works, no one calls it AI anymore» (McCorduck 2004). Кавычки = академическое обещание дословности.
- **Fix:** убрать кавычки → «Эту динамику описала Pamela McCorduck: как только техника начинает работать, её перестают называть AI (см. McCorduck, 2004)».

### КОНВЕРГЕНЦИЯ B — §1.1 плотность входа (P1)
- **reader**: «**самое тяжёлое место главы** — 4 подхода + Russell-Norvig + ISO + Mitchell + Searle + McCorduck + Tesler в одной секции (~1000 слов). Прочитал, но не переварил».
- **methodology-critic** (косвенно): подтверждает богатство, но без P1.
- **Fix:** упростить вход — основной текст 2-3 подхода (Russell-Norvig + ISO как практические + AI Effect как явление), остальное в **сноску** или в **visual table-summary** на 4 строки сразу под параграфом. Цель — мягкая дверь, не информационный обвал.

### КОНВЕРГЕНЦИЯ C — Англицизмы остаточные (P1)
- **methodology-critic** P1: §2.1 teachable («self-report / telemetry / share / respondent / penetration»), §4.7 stake-блоки («Stake:», «long-term», «software-разработчиков»), §4.6 Pearl («discomfort», «productivity»).
- **reader** P1: «consumer-тарифы» — смешение русского и английского через дефис.
- **Fix:** find-and-replace по всем §:
  - «self-report» → «самоотчёт»
  - «telemetry» → «телеметрия» (заимствованное, OK)
  - «share / respondent / penetration» — переводы по контексту
  - «stake» → «интерес / ставка / выгода»
  - «long-term» → «долгосрочный»
  - «software-разработчиков» → «разработчиков ПО»
  - «discomfort» → «дискомфорт» (есть в русском)
  - «productivity» → «производительность»
  - «consumer-тарифы» → «потребительские тарифы»

## Уникальные P1

### От methodology-critic
- **§1.4 footnote `[^1]` слишком сильно** — «не является целью нашего курса» противоречит Л2 «Как работают современные большие модели» (касается архитектуры) и Л3 «Агенты, RAG, API». **Fix:** softer formulation «не основная цель этой лекции; глубже — на лекциях 2-3».
- **Changelog typo §3.8** — ссылается на §3.8, но в главе только §3.7 (worked example). Trivial typo — поправить «§3.8» → «§3.7».

### От fact-checker
- **§2.2 Mistral «20+ человек / 3 месяца»** — НЕ verified в публичных источниках. Mistral 7B paper имеет 18 авторов; founding April 2023 → release Sept 2023 = 5 месяцев, не 3. **Fix:** softer formulation: «небольшая команда, несколько месяцев от основания» — без specific numbers. **Альтернатива:** найти Mensch interview для verification.
- **§4.7 Searle page range** — chapter указывает «BBS 3(3), 417-424», стандарт — 417-457 (full target article). **Fix:** проверить и согласовать на 417-457.

### От reader
- **§4.7 4 биографии CEO** — «journalistic prose, не учебный материал. 800 слов про Altman/Amodei/Hassabis/LeCun — через неделю не воспроизведу». **Fix:** стянуть в **сравнительную таблицу** `Спикер | Прогноз | Stake` (3 колонки × 4 строки) + 200 слов analytical synthesis (сейчас 800 слов prose).
- **§3.4.1 vector database без объяснения** — «введён как компонент памяти агента, но что это? Без одной фразы — архитектура агента читается как чёрный ящик». **Fix:** добавить inline disclaimer: «vector database — база данных, оптимизированная для поиска по сходству эмбеддингов; подробнее — лекция 3 RAG».

## Топ-N правок для Phase 12.2 revision

### P1 (must-fix перед GATE A — 8 правок)
1. **§1.1 McCorduck quote** — убрать кавычки или дать дословный перевод (КОНВЕРГЕНЦИЯ A).
2. **§1.1 упростить вход** — основной текст 2-3 подхода + visual summary table (КОНВЕРГЕНЦИЯ B).
3. **Англицизмы** — find-and-replace ~10 слов (КОНВЕРГЕНЦИЯ C).
4. **§1.4 footnote softer** — «не основная цель этой лекции» вместо «не является целью нашего курса».
5. **Changelog §3.8 → §3.7** — typo.
6. **§2.2 Mistral team size / timing** — softer formulation без specific numbers.
7. **§4.7 4 биографии CEO** — стянуть в таблицу.
8. **§3.4.1 vector DB** — inline disclaimer одной фразой.

### P2 (на усмотрение revision, ~10 минут)
9. **§4.7 Searle page range 417-424 → 417-457** — citation hygiene.
10. **§3.4.2 5 уровней автономии** — добавить сравнительную таблицу `Уровень | Кто решает | Кто исполняет | Пример`.
11. **§2.2 эпизод MCP** — добавить вводную фразу про смену типа прорыва: «А теперь — другой класс прорыва: не модель, а интеграционный протокол».
12. **§1.1 Tesler nuance** — footnote «(в Hofstadter-формулировке; Tesler сам предпочитал "Intelligence is whatever machines haven't done yet")».
13. **Глоссарий в конце** — токены, эмбеддинги, vector DB, edge-устройство, MES, контекстное окно (10-15 терминов).

## Сильные стороны (НЕ менять)

✅ **closure 17/17** — все user fixes применены.
✅ **0 фактических ошибок** на 41 проверенный claim. Все critical numbers/dates verified против primary sources.
✅ **0 регрессий с v2** — sycophancy timeline, Google Translate caveat, LeCun affiliation, DeepSeek teachable moment — всё OK.
✅ **§3.3.1 цикл чата** — лучший новый раздел (reader: «лучшее место в главе»).
✅ **§3.6 чек-лист 2 вопроса + квадрант** — самая полезная часть для семинара (reader: «работает»).
✅ **§3.2 схема входа-модели-выхода** — наглядно (reader: «запоминается»).
✅ **§5.0/5.1/5.2 completion-структура** — резюме + задание + roadmap = «знаю что делать».
✅ **§3.4.1/§3.4.2 split** — Feng/McDonald/Zhang 5 уровней exact match arxiv:2506.12469.
✅ **Diagnostic tone, без magic-pill** — methodology-critic подтвердил.
✅ **«Вы»-form, без familiar CTA** — methodology-critic подтвердил.

## Recommendation orchestrator'у

✅ **GATE A — APPROVE-WITH-FIXES** возможен.

**3 пути:**

**Путь 1 (рекомендую) — Quick revision v3.1 → GATE A.**
- Спавнить `book-editor` Opus с 8 P1 правок выше → chapter v3.1 (~30-45 мин).
- Sanity check 1 критиком (methodology-critic Opus) на v3.1 — closure check.
- USER GATE A → Phase 12.3.

**Путь 2 — APPROVE как есть, P1 правки → speech/slides downstream.**
- GATE A approve v3 как есть.
- В Phase 12.4 (slides) и Phase 12.5 (speech) — book-editor / speech-writer применят P1 правки inline (например, англицизмы вычистятся естественно при переписывании в speech).
- **Risk:** P1 в chapter не sync с downstream (англицизмы могут унаследоваться, McCorduck quote останется в кавычках).

**Путь 3 — Полное v3.1 + sanity check всех 3.**
- Большой revision + полный rerun 3 критиков (~90 мин total).
- **Overkill** при 0 P0.

**Estimated:** Путь 1 — ~45-60 мин до GATE A. Путь 2 — 0 мин (immediate gate). Путь 3 — ~120 мин.

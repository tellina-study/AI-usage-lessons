VERDICT: APPROVE-CLEAN

# Fact-Checker Report — Лекция 4 delta Решения #103 — 2026-05-17

**Scope:** УЗКАЯ delta-проверка каскада Решения #103 (issue #99). НЕ пере-ревью всего артефакта.
**Артефакты:** chapter v1.3 (chapter-part2.md §4.5) / deck v3.4 (slides/s22a-curl-slop.md + rendered/lec-04.pptx slide 24) / speech v1.3 (фрагмент [s22a · 2 мин], l.403-413).
**Метод:** book-first сверка s22a против chapter §4.5 (эталон истины); cascade-rename integrity; volatile-discipline; v1.x regression; tag-unification. Веб-верификация curl-чисел НЕ требовалась — все volatile-числа корректно изолированы в `[FACT-CHECK]`-маркерах + chapter-источниках (The New Stack / The Register 2026-01-21 / Socket), на видимом/устном слое отсутствуют (см. §2).

## Severity counts
- P0 (false fact / broken citation / direction inversion / misquote): **0**
- P1 (missing source / suspicious number / volatile on visible / rename distortion): **0**
- P2 (cite format / minor): **0**

## 1. s22a book-first == chapter §4.5 — PASS

Каждый факт slide s22a (md + PPTX slide 24) и speech-фрагмента [s22a] сверён против chapter-part2.md §4.5 (l.200-209) + Deep-dive box 4 (l.261). **0 фактов вне §4.5.**

| Факт §4.5 (эталон) | slide s22a (md+PPTX) | speech [s22a] | Verdict |
|---|---|---|---|
| curl — критич. OSS HTTP-клиент, малая команда, ведёт Daniel Stenberg | ✓ (Stenberg в speaker notes косвенно «AI-анализаторы в правильных руках»; имя явно в speech l.413) | ✓ «Daniel Stenberg, который ведёт curl» | VERIFIED |
| bug-bounty: поток LLM-«отчётов», объём вырос, доля валидных рухнула | ✓ «объём кратно вырос, доля валидных рухнула» | ✓ «Объём кратно вырос, а доля валидных обрушилась» | VERIFIED |
| Фиктивный отчёт о HTTP/3 + GDB-дампы + ссылка на несуществующую функцию | ✓ «фиктивные GDB-дампы + несуществующая функция» | ✓ «уязвимости в HTTP/3, отладочные дампы, несуществующая функция» | VERIFIED |
| С нач. 2026 curl свернул открытый bug-bounty | ✓ «С начала 2026 года открытый приём свёрнут» | ✓ «С начала 2026 года curl фактически свернул» | VERIFIED |
| Асимметрия: фейк = секунды/≈0 vs опровержение = часы человека | ✓ две колонки ЛЕВО/ПРАВО | ✓ дословно по смыслу | VERIFIED |
| DDoS на внимание сопровождающих; атакуется невосполнимый ресурс — время | ✓ | ✓ | VERIFIED |
| Риск переносится на supply-chain (от curl зависят почти все) | ✓ | ✓ | VERIFIED |
| Stenberg: AI — инструмент, анализаторы «в правильных руках» находят реальные баги | ✓ speaker notes | ✓ l.413 paraphrase + «в правильных руках» в кавычках = дословно совпадает с §4.5 l.209 | VERIFIED |
| Альтернатива: приватное раскрытие / убрать junk-стимул / воспроизводимый PoC-барьер | ✓ все 3 | ✓ все 3 | VERIFIED |
| Критерий «когда AI здесь опасен» (открытый процесс + дорогая людская валидация) | ✓ footer | ✓ закрытие фрагмента | VERIFIED |

**Misquote-check (Citation Hygiene):** единственная кавычка-цитата Stenberg — «в правильных руках» — дословно совпадает с chapter §4.5 l.209 («в правильных руках»). Остальное — корректный paraphrase без кавычек. **0 misquote.**

**Phantom-fact check:** ни slide, ни speech не вводят фактов сверх §4.5. «× 1000+» на визуале — НЕ volatile bug-bounty-стат, а ось асимметрии стоимости, дословно деривирована из §4.5 l.207 «дешевеет в тысячи раз». In-bucket.

## 2. Volatile-discipline (×8 / <5% / >15% / даты) — PASS

| Слой | ×8 / <5% / >15% / «1 на 20» / «1 февраля 2026» | Verdict |
|---|---|---|
| Visible slide body (s22a md) | ОТСУТСТВУЮТ — только направление словами («кратно вырос», «обрушилась») | ✓ |
| Visible PPTX slide 24 (все shapes) | ОТСУТСТВУЮТ — только «кратно вырос, доля валидных рухнула» + «× 1000+» (ось асимметрии, не bug-bounty) | ✓ |
| Spoken speech [s22a] l.405-413 | ОТСУТСТВУЮТ — «Объём кратно вырос, а доля валидных обрушилась» | ✓ |
| Speaker notes s22a (PPTX + md) | Корректно: только `[FACT-CHECK: curl valid-rate <5%, ×8 объём, дата сворачивания]` маркер | ✓ |
| speech preflight l.34 | Корректно: `[FACT-CHECK]` curl + источники (The New Stack; The Register 2026-01-21; Socket); «на видимом/устном слое — только направление словами, точные доли НЕ называть» | ✓ |
| chapter §4.5 l.205 | Точные числа допустимы (academic source-of-truth) + `[FACT-CHECK]`-маркер + 3 источника | ✓ |

Точные volatile-числа присутствуют **только** где разрешено (chapter + speaker-notes/preflight FACT-CHECK), отсутствуют на видимом/устном слое. Полное соответствие Решению #100/#9 (freshness, паттерн s12/s27). **P1 не зафиксировано.**

## 3. Cascade-rename мейнтейнер→сопровождающий — PASS (факты не искажены)

- **Residual «мейнтейнер/maintainer»:** 0 вхождений в chapter.md/part2/part3, speech.md, slides/*.md (исключая корректные упоминания самого Решения #103 в changelog).
- **METR-формулировки идентичны по смыслу, только термин:**
  - chapter.md:106 — «сопровождающие зрелых проектов (репозитории с десятками тысяч звёзд)», 16 разработчиков / 246 задач / прогноз +24% / пост +20% / факт −19% / arXiv:2507.09089 — числа НЕ затронуты.
  - chapter-part2 §3.5 l.87 — «16 опытных OSS-разработчиков, сопровождающие зрелых репозиториев (22k+ звёзд), 246 реальных задач» — идентично.
  - chapter-part2 Deep-dive box 3 l.114 — «n = 16, 246 задач, +19% времени, прогноз −24%, пост −20%» — идентично.
  - speech l.43-45 — «Шестнадцать опытных разработчиков… сопровождающие зрелых проектов… Двести сорок шесть… на девятнадцать процентов больше… двадцать четыре… двадцать» — идентично.
  - slide s01 speaker notes (PPTX slide 1) — «сопровождающие зрелых проектов… двумястами сорока шестью… на девятнадцать процентов больше… двадцать четыре / двадцать процентов» — идентично.
- Замена чисто терминологическая (anglicism→русский эквивалент); смысл «эксперт на своём знакомом сложном легаси» сохранён везде. curl-кейс: «сопровождающий» в асимметрии (фейк секунды vs опровержение часы) — смысл идентичен §4.5. **0 искажений от rename (P0/P1 не зафиксировано).**

## 4. v1.x regression (числа вне каскада #103) — PASS

Все ключевые числа сверены, присутствуют, не затронуты каскадом:
- METR −19% (9×) / −24% (3×) / −20% (4×) — стабильны.
- Copilot 55,8% / «примерно на 56%» (chapter:51,190) — стабильно.
- SWE-bench 88,7 / 64,3 (chapter:295, speech:26,30) — стабильно.
- GitClear 211M (chapter:309,352; part2:259; speech:249,615) — стабильно.
- slopsquatting 576 000 / ~20% / 43% / 58% (part2:218,220,222,261) — стабильно.
- Anthropic n=52 / −17% (part3:21,196,202,207,209,259,288,299,344) — стабильно.
- Replit 95/100 (part2:135,140; speech:72,76,295,299) — стабильно.
- Тулы 2026 (Copilot ghost-text/Cursor Tab/JetBrains; Claude Code/Codex/Devin) с `[VFY-day-of]` — не затронуты.

Каскад #103 строго targeted: vol/numbers/citations/strict-in/тул-секции v1.2 не менялись (подтверждено changelog chapter v1.3 l.18 + grep). **0 регрессий.**

## 5. Tag-унификация [VERIFY-DAY-OF]→[VFY-day-of] — PASS

- Residual `[VERIFY-DAY-OF]` в видимом/устном/notes-слое: **0** (грэп по speech.md, slides/*.md, chapter*.md, deck*.yaml — единственные вхождения «VERIFY-DAY-OF» это описание самой замены в changelog/decisions, что корректно).
- `[VFY-day-of]` консистентен: 12 вхождений в speech.md (l.25/26/225 и preflight-блок), стиль единый.
- s25/s32 curl-callbacks (speech l.465 «тот же slop, что свалил bug-bounty curl»; l.577 «curl — это AI, масштабирующий шум там, где валидация лежит на людях») — 1-фразовые callback'и, дословно согласованы с §4.5, НЕ re-narration. Консолидация в s22a-beat подтверждена.
- **0 фактических потерь от замены тега.**

## Верификация curl-источников (Freshness)

```
Fact: «curl свернул открытый bug-bounty; объём LLM-отчётов ×8; валидных <5%»
Source claimed: The New Stack; The Register 2026-01-21; Socket
Source date: 2026-01-21 (The Register)
Lecture date: 2026-05-17 (production), читается позже
Refresh cadence: yearly+ (направление/асимметрия — концептуально стабильно;
                  точные доли — quarterly, но НЕ на видимом слое)
Verdict: VERIFIED (направление) — точные доли корректно [FACT-CHECK] + day-of preflight
```
Volatile-числа корректно НЕ на видимом/устном слое; точные доли несут `[FACT-CHECK]` + preflight day-of-lecture verify (источники указаны). Freshness-дисциплина соблюдена — отдельный freshness-report для узкой delta не требуется (единственный новый volatile-кластер s22a уже покрыт preflight l.34).

## Топ-правок до публикации
**Нет.** Delta Решения #103 чистая по фактам: 0 P0 / 0 P1 / 0 P2.

## Сводка
- **Verdict:** APPROVE-CLEAN
- **s22a book-first == §4.5:** PASS — 10/10 фактов VERIFIED, 0 phantom-фактов, 0 misquote (Stenberg «в правильных руках» — дословно)
- **Volatile-дисциплина:** PASS — ×8/<5%/даты отсутствуют на видимом+устном слое, только в `[FACT-CHECK]`+chapter+preflight
- **Rename не исказил:** PASS — 0 residual «мейнтейнер», все METR-числа (16/246/−19/−24/−20/arXiv) идентичны во всех 5 точках
- **v1.x не регрессировал:** PASS — все ключевые числа стабильны, каскад strictly targeted
- **Tag-унификация:** PASS — 0 residual [VERIFY-DAY-OF], 0 фактических потерь

# Workflow — рефлексия Лекции 4

## Проблема 1 (главная): несущая ось не была keystone-слайдом до 1-го погружения
**Симптом:** owner забраковал deck v2 — «где сами уровни и их описание?! ты вообще сторителлинг продумывал? надо перетряхивать». s03 был защитным Л3-мэппингом («Лекция 4 не вводит новый аппарат»), s04 — «возвращаемся 5 раз» meta + §-коды, уровни A/B/C/D «всплывали» на s06.
**Корень:** plan-v2-final §4 не делал несущую ось (лестница A→D) отдельным keystone-слайдом ДО первого погружения. methodology-critic Phase-1 проверял LO-coverage / assertion-evidence / strict-in, но НЕ «load-bearing axis = standalone keystone before first deep-dive». Phase-4 deck-QA тоже не имел этой проверки.
**Стоимость:** deck v2→v3 (полная Раздел-0 перестройка, 5-агентная re-QA) → v3.1 (tone-strip хвост, 3-агентная re-QA). ~5 циклов.
**Улучшение IMP-1:** keystone-axis ENFORCED-проверка в 3 точках — methodology-critic checklist (Phase 1 plan + Phase 4 deck), lecture-outline template (обязательный пункт), Pre-USER-GATE walkthrough. Формулировка: «Несущая концептуальная ось лекции предъявлена ОТДЕЛЬНЫМ keystone-слайдом в Разделе 0 ДО первого погружения в неё? Заголовок/1-я строка — про саму ось, не про устройство курса/защиту подхода?»

## Проблема 2: usage-limit обработан как subagent-failure
**Симптом:** book-editor (chapter v1.3) упал «You've hit your limit · resets 9:40am» (0 токенов). Я сделал chapter-rename напрямую, сославшись на «Subagent-failure rule → do the work directly».
**Корень:** конфликт двух правил. Generic CLAUDE.md: «If a subagent fails, do the work directly». Специфичная память `feedback_subagent_usage_limit`: «usage-лимит ≠ subagent failure; ждать сброса + ре-делегировать, НЕ подменять оркестратором». Я применил generic вместо специфичного (specific должен побеждать general).
**Митигация по факту:** контент критик-валиден (consistency APPROVE-WITH-POLISH, rename полный, book-first цел); deck/speech после сброса корректно ре-делегированы; память исправлена (неверный урок не распространился).
**Улучшение IMP-2:** в CLAUDE.md Subagent Rules — явная развилка ПЕРЕД «do directly»: классифицировать сбой. usage/rate/quota-limit (0 токенов, «resets HH:MM») → НЕ failure: `ScheduleWakeup`/ждать сброса + ре-делегировать ТУ ЖЕ задачу; НИКОГДА не self-implement. Logic-failure (агент отработал, но результат негоден/ошибка инструмента) → тогда do directly / re-delegate с правкой.

## Проблема 3: scaffold/§/[VFY]-leak рецидив + ложный self-grep
**Симптом:** §-коды/[VFY]/«точка возврата»/«— в главе» на видимом слое ~16 слайдов (v3 SYNTHESIS), designer-self-grep вернул TOTAL=0 (ложно — regex не ловил словесные scaffold-фразы). Поймано orchestrator independent grep.
**Корень:** anti-pattern #36–#39 существовал, но не был обязательным gating-шагом с НЕзависимой проверкой; полагались на self-report субагента.
**Улучшение IMP-4:** Pre-USER-GATE (slides/speech) — обязательный orchestrator-independent grep по rendered pptx видимому слою (паттерн включает СЛОВЕСНЫЕ scaffold-фразы, не только коды), цель TOTAL=0; self-report субагента НЕ засчитывается как verification.

## Что сработало
- suffix-ID для всех post-GATE-A добавлений (4×) — 0 renumber-каскада в финализированную главу.
- book-first строго последовательно (chapter→deck→speech); никогда параллельно — 0 derive-drift.
- Independent verification > trust report (поймал ложный TOTAL=0, designer false-UNMODIFIED-confusion).
- Isolated commits от parallel-сессии (explicit paths).

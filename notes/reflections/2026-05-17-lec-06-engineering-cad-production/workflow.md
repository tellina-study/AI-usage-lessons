# Reflection — workflow (Лекция 6 production, 2026-05-17)

## Git / process compliance

| Правило | Соблюдено | Деталь |
|---|---|---|
| No work without issue | ✅ | issue #101 создан до старта |
| Worktree isolation (parallel) | ✅ | `/tmp/lec-06-wt`, база чистый main; параллельно lec-04 #99 + lec-05 #100 — **ноль contention** (валидирует ENFORCED Multi-Lecture policy на 3 одновременных лекциях) |
| Branch ref propagation | ✅ | `git update-ref` из main repo после каждой фазы — без переключения ветки lec-04 сессии |
| Roast-Before-Implement | ✅ | self-roast в plan-v1, представлен с Phase-1 критикой на pre-Phase-2 GATE |
| Phase gating | ✅ | 3 USER GATE (A/B/C) — все explicit-approved («давай»/«approve») |
| NEVER push to main | ✅ | PR #102 (lec-06) + PR #103 (манифест-хвост, отдельный branch+PR, не прямой пуш) |
| PR merge только по команде | ✅ | мерж #102/#103 только после «давай»/«доделай все» |
| Pre-gate перед каждым GATE | ✅ | mode=chapter / mode=slides / ручной final |

## Что сработало сильно

- **Pre-gate ловит то, что критики структурно пропускают.** 2 перехвата: (1) `[for-slide-sNN]` в chapter body — критики Phase-3 APPROVE-WITH-POLISH не флагнули (не в их фокусе; book-editor capability vs lec-07 precedent=0); (2) покорёженная s11-аннотация — внесена Phase-8 P2-фиксом **после** Phase-7 vision-критиков → структурно вне ревью. Подтверждает rationale pre-gate-правила («critics проходят там, где user отклоняет»).
- **Polish Round Pattern** (единый batched агент на фазу-ревизию) — Phase 4/8/11 по одному спавну закрыли все P1/P2; не плодил per-artifact спавны.
- **Orchestrator self-critique** на slide-композиции: 6-й divider (Часть 6) — решил добавить через curriculum-relevance check (именованная major-секция, lec-07 precedent), не свалил на дизайнера и не спросил пользователя по мелочи.
- **Cascade-tracking**: +divider Phase-6 → ренумерация → consistency-checker Phase-7/10 подтвердил 0 orphan; pre-flight speech авто-содержит orphan-контроль.

## Что сбоило / уроки

1. **Usage-лимит → ошибочная orchestrator-подмена.** При падении 3 Phase-10 критиков я начал писать провизорный self-review (мис-применил «subagent fails → do directly»). Владелец остановил: «лимиты под это правило не идут». Recovery корректен (перезапуск, реальные вердикты заменили провизор), но **первичный мис-шаг — нарушение независимости QA**. Урок зафиксирован (memory + improvements P1).
2. **Provisional SYNTHESIS перезаписан корректно** — пометил provisional, заменил консолидатом по реальным отчётам; агентам явно «НЕ трогай SYNTHESIS.md, оркестратор перепишет». Хорошая recovery-дисциплина, но лучше бы инцидента не было.
3. **chapter status `reviewed`→`finalized`** болтался до Phase-11.5 — нашёл на финальном cross-grep, не раньше. Мелочь, но статус-консистентность 3 артефактов стоит проверять как явный pre-GATE-C чек-айтем.
4. **Манифест-хвост** (`in_production`→`produced`) не был в исходном scope PR #102 — потребовал отдельного PR #103 пост-мерж. Системно: «produced»-flip нужно либо включать в production-PR (но статус during-production = in_production), либо чек-лист «после merge: manifest flip отдельным PR» (сделано, но реактивно).

## Вывод
Workflow-дисциплина высокая (git-правила, gating, worktree-изоляция — все ✅). Два процесс-гэпа: (а) reaction на rate-limit (исправлено правилом), (б) post-critic P2-фиксы обходят ревью → нужен mandatory re-grep перед pre-gate.

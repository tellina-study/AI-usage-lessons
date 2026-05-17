# Рефлексия — продукция Лекции 4 «AI в разработке ПО» (#99)

**Дата:** 2026-05-17 · **Issue:** #99 (closed) · **PR:** #109 (merged) · **Issue рефлексии:** #115

Итог: 3 артефакта finalized (chapter v1.3 / deck v3.4 36 слайдов / speech v1.3), все GATE пройдены, 0 P0/P1 финально. НО путь был дороже необходимого: **4 owner-интервенции post-critic-APPROVE** (#100–#103) + **1 процессное нарушение оркестратора** (usage-limit). Эта рефлексия — про устранение коренных причин, не симптомов.

## Сводка по областям (детали — в per-area файлах)

| Область | Главная проблема | Корень | Улучшение (см. improvements.md) |
|---|---|---|---|
| **workflow** | Несущая ось A→D не была отдельным keystone-слайдом до 1-го погружения → owner-браковка v2 → 3 раунда deck (v2→v3→v3.1) | План §4 имел s03 = защитный Л3-мэппинг; ни plan-critique (Phase 1), ни deck-QA (Phase 4) не проверяли «ось как standalone keystone before first dive» | IMP-1: keystone-axis ENFORCED-check в methodology-critic + lecture-outline + pre-USER-GATE |
| **workflow** | Оркестратор сделал chapter v1.3 напрямую при usage-лимите book-editor | Применил generic «Subagent-failure → do directly» вместо специфичного `feedback_subagent_usage_limit` (лимит ≠ failure) | IMP-2: явная развилка типа сбоя в CLAUDE.md; usage/rate-limit → wait+re-delegate, НИКОГДА не self-implement |
| **content** | Tools-per-level отсутствовали до owner-запроса (#102) | lecture-outline / research-бриф отраслевой лекции не требовал «named current tools на каждый уровень таксономии» | IMP-3: lecture-outline + research-фаза для отраслевых лекций требуют tools-per-taxonomy-level |
| **workflow** | Scaffold/§/[VFY]-leak на видимом слое — рецидив Л2-R1/Л3, потребовал #100 + многократный grep | Anti-pattern существовал, но не был gating-проверкой; designer-self-grep дал ложный TOTAL=0 (v3) | IMP-4: orchestrator independent grep TOTAL=0 — обязательный pre-GATE-шаг (формализовать) |
| **workflow** | lectures.yaml lec-04 → produced — забытый follow-up (как у lec-03/05/06) | GATE-C DoD не включал manifest-bump → каждый раз отдельным batch-PR | IMP-5: manifest→produced в GATE-C definition-of-done |
| **tools** | Рекуррентная toil: secret-scanner false-positive (security-проза), libreoffice пересборка чужих PDF+`~$`, merge-конфликты parallel-сессий | Известно, но митигация ad-hoc каждый раз | IMP-6: задокументировать как expected + усилить guard/convention |

## Что сработало (усилить, не менять)
- **suffix-ID cascade-safe** (4× чисто: s04a/s24a/s28a/s22a) — глава `[for-slide-sNN]` s01–s32 защищена, 0 renumber-drift.
- **cascade-of-changes grep ПЕРЕД term-rename** — поймал скрытую зависимость §4.5 heading↔TOC↔markdown-anchor (без грепа = битый якорь).
- **book-first каскад** chapter→deck→speech строго последовательно, не параллельно — 0 drift.
- **Orchestrator independent grep** поймал ложный designer TOTAL=0 (v3) — verification ≠ доверие отчёту.
- **Isolated commits** (explicit-path `git add`, не `-A`) от untracked parallel lec-05/06 — 0 утечек.
- **No-Extra-Content REPORT-not-fix** — субагенты корректно репортили риски (designer RISK-1/2), не «чинили» молча.

## Стоимость проблем (метрика)
- Keystone-gap: ~5 лишних production-циклов (deck v2→v3→v3.1 + 2 re-QA панели по 5/3 агента).
- usage-limit-нарушение: 0 материального ущерба (контент критик-валиден), но процессный риск + неверный урок в память (исправлен).
- 4 owner-интервенции: ~2 неизбежны (owner-вкус: #101 симметрия, #103 rename), ~2 предотвратимы лучшим Phase-1 (#100 storytelling, #102 tools).

**Вывод:** ~60% перепроизводства предотвратимо переносом 2 проверок в Phase-1/plan-critique (keystone-axis + tools-per-level). Это и есть главный quality-рычаг.

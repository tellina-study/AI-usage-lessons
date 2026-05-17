# Improvements — Лекция 6 production (2026-05-17)

Извлечено из tools/workflow/content/user-feedback. Priority P0–P3 · Effort S/M/L.

| # | Pri | Eff | Цель (компонент) | Действие | Issue |
|---|---|---|---|---|---|
| 1 | **P1** | S | `CLAUDE.md` §Subagent Rules + `notes/decisions.md` | Явно: usage/rate-limit субагента ≠ «subagent failure» для правила «do the work directly». Корректная реакция: дождаться сброса + перезапустить тот же спавн; провизорный orchestrator-self-review (если делался) пометить provisional и заменить консолидатом по реальным отчётам; не финализировать артефакт до реальных вердиктов. | create |
| 2 | **P1** | M | `tools/lecture-production/README.md` §3.5 + `.claude/skills/pre-user-gate/SKILL.md` | Post-critic P2/P1-фиксы (внесённые в Phase-4/8/11 revision ПОСЛЕ ревью критиков) обходят critic-ревью → mandatory: после revision-агента — targeted re-grep + (для slides) mini visual re-check затронутых слайдов ПЕРЕД pre-gate. Якорь: s11 покорёженная аннотация прошла именно так. | create |
| 3 | **P1** | S | `.claude/agents/book-editor.md` + `tools/lecture-production/README.md` §4 + pre-user-gate chapter-grep | `[for-slide-sNN]` authoring-маркеры НЕ должны попадать в finalized `chapter.md` body (lec-07 precedent=0; lec-06 протёк 27×). Зафиксировать как explicit DoD book-editor + pre-gate chapter-grep `\[for-slide-s` == 0. | create |
| 4 | P2 | S | secret-scanner hook (`.claude/settings*` / hook script) | Whitelist повторяющихся false-positive паттернов (187-ФЗ/58-ФЗ, числовая нормативная проза) — снять шум на каждом коммите lecture-контента. | batch (#97-смежн.) |
| 5 | P2 | S | `tools/presentation-build/README.md` + `notes/mcp-limitations.md` | build-script template: assert `ROOT == worktree path` в начале `build_lecNN.py` (Phase-6 пустые-notes gotcha при parallel worktree). | batch |
| 6 | P2 | M | `tools/lecture-production/README.md` §3 + pre-gate | Glossary-lock как tracked-артефакт: после GATE-A требовать `catalog`-glossary запись лекции; consistency-checker сверяет canonical-форму перед GATE-B/C (L6 не был зафиксирован). | create |
| 7 | P2 | S | `tools/lecture-production/README.md` §3.6 | Канонизировать ОДИН счётный рецепт strict-in (что считается полностью-in-bucket; partial→out; знаменатель = total min/words) — снизить variance оценок (book-editor 33% vs methodology 40%; speech 62% vs 44%). | create |
| 8 | P3 | S | orchestrator habit / `workflows/` | Pre-GATE-C чек-айтем: статус-консистентность 3 артефактов (chapter/deck/speech все = finalized) + манифест produced-flip как явный post-merge step (не реактивно). | batch |

## Связи
- #1, #8 ↔ user-corrections (usage-лимит, completeness). Memory: `feedback_subagent_usage_limit`, `feedback_governance_rules`.
- #2, #3 ↔ pre-gate rationale (ловит post-critic regressions / scaffolding-leak).
- #5 ↔ Multi-Lecture Parallel Production policy (worktree-ROOT).
- #6, #7 ↔ ENFORCED AI-Failure measurement governance ([[feedback_governance_rules]]).

## Созданные issues (P1)
- #1 → **#105** (CLAUDE.md usage-лимит ≠ fail)
- #2 → **#106** (post-critic фиксы → re-grep перед pre-gate)
- #3 → **#107** ([for-slide-sNN] не в finalized chapter)
- P2/P3 (#4–#8) — не плодим issues, остаются в этом improvements.md / батч с #97-смежными.

## Резюме
3×P1 (создать issues), 4×P2 (создать ключевые / батчить смежные), 1×P3 (habit/batch). Все — процессные, не содержательные: production-качество лекции высокое, улучшать нужно guardrails вокруг post-critic-фиксов, scaffolding-гигиену, измерительную методику и реакцию на infra-лимиты.

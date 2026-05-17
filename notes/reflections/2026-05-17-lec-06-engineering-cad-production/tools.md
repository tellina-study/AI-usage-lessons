# Reflection — tools (Лекция 6 production, 2026-05-17)

## Субагенты — что вызывалось

| Агент | Спавнов | Результат |
|---|---|---|
| general-purpose (research) | 4 (parallel) | ✅ 4 заметки ~13.8k слов; honest «что не подтвердилось» секции — образцовая эпистемическая гигиена; подозрительные arXiv-id (2601/2603) сами флагнули → book-editor не пустил в chapter (цепочка сработала) |
| book-editor | 4 (Ph2 draft / Ph4 revision / pre-gate strip-markers / Ph11.5 status-flip) | ✅ chapter 12.9k, все P1/P2 закрыты; REPORT-дисциплина высокая (§X.X-judgment, [for-slide] flag) |
| presentation-designer | 4 (Ph5 структура / Ph6 render / Ph8 revision / pre-gate s11) | ✅ 32 слайда; сам поймал worktree-ROOT-баг (пустые notes) и почистил stray-артефакт |
| speech-writer | 2 (Ph9 / Ph11) | ✅ ~5.8k, Mars-мотив, pre-flight 8 actionable |
| methodology-critic | 4 (Ph1/3/7/10) | ✅ независимые strict-in замеры; Ph10 — после usage-лимита перезапуск |
| fact-checker | 3 (Ph3/7/10) | ✅ 30/30 [FACT-CHECK] live-верифицированы, 0 ошибок |
| reader-simulator | 4 (Ph1 text / Ph3 text / pre-render text / Ph7 rendered) | ✅ поймал сквозную «матбаза-болезнь», подтвердил её снятие |
| consistency-checker | 2 (Ph7 / Ph10) | ✅ tri-artifact, 0 drift, strict-in holistic confirm |
| presentation-critic / student-simulator | 1 / 1 (Ph7) | ✅ vision-ревью, P1-DELETE рекомендации |

Всего ~29 спавнов, 11 фаз. Делегирование работало; producer↔critic чередование держало качество.

## Сбои инструментов

1. **Usage-лимит 3 Phase-10 критиков одновременно** (methodology+fact+consistency вернули 0 tokens, «resets 9:40 МСК»). Критично: я ошибочно применил правило «if subagent fails — do directly» и сделал провизорный orchestrator-self-review. **Владелец скорректировал: usage-лимит ≠ subagent-failure.** После сброса перезапуск всех 3 — успех, вердикты подтвердили провизорные цифры независимо. → memory `feedback_subagent_usage_limit`, propagate в CLAUDE.md/decisions.

2. **presentation-designer Phase-6: build-script `ROOT` указывал на main-repo, не worktree** → `load_notes()` пусто → speaker notes пустые в первом PPTX. Designer сам обнаружил (vision-loop), исправил ROOT→worktree, пере-рендер. Worktree-isolation gotcha — не задокументирован в template. → mcp-limitations / presentation-build README.

3. **Pre-commit secret-scanner повторно false-positive** на «187-ФЗ/58-ФЗ» и числовой прозе (КИИ-параграф) — на ~5 коммитах. Шум, не блокер (checks passed), но повторяющийся. → tune hook whitelist.

## Skills

- `/pre-user-gate` ×2 (chapter, slides) + ручной mode=final. **Окупился дважды:** поймал scaffolding-протечку `[for-slide-sNN]` (27×, chapter) и покорёженную s11-аннотацию (внесена Phase-8 P2-фиксом ПОСЛЕ Phase-7 критиков). Оба — то, что критики структурно пропустили (P2-фикс мимо ревью).
- `/reflect` — текущий.
- Vision-инструмент (Read PNG) для orchestrator visual-sweep на pre-gate B — 12 ключевых слайдов, эффективно (не все 32).

## Вывод
Инструментарий зрелый. Главный tools-урок — usage-лимит обрабатывать как transient infra (ждать+перезапуск), не подменять. Второй — build-script worktree-ROOT нужен assert.

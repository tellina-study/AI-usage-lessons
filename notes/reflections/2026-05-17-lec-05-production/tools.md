# Reflection — tools (Лекция 5 production, issue #100)

## Subagents

**Что сработало:**
- 11-фазный пайплайн отработал end-to-end: book-editor ×3 (plan, chapter, revisions), presentation-designer ×2 (Phase 5+6, Phase 8), speech-writer ×2, критики (methodology/fact/reader/consistency/presentation/student) на Phase 1/3/7/10. Все verdicts по 4-уровневой шкале, counter-check соблюдён.
- **Critic ловит то, что producer self-report пропускает.** Phase 9 speech-writer заявил «ВСЕ 33 ≤95 WPM, max s28=94.7, PROVEN PASS» — фактически s28=100.3 (non-greedy `«…»` баг в самопроверочном скрипте). methodology-critic Phase 10 поймал независимым токенайзером → REVISE. Это валидация ценности critic-фазы: **самоотчёт producer'а по метрике нельзя принимать как gate-сигнал.**
- **Re-spawn после usage-лимита сработал.** Phase 10 (3 критика) упали на usage-лимите с 0 токенов; после сброса пере-спавнены заново (не подменял оркестратором). Консистентно с [[feedback_subagent_usage_limit]].
- presentation-designer корректно следовал No-Extra-Content + report-not-apply: s31-агрегацию и s04a-suffix-divider **отчитал явно**, не сделал молча; аналогии-диаграммы (d16/d22/d26b/d31) деривированы из chapter (не новый контент).

**Что сломалось:**
- **Ad-hoc orchestrator-скрипт для независимой WPM-верификации (Phase 11.5) тоже сломался** — крудовый regex-сплиттер фрагментов дал s32=794 WPM (захватил хвост файла с non-spoken секциями), divider'ы 0.3 мин показал 100-120 WPM (WPM-exempt). Вывод: **ad-hoc одноразовые greps для pacing/word-count ненадёжны; авторитетная ре-верификация — пере-спавн профильного critic'а с его официальным токенайзером** (сделал — methodology-wpm-recheck = PASS).
- pre-gate pacing-grep `Σ duration_min` по split `deck.yaml`+`deck-part2.yaml` суммировал `totals:`/metadata-поля → ложные 144 мин (реально 70+5). Пришлось вручную исследовать структуру.

## MCP / toolchain
- PowerPoint MCP + render-toolchain (libreoffice→pdf→pdftoppm) отработали без новых limitation'ов (designer читал notes/mcp-limitations.md по брифу).
- gh CLI: PR create+merge+issue-close без проблем; PR «Closes #100» авто-закрыл issue.

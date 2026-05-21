# Лекция 11 — Tools reflection

**Дата:** 2026-05-21
**Issue:** #131

## MCP servers / subagents / skills что использовал

### Subagents (spawn count)
- **book-editor** ×4 (Phase 2 chapter draft, Phase 4 v2 revision, Phase 4b v3 expansion to 30k, Phase 4d v4 finalize + continuation после usage-limit hit)
- **presentation-designer** ×3 (Phase 5+6 initial 39 slides + visual loop, Phase 8 heavy revision v1→v2 41 slides, Phase 8.5 timing markers fix, Phase 11 parallel scope s21/s32/s35/s38, Phase 11.5 brewery fix)
- **speech-writer** ×2 (Phase 9 draft, Phase 11 v1→v2 revision)
- **methodology-critic** ×3 (Phase 1 plan, Phase 3 chapter v1, Phase 4c chapter v3, Phase 10 speech v1)
- **fact-checker** ×3 (Phase 3 chapter v1, Phase 4c chapter v3, Phase 7 slides v1, Phase 10 speech v1)
- **reader-simulator** ×2 (Phase 1 plan text-only, Phase 3 chapter v1 text-only, Phase 7 slides v1 rendered)
- **presentation-critic** ×1 (Phase 7)
- **student-simulator** ×1 (Phase 7)
- **consistency-checker** ×2 (Phase 7 slides, Phase 10 final triplet)
- **general-purpose** ×1 (Phase 0 research)

Итого ~22 agent spawn'ов на полное production. Это сопоставимо с предыдущими отраслевыми лекциями (L5/L6/L8/L9).

### Skills used
- `/pre-user-gate mode=chapter` (GATE A)
- `/pre-user-gate mode=slides` (GATE B)
- `/pre-user-gate mode=final` (GATE C)
- `/reflect` (этот сessio)

### Что failed / какие проблемы

**1. Subagent usage limit (Phase 4d revision)**
- Book-editor агент уперся в session limit (resets 11:10 МСК) после 70 tool uses
- Per memory rule `feedback_subagent_usage_limit`: НЕ self-implement, wait + re-delegate.
- **Что сработало:** правильно классифицировал — НЕ написал контент сам, дождался reset (актуальный момент уже был после), commit'нул partial work с явным «Phase 4d partial: P0(3) + 4 P1 closed; pending P1-1 russification sweep + ...», re-delegated continuation. Continuation спавн завершил оставшееся.
- **Lesson:** classification работает, partial commit с честным statement remaining-work помогает re-delegate efficiently.

**2. PowerPoint MCP — нет проблем**
- Все 41 slide отрендерены через `office-powerpoint-mcp-server`. Build scripts (build_lec11.py + build_lec11_part2.py) сработали стабильно через 3+ render rounds.
- `[VERIFY-DAY-OF]`, `[FACT-CHECK]` markers не leaked в visible body (проверено independent regex).

**3. WebSearch (fact-checker)**
- WebSearch использовался для verification фактов: McKinsey 2025, S&P Global 46%, Tesla Optimus dates, IBM Watson sale, BASF Geismar, POSCO etc.
- Стабильно работало, нет fallback'ов на curl/python (memory rule `feedback_use_mcp_directly`).

**4. workspace-mcp — не использовался**
- L11 production был полностью «code-first» — chapter / slides / speech в репо markdown, без Google Drive integration. Это в норме для производственного pipeline (workspace-mcp используется для publish target, который deferred).

### Successes (carry-forward)

- **Phase 7 parallel critics (5 spawns одновременно)** — успешно, все async returned within ~10 мин combined. Background mode работает надёжно.
- **Phase 10 parallel critics (3 spawns)** — то же.
- **Phase 11 parallel revision (speech-writer + presentation-designer одновременно)** — эффективно по времени, но **created scope gap** (brewery slide drift) → cross-artifact verify mandatory.
- **Independent PPTX visible body grep через python-pptx** — caught designer self-report FALSE дважды. Без этого independent verify — два P0 ушли бы к user.

### Что хотелось бы иметь

- **Designer-extras grep script** в `tools/presentation-build/` — централизованный python tool для checks (timing markers / LO codes / VFY leaks / callbacks) над rendered PPTX, чтобы любой pre-gate walkthrough мог запустить single command, а не каждый раз писать inline regex (см. improvements.md).
- **Deep latin-token scan script** аналогично — централизованный в `tools/presentation-build/deep_latin_scan.py` (или уже там?) и вызываемый из pre-user-gate skill автоматически.
- **Hero size measurement tool** — на основе PPTX shape coordinates + slide dimensions, чтобы measure area % реально, не trust agent self-report.

## Tools that worked well — keep using

- python-pptx extract → independent visible-body text для grep (Phase 8.5 + 11.5 caught designer self-report fail using this)
- Multi-spawn background мode для parallel critics — saves wall-clock time
- Reader pre-render image inspection (Read tool with PNG path) — Claude vision captured hero size discrepancy on s01/s39

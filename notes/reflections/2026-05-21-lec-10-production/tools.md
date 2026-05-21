# Tools — Лекция 10 production retrospective

**Дата:** 2026-05-21. **Issue:** #126 closed. **PR:** #136 merged. **Reflection issue:** #137.

## MCP-серверы (использовано)

- **github mcp** — issue_write (create #126, #137), PR merge (gh CLI direct для #136), branch ref update. Стабильно.
- **PowerPoint MCP** — через python builders (build_lec10_p1/p2/p3.py + libreoffice headless + pdftoppm). 43 slides × 3.2 iter average — выдержал. Phase 6 + Phase 8 + Phase 11 — три separate render passes, без проблем.
- **workspace-mcp** — не использовался в этой сессии (все артефакты git-tracked, не Drive).
- **document-loader** — не использовался (chapter 3 файла, текст плоский).
- **drawio** — не использовался (схемы в slides через QuickChart + Lucide icons, не drawio в этой лекции).
- **local-rag** — не использовался.

## Subagent invocations (~25 за сессию)

### Producer agents

| Agent | Spawned | Outcome |
|---|---|---|
| general-purpose (research × 4) | 4 (Phase 1) | ✓ all 4 — 22k слов фактуры (01-real-applications 5618w, 02-failures 6621w, 03-trends 6319w, 04-russian 3790w) |
| book-editor (plan v1 synthesis) | 1 (Phase 1) | ✓ plan-v1 + 00-summary |
| book-editor (plan v2 revise) | 1 (Phase 1) | ✓ plan-v2 APPROVE-CLEAN |
| book-editor (chapter v1) | 1 (Phase 2) | ✓ stopped early; re-spawned с 3-part brief |
| book-editor (chapter v1 3-part) | 1 (Phase 2) | ✓ 21 697 слов / 3 files ≤600 строк |
| book-editor (chapter v2 revise) | 1 (Phase 4) | ✓ 26 519 слов, 5 P0 + 8 P1 + 6 reader P1 fixes |
| book-editor (chapter v3 expansion) | 1 (Phase 4b) | ⚠️ **usage limit hit** — partial 31 194 / target met. Re-delegate not needed (target achieved). |
| book-editor (chapter v3.1 polish) | 1 (Phase 4d) | ✓ 31 960 слов, 7 P1 + 5 P2 batched |
| presentation-designer (Phase 5 spec) | 1 | ✓ 43 slides spec + deck.yaml + all sNN-*.md |
| presentation-designer (Phase 6 visual loop) | 1 | ✓ 43 slides × 3.2 iter mean / max 4 / 0 escalations. PowerPoint MCP + python builders + libreoffice + pdftoppm стабильны. |
| presentation-designer (Phase 8 v2 revise) | 1 (combined w/ 2 ENFORCED rules) | ✓ 8 P0 + 32 P1 batched в один agent. **Pattern proven: batched revision эффективнее serial.** |
| speech-writer (Phase 9 v1) | 1 | ✓ 5,871 слов / 72.5 wpm / 2 anglicism critical hits (vs Лекция 8 catastrophe 919!) |
| book-editor (Phase 11 batched revise) | 1 (3 artifacts atomic) | ⚠️ **usage limit hit** at start — re-spawned после reset 17:00 MSK; second invocation ✓ |
| book-editor (Phase 11 re-spawn) | 1 | ✓ speech v2 + chapter v3.2→v3.3 cascade + slides s05/s10/s37s re-render |

### Critic agents

| Agent | Count | Pattern |
|---|---|---|
| methodology-critic | 5 (plan-v1, plan-v2 narrow, chapter-v1, chapter-v3 narrow, speech-v1) | Все 5 returned actionable verdicts; counter-check trigger (≥5 P1 → REVISE) сработал на chapter-v1 (8 P1 → REVISE) + slides-v1 (10 P1 от presentation-critic → REVISE) |
| fact-checker | 4 (chapter-v1, chapter-v3 narrow, slides-v1, speech-v1) | Full citation sweep на chapter-v1 + slides-v1 + speech-v1 (не subset — Лекция 9 lesson). 5 P0 в chapter-v1 + 4 P0 в slides-v1 + 3 P0 в speech-v1 — все WebSearch-verified |
| reader-simulator (text-only) | 2 (plan-v1, chapter-v1) | Caught P0s missed by methodology — closed-loop undefined, jargon без glossary, vertical farming распилка |
| reader-simulator (rendered) | 1 (slides-v1) | 2-weeks self-containedness check — 83% strong, 8 P1 polish |
| presentation-critic | 1 (slides-v1) | Vision-enabled — caught s02 cover wrong title (P0!), 84 anglicism non-brand (vs designer self-report 66) |
| student-simulator | 1 (slides-v1) | Caught s09 density burnout (P0), spec card font ≥14pt (P0) |
| consistency-checker | 2 (slides-v1 chapter↔slides, speech-v1 3-artifact) | Caught D1 Магнит missing, D3 5-level ladder missing в s37, Tzachor date drift, Bowery $500M drift |

**Total ~25 agent invocations**, 2 usage-limit hits, **0 fundamental failures**. Все REVISE verdicts были обоснованы и привели к concrete fixes.

## Worktree + git update-ref pattern

- `/tmp/lec-10-wt` создан с `git worktree add -b issue-126-lec-10 origin/main`
- Все edits в worktree; commits в worktree branch
- `git -C main_repo update-ref refs/heads/issue-126-lec-10 <commit-sha>` — sync branch ref после каждого commit для visibility в main repo path
- Pre-USER-GATE B artifacts sync: rsync from worktree → main repo `library/lectures/lec-10/` (PPTX + PDF accessible до GATE)
- Финальный cleanup: `git worktree remove --force` + `git branch -D` после merge

**Verdict:** worktree-pattern проверенный, scales для parallel lectures (lec-12/13/14 worktrees coexist).

## Что мешало

### Usage limits (2 раза)
- **Phase 4b chapter v3 expansion:** hit limit mid-expansion. Partial result (Part 1 expanded substantially) — target ≥30k achieved, не было нужды re-spawn.
- **Phase 11 batched revise:** hit limit на start. Re-spawned после 17:00 MSK reset; second invocation completed successfully. **Memory rule `feedback_subagent_usage_limit` correctly applied** — orchestrator не self-implement.

### Self-report inflation
- Phase 6 designer self-report «66 unique non-brand candidates, all proper nouns» → independent presentation-critic scan **84 hits** (~27% inflation).
- Phase 9 speech-writer self-report «2 critical anglicism hits» → independent methodology-critic broad regex **43 hits**.
- **Pattern:** subagent self-grep НЕ совпадает с independent broad-regex orchestrator pass. **Pre-USER-GATE Walkthrough Rule §5** уже ENFORCED orchestrator-INDEPENDENT — это работает.

### Tools без issue
- Python builders для PPTX (build_lec10_p1.py + p2.py + p3.py) — 4 итерации (Phase 6 / Phase 8 v2 / Phase 11 cascade s05/s10/s37s). Stable, ~600 lines each.
- Libreoffice headless + pdftoppm для PNG snapshots — стабильно на 43 slides × 3-4 раза = ~150 conversion ops без сбоев.

## Новые tools или improvements нужны?

- **NEW:** orchestrator-INDEPENDENT timing+methodology grep (Pre-USER-GATE Walkthrough §5 расширено) — уже в инфраструктуре через PR #136.
- **NEW:** Baseline coverage sample check (Pre-USER-GATE точка 12) — уже в инфраструктуре.
- **WISH:** auto-script `tools/presentation-build/preflight_grep.py` для one-shot independent walkthrough всех 3 групп (scaffold + timing + methodology + baseline sample) — manual grep работает, но автоматизация снизит cognitive load. **→ improvements.md P2.**

## Permission issues

Нет permission issues. Все MCP servers + git + python + libreoffice работали без auth/scope проблем.

## Tool selection mistakes

Нет фундаментальных mistakes. Один minor — Phase 5 sub-IDs (s30b, s37s, s38s, s35c, s36c) создали non-sequential нумерация, что путало critics в Phase 7 (presentation-critic ссылался на s42/s43 = pptx index; consistency-checker на slide_id с sub-IDs). **→ improvements.md P3:** post-Phase 5 renumber sub-IDs to sequential before Phase 6 rendering.

## Summary

Tool stack stable; 25 agent invocations / 2 usage-limits handled / 0 fundamental failures. Batched revision pattern (Phase 8 + Phase 11) проверен и эффективен. Pre-USER-GATE orchestrator-INDEPENDENT grep дополнен 2 NEW groups (timing + methodology + baseline) — уже в инфраструктуре через PR #136.

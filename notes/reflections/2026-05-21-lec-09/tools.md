# tools.md — Лекция 9 production

**Session:** 2026-05-20 to 2026-05-21
**Issue:** #118 → PR #120 merged

## Subagents used (17 spawns total)

| Phase | Agent | Outcome |
|---|---|---|
| 0 | general-purpose (research) | ✓ 5 файлов, 110 источников |
| 1 | methodology-critic + reader-simulator(text-only) | ✓ 2 parallel |
| 1 | book-editor (plan v1+v2) | ✓ 2 sequential |
| 2 | book-editor (chapter v1 draft) | ✓ |
| 3 | methodology-critic + fact-checker + reader-simulator(text-only) | ✓ 3 parallel |
| 4 | book-editor (chapter v1→v2 revision) | ✓ |
| 4 | fact-checker (subset rerun UN LAWS) | ✓ |
| 4 | book-editor (chapter v2→v3 anonymize + glossary) | ✓ |
| 5-6 | presentation-designer (deck v1 + v2 revision) | ✓ 2 spawns, second after orchestrator flagged P0s |
| 7 | presentation-critic + student-sim + reader-rendered + consistency + fact-checker | **4 of 5 первично; consistency-checker FAILED API 529 × 2; 3-й retry succeeded** |
| 8 | presentation-designer (slides v2→v3) | ✓ |
| 9 | speech-writer | ✓ |
| 10 | methodology-critic + fact-checker + consistency-checker | ✓ 3 parallel |
| 11 | presentation-designer (s18b source) + speech-writer (v1→v2) | ✓ 2 parallel |

## Tool failures

### API 529 Overloaded × 2 (consistency-checker Phase 7)
- **What:** Anthropic API server-side overload errors. First retry — 0 tool uses, 0 tokens, immediate fail.
- **When:** During parallel 5-critic Phase 7 spawn.
- **Resolved:** 3rd retry succeeded после ~30 min cooldown.
- **Structural?** Не subagent failure (memory rule `feedback_subagent_usage_limit`). Не «do work directly» trigger.
- **Lesson:** API 529 на critic-spawns не редкость когда параллельно 5+. Defer retry на 30+ min, не immediate.

### Speech-writer self-report inflation
- **What:** Phase 9 v1 self-report «0 anglicism hits» — реальность 107 distinct patterns / 186 occurrences.
- **What:** Phase 5-6 designer v1 self-report «72% media-rich» — реальность 0 real photos (только primitives + icons).
- **Structural:** Subagent self-report без orchestrator-side verification regex / count → systematically inflated.
- **Lesson:** Need agent-side mandatory output checks ДО submission (e.g., speech-writer should run own anglicism grep + report actual count, not narrative «0 hits»).

## Skills used

- `/loop` — not used (production был ad-hoc driven, not interval polling)
- `/pre-user-gate` — not invoked explicitly, but manual walkthrough done at each gate (A/B/C)
- `/reflect` — invoked at session end (this session)

**Gap:** `/pre-user-gate` skill exists but wasn't auto-triggered between gates. Worked manually OK but inconsistent.

## MCP / render-toolchain issues

### Chrome missing for mermaid-cli
- **Documented:** `notes/mcp-limitations.md` #118-1 — добавлено при Phase 5-6 v1.
- **Workaround:** python-pptx shapes для diagrams вместо mermaid.
- **OK** — designer agent applied workaround, не блокировал production.

### Wikimedia REST API as image acquisition source
- **Worked:** Tier 2 (Wikipedia REST → Commons imageinfo) succeeded для 17/15 photo targets (113%).
- **Initial fail:** Direct URL downloads 404/429 — switched to Commons API thumbnails.
- **Lesson:** 6-tier acquisition pattern из `feedback_no_mock_fallbacks` работает, но agent default Tier 1 (og:image) failed, нужно явно encouraging Tier 2.

## Permission issues

- Worktree write OK
- Main repo sync OK (PPTX + PDF копировались)
- GitHub PR create OK
- GitHub PR merge OK через `gh pr merge`
- Local branch delete blocked initially (worktree still attached) — `git worktree remove` решил

## Tool selection mistakes

- **Direct chapter v3→v4 P0 fact fixes via orchestrator Edit** — вместо delegation book-editor. Это были exact string replacements, low-risk, но конкретно границу «orchestrator-allowed vs delegate» можно поджать. Лекция 9 — приемлемо, но для бОльших изменений (например glossary RU column expansion) надо явно delegate.

- **Phase 5-6 v1 designer brief не включал явно `feedback_no_mock_fallbacks`** — это memory rule, и default subagent brief должен включать его для media-heavy decks. Только после первого v1 fail orchestrator добавил в v2 brief. Должно быть default в `.claude/agents/presentation-designer.md` или skill `/build-deck`.

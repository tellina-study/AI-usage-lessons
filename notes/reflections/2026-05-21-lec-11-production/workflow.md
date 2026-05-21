# Лекция 11 — Workflow reflection

**Дата:** 2026-05-21
**Issue:** #131

## Git compliance

### Mandatory Git Rules (CLAUDE.md)
- ✓ NEVER push to main directly — branch `issue-127-lec-11-manufacturing` создан, всё через PR #130
- ✓ Branch naming `issue-127-lec-11-manufacturing` — convention compliant
- ✓ Every commit references issue `#127` в message — все 36 commits
- ✓ create branch → commit → push → PR → merge — выполнено
- ✓ PR merge только по прямому указанию user («мерж, рефлексируй, закрывай» — explicit) — мержил сам через `gh pr merge`
- ✓ No work without an issue — issue #127 создан до старта работы

**Bonus issue #128** (Chapter 30k baseline rule PR #129) — создан в parallel branch когда user сказал «запишешь 30к минимум в базовые правила». Отделён в свой branch + PR для clean review. Both merged.

### Worktree isolation (Multi-Lecture Parallel)
- ✓ Worktree `/tmp/lec-11-wt` поднят на `--detach` from main, branch `issue-127-lec-11-manufacturing` checked out внутри
- ✓ Все subagent spawns включали explicit «cd /tmp/lec-11-wt FIRST» в prompt + check `git branch --show-current`
- ✓ Branch ref пропагирован через push (не git update-ref — pushed напрямую от worktree)
- ✓ Pre-USER-GATE B/C artifacts sync mandatory выполнен (с inode-diff verification)
- ✓ Не было branch contention с parallel session (other lectures не в production)

## Phase gating compliance

### 11 phases + 3 USER GATEs все passed:
- Phase 0 — Research (general-purpose агент)
- Phase 1 — Plan v1 → critique → Plan v2
- Phase 2 — Chapter draft v1
- Phase 3 — 3-critic critique (parallel)
- Phase 4 — Chapter revision v2
- **Phase 4b** (бонус) — Chapter expansion v2→v3 (30k owner mandate) — **новая фаза, не в стандартном pipeline**, проложена ad-hoc
- Phase 4c — Chapter v3 focused critique (methodology + fact-checker, без reader-text-only — структура не менялась)
- Phase 4d — Chapter v4 finalize (hit usage limit + continuation re-delegate)
- **Phase 4e** (бонус) — Multi-part split v4→v5 (доп. shape за рамкой стандарта)
- Phase 4.5 — Pre-USER-GATE A walkthrough → **GATE A approved**
- Phase 5 — Slides content design (deck.yaml + slides/*.md)
- Phase 6 — Slides visual loop (39 slides render)
- Phase 7 — 5-critic QA (parallel)
- Phase 8 — Slides v1→v2 heavy revision (9 P0 + 28 P1 + 12 P2 + owner mandates M1/M2/M3 + 2 new slides s34b/s34c)
- Phase 8.5 — Pre-USER-GATE B walkthrough caught timing markers P0 → quick fix → **GATE B approved**
- Phase 9 — Speech draft v1
- Phase 10 — 3-critic critique (parallel)
- Phase 11 — Speech v1→v2 revision parallel со slide patches (4 slides)
- Phase 11.5 — Pre-USER-GATE C walkthrough caught brewery slide drift P0 → quick fix → **GATE C approved**

**3 USER GATE breakdown:**
- GATE A — 2 рaунда (v4 single-file + v5 multi-part after user requested split)
- GATE B — 1 раунд (после Phase 8.5 timing fix)
- GATE C — 1 раунд

**Counter-factual:** Lec-1 had 3 user feedback rounds AFTER critic approve. Lec-11 имел 0 rounds после GATE — pre-USER-GATE walkthrough поймал все P0 до presenting. Это паттерн который окупается.

## Roast-before-implement

Не вижу строгого roast step в L11 production — это standard pipeline с known phases. Но **owner explicit decisions** добавляли роасты в реальном времени:
- Owner «30к цель твоя» после approval v2 chapter — это de facto roast «too thin, deepen»
- Owner «убери методические и временные комментарии» — это de facto roast того что designer полу-implicit добавил
- Owner «переведи цитаты на русский» — это de facto roast «English quotes на visible body это конфликт с RU аудиторией»

Эти 3 mid-stream re-directs добавили несколько revision rounds но улучшили финальный quality. Worth it.

## ENFORCED rules compliance

### AI-Failure & Judgment ≥30% strict-in (фундаментальное)
- ✓ Chapter v5: 41.1% chapter words (methodology-critic independent recount)
- ✓ Slides v2.2: 61% strict-in (presentation-critic Phase 7)
- ✓ Speech v2: ~40-45% strict-in (methodology-critic Phase 10 41.1%)
- ✓ Distributed по всем 5 разделам, не сконцентрировано в §4
- ✓ L4+ (waiver не доступен), правило применено

### Chapter Depth Baseline ≥30k (новое, recorded PR #129)
- ✓ Chapter v5: 30 930 слов (target hit ±5%)
- ✓ Multi-part split при >600 строк: 3 файла (409/510/592)

### Pre-USER-GATE Walkthrough (ENFORCED)
- ✓ GATE A walkthrough run twice (v4 + v5 split)
- ✓ GATE B walkthrough caught timing P0 → fix → re-run
- ✓ GATE C walkthrough caught brewery P0 → fix → re-run
- ✓ Designer-extras grep ORCHESTRATOR-INDEPENDENT каждый раз (Лекция 4 lesson ENFORCED)
- ✓ Deep latin-token scan на rendered PPTX visible body (Лекция 8 lesson ENFORCED)
- ✓ Hero check ≥40% area (Лекция 8 lesson ENFORCED)
- ✓ Real-image verification sample (Лекция 8 lesson ENFORCED)

### No Extra Content Rule
- ✓ Designer-extras owner-mandate M1 enforced
- ⚠️ But designer SELF-REPORT was FALSE дважды (Phase 8 → timing markers; Phase 11 → brewery drift). Independent verify caught both.

### Anonymization
- ✓ 0 named institutions (МГТУ/Бауман/ИУ/Кафедра) во всех 3 артефактах
- ✓ Audience «студенты-инженеры 3 курса (универсальная)»

## Что не сработало (workflow gaps)

### Designer self-report reliability
**Phase 8 producer report:** «designer-extras 17→0, timing markers сметены, hero ≥40%»  
**Independent reality:** 10 timing markers still visible on 6 dividers, hero s01 31% / s39 32.5% (NOT ≥40%)

**Phase 11 producer report:** «4 slide fixes complete (s21/s32/s35/s38)»  
**Independent reality:** brewery slide s34c left with 60K bph drift (still pointed к chapter §4.3c 30K). Designer parallel scope didn't include s34c (speech-writer fixed brewery in speech, designer fixed unrelated slides).

**Lesson:** Лекция 4 «designer self-grep FALSE» паттерн повторился ДВАЖДЫ в L11. Independent orchestrator regex/grep остаётся mandatory. См. improvements.md для централизованных tools.

### Parallel revision scope drift
Phase 11 spawned speech-writer + presentation-designer параллельно. Каждый получил scope brief. Speech-writer фиксил **brewery numbers в speech** (P0-1 alignment). Presentation-designer фиксил **s21/s32/s35/s38** (slide P0s). Brewery slide s34c НЕ был в scope ни одного.

**Lesson:** при parallel revision спавнах — orchestrator должен **explicitly** перечислить cross-artifact alignment requirements, не assume что producer проинвентаризует sibling artifacts. Brewery нужно было быть в scope **обоих** агентов с явным «verify alignment your fix matches other artifact's fix».

### Snapshot numbering shift
s34b + s34c вставлены between s34 и s35. PNG snapshots renumbered (s-35.png теперь это s34b, s-36 — s34c, s-39 — s37 recap, s-41 — s39 closing hero). При pre-USER-GATE walkthrough визуально перепутал s-39.png с slide s39 — поначалу думал что closing hero не на месте.

**Lesson:** mapping rendered-PNG-position vs source-slide-ID — нужен явный sidecar (например, `rendered/slide-index.yaml` с маппингом). При check'ах визуально надо использовать source name, не position.

## Что сработало (carry-forward)

- **Worktree isolation** + branch push from worktree without main checkout — clean.
- **Background parallel critics** (5 в Phase 7, 3 в Phase 10) — saves wall-clock time.
- **Pre-USER-GATE walkthrough as separate phase** ловит P0 до presenting user — saves user-feedback rounds.
- **Manifest update в том же finalizing PR** (GATE-C definition-of-done ENFORCED — соблюдено).
- **Issue → branch → PR → merge → close cycle** runs cleanly with `gh` CLI.
- **Honest partial commits при usage-limit** позволяют resume без потери work.

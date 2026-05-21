# Лекция 11 — Improvements

**Дата:** 2026-05-21
**Issue:** #131

## Actionable improvements (extracted from 4 reflection files)

| # | Improvement | Priority | Effort | Component | Action |
|---|---|---|---|---|---|
| I-1 | **Designer-extras grep script централизованный** | P0 | S | `tools/presentation-build/deep_designer_extras_scan.py` (existing file ref) | Создать (или дополнить) single script that runs orchestrator-INDEPENDENT regex sweep over rendered PPTX visible body. Pattern includes: Лектору / Вы здесь / [VFY] / [FACT-CHECK] / LO[1-9] / §[0-9] / → s[0-9] / (sNN) / тайминг «N мин» / callback / возвращаемся / payoff / course-scaffold. Invoke from pre-user-gate skill automatically. |
| I-2 | **Cross-artifact numbers alignment check script** | P0 | M | `tools/lecture-production/cross_artifact_numbers_check.py` (new) | Создать script: scan chapter+slides+speech for measurable claims (numbers, percentages, dates, dollar amounts) + report drift between artifacts. Anchor to chapter as canonical. Caught brewery drift would be auto-detected before GATE C. |
| I-3 | **Parallel revision agent scope cross-reference mandate** | P0 | S | `tools/lecture-production/README.md` § «Polish Round Pattern» | Add rule: «When spawning parallel revision agents (speech-writer + presentation-designer simultaneously), brief MUST include EXPLICIT cross-artifact alignment requirements — каждый агент verify его fix matches sibling artifact's fix. Anchored к canonical source (usually chapter)». Carry forward от L11 Phase 11 brewery scope gap. |
| I-4 | **Hero size measurement independent tool** | P1 | M | `tools/presentation-build/hero_size_check.py` (new) | Создать script: extract image shape coordinates from PPTX (python-pptx shape.width × height) / slide_dimensions → calculate area %. Used to verify designer hero self-report (≥40% mandate). Caught L11 s01 31% / s39 32.5% would have flagged P0 before GATE B. |
| I-5 | **Pre-USER-GATE skill: invoke централизованные scripts** | P1 | S | `.claude/skills/pre-user-gate/SKILL.md` | Update skill: each Step (designer-extras grep / deep latin / hero check) calls централизованный script вместо inline regex. Reduces manual orchestrator effort + ensures consistency. |
| I-6 | **Russification rule: include quote translation mandate** | P1 | S | `~/.claude/projects/-home-levko-AI-usage-lessons/memory/feedback_russification.md` | Update memory rule: «Russification mandate extends to foreign-language quotes — RU primary, original (English/etc.) optional in speaker notes parenthetical italic gloss only». Caught L11 owner mandate M3 explicit. |
| I-7 | **Rendered PPTX slide-index sidecar** | P2 | S | `library/lectures/lec-NN/rendered/slide-index.yaml` | Auto-generated mapping: rendered_PNG_position → source_slide_id (е.g. «s-36.png → s34c-brewery-cv-qc-pass.md»). Helps orchestrator visual sweeps after slide insertions. L11 had s34b/s34c insertion → PNG numbering shifted +2; mapping not obvious. |
| I-8 | **Numbers convention lock at Phase 1 plan** | P1 | S | `templates/lecture-outline.md` + Phase 1 plan-checklist | Add section в plan template: «Numbers convention lock» — every worked example numbers locked at plan stage (e.g. brewery «30K bph canonical»), propagated to all 3 artifacts. No revision allowed without explicit cascade-of-changes check. |
| I-9 | **Proactive L_{N-1} compare in GATE walkthroughs** | P1 | S | `.claude/skills/pre-user-gate/SKILL.md` (or orchestrator pattern) | Add to GATE walkthrough: «compare quality metrics vs L_{N-1} + L_{N-2} (chapter word count / slide count / failure-bucket % / media coverage)». Flag any drop proactively. L11 owner had to flag «chapter L4/L5 length». |
| I-10 | **Cornerstones full-phrase introduction verification** | P2 | S | `consistency-checker` agent prompt | Update: «when artifact uses acronym (e.g. RL, CV, PdM), verify first occurrence has inline gloss с full canonical phrase (обучение с подкреплением, компьютерное зрение, прогностическое обслуживание)». L11 slides had 0 «обучение с подкреплением» full phrase — only «RL» acronym. |
| I-11 | **Numbered owner mandates M1/M2/M3 pattern formal recognition** | P2 | XS | `CLAUDE.md` anti-patterns table или methodology section | Add note: «Owner multi-part mandates often arrive as «do X + do Y + do Z». Orchestrator labels each as M1/M2/M3 in spawn briefs, treats each как independent acceptance criterion. L11 M1 (no methodology comments) / M2 (no anglicisms) / M3 (translate quotes) worked well.» |
| I-12 | **Phase 4b chapter expansion as standard pipeline option** | P2 | M | `tools/lecture-production/README.md` § «Workflow» | Pipeline currently doesn't have explicit «chapter expansion phase» between Phase 4 (v2 finalize) and Phase 5 (slides). Add Phase 4b conditional: «if owner explicit deep-target, spawn expansion book-editor». L11 used this ad-hoc. |
| I-13 | **Chapter Multi-part split as Phase 4e** | P2 | S | `tools/lecture-production/README.md` § «Workflow» | Document Phase 4e (multi-part split при >600 строк per file) as standard step. L11 used ad-hoc. CLAUDE.md «Chapter Depth Baseline» already mandates split at ≥30k → bake into pipeline. |

## Priority breakdown

- **P0 (3):** Designer-extras script (I-1) / Cross-artifact numbers check (I-2) / Parallel revision cross-reference mandate (I-3)
- **P1 (5):** Hero size check (I-4) / Pre-USER-GATE central scripts (I-5) / Russification quote translation (I-6) / Numbers convention lock (I-8) / Proactive L_{N-1} compare (I-9)
- **P2 (5):** Slide index sidecar (I-7) / Cornerstones acronym verification (I-10) / Mandate M-numbering pattern (I-11) / Phase 4b expansion (I-12) / Phase 4e split (I-13)

## Action plan

### Immediate (этот reflection PR)
- ✓ Update memory rule `feedback_russification` с quote translation mandate (I-6) — small inline update
- ✓ Update CLAUDE.md anti-patterns / Polish Round Pattern with parallel revision cross-reference mandate (I-3)
- ✓ Update `tools/lecture-production/README.md` § Workflow с Phase 4b + 4e formal entries (I-12 + I-13)
- ✓ Note Russification mandate extension в memory

### Follow-up issues to create (per reflect skill step 5)
- **Issue для I-1** Designer-extras script — может уже частично существует (mentioned в CLAUDE.md «deep_latin_scan.py»); create issue для full implementation OR audit что есть
- **Issue для I-2** Cross-artifact numbers alignment check script — new tool, need design
- **Issue для I-4** Hero size measurement tool — new tool
- **Issue для I-5** Pre-USER-GATE skill scripts integration — depends on I-1/I-4

## Carry-forward для L10 / L12 / L13+

1. **Variant C-style keystone** (two-column taxonomy contrast) — proven pattern для отраслевых лекций
2. **3 worked examples bi-directional filter** (pass + pass + fail) — strong LO8 demonstration
3. **4 categories decision framework** — actionable artifact
4. **5 vendor questions** (Q5 «past failures») — concrete deliverable
5. **Real Wikimedia CC-BY-SA Tier 2 acquisition** — clean licensing pattern (Tier 1 press kits + Tier 2 Wikimedia first)
6. **Chapter ≥30k baseline + multi-part split при >600** — теперь enforced rule
7. **M1/M2/M3 owner mandate labeling** — clean spawn brief structure
8. **Independent verify cross-artifact + designer-extras** — Лекция 4 паттерн всё ещё повторяется → этот check критичен
9. **Honest partial commit при usage-limit + re-delegate** — successful pattern для resume

# Consolidated Implementation Plan — Lecture 1 → Lecture 2 quality leap

**Source documents:**
- `REFLECTION.md` (broad, ~6750 words, 7 categories, 12 sections) — primary failure-mode catalog.
- `REFLECTION-roast.md` (~3500 words) — methodology-critic roast: 15 missed failures + 12 unactionable→concretize + 8 risks for L2 + 10 extra recommendations.
- `REFLECTION-visual-audit.md` (presentation-critic visual specialist) — 16 designer self-acceptance fails + 7 schema design patterns + Schema Readability Checklist (7 subtypes) + No Extra Content Rule + 5-Second Test + Visual Loop iteration cap + Cross-Slide Redundancy grep + Projector Readability + Iconography Discipline + Visual Mass Balance + 20 visual anti-patterns (16-35).

**Date:** 2026-05-13.
**Goal:** одно-shot quality на Лекции 2, без 3 раундов user feedback.
**Pre-condition for use:** этот документ — единственный источник для implementation phase. Не нужно читать reflections заново.

---

## Executive Summary

Production Лекции 1 v3.x дала APPROVE-WITH-MINOR от всех 4 critics на финальных артефактах, но **user возвращался с substantial revisions трижды** (62 user-driven changes в 3 раундах). Корневая причина — критики проверяют compliance с playbook, но **слепы к 5 классам проблем**: (1) schema readability for laymen (s11/s13/s16 переделывались 2-3 раза), (2) curriculum relevance (Pearl/ARC-AGI/Copilot — методически OK, но не для introductory лекции), (3) terminology drift между артефактами («Приложение-робот» имел 3 формы), (4) designer-added content без request (тайминг, «вы здесь», «Лектору» секция, subtitle, s14-deletion), (5) tools/data freshness (Llama-3 как «свежий пример», ARC-AGI 37.6% устарело за 2 дня). Visual production — 14+ итераций, 5 параллельных designers с file-lock конфликтами, 562 PNG snapshots (71MB, P0-bloat при масштабе 17 лекций), build script proliferation (7 scripts).

**Critical changeset (16 файлов):** 1 CLAUDE.md (Pre-USER-GATE protocol + No-Extra-Content rule + glossary lock), 9 agent prompts (`presentation-designer.md` основная переработка с Schema Readability Checklist для 7 subtypes + 5-Second Test + No Extra Content + Iconography Discipline + Visual Mass Balance + Cross-Slide Redundancy grep + Projector Readability + Visual Loop iter cap; остальные 8 — точечные дополнения), 2 methodology docs (`tools/lecture-production/README.md` + `tools/presentation-build/README.md`), 2 notes (`notes/decisions.md` + 20 anti-patterns + `notes/mcp-limitations.md` + 3 новых записи), 1 skill (`build-deck/SKILL.md`), `.gitignore` snapshot policy + build script consolidation policy.

**Estimated effort:** 6-8 hours total. Phase 1 (P0 agent updates) — 2-3 hours; Phase 2 (P0 methodology docs) — 1 hour; Phase 3 (P1 decisions + limitations) — 1 hour; Phase 4 (P1 CLAUDE.md) — 30 min; Phase 5 (P2 hygiene) — 1 hour; Phase 6 (P2 skills) — optional 30-60 min.

**ROI estimate:** Без implementation Л2 повторит 2-3 user feedback rounds × 5 hours wall-clock = 10-15 hours потерь. С implementation — целевая метрика 1 user feedback round (~2-3 hours). Net savings 7-12 hours за Л2 + cumulative effect для Л3-Л17.

---

## Top-10 Action Items (приоритизировано по impact × ease)

| # | Action | Priority | Effort | Files affected | Source ref |
|---|---|---|---|---|---|
| 1 | Schema Readability Checklist для 7 subtypes (matrix/quadrant/layered/cycle/pipeline/timeline/architecture) + 5-Second Test gate | **P0** | 60 min | `presentation-designer.md`, `presentation-critic.md`, `tools/presentation-build/README.md` | REFLECTION §3.1 + §4.1 + §5.3, ROAST #2 unactionable, VISUAL-AUDIT primary content |
| 2 | No Extra Content Rule (8 forbidden additions: subtitle, navigation marker, тайминг, лектору section, «вы здесь», color-only highlight + text marker redundancy, designer-driven slide deletion без user request, dummy SVG/icon decorations) | **P0** | 30 min | `presentation-designer.md`, `presentation-critic.md`, CLAUDE.md | REFLECTION §3.1 Failure 2 + §2.4 + ROAST #2 (s14 deletion), VISUAL-AUDIT |
| 3 | Pre-USER-GATE walkthrough protocol (orchestrator scrolls through PNG + reads notes-as-student + lists issues BEFORE presenting to user) | **P0** | 45 min | CLAUDE.md, `tools/lecture-production/README.md`, `build-deck/SKILL.md` | REFLECTION §7.4 + Top-5 P0-2 + ROAST Risk 4 |
| 4 | WPM hard rule в speech-writer (refuse output if any fragment >95 WPM; trim/split рекомендация) | **P0** | 15 min | `speech-writer.md` | ROAST missed failure #1 + Risk 1 |
| 5 | Speaker notes contract: 150-300 words readable text, NO layout descriptions, NO лекторские cues, derived from chapter §X + speech [sNN] | **P0** | 30 min | `presentation-designer.md`, `book-editor.md`, `tools/lecture-production/README.md` | REFLECTION §2.1 #1 + §5.1 + Top-5 P0-1 |
| 6 | Curriculum relevance + freshness check в methodology-critic (Bloom-level threshold matrix per lecture-level + temporal relevance per AI/benchmark fact) | **P0** | 30 min | `methodology-critic.md` | REFLECTION §3.4 + §5.6 + ROAST missed #11 |
| 7 | Terminology drift sub-check + glossary lock после chapter approval (consistency-checker запускается перед каждым USER GATE; critics flag inconsistency, MAY NOT propose rename) | **P0** | 30 min | `consistency-checker.md`, `tools/lecture-production/README.md`, CLAUDE.md | REFLECTION §3.6 + §5.2 + ROAST missed #6 + Risk 6 |
| 8 | Visual Mass Balance + Cross-Slide Redundancy grep + Projector Readability (50% zoom) + Iconography Discipline в presentation-designer + presentation-critic | **P0** | 45 min | `presentation-designer.md`, `presentation-critic.md`, `tools/presentation-build/README.md` | VISUAL-AUDIT (primary), REFLECTION §4.1 |
| 9 | Snapshot gitignore policy (gitignore ALL `**/snapshots/iter*.png` + `**/snapshots/fix*.png` AND все iteration-snapshot variants; keep only `sNN.png` финальные) + build script consolidation policy (1 canonical `build.py` per lecture) | **P0** | 30 min | `.gitignore`, `tools/lecture-production/README.md` | REFLECTION §6.3 + §8.1 + ROAST missed #7 + #8 + Risk 8 |
| 10 | Visual Loop iteration cap (max 7 iter per slide → automatic STOP + escalate to orchestrator) + designer brief strict YAML format (modify/leave_untouched/forbidden_additions) | **P1** | 30 min | `presentation-designer.md`, `tools/presentation-build/README.md`, `build-deck/SKILL.md` | REFLECTION §3.1 Failure 1 + ROAST extra #5 + #6, VISUAL-AUDIT iteration cap |

---

## File-by-file Changeset

### 1. `CLAUDE.md`

**Current state (relevant sections):** Phase Gating Rule, Subagent Rules, Anti-Patterns table, Working Conventions/Subagents.

**Changes (4 additions, 1 update):**

#### 1.1 ADD section «Pre-USER-GATE Protocol (ENFORCED)» — после «Phase Gating Rule»

Дословно для добавления:
```markdown
## Pre-USER-GATE Protocol (ENFORCED)

Before presenting any artefact for USER GATE approval, orchestrator MUST run the
`pre-gate-review` skill (or do equivalent manually). This catches issues that
critics miss (relevance, schema readability, terminology drift, designer-added
extras).

**Procedure:**
1. **Visual scan all PNG snapshots** (slides) — list issues found.
   Use Read tool on each `library/lectures/lec-NN/rendered/snapshots/sNN.png`.
2. **Read all speaker notes as student** — list places where notes describe
   layout instead of explaining content for self-study.
3. **Read speech as lecturer-perspective** if applicable — list orphan
   references (sections referencing deleted slides), WPM violations
   (>95 wpm на любом фрагменте), tone drift.
4. **Run automated checks:**
   - `grep -i 'лектору\|вы здесь\|субтитр\|на этой странице'` across slides/*.md
     (designer-added markers — should be empty).
   - `grep -i 'iter[0-9]\|fix[0-9]'` across snapshots/ (iteration leaks — should be empty).
   - Cross-slide content redundancy: `grep` titles + assertions for repeats.
5. **Apply quick fixes** (P2 cosmetic) directly OR delegate to producer agent.
6. **Present to user** as: «I reviewed and found N issues — fixed M, pending K
   because [reason]. Anything you'd add?»

**Hard rule:** «approve» = «I (orchestrator) reviewed visually + critics
approved», NOT «critics approved». No USER GATE without explicit pre-review
report from orchestrator.
```

#### 1.2 ADD section «No Extra Content Rule (ENFORCED)» — после «Anti-Patterns»

Дословно:
```markdown
## No Extra Content Rule (ENFORCED for designer/writer agents)

Producer agents (`presentation-designer`, `book-editor`, `speech-writer`) MUST
NOT add content beyond what the task brief requests. **Improvements are
REPORTED to orchestrator, not implemented.**

**8 forbidden additions** (concrete enforcement list):
1. Слайд-subtitle, не запрошенные в brief.
2. Navigation markers («вы здесь», «продолжаем», «к следующему разделу»).
3. Тайминг видимый студенту (на слайде, в notes для студента — не в speech.md).
4. «Лектору» секции внутри speaker notes (cues для лектора → speech.md, не notes).
5. Decorative SVG/icons без semantic role (только если schema требует визуально).
6. Color-only highlight + text marker redundancy (single mechanism per signal).
7. Designer-driven slide deletion/addition без user request (s14 deletion case).
8. Cross-slide bridge text не запрошенный («как мы видели на s10», «вспомним»).

**Enforcement:** `presentation-critic` runs grep на designer output vs task
brief deliverables list — любое addition flagged как P1.

**Exception:** если designer/writer видит opportunity for improvement — REPORT
в final message orchestrator'у с «proposed addition + reasoning», ждать
explicit approval.
```

#### 1.3 ADD section «Glossary Lock (ENFORCED)» — после «No Extra Content Rule»

Дословно:
```markdown
## Glossary Lock (ENFORCED, after chapter approval)

После Phase 4 USER GATE 1 (chapter approved) — orchestrator generates
`library/lectures/lec-NN/glossary.yaml` со списком 15-25 ключевых терминов
лекции. Все downstream artefacts (slides, speech) MUST использовать **exact
form** терминов из glossary.

**Critics MAY:** flag inconsistency (term X has form A в chapter, form B в slide).
**Critics MAY NOT:** suggest rename без explicit USER approval. Critic-driven
terminology rename = pattern, который сам создаёт drift (см. case
«Приложение-робот → -автоматизация → в режиме автоматизации»).

**Glossary format:**
```yaml
glossary:
  - canonical: "Приложение-робот"
    aliases_forbidden: ["Приложение-автоматизация", "Приложение (автоматизация)"]
    definition_short: "Программа, выполняющая последовательность действий без AI."
    introduced_in: chapter §3.6
  - canonical: "narrow AI"
    aliases_allowed: ["узкоспециализированный AI"]
    forbidden_in_lecture: false
```

Glossary update — только через explicit USER approval + sync во все 3 артефакта.
```

#### 1.4 UPDATE existing section «Subagent Rules» — добавить 2 строки в конец

Добавить:
```markdown
- All critic agents MUST save reports as files before completing. Path enforced
  in spawn prompt (`output_file: ABSOLUTE_PATH`). If save fails, agent must
  Write retry explicitly + Bash verify path. If still fails — STOP and report.
- Designer/writer agents do NOT add content not requested in task brief
  (см. «No Extra Content Rule» секция). Improvements are REPORTED, not
  implemented.
```

#### 1.5 UPDATE «Anti-Patterns» table — add 4 rows

Добавить:
```markdown
| Designer adds content not in task brief | Producer agents REPORT improvements, not apply |
| Critics rename terms post-chapter-approval | Glossary lock — critics flag, do not propose rename |
| USER GATE without orchestrator pre-review | Pre-USER-GATE walkthrough mandatory (see protocol) |
| Snapshots committed to repo | Gitignore all snapshots, derive on demand |
```

---

### 2. `.claude/agents/presentation-designer.md`

**Current state:** 254 lines, 12 sections (палитра, Visual Motif, типографика, footer-tax, anti-patterns, toolset, workflow, per-slide recipes, output, что не делаешь). **Heaviest changes** — 8 new sections + 2 updates.

#### 2.1 ADD section «Schema Readability Checklist» — после «ANTI-PATTERNS»

Дословно (полный текст для вставки):
```markdown
## Schema Readability Checklist (ENFORCED, per slide-type)

Для каждого слайда с **custom schema** (non-cover, non-text-only) — пройти
per-subtype checklist ДО final accept. Если хотя бы один пункт не выполнен —
redo.

### Subtype: Matrix / Quadrant (2×2)
- [ ] Axis labels INSIDE quadrant (не за пределами bounding box).
- [ ] Axis-direction-of-scale обозначен стрелкой ИЛИ explicit «больше →».
- [ ] Marker direction-of-scale соответствует intuitive direction
      (например, «лучшее» = upper-right; не нужно объяснять зрителю).
- [ ] Точки в углах не overflow за грани quadrant.
- [ ] Font ≥12pt для axis labels, ≥14pt для cell content.
- [ ] Max 2 строки текста в каждой ячейке.
- [ ] Единый язык axis + cell content (RU only, не mix RU+EN).

### Subtype: Timeline (chronological)
- [ ] Events single-line через em-dash («2017 — Transformer paper»).
- [ ] Year labels не пересекают band borders/separators.
- [ ] Max 3 события per band (если >3 — компактнее или split на 2 timeline).
- [ ] Pivot year (главное событие) ≥2× размер шрифта остальных.
- [ ] Direction of time (left→right) explicit стрелкой ИЛИ через background gradient.
- [ ] Если timeline — основной визуал, занимать ≥60% slide width.

### Subtype: Layered (architectural levels)
- [ ] Common bottom edge (layers выровнены по нижней грани, НЕ centred).
- [ ] Component labels per layer (не «4 пустые концентрические рамки»).
- [ ] Max 4 уровня (если >4 — split или collapse adjacent).
- [ ] Visual hierarchy: deepest layer = largest, top = smallest (или inverse).
- [ ] Inter-layer connectors (стрелки depend_on / inherits) если architectural.

### Subtype: Cycle / Loop (process repetition)
- [ ] Start/end visible (явная entry point — gold dot или label «start»).
- [ ] Arrow direction obvious (clockwise default, counter-clockwise — explicit
      label).
- [ ] Max 6 шагов OR компактная форма (e.g. «User ↔ Model» 2-actor dialog).
- [ ] Если 6+ шагов — переходить на pipeline subtype или split на 2 cycle.
- [ ] Avoid centering «LOOP» badge — обычно decoration без semantic value.
- [ ] User/actor icon представлен (не только abstract boxes).

### Subtype: Pipeline (sequential transformations)
- [ ] Use `MSO_SHAPE.RIGHT_ARROW` shapes для arrows (не `filled_rect+rotated_triangle` гибрид).
- [ ] Unified language sub-labels (не mix «вход» / «output» / «результат»).
- [ ] Max 5 stages (если >5 — split на 2 pipeline).
- [ ] Each stage label ≤3 слов.
- [ ] Output of stage N visually connected to input of stage N+1
      (overlap или explicit connector).

### Subtype: Comparison (2 columns)
- [ ] Identical structure в обеих колонках (parallel layout).
- [ ] Identical row count + identical row headers.
- [ ] Visual tie-break: один маркер (gold border / icon) на «winner»,
      если comparison имеет lean.
- [ ] Equal column widths.

### Subtype: Architecture (component map)
- [ ] Components grouped by tier (frontend / backend / data).
- [ ] Connections labeled (не abstract lines).
- [ ] Boxes уровень consistent — не mix tiny с huge.
- [ ] Если architecture — основной визуал, occupy ≥70% canvas.
```

#### 2.2 ADD section «5-Second Test (final accept gate)» — после Schema Readability Checklist

Дословно:
```markdown
## 5-Second Test (final accept gate, ENFORCED)

Перед declaring slide done — выполни 5-Second Test:

1. Render финальный PNG.
2. Read PNG через Claude vision.
3. **Спроси себя:** "If I show this to студент с 5-го ряда на проекторе, did
   they understand the main message in 5 seconds?"
4. **If NO** — redo. Что мешает: too much text, schema требует чтения labels,
   gold highlight не на главном, hierarchy unclear, etc.
5. **If YES** — продолжай к следующему слайду.

**Counterexamples (provoke critical eye):**
- Если main number прячется среди других чисел → fail.
- Если схема требует чтения axis labels чтобы понять что показано → fail.
- Если 4 одинаковых блока без визуальной differentiation → fail.
- Если для понимания нужно прочитать ≥2 предложения → fail (assertion title
  должен передать main message).

5-Second Test НЕ заменяет 3 minimum visual loop iterations — он применяется
после iter ≥3 как final accept gate.
```

#### 2.3 ADD section «No Extra Content Rule» — после «5-Second Test»

Дословно:
```markdown
## No Extra Content Rule (ENFORCED)

Делай только то, что в task brief. **Не добавляй ничего «полезного»**, что
brief не запросил.

**8 forbidden additions:**
1. Slide subtitle, не запрошенный в brief.
2. Navigation markers («вы здесь», «продолжаем», «следующий раздел»).
3. Тайминг видимый студенту на слайде.
4. «Лектору» секции в speaker notes (lectorские cues → speech.md).
5. Decorative SVG/icons без semantic role.
6. Color-only highlight + text marker redundancy.
7. Slide deletion/addition без user request (s14-deletion case — paraphrasing
   ≠ duplicate, asking before removing).
8. Cross-slide bridge text не запрошенный.

**Если видишь opportunity for improvement** — REPORT в final message
orchestrator'у:
```
PROPOSED ADDITION:
  slide: sNN
  what: «navigation marker showing position in lecture»
  reasoning: «students may lose orientation by minute 40»
  await_approval: yes
```

Не applyить без approval.
```

#### 2.4 ADD section «Cross-Slide Redundancy grep» — после «No Extra Content Rule»

Дословно:
```markdown
## Cross-Slide Redundancy Detection (pre-final scan)

Перед declaring deck done — run automated check на повторы между слайдами:

```bash
# 1. Extract assertions from all slides:
grep -h '^assertion:' library/lectures/lec-NN/slides/*.md > /tmp/assertions.txt

# 2. Extract first-line content from PNGs (через extract_slide_text MCP):
# (manual: prep list of all slide titles + main visual element)

# 3. Look for duplicates:
# - Identical chart на 2+ slides (e.g. bar chart на s04 + s17 в Лекции 1).
# - Same statistic cited 2+ times (e.g. «43% DeepSeek» на s04 + s17).
# - Same icon set (если 5 слайдов = 5 одинаковых icon-cards — скучно).
# - Same assertion phrasing (paraphrasing → consolidate or differentiate).
```

**If duplicate found:** consolidate (delete one, link to the other) ИЛИ
differentiate (one shows %, other shows absolute number).
```

#### 2.5 ADD section «Projector Readability Test» — после Cross-Slide Redundancy

Дословно:
```markdown
## Projector Readability Test (50% zoom check)

Студент с 5-го ряда видит slide ≈ 50% от full screen size. Тест:

1. Открыть финальный PNG.
2. Уменьшить до 50% (mentally OR through file viewer).
3. **Спросить:** «Главный message всё ещё читается?»
4. **If NO:**
   - Body text too small → ≥18pt minimum.
   - Sub-labels invisible → ≥14pt OR убрать вовсе.
   - Schema connectors invisible → thicker strokes (≥2pt).
   - Background pattern шумит → убрать или contrast.
5. **If YES** — accept.

**Hard minimums (16:9 13.33×7.5"):**
- Title / assertion: ≥24pt (28pt preferred).
- Body / paragraph: ≥18pt (16pt только если 2-row max).
- Footer / source: ≥12pt.
- Chart axis labels: ≥14pt.
- Connector strokes: ≥2pt.
- Icon size: ≥48px (96px для main visuals).
```

#### 2.6 ADD section «Iconography Discipline» — после «Projector Readability»

Дословно:
```markdown
## Iconography Discipline (ENFORCED)

Иконки — **semantic role**, не decoration. Правила:

1. **Один icon set per deck** (Lucide ИЛИ Phosphor ИЛИ Heroicons — не mix).
   Logos AI-сервисов через LobeHub — это OTHER set, OK to coexist.
2. **Recolor в палитру** (`#065A82` primary OR `#1C7293` secondary OR `#028090` teal).
   Никаких black/grey без recolor.
3. **Размер consistency:** 96px для main visuals, 48px для inline,
   24px для chart-bar prefixes.
4. **Semantic role обязателен:**
   - Icon `camera` для slide про vision-AI — OK.
   - Icon `lightbulb` для slide «вот идея» — bad (decoration).
   - Icon `arrow-right` без destination — bad (decoration).
5. **Maximum 4 distinct icons per slide.** 6+ icons = visual noise.
6. **No emoji-style icons** (smiley faces, party poppers) в educational decks.
```

#### 2.7 ADD section «Visual Mass Balance» — после «Iconography Discipline»

Дословно:
```markdown
## Visual Mass Balance (ENFORCED)

Слайд = 2-column ИЛИ 3-region layout. **Mass balance** = total «visual weight»
левой и правой половины roughly equal.

**Visual weight rules:**
- Большой dark block weighs больше, чем small light block.
- Image weighs больше, чем text того же размера.
- Saturated color weighs больше, чем muted.

**Тест:**
1. Squint at slide PNG (mentally blur).
2. Если одна половина «тянет вниз/в сторону» — rebalance.
3. **Fixes:**
   - Move dominant element ближе к centre.
   - Add counter-weight (icon, callout, secondary visual) на пустую сторону.
   - Resize visual чтобы match text-block visual mass.
4. **Counter-example:** s11 v3 round 3 #9 — «квадраты не центрировать, по
   нижней границе» — user feedback ровно про visual mass, центрирование
   создавало плавающее ощущение.

**Layout templates by mass:**
- **Asymmetric 60/40:** main visual 60%, text 40% — visual weight roughly 50/50.
- **Symmetric 50/50:** equal columns, parallel structure (use для comparison).
- **Hero 70/30:** dominant single element (chart, illustration), text 30%.
- **Tile 33/33/33 (3 columns):** equal mass per column, useful для 3-step process.
```

#### 2.8 ADD section «Visual Loop Iteration Cap» — UPDATE existing «Workflow per slide»

В конце текущей секции «Workflow per slide» добавить:
```markdown
## Visual Loop Iteration Cap (ENFORCED)

**Hard cap: 7 iterations per slide.** Если на 7-й итерации schema всё ещё не
работает — STOP and escalate.

**Escalation procedure:**
1. Save current PNG + iter-7-blocked.png.
2. Write to orchestrator:
   ```
   ESCALATION:
     slide: sNN
     iterations_attempted: 7
     approaches_tried: [list of N approaches]
     remaining_issues: [what doesn't work]
     proposed_alternatives:
       - simplify schema (move detail to chapter)
       - replace схема picture (illustration вместо diagram)
       - split slide на 2
       - delete slide entirely (if relevance unclear)
     await_decision: yes
   ```
3. Не повторять iteration #8 без orchestrator/user input.

**Why:** Beyond iter 7, marginal gain falls к 0; продолжение = sink cost
fallacy. Reflection данные: s11/s13/s16/s21 потребовали по 5+ iter, и user в
итоге всё равно отверг — иногда concept нуждается в redesign, не в polish.
```

#### 2.9 ADD section «Designer Brief Strict Format» — после «Toolset»

Дословно:
```markdown
## Designer Brief — Strict Format

Когда orchestrator спавнит designer'а с list правок (Fix iteration), brief MUST
быть в **explicit YAML format**:

```yaml
modify:
  - s07: change timeline events from 12 to 9 (remove 2024-Llama, 2024-MCP)
  - s09: replace Llama-3 logo with OpenClaw, MCP с Kimi K2.5
  - s12: добавить иконки в каждой ячейке matrix (`camera`, `cpu`, `database`, `users`)

leave_untouched: [s01-s06, s08, s10, s11, s13-s28, s30-s33]

forbidden_additions: [subtitle, navigation marker, лектору section,
                      decorative icons без semantic role,
                      cross-slide bridge text]

acceptance_criteria:
  - all modified slides pass 5-Second Test
  - no new content added beyond modify list
  - no slides deleted
  - WPM in speaker notes ≤95
```

**Designer rule:** любое отклонение от modify-list (e.g. «попутно поправил s10
тоже») = P1 deviation. Report deviation to orchestrator перед apply.

**Parallel designer spawns:** если spawn 5 designers одновременно —
**non-overlapping slide ownership**. Each designer brief MUST contain
explicit `leave_untouched: [list]`. Orchestrator validates non-overlap before
spawn (skill `/spawn-designers`).
```

#### 2.10 UPDATE «Speaker notes» mention в section §s05a и других — make explicit contract

Заменить любое упоминание `Speaker notes — что говорит преподаватель (1-3 абзаца)` на:

```markdown
### Speaker notes — STRICT CONTRACT

**Format (per slide):**
- **Length:** 150-300 слов (target ~200).
- **Type:** READABLE STUDENT TEXT для self-study (читает студент через 2 недели,
  без преподавателя).
- **Source:** derived from chapter §X (primary) + speech [sNN] (secondary).
- **Tone:** book-style, не разговорный (отличается от speech.md).

**FORBIDDEN в notes:**
- Layout descriptions («слева donut, справа bar») — это для designer, не student.
- Director's cues («[пауза]», «[поднять руку]») — это speech.md.
- Лекторские заметки «помни упомянуть X» — это speech.md.
- Тайминг («3 мин на этот слайд») — это speech.md.

**DoD (independent от reader-simulator):**
- Word count в [150, 300] range (auto-check).
- No phrases starting with «Лектор:», «Лектору:», «Note to self:».
- No phrases с «[пауза]», «[слайд]», «[интерактив]».
- Reader-simulator mode=rendered: ≥30/N self-contained для прохода.
- Sample 3 случайных слайдов проверены человеком (orchestrator pre-USER-GATE).
```

---

### 3. `.claude/agents/book-editor.md`

**Current state:** 130 lines, focuses на chapter длиной 8-12k, structure, anti-patterns.

#### 3.1 ADD section «Speaker Notes Hand-Off» — после «Anti-patterns»

Дословно:
```markdown
## Speaker Notes Hand-Off (для downstream slides)

Когда пишешь chapter, добавляй marker **`[for-slide-sNN]`** в начале параграфа,
если он будет основой для speaker notes конкретного слайда.

Example:
```markdown
### §3.6 Приложение-робот

[for-slide-s14]
Программа, которая выполняет последовательность действий без AI, называется
«приложение-робот». Это не AI — это автоматизация. Например...
```

Это позволяет presentation-designer'у:
1. Найти исходный chapter material для notes (`grep '\[for-slide-s14\]' chapter.md`).
2. Адаптировать в 150-300 слов notes (compress, не paraphrase).
3. Сохранить terminology consistency (используя exact form из chapter).
```

#### 3.2 ADD section «Cross-reference to Course Structure» — после «Speaker Notes Hand-Off»

Дословно:
```markdown
## Cross-Reference to Course Structure (ENFORCED)

Перед написанием footnote типа «не является целью нашего курса» / «эту тему
покроем в Лекции X» — **обязательно** проверить:

1. Read `catalog/manifests/lectures.yaml` для course-wide LO mapping.
2. Read `00-course/программа.md` (Drive doc, через workspace-mcp) для
   actual lecture topics.
3. Verify claim не противоречит реальной программе.

**Counterexample (из Л1):** chapter v3 §1.4 footnote «не является целью нашего
курса» (про architecture topics) — противоречил Лекции 2 «Как работают
современные большие модели», которая явно про architecture.

Если не уверен — пометь `[CROSS-REF-VERIFY: lecture program]` для fact-checker.
```

#### 3.3 ADD section «Mark Unverified Specifics» — UPDATE existing anti-pattern «Не выдумывать факты»

Заменить current строку на:
```markdown
- ❌ **Не выдумывать факты** — если не уверен в цифре/дате, пометь
  `[FACT-CHECK: source needed]` для fact-checker.
- ❌ **Не давать specific numbers без source** (e.g. «20+ человек / 3 месяца»
  про Mistral) — даже если plausible, без verifiable source = `[FACT-CHECK]`.
- ❌ **Не делать claims про tools/benchmarks с числами** без attached
  «as of {date}» tag (e.g. «ARC-AGI лучший результат — 37.6%» становится
  устаревшим за дни). Каждое такое claim → `[FRESHNESS-CHECK: monthly cadence]`.
```

#### 3.4 ADD section «Cascade-of-Changes Tracking» — после «Workflow / Revision»

Дословно:
```markdown
## Cascade-of-Changes Tracking (ENFORCED при revisions)

Когда orchestrator/user просит изменение в chapter — track downstream impact:

1. Read changes request.
2. **Before applying** — list slides + speech sections, которые могут быть
   affected (через grep на ключевые phrases).
3. Apply chapter changes.
4. **After applying** — output `chapter-changes-vN.md` со структурой:
   ```markdown
   # Chapter changes vN
   ## Applied:
   - §3.6: переименовали «Приложение-автоматизация» → «Приложение-робот»
   ## Downstream impact (orchestrator should trigger):
   - slides: s14 (мentions «Приложение-автоматизация» 3 раза)
   - speech: [s14 · 4 мин], [s15 · 2 мин]
   - glossary.yaml: update canonical form
   ```
5. Orchestrator использует impact list для триггеринга consistency-checker
   + presentation-designer fix.
```

---

### 4. `.claude/agents/speech-writer.md`

**Current state:** 142 lines, sections — структура, стиль, content, anti-patterns, workflow.

#### 4.1 ADD section «WPM Hard Rule» — после «Anti-patterns»

Дословно:
```markdown
## WPM Hard Rule (ENFORCED)

**Любой speech fragment с WPM > 95 = P0, не submit.**

WPM (words per minute) calculation:
```
fragment_wpm = word_count / duration_min
```

DoD example:
- `[s07 · 3 мин]` имеет 285 слов → 95 WPM ✓
- `[s07 · 3 мин]` имеет 320 слов → 107 WPM ✗ (P0 — refuse output)

**Если fragment превышает 95 WPM:**
1. **Trim content** — удалить filler phrases, упростить предложения.
2. **Split slide** — если content реально не помещается в выделенный duration,
   request slide split (e.g. s19 split на s19+s19a в Л1).
3. **Increase duration** — если slide critical, request orchestrator увеличить
   duration_min для этого слайда (consult deck.yaml).

**Pre-submit check:** для каждого `[sNN · X мин]` fragment — count words,
verify ≤ 95 × X. Если хотя бы один fragment fails — STOP, fix.

**Counterexample (из Л1 v3.2):** s07 / s09 / s17 finalized с 102-107 WPM,
прошли как «8 of 10 ≤97 acceptable». Это violation DoD, не должно повториться.
```

#### 4.2 ADD section «Inclusive Language Distribution Check» — после WPM Hard Rule

Дословно:
```markdown
## «Мы с вами» Distribution Check

`Inclusive language` — «мы с вами», «давайте посмотрим», «нам важно понимать».
**Distribution check:** каждый 2-3-минутный fragment должен иметь хотя бы 1
inclusive marker. Не «мы с вами» × 5 в первом параграфе и 0 в остальных.

Pre-submit check:
```bash
# Для каждого section, count inclusive markers:
grep -c '(мы с вами|давайте|нам важно)' speech.md
```

Если средняя plotность < 1 marker / 200 слов → revisit, raspraviy более ровно.
```

#### 4.3 ADD section «Pre-Flight Sync Rule» — после «Workflow / Revision»

Дословно:
```markdown
## Pre-Flight Sync Rule (auto-regenerate from deck.yaml)

`Подготовка перед лекцией` section в speech.md (preflight checklist for
lecturer) — MUST sync с current deck.yaml автоматически.

**Procedure (run at end of each speech revision):**
1. Read `deck.yaml` for current slides list + interaction markers.
2. For each slide с `interaction:` поле — generate preflight item.
3. For each `live_demo` тип — generate backup screenshot reminder.
4. **Detect orphan references:** any `[sNN ...]` mention в preflight для слайда
   которого нет в current deck.yaml = orphan, REMOVE.

**Counterexample (из Л1 v3.x):** speech v3 имел `[s26 pre-flight для ARC-AGI]`
блок после deletion s26 в v3.1. consistency-checker поймал как P0. Should be
auto-prevented через sync rule.
```

#### 4.4 ADD section «Англицизм Cleanup Pass» — после «Pre-Flight Sync Rule»

Дословно:
```markdown
## Англицизм Cleanup Pass (ENFORCED, after first draft)

Speech tends to drift к англицизмам, даже если chapter clean. Run explicit pass:

```bash
# Forbidden anglicisms list (per-lecture, extend as needed):
ANGLO_LIST="стейкс|фоллбек|пайплайн|кейс|инсайт|workflow|edge case|фит|релиз|деплой|фича|митап"
grep -E "$ANGLO_LIST" speech.md
```

Replace with native:
| Англицизм | Replacement |
|---|---|
| стейкс | ставки |
| фоллбек | запасной вариант |
| пайплайн | конвейер / последовательность |
| кейс | случай / пример |
| инсайт | вывод / находка |
| workflow | процесс работы |
| edge case | граничный случай |
| фит | соответствие |

**Per-lecture extension:** at start, read chapter.md tone-rules section, extract
forbidden anglicisms list, add к above. Sync с consistency-checker glossary.
```

---

### 5. `.claude/agents/methodology-critic.md`

**Current state:** 119 lines, universal/chapter/plan/slides-specific checklists.

#### 5.1 ADD subsection «Curriculum Relevance Check» — внутри «Chapter-specific» И «Slides-specific»

Дословно (для slides-specific section):
```markdown
#### Curriculum Relevance Check (per slide AND per chapter section)

For each slide / chapter section — answer:
**«Зачем студенту лекции N (introductory / intermediate / advanced) этот концепт?»**

**Lecture-level mapping** (`catalog/manifests/lectures.yaml`):
- Lectures 1-3: introductory.
- Lectures 4-12: intermediate.
- Lectures 13-17: advanced.

**Decision matrix (Bloom level × lecture level):**

| Bloom level | introductory (L1-3) | intermediate (L4-12) | advanced (L13-17) |
|---|---|---|---|
| Remember / Understand | KEEP | KEEP | KEEP (if foundational) |
| Apply | REVIEW (depends на context) | KEEP | KEEP |
| Analyze | RECOMMEND DELETE / DEFER | REVIEW | KEEP |
| Evaluate / Create | RECOMMEND DELETE / DEFER | RECOMMEND DELETE / DEFER | KEEP |

**Counterexamples (from L1 v3):**
- Pearl 3 уровня causality (Evaluate level) в Лекции 1 (introductory) →
  RECOMMEND DELETE (user removed это в round 1 #18).
- ARC-AGI economics (Analyze level) в Лекции 1 → RECOMMEND DELETE.
- Copilot worked example с 4 axes (Apply level + complex) → REVIEW; user
  упростил до 2 осей в round 1 #4.

**Output severity:** если RECOMMEND DELETE — severity P1 «Curriculum mismatch».
```

#### 5.2 ADD subsection «Term Canonical-Validity Check» — внутри «Universal»

Дословно:
```markdown
#### Term Canonical-Validity Check

For each new term introduced — verify it is **canonical в литературе**, не
редакторский «clean phrasing».

**Insider phrasing (RED FLAG patterns):**
- «рабочее определение X» — означает «я придумал термин для удобства».
- «прикладное X» — adjective добавлен для disambiguation, но не каноничный.
- «X в режиме Y» — periphrasis вместо canonical form.

**Verification:**
1. Search Google Scholar / Wikipedia: «{term} definition».
2. Verify form matches academic literature OR explicit dictionary.
3. If only matches custom usage — flag P1 «Insider phrasing — use canonical {alternative}».

**Counterexample (из Л1):** chapter v2 §1.1 «рабочее определение AI» — user:
«что за рабочее определение ты выдумал?». Каноничные: «narrow AI» (Bostrom),
«weak AI» (Searle 1980), «artificial general intelligence (AGI)» (Goertzel).
```

#### 5.3 ADD subsection «Tools/Benchmark Freshness Check» — внутри «Universal»

Дословно:
```markdown
#### Tools / Benchmark Freshness Check (для AI-domain content)

Каждое claim про «AI tool X» / «benchmark Y» / «model Z» — verify temporal
relevance.

**Per-claim required metadata:**
- Date of source.
- Typical refresh cadence для этого данного:
  - AI benchmark scores (ARC-AGI, MMLU, HumanEval, agentic-bench): **weekly**.
  - LLM market share / usage stats: **quarterly**.
  - Tool feature lists: **monthly**.
  - Conceptual claims (architecture, theory): **yearly+**.
- «Verify on day-of-lecture»: yes/no.

**Decision matrix:**
- Refresh cadence < 1 month + lecture date > source date by > 1 month → P0
  «Likely stale, verify».
- Refresh cadence 1-3 months + lecture date > source date by > 3 months → P1.
- Refresh cadence yearly+ → P2 cite year.

**Counterexample (из Л1):** ARC-AGI 37.6% (chapter draft date) устарел до
68.8% (Opus 4.6) и 85% (GPT-5.5) за 2 дня к user review. Llama-3 / MCP как
«свежие примеры» — устарели relative to OpenClaw / Kimi K2.5.

**Output:** generate `freshness-report.md` в qa-reports/{date}/ со списком
claims + cadence + verify-on date.
```

#### 5.4 ADD subsection «Designer-Added Content Audit» — внутри «Slides-specific»

Дословно:
```markdown
#### Designer-Added Content Audit

Compare current `slides/*.md` против previous version (git diff) — flag любые
additions, которые не correspond к user-requested changes.

**Forbidden additions list** (8 items, see CLAUDE.md «No Extra Content Rule»):
1. Subtitle, не запрошенный.
2. Navigation markers.
3. Тайминг видимый студенту.
4. «Лектору» секции в notes.
5. Decorative SVG/icons без semantic role.
6. Color-only highlight + text marker redundancy.
7. Designer-driven slide deletion/addition.
8. Cross-slide bridge text не запрошенный.

**Procedure:**
1. `git diff HEAD~1 library/lectures/lec-NN/slides/` (или vs last critic-approved version).
2. Categorize each addition:
   - REQUESTED (matches user/orchestrator brief) — OK.
   - DESIGNER-INITIATIVE (not in brief) — flag P1 «Designer-added content».
3. Output list в methodology-critic report.
```

#### 5.5 UPDATE «Output / Severity» section — новый verdict scale

Заменить current «Severity» section на:
```markdown
## Output Verdict (ENFORCED scale)

**Verdict line MUST be first line of report:**

```
VERDICT: REJECT | REVISE | APPROVE-WITH-POLISH | APPROVE-CLEAN
```

| Verdict | When |
|---|---|
| REJECT | Any P0 (методически непригоден) |
| REVISE | 5+ P1 OR critical curriculum mismatch — must fix before show |
| APPROVE-WITH-POLISH | ≤4 P1 — show-able с known caveats |
| APPROVE-CLEAN | 0 P1 (все только P2 или meet hold) |

**Counter check (mandatory):** если ты wrote ≥5 P1 issues но verdict =
APPROVE-WITH-POLISH — STOP, change verdict to REVISE.

**Severity definitions:**
- **P0** — артефакт методически непригоден (термин не определён, LO не покрыт,
  концепт-перескок, cognitive overload, curriculum mismatch для introductory).
- **P1** — заметно вредит обучению (нет self-check, тон неуважителен, тезис
  без доказательства, terminology drift, designer-added content).
- **P2** — мелочи (порядок терминов, мелкая нестыковка).
```

---

### 6. `.claude/agents/presentation-critic.md`

**Current state:** 87 lines, методика + визуал + нарратив checklists.

#### 6.1 ADD subsection «Schema Readability Evaluation» — внутри «Визуал»

Дословно:
```markdown
- [ ] **Schema readability per subtype** (см. presentation-designer.md «Schema
      Readability Checklist»). Для каждого слайда с custom schema — verify все
      pункты subtype-specific checklist (matrix/quadrant/timeline/layered/cycle/
      pipeline/comparison/architecture).
- [ ] **5-Second Test passes** — would student с 5-го ряда понять main message
      за 5 sec? If no — flag P1.
- [ ] **Projector Readability (50% zoom)** — body text readable, sub-labels
      visible, connectors thick enough.
```

#### 6.2 ADD subsection «Cross-Slide Redundancy Detection» — после «Визуал»

Дословно:
```markdown
### Cross-Slide Redundancy Detection

Run grep на повторы между слайдами:
- Same chart type + same data на 2+ слайдах (e.g. bar chart на s04 + s17 в Л1).
- Same statistic cited 2+ times без differentiation.
- Same icon set repeated identically.
- Identical / paraphrased assertions.

**If found:** flag P1 «Cross-slide redundancy: sNN duplicates sMM —
consolidate or differentiate».
```

#### 6.3 ADD subsection «Designer-Added Extras Detection» — после «Cross-Slide Redundancy»

Дословно:
```markdown
### Designer-Added Extras Detection

Compare current snapshots vs previous version. Flag any visual additions не из
user brief (см. «No Extra Content Rule» в CLAUDE.md).

**Manual check on each slide:**
- Есть ли subtitle, который не упоминался в task brief?
- Есть ли «вы здесь» / тайминг markers?
- Есть ли «Лектору» секции в speaker notes?
- Есть ли decorative icons без semantic role?
- Был ли удалён слайд без user request (compare deck.yaml vs previous)?

**Output:** flag each as P1 «Designer-added extras».
```

#### 6.4 UPDATE «Severity» section — новый verdict scale (mirror methodology-critic)

Заменить current «Severity» section на the 4-level scale (see §5.5 above).

#### 6.5 ADD section «Save Report Mandate» — в конце файла

Дословно:
```markdown
## Save Report Mandate (ENFORCED)

Before declaring done — MUST save report as file. Path enforced в spawn prompt.

**Procedure:**
1. Write `library/lectures/lec-NN/qa-reports/{date}-vN/presentation-critic.md`.
2. If Write fails (Permission denied / path not exist) — Bash to verify path
   exists / mkdir if needed.
3. Retry Write.
4. If still fails — STOP, report to orchestrator with full content в final message.
```

---

### 7. `.claude/agents/consistency-checker.md`

**Current state:** 113 lines, 7 check categories, cross-artifact matrix output.

#### 7.1 ADD section «Terminology Drift Sub-Check» — новый mode

Дословно:
```markdown
## Mode: terminology-only (lightweight, runs at every USER GATE)

When orchestrator passes `mode=terminology-only`, run **only** terminology
checks (skip coverage / sequence / etc.). Quick scan suitable для pre-USER-GATE.

**Procedure:**
1. Read `library/lectures/lec-NN/glossary.yaml` (если exists).
2. For each canonical term + aliases_forbidden:
   ```bash
   grep -n "$forbidden_form" library/lectures/lec-NN/{chapter.md,slides/*.md,speech.md}
   ```
3. For each term без glossary entry — check if appears в 2+ форм across
   artifacts (auto-detect drift).

**Output (lightweight):**
```markdown
# Terminology Drift Report — Лекция N — {date} (mode=terminology-only)

VERDICT: REJECT | REVISE | APPROVE-WITH-POLISH | APPROVE-CLEAN

## Drift detected:
- Term «Приложение-робот» has 3 forms across artifacts:
  - chapter.md: «Приложение-робот» × 5
  - slides/s14.md: «Приложение-автоматизация» × 2
  - speech.md: «Приложение в режиме автоматизации» × 1
  - **Recommendation:** sync all к canonical from glossary («Приложение-робот»).

## Untracked terms (not в glossary, но appears 2+ форм):
- ...
```
```

#### 7.2 UPDATE «When to run» — extend phases

Заменить current top-of-file phase mention to:
```markdown
**REQUIRED READING:** Before any work, read:
1. `tools/lecture-production/README.md` — pipeline (твоя роль = Phase 4, 7, 10
   для full mode; Phase 4.5, 7.5, 10.5 для terminology-only mode).
2. ...
```

И добавить phase note:
```markdown
## Phase mapping

- **Phase 4 (after chapter draft):** mode=`chapter-only` — verify chapter terms
  vs research notes, generate initial glossary.
- **Phase 7 (after slides finalized):** mode=`chapter+slides` — verify slides
  align с chapter, terminology, references.
- **Phase 10 (after speech draft):** mode=`full` — все 3 артефакта.
- **Pre-USER-GATE (любой):** mode=`terminology-only` — quick drift scan.
```

#### 7.3 ADD section «Glossary Lock Enforcement» — в конец файла

Дословно:
```markdown
## Glossary Lock Enforcement (ENFORCED)

После Phase 4 USER GATE 1 (chapter approved) — orchestrator generates
`library/lectures/lec-NN/glossary.yaml`.

**Critic rule:** в downstream phases (7, 10), консистенси-checker MAY:
- Flag inconsistency: «term X has form Y в slide, form Z в chapter».

**Critic rule:** консистенси-checker MAY NOT:
- Suggest rename term без USER approval.
- Apply rename automatically.
- Recommend changes to glossary canonical form (только REPORT).

Если думает что glossary canonical неоптимальна — output rename proposal в
report «PROPOSED GLOSSARY UPDATE: ... — needs user approval».
```

---

### 8. `.claude/agents/fact-checker.md`

**Current state:** 125 lines, 6 check categories, severity P0/P1/P2.

#### 8.1 ADD subsection «Curriculum / Drive Sync Check» — внутри «Что проверяешь»

Дословно:
```markdown
### 7. Curriculum / Drive Sync (для лекций с real curriculum data)

Если артефакт содержит claims про course structure (modules count, lecture
sequence, instructor info, course duration) — verify против Drive doc:

**Procedure:**
1. Read `00-course/программа.md` (Drive doc) через workspace-mcp:
   ```
   mcp__workspace-mcp__get_doc_as_markdown
     user_google_email=kzlevko@gmail.com
     document_id={course program doc ID}
   ```
2. Read `catalog/manifests/lectures.yaml` для lecture mapping.
3. Compare claims:
   - «4 блока курса» vs реальные «3 модуля × 17 лекций».
   - «Лекция 6 покрывает X» vs actual lecture 6 topic.
   - Instructor name vs official.
4. **If mismatch:** P0 «Curriculum hallucination — verify against Drive».

**Counterexample (из Л1):** s27 (later s30) roadmap в chapter показывала
«4 блока (Основы / Инструменты / Интеграция / Границы)» — реально 3 модуля
× 17 лекций. User поймал в round 1 #20, не fact-checker.
```

#### 8.2 ADD subsection «Tools/Benchmark Freshness» — внутри «Что проверяешь»

Дословно (mirror methodology-critic, но focused на verification):
```markdown
### 8. Tools / Benchmark Freshness (для AI-domain content)

Each AI-tool / benchmark / model claim — record metadata:

```
Fact: «{exact quote}»
Number: {%, score, count}
Source: {URL, doc, paper}
Source date: {YYYY-MM-DD}
Lecture date: {YYYY-MM-DD}
Refresh cadence: {weekly | monthly | quarterly | yearly+}
Days delta: {lecture - source}
Verify-on-day-of-lecture: {yes if cadence < 1 month AND days_delta > cadence}
Verdict: VERIFIED | NEEDS-REFRESH | UNVERIFIABLE
```

**Refresh cadences:**
- AI benchmark scores: weekly.
- LLM market shares: quarterly.
- Tool feature lists: monthly.
- Conceptual claims: yearly+.

**Output:** `freshness-report.md` в qa-reports/{date}/ со полным списком +
top-N items needing refresh on day of lecture.

**Counterexample (из Л1):** ARC-AGI 37.6% (source Apr 2026) → outdated by
30+ percentage points за 2 дня (Opus 4.6 = 68.8%, GPT-5.5 = 85%).
```

#### 8.3 ADD «Mandatory File Save» — в section «Tools»

Заменить current «Tools» section с добавлением:
```markdown
## Mandatory File Save (ENFORCED)

Before declaring done — MUST save report as file:
- Path: `library/lectures/lec-NN/qa-reports/{date}-vN/fact-checker.md`.
- If Write fails — Bash to verify path / mkdir, retry Write.
- If still fails — STOP, output full content in final message + flag
  orchestrator: «Save failed, content in chat, please save manually».

**Counterexample (из Л1 v3.x):** fact-checker не сохранил отчёт — content
embedded в SYNTHESIS только. Если orchestrator сессия закроется — отчёт
потерян. Should not happen again.
```

#### 8.4 UPDATE «Severity» — verdict scale

Mirror change to 4-level verdict scale (see §5.5).

---

### 9. `.claude/agents/student-simulator.md`

**Current state:** 76 lines, fictional студент ИУ6 perspective.

#### 9.1 ADD subsection «Schema Readability per Slide Perspective» — внутри «Чек-лист»

Дословно (добавить новый item к existing 6):
```markdown
7. **Схема читается?** Если на слайде есть схема (matrix/quadrant/timeline/
   cycle/etc.) — what do I take away за 5 сек? Если не понимаю — что мешает?
   - Названия осей за пределами схемы → «не понимаю что показано».
   - Стрелки направлены не intuitively → «не понимаю порядок».
   - Слишком много элементов → «глаза разбегаются».
   - Schema без user/actor → «где Я в этой схеме?»
```

#### 9.2 ADD subsection «Explicit Slides-to-Delete Recommendation» — внутри «Output»

Заменить или дополнить final output section:
```markdown
## Explicit «Slides to Delete» Recommendation (ENFORCED)

В Сводку добавить отдельную секцию:

```markdown
## Кандидаты на удаление (для introductory лекции)

- **sNN — {название}** — слишком абстрактно для 3-го курса, я отвлёкся.
  RECOMMEND DELETE для introductory лекции.
- **sMM — {название}** — повтор s04 другими словами.
  RECOMMEND CONSOLIDATE с s04.
```

Не лимитируй severity до P1 «boring». Если слайд для introductory лекции —
**RECOMMEND DELETE** explicit. Это не цензура — это «лектор может оценить и
решить».

**Counterexample (из Л1):** student-simulator называл s27 (4 спикера AGI) и
s28 (Pearl) «не идеально для зала» severity P1, но не RECOMMEND DELETE. User
позже удалил оба после долгого размышления — мог бы сэкономить раунд.
```

---

### 10. `.claude/agents/reader-simulator.md`

**Current state:** 102 lines, 2 режима (text-only + rendered).

#### 10.1 ADD subsection «Self-Containedness Threshold Escalation» — внутри «Output / Режим B»

Дополнить final output section:
```markdown
## Self-Containedness Absolute Threshold (ENFORCED, mode=rendered)

**Hard threshold:**
- ≥30/N slides self-contained = APPROVE-CLEAN.
- 25-29/N = APPROVE-WITH-POLISH (show-able, polishing recommended).
- 20-24/N = REVISE (notes need substantive rewrite).
- <20/N = REJECT (deck не работает для self-study).

**Не сравнивать с previous version «better than v2»** — это не критерий
absolute. Self-containedness — ABSOLUTE goal (lecture pересматривается через
2 недели для подготовки к РК).

**Если <30/N:** add к Сводка section «Structural Blocker Assessment»:
```markdown
## Structural Blockers (для slides не self-contained)

Of N self-contained-fail slides, classify:
- **Notes-fixes** (just expand notes ~150 words): sXX, sYY, sZZ.
- **Schema redesign** (visual itself broken without explanation): sAA, sBB.
- **Structural cuts** (slide reaily cannot be self-contained even with notes):
  sCC — RECOMMEND DELETE for self-study version.
```

This forces ясное decision per failed slide, не «28/34 = OK».
```

---

### 11. `tools/lecture-production/README.md`

**Current state:** 207 lines, 12 sections, 10-фазный pipeline + 3 USER GATEs.

#### 11.1 ADD section «Pre-USER-GATE Walkthrough» — после «3. Workflow» 

Дословно:
```markdown
## 3.1 Pre-USER-GATE Walkthrough (ENFORCED, перед каждым USER GATE)

Перед презентацией артефакта user'у на USER GATE — orchestrator (или
sub-orchestrator agent) MUST выполнить pre-review.

**Procedure (~15-30 минут wall-clock):**
1. **Visual scan all PNG snapshots** через Read tool.
2. **Read all speaker notes** as student-perspective.
3. **Read speech (if applicable)** as lecturer-perspective.
4. **Run automated checks:**
   - `grep -i 'лектору\|вы здесь\|субтитр'` — designer extras detection.
   - WPM check (для speech): for each `[sNN · X мин]`, count words ≤ 95X.
   - Cross-slide redundancy: titles + assertions duplicates.
   - Terminology drift: consistency-checker mode=terminology-only.
5. **List 10+ issues** found.
6. **Apply quick fixes** (P2 cosmetic) directly via subagent.
7. **Present to user** as: «I reviewed N artifacts, found K issues, fixed M,
   pending L because [reason]. Anything you'd add?»

**Hard rule:** «approve» = «orchestrator reviewed visually + critics approved»,
NOT «critics approved alone». NEVER USER GATE без explicit pre-review report.

**Skill option:** invoke `/pre-gate-review {phase}` (см. `.claude/skills/`).
Skill spawns pre-gate-reviewer subagent с pinned checklist + automated greps +
returns issue list для orchestrator review.
```

#### 11.2 ADD section «Cascade-of-Changes Tracking» — после Pre-USER-GATE Walkthrough

Дословно:
```markdown
## 3.2 Cascade-of-Changes Tracking (ENFORCED, при revisions)

Когда user/orchestrator request change в одном артефакте — track downstream impact:

**Procedure:**
1. **Read change request.**
2. **List affected artefacts** через grep (chapter ↔ slides ↔ speech).
3. **Apply primary change** через relevant producer (book-editor / designer /
   speech-writer).
4. **Producer outputs `*-changes-vN.md`** rationale + downstream impact list:
   ```markdown
   # Changes vN
   ## Applied:
   - Chapter §3.6: term «Приложение-автоматизация» → «Приложение-робот»
   ## Downstream impact (orchestrator should trigger):
   - slides/s14.md: 3 mentions требуют sync
   - speech.md: [s14 · 4 мин] mentions требуют sync
   - glossary.yaml: update canonical
   ```
5. **Orchestrator triggers** consistency-checker mode=terminology-only,
   plus presentation-designer/speech-writer fix iterations.
6. **Pre-USER-GATE walkthrough** verifies cascade complete.

**Counterexample (из Л1):** user round 1 #12 «ссылки на чек-лист сломаются» —
designer удалил чек-лист, но не sync ссылки в других слайдах (3 P1 потом).
```

#### 11.3 UPDATE Phase 7 — добавить consistency-checker

В section «3. Workflow» обновить Phase 7:
```markdown
│ Phase 7 — Slides QA                                             │
│ Agents (parallel): presentation-critic + student-simulator +    │
│                    reader-simulator mode=rendered +             │
│                    fact-checker (если данные на slides) +       │
│                    consistency-checker mode=chapter+slides       │
│ Output: 5 reports → SYNTHESIS                                   │
```

#### 11.4 ADD section «Speaker Notes Contract» — после «6. Размер artifacts»

Дословно:
```markdown
## 6.1 Speaker Notes Contract (ENFORCED)

Speaker notes per slide:
- **Length:** 150-300 слов (target ~200).
- **Type:** READABLE STUDENT TEXT для self-study.
- **Source:** derived from chapter §X (primary) + speech [sNN] (secondary).
- **Tone:** book-style, не разговорный (отличается от speech.md).

**FORBIDDEN в notes:**
- Layout descriptions («слева donut, справа bar»).
- Director's cues («[пауза]», «[поднять руку]»).
- Лекторские заметки.
- Тайминг.

**DoD (independent от reader-simulator):**
- Word count в [150, 300] range (auto-check).
- No phrases starting with «Лектор:», «Лектору:», «Note to self:».
- No phrases с «[пауза]», «[слайд]», «[интерактив]».
- Reader-simulator mode=rendered: ≥30/N self-contained.
- Sample 3 случайных слайдов проверены человеком (orchestrator pre-USER-GATE).
```

#### 11.5 ADD section «Curriculum-Level Metadata» — после «6.1 Speaker Notes Contract»

Дословно:
```markdown
## 6.2 Curriculum-Level Metadata

Each lecture in `catalog/manifests/lectures.yaml` MUST have:
```yaml
- id: lec-01
  title: "AI вокруг нас"
  curriculum_level: introductory  # introductory | intermediate | advanced
  module: 1
  ...
```

**Mapping:**
- Lectures 1-3: introductory.
- Lectures 4-12: intermediate.
- Lectures 13-17: advanced.

**Used by:** methodology-critic для «Curriculum Relevance Check» (см.
`.claude/agents/methodology-critic.md`).
```

#### 11.6 ADD section «Glossary Lock Phase 4.5» — в section «3. Workflow»

В workflow diagram добавить между Phase 4 и USER GATE 1:
```markdown
├─────────────────────────────────────────────────────────────────┤
│ Phase 4.5 — Glossary lock                                       │
│ Orchestrator generates library/lectures/lec-NN/glossary.yaml    │
│ from chapter.md (15-25 ключевых терминов).                       │
│ Used by all downstream agents (slides, speech, critics).         │
├─────────────────────────────────────────────────────────────────┤
│ ✋ USER GATE 1 — chapter approved                                │
```

#### 11.7 UPDATE «7. Anti-patterns» — add 4 new

Добавить:
```markdown
9. ❌ **USER GATE без orchestrator pre-review** — «critics approved» ≠
    «I (orchestrator) reviewed». Pre-USER-GATE walkthrough mandatory.
10. ❌ **Designer-added content** — producers do NOT add content not in brief.
11. ❌ **Critic-driven terminology rename без user approval** — glossary lock
     after chapter approval, critics flag, не propose rename.
12. ❌ **Snapshot bloat в repo** — gitignore all `**/snapshots/iter*.png` +
     `**/snapshots/fix*.png`, keep only финальные `sNN.png`.
```

---

### 12. `tools/presentation-build/README.md`

**Current state:** 266 lines, 12 sections, slide-types library, visual-loop, anti-patterns.

#### 12.1 ADD section «Schema Readability Acceptance Gate» — в section «§4 Slide-types library»

После описания slide-types добавить:
```markdown
### Schema Readability Acceptance Gate (ENFORCED)

Каждый слайд с **custom schema** (matrix/quadrant/layered/cycle/pipeline/
timeline/comparison/architecture) — pass per-subtype Schema Readability
Checklist (см. `.claude/agents/presentation-designer.md` § «Schema Readability
Checklist»).

**Acceptance procedure:**
1. Designer renders schema через Visual Loop (min 3 iter).
2. Designer self-checks per-subtype checklist.
3. Designer applies 5-Second Test (см. designer playbook).
4. Designer applies Projector Readability Test (50% zoom).
5. Only after all 4 pass — declare slide done.

**Critic verification:** presentation-critic re-runs Schema Readability +
5-Second Test для каждого custom-schema слайда.
```

#### 12.2 EXTEND «§4 Slide-types library» — добавить subtypes

К existing 8 types добавить расширения для schema-heavy слайдов:
```markdown
**Schema subtypes** (used within `assertion_visual` или standalone):

| Subtype | Pattern | Iter expectations |
|---|---|---|
| `matrix_2x2` | 2×2 grid с axes inside, marker в каждой ячейке | works first-try (2-3 iter) если labels внутри quadrant |
| `quadrant` | Same as matrix, но 4 регионa без grid | 2-3 iter typically |
| `timeline` | Horizontal/vertical chronology с events | 2-3 iter если ≤6 events; 4-5 iter если denser |
| `layered` | Architectural levels с component labels | 3-4 iter — common bottom edge tricky |
| `cycle` | Circular flow с start/end + arrows | needs 4-5 iter typically; consider compact dialog form for 2-actor |
| `pipeline` | Sequential stages с RIGHT_ARROW shapes | 2-3 iter если ≤5 stages |
| `comparison_2col` | Two parallel columns с identical structure | works first-try |
| `architecture` | Component map с tier groupings | 3-4 iter для clarity |

**Pattern: works first-try (1-2 iter):**
- comparison_2col, matrix_2x2 (если правильно подготовлен brief).

**Pattern: needs 2-3 iter:**
- pipeline, quadrant, timeline (если ≤6 events).

**Pattern: needs structural redesign (4+ iter):**
- cycle (особенно если >4 steps), layered (если >4 уровней), dense timeline,
  any custom architecture.

**Decision rule:** если subtype в pattern «needs structural redesign» — рассмотреть
upfront, можно ли упростить (cycle с 6+ step → 2-actor dialog; layered с
5+ уровней → split на 2 слайда).
```

#### 12.3 UPDATE «§9 Anti-patterns» — extend top-10 to top-35

Заменить current top-10 list на extended:
```markdown
## 9. Anti-patterns — top-35

**Original top-10:**
1-10 (см. existing).

**Visual-audit additions (16-35):**

11. ❌ **Schema acceptance без 5-Second Test** — если students не понимают
     за 5 сек, schema fails goal.
12. ❌ **Axis labels за пределами quadrant/matrix** — должны быть INSIDE
     или explicit «axis here» indicator.
13. ❌ **Layered diagram centred вместо common-bottom-edge** — visually
     плавающий, нет «foundation».
14. ❌ **Cycle с 6+ steps как vertical list** — не cycle, это linear flow с
     loop hint. Если действительно cycle — компактная dialog form.
15. ❌ **Pipeline с filled_rect + rotated_triangle вместо MSO_SHAPE.RIGHT_ARROW** —
     гибрид «выглядит сломанно».
16. ❌ **Custom-coined «рабочие термины»** на слайдах — use canonical из
     glossary.
17. ❌ **Designer-added subtitle** на cover slide без user request.
18. ❌ **«Лектору» секция в speaker notes** — cues for lecturer → speech.md,
     не student-facing notes.
19. ❌ **Тайминг видимый студенту** на слайде или в notes — для лектора
     только.
20. ❌ **«Вы здесь» / navigation markers** — duplicate of agenda + visual noise.
21. ❌ **Color-only highlight + text marker redundancy** — single mechanism
     per signal.
22. ❌ **Cross-slide content redundancy** (same chart на s04 + s17) —
     consolidate or differentiate.
23. ❌ **Designer-driven slide deletion без user request** — paraphrasing ≠
     duplicate, ask before remove.
24. ❌ **AI tools/benchmarks без freshness check** — данные устаревают за
     дни/недели.
25. ❌ **Self-acceptance без projector test (50% zoom)** — body text invisible
     с 5-го ряда.
26. ❌ **Mixed icon sets** (Lucide + Phosphor + Heroicons random) — pick one.
27. ❌ **Decorative icons без semantic role** — visual noise.
28. ❌ **6+ icons per slide** — visual noise, eye не знает где focus.
29. ❌ **Visual mass imbalance** — squint test fails, одна сторона тянет.
30. ❌ **Schema без user/actor presence** (когда контекст implies user) —
     «где Я в этой схеме?» — student question.
31. ❌ **Marker direction-of-scale не intuitive** (например quadrant с
     «лучшее» в bottom-left) — нужен explicit explainer.
32. ❌ **Dense timeline (12 events на 1 row)** — split на 2 timeline или
     condense.
33. ❌ **Schema text wraps mid-word** («перево / д») — fix через line-break
     или reduce text.
34. ❌ **Verdict APPROVE-WITH-MINOR с 5+ P1** — verdict scale violation.
35. ❌ **Visual loop > 7 iter без stop** — escalate; iter beyond 7 = sink cost.
```

#### 12.4 ADD section «§5.1 Pre-Design Wireframe» — в section «§5 Visual-loop workflow»

Перед current «1. PLAN — choose slide type» добавить:
```markdown
### §5.1 Pre-Design Wireframe (ENFORCED для custom schema)

Любой слайд с **custom schema** (matrix/quadrant/cycle/layered/pipeline/
timeline/architecture) — designer **сначала рисует ASCII или mermaid wireframe**,
orchestrator approves, **потом** PowerPoint MCP render.

**Procedure:**
1. Read task brief.
2. Choose subtype из `§4 slide-types library`.
3. **Sketch wireframe** в ASCII или mermaid (15 минут):
   ```
   Pre-design wireframe for s12:

   +------------------------------+
   | Title: Когда AI работает    |
   +------------------------------+
   | DA       | DA              |
   |  +-----+ |  +-----+        |
   |  |OK   | |  |OK + |        |  <- gold marker
   |  +-----+ |  +-----+        |
   |  Image  |  Vision           |
   +----------+------------------+
   | NET      | NET              |
   |  +-----+ |  +-----+        |
   |  |No   | |  |No   |        |
   |  +-----+ |  +-----+        |
   |  Music  |  Sentiment       |
   +----------+------------------+
   |     SUITABILITY -->          |   <- axis (правее = более suitable)
   +------------------------------+
   ```
4. Output wireframe в final message; await orchestrator approval.
5. Only after approval — proceed to Visual Loop step 1.

**Why:** реальные данные L1 v3 — s11/s13/s16/s21 потребовали по 5+ visual loop
iter, и user всё равно отверг. Pre-wireframe мог бы сэкономить 50%+ визуал.
```

#### 12.5 UPDATE «§5 Visual-loop workflow» — добавить iteration cap

В конце section добавить:
```markdown
### Visual Loop Iteration Cap (ENFORCED)

**Hard cap: 7 iterations per slide.**

If iter 7 не дал acceptable result:
1. Save current PNG + iter-7-blocked.png.
2. Write escalation:
   ```
   ESCALATION: slide sNN, 7 iter, что пробовал, что remains broken,
                4 alternatives (simplify/replace/split/delete).
   ```
3. Await orchestrator/user decision.

**Marginal-gain hypothesis:** beyond iter 7, marginal gain → 0; продолжение =
sink cost fallacy.
```

---

### 13. `notes/decisions.md`

**Current state:** 202 lines, current anti-patterns table has 15 items в section «2026-05-12 — Presentation pipeline».

#### 13.1 ADD new section «2026-05-13 — Lecture 1 v3 production lessons (20 anti-patterns 16-35)»

Add at end of file:
```markdown
## 2026-05-13 — Lecture 1 v3 production lessons

**Контекст:** day-long production Лекции 1 v3.x — chapter v3.1 (16k слов),
slides v3.2 (33 слайда), speech v3.1 (5.1k слов). Все 4 critic agents
APPROVE-WITH-MINOR. User вернулся с 23 + 8 + 19 = 62 substantive revisions
across 3 раундах. Reflections: REFLECTION.md (broad, 7 categories) +
REFLECTION-roast.md (15 missed failures) + REFLECTION-visual-audit.md
(visual specialist deep-dive).

**Implementation plan:** REFLECTION-CONSOLIDATED.md.

### Anti-patterns 16-35 (extension к pipeline catalog 1-15)

| # | Anti-pattern | Чем заменить | Источник |
|---|---|---|---|
| 16 | Designer-added content not in task brief (subtitle, navigation marker, тайминг) | Producer agents REPORT improvements, не apply | REFLECTION §2.4 + §3.1 Failure 2 |
| 17 | Layout descriptions в speaker notes («слева donut, справа bar») | Notes = readable student text 150-300 words derived from chapter+speech | REFLECTION §2.1 #1 + §5.1 |
| 18 | Color-only highlight + text marker (single signal duplicated) | Single mechanism per signal | REFLECTION §4.1 |
| 19 | Cross-slide content redundancy (bar chart на s04 + s17) | Consolidate or differentiate; pre-final grep | REFLECTION §2.3 #13 + §4.1 |
| 20 | AI tools/benchmarks без freshness check (Llama-3 «свежий», ARC-AGI 37.6%) | Per-claim freshness metadata + verify-on-day-of-lecture | REFLECTION §3.5 Failure 2 + §6 |
| 21 | Critic verdict APPROVE-WITH-MINOR при 5+ P1 | New verdict scale REJECT/REVISE/APPROVE-WITH-POLISH/APPROVE-CLEAN | REFLECTION §4.2 |
| 22 | USER GATE без orchestrator pre-review walkthrough | Pre-USER-GATE protocol mandatory | REFLECTION §7.4 + Top-5 P0-2 |
| 23 | Schema acceptance без 5-Second Test | 5-Second Test as final accept gate | VISUAL-AUDIT |
| 24 | Axis labels outside quadrant / matrix | Labels INSIDE quadrant с direction-of-scale | VISUAL-AUDIT + REFLECTION §3.7 |
| 25 | Cycle с 6+ steps как vertical list | Compact dialog form OR pipeline subtype | REFLECTION §3.1 Failure 1 + Fix-18 |
| 26 | Pipeline с filled_rect+triangle гибрид (не RIGHT_ARROW) | MSO_SHAPE.RIGHT_ARROW shapes | REFLECTION §6.1 New observation |
| 27 | Custom-coined «рабочие термины» («рабочее определение AI», «приложение-робот») | Canonical из glossary; verify via Google Scholar | REFLECTION §3.4 Failure 2 + §5.2 |
| 28 | Designer-driven slide deletion без user request (s14 deletion) | Ask before remove; paraphrasing ≠ duplicate | ROAST missed #2 |
| 29 | WPM violations passed как «8 of 10 ≤97 acceptable» | Hard rule: any fragment >95 WPM = P0, refuse output | ROAST missed #1 |
| 30 | Self-containedness 28/34 «better than v2» considered OK | Absolute threshold ≥30/N; <20 = REJECT | ROAST missed #12 |
| 31 | Snapshots в repo (562 PNG, 71 MB) | gitignore all snapshots, derive on demand | REFLECTION §6.3 + §8.1 + ROAST #7 |
| 32 | Build script proliferation (7 versions per lecture) | Single canonical build.py per lecture + git history | REFLECTION §8.2 + ROAST #8 |
| 33 | Mixed icon sets (Lucide + Phosphor + Heroicons random) | One set per deck (LobeHub for AI logos OK) | VISUAL-AUDIT |
| 34 | Visual mass imbalance (squint test fails) | Visual Mass Balance rule + counter-weight technique | VISUAL-AUDIT + REFLECTION §2.3 #9 |
| 35 | Visual loop iter > 7 без escalation (sink cost) | Hard cap 7, escalate to user with alternatives | REFLECTION + ROAST extra #5 |

### Schema readability per type (7 subtypes)

(Полный checklist — см. `.claude/agents/presentation-designer.md` § «Schema
Readability Checklist».)

Patterns observed:
- **Works first-try (1-2 iter):** comparison_2col, matrix_2x2 (с правильным brief).
- **Needs 2-3 iter:** pipeline (≤5 stages), quadrant, timeline (≤6 events).
- **Needs structural redesign (4+ iter):** cycle (>4 steps), layered (>4 levels),
  dense timeline, custom architecture.

### Pre-USER-GATE walkthrough protocol

(Полный procedure — см. CLAUDE.md § «Pre-USER-GATE Protocol» + `tools/lecture-production/README.md`
§ «3.1 Pre-USER-GATE Walkthrough».)

Hard rule: «approve» ≠ «critics approved», requires explicit orchestrator
pre-review.

### Glossary lock после chapter approval

После Phase 4 USER GATE 1 — orchestrator generates `library/lectures/lec-NN/glossary.yaml`.
Critics MAY flag inconsistency, MAY NOT propose rename без user approval.
(см. CLAUDE.md § «Glossary Lock» + consistency-checker.md § «Glossary Lock Enforcement».)

### Critic blind spots каталог (10 items)

(Полный список с примерами — см. REFLECTION.md §4.1.) Top blind spots:
1. Schema readability for laymen.
2. Curriculum relevance (intro/intermediate/advanced match).
3. Visual centring of charts.
4. Cross-slide redundancy.
5. Term canonical-validity.
6. Tools/benchmark freshness.
7. Designer-added content.
8. Color-only highlights vs text markers.
9. Notes-as-readable-text vs layout descriptions.
10. Title-vs-body assertion alignment.

### Verdict scale recalibration

Old: APPROVE-WITH-MINOR / REJECT (binary-ish).
New: REJECT (any P0) / REVISE (5+ P1) / APPROVE-WITH-POLISH (≤4 P1) /
APPROVE-CLEAN (0 P1).
Counter-check enforced в каждом critic agent prompt.
```

---

### 14. `notes/mcp-limitations.md`

**Current state:** 317 lines, organized by server.

#### 14.1 ADD 3 new entries в section «powerpoint»

```markdown
### [#69-pptx-1] LibreOffice convert overhead at scale

- **Tool:** `libreoffice --headless --convert-to pdf` в Visual Loop.
- **Symptom:** Каждая визуальная итерация = libreoffice headless ~3-5 сек на
  30+ slides. С 14 итерациями × 5 параллельных designers = 1+ минута чистого
  latency только на convert.
- **Severity:** P2 (workaround существует).
- **Workaround:** (a) convert per-slide если возможно (`--convert-to pdf
  --convert-to:writer_pdf_Export:SinglePagePerSheet` — нужно проверить);
  (b) batch convert vs per-iter (запускать convert one для всех designers);
  (c) reduce slide count для visual loop (focus на изменённые slides only).
- **Status:** active.
- **First seen in:** Л1 v3.x production (2026-05-13).

### [#69-pptx-2] python-pptx-direct vs MCP-based для full-deck builds

- **Server:** `powerpoint` (MCP).
- **Symptom:** Для full-deck rebuild (33 slides × 5+ iter), MCP-based approach
  значительно медленнее python-pptx direct script. Causes:
  (1) full-rebuild на каждой итерации делает MCP iterative API бесполезным;
  (2) python-pptx даёт прямой контроль над XML inject (для backgrounds, runs);
  (3) MCP serialization-deserialization overhead.
- **Severity:** P2 (architectural decision).
- **Workaround:** **Для full-deck builds — python-pptx direct script** +
  helper functions (canonical `build.py` per lecture). MCP — для quick spike /
  preview / individual slide tweaks.
- **Status:** active (decision recorded).
- **First seen in:** Л1 v3.x production (2026-05-13).

### [#69-pptx-3] MSO_SHAPE.RIGHT_ARROW vs filled_rect+rotated_triangle для arrows

- **Server:** `powerpoint`.
- **Tool / feature:** `add_shape`.
- **Symptom:** При попытке нарисовать arrow через гибрид `filled_rect` +
  `rotated_triangle` — visually выглядит «сломанно», не как proper connector
  arrow. Real cause — proportions tail+head не consistent.
- **Severity:** P3 (cosmetic but affects credibility).
- **Workaround:** Use `MSO_SHAPE.RIGHT_ARROW` shape directly — proper proportions.
  Confirmed working в Л1 v3.2 Fix-11.
- **Status:** active (workaround надёжный).
- **First seen in:** Л1 v3.2 (2026-05-13).
```

#### 14.2 UPDATE existing [#54-1] и [#54-3] severity

Изменить severity from `P1`/`P2` to `P0-PRIORITY-FOR-FORK now` для обоих.
Обоснование: at scale 17 lectures × 30 slides × 5+ iter каждая, отсутствие
`list_shapes` + `update_shape_position` = 12-20 hours overhead per course.
Fork = 3 hours one-time → 4× ROI.

Add note:
```markdown
**ROI estimate (2026-05-13 review):** list_shapes + update_shape_position
saved time = ~3-5 min per visual iter × 14 iter × 17 lectures = 12-20 hours.
Fork = 3 hours one-time → 4× ROI. **Recommendation: fork now**, до начала
Лекции 2.
```

#### 14.3 UPDATE «Last update» line at bottom

```markdown
**Last update:** 2026-05-13 (Л1 v3.x production — добавлены [#69-pptx-1],
[#69-pptx-2], [#69-pptx-3]; updated severity для [#54-1] и [#54-3] to fork-now).
```

---

### 15. `.claude/skills/build-deck/SKILL.md`

**Current state:** 132 lines, 7 phases (Read source / Reader-text-only / Render / 3 QA / Synthesize / Repeat / Update manifest).

#### 15.1 ADD Phase 4.5 «Pre-USER-GATE walkthrough» — between Phase 5 and Phase 6

Дословно (insert между current «Phase 5 — Synthesize + fix iteration» and «Phase 6 — Repeat»):
```markdown
### Phase 5.5 — Pre-USER-GATE walkthrough (ENFORCED)

**Перед** presenting visual results to user — orchestrator MUST run
pre-review (~15-30 min wall-clock).

**Procedure:**
1. Read all `library/lectures/lec-NN/rendered/snapshots/sNN.png` через Read tool.
2. Read all `library/lectures/lec-NN/slides/sNN.md` (speaker notes section).
3. Run automated greps:
   ```bash
   # Designer extras detection:
   grep -rE 'лектору|вы здесь|субтитр|на этой странице|следующий раздел' \
        library/lectures/lec-NN/slides/

   # Iteration leaks in snapshots:
   ls library/lectures/lec-NN/rendered/snapshots/ | grep -E 'iter|fix'

   # Cross-slide assertion duplicates:
   grep -h '^assertion:' library/lectures/lec-NN/slides/*.md | sort | uniq -d
   ```
4. Spawn `consistency-checker` mode=`terminology-only` для quick drift scan.
5. List 10+ issues found.
6. Apply quick fixes (P2 cosmetic) directly via subagent OR `presentation-designer` short fix.
7. Present to user as: «Я просмотрел N слайдов, нашёл K issues, фиксанул M,
   остался L because [reason]. Anything ты бы добавил?»

**Hard rule:** never present to user as USER GATE без explicit pre-review report.
```

#### 15.2 ADD section «Spawn Designer Strict Brief Format» — внутри Phase 3

В Phase 3 (Render) добавить:
```markdown
**Designer brief format (strict YAML):**
```yaml
modify:
  - sNN: <specific change description>
leave_untouched: [list of slide IDs NOT to modify]
forbidden_additions: [subtitle, navigation marker, лектору section,
                      decorative icons без semantic role,
                      cross-slide bridge text]
acceptance_criteria:
  - all modified slides pass 5-Second Test
  - no new content added beyond modify list
  - WPM in speaker notes ≤95 if applicable
```

**Parallel designer spawns:** если spawn 5 designers одновременно —
non-overlapping slide ownership. Each designer brief contains explicit
`leave_untouched: [list]`. Orchestrator validates non-overlap before spawn.
```

#### 15.3 UPDATE «If something fails» — add iteration cap rule

В section «Если что-то падает» добавить:
```markdown
- **5+ iter без прогресса** → STOP, обсудить с пользователем (возможно
  концепция слайда нуждается в пересмотре, не дизайн). **Hard cap: 7 iter** —
  если на 7-й нет результата, designer auto-escalates с list of
  alternatives (simplify / replace / split / delete).
```

---

### 16. Repository hygiene

#### 16.1 `.gitignore` — ADD snapshot policy

В конец `.gitignore` добавить:
```
# Lecture rendered snapshots (regeneratable from PPTX)
library/lectures/*/rendered/snapshots/
# Iteration logs per-version (use single rolling iteration-log.md instead)
library/lectures/*/rendered/iteration-log-v*.md
# Old build scripts (consolidate to single canonical build.py per lecture)
library/lectures/*/rendered/build_*_v*.py
```

**Decision recorded:** ALL snapshots gitignored (не только iter*.png), regenerable from PPTX. Rationale (ROAST item #9): final sNN.png тоже rebuildable from PPTX через libreoffice → repo size flat. Если нужен публичный snapshot view — separate `published/` directory.

#### 16.2 Build script consolidation policy

Add к `tools/lecture-production/README.md` § «6.3 Build Script Policy»:
```markdown
## 6.3 Build Script Policy (ENFORCED для new lectures)

Each lecture MAY have:
- `library/lectures/lec-NN/rendered/build.py` — canonical builder (single file).
- Versioning через git history, NOT через filename suffix.

**FORBIDDEN:**
- `build_lec02_v3.py`, `build_lec02_v31.py`, `build_v36.py`, etc. — proliferation.
- Multiple build scripts per lecture.

**Template:**
- Each new lecture copies from `tools/lecture-production/lecture-template/build.py`,
  NOT from previous lecture's build script (avoids snowball).
- (Template directory to be created в Phase 5 implementation.)

**Migration plan для Л1:**
- Keep current build_lec01_v32.py as canonical → rename to `build.py`.
- Delete (or archive) build_lec01_full.py, _v2.py, _v3.py, _v31.py, _v36.py.
- Iteration logs v2/v3/v31/v32/v34/v4 → merge to single `iteration-log.md` +
  delete versioned variants.
```

#### 16.3 QA reports organization

Add к `tools/lecture-production/README.md` § «6.4 QA Reports Layout»:
```markdown
## 6.4 QA Reports Layout (ENFORCED)

**Standard schema:**
```
library/lectures/lec-NN/qa-reports/
  {YYYY-MM-DD}-phase{N}-{artifact}-v{V}/
    methodology-critic.md
    fact-checker.md
    presentation-critic.md
    student-simulator.md
    reader-rendered.md (или reader-text-only.md)
    consistency-checker.md
    SYNTHESIS.md
    freshness-report.md  (если применимо)
```

**Examples:**
- `2026-05-13-phase4-chapter-v3.1/`
- `2026-05-13-phase7-slides-v3.2/`
- `2026-05-13-phase10-speech-v3.1/`

**FORBIDDEN:**
- Mixing per-version + per-feedback-batch (e.g. `2026-05-12-chapter-v1/`,
  `2026-05-12-deck-v2/`, `2026-05-13-user-feedback-23/` — inconsistent).
- Multiple folders per same artifact-version.

**Migration plan для Л1:**
- Existing 9 folders → consolidate to 4: phase4-chapter, phase7-slides,
  phase10-speech, user-feedback (cross-cutting).
```

---

## Risks Лекции 2 (что осталось open после implementation)

Даже после implementation P0+P1, эти риски остаются — нужен conscious monitoring во время Л2 production:

### Risk A (P1): Schema readability — pre-wireframe не guarantees first-try success

Pre-design wireframe — добавлен (§12.4), но реальные данные L1 показывают что некоторые subtypes (cycle с 4+ steps, dense layered) inherently требуют 4-5 iter даже с wireframe. Risk: первый Л2 attempt всё равно может попасть в visual loop overhead.

**Mitigation:** track per-subtype iter count в Л2; если cycle/layered/dense-timeline превышает expected pattern (4-5 iter) — escalate to redesign, not polish.

### Risk B (P1): User-positional vs slide-ID translation overhead

Round 1 #3 показал — user говорит «слайд 7», у нас s06. Reflection §5.4 предлагает orchestrator skill для translation, но не реализован. Risk: каждый user feedback round будет 5-10 минут на disambiguation.

**Mitigation:** в начале каждой user-review session — orchestrator выводит slide-ID ↔ position map: «s01→1, s02→2, s02a→3, s03→4, ..., s10→13, s11→14, ...». User работает с position numbers, orchestrator translates.

### Risk C (P1): Critic-driven content additions (Pearl, ARC-AGI patterns)

Pearl + ARC-AGI слайды — добавлены critics (methodology) в раунд v2/v3, удалены user в round 1. Critic «evaluate-level» рекомендации могут снова добавить overly-deep концепты. Curriculum Relevance Check (§5.1) частично mitigates, но subjective.

**Mitigation:** critics в Л2 имеют explicit instruction «for introductory lecture (L2 = «Современные большие модели»), curriculum_level = intermediate — KEEP analyze-level, RECOMMEND DELETE evaluate-level». Tracking — orchestrator review каждое critic recommendation на Bloom level соответствие.

### Risk D (P1): Tools/benchmark freshness — даже с freshness check данные устаревают между Phase 7 (slides QA) и USER GATE 3 (final)

Production cycle Л2 предположительно ~2-3 days. AI benchmarks shift weekly. Even с freshness check at Phase 3, к Phase 11 (final) данные могут быть stale.

**Mitigation:** freshness check выполняется **дважды** — Phase 3 (initial) + перед USER GATE 3 (final). Diff report — что изменилось since Phase 3. Lecturer pre-flight (день лекции) — третий final check.

### Risk E (P1): «Designer-added content» не полностью преодолимо в creative role

No Extra Content Rule (§1.2 + §2.3 + §13 anti-pattern 16) — strict, но designer-Opus-4.7 имеет creative tendency. Даже с explicit rule, edge cases возможны (e.g. designer думает «эта icon — semantic role», user disagrees).

**Mitigation:** review каждый designer-output diff (vs previous version) для new additions; default — challenge any addition не in brief; designer должен defend, не просто apply.

---

## Open questions для user

Перед implementation start — нужны explicit answers:

1. **Pre-USER-GATE walkthrough — manual orchestrator или auto skill?** Ramping up `pre-gate-review` skill (option B in §15.1) добавляет 1-2 часа implementation effort, но даёт ROI = repeatable + faster (vs 30 min manual × 3 USER GATEs × 17 lectures = 25.5 hours manual). **Recommend: auto skill (Phase 6 в plan).** Confirm?

2. **PowerPoint MCP fork** (list_shapes + update_shape_position + delete_shape) — invest 3 часа сейчас или продолжать build-script-direct approach? §14 рекомендует fork now (4× ROI), но это extra one-time engineering. **Recommend: fork now, до Л2 start.** Confirm?

3. **Curriculum levels mapping** (`catalog/manifests/lectures.yaml`) — нужен сейчас, до methodology-critic implementation. Owner-я: оркестратор или user? Если orchestrator — он генерирует initial mapping (Lectures 1-3 introductory, 4-12 intermediate, 13-17 advanced) и user approves в одной reply. **Recommend: orchestrator-generated, user one-shot approve.** Confirm?

4. **Pearl + ARC-AGI слайды в финальной Л1 v3.2** — оставлены (user не explicit удалил after round 3). Для Л2 — учитывать как «accepted inclusion» или удалить retroactively? Decision affects Curriculum Relevance Check matrix calibration.

5. **«Лектору» vs speaker notes split** — round 1 #1 implied «Лектору» секция допустима как отдельный блок. Round 3 #1 «убери раздел для лектора». Финальное правило: **без «Лектору» секции в notes вообще, всё в speech.md?** Need explicit confirmation.

6. **Tools/benchmarks freshness — practical workflow.** Lecture-day script `bin/freshness-check.sh` для greping benchmarks + showing «outdated» warnings — нужен / отложен / не нужен (всё в methodology-critic + fact-checker)?

7. **Designer-added vs requested split — strict «do nothing not asked» граница.** Может убить creative input. Где cut-off — «do nothing» или «do nothing структурно меняющее»? Cosmetic decisions (color choice, exact position) — designer's domain или user's?

8. **Verdict scale change — show ли user видеть REVISE vs APPROVE-WITH-POLISH explicitly,** or нужна binary «can show / cannot»? §5.5 предлагает 4-level, но maybe 2-level (REJECT / APPROVE-WITH-CAVEATS) проще.

9. **5 параллельных designers vs 1 sequential.** Sequential безопаснее (no race conditions), но дольше. Decision rule — at what threshold (slides count, fix count) спавнить parallel? Maybe always sequential для critical changes, parallel только для cosmetic.

10. **Glossary lock — реальность.** §1.3 + §11.6 предлагают auto-generation orchestrator после chapter approve. Realistic — нужен ли user review glossary до lock? Если да — добавляется extra USER GATE (4-я gate).

---

## Implementation Phases

### Phase 1 (P0, 2-3 hours): Agent prompts updates

**Sequence (independent edits, can be parallel):**

1. **`presentation-designer.md`** (largest changes — 8 new sections + 2 updates):
   - Schema Readability Checklist (7 subtypes) (§2.1)
   - 5-Second Test (§2.2)
   - No Extra Content Rule (§2.3)
   - Cross-Slide Redundancy grep (§2.4)
   - Projector Readability Test (§2.5)
   - Iconography Discipline (§2.6)
   - Visual Mass Balance (§2.7)
   - Visual Loop Iteration Cap (§2.8)
   - Designer Brief Strict Format (§2.9)
   - Speaker Notes contract update (§2.10)
   - **Estimated:** 90 min

2. **`methodology-critic.md`** (4 additions + verdict scale):
   - Curriculum Relevance Check (§5.1)
   - Term Canonical-Validity Check (§5.2)
   - Tools/Benchmark Freshness Check (§5.3)
   - Designer-Added Content Audit (§5.4)
   - Verdict scale (§5.5)
   - **Estimated:** 30 min

3. **`presentation-critic.md`** (5 additions):
   - Schema Readability Evaluation (§6.1)
   - Cross-Slide Redundancy Detection (§6.2)
   - Designer-Added Extras Detection (§6.3)
   - Verdict scale update (§6.4)
   - Save Report Mandate (§6.5)
   - **Estimated:** 20 min

4. **`consistency-checker.md`** (3 additions):
   - Mode terminology-only (§7.1)
   - Phase mapping update (§7.2)
   - Glossary Lock Enforcement (§7.3)
   - **Estimated:** 20 min

5. **`speech-writer.md`** (4 additions):
   - WPM Hard Rule (§4.1)
   - «Мы с вами» Distribution (§4.2)
   - Pre-Flight Sync Rule (§4.3)
   - Англицизм Cleanup Pass (§4.4)
   - **Estimated:** 25 min

6. **`book-editor.md`** (4 additions):
   - Speaker Notes Hand-Off (§3.1)
   - Cross-reference to Course Structure (§3.2)
   - Mark Unverified Specifics update (§3.3)
   - Cascade-of-Changes Tracking (§3.4)
   - **Estimated:** 20 min

7. **`fact-checker.md`** (4 additions):
   - Curriculum / Drive Sync Check (§8.1)
   - Tools/Benchmark Freshness (§8.2)
   - Mandatory File Save (§8.3)
   - Verdict scale update (§8.4)
   - **Estimated:** 20 min

8. **`student-simulator.md`** (2 additions):
   - Schema Readability per Slide Perspective (§9.1)
   - Explicit Slides-to-Delete (§9.2)
   - **Estimated:** 15 min

9. **`reader-simulator.md`** (1 addition):
   - Self-Containedness Threshold Escalation (§10.1)
   - **Estimated:** 10 min

**Phase 1 total:** ~250 min wall-clock if parallel; ~4 hours if sequential. **Subagent delegation possible per file.**

### Phase 2 (P0, 1 hour): Methodology docs updates

1. **`tools/presentation-build/README.md`** (3 additions + extension):
   - Schema Readability Acceptance Gate (§12.1)
   - Schema subtypes extension в slide-types library (§12.2)
   - Anti-patterns 16-35 (§12.3)
   - Pre-Design Wireframe (§12.4)
   - Visual Loop Iteration Cap (§12.5)
   - **Estimated:** 30 min

2. **`tools/lecture-production/README.md`** (5 additions):
   - Pre-USER-GATE Walkthrough (§11.1)
   - Cascade-of-Changes Tracking (§11.2)
   - Phase 7 update (§11.3)
   - Speaker Notes Contract (§11.4)
   - Curriculum-Level Metadata (§11.5)
   - Glossary Lock Phase 4.5 (§11.6)
   - Anti-patterns 9-12 (§11.7)
   - **Estimated:** 30 min

**Phase 2 total:** ~60 min.

### Phase 3 (P1, 1 hour): Decisions + limitations

1. **`notes/decisions.md`** — new section «2026-05-13 — Lecture 1 v3 production lessons» с 20 anti-patterns (16-35) + summary tables. **Estimated:** 40 min.

2. **`notes/mcp-limitations.md`** — 3 new entries (#69-pptx-1/2/3) + severity update для #54-1 + #54-3 + Last update line. **Estimated:** 20 min.

**Phase 3 total:** ~60 min.

### Phase 4 (P1, 30 min): CLAUDE.md updates

1. **`CLAUDE.md`** — 3 new sections + 2 updates:
   - Pre-USER-GATE Protocol (§1.1)
   - No Extra Content Rule (§1.2)
   - Glossary Lock (§1.3)
   - Subagent Rules update (§1.4)
   - Anti-Patterns table 4 new rows (§1.5)
   - **Estimated:** 30 min.

### Phase 5 (P2, 1 hour): Repository hygiene

1. **`.gitignore`** — snapshot policy + iteration logs + build script suffix patterns (§16.1). **Estimated:** 5 min + cleanup.
2. **Build script consolidation для Л1** (§16.2) — rename `build_lec01_v32.py` → `build.py`, delete/archive others, merge iteration logs. Subagent task. **Estimated:** 30 min.
3. **QA reports organization** (§16.3) — rename existing 9 folders to standardized schema. Subagent task. **Estimated:** 25 min.

**Phase 5 total:** ~60 min.

### Phase 6 (P2, 30-60 min, optional): Skills

1. **`.claude/skills/build-deck/SKILL.md`** — Phase 5.5 addition + Designer Brief Strict Format + iteration cap rule (§15.1, §15.2, §15.3). **Estimated:** 30 min.

2. **(Optional) `.claude/skills/pre-gate-review/SKILL.md`** — new skill that automates orchestrator pre-USER-GATE walkthrough. **Estimated:** 30 min for skeleton; iterative refinement during Л2.

**Phase 6 total:** 30-60 min.

---

## Total Estimated Effort

| Phase | Items | Time | Priority |
|---|---|---|---|
| Phase 1 | 9 agent prompts | 4 hours | P0 |
| Phase 2 | 2 methodology docs | 1 hour | P0 |
| Phase 3 | decisions + limitations | 1 hour | P1 |
| Phase 4 | CLAUDE.md | 30 min | P1 |
| Phase 5 | repo hygiene | 1 hour | P2 |
| Phase 6 | skills | 30-60 min | P2 |
| **TOTAL** | 16 files | **~7-8 hours** | — |

**P0 only (must-have перед Л2):** Phase 1 + Phase 2 = ~5 hours.
**P0+P1 (recommended):** + Phase 3 + Phase 4 = ~6.5 hours.
**Full implementation:** ~8 hours.

---

## Sequencing Notes

**Critical dependencies:**
- CLAUDE.md «Glossary Lock» reference = consistency-checker «Glossary Lock Enforcement» depends on. Update CLAUDE.md FIRST or in parallel с consistency-checker.
- presentation-designer «Schema Readability Checklist» = presentation-critic «Schema Readability Evaluation» mirrors. Update designer FIRST.
- tools/lecture-production «Phase 4.5 Glossary lock» = consistency-checker phases. Update README FIRST or в parallel.

**Independent edits (parallel-safe):**
- All 9 agent prompts can be edited in parallel via subagent delegation.
- decisions.md + mcp-limitations.md independent.
- .gitignore independent.

**Recommended order для один-человек execution:**
1. Phase 4 (CLAUDE.md) — sets baseline rules referenced by other docs.
2. Phase 2 (methodology docs) — sets pipeline references.
3. Phase 1 (agents) — bulk implementation, can be parallelized via subagents.
4. Phase 3 (decisions + limitations) — references implementation.
5. Phase 5 (hygiene) — cleanup after.
6. Phase 6 (skills) — optional polish.

---

## Top-3 Critical Changes (если только 3 успеть до Л2)

Если время не хватает для full implementation — minimal viable changeset для preventing Л1-style 3-round rework:

### Critical 1: Pre-USER-GATE Walkthrough Protocol
**Files:** CLAUDE.md (§1.1) + tools/lecture-production/README.md (§11.1) + build-deck/SKILL.md (§15.1).
**Effort:** 60 min total.
**Impact:** addresses **REFLECTION §7.4** — главный root cause «approve» = «critics approved», not «I reviewed». Каждый из 3 user feedback rounds Л1 — после critic-approve, before orchestrator pre-review. Это **single biggest** preventable cause of rework.
**Why critical:** affects ALL 3 USER GATEs × ALL future lectures.

### Critical 2: Schema Readability Checklist (7 subtypes) + 5-Second Test + No Extra Content Rule
**Files:** presentation-designer.md (§2.1, §2.2, §2.3) + presentation-critic.md (§6.1, §6.3) + tools/presentation-build/README.md (§12.1, §12.3 anti-patterns 16-35).
**Effort:** 90 min total.
**Impact:** addresses **VISUAL-AUDIT primary content** — schema redesigns в s11/s13/s16/s21 (5+ iter каждый, user всё равно отверг) + designer-added extras (тайминг, «вы здесь», «Лектору», subtitle). **62 user-driven changes Л1 — ~40% visual + designer-added.**
**Why critical:** addresses **biggest single chunk** of user feedback (visual + designer extras).

### Critical 3: WPM Hard Rule + Speaker Notes Contract
**Files:** speech-writer.md (§4.1) + presentation-designer.md (§2.10 speaker notes) + book-editor.md (§3.1 speaker notes hand-off).
**Effort:** 60 min total.
**Impact:** addresses **ROAST missed #1** (WPM violations прошли в финальную speech v3.2 как acceptable — methodology DoD violation) + **REFLECTION §2.1 #1** (round 1 fix #1 = «notes должны быть читаемым текстом, не описанием layout» — самое крупное user замечание).
**Why critical:** **WPM** = methodology-critic blind spot для DoD enforcement; **notes contract** = #1 user complaint в round 1.

**Top-3 total effort:** ~3.5 hours. Catches ~70% of Л1 v3 failure modes if applied.

---

*Конец consolidated plan. Готов для implementation. Следующий шаг — user approval + Phase 1 spawn.*

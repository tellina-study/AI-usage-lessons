# Multi-artifact Lecture Production Pipeline

**Canonical doc** для сборки полной лекции (3 финальных артефакта). Любой агент, работающий над лекционным материалом, читает этот файл **первым**.

**Связан с** `tools/presentation-build/README.md` — он покрывает только slides-specific. Этот README — **полный пайплайн**, slides — одна из фаз.

---

## 1. Финальные артефакты (3 на каждую лекцию)

```
library/lectures/lec-NN/
  chapter.md              ← глава методички ~8-12k слов (academic)         [PRIMARY = source of truth]
  rendered/lec-NN.pptx    ← презентация со speaker notes для студентов     [DERIVED from chapter]
  speech.md               ← речь лектора ~4-6k слов (conversational)        [DERIVED from chapter + slides]
```

**Source of truth:** `chapter.md`. Slides и speech derive из неё. При conflict — fix slides/speech, не chapter (если chapter сам не ошибается).

---

## 2. Промежуточные артефакты

```
library/lectures/lec-NN/
  deck.yaml               ← структура слайдов (см. tools/presentation-build/README.md)
  slides/
    sNN-*.md              ← per-slide content (assertion + visible + speaker notes)
  rendered/
    snapshots/sNN.png     ← визуальные снапшоты
    iteration-log.md      ← лог визуального цикла
    assets/               ← icons, charts, diagrams, illustrations
  qa-reports/
    {YYYY-MM-DD-vN}/
      methodology-critic.md
      fact-checker.md
      reader-text-only.md
      presentation-critic.md
      student-simulator.md
      reader-rendered.md
      consistency-checker.md
      SYNTHESIS.md
```

И **в репо вне library/**:
- `notes/lecture-N-review/final/new-plan-vN-final.md` — narrative план (input для chapter).
- `notes/research/lecture-N/*.md` — research notes (источники, факты).

---

## 3. Workflow (11 фаз + 3 USER GATEs A/B/C)

```
┌─────────────────────────────────────────────────────────────────┐
│ Phase 1 — Plan critique                                         │
│ Agents: methodology-critic + reader-text-only (на v4 plan)      │
│ Output: notes/lecture-N-review/{date}/critique-of-vN.md         │
├─────────────────────────────────────────────────────────────────┤
│ Phase 2 — Chapter draft                                         │
│ Agent: book-editor                                              │
│ Output: library/lectures/lec-NN/chapter.md (status=draft)       │
├─────────────────────────────────────────────────────────────────┤
│ Phase 3 — Chapter critique                                      │
│ Agents (parallel): methodology-critic + fact-checker +          │
│                    reader-simulator mode=text-only              │
│ Output: 3 reports → SYNTHESIS                                   │
├─────────────────────────────────────────────────────────────────┤
│ Phase 4 — Chapter revision (book-editor) → finalize             │
│ Status: draft → reviewed → finalized                            │
├─────────────────────────────────────────────────────────────────┤
│ Phase 4.5 — Pre-USER-GATE walkthrough (orchestrator self-review)│
│ Skill: /pre-user-gate (mode=chapter)                            │
│ Steps: read chapter as student, find P0/P1 NOT caught by critics│
│ Outcome: fix P0/P1 BEFORE presenting GATE A                     │
├─────────────────────────────────────────────────────────────────┤
│ ✋ USER GATE A — chapter approved                                │
│ Criteria: pre-gate walkthrough INCLUDED reading test            │
├─────────────────────────────────────────────────────────────────┤
│ Phase 5 — Slides update from chapter                            │
│ Agent: presentation-designer (refine deck.yaml + slides/*.md)   │
│ Update assertions / learning_goals из chapter                   │
├─────────────────────────────────────────────────────────────────┤
│ Phase 6 — Slides design + visual loop                           │
│ Agent: presentation-designer (visual-loop min 3 / max 7 iter    │
│   per slide, escalate at iter 7)                                │
│ See: tools/presentation-build/README.md §5, §5.5, §5.6          │
├─────────────────────────────────────────────────────────────────┤
│ Phase 7 — Slides QA                                             │
│ Agents (parallel): presentation-critic + student-simulator +    │
│                    reader-simulator mode=rendered +             │
│                    consistency-checker (chapter ↔ slides) +     │
│                    fact-checker (если данные на slides)         │
│ Output: 5 reports → SYNTHESIS                                   │
├─────────────────────────────────────────────────────────────────┤
│ Phase 8 — Slides revision → finalize                            │
├─────────────────────────────────────────────────────────────────┤
│ Phase 8.5 — Pre-USER-GATE walkthrough (orchestrator self-review)│
│ Skill: /pre-user-gate (mode=slides)                             │
│ Steps: visual sweep all PNGs + read 5-7 random speaker notes +  │
│   designer-extras grep + checklist (schemas, terminology, etc.) │
│ Outcome: fix P0/P1 BEFORE presenting GATE B                     │
├─────────────────────────────────────────────────────────────────┤
│ ✋ USER GATE B — slides approved                                 │
│ Criteria: pre-gate walkthrough INCLUDED visual sweep            │
├─────────────────────────────────────────────────────────────────┤
│ Phase 9 — Speech draft                                          │
│ Agent: speech-writer (из finalized chapter + slides)            │
│ Output: library/lectures/lec-NN/speech.md (status=draft)        │
├─────────────────────────────────────────────────────────────────┤
│ Phase 10 — Speech critique + consistency check                  │
│ Agents (parallel): methodology-critic (speech-specific) +       │
│                    fact-checker (на speech) +                   │
│                    consistency-checker (chapter ↔ slides ↔ speech)│
│ Output: 3 reports → SYNTHESIS                                   │
├─────────────────────────────────────────────────────────────────┤
│ Phase 11 — Speech revision → finalize                           │
├─────────────────────────────────────────────────────────────────┤
│ Phase 11.5 — Pre-USER-GATE walkthrough (orchestrator self-review)│
│ Skill: /pre-user-gate (mode=final)                              │
│ Steps: cross-artifact consistency grep + pre-flight checklist   │
│   actionability + cornerstone concepts alignment                │
│ Outcome: fix P0/P1 BEFORE presenting GATE C                     │
├─────────────────────────────────────────────────────────────────┤
│ ✋ USER GATE C — final approval (всё 3 артефакта)                │
│ Criteria: pre-gate walkthrough INCLUDED cross-artifact grep     │
└─────────────────────────────────────────────────────────────────┘
```

**Каждый USER GATE — explicit approval.** Не двигаться к следующей фазе без него.

### USER GATE criteria (явно)

| Gate | Что approve | Pre-gate walkthrough mode | Что обязательно сделано |
|---|---|---|---|
| **GATE A** | chapter.md (status=reviewed) | `/pre-user-gate mode=chapter` | Reading test: orchestrator прочитал главу как студент, найдены P0/P1 (relevance, terminology, factual, reading flow), исправлены ДО presenting user. |
| **GATE B** | slides (deck.yaml + slides/*.md + rendered/lec-NN.pptx + snapshots) | `/pre-user-gate mode=slides` | Visual sweep: открыты все PNG, проверена schema readability + designer-extras grep («Лектору», «Вы здесь», тайминг, subtitle) + speaker notes sample read + checklist (palette, gold ≥1×, footer-tax 0, англицизмы 0). |
| **GATE C** | final 3 artifacts (chapter + slides + speech) | `/pre-user-gate mode=final` | Cross-artifact consistency grep: cornerstone концепты aligned (central question, ключевые термины, числа, attributions, roadmap), terminology unified, pre-flight в speech actionable + 0 orphan refs к удалённым slides. |

**Принцип pre-gate walkthrough:** «critics проходят там, где user отклоняет» (Лекция 1 v3 had 3 user feedback rounds после critic-approve). Pre-gate walkthrough — orchestrator-level self-review, который дублирует user-perspective и ловит P0/P1 ДО formal gate'а. См. `.claude/skills/pre-user-gate/SKILL.md`.

---

## 3.5 Cascade-of-changes tracking (ENFORCED)

Когда меняется content одного artifact, downstream artifacts могут разъехаться. Orchestrator **обязан** трекать cascade и автоматически проверять impact.

### Триггеры cascade-check

| Изменение | Что грепать downstream |
|---|---|
| **Slide rename** (sNN-old-id → sNN-new-id) | speech.md, chapter.md, other slides/*.md, qa-reports — на старый ID |
| **Term renaming** (например, «Приложение-робот» → «AI-приложение») | grep по всем 3 artifacts; consistency-checker пересчитать |
| **Roadmap shift** (модули программы курса reshuffle) | chapter §intro, slides «карта курса», speech «карта курса», `catalog/manifests/lectures.yaml` |
| **Slide deletion** | speech pre-flight checklist (orphan refs!), other slides «callbacks к sNN», chapter §«ссылки на материал» |
| **Chapter section restructure** | slides assertions (если sourced from chapter §X), speech pacing (если глава была reference для timing) |

### Workflow cascade-check

1. **Detect change** — orchestrator замечает diff в одном из 3 artifacts.
2. **Auto-grep** — orchestrator (или pre-user-gate skill) grepает downstream на старые references.
3. **Report cascade list** — список найденных «orphan / stale» references → revision agent (book-editor / presentation-designer / speech-writer) фиксит.
4. **Re-run consistency-checker** — после revision sync verifies.

**Якорь правила:** speech v3 в Лекции 1 имел orphan reference на удалённый s26 (ARC-AGI слайд) — consistency-checker поймал как P0 на финальной фазе. Если бы cascade-check работал на этапе deletion — поймали бы сразу.

---

## 4. Роли всех агентов (8 total)

### Производители (writers / builders)
| Agent | Что производит | Capabilities (NEW from Лекции 1 v3) | Phase |
|---|---|---|---|
| `book-editor` | `chapter.md` | Mark unverified specifics `[FACT-CHECK]`; cross-reference course structure (Drive doc) для footnotes; speaker-notes section markers `[for-slide-sNN]` | 2, 4 (revisions) |
| `presentation-designer` | slides/*.md adjustments + rendered PPTX + snapshots | **Schema Readability Checklist** per schema slide; **No-extra-content rule** (do nothing not in brief); **Speaker notes contract** (150-300 words readable text, NO layout descriptions); per-designer file ownership при parallel spawn; visual-loop max 7 iter с escalation | 5, 6, 8 |
| `speech-writer` | `speech.md` | Pre-flight sync с deck.yaml (auto-regenerate при slide deletions); англицизм cleanup pass; reference user-provided Drive docs | 9, 11 (revisions) |

### Критики (reviewers, read-only)
| Agent | Что проверяет | Capabilities (NEW) | Phase |
|---|---|---|---|
| `methodology-critic` | Pedagogical depth, LO coverage, sequence, assertion-evidence | **Curriculum Relevance check** («зачем в лекции N — introductory/intermediate/advanced?»); **Term canonical-validity** (insider phrasing detection); англицизмы в tone-analysis; designer-added content audit | 1, 3, 7, 10 |
| `fact-checker` | Цифры, даты, attribution, citations | **Freshness verification** (date of source + refresh cadence + verify-on-day-of-lecture для < 1 month); user-provided source documents (Drive); mandatory file save | 3, 7, 10 |
| `presentation-critic` | Визуал deck'а (overlap, contrast, hierarchy, anti-patterns) | **Schema Readability check** (mirror designer's checklist); cross-slide redundancy grep; **5-second teach test** для diagrams; updated verdict scale (REJECT / REVISE / APPROVE-WITH-POLISH / APPROVE-CLEAN) | 7 |
| `student-simulator` | Студент в зале (PNG + speaker notes) | **Explicit slides-to-delete recommendation** (P1-DELETE category) | 7 |
| `reader-simulator` | 2 mode'а: `text-only` (md без рендера) + `rendered` (PNG + notes через 2 нед) | **Structural blocker assessment** (mode=rendered: notes-fix vs structural cut) | 1, 3, 7 |
| `consistency-checker` | Chapter ↔ slides ↔ speech alignment | **Terminology Drift sub-mode** (`terminology-only`): grep по watched terms перед каждым USER GATE; runs Phase 4.5, 8.5, 11.5 (не только 10) | 4.5, 7, 10, 11.5 |

### Pre-USER-GATE walkthrough (orchestrator skill)

`/pre-user-gate` — orchestrator self-review skill, запускается перед каждым USER GATE (A/B/C). Дублирует user-perspective, ловит P0/P1 что critics miss. См. `.claude/skills/pre-user-gate/SKILL.md`.

---

## 5. Источники по теме

### Chapter authoring
- Russell & Norvig **AIMA** 4th ed — образец академического текста.
- Mayer's **Multimedia Learning Principles** — application для chapter ↔ slides split.
- **Bloom's taxonomy** — для калибровки LO levels.
- **Retrieval practice** — для self-check вопросов.

### Speech writing
- TED-talks transcripts (NPR-style) — для conversational pacing.
- Карнеги «Как выступать публично» — основы.
- Anthropic **pptx skill** § «assume there are problems» — applies to speech tooltipи.

---

## 6. Размер artifacts

| Артефакт | Длина | Pacing |
|---|---|---|
| `chapter.md` | 8-12k слов (~30-50 страниц A4) | Self-study, ~30-60 мин чтения |
| `slides/*.md` | ~150-300 слов на slide × 25-30 slides ≈ 5-8k слов суммарно | Visible content + speaker notes |
| `speech.md` | 4-6k слов (≈70-80 wpm × 75 мин) | Сliceful pacing, паузы, переходы |

**Если chapter < 5k или > 15k — red flag** (либо мало материала для лекции, либо overload).

---

## 7. Anti-patterns (cross-artifact)

1. ❌ **Chapter повторяет slides дословно** — chapter должен быть deeper / wider.
2. ❌ **Speech читает chapter** — speech conversational, не learning.
3. ❌ **Slides не покрывают LO chapter'а** — coverage gap.
4. ❌ **Drift между artifacts** — цифры не сходятся, tone разный, ссылки разные.
5. ❌ **«Магическая пилюля» tone** в любом из 3 — нарушение D5.
6. ❌ **Local audience binding** («инженер ИУ6») в chapter — она универсальная для переиспользования.
7. ❌ **Skip USER GATE** — каждый gate explicit.
8. ❌ **Single-pass без critic'а** — каждый артефакт должен пройти ≥1 critic перед финализацией.

---

## 8. Связь с slides-specific pipeline

`tools/presentation-build/README.md` — фокусируется на slides:
- Palette (Ocean Gradient + Teal + Gold).
- Visual motif (Ocean rounded box).
- Slide-types library (8 типов).
- Visual-loop (min 3 iter).
- 3 QA-агента для slides (presentation-critic / student-simulator / reader-rendered).

Этот файл — **расширение**, добавляющее chapter + speech + новых критиков (`methodology-critic`, `fact-checker`, `consistency-checker`).

---

## 9. Текущий статус (#64 EPIC)

- ✅ **#65 (этот sub-issue)** — 5 агентов созданы, README написан, CLAUDE.md обновлён.
- 🟡 **#64.B** — Phase 1 пилота (re-review v4 plan Лекции 1).
- ⬜ **#64.C** — Phase 2-3 (chapter draft + critique).
- ⬜ **#64.D** — Phase 5-7 (slides update + design + QA).
- ⬜ **#64.E** — Phase 9-10 (speech draft + critique).
- ⬜ **#64.F** — Phase 11 (final approval).
- ⬜ **#64.G** — Methodology stabilization.

После #64.G — отдельный EPIC «Factory: scale to L2-L17».

---

## 10. References

- `notes/decisions.md` § «2026-05-12 — Presentation pipeline» — anti-patterns каталог + iteration journey.
- `notes/mcp-limitations.md` — gotchas tools.
- `tools/presentation-build/README.md` — slides-specific.
- Anthropic **pptx skill** (knowledge source): `github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md`.
- Penn State **assertion-evidence**: `writing.engr.psu.edu/ae_comprehension.pdf`.
- McGill **Design slides to support learning**: `teachingkb.mcgill.ca`.

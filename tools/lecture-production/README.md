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

## 3. Workflow (10 фаз + 3 USER GATEs)

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
│ ✋ USER GATE 1 — chapter approved                                │
├─────────────────────────────────────────────────────────────────┤
│ Phase 5 — Slides update from chapter                            │
│ Agent: presentation-designer (refine deck.yaml + slides/*.md)   │
│ Update assertions / learning_goals из chapter                   │
├─────────────────────────────────────────────────────────────────┤
│ Phase 6 — Slides design + visual loop                           │
│ Agent: presentation-designer (visual-loop min 3 iter per slide) │
│ See: tools/presentation-build/README.md §5                      │
├─────────────────────────────────────────────────────────────────┤
│ Phase 7 — Slides QA                                             │
│ Agents (parallel): presentation-critic + student-simulator +    │
│                    reader-simulator mode=rendered +             │
│                    fact-checker (если данные на slides)         │
│ Output: 4 reports → SYNTHESIS                                   │
├─────────────────────────────────────────────────────────────────┤
│ Phase 8 — Slides revision → finalize                            │
├─────────────────────────────────────────────────────────────────┤
│ ✋ USER GATE 2 — slides approved                                 │
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
│ ✋ USER GATE 3 — final approval (всё 3 артефакта)                │
└─────────────────────────────────────────────────────────────────┘
```

**Каждый USER GATE — explicit approval.** Не двигаться к следующей фазе без него.

---

## 4. Роли всех агентов (8 total)

### Производители (writers / builders)
| Agent | Что производит | Phase |
|---|---|---|
| `book-editor` | `chapter.md` | 2, 4 (revisions) |
| `presentation-designer` | slides/*.md adjustments + rendered PPTX + snapshots | 5, 6, 8 |
| `speech-writer` | `speech.md` | 9, 11 (revisions) |

### Критики (reviewers, read-only)
| Agent | Что проверяет | Phase |
|---|---|---|
| `methodology-critic` | Pedagogical depth, LO coverage, sequence, assertion-evidence | 1, 3, 7, 10 |
| `fact-checker` | Цифры, даты, attribution, citations | 3, 7, 10 |
| `presentation-critic` | Визуал deck'а (overlap, contrast, hierarchy, anti-patterns) | 7 |
| `student-simulator` | Студент в зале (PNG + speaker notes) | 7 |
| `reader-simulator` | 2 mode'а: `text-only` (md без рендера) + `rendered` (PNG + notes через 2 нед) | 1, 3, 7 |
| `consistency-checker` | Chapter ↔ slides ↔ speech alignment | 10 |

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

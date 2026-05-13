# QA reports — Лекция 1

Каталог QA-отчётов critic-агентов (`methodology-critic`, `fact-checker`, `presentation-critic`, `student-simulator`, `reader-simulator`, `consistency-checker`) по лекции 1 — пилот pipeline'а лекции, EPIC #64 + последующие revision rounds.

> **Структура папок здесь — historical**, она не следует current ENFORCED schema из `tools/lecture-production/README.md` § 6.4 (которая будет применяться начиная с Лекции 2). См. ниже как ориентироваться.

---

## Карта раундов (chronological)

| Папка | Раунд / Артефакт | Версия | Что внутри |
|---|---|---|---|
| `2026-05-12/` | **Earliest reader sanity** на chapter draft | v0/v1 (pre-pilot) | `reader-text-only.md` — initial check до выделения per-artifact rounds |
| `2026-05-12-chapter-v1/` | **Phase 4** (chapter QA), round 1 | chapter v1 | Полный набор: `SYNTHESIS.md` + `methodology-critic.md` + `fact-checker.md` + `reader-text-only.md` |
| `2026-05-12-chapter-v2/` | **Phase 4 sanity** после revision | chapter v2 | `sanity-check-methodology.md` (повторный pass только methodology-critic'а) |
| `2026-05-12-deck-v1/` | **Phase 7** (slides QA), round 1 | deck v1 | Полный набор: `SYNTHESIS.md` + `fact-checker.md` + `presentation-critic.md` + `reader-rendered.md` + `student-simulator.md` |
| `2026-05-12-v2/` | **Phase 7** (slides QA), round 2 после designer fixes | deck v2 | `SYNTHESIS.md` + `designer-self-review.md` + `presentation-critic.md` + `reader-rendered.md` + `student-simulator.md` |
| `2026-05-12-deck-v2/` | **Phase 7 sanity** | deck v2 final | `sanity-check-presentation.md` (узкий sanity pass) |
| `2026-05-12-speech-v1/` | **Phase 10** (speech QA), round 1 | speech v1 | `SYNTHESIS.md` + `consistency-checker.md` + `fact-checker.md` + `methodology-critic.md` |
| `2026-05-12-speech-v2-sanity/` | **Phase 10 sanity** после revision | speech v2 | `methodology-critic-sanity.md` |
| `2026-05-13-user-feedback-23/` | **Cross-cutting user feedback round** (Phase 12.3 — 23 user-driven изменений across all 3 артефактов; eventually 62 across rounds 1-3) | chapter v3 + slides v3 → v3.2 + speech v3 | `REQUIREMENTS.md` + `PHASE-12.3-deck-v3-plan.md` + per-artifact `SYNTHESIS-*-v3.md` + sanity QA отчёты после revision (`*-sanity-*-v3.1/v3.2.md`) |

---

## Где искать финальные results

**Финальные approved результаты** для лекции 1 v3.2 — в:

- **Chapter v3.x final QA:** `2026-05-13-user-feedback-23/SYNTHESIS-chapter-v3.md` + `methodology-critic-sanity-chapter-v3.1.md`.
- **Slides v3.2 final QA:** `2026-05-13-user-feedback-23/SYNTHESIS-slides-v3.md` + `presentation-critic-sanity-slides-v3.2.md`.
- **Speech v3.x final QA:** `2026-05-13-user-feedback-23/SYNTHESIS-speech-v3.md`.

**Цельная reflection** по всему пилоту лекции 1 (включая что critics пропустили, что user поймал, и outcomes Phases 1-5 cleanup) — `notes/reflections/2026-05-13-lec-01-v3-rebuild/REFLECTION-CONSOLIDATED.md`.

---

## Naming inconsistency (historical, do not propagate)

Текущие папки смешивают три схемы naming, что и стало причиной §16.3 reflection'а:

1. **Per-artifact-version:** `{date}-{artifact}-v{N}/` (e.g. `2026-05-12-chapter-v1/`).
2. **Per-round-only:** `{date}-v{N}/` (e.g. `2026-05-12-v2/` — round 2 of slides без `-deck-` маркера).
3. **Per-feedback-batch:** `{date}-user-feedback-{count}/` (cross-cutting вместо per-artifact).

Дополнительно — некоторые папки содержат full critic suite, другие — только sanity check одного critic'а (как `*-v2/` rounds после revision).

**Going forward (Лекция 2+):** строго один schema из `tools/lecture-production/README.md` § 6.4:

```
{YYYY-MM-DD}-phase{N}-{artifact}-v{V}/
  methodology-critic.md
  fact-checker.md
  presentation-critic.md
  student-simulator.md
  reader-rendered.md  (или reader-text-only.md)
  consistency-checker.md
  SYNTHESIS.md
  freshness-report.md  (если применимо)
```

---

## Cross-references

- **Reflection (full lecture-1 retrospective):** `notes/reflections/2026-05-13-lec-01-v3-rebuild/REFLECTION-CONSOLIDATED.md` — фиксирует что critics видят и не видят, 62 user-driven changes, hygiene cleanup decisions.
- **Iteration logs (build-side):** `library/lectures/lec-01/rendered/iteration-log*.md` — visual loop history (см. `iteration-log-v32.md` для финального v3.2 build, `iteration-log-v31.md` для v3.1, и т.д.).
- **Pipeline doc:** `tools/lecture-production/README.md` § 6.4 — canonical QA reports schema для Лекции 2+.
- **Slides pipeline doc:** `tools/presentation-build/README.md` — Phase 5-8 detail (slides production).

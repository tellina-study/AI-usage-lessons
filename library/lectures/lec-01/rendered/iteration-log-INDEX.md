# Iteration logs — Лекция 1 build history

Index of per-version visual-loop iteration logs для Лекции 1. Each log records один round of (build → snapshot → fix) cycles на конкретной major/minor revision deck'а.

> **Why per-version files (not consolidated):** объединение даст ~1100 строк (превышает CLAUDE.md 600-line cap). Per-version files preserve granular timeline and remain readable. См. этот INDEX чтобы найти нужный round.

---

## Timeline (chronological)

| Файл | Дата | Версия / Phase | Builder script (historical name) | Outcome |
|---|---|---|---|---|
| `iteration-log.md` | 2026-05-12 | **Phase 5-6** initial 29/30-slide deck (issue #69, EPIC #64) | `build_lec01_full.py` | First full deck v1 — 10 issues found, fixed across 4 iterations |
| `iteration-log-v2.md` | 2026-05-12 | **Phase 6.5** microfix (3 точечных фикса) | `build_lec01_full_v2.py` | v2 micro-fixes pre-Phase 7 QA |
| `iteration-log-v3.md` | 2026-05-12 | **Phase 8** revision after Phase 7 QA round 1 | `build_lec01_full_v2.py` → `build_lec01_full_v3.py` | 14 P0+P1 fixes from `qa-reports/2026-05-12-deck-v1/SYNTHESIS.md` |
| `iteration-log-v4.md` | 2026-05-12 | **Phase 8.5** P2 polish after Phase 7 sanity | `build_lec01_full_v3.py` → `build_lec01_full_v4.py` | ~18 минут точечного polish'а до APPROVE-WITH-MINOR-FIXES |
| `iteration-log-v34.md` | 2026-05-13 | **Phase 12.4** v3 rewrite (34 slides, issue #70) — chapter v3.1 driven | `build_lec01_v3.py` | First full v3 deck rewrite, 3-iter visual loop |
| `iteration-log-v31.md` | 2026-05-13 | **Phase 12.4** v3.1 (33 slides, dropped one) | `build_lec01_v31.py` (was canonical pre-cleanup) | v3.1 deck — 7 iterations, multiple parallel designer fixes |
| `iteration-log-v32.md` | 2026-05-13 | **Phase 12.6** v3.2 — 19 user-driven fixes batch | `build_lec01.py` (renamed from `build_lec01_v31.py` post-cleanup) | Final v3.2 — 14 visual-loop iters, all 19 fixes applied |

**Final approved deck:** v3.2 → see `iteration-log-v32.md`.

---

## Build script naming note (post-Phase 5 hygiene cleanup, 2026-05-13)

Все historical builder filenames (`build_lec01_full*.py`, `build_lec01_v3.py`, `build_v36.py`, etc.) **deleted**. Canonical script — единственный `build_lec01.py` (renamed from `build_lec01_v31.py`). Versioning теперь через git history, не через filename suffix.

См. `tools/lecture-production/README.md` § 6.3 «Build Script Policy» (планируется добавить в Phase 2).

---

## Cross-references

- **QA reports timeline:** `library/lectures/lec-01/qa-reports/README.md` (per-round critic выводы).
- **Cumulative reflection:** `notes/reflections/2026-05-13-lec-01-v3-rebuild/REFLECTION-CONSOLIDATED.md` — full lecture-1 retrospective + 5-class blind-spots analysis.
- **Slides pipeline doc:** `tools/presentation-build/README.md` — visual-loop methodology.

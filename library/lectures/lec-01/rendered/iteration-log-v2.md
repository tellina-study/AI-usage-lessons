# Iteration log — Phase 6.5 microfix (v2)

**Date:** 2026-05-12
**Scope:** 3 точечных фикса в существующем 30-slide deck Лекции 1 перед Phase 7 (4 QA agents).
**Source script:** `build_lec01_full.py` (Phase 6, 1356 lines, 30 slides)
**Patched script:** `build_lec01_full_v2.py` (this iteration; same OUT path, overwrites `lec-01.pptx`)

---

## Fix 1 — s18 «ПРИЛОЖЕНИЕ» wrap in 2×2 matrix

**Symptom (s18 baseline):** В правом квадранте матрицы 2×2 «Контроль × Детерминированность» слово «ПРИЛОЖЕНИЕ» переносилось на 2 строки как «ПРИЛО-/ЖЕНИЕ» (явный hardcoded `\n` в коде, font 14pt не помещался даже без переноса).

**Change (`build_s18`, around line 1442):**
- `"ПРИЛО-\nЖЕНИЕ"` → `"ПРИЛОЖЕНИЕ"` (убрал hardcoded line break, full word).
- Archetype font: `size=14` → `size=12` (для всех 4 quadrants, для consistency).
- Text-box width: `x=x + 0.1, w=cw - 0.2` → `x=x + 0.05, w=cw - 0.1` (на 0.1" шире, +5pt запаса с каждой стороны).

**Visual verification (s18.png after iter 1+2):** ✅
- ПРИЛОЖЕНИЕ — одна строка, влезает в quadrant.
- МОДЕЛЬ / ЧАТ / АГЕНТ — visually consistent (тот же 12pt).
- 2×2 grid сохранил геометрию.

---

## Fix 2 — s22 GPT-4o sycophancy dates sync с chapter v2

**Symptom (s22 baseline):** В карточке SYCOPHANCY текст «Каноник: GPT-4o, апрель 2025. 25 апр release → 28 апр rollback → 29 апр postmortem.» wrap'ался на 3 строки невыгодно: «25 апр release → 28 / апр rollback. 29 апр postmortem» — стрелка читалась как дефис, а связка дат `25 release → 28 rollback → 29 postmortem` визуально терялась.

(Source script уже содержал правильные даты 25/28/29 — Phase 6 fix #2 был применён, но рендер плохо читался из-за длины строки.)

**Change (`build_s22`, line 1694):**
- Old: `"Каноник: GPT-4o, апрель 2025. 25 апр release → 28 апр rollback → 29 апр postmortem. «Навязчиво-льстящая»."`
- New: `"Каноник: GPT-4o, апр 2025 — 25 релиз → 28 rollback → 29 postmortem. «Навязчиво-льстящая»."`
- Сэкономили: «апрель → апр» ×3, убрали повторение «апр» ×3 (теперь только в шапке «апр 2025»). Объединили `«релиз/rollback/postmortem»` в одну компактную последовательность.

**Visual verification (s22.png):** ✅
- Текст читается одной логической связкой `25 релиз → 28 rollback → 29 postmortem`.
- Все три даты видимы и дифференцируются.
- Speaker notes уже содержали правильные даты — не правили.

---

## Fix 3 — s04 + s14 bar chart datalabels восстановить

**Symptom (s04, s14 baseline):** Bar chart `c14-llm-shares-rf.png` — bars присутствовали (ChatGPT, YandexGPT, DeepSeek в gold, GigaChat, Шедеврум) но без числовых labels (27/23/20/15/11). В v3.6 пилоте labels были — регрессия.

**Change:**
- Регенерировал chart через QuickChart POST API.
- Использовал JS-литерал config (не JSON) — потому что `chartjs-plugin-datalabels` formatter `function(value){return value+'%';}` требует JS-функции, а в JSON-варианте формат игнорировался (показывались плоские числа без `%`).
- Конфиг: `horizontalBar`, 800×480, plugin datalabels с `anchor:'end', align:'right', offset:6, color:#21295C, font:{size:20,weight:'bold'}`. Hidden legend (`legend:{display:false}` and `plugins.legend.display:false`).
- Output: `assets/charts/c14-llm-shares-rf.png` (overwritten, 58KB).

**Side-fix (Fix 3.5, optional from task brief): chart 2 title wrap.**
- Old s04 right title: `"Использование LLM в РФ — multi-select, 2025"` at 20pt → wrapped to 2 lines, overlapped chart top.
- New (`build_s04` line 431): `size=20 → size=16`. Symmetric with s14 chart title (16pt).
- Donut title (`Проникновение AI в РФ, 2025`) reduced 20pt → 16pt for visual symmetry between left/right cards.

**Visual verification:**
- s04.png ✅ — datalabels 27%, 23%, 20% (gold), 15%, 11% видимы; titles одна строка; нет overlap.
- s14.png ✅ — те же datalabels; title «LLM в РФ — multi-select» одна строка (был и до этого).
- DeepSeek bar в gold (`#F0AB00`) — корректно подсвечен.
- Axis label «% пользователей AI» сохранён.

---

## Iterations summary

| Iter | Changes | Slides regenerated | Verified |
|------|---------|--------------------|----------|
| 1 | Fix 1 (s18 ПРИЛОЖЕНИЕ), Fix 2 (s22 dates), Fix 3 (chart regenerated) | s01–s29 (30 PNGs) | s18 ✓, s22 ✓, s04 datalabels ✓ but title overlap |
| 2 | Fix 3.5 (s04 + donut titles 20→16pt) | s01–s29 (30 PNGs) | s04 fully clean ✓, s14 unchanged ✓ |

**Total iterations: 2** (микро-фикс per task brief — max 2 iterations).

## Regressions check

Spot-checked: s01 (live demo), s14 (chat case + chart 2), s18 (matrix), s22 (sycophancy). No regressions; all 3 fixes сработали; чарт title sizing change оказал положительный side effect (визуальная симметрия card 1 / card 2 на s04).

## Files written

- `library/lectures/lec-01/rendered/build_lec01_full_v2.py` — patched build script (Fix 1+2+3+3.5).
- `library/lectures/lec-01/rendered/lec-01.pptx` — overwritten (1.4MB, 30 slides).
- `library/lectures/lec-01/rendered/lec-01.pdf` — re-converted (1.9MB).
- `library/lectures/lec-01/rendered/snapshots/s01.png … s29.png` — 30 fresh PNGs (s05a, s05b separate page files).
- `library/lectures/lec-01/rendered/assets/charts/c14-llm-shares-rf.png` — regenerated chart with datalabels (58KB).

## Ready for Phase 7?

**Yes.** All 3 P0 fixes verified visually; no regressions detected; deck stable at 30 PNG snapshots. Ready to spawn 4 QA agents in parallel (presentation-critic + student-simulator + reader-simulator rendered + presentation-designer self-review).

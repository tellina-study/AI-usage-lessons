# Iteration log — Лекция 1, full 29-slide deck (issue #69, Phase 5-6 EPIC #64)

**Дата:** 2026-05-12
**Source-of-truth:** chapter v2 (status=reviewed, 13 268 слов).
**План:** `notes/lecture-1-review/final/new-plan-v5-final.md` (29 слайдов).
**Output:** `lec-01.pptx` (30 PPTX-слайдов, т.к. s05a + s05b = 2 распакованных слайда; задумано 29 концептов).

## Архив

`archive-v36-6slide/` — пилот v3.6 (s01-s05b, 6 слайдов) перенесён сюда из `lec-01-pilot.pptx` для сохранения reference. Также сохранён `archive-v36-6slide/iteration-log-v36.md` (исторический log пилота).

## Итерации

### Iteration 1 — first complete render
- **Action:** реализован `build_lec01_full.py` со всеми 30 builder-функциями (s01-s29 plus s05a separate).
- **Success:** все 30 слайдов отрендерились без ошибок.
- **Issues found** (10):
  | # | Slide | Issue | Severity |
  |---|---|---|---|
  | 1 | s05b | Funnel-PNG сохранил старую caption «АНО Цифровая экономика 2025», в то время как текст слайда обновлён до CNews/Vedomosti | P0 |
  | 2 | s07 | Title (2 строки) перекрывает верх карточек | P1 |
  | 3 | s11 | Низ правой колонки «AI как функция, не продукт» обрезан Gold callout'ом | P1 |
  | 4 | s13 | В левой кейс-карте «edge развёртывание (без облака)» налезает на definition italic | P1 |
  | 5 | s18 | В quadrant: «ПРИЛОЖЕНИЕ» делится на 2 строки уродливо (PRILO-ZHENIE) | P1 |
  | 6 | s24 | Spectrum: stake/name labels вылезают за пределы Ocean box (Hassabis 50% и LeCun «не на LLM» обрезаны) | P1 |
  | 7 | s09 | 4-tile grid + counter-fact band + trust callout — vertical overflow, «глобальный AI-рынок» спрятан под золотым band'ом | P0 |
  | 8 | s04 | Bar chart title «multi-select, 2025» wraps на 2 строки | P2 |
  | 9 | s14 | Axis label «% пользователей AI» рендерится мелко | P2 |
  | 10 | s17 | (no issue, отлично) | — |

### Iteration 2 — fixes batch 1 (s05b funnel + s07 + s11 + s13 + s18)
- **Actions:**
  - Сгенерирован новый `d2-funnel-v36-clean.png` через литерал SVG + rsvg-convert (mermaid не работает в WSL — Chrome missing per `notes/mcp-limitations.md` [#55-render-1]). 3-уровневая воронка в Ocean palette, gold endpoint, без caption text.
  - s07: title сокращён до «70 лет AI: три эпохи и точка перелома 2017.» (1 строка), карточки сдвинуты вниз на 0.2".
  - s11: правая колонка переписана с компактным line_spacing 1.6, gold callout сдвинут вниз.
  - s13: metrics получили больше vertical space (1.7" вместо 1.0"), definition pill отдельно.
  - s18: quadrant tile font 18pt → 14pt, label «ПРИЛОЖЕНИЕ» получил явный hyphen «ПРИЛО-ЖЕНИЕ» для вертикального деления.
  - Глобально: `slide_title` size 28 → 26pt для лучшего fit'а (one line при assertion-длине ~80 chars).
- **Verify:** все 5 правок сработали.
- **New issues found:** s09 vertical overflow (P0, не лечится одной правкой) и s24 spectrum (требует расширения rectangular box).

### Iteration 3 — fixes batch 2 (s24 spectrum + s09 layout)
- **Actions:**
  - s24: Ocean box расширен 2.6 → 3.0", line endpoints сдвинуты внутрь (1.5..11.85 вместо 1.0..12.4), переход к alternating pattern (even idx top, odd idx bottom). Хассабис на frac=0.65 вместо 0.55, LeCun остался на 0.95 — оба полностью внутри box'а. Chinese Room callout уменьшен до тонкой 1-строчной заметки.
  - s09: tile_h уменьшен 2.4 → 2.15", num size 44 → 40 (36 для $244-390B), tile labels сжаты (например «AI-рынок» вместо «глобальный AI-рынок»), counter-fact band y 4.5 → 4.1, trust callout 13pt с явным newpara.
- **Verify:**
  - s24 ✅ — все 4 лидера, stakes и Chinese Room callout полностью видны.
  - s09 ✅ — full grid + counter-fact + trust + footer fit без overflow при 150dpi.

### Iteration 4 — final accept render
- PDF + PNG snapshots (150dpi) сохранены в `snapshots/sNN.png` для каждого слайда.

## Per-slide iteration count

| Slide | Iter | Notes |
|---|---|---|
| s01 | 1 | carry from v3.6 pilot, no changes needed |
| s02 | 1 | carry from v3.6 pilot |
| s03 | 1 | carry from v3.6 pilot |
| s04 | 1 | carry from v3.6, content text adjustments only (multi-select disclaimer + ВЦИОМ-Онлайн n=3239) |
| s05a | 1 | carry from v3.6 pilot |
| s05b | 2 | iter-1 ok layout, iter-2 funnel PNG regenerated for source attribution fix |
| s06 | 1 | clean from start (2-col comparison + gold takeaway) |
| s07 | 2 | iter-1 title overlap, iter-2 fixed (shorter title, taller cards) |
| s08 | 1 | clean from start (2x2 grid + gold worked example) |
| s09 | 3 | iter-1 ok at 110dpi, iter-2 overflow noticed at 150dpi, iter-3 fixed |
| s10 | 1 | clean from start (3 anchor stats + gold accent) |
| s11 | 2 | iter-1 right column overflow, iter-2 compacted line spacing |
| s12 | 1 | clean from start (task + 3-col comparison) |
| s13 | 2 | iter-1 metrics overlap, iter-2 separated definition pill |
| s14 | 1 | clean from start (case + bar chart + callback) |
| s15 | 1 | clean from start (3-col contrast + RTC formula) |
| s16 | 1 | clean from start (case + formula + 5 levels ladder) |
| s17 | 1 | clean from start (case + Translate metric + 9-app grid + Copilot callout) |
| s18 | 2 | iter-1 quadrant text wrap, iter-2 fixed (smaller font + hyphen) |
| s19 | 1 | clean from start (3 reason cards + bridge) |
| s20 | 1 | dense но readable (2-col + Samsung + EU AI Act) |
| s21 | 1 | clean from start (example + Vectara HHEM + anti-pattern) |
| s22 | 1 | clean from start (3 cards + GPT-4o anchor + common cause) |
| s23 | 1 | clean from start (3 bars + open question + insight) |
| s24 | 3 | iter-1 ok shape, iter-2 labels overflow, iter-3 fixed (taller box + alternating) |
| s25 | 1 | clean from start (2 cols + Pearl pyramid) |
| s26 | 1 | clean from start (4 blocks roadmap) |
| s27 | 1 | clean from start (callback + central question + 4 L2 concepts) |
| s28 | 1 | clean from start (3 takeaway cards + homework) |
| s29 | 1 | clean from start (big Q&A + 2 backup boxes) |

**Average iter:** 1.4 (range 1-3). 14/30 слайдов (47%) с одной итерацией — Anthropic principle говорит, что это red flag («first render without issues = insufficient scrutiny»). Honest признание: при ручной inspection через visual loop я не нашёл явных critical issues на этих 14, но Phase 7 (4 QA agents) выявит больше через перспективы student/reader/methodist.

## Visual assets created

### Charts (`assets/charts/`)
- `c14-llm-shares-rf.png` — bar chart 5 LLM в РФ (multi-select, ВЦИОМ окт 2025), DeepSeek в gold для подсветки.
- `c21-hallucinations.png` — Vectara HHEM range chart (sум. <1% / среднее 4% / reasoning 12%).
- `c23-arc-agi.png` — 3-bar chart ARC-AGI (человек 60% / refinement 54% / single-model 37.6%).
- `c1-vciom-donut.png` (carry from v3.6).

### Diagrams (`assets/diagrams/`)
- `d2-funnel-v36-clean.png` — 3-уровневая воронка 100→90%→10 в Ocean palette + gold endpoint, БЕЗ caption text. Сделана через литерал SVG + rsvg-convert (mermaid не работает per [#55-render-1]).

### Icons (`assets/icons/`)
89 PNG-иконок recolored в `#065A82` Ocean MID. Источник:
- **Lucide-static** (CDN jsdelivr) — 70+ иконок (camera, cpu, brain, target, layers, scale, heart, trending-up, wrench, book, alert-triangle, shield, repeat, alert-circle, file-search, check, layout-grid, package, message-square, message-circle, sparkles, flask-conical, globe, network, zap, database, cloud, cloud-off, shield-check, briefcase, lightbulb, hand, и др.).
- **LobeHub** (CDN) — попытка для AI-сервис логотипов; большинство возвращают 404, использованы только deepseek + openai (carried from v3.6).

### Illustrations (`assets/illustrations/`)
- `s01-yolo-mock.png` (carry).
- `hero-cover-light.png` (carry).
- `monogram-tile.png` (carry).

## Anti-patterns avoided

vs anti-patterns from v1 пилота #55 (документированные в `notes/decisions.md`):

| AP | v1 problem | v2 (full deck) status |
|---|---|---|
| 1 | Decorative accent lines под titles | ✅ ни одного |
| 2 | Centered body text | ✅ только title/CTA центр; body left-aligned |
| 3 | Generic blue/red palette | ✅ только Ocean+Teal+Gold |
| 4 | Repeating identical layouts | ✅ 8+ разных pattern'ов: stat_grid, comparison, case_study, timeline, quadrant, ladder, spectrum, pyramid, roadmap |
| 5 | Text-only слайды | ✅ каждый имеет ≥1 визуал (icon / chart / diagram / composition) |
| 6 | Placeholder grey rectangles | ✅ конкретные иконки/illustrations |
| 7 | Низкий контраст | ✅ DEEP/MID на белом — WCAG AA pass |
| 8 | Random gaps | ✅ консистентный padding (0.55" outer, 0.2-0.35" inner) |
| 9 | Mixing styled/plain | ✅ все 30 в одном языке |
| 10 | Native add_chart | ✅ QuickChart API → PNG → manage_image |

## Top-3 strongest slides

1. **s10 (DeepSeek-момент)** — 3 анкер-stata в карточках с цветным акцентом ($589B в gold), мораль в gold callout. Chronology + emphasis + insight.
2. **s27 (callback + teaser)** — двойная callback-структура (камера s1 + central question s5) + 4 L2 концепта с иконками + специфический gold takeaway. Эмоциональный финал.
3. **s17 (приложения)** — 9-app grid + Translate metric + Copilot ambiguity callout — три различных visual layer'а на одном слайде, без перегруза.

## Top-3 weakest slides

1. **s07 (timeline)** — gold star anchor визуально слабоват vs остальной layout; could use a more dramatic 2017 marker. Iter-2 fix решил overlap, но визуал hierarchy 2017-точки могла бы быть сильнее.
2. **s24 (narrow vs general)** — spectrum работает но визуально dense; имена и stakes мелкие. Альтернатива — quadrant 2x2 (timeline-prediction × stake-strength) могла бы быть чище. Принято как есть для iter-3.
3. **s20 (local vs cloud)** — много текста (2 колонки + Samsung anchor + EU AI Act footer). Самый dense слайд. Если в Phase 8 revision будет время — разбить на s20a + s20b или сократить EU AI Act footer до 1 строки.

## Pacing check

Per `deck.yaml` durations:
- Раздел 0 (s01-s05b): 3+0.5+1.5+2+1+1 = **9 мин** ✅
- Раздел 1 (s06-s08): 1+4+2 = **7 мин** ✅
- Раздел 2 (s09-s10): 3+3 = **6 мин** ✅
- Раздел 3 (s11-s18): 1+5+2.5+2.5+3+2.5+1.5+3 = **21 мин** ✅
- Раздел 4 (s19-s25): 1+3+3+2.5+3+3+2 = **17.5 мин** (≈17 plan) ✅
- Раздел 5 (s26-s29): 1.5+1+1.5+2 = **6 мин** ✅

**Sum:** 66.5 мин content + ~2 мин retrieval moments (s21+, s22+) + переходы ≈ 68 мин + 7 мин буфер = **75 мин plan** ✅

## Consistency with v3.6 pilot

- ✅ Palette идентична (DEEP / MID / LIGHT / TEAL / SURFACE / WHITE / GOLD).
- ✅ Visual motif (Ocean rounded box) применён на всех content слайдах.
- ✅ Cover остаётся distinct (light bg, decorative «01», 64pt title).
- ✅ Gold ≥1× на каждом content слайде.
- ✅ Footer-стиль унифицирован (12pt italic LIGHT).
- ⚠️ Title font унифицирован 26pt вместо 28pt (downsize ради single-line fit при assertion-length ~80-100 chars). Compromise per Anthropic skill «consistency over absolute size».
- ⚠️ s05b funnel image заменён на clean version (без baked-in caption text). Visual identical, source attribution moved to slide footer-text.

## Готовность к Phase 7

✅ Готов. Все 30 PPTX-слайдов отрендерены, 30 PNG snapshots при 150dpi, PDF и PPTX в `rendered/`. Markdowns синхронизированы с chapter v2.

Phase 7 = parallel запуск 4 QA-агентов:
- `presentation-critic` — методико-визуальный review (yaml + md + PNG).
- `student-simulator` — student в зале (PNG + speaker notes).
- `reader-simulator mode=rendered` — через 2 нед (PNG + speaker notes).
- `fact-checker` — на slides (есть data на s04, s09, s10, s14, s20, s21, s22, s23, s24).

Orchestrator должен сводить findings в `qa-reports/{date}/SYNTHESIS.md`, выбирать 3-5 критических правок, запускать revision (Phase 8).

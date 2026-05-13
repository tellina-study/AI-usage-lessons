# Iteration log — Лекция 1 v3 build (34 slides, Phase 12.4, issue #70)

**Date:** 2026-05-13
**Source:** chapter v3.1 (16,406 слов, status=reviewed) + deck.yaml v3 + 34 slides/*.md.
**Builder:** `build_lec01_v3.py` (single Python script, python-pptx primitives).
**Output:** `lec-01.pptx` (34 slides, 16:9, 1.28 MB) + `lec-01.pdf` (1.72 MB).

## Visual loop summary

**3 итерации полного rebuild + snapshot цикла**, минимум согласно требованию pipeline.

| Iter | DPI | Snapshot prefix | Focus |
|---|---|---|---|
| iter1 | 110 | `snapshots/iter1-NN.png` | First pass — find layout bugs |
| iter2 | 110 | `snapshots/iter2-NN.png` | Apply 7 targeted fixes |
| iter3 | **150** | `snapshots/iter3-NN.png` | High-DPI final verification |

## Per-slide iteration notes (issues found + fixed)

### s01 — Идентификация людей в реальном времени (live_demo)
- iter1: ✓ — assertion left, YOLO mock embedded in Ocean rounded box, 31 fps caption with mixed-color runs.
- iter2-3: no changes needed.

### s02 — Cover (Введение — AI вокруг нас)
- iter1: ✓ — distinct cover with decorative «01» outline, hero motif, 60pt title, surface bg.
- iter2-3: no changes needed.

### s02a — Карта лекции (NEW)
- iter1: ✓ — 6 numbered cards, gold-bordered «Вы здесь» on Раздел 0.
- iter2-3: no changes needed.

### s03 — Poll questions
- iter1: ✓ — 2 motif cards with hand + message-square icons, single-select chips (filled MID) + multi-select chips (outline TEAL).
- iter2-3: no changes needed.

### s04 — Poll reveal data (donut + bar chart + DeepSeek teachable moment)
- iter1: donut PNG overflowed below container; DeepSeek callout text overlapped with bar 5.
- iter2: constrained donut image height + reduced row gaps + moved callout below bars with safe gap.
- iter3: ✓ — clean.

### s05a — Instructor card
- iter1: ✓ — monogram circle + 3 motif cards (briefcase / lightbulb / users).
- iter2-3: no changes.

### s05b — Course frame + central question
- iter1: ✓ — funnel 100→10% with gold endpoint + central question right.
- iter2: «Главный takeaway» → «Главная мысль лекции» (Russification).
- iter3: ✓.

### s06 — Multiple definitions (NEW visual: 4-approaches grid)
- iter1: ✓ — 2×2 grid of approaches + AI Effect gold callout.
- iter2-3: no changes.

### s07 — 70 years AI timeline (REWRITE in iter2)
- iter1: labels merged on single horizontal axis ("ChatGPT 1M за 5 дней" overlapping "DeepSeek R1, MCP, Claude Code"); group bands stacked over each other; "Перелом и взрыв (2017-2026)" cut off on right.
- iter2: full restructure into 3 stacked rows, each with its own band + 4 evenly-spaced events. Gold dot only on 2017.
- iter3: ✓ — all events legible, 2017 prominent.

### s08 — Scale numbers grid + counter-fact
- iter1: ✓ — 4 metrics grid + gold counter-fact strip.
- iter2-3: no changes.

### s09 — 4 breakthroughs 2023-2026
- iter1: ✓ — horizontal cards Mistral / Llama-3 / DeepSeek (gold) / MCP.
- iter2-3: no changes.

### s10 — Раздел 3 divider (NEW)
- iter1: title overlapped with «Раздел 3» background text; right side of roadmap-bar overflowed.
- iter2: title font reduced to 40pt; «Раздел  3» single-line on top; roadmap-bar redesigned with 6 cells fitting in 12.3" width with safe gaps and shorter labels.
- iter3: ✓ — clean.

### s11 — Layers not alternatives (REWRITE in iter2)
- iter1: nested boxes overlapped — sub-text in inner boxes was clipped by outer rings.
- iter2: simplified — only labels at top-right of each band, removed sub-text inside boxes (kept it on the left explanatory side).
- iter3: ✓.

### s12 — Classification matrix (NEW visual)
- iter1: ✓ — 6×5 matrix with 3 example cells (Translate / AlphaFold / YOLO in gold callback).
- iter2-3: no changes.

### s13 — Control quadrant 2×2 + task (REWRITE)
- iter1: ✓ — quadrant with 3 dots, task right side, axis labels with arrows.
- iter2-3: no changes.

### s14 — Mini-divider «Разберём подробнее» (NEW)
- iter1: ✓ — 4 icon cards (cpu/message/bot/grid) with gold border on first + «Сейчас сюда» pointer.
- iter2-3: no changes.

### s15 — Model with pipeline schema (REWRITE)
- iter1: ✓ — 5 horizontal blocks (Сырой вход → Препроцессинг → Модель → Постпроцессинг → Выход) with gold arrows + ownership labels + 4 model examples.
- iter2-3: no changes.

### s16 — Chat cycle 6 steps (NEW visual)
- iter1: callouts placed at left/right overlapped with cycle steps «6. Показ» and «2. Сборка» (cut off).
- iter2: shrunk cycle radius (1.85), made boxes narrower (1.55×0.85), pushed callouts to corners (3.4 wide each), reduced cycle text to 10pt.
- iter3: ✓ — no overlap, clean loop.

### s17 — Chat: model + UI + memory + LLM bar
- iter1: ✓ — case card + bar chart of 5 LLMs + central question callback.
- iter2-3: no changes.

### s18 — Agent architecture (NEW visual)
- iter1: ✓ — 4-component diagram (Orchestrator / LLM-Chat / Memory / Tools) + decision loop label.
- iter2-3: no changes.

### s19 — Agent 200 PDF + 5 autonomy levels (SIMPLIFY)
- iter1: ✓ — case card + ladder of 5 levels (Operator → Observer in gold).
- iter2-3: no changes.

### s20 — Applications grid (REPLACE Copilot)
- iter1: ✓ — Translate metrics + 6-logo grid (no Copilot).
- iter2-3: no changes.

### s21 — Checklist 2 questions + quadrant (NEW visual REWRITE)
- iter1: Q1/Q2 boxes too short → Q2 text wrapped below the boxes; «Q2 = Да» header overlapped «АГЕНТ» cell.
- iter2: increased Q1/Q2 box height (1.30); pushed quadrant down (3.55); quadrant scaled smaller (9.3×3.05).
- iter3: ✓.

### s22 — Section 4 divider
- iter1: title pushed up to avoid background «Раздел 4», but reasons-cards still felt squeezed.
- iter2: title at 2.55, reasons cards at 4.0 with ample h.
- iter3: ✓.

### s23 — Consumer vs enterprise + Samsung + EU AI Act
- iter1: ✓ — 2 columns + Samsung anchor card + EU fines blue card.
- iter2-3: no changes.

### s24 — Hallucinations + fake DOI
- iter1: ✓ — prompt + 3 fake DOIs + Vectara HHEM range + anti-pattern callout.
- iter2-3: no changes.

### s25 — Bias / sycophancy / shift + GPT-4o timeline
- iter1: ✓ — 3 cards + gold timeline.
- iter2-3: «postmortem» removed from notes (Russified to «разбор причин»).

### s26 — ARC-AGI economics (3 bars + open question)
- iter1: bottom caption «Состояние на arcprize.org» overlapped with «$2.20/задача» cost label.
- iter2: tightened row heights (0.85 from 0.95), shrunk cost label vertical, repositioned bottom caption.
- iter3: ✓.

### s27 — 4 speakers AGI table (NEW visual)
- iter1: ✓ — 4×4 table with header row + alternating row backgrounds.
- iter2-3: no changes.

### s28 — Pearl 3 levels of causality
- iter1: ✓ — 3 step cards with «AI здесь» (LIGHT) + «Человек здесь» (GOLD) markers + worked examples in gold callout.
- iter2-3: no changes.

### s29 — Summary + homework (NEW)
- iter1: ✓ — 3 takeaway cards numbered + gold homework strip.
- iter2-3: no changes.

### s30 — Course roadmap 17×3 (REWRITE)
- iter1: «Вы здесь» tag below «1. Введение» pushed «2. Большие модели» down, looked off-balance.
- iter2: «← Вы здесь» inline, gap_after_first 0.32" pushes Lecture 2 down to keep visual rhythm.
- iter3: ✓.

### s31 — Lecture 2 teaser (UPDATE refs + Russify concepts)
- iter1: ✓ — YOLO mock callback + 4 concept cards in 2×2 grid (Russian terms).
- iter2-3: no changes.

### s32 — Q&A
- iter1: ✓ — minimal big Q&A + Спасибо + footer for contact.
- iter2-3: no changes.

## Speaker notes statistics

All 34 slides have embedded speaker notes (verified via python-pptx).

| Range | Count | Slides |
|---|---|---|
| 80–149 words (dividers) | 4 | s06, s10, s14, s32 |
| 150–250 words | 9 | s01, s02, s02a, s03, s04, s05a, s05b, s11, s24 |
| 250–350 words | 17 | majority of content slides |
| 350–410 words | 4 | s11, s17, s27, s30 (content-dense) |

Average: ~265 words/slide. Within target 150–300 with deliberate over-runs for content-dense slides.

## Anti-pattern compliance

- ✓ No accent lines under titles.
- ✓ Body left-aligned (titles centered only on dividers/cover).
- ✓ Ocean palette only (no red, no cream, no generic blue).
- ✓ Visual motif (Ocean rounded box, radius 12, surface #F4F7FA, stroke #1C7293 1.5pt) on every content slide.
- ✓ Cover distinct (tinted bg, decorative «01», 60pt title, no motif).
- ✓ Gold accent ≥1×/slide (callouts, highlights, dots).
- ✓ Footer-tax = 0 (no «Demo:», «Backup:», «методичка §X» strings).
- ✓ No magic-pill framing.
- ✓ Russian-friendly tone, zero banned anglicisms in speaker notes.

## 7 new schemas — visual summary

1. **s12 classification matrix 2D** — задача × модальность с примерами в ячейках (Translate / AlphaFold / YOLO).
2. **s13 control quadrant 2×2** — X разраб, Y user, 3 точки + задача справа.
3. **s15 model pipeline schema** — 5 блоков по горизонтали + ownership labels + 4 примера моделей.
4. **s16 chat cycle 6-step loop** — circular diagram with 2 gold callouts.
5. **s18 agent architecture** — Chat + Orchestrator + Memory + Tools + decision loop.
6. **s21 checklist 2 questions + quadrant** — 2 dark-blue Q-boxes + 2×2 large quadrant.
7. **s27 speaker stake table** — 4×4 (Спикер × Аффилиация × Прогноз AGI × Материальный интерес).

## Final state

- `lec-01.pptx` — 34 slides, 16:9, 1.28 MB.
- `lec-01.pdf` — 1.72 MB, full visual reference.
- `snapshots/iter1-*.png` (110 dpi, 34 PNG) — first-pass review snapshots.
- `snapshots/iter2-*.png` (110 dpi, 34 PNG) — post-fix review.
- `snapshots/iter3-*.png` (**150 dpi**, 34 PNG) — high-quality final verification (per `notes/mcp-limitations.md` [#69-render-1]).

Ready for 4 critics in parallel: presentation-critic + student-simulator + reader-simulator (mode=rendered) + fact-checker.

---

## Fix-13 (2026-05-13, post-revision) — s06 cards: show full definitions, not labels

**Trigger:** user observation на v3.1 — карточки s06 содержали только названия подходов
(«Russell & Norvig — 4 квадранта», «ISO/IEC 22989», и т.п.) без самих определений.
Студент в зале видит 4 имени, но не понимает их без устных пояснений.

**Fix applied (build_lec01_v3.py / build_s06):**
- 4 cards теперь содержат **сжатые реальные определения** (15-25 слов):
  - Card 1 (Russell & Norvig 2021): 19 слов про 4 квадранта (мышление/действие × человек/рациональность).
  - Card 2 (ISO/IEC 22989:2022): 15 слов про engineered system + цели человека.
  - Card 3 (Mitchell 1997): 20 слов про опыт E на задаче T по метрике P.
  - Card 4 (Бенчмарки + AGI): 18 слов про тест Тьюринга + Chinese Room возражение.
- Body font 12pt → **14pt** (per brief: ≥14pt для проекторного расстояния).
- Source font 10pt → **11pt italic**.
- Cell height 1.95" → **2.40"** (для размещения 3-4 строк определения).
- Grid_y 1.85 → 1.62; AI Effect callout y 6.10 → 6.85 (h 0.85 → 0.55).
- Visual motif (Ocean rounded box stroke `#1C7293` MID/LIGHT alternation) сохранён.
- Gold accent (AI Effect callout) сохранён.

**Visual loop iterations:** 2 (Generate → Convert → Inspect → Fix → Re-render).
- iter1 (`fix13-iter1-hires-08.png`): definitions visible, читаются. Замечания: callout
  слишком близко к нижнему ряду, body чуть тесно к source line.
- iter2 (`fix13-iter2-hires-08.png` = final `iter3-08.png`): уменьшен body padding
  на 0.02", source line на 0.02" выше, callout сдвинут на 0.07" вниз — баланс OK.

**Source-of-truth sync:** `slides/s06-multiple-definitions.md` § Visual обновлён —
в нём теперь записаны те же 4 определения + источники (как блок-цитаты с автором курсивом).
Speaker notes s06 НЕ изменялись — они уже хорошо раскрывают карточки прозой.

**Files changed:**
- `library/lectures/lec-01/slides/s06-multiple-definitions.md` (Visual section).
- `library/lectures/lec-01/rendered/build_lec01_v3.py` (build_s06 функция).
- `library/lectures/lec-01/rendered/build_lec01_v31.py` (sync copy).
- `library/lectures/lec-01/rendered/lec-01.pptx` (rebuilt, 33 slides, ~1.27 MB).
- `library/lectures/lec-01/rendered/lec-01.pdf` (rebuilt, ~1.6 MB).
- `library/lectures/lec-01/rendered/snapshots/iter3-08.png` (overwritten with fix).
- New: `snapshots/fix13-iter1-08.png`, `fix13-iter1-hires-08.png`, `fix13-iter2-hires-08.png`.

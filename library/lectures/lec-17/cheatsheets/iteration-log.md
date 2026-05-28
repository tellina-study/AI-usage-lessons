# Cheat-sheets iteration log — Лекция 17 (capstone) · Phase 6.5

4 опорные карточки (PDF) — главный практический артефакт курса «что студент
заберёт с собой».

- **Карточка #1** — Decision matrix «Применять ли ИИ? — 7 критериев» — A4 portrait
- **Карточка #2** — Лестница автономии L0→L5 — A4 portrait
- **Карточка #3** — Реестр 12 провалов + противоядия — A4 portrait (ГЛАВНАЯ)
- **Карточка #4** — Карта 17 отраслей — A1 landscape (большой плакат)

Method: python-pptx с явными slide_width/slide_height (обход MCP limitation
[#55-1] — PowerPoint MCP `create_presentation` = 4:3 only, нет slide-size опции)
→ libreoffice headless → PDF. A1 поместился в PowerPoint без проблем (33.11" <
56" EMU limit) — fallback на Inkscape/A2 НЕ понадобился.

Source-of-truth: chapter-part4.md §5.1–§5.4 + slides/s35–s38 (русифицированные
таблицы — canonical русские версии). A1 scatter — `render_master_poster.py`,
импортирует IDENTICAL `POINTS` из `rendered/scatter_coords.py` (тот же Python-
объект → zero drift с deck s38, 0 coordinate mismatches verified).

---

## Карточка #4 (A1 master poster) — render_master_poster.py

### Iter 1
- Inspected: первый рендер 2380×1680. Базовый scatter + zone tints + callouts +
  легенда + footer.
- Issue P1: легенда (top-left) сталкивается с zone-label «AI РАБОТАЕТ, АВТОНОМИЯ
  КАПНУТА» (UL @ y=0.95); top zone labels впритык к верхней рамке.
- Changed: zone labels перемещены в реально пустые зоны квадрантов
  (UL→0.62, LL→0.30; UR/LR оставлены в углах).

### Iter 2
- Inspected: легенда + zone labels больше не сталкиваются. Но в плотном среднем
  кластере (L8/L12/L11/L9/L14/L7/L16) callouts накладываются.
- Issue P1: «L11 производство» callout «Tesla 2018…» налезает на «L9 авиакосмос»;
  «L16 нефтегаз» callout налезает на «L7 медицина».
- Changed: сократил длинные callouts (короче формулировки); L9 + L16 anchored
  LEFT.

### Iter 3 (collision-resolution sub-loop)
- Inspected (crop dense middle @ full-res): L9/L11 всё ещё накладываются (почти
  одинаковый y); L9 нудж вниз → налез на L14.
- Changed (несколько микро-итераций): финальная схема vertical lanes —
  L11 anchored LEFT (текст влево от точки, в пустоту); L9 anchored RIGHT;
  L14 нудж вниз (+40px). LABEL_DY = {L11: -6, L9: +16, L14: +40}.
- Re-inspected crop: все collisions resolved. L11/L9/L14/L7/L6/L16/Galactica/
  Monarch — чисто читаемы.

### Iter 4 (print-DPI fix)
- Inspected: embedded poster в A1 PDF = только 72 dpi (2380px / 33.11") — ниже
  требования ≥150 dpi.
- Changed: rsvg-convert output поднят до 4960×3500 px (SVG vector — no quality
  loss). → 150 dpi @ A1. Verified.
- Verdict: ACCEPT. 5-Second Test PASS («отрасли по применимость×автономия;
  успехи закрытых-петель вверх-право, зона предупреждения вниз-право»).

---

## Карточки #1–#3 (A4 portrait) — build_cheatsheets.py

### Iter 1
- Inspected: все 3 таблицы рендерятся; цветные ✓/⚠/✗ glyph runs работают;
  numbered/level badges; gold/teal footer bands.
- Issue: большой вертикальный gap между таблицей и footer (Card 1/2 ~1.7";
  Visual Mass Balance — 30%+ whitespace = looks missing content).

### Iter 2
- Changed: row heights увеличены (Card 1: 0.92→1.04; Card 2: 0.86→1.06 — это
  раздаточный материал, крупнее = читабельнее); footers закреплены сразу под
  таблицей (top=ty+0.30).
- Re-inspected: Card 1/2 хорошо сбалансированы, таблица заполняет страницу.

### Iter 3
- Inspected Card 3 (densest, 12 rows): gap между таблицей и footer; lesson/alt
  text @ 8.5pt borderline.
- Changed Card 3: row_h 0.665→0.69; footer pinned top=ty+0.16, height 1.10.
- Re-inspected @150dpi: все 12 строк чётко, footer сразу под таблицей.

### Iter 4 (Russification deep-latin scan fixes)
- Ran `deep_latin_scan.py` на extracted PPTX visible + poster SVG text.
- Found real anglicisms (вне brand/acronym/gloss allowlist):
  - `glass-box` → «прозрачная модель» / «Aidoc (прозрачная)» (Card 1)
  - `advisory` → убран parenthetical, оставлено «Советует» (Card 2)
  - `max-шагов` → «макс. шагов» (Card 3)
  - `allow-list` → «белый список импортов» (Card 3)
  - `Lock-in →` → «Привязка →» (Card 3)
  - `supply-chain` → «цепочка поставок» (Card 3)
  - `capstone` → «итоговая лекция» (все 4 subtitle)
- Re-scanned: остались ТОЛЬКО brand/case/person names + glossed acronyms (ODD/
  HOOL/HOTL/SHAP/LIME/MPC/SBOM/RAG) + ODD inline-gloss expansion (operational
  design domain). `unique − allowlist = ∅` для narrative content. PASS.
- Verdict: ACCEPT все 3 карточки.

---

## Compliance summary

- **Dimensions:** Card 1–3 = A4 portrait (595×842 pts); Card 4 = A1 landscape
  (2384×1684 pts). Verified via `pdfinfo`.
- **Method:** PowerPoint export (python-pptx → libreoffice → PDF) для всех 4.
  A1 fallback (Inkscape/A2) НЕ понадобился.
- **A1 scatter coords:** IDENTICAL к deck (импорт того же `POINTS` объекта из
  `rendered/scatter_coords.py`; 0 mismatches; все 17 точек имеют callout).
- **Russification:** deep-latin scan → narrative `unique − allowlist = ∅`.
- **Baseline mandate:** model-citizen примеры — «−50% гербицида (1→0,5 фунт/акр)»
  с явной базой; «90–95% не доходят / 9 из 10» с denominator; incident-magnitude
  figures ($25М, 8,5М машин, 102/38%) с inline proportion где применимо.
- **Ocean palette:** LOCKED v3 — DEEP/MID/LIGHT + Teal + Gold (≥1× каждая
  карточка: Card 1 gold footer, Card 2 gold L5, Card 3 gold badge+footer, Card 4
  gold warning zone). ✓/✗ glyph green/red — semantic verdict colors (не palette
  accent).
- **Print quality:** A4 cards vector text (∞ dpi). A1 embedded poster = 150 dpi.
- **NO timing / NO methodology:** проверено — карточки = student reference, нет
  минут, нет «методически важно», нет «strict_in» (internal term).

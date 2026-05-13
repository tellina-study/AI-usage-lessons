# Iteration log — Лекция 1 v3.1 (Phase 12.4 revision, issue #70)

**Date:** 2026-05-13
**Source:** chapter v3.1 (16,406 слов, status=reviewed) + deck.yaml v3.1 + 33 slides/*.md.
**Builder:** `build_lec01_v31.py` (single Python script, python-pptx primitives).
**Output:** `lec-01.pptx` (33 slides, 16:9, ~1.3 MB) + `lec-01.pdf` (~1.6 MB) + 33 snapshots iter7.

## Scope (per task brief)

**STAGE 1 — File operations (DONE):**
- Deleted `s26-arc-agi-economics.md` and `s28-pearl-3-levels.md`.
- Renamed (5): s27→s26, s29→s28, s30→s29, s31→s30, s32→s31. Updated `id:` in frontmatter for all 5.
- Created NEW `s27-section5-divider.md` (per DoD §10 + reader-rendered feedback).

**STAGE 2 — Content fixes (DONE — 11/11):**

| # | Fix | Where | Status |
|---|---|---|---|
| 1 | s13 speaker notes: Model = left-top, Agent = right-bottom (was «правый нижний» — wrong) | s13 md notes | ✅ Applied |
| 2 | «Приложение-робот» → «Приложение (автоматизация)»; 2 types of apps explanation | s21 visual + notes; s20 notes | ✅ Applied |
| 3 | NEW divider раздел 5 («Что забрать домой») | s27 md (NEW) + build_s27 | ✅ Applied |
| 4 | ARC-AGI deletion (no other action needed — s26-old removed) | s26 md (deleted) | ✅ Applied |
| 5 | s05b funnel «10% в проде» → «10% доходят до прода»; widened gold plate (0.55 → 0.85 fun_w fraction) | build_s05b | ✅ Applied |
| 6 | s13 axis labels enlarged 10pt → 13-15pt | build_s13 | ✅ Applied |
| 7 | s15 RU/EN sub-labels unified to RU (camera frame → кадр камеры; resize → масштабирование; etc.) | build_s15 | ✅ Applied |
| 8 | s21 axis labels Q1/Q2 moved INSIDE quadrant (Q1 inside left edge, Q2 above top) | build_s21 | ✅ Applied |
| 9 | s08 «90% откатов» n=50 caveat added to speaker notes | s08 md notes | ✅ Applied |
| 10 | s07 Vaswani timestamp «на сегодня» → «на май 2026» | s07 md notes | ✅ Applied |
| 11 | s29 PARTS disclaimer in notes (RTF/CRISPE/RACE alternatives mentioned) | s29 md notes | ✅ Applied |

**Bonus fix:** s28 takeaway 3 — removed Pearl reference («Pearl: AI устойчиво на уровне 1, человек на 3») since Pearl slide is gone. Replaced with «Граница «AI / не-AI» — ваша инженерная зона».

**Fix-12 (NEW from user, applied during revision):**

| # | Fix | Where | Status |
|---|---|---|---|
| 12 | Remove timing from visible content of all slides (lecture map + dividers) | s02a md + build_s02a + audit of build script | ✅ Applied |

**Detail:**
- s02a-lecture-map.md: title was «Карта лекции: 5 разделов **за 75 минут**» → «Карта лекции — 5 разделов»; assertion updated. Visual description rewritten: cards no longer carry «9.5 мин / 5.5 мин / 6 мин / 23 мин / 17 мин / 6 мин» captions; instead each card carries a 1-phrase description (e.g. «Где мы сейчас как пользователи», «Цифры рынка 2022–2026»).
- build_s02a(): tuple `("0", "Открытие\nи опросы", "9.5 мин", LIGHT)` → `("0", "Открытие\nи опросы", "Где мы сейчас\nкак пользователи", LIGHT)`. All six entries updated. Title argument updated. Pointer text widened to fit «↑ Вы здесь — Раздел 0» on one line.
- Roadmap-bar in section dividers (s10/s14/s22/s27): audited `roadmap_bar()` — already contains no timing (only «0 Открытие · 1 AI · 2 Сейчас · 3 Способы · 4 Границы · 5 Итог» + «Вы здесь — раздел N из 5»). No edit needed.
- Other slides: full grep `(минут|XX мин)` over build script confirms zero remaining timing strings in visible content. The only remaining `мин` occurrences are in the comment header (`75-min лекция`, line 9) and `min(` numerical helpers — neither is rendered.
- Speaker notes preserved: minutes in `## Speaker notes` and `## Лектору` sections of slide markdown (e.g. s02a notes: «самый большой, 23 минуты») are kept — these are for the lecturer, not student-visible. Per Fix-12 spec.
- deck.yaml `pacing:` section preserved — manifest, not on slides.
- Verified by re-render: snapshots/s02a-fix12b-03.png (lecture map clean), probe-12.png (s10 «Раздел 3» divider clean), s27-divider-29.png (s27 «Раздел 5» divider clean).

**STAGE 3 — Render PPTX + visual loop (DONE):**

Build script changes:
- Removed `build_s26` (old ARC) and `build_s28` (old Pearl) function bodies.
- Renamed `build_s27` → `build_s26` (4-speaker AGI table).
- Added NEW `build_s27` (section 5 divider, per spec: «Раздел 5» + «Что забрать домой» + frame phrase + roadmap-bar with «Вы здесь — раздел 5 из 5»).
- Renamed `build_s29` → `build_s28` (summary).
- Renamed `build_s30` → `build_s29` (roadmap).
- Renamed `build_s31` → `build_s30` (lec2 teaser).
- Renamed `build_s32` → `build_s31` (Q&A).
- Updated all `load_notes("sNN")` calls to match new IDs.
- Updated BUILDERS list to 33 elements.
- Updated docstring at top of file to reflect v3.1 changes.

## Visual loop iterations (4 total: iter4, iter5, iter6, iter7)

| Iter | Focus | Output | Issues found → fixed |
|---|---|---|---|
| iter4 | First v3.1 build after structural changes | snapshots/iter4-NN.png | s13 axis labels overlap with X-axis labels; s05b «10% доходят до прода» wraps to 2 lines; s21 «ПРИЛОЖЕНИЕ (автоматизация)» wraps awkwardly; Q1=Да label invisible. |
| iter5 | Apply round-1 visual fixes | snapshots/iter5-NN.png | s13: Y-axis «Контроль пользователя» wraps poorly, X-axis label overlaps Agent sub-text; s31 Q&A «Спасибо» partially overlapped by «Q&A» tail. |
| iter6 | Adjust s13 quadrant geometry + reposition Q&A; verify s21 fix («ПРИЛОЖЕНИЕ» on 1 line, Q1=Да/Нет inside) | snapshots/iter6-NN.png | s13: «↓ низкий» on Y-axis still overlapped Agent sub-label «низкий user»; X-axis arrows clipped agent area. |
| iter7 | Move Y-axis «низкий ↓» OUTSIDE quadrant (below bottom-left), X-axis range markers («← низкий» / «высокий →») moved INSIDE TOP edge of quadrant (away from agent at bottom). | snapshots/iter7-NN.png | ✅ All issues resolved. Final accept. |

## Per-slide changes (delta from v3 → v3.1)

### s05b — Course frame (Fix-5)
- iter4: gold «10% в проде» → «10% доходят до прода»; bot_w widened 0.30 → 0.55 fun_w. Still wrapped 2 lines.
- iter5: bot_w further widened 0.55 → 0.85; size 20pt → 22pt. → 1 line, perfect.

### s07 — Timeline 2017 (Fix-10)
- Notes only: «На сегодня статья имеет более ста шестидесяти тысяч цитирований» → «На май две тысячи двадцать шестого статья имеет более ста шестидесяти тысяч цитирований». Visual unchanged.

### s08 — Scale numbers (Fix-9)
- Notes only: added explicit n=50 caveat with CNews/Vedomosti/Intellectual Analytics источниками: «оценка построена на выборке примерно из пятидесяти крупнейших российских организаций... за март две тысячи двадцать шестого года. Это не репрезентативная выборка по всей экономике; это срез по крупным игрокам». Visual unchanged.

### s13 — Control quadrant (Fix-1, Fix-6)
- Notes (Fix-1): Model description «правый нижний угол» (wrong) → «левый верхний угол» (correct, matches visual). Agent description «левый верхний» (wrong) → «правый нижний угол» (correct). Visual unchanged here — the visual was correct, notes were inverted.
- Visual (Fix-6): Y-axis «Контроль пользователя» enlarged 12pt → 15pt; «↑ высокий» / «↓ низкий» enlarged 10pt → 11pt and made italic. X-axis label «Контроль разработчика» enlarged 12pt → 15pt. «← низкий» / «высокий →» markers moved INSIDE the quadrant top edge (away from Agent circle's sub-label at bottom-right).

### s15 — Model pipeline (Fix-7)
- Visual: Sub-labels unified to RU.
  - «camera frame, текст, audio» → «кадр камеры, текст, звук»
  - «resize, norm, tokenize» → «масштабирование, обрезка, токенизация»
  - «inference» → «инференс»
  - «NMS, softmax» → «фильтрация, нормализация»
  - «JSON, label, action» → «JSON, метка, действие»

### s20 — Applications (Fix-2 bridge)
- Notes: added explanation about 2 types of apps (with UI / without UI), with bridge phrase «На следующем слайде, когда мы соберём чек-лист в квадрант, эти два типа окажутся в разных углах».

### s21 — Checklist 2 questions + quadrant (Fix-2, Fix-8)
- Visual (Fix-2): «ПРИЛОЖЕНИЕ-РОБОТ» → «ПРИЛОЖЕНИЕ»; sub-text adjusted to «ETL с AI-классификатором (автоматизация)».
- Visual (Fix-8): Q1 axis labels (Q1=Да / Q1=Нет) moved INSIDE quadrant left edge (was outside right edge); Q2 labels stay at top edge but with reduced gap (-0.40 → -0.32).
- Notes (Fix-2): rewritten Q4 corner explanation — instead of «Приложение-робот — это автоматизированное приложение», explained two types of applications and how they map to the quadrant: with-UI apps in upper-left/upper-right or as Model corner; automated-no-UI apps in lower-right.

### s26 — Narrow vs general 4 speakers (renamed from old s27)
- File rename only. Build function renamed. `id:` in md frontmatter updated. Content unchanged.

### s27 — Section 5 divider (NEW)
- New file `s27-section5-divider.md` created based on s10/s14/s22 divider pattern.
- New `build_s27` function in build script — minimalist divider like s10:
  - Large «Раздел 5» (~110pt) outline color top-center.
  - Title «Что забрать домой» (40pt bold deep).
  - Frame phrase «Резюме · задание к семинару 1 · карта семестра · тизер лекции 2.» (22pt italic mid).
  - Roadmap-bar with gold marker on cell 5 («5 Итог»).
  - «Вы здесь — раздел 5 из 5» footer.
- Speaker notes ~150 words: recap of 4 sections + preview of section 5 contents + pacing instruction.

### s28 — Summary + homework (renamed from old s29)
- File rename. Build function renamed. `id:` updated.
- Content delta: takeaway 3 changed — removed Pearl reference (since Pearl slide deleted), replaced with «Граница «AI / не-AI» — ваша инженерная зона».

### s29 — Course roadmap (renamed from old s30) (Fix-11)
- File rename. Build function renamed. `id:` updated.
- Notes: added PARTS disclaimer paragraph mentioning RTF, CRISPE, RACE, RISEN, TAG as established alternatives. Visual unchanged.

### s30, s31 — Lec2 teaser, Q&A (renamed)
- File renames only. Build function renames. `id:` updated.
- s31 Q&A: visual repositioned (iter5/6) — Q&A title moved to y=1.9, h=2.4, size 140pt; «Спасибо» moved to y=5.4 to avoid Q&A tail clipping.

## Dropped/skipped
- None. All 11 fixes applied + 1 bonus fix (s28 takeaway 3 Pearl removal).

---

## Fix-14 (2026-05-13) — s07 timeline-2017 wraps + 2017 emphasis

**Trigger:** user critical observation + presentation-critic P1-6 («дату 2017 можно сделать крупнее, чтобы конкурировать с "Attention Is All You Need"»).

**Problem (iter3-09.png — pre-fix):** Timeline had 12 events (4 per band × 3 bands). Each event got ~2.39" horizontal room, forcing labels like "Turing\nImitation Game" to wrap with hard-coded `\n` breaks that didn't match natural reading flow. Date 2017 was 11pt — same as other dates — so it didn't stand out as the pivot. AI Effect callout intact at bottom (kept as-is).

**Fix in `build_s07()`:**
1. Reduced events 12 → 9 (3 per band). Dropped: 1956 Дартмут, 1980-е Экспертные системы (kept as parent label), 2024 MCP. Each event now gets ~3.18" horizontal room.
2. Event labels: "Turing — Imitation Game" instead of "Turing\nImitation Game" — em-dash separator, single line. Font 9.5pt → 12pt.
3. Year labels (non-pivot): 11pt → 14pt bold.
4. **Pivot year 2017: 28pt bold gold**, repositioned BELOW the larger oval (not overlapping). Was 11pt → now ~3× larger, dominant focal point.
5. Pivot oval: diameter 0.30" → 0.42", stroke 1.5pt → 2.0pt — anchors gold focal point.
6. Group labels: 11pt → 12pt with line_spacing=1.20 (allows clean 2-line wrap on left when parenthesis content overflows).
7. Renamed band 3 «Перелом и взрыв (2017 — 2026)» → «(2012 — 2026)» to include AlexNet correctly.
8. Last event "ChatGPT → DeepSeek R1, Claude Code" combines 2022/2025-26 ChatGPT-era milestones into one cell labeled "2022—26" — saves slot, retains all named systems.

**Speaker notes:** unchanged (per Fix-14 spec — they remain comprehensive and mention all dropped events including Дартмут 1956, экспертные системы XCON/MYCIN/Пятое поколение, MCP-era reasoning models 2024-26, so verbal coverage is preserved).

**Markdown sync:** `slides/s07-timeline-2017.md` `## Visual` rewritten to describe 9-event 3-band layout + note that дополнительные события 1956 и 2024 проговариваются голосом.

**Visual loop iterations:**
| Iter | Output | Issues found → fixed |
|---|---|---|
| iter4-s07-09 | First Fix-14 build | 2017 year text overlapped gold oval (text at band_y+0.78, oval extending to band_y+0.86). |
| iter5-s07-09 | Pivot year y +0.14, x widened 0.40→0.60, h grew | ✅ Clean — 2017 sits below oval, no overlap. Promoted to canonical iter3-09.png. |

**Result:** All 9 event labels render on **single lines** (no wraps). 2017 is now the visual centerpiece (28pt gold below 0.42" gold oval) — clearly competes with «Attention Is All You Need». AI Effect callout preserved unchanged.

**Snapshot:** `snapshots/iter3-09.png` (overwritten with iter5 result), also kept as `snapshots/iter5-s07-09.png` for diff trail.

## Fix-16 (2026-05-13) — s13 control quadrant axes swap (Agent → right-top)

**Trigger:** user critical observation — «На квадранте контроля 3 способов поменять оси, чтобы Агент = правый-верхний квадрант». Intuitively reinforces the «слоистая модель» from s11 (более обвязки = больше контроль разраб + больше делегирование от user → дальше вправо-вверх по диагонали).

**Problem (iter7-15.png — pre-fix):**
- X axis = «Контроль разработчика» (низкий → высокий).
- Y axis = «Контроль пользователя» (низкий → высокий).
- Модель: левый-верхний (низкий разраб + высокий user).
- Чат: центр.
- Агент: правый-нижний (высокий разраб + низкий user).

The «Агент = right-bottom» placement worked, but visually inverted the natural diagonal that mirrors layered architecture. User wanted Agent at right-TOP so the «больше обвязки → дальше вправо-вверх» metaphor reads cleanly.

**Fix in `build_s13()`:**
1. **X axis renamed:** «Контроль разработчика» → «**Делегирование от пользователя**» (низкий → высокий).
2. **Y axis renamed:** «Контроль пользователя» → «**Контроль разработчика**» (низкий → высокий).
3. **Point placement reversed along the diagonal:**
   - Модель: (fx=0.20, fy=0.68) — bottom-left (sub-text «Сам контролирует каждый шаг»).
   - Чат: (0.50, 0.50) — center (unchanged).
   - Агент: (fx=0.80, fy=0.20) — top-right, **GOLD** (sub-text «Делегирует задачу, разраб задаёт каркас»).
4. **Empty-quadrant labels** (italic 10pt slate, near corners):
   - Top-left (X=low delegation, Y=high разраб control): «нет смысла».
   - Bottom-right (X=high delegation, Y=low разраб control): «опасная зона».
5. **Circle diameter** 1.05" → 0.95" — frees vertical space so each circle + sub-text fit cleanly inside their respective half (above/below the cross-line).
6. **X-axis range markers** «← низкий» / «высокий →» moved BELOW the X-axis label (outside quadrant) — previously they were INSIDE the top edge, but now Агент occupies that exact area so they had to move out.
7. **Speaker notes rewritten** in `slides/s13-control-quadrant-3-ways.md` to match new axis semantics, including the new «two empty quadrants explain why placement is non-random» paragraph (the diagonal from bottom-left to top-right is the natural trajectory: more delegation requires more guard-rail caркаs).

**Markdown sync:** `s13-control-quadrant-3-ways.md` `## Visual` and `## Speaker notes` sections rewritten. Frontmatter `visual.primary` description updated to new axis semantics.

**Visual loop iterations:**
| Iter | Output | Issues found → fixed |
|---|---|---|
| iter1 (built as iter8-15) | First Fix-16 build with d=1.05, fy 0.78/0.22 | Модель sub-text «каждый шаг» overflowed bottom of quadrant box (sub_y_end > qy+qh). Agent sub-text just barely crossed the horizontal divider. |
| iter2 (built as iter9hi-15 + iter8-15 at 150dpi) | Reduced d to 0.95, repositioned fy to 0.68/0.20, narrowed sub-text box, moved sub_y closer (cy+0.50) | ✅ All elements fit cleanly within quadrant halves. Модель sub-text fully visible inside bottom-left quadrant. Агент sub-text sits 0.13" above the horizontal cross-line. Empty-corner labels render correctly. |

**Result:** Agent now sits in right-top quadrant (gold), Модель in bottom-left, Чат in center. Diagonal pattern (bottom-left → center → top-right) visually reinforces «больше делегирования требует больше каркаса» — matching the layered model story from s11. Empty-corner labels («нет смысла» / «опасная зона») contextualise why the diagonal is the natural trajectory.

**Snapshots:**
- `snapshots/iter8-15.png` (150dpi, canonical) — final accept.
- `snapshots/iter9hi-15.png` (200dpi, debug-quality inspection).

**Coordination:** Fix-16 runs alongside background designers Fix-12 (timing), Fix-13 (s06), Fix-14 (s07), Fix-15 (s11) — none touch s13. PPTX wasn't locked at start; clean rebuild.

## Fix-15 (2026-05-13) — s11 layers-not-alternatives: component labels per layer

**Trigger:** user critical observation — «На s11 (Способы реализации = слои) потеряны компоненты, которые добавляет каждый слой». Spec в md явно требовал «Подписи компонентов в каждом слое», но v3.1 рендер показывал только названия (Модель / Чат / Агент / Приложение).

**Problem (iter7-13.png — pre-fix):** 4 концентрических Ocean rounded box, каждый с одной подписью названия в углу. Что добавляет каждый слой — не видно. Студент не видит мостика «модель → чат добавляет UI и память → агент добавляет инструменты и планирование → приложение добавляет UX-обвязку».

**Fix in `build_s11()`:**
1. Каждый layer теперь содержит название (14pt bold, цвет ring stroke) + 1-line component caption (12pt italic DEEP).
2. Component captions (что слой ADD-ит к предыдущему):
   - **Приложение:** «+ AI внутри продукта · формы, кнопки, интеграции · промпты скрыты от пользователя».
   - **Агент:** «+ инструменты (API, поиск, код) · планирование · vector DB».
   - **Чат:** «+ UI диалога · память истории сообщений».
   - **Модель:** «stateless: вход → модель → выход» (10pt italic centered, без +).
3. Box sizes пересчитаны для top-strip компонента + label: outer 7.6×5.6, Agent 5.8×4.0, Chat 4.0×2.4, Model 2.4×1.0. Strip между outer и Agent ≈ 0.80", достаточно под 14pt label + 12pt italic comp + padding.
4. Левая explanation column сжата до 1 параграфа (2.6" вместо 4 строк bullet-list — иначе выглядела как дублирование).

**Speaker notes:** не трогались (per Fix-15 spec — they remain comprehensive).

**Markdown sync:** `slides/s11-layers-not-alternatives.md` `## Visual` обновлён — explicit перечень что в каждом слое, упоминание 12pt italic для components.

**Visual loop iterations (5 total — iter8 .. iter12):**
| Iter | Output | Issues found → fixed |
|---|---|---|
| iter8-s11-13 | First Fix-15 attempt — component captions 10pt italic, sizes 7.0×5.4 outer | Agent caption «vector DB» wrapped to 2nd line and overlapped Chat box top stroke. Application caption fit but barely (10pt was too small per spec). |
| iter9-s11-13 | Bumped sizes outer 7.4×5.6, kept 9-10pt italic for safety | All single-line ✓, but font too small per «12-14pt readable from projector» spec. |
| iter10-s11-13 | Promoted to 12pt italic with 2-line components | 2nd lines crossed inner box borders (Application's «формы · кнопки · интеграции...» sat on Agent stroke; Agent's «+ планирование...» on Chat stroke; Chat's caption overlapped Model). Strips were too narrow for 2 lines at 12pt. |
| iter11-s11-13 | Reverted to single-line per layer at 12pt italic; kept large boxes | Application caption «+ AI как компонент UX · формы · кнопки · интеграции · пользователь не видит промпты» (89 chars) wrapped. «промпты» дрейфовала на 2-ю строку (но не пересекала Agent border). Acceptable but not clean. |
| iter12-s11-13 | Trimmed Application caption to 71 chars: «+ AI внутри продукта · формы, кнопки, интеграции · промпты скрыты от пользователя» | ✅ All 4 layers — name + components on **single lines** at 12pt italic. No box-border crossings. Promoted to canonical `iter8-13.png`. |

**Result:** Каждый слой теперь явно показывает что он добавляет. Слоистая mental model читается с одного взгляда. Gold accent сохранён (callout «Выбор слоя — инженерное решение, не альтернатива» + heading «включает предыдущий»). Visual motif (Ocean rounded box stroke) на каждом слое в цвете соответствующей роли (DEEP / MID / LIGHT / TEAL).

**Snapshots:**
- `snapshots/iter12-s11-13.png` (iter trail).
- `snapshots/iter8-13.png` (canonical — copy of iter12).

**Coordination:** Fix-15 ran sequentially after waiting for libreoffice convert from another designer (Fix-16 / Fix-14). PPTX file lock checked before each build. No conflicts on `build_s11()` function (other designers touched s07, s13).

## Final pacing
- 62.5 active min + 12.5 buffer = 75 min total. Matches deck.yaml v3.1 spec.

## Slide count verification
- Was: 34 (v3).
- Removed: 2 (s26 ARC, s28 Pearl) = 32.
- Added: 1 (NEW s27 divider раздел 5) = 33.
- Final: 33 slides. ✅ Matches deck.yaml v3.1 (s01..s31 plus s02a, s05a, s05b).

## Files

| File | Purpose |
|---|---|
| `build_lec01_v31.py` | Build script v3.1 (copy of v3 with all changes) |
| `build_lec01_v3.py` | Build script v3.1 (also updated in-place — same content) |
| `lec-01.pptx` | Final PPTX (33 slides) |
| `lec-01.pdf` | PDF export |
| `snapshots/iter4-*.png` ... `iter7-*.png` | Visual loop snapshots (4 iterations × 33 slides) |
| `iteration-log-v31.md` | This log |

---

## Fix-19 (2026-05-13) — remove "вы здесь / сюда" text markers from all nav-slides

**Trigger:** user observation post-Fix-17/18 unification — «убери со всех промежуточных слайдов текст — вы здесь, сюда и т.д. достаточно выделения цветом».

**Rationale:** на nav-slides (s02a карта лекции, s10/s22/s27 section dividers, s29 course roadmap) текущая позиция уже подсвечена gold (заливка карточки или цвет текста). Текстовый маркер «↑ Вы здесь — Раздел N» был дублированием — color highlight даёт ту же информацию на 0.3 секунды быстрее без шума.

**Coordination:** Fix-19 запущен параллельно с Fix-17 (unify nav slides) / Fix-18 (s16 cycle). Стратегия: дождаться 180s стабильности `build_lec01_v31.py` (Fix-17 активно правит nav-slide функции через новый `nav_slide()` helper). Wait через background task + Monitor; первая попытка edit конфликтнула (file modified), retry прошёл. Финальная стабильность достигнута в 12:17:55.

**Edits applied to `build_lec01_v31.py`:**

| Location | Before | After |
|---|---|---|
| `roadmap_bar()` line 290-292 | `text_box(... "Вы здесь — раздел {here_idx} из 5", color=GOLD ...)` под bar | Удалено. Текущая секция bar — gold cell, остальные — soft grey. |
| `nav_slide()` line 377-382 (helper added Fix-17) | `if sub_marker: text_box(... color=GOLD ...)` под highlighted card | Параметр `sub_marker` сохранён в сигнатуре (backward-compat) но игнорируется (`_ = sub_marker`). Docstring помечает его DEPRECATED. |
| `build_s02a()` (старый монолит) | `text_box(... "↑ Вы здесь — Раздел 0", color=GOLD ...)` под карточкой 0 | Удалено. Карточка 0 уже gold-stroke (overview state) или gold-filled (zoom-in state). |
| `build_s02a()` (новый — через `nav_slide`) | `nav_slide(..., sub_marker="↑ Вы здесь — раздел 0 (Открытие)")` | `nav_slide(...)` без sub_marker. |
| `build_s10()` (новый — через `nav_slide`) | `nav_slide(..., sub_marker="↓ Сейчас сюда")` | `nav_slide(...)` без sub_marker. |
| `build_s22()` (новый — через `nav_slide`) | `nav_slide(..., sub_marker="↓ Сейчас сюда")` | `nav_slide(...)` без sub_marker. |
| `build_s14()` (legacy mini-divider, удалён из BUILDERS Fix-17) | `if is_now: text_box(... "↓ Сейчас сюда", color=GOLD ...)` | Удалено в legacy функции — больше не вызывается из BUILDERS. |
| `build_s27()` (section 5 divider) | comment `# Roadmap bar with «Вы здесь — раздел 5 из 5»` | Comment обновлён: `# Roadmap bar — current section (5 Итог) is highlighted by gold cell (Fix-19: no text marker)`. Сама `roadmap_bar()` уже без текста. |
| `build_s29()` (course roadmap 17×3) | `text_box(..., text="←  Вы здесь", color=GOLD)` рядом с «1. Введение» + extra `gap_after_first` | Удалено. «1. Введение» уже выделена — `bold=True, color=GOLD, size=10.5`. Lectures list теперь равномерный (no extra gap). |

**Edits applied to slide MD files (Source-of-truth sync):**

| File | Edit |
|---|---|
| `slides/s02a-lecture-map.md` § visual.primary | «gold-маркер «Вы здесь — Раздел 0»» → «Активный раздел (Раздел 0) подсвечен gold-обводкой карточки» |
| `slides/s02a-lecture-map.md` ## Visual | Тот же smysl — текстовый маркер заменён на описание color-highlight механики |
| `slides/s10-section3-divider.md` § visual.primary, ## Visual, ## Лектору | Удалены упоминания «маркер «Вы здесь»». «Жест в сторону roadmap-bar — указать на gold-подсвеченную секцию.» |
| `slides/s22-section4-boundaries.md` ## Visual | «gold-маркер «Вы здесь — Раздел 4»» → «текущая секция (4 Границы) подсвечена gold — без текстового маркера» |
| `slides/s27-section5-divider.md` § visual.primary, ## Visual, ## Лектору | «маркер «Вы здесь — 5 из 5»» → «gold-подсветка финальной секции». Лектору жест указывает на gold cell. |
| `slides/s29-course-roadmap-17x3.md` § visual.primary, ## Visual, ## Лектору | «gold-маркер «Вы здесь — Лекция 1»» → «Текущая лекция (1. Введение) подсвечена gold-цветом + bold — без текстового маркера». Лектору указать на подсвеченную лекцию. |
| `slides/s14-deep-dive-divider.md` | НЕ редактировался — файл удалён Fix-17 (см. BUILDERS comment line 1976-1979). Legacy `build_s14()` функция остаётся в коде но не вызывается. |

**Speaker notes preserved:** в notes лектора (`## Speaker notes` + `## Лектору`) могут оставаться фразы типа «мы сейчас в разделе 0» — это для оратора, не для слайда. Per Fix-19 spec.

**Visual loop iterations:** 1 (single iteration sufficient — Fix-19 — pure removal task; layout otherwise stable from Fix-17).

| Iter | Output | Verification |
|---|---|---|
| iter1 | `snapshots/fix19-iter1-{s02a,s10,s22,s27,s29}-NN.png` | ✅ Все 5 nav-slides рендерятся БЕЗ текстовых маркеров. Цветовое выделение (gold-filled card на s02a/s10/s22/s27, gold+bold text на s29) — единственный навигационный индикатор. |

**Verification grep:**
- `grep -E "вы здесь|сейчас сюда" build_lec01_v31.py` → only in code comments (Fix-19 markers).
- `grep -E "вы здесь|сейчас сюда" slides/*.md` → 0 matches.
- `grep -E "↑ Вы здесь|↓ Сейчас|← Вы здесь" build_lec01_v31.py` → only in Fix-19 code comments.

**Build output:** 32 slides (33 → 32 due to Fix-17 deleting s14 from BUILDERS). Pacing recovered: −0.5 min from active = 62.0 active + 12.5 buffer = 74.5 min ≈ 75-min plan.

**Files changed in Fix-19:**
- `library/lectures/lec-01/rendered/build_lec01_v31.py` (4 edits in helpers, 4 edits in nav-slide builders, 1 comment update).
- `library/lectures/lec-01/slides/s02a-lecture-map.md` (visual.primary + ## Visual).
- `library/lectures/lec-01/slides/s10-section3-divider.md` (visual.primary + ## Visual + ## Лектору).
- `library/lectures/lec-01/slides/s22-section4-boundaries.md` (## Visual).
- `library/lectures/lec-01/slides/s27-section5-divider.md` (visual.primary + ## Visual + ## Лектору).
- `library/lectures/lec-01/slides/s29-course-roadmap-17x3.md` (visual.primary + ## Visual + ## Лектору).
- `library/lectures/lec-01/rendered/lec-01.pptx` (rebuilt, 32 slides, 1.26 MB).
- `library/lectures/lec-01/rendered/lec-01.pdf` (rebuilt, 1.56 MB).
- New snapshots: `snapshots/fix19-iter1-{s02a-03,s10-12,s22-23,s27-28,s29-30}.png` (110 dpi, single iter).

---

## Fix-17 + Fix-18 — Unified navigation slides + s16 chat cycle linear flow (2026-05-13)

### Fix-17 — Unified nav slides (single template across s02a / s10 / s22 / s27)

**User feedback (2026-05-13):** все navigation slides выглядят разными визуалами (s02a — 6 cards карта, s10/s22/s27 — большое «Раздел N» + roadmap-bar внизу, s14 — mini-divider с 4 типами). Нужен один template, чтобы при каждом nav-slide была видна вся карта лекции и текущая позиция выделена.

**Decision:** Variant A («single template with step-highlight»):
- Все nav slides используют один helper `nav_slide(slide, here_idx, title, frame_phrase, sub_marker)` (line 319 build_lec01_v31.py).
- 6 cards (sections 0..5) horizontal — точно как в s02a — на каждом nav slide.
- В overview state (s02a, here_idx=0) и zoom-in state (s10/s22/s27, here_idx>=1) скелет одинаковый, current card highlighted в gold (filled с белым текстом для zoom-in, gold border + filled для overview).
- Title слайда подсказывает, в какую секцию мы заходим.
- Frame phrase (1 строка italic) — short framing подзаголовок.

**Decision per s14 (deep-dive divider):** УДАЛЁН.
- Reason: paraphrased s10 framing («не альтернативы, а слои» + «разберём подробнее каждый») — близкие сообщения, дублирование.
- 4-type icons (модель / чат / агент / приложение) breaks the lecture's 5-section navigation grammar.
- Pacing benefit: -0.5 min from active, +0.5 min buffer.
- Verbal transition «Дальше — детальный разбор каждого из четырёх типов: модель, чат, агент, приложение» добавлен в s13 «Лектору» speaker notes.

**Files changed:**
- `library/lectures/lec-01/rendered/build_lec01_v31.py`:
  - Added `NAV_SECTIONS` constant + `nav_slide()` helper (lines 308-380).
  - Rewrote `build_s02a` (overview, here_idx=0).
  - Rewrote `build_s10` (zoom-in, here_idx=3).
  - Rewrote `build_s22` (zoom-in, here_idx=4).
  - Rewrote `build_s27` (zoom-in, here_idx=5).
  - Deleted `build_s14`. Removed from BUILDERS list with comment.
- `library/lectures/lec-01/deck.yaml`:
  - Replaced s14 entry with deletion comment.
  - Updated section_3 timing 23 → 22.5 min.
  - Updated active_min 62.5 → 62.0; buffer_min 12.5 → 13.0.
  - Added `deletions_in_fix17` and `fix17_unified_nav` blocks.
- `library/lectures/lec-01/slides/s14-deep-dive-divider.md` — DELETED.
- `library/lectures/lec-01/slides/s13-control-quadrant-3-ways.md` — added verbal transition note in «Лектору».

**Iterations:**
- iter1 (visual loop): all 4 nav slides rendered correctly with unified template; sub_marker «Вы здесь» / «↓ Сейчас сюда» suppressed by Fix-19 (parallel designer's earlier change — gold-filled card is sufficient navigation cue). Accepted.

**Snapshots (final, 150 dpi):**
- `snapshots/s02a-03.png` (overview state, section 0 highlighted gold).
- `snapshots/s10-12.png` (zoom-in state, section 3 highlighted gold).
- `snapshots/s22-23.png` (zoom-in state, section 4 highlighted gold).
- `snapshots/s27-28.png` (zoom-in state, section 5 highlighted gold).

### Fix-18 — s16 chat cycle: rewrite from circular to linear vertical flow

**User feedback (2026-05-13):** «не читается». Original layout — 6 boxes in circle around center «LOOP» badge. Step order не считывается, callouts overlap with step boxes, magic «LOOP» badge confusing.

**Decision:** Linear vertical flow в левой колонке (6 numbered step boxes сверху-вниз с down-arrows между ними) + 2 gold callouts в правой колонке, anchored vertically к step 2 и step 5. Loop indicator в gold-tinted box ниже step 6. Bottom takeaway полной шириной снизу.

**Files changed:**
- `library/lectures/lec-01/rendered/build_lec01_v31.py`:
  - Rewrote `build_s16` (was circular layout → vertical linear flow).
  - Used `MSO_SHAPE.DOWN_ARROW` for inter-step arrows (better than rotated RIGHT_TRIANGLE).
- `library/lectures/lec-01/slides/s16-chat-cycle-schema.md`:
  - Updated `visual.primary` description (was «6_step_loop_diagram» → «6_step_linear_flow»).
  - Updated `## Visual` section with new layout description.

**Iterations:**
- iter1: layout works, callouts visible, but down-arrows (filled_rect + RIGHT_TRIANGLE) look small and don't read as proper arrows.
- iter2: switched to MSO_SHAPE.DOWN_ARROW (proper arrow shape), increased step_top to give more vertical room. Callouts now vertically centred against step 2 and step 5. Loop indicator wrapped in gold-tinted box. **But** loop indicator and bottom takeaway overlap (loop box ends y=7.23, takeaway at y=7.10).
- iter3: reduced step_h (0.62→0.58) and pitch (0.88→0.80) to compress vertical layout; bottom takeaway moved to y=7.05 (clear of loop indicator). Final.

**Snapshot (final, 150 dpi):**
- `snapshots/s16-17.png` (linear vertical flow with side callouts).

### Build outputs
- `library/lectures/lec-01/rendered/lec-01.pptx` (32 slides, was 33 — s14 removed).
- `library/lectures/lec-01/rendered/lec-01.pdf` (regenerated).
- All 32 slide snapshots at 110 dpi: `snapshots/fix17-iter3-NN.png`.
- All 32 slide snapshots at 150 dpi: `snapshots/iter8-NN.png`.

### Pacing impact
- Section 3: 23 → 22.5 min (-0.5 from s14 deletion).
- Total active: 62.5 → 62.0 min (-0.5).
- Buffer: 12.5 → 13.0 min (+0.5 — pacing relief).
- Final 75 min total preserved.

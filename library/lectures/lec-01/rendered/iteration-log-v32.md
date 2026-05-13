# Iteration log — Лекция 1 v3.2 (Phase 12.6 revision, 19 user fixes batch)

**Date:** 2026-05-13
**Source:** chapter v3.1 + deck.yaml v3.1 → v3.2 + 32 slides → 33 (s19 split into s19+s19a)
**Builder:** `build_lec01.py` (in-place updates; renamed from `build_lec01_v31.py` during Phase 5 hygiene cleanup, 2026-05-13).
**Output:** `lec-01.pptx` (33 slides, 16:9, ~1.3 MB) + `lec-01.pdf` + 33 snapshots iter14.

## Scope (Phase 12.6 task brief, 19 fixes)

| # | Fix | Where | Status |
|---|---|---|---|
| 1 | GLOBAL: Strip «Лектору» section from all 32 slides/sNN-*.md + update load_notes() | 32 .md files + build script | ✅ Done |
| 2 | s02a: Remove «Что мы пройдём за 75 минут — и в каком порядке» | build_s02a frame_phrase=None | ✅ Done |
| 3 | s04: Bar chart 5 → 8 LLM options matching s03 chips | build_s04 + s04 md | ✅ Done |
| 4 | s04: Donut centred «51%» + circular aspect | build_s04 + regenerated PNG (square 1200×1200) | ✅ Done |
| 5 | s04: Remove bottom takeaway band «Сравнивайте методологии…» | build_s04 | ✅ Done |
| 6 | s05b: Funnel «10% доходят до прода» single-line readable | build_s05b widened blocks, 24pt | ✅ Done |
| 7 | s07: Single-line event labels; remove AI Effect callout; add Vaswani-2017 deep-dive (8 authors, self-attention, 160K+ citations) | build_s07 + s07 md | ✅ Done |
| 8 | s09: Remove Llama-3 + MCP; add OpenClaw (Steinberger Nov 2025, 100K stars) and Kimi K2.5 (Moonshot Jan 2026, swarm mode) | build_s09 + s09 md | ✅ Done |
| 9 | s11: Layers bottom-aligned; component captions on teal-tinted filled blocks | build_s11 + s11 md | ✅ Done |
| 10 | s12: Lucide icons per task; single-line column headers; matrix filled with 26+ examples | build_s12 + s12 md + 6 new icons downloaded | ✅ Done |
| 11 | s15: Pipeline arrows replaced with proper RIGHT_ARROW shapes | build_s15 | ✅ Done |
| 12 | s16: Chat cycle redesigned as compact dialog cycle (USER ↔ Message ↔ LLM ↔ Answer ↔ USER + system prompt + ⋮) | build_s16 + s16 md | ✅ Done |
| 13 | s17: Bar chart → production-disclaimer card («чистые чаты почти не используются в prod, везде RAG/агенты») | build_s17 + s17 md | ✅ Done |
| 14 | s18: USER added to architecture with bidirectional arrows to Chat | build_s18 + s18 md | ✅ Done |
| 15 | s19 SPLIT: s19 = sequential 200 PDF steps with tool annotations; NEW s19a = 5 levels + Human-in/on/out-of-the-loop framings | build_s19 rewritten + build_s19a NEW + new s19a md | ✅ Done |
| 16 | s21: Q1 vertical-LEFT (markers ДА/НЕТ beside top/bottom rows); Q2 horizontal-BOTTOM (markers НЕТ/ДА under columns); bottom takeaway removed | build_s21 v4 (3 sub-iterations needed) | ✅ Done |
| 17 | s28: Homework wording «защитите выбор перед группой» → «принесите → пропустите через 2-вопросный квадрант → одностраничный разбор» | build_s28 + s28 md | ✅ Done |
| 18 | s29 + chapter §5.2: Module reshuffle — Лекция 6 M1→M2; Лекция 8 M1→M3 | build_s29 + chapter.md §5.2 | ✅ Done |
| 19 | s30: Remove YOLO callback frame; full-width 4-concept grid + 1-phrase frame | build_s30 + s30 md | ✅ Done |

## Visual loop iterations

5 build cycles (iter9 → iter10 → iter11 → iter12 → iter13 → iter14 final) addressing visible artifacts:

### iter9 (first build after all 19 fixes applied)
Found:
- s07: timeline year labels rendered INSIDE next band — geometry off (event_y = band_y - 0.02 + year_y = band_y + 0.95 → year overlapped next band start).
- s11: outer Application box overlapped slide title — top edge too low; left explanation column missing (lost in v9 rewrite).
- s09: text wraps in OpenClaw («100K★ за квартал\n22 каналов · 100 skills») and Kimi K2.5 («open multimodal\nswarm mode: 100 sub-agents») — text too long for card.
- s04: «Ничем — см. donut слева» wrapped past «% пользователей AI» caption.
- s21: «ВОПРОС 2» title rendered BELOW slide bottom (off-canvas).

### iter10 (round-1 fixes applied)
- s07: re-geometry'd with band_h 1.10→1.40, event labels in TOP HALF, year labels in BOTTOM HALF of each band. Vaswani callout pushed down to 6.30.
- s11: outer box top edge raised to 1.65 (h reduced 5.4→5.0); restored left explanation column (3 text_box + gold_callout).
- s09: trimmed card subtitles to 2 lines.
- s04: shortened «нет данных РФ» / «(см. donut слева)» tags inline.
- s21: marker_y placed BEFORE Q2 title so order is markers-then-title.

Found:
- s04: «↑ Та же страна…» callout still overlapped «*Сумма >100%…» footnote.
- s21: Q1 title «ВОПРОС 1» / «Нужно ли…?» overlapped slide title at top — placed text ABOVE quadrant which collided with title.

### iter11
- s04: callout y moved closer to bars; footnote pulled to bar_y+bar_h-0.45.
- s21: Q1 layout redesigned — markers in narrow left column, question text in middle column wedged BETWEEN markers (no above-quadrant zone).

Found:
- s04: footnote y still too far down (overlapping callout). Bar box height too tight.
- s21: Q1 «ВОПРОС 1» STILL overlapped main title (placed at quad_y - 0.85 = 0.80, title spans 0.45-1.60).

### iter12
- s04: row_h 0.36 → 0.34; callout y derived from bar_top+8*row_h+0.10; footnote at callout_y+0.45 — clear separation.
- s21: Q1 v4 — markers FAR LEFT in narrow column (q1_x+0.10), question text in middle column at vertical centre (centre_y - 0.55).

Found:
- s21: Q1 vertical layout works; «ВОПРОС 2» title overlap issue solved by markers-then-title order. ✅

### iter13 (final accept)
All 33 slides render cleanly:
- Title clear of content boxes.
- Text boxes not overlapping.
- Donut centred number visible.
- Bar charts complete with all 8 LLM rows + DeepSeek callout + footnote.
- Funnel single-line endpoints.
- Timeline single-line event labels with 2017 gold pivot prominent.
- 4 episodes (s09) all readable single-line subtitles.
- Layers bottom-aligned with teal-tinted component strips.
- Matrix (s12) with icons, 26+ filled cells, YOLO gold callback.
- Pipeline (s15) with proper RIGHT_ARROW shapes.
- Dialog cycle (s16) with USER/Message/LLM/Answer + system prompt overlay.
- Production disclaimer (s17) with clear card layout.
- Architecture (s18) with USER and bidirectional arrows.
- 200 PDF steps (s19) with tool annotations on each step.
- Autonomy levels (s19a NEW) with 5 levels + 4 loop framings.
- Quadrant (s21) with Q1-vertical-LEFT and Q2-horizontal-BOTTOM markers.
- Homework simplified (s28).
- Module reshuffle reflected (s29 + chapter §5.2).
- Lec 2 teaser clean (s30).

### iter14 (sanity rebuild post chapter + deck.yaml updates)
Rebuilt to verify no regression after chapter and deck.yaml metadata updates. All 33 slides still clean.

## Per-slide changes (delta v3.1 → v3.2)

### Speaker notes — GLOBAL (Fix-1)
- All 32 slide markdowns: «## Лектору ... » section + preceding `---` separator REMOVED via Python regex.
- `load_notes()` in build script simplified — no longer extracts «Лектору» block; just reads «## Speaker notes» up to next heading.
- Net effect: speaker notes are now ONLY readable student-text (150-300 words), no lecturer-cues. Lecturer prep moves to speech.md (separate artifact).

### s02a (Fix-2) — frame_phrase=None
- `nav_slide(here_idx=0, title=..., frame_phrase=None)` — subtitle removed.
- s02a md: visual.primary updated.

### s04 (Fix-3, Fix-4, Fix-5)
- Donut PNG regenerated via QuickChart — now square 1200×1200 with cutoutPercentage=62.
- Centre overlay «51%» 56pt DEEP + «раз в неделю и чаще» 11pt italic.
- Bar chart now has 8 rows (was 5): ChatGPT/YandexGPT/DeepSeek (gold)/GigaChat/Шедеврум with %; Claude/Gemini «нет данных РФ»; Ничем «(см. donut слева)».
- DeepSeek 43% Microsoft callout retained, footnote retained, takeaway band REMOVED.
- s04 md: visual.primary fully rewritten.

### s05b (Fix-6)
- Funnel blocks: top 100% trapezoid (full width), middle −90% (75% width), bottom 10% gold (FULL width).
- All 3 levels at 20-24pt, single-line text.
- Vertical spacing tighter.

### s07 (Fix-7)
- Reduced events 12 → 9 (3 per band).
- Single-line labels via em-dash separator.
- Year sits BELOW band line (event label sits ABOVE).
- 2017 pivot: 22pt gold year + 0.42" gold oval — dominant.
- AI Effect callout REMOVED. Replaced with Vaswani-2017 deep-dive (8 authors named, self-attention, 160K+ citations on May 2026).

### s09 (Fix-8)
- Episodes: Mistral 7B / DeepSeek R1 (gold) / OpenClaw / Kimi K2.5.
- Removed: Llama-3 (Meta — already-big lab), MCP (infra protocol, weaker narrative).
- Added: OpenClaw (Steinberger Nov 2025, 100K★ за квартал, P. Steinberger ушёл в OpenAI 14 февраля 2026).
- Added: Kimi K2.5 (Moonshot AI Jan 2026, swarm mode 100 sub-agents).
- s09 md notes fully rewritten.

### s11 (Fix-9)
- Bottom-aligned nested layers (common bottom edge at 6.65, outer top edge 1.65).
- Component captions on teal-tinted filled strips inside top of each layer (not floating text).
- Sizes: outer 7.6×5.0, Agent 5.9×3.6, Chat 4.3×2.3, Model 2.6×1.0.
- Left explanation column restored.
- s11 md: visual.primary updated.

### s12 (Fix-10)
- 6 Lucide icons downloaded + recolored: tag, scan-line, search, sparkles, trending-up, list-checks.
- Column headers single-line short labels («Классиф.», «Распозн.», etc.) with icon above.
- Matrix 6×5 (30 cells) — 26+ filled with concrete products: BERT/spaCy/BM25/CLIP/GPT-4o/DALL-E/Whisper/AlphaFold/Prophet/ARIMA/ReAct/Devin/OpenClaw etc.
- Color coding: MID classifiers/search, LIGHT recognition/forecast/planning, TEAL generation, GOLD YOLO callback.
- s12 md: visual.primary fully rewritten.

### s15 (Fix-11)
- Pipeline arrows replaced: was filled_rect + rotated RIGHT_TRIANGLE → now proper MSO_SHAPE.RIGHT_ARROW (single shape, cleaner).
- arrow_w 0.45 → 0.55 (more breathing room).

### s16 (Fix-12) — MAJOR redesign
- Old layout: 6 vertical step boxes + 2 callouts + loop indicator.
- New layout: compact dialog-cycle. Two USER icons (sender top, receiver bottom) on left. Two horizontal blocks (Message + Answer) in middle column. LLM box on right (spans both rows). System prompt block above Message with gold DOWN_ARROW «merges into». USER → Message → LLM (RIGHT_ARROW), LLM → Answer → USER (LEFT_ARROW). Continuation indicator «⋮ следующая итерация» under Answer.
- 2 gold callouts on right: «Контроль через системный промпт», «Ограничение — контекстное окно (128k-1M)».
- Bottom takeaway preserved.
- s16 md: visual.primary fully rewritten.

### s17 (Fix-13)
- Right-side bar chart (LLM РФ) REPLACED with production-disclaimer card.
- Card content: «Чистые чаты почти не используются в production. Почти везде они расширены до агентов — хотя бы для долгосрочной памяти и поиска по корпоративной базе (RAG). Архитектуру агента разберём на следующем слайде».
- Card style: gold-tinted Ocean rounded box with gold stroke.
- s17 md: visual.primary + speaker notes updated.

### s18 (Fix-14)
- USER icon added on LEFT (1.4" diameter circle, LIGHT blue, "USER" white text).
- Two arrows USER ↔ Chat: top RIGHT_ARROW (request, MID), bottom LEFT_ARROW (response, TEAL).
- Layout shifted: chat centre cx=7.30 (was 6.65) to make room for USER on left.
- Memory + Tools moved to BELOW chat (was flanking sides); cleaner with USER on left.
- s18 md: visual.primary updated.

### s19 (Fix-15 part A) — sequential steps
- Old content (200 PDF case + 5 levels of autonomy) split.
- Now: case card on left (compact), 7 sequential steps on right with tool annotations.
- Steps: 1) Получить список → file system; 2) Открыть PDF #1 → PDF reader; 3) Извлечь текст → text extraction; 4) Сводка → vector DB → embeddings + vector DB; 5) Найти ключевые поля → search + LLM extract; 6) Записать строку → Sheets API / CSV writer; 7) Цикл по 200 файлам → orchestrator loop (gold).
- Gold callout: «Агент = последовательность вызовов инструментов, оркестрируемая LLM».
- s19 md fully rewritten.

### s19a (Fix-15 part B) — NEW slide for autonomy
- Left card: 5 уровней автономии (Feng/McDonald/Zhang 2025) — Operator/Collaborator/Consultant/Approver/Observer (gold), bottom-up ladder.
- Right card: 4 framings — Human-in-the-loop / Human-on-the-loop / Human-out-of-the-loop (gold) / Override modes.
- Bottom gold callout: «Уровень автономии — выбор продукта, не свойство модели».
- s19a md NEW.

### s21 (Fix-16) — quadrant axes redesign
- Q1 axis is now VERTICAL on LEFT side: ДА marker (gold-tinted, beside top half) + НЕТ marker (white, beside bottom half) in narrow leftmost column; ВОПРОС 1 + question text in middle column wedged at vertical centre between markers.
- Q2 axis is now HORIZONTAL at BOTTOM: НЕТ marker (white, under left column) + ДА marker (gold-tinted, under right column); ВОПРОС 2 + question title BELOW markers.
- Bottom takeaway («Подумайте 30 секунд…») REMOVED.
- Quadrant area: shrunk to 7.50×4.10 to fit Q2 markers + title within slide bottom.

### s28 (Fix-17) — homework
- Old: «возьмите свой AI-инструмент → пропустите через 2-вопросный квадрант → защитите выбор перед группой».
- New: «Принесите свой AI-инструмент → пропустите через 2-вопросный квадрант → одностраничный разбор».
- s28 md: visual + speaker notes updated.

### s29 (Fix-18) + chapter §5.2 — module reshuffle
- Module 1 (lec 1-5, 7): «Основы + знакомые индустрии» — 6 lectures.
- Module 2 (lec 6, 9-12): «Высокотехнологичные отрасли» — 5 lectures (added 6 Инж. проект.).
- Module 3 (lec 8, 13-17): «Креатив, ИКТ, наука, добыча, синтез» — 6 lectures (added 8 Креативные).
- Module width on slide proportional to lecture count.
- Chapter §5.2 updated to match: 3 tables (Module 1 / 2 / 3) with new lecture lists.

### s30 (Fix-19) — lec 2 teaser
- Removed: YOLO callback frame on left half.
- Now: full-width 4-concept grid 2×2 (Токены / Эмбеддинги / Внимание / Температура) with bigger cards.
- Bottom 1-phrase frame: «Эти 4 концепта объясняют поведение всех современных LLM — от ChatGPT до DeepSeek».
- s30 md: visual.primary + speaker notes updated.

## Files changed

| File | Type |
|---|---|
| `library/lectures/lec-01/rendered/build_lec01_v31.py` | major rewrite of 11 builders + load_notes() update + new build_s19a |
| `library/lectures/lec-01/rendered/lec-01.pptx` | rebuilt 33 slides |
| `library/lectures/lec-01/rendered/lec-01.pdf` | rebuilt |
| `library/lectures/lec-01/rendered/snapshots/iter9-*.png` ... `iter14-*.png` | 5 iterations × 33 slides |
| `library/lectures/lec-01/rendered/assets/charts/c1-vciom-donut.png` | regenerated (square 1200×1200) |
| `library/lectures/lec-01/rendered/assets/icons/lucide-{tag,scan-line,search,sparkles,trending-up,list-checks}-blue.png` | NEW (6 icons for s12) |
| `library/lectures/lec-01/slides/*.md` | 32 files: «Лектору» stripped (Fix-1) |
| `library/lectures/lec-01/slides/s04-poll-reveal-data.md` | visual rewritten (Fix-3,4,5) |
| `library/lectures/lec-01/slides/s07-timeline-2017.md` | visual updated (Fix-7) |
| `library/lectures/lec-01/slides/s09-breakthroughs-2023-2026.md` | episodes rewritten (Fix-8) |
| `library/lectures/lec-01/slides/s11-layers-not-alternatives.md` | visual updated (Fix-9) |
| `library/lectures/lec-01/slides/s12-classification-task-modality.md` | visual rewritten (Fix-10) |
| `library/lectures/lec-01/slides/s16-chat-cycle-schema.md` | visual + title rewritten (Fix-12) |
| `library/lectures/lec-01/slides/s17-chat-model-ui-memory.md` | visual + speaker notes (Fix-13) |
| `library/lectures/lec-01/slides/s18-agent-architecture-schema.md` | visual updated (Fix-14) |
| `library/lectures/lec-01/slides/s19-agent-200pdf-autonomy-levels.md` | fully rewritten — 200 PDF only (Fix-15) |
| `library/lectures/lec-01/slides/s19a-autonomy-levels.md` | NEW (Fix-15) |
| `library/lectures/lec-01/slides/s28-summary-homework.md` | homework wording (Fix-17) |
| `library/lectures/lec-01/slides/s30-lecture2-teaser.md` | visual + speaker notes (Fix-19) |
| `library/lectures/lec-01/chapter.md` §5.2 | module reshuffle (Fix-18) |
| `library/lectures/lec-01/deck.yaml` | s19a entry added; v3.2 metadata + fix list; pacing updated |

## Slide count: 33
- v3.1 had 32 slides.
- +1 (NEW s19a) → 33.

## Pacing
- Active: 62.5 min (was 62.0; +0.5 from s19 split).
- Buffer: 12.5 min (was 13.0).
- Total: 75 min preserved.
- Section 3 (4 ways): 23.0 min (was 22.5; +0.5 from s19 split).

## Ready for next phase?

YES.

Recommended next steps:
1. **speech-writer Opus** — update speech.md to reflect:
   - New s19+s19a split (200 PDF + autonomy levels).
   - New s09 episodes (OpenClaw, Kimi K2.5).
   - s07 Vaswani callout instead of AI Effect duplicate.
   - s17 production disclaimer instead of bar chart.
   - s28 simplified homework.
   - s29 + chapter module reshuffle (Лекция 6 → М2, Лекция 8 → М3).
   - s16 dialog cycle visual (was 6 linear steps).
2. **Sanity check by 1 critic** (presentation-critic or student-simulator) on the 33-slide deck.
3. Present to user for accept.

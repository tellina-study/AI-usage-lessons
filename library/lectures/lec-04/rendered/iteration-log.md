# Лекция 4 (lec-04) — Iteration log, часть 2

> **Начало** (v1 → Phase 8.7) — в [`iteration-log-part1.md`](iteration-log-part1.md). Этот файл — продолжение (Phase 8.8 + перенумерация #92).

## Phase 8.8 — Surgical 13-fix iteration (Лекция 4)

User feedback after v4 deck (commit `8bd889e`) — 13 точечных issues. Applied
all 13 без general redesign.

### Fixes applied (13/13)

| # | Slide | Fix | Status |
|---|---|---|---|
| 1 | s02 | Удалить footer line «Курс · 75 мин · 13 мая 2026» — minimal cover | DONE |
| 2 | s05 | Удалить «ЦЕНТРАЛЬНЫЙ ВОПРОС ЛЕКЦИИ» banner | DONE |
| 3 | s05 | Удалить footer «Стейкс: $22–38 млрд …» (anglicism + irrelevant) | DONE |
| 4 | s06 | Удалить editorial commentary footer «Фокус лекции — квадранты с золотой подсветкой…» | DONE |
| 5 | s06 | Упростить axes (Option A): single-word «изображения / текст», «один пациент / популяция»; «модальность» как side-label | DONE |
| 6 | s08, s05b | «инструктивный пример» / «инструктивный кейс» → «показательный кейс» | DONE |
| 7 | s10, s19 | Specificity definition: «не напуганных» → «верно классифицированных как здоровые»; aligned all 4 metric definitions | DONE |
| 8 | s11 | Title: «парадокс augmentation» → «AI один сильнее тандема врач+AI» (Russian-pure); also third row Goh insight rewritten | DONE |
| 9 | s19 | Micro-exercise → lecture content «AI как объяснитель» (3 мин, no student activity); раздел 4 «Микро-упражнение» удалён; structure 6→5 sections; s18a divider removed | DONE |
| 10 | s05, s08, s14, s20, s27 | Photo captions updated «Иллюстрация: …» (honest acknowledgment; no specific Russian context claim) | PARTIAL |
| 11 | s20 | 3 items enriched with 1-2 sentence explanation + scale stat per item | DONE |
| 12 | s13, s21 | «Black-пациентов» → «чернокожих пациентов» (Russian convention, all instances) | DONE |
| 13 | s29 | Remove 3 backup discussion prompts; minimal Q&A («Вопросы?» + «Спасибо за внимание») | DONE |

### Section restructure (Fix 9 cascade)

- **Was:** 6 sections (0–6), 7 cards on progress bar.
- **Now:** 5 sections (0–5), 6 cards on progress bar.
- **Deleted:** Section 4 «Микро-упражнение» (s18a divider).
- **s19** теперь lecture content в Section 4 «Этика и ответственность» как
  natural intro к LLM-границам.
- **s19a frame_phrase** обновлён: «AI как объяснитель · Obermeyer · NEDA Tessa
  · Change Healthcare · 4 актёра».
- **s24a** теперь section 5 (было 6), `here_idx=5`.
- **deck.yaml:** LO4 dropped из `learning_outcomes` (was apply-based для
  micro-exercise; больше нет student activity); s18a entry deleted; s19
  updated to `duration_min=3` + new assertion/learning_outcomes.

### Build pipeline (Phase 8.8)

Files edited:
- `rendered/build_lec04.py` (13 surgical edits — see Fix numbers)
- `slides/s19-micro-exercise-llm-explainer.md` (FULL REWRITE — micro-exercise → AI explainer)
- `slides/s19a-section5-divider.md` (section number 5→4 + frame_phrase update)
- `slides/s24a-section6-divider.md` (section number 6→5 + speaker notes update)
- `deck.yaml` (LO4 drop, s18a entry remove, s19 metadata update, s19a/s24a section numbers)
- `iteration-log.md` (this entry)

Assets added:
- `assets/icons/lucide-book-open-blue.png` (для s19 cards)
- `assets/icons/lucide-graduation-cap-blue.png` (для s19 cards)

### Iterations breakdown (Phase 8.8)

| Iter | Focus | Outcome |
|---|---|---|
| 1 | Apply fixes 1–4, 6, 7, 12, 13 (simple text edits) | Build OK |
| 2 | Apply fix 8 (s11 title) + fix 11 (s20 enrichment) | Build OK |
| 3 | Apply fix 5 (s06 axes Option A) + fix 9 (s19 micro→lecture, section 6→5) | Build OK after restructure of NAV_SECTIONS + builders list |
| 4 | Apply fix 10 (photo captions «Иллюстрация: …») | Build OK |
| 5 | Re-render full deck (libreoffice → pdftoppm) — 34 snapshots | Generated |
| 6 | Vision review — identified s06 «МОДАЛЬНОСТЬ» wrapping issue + s11 title clip | Found |
| 7 | Iter 2 fixes: s06 axis label restructure (horizontal markers) + s11 title height 1.15→1.35 + row_y shift | Re-rendered, accepted |

### Forbidden patterns final scan (0 expected)

- `augmentation`: 2 matches — both inside `# Fix 8 (Phase 8.8): «парадокс augmentation» → …` comments. ✅
- `Black-`: 0 matches (BlackCat ransomware name preserved as proper noun).
- `инструктивн`: 2 matches — both in `# Fix 6 (Phase 8.8): «инструктивный кейс» (anglicism) → …` comments. ✅
- `не напуганн`: 1 match — inside `# Fix 7 (Phase 8.8): «не напуганных» → …` comment. ✅
- `Стейкс`: 1 match — inside `# Fix 3 (Phase 8.8): footer line «Стейкс: …» удалена` comment. ✅

### Final deck stats (Phase 8.8)

- **Total slides:** 34 (was 35 in 8.7; −1 после удаления s18a).
- **Section dividers:** 5 (was 6; −1 после удаления Section 4).
- **Progress bar cards:** 6 (was 7).
- **Sections:** 5 (0..5; was 6: 0..6).
- **LOs in deck:** LO1, LO2, LO3, LO8 (was LO1..LO4, LO8; −LO4).
- **Photos with «Иллюстрация:» honest captions:** 5 (s05, s08, s14, s20, s27).

---

# Issue #92 — Renumber 4→7 downstream cascade (deck artifacts)

**Issue:** #92 · **Branch:** issue-92-lec-04-renumber-l7 · **Date:** 2026-05-16
**Scope:** deck-only (chapter/speech уже обновлены book-first; qa-reports не трогались).
**Source of truth:** chapter.md §5.2/§5.3 + speech.md s28 block (canon-true).

## Changed slides (4) — verified via pptx-vs-HEAD slide-by-slide diff

| Slide | Change |
|---|---|
| s02 cover | decorative «04»→«07»; assertion/title «Лекция 4»→«Лекция 7» |
| s24a divider | frame_phrase «тизер Лекции 6»→«что дальше»; notes canon-sync (L9→L17) |
| s26 takeaways | card3 «Личная версия → Лекция 14»→«Финал — Лекция 17»; gold-strip + notes canon-sync |
| s28 what-next | full rewrite: removed Коллоквиум1 / Лекция6=производство teaser / Lec9 arrow / Lec14; new 2-card number-neutral forward + копилка→Лекция 17 |

30 slides byte-identical (text+notes) vs git HEAD pptx — no collateral regression.

## Visual loop — s28 (≥3 iter)

### Iter 1 — s28
- (a) inspected: new 2-card layout, canon-correctness, mass balance.
- (b) changed: rebuilt build_s28 (2 Ocean cards, trending-up + list-checks
  icons, gold highlight «четвёртая отраслевая лекция», gold-strip L17).
- (c) pass: canon PASS (0 violations), palette/motif PASS; FAIL Visual Mass
  Balance — Card 2 ~30% empty vs dense Card 1.

### Iter 2 — s28
- (a) inspected: card-vs-card mass balance.
- (b) changed: each obs = bold term + canon §5.3 gloss (2-line blocks),
  closing line color LIGHT→MID.
- (c) pass: mass improved; FAIL — reverse imbalance, Card 1 now emptier
  (~40% bottom whitespace) than Card 2.

### Iter 3 — s28 (ACCEPT)
- (a) inspected: symmetric structure, projector readability, 5-sec test.
- (b) changed: Card 1 body → 13pt + italic closing line «Принципы
  переносятся…» at card_y+3.62 (parallel to Card 2 closing line).
- (c) pass: Visual Mass Balance PASS (both cards end ~card_y+3.97),
  Schema(matrix/2-card) PASS, Projector 50% PASS (min 11pt italic),
  5-Sec PASS (main msg = assertion).

## 5-Second Test — final accept gate (all PASS)

- s02: read «AI в медицине · Лекция 07» = assertion. PASS.
- s24a: read «Заключение · 3 наблюдения · что дальше · Q&A» = assertion. PASS.
- s26: read «3 вывода + 3 принципа→копилка, финал L17» = assertion. PASS.
- s28: read «медицина=4-я отраслевая, тур продолжается, копилка→L17» = assertion. PASS.

## Canon scan — 0 violations

pptx full-text + notes regex scan: 0 hits of «Лекция 4/6/9/14», «Коллоквиум»,
«Практикум», «Cognitive/Agro Pilot». Cover decorative number = «07».

## Notes word counts (changed slides)

s28=197, s26=248 (both within [150,300]). s02=108, s24a=104 — cover/divider
non-content slides, short by design, pre-existing (not lengthened by #92).

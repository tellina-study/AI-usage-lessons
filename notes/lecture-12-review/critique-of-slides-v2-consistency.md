---
critique_of: chapter v3 ↔ slides v2 alignment
critic: consistency-checker (verification pass v1 → v2)
verdict: APPROVE-CLEAN
previous_verdict: REVISE (1 P0 + 2 P1 + 1 P2)
created: 2026-05-22
---

# Verification summary

Slides v2 closes **all 4 items** from v1 critique: 1/1 P0, 2/2 P1, 1/1 P2.

- **P0 D1 (s17 PLC compile contradiction)** — **CLOSED**. Rendered visible body now reads «**Код скомпилируется в TIA Portal без ошибок** … но в режиме исполнения PLC уйдёт в **STOP-mode** — остановка всего оборудования» + «Корневая причина. Универсальная языковая модель не знает циклическое исполнение и допустимые адреса конкретной модели». Speaker notes mirror exact chapter §3.4 language: «Адрес %M99999 синтаксически валиден — код **скомпилируется** в Siemens TIA Portal без ошибок синтаксического анализатора. Но при попытке исполнения PLC обнаружит обращение за пределы адресного пространства M и уйдёт в режим STOP». Pedagogical message of §3.4 («compile ≠ run safely», AI выдаёт plausible code that compiles) **fully preserved** на rendered body AND notes.
- **P1 D2 (LO8 phantom)** — **CLOSED**. `grep -rn "LO8"` across `slides/*.md` + `deck.yaml` returns 0 hits. All 3 v1 references in s03 + s28 + s39 speaker notes удалены.
- **P1 D3 (s20 Yokogawa premier-minister 2023 cascade-edit gap)** — **CLOSED**. Speaker notes теперь: «Алгоритм отмечен **индустриальными наградами** за вклад в промышленный ИИ; точная атрибуция награды не критична для архитектурного разбора». Exact match с chapter-part2.md §4.2 line 222 «Алгоритм FKDPP был отмечен индустриальными наградами … точная атрибуция не критична». Rendered visible body s20 PNG shows «отмечен индустриальными наградами» в FKDPP info card. NO premier-minister claim, NO 2023 award year.
- **P2 D4 (Edge AI / Крайний AI drift on s33 visible body)** — **CLOSED on the specific surface flagged**. Rendered s33 visible body now reads «**3. ИИ на границе сети**» (canonical RU per chapter §6.3) + subtitle «OPC UA + TSN + **ИИ на границе сети** inference <10 мс». «Edge AI» **больше не появляется как primary surface form** на rendered visible body s33. Чистая RU canonical surface as advised.

**Verdict APPROVE-CLEAN justified:** 4/4 v1 issues closed; v2 introduced no new P0/P1 drift; numbers re-sample (10 samples) 10/10 match. Residual «edge AI» mentions in speaker notes of other slides (s32, s33, s34, s38, s04, s25) — within chapter-defined gloss permission («edge AI (крайний / локальный ИИ-инференс)», chapter.md line 101) and не contradict canonical. Glossary-lock decision deferred to USER GATE B is **not blocking** — chapter explicitly allows both surfaces as gloss pair.

# Issue closure status

## P0 D1 — s17 PLC compile/run inversion → CLOSED

**v1 problem (visible body):** «Адрес %M99999 не существует — PLC откажется компилировать» (inverted §3.4 pedagogical message).

**v2 rendered visible body (`rendered/snapshots/s-17.png`, verified):**
- «**Код скомпилируется в TIA Portal без ошибок**»
- «но в режиме исполнения PLC уйдёт в **STOP-mode** — остановка всего оборудования»
- «**Корневая причина.** Универсальная языковая модель не знает циклическое исполнение и допустимые адреса конкретной модели»

**v2 speaker notes (s17-plc-copilot-vs-chatgpt.md line 14):**
> «Адрес %M99999 синтаксически валиден — код скомпилируется в Siemens TIA Portal без ошибок синтаксического анализатора. Но при попытке исполнения PLC обнаружит обращение за пределы адресного пространства M и уйдёт в режим STOP — то есть остановит всё оборудование … Это не „иногда галлюцинирует", это структурное ограничение.»

**Chapter §3.4 (chapter-part2.md anchor) reference:**
> «Этот код **скомпилируется** в Siemens TIA Portal без видимых ошибок синтаксического анализатора. Что не так. Этот код **не запустится на S7-1500**. … Адрес вне адресного пространства приводит к остановке PLC в режим STOP.»

**Match:** exact. Both rendered visible body AND speaker notes now correctly preserve §3.4 pedagogical inversion (compile-time success ≠ runtime safety, AI выдаёт plausible code that compiles — это и есть danger).

## P1 D2 — LO8 phantom across s03/s28/s39 → CLOSED

**Grep verification (worktree):**
```
grep -rn "LO8" /tmp/lec-12-wt/library/lectures/lec-12/slides/ /tmp/lec-12-wt/library/lectures/lec-12/deck.yaml
→ 0 hits
```

**v2 speaker notes (verified line-by-line):**
- s03 (lecture-map) line 16: «**центральный результат лекции для LO7**» (only LO7, no LO8)
- s28 (10 criteria matrix) line 14: «**центральный результат лекции для LO7**» (only LO7)
- s39 (closing) line 18: «**центральный результат лекции для LO7**» (only LO7)

All 3 v1 «и LO8» orphan references удалены. Chapter frontmatter declaration `learning_outcomes: [LO2, LO5, LO7]` теперь fully synced со speaker notes.

## P1 D3 — s20 Yokogawa premier-minister cascade-edit gap → CLOSED

**v1 problem (speaker notes):** «За эту работу команда Yokogawa получила премию премьер-министра Японии в 2023» — definitive without caveat, contradicting chapter `[FACT-CHECK]` marker.

**v2 speaker notes (s20-yokogawa-fkdpp.md line 14):**
> «Алгоритм отмечен **индустриальными наградами** за вклад в промышленный ИИ; **точная атрибуция награды не критична для архитектурного разбора**.»

**v2 rendered visible body (`rendered/snapshots/s-20.png`, FKDPP info card):**
> «Yokogawa + NAIST, 2018 · off-policy RL · факториальная ядровая декомпозиция · **отмечен индустриальными наградами**»

**Chapter §4.2 (chapter-part2.md line 222) reference:**
> «Алгоритм FKDPP был отмечен **индустриальными наградами** за вклад в промышленный AI [FACT-CHECK: точная награда — verify через press release Yokogawa]. **Точная атрибуция не критична для дальнейшего изложения**.»

**Match:** exact. NO premier-minister claim. NO 2023 year. NO definitive METI/PM attribution. Lecturer cannot accidentally voice an unverified definitive claim — wording explicitly punts attribution.

## P2 D4 — Edge AI / Крайний AI surface form on s33 visible body → CLOSED

**v1 problem (rendered s33 visible body):** layer 3 label was bare English «**Edge AI**».

**v2 rendered visible body (`rendered/snapshots/s-33.png`, verified):**
- Subtitle: «OPC UA + TSN + **ИИ на границе сети** inference <10 мс — операционные условия для A2»
- Layer 3 row: «**3. ИИ на границе сети** … промышленные ИИ-серверы на шкафах оборудования · инференс <10 мс (NVIDIA Jetson)»

**Chapter §6.3 (chapter-part3.md) canonical:**
> «**§6.3. Крайний AI: ИИ на границе сети, инференс менее 10 мс**»

**Match (on s33 visible body):** RU canonical preserved. The bare English «Edge AI» as layer label on rendered PNG — removed. «ИИ на границе сети» — surface form aligned with chapter §6 chapter-part3 §6.3 title gloss «ИИ на границе сети».

**Note (NOT blocking):** «edge AI» appears in speaker notes of s32 (divider), s33 (notes line 14 — for «Слой третий: edge AI»), s34 (assertion + notes), s04 / s25 (notes), s38 (assertion + role 4). Chapter.md line 101 explicitly defines this как gloss-pair: «**edge AI** (крайний / локальный ИИ-инференс)». Chapter-part4 line 314 lists «**Крайний AI engineer** (edge AI engineer) — рост 30%+» as career role canonical. Speaker-notes gloss usage is **within chapter-defined gloss permission**. The specific D4 surface (s33 visible body) is now canonical RU. Glossary lock can finalize this in a follow-up but is non-blocking.

# Numbers re-sample (10 total — 5 new, plus 5 from v1)

| # | Claim | Chapter location | Slide location | Match |
|---|---|---|---|---|
| 1 | $36.19B → $180.28B CAGR 37.87% | chapter.md line 99 + §1.3 | s08 visible chart («36.19» → «180.28») + notes line 14 («36,19 → 180,28 миллиарда, темп 37,87%») | ✓ exact |
| 2 | 75% twin fail / 11% O&G / 14% expectation | chapter.md line 99 + §1.4 line 265 + 282 | s08 notes («75%, 11%, 14%») + s30 («75% twin без ROI / 11% O&G / 14%») | ✓ exact |
| 3 | PdM ROI 10:1 за 2 года | chapter.md §2.3 | s13 assertion + notes line 14 «ROI 10 к 1 за 2 года» | ✓ exact |
| 4 | Yokogawa FKDPP / JSR / 35 days / 2022 | chapter-part2 §4.2 lines 220-224 | s20 assertion + notes line 16 «35 дней непрерывной … JSR в 2022» | ✓ exact |
| 5 | Lighthouse 220+ / 35 стран / 23 новых / 90% / +16% EBIT | chapter-part3 §6.4 line 336+ | s35 notes line 16 «220+ заводов в 35 странах … 23 новых … 90% … плюс 16%» | ✓ exact |
| 6 | **NEW:** Pharma FDA ±0.1% vs AI ±0.5% (gap 5×) | chapter-part3 §5.3 lines 187-200 | s29 visible matrix + notes line 16-20 «±0,5% vs ±0,1% … gap … несовместимо» | ✓ exact (5× gap explicit в chapter line 200) |
| 7 | **NEW:** PdM $200K-$600K → $1.2M-$3.5M / 18-36 мес | chapter.md §2.3 | s13 notes line 16 «от 200 тысяч до 600 тысяч … от 1,2 до 3,5 миллионов … 18 до 36 месяцев» | ✓ exact |
| 8 | **NEW:** Cement 57× ROI за 6 месяцев / Chemical $2M | chapter.md §2.3 | s13 notes line 18 «Cement plant: 57× ROI за 6 месяцев … Chemical plant: 2 миллиона долларов годовой экономии» | ✓ exact |
| 9 | **NEW:** PLC code 3-4 дня → 10 мин / 85% точность / 15% engineer-catch | chapter-part2 §3.3 | s17 assertion + notes line 16 «3–4 дня инженерной работы, делается за 10 минут … 85% точности … 15% ошибок ловит инженер» | ✓ exact |
| 10 | **NEW:** $17.15B OPC UA + MQTT AI 2026 | chapter.md line 99 + §6.2 | s08 visible («17.15») + notes line 14 «17,15 миллиарда в 2026» | ✓ exact |

**10/10 numbers match.** Fidelity preserved через v1→v2 revision.

# New drift items (introduced by v2 revision)

**None.** Revision was minimal-scope (text edits only for D1/D2/D3/D4 — no structural changes, no new claims). Re-grep verified:
- `grep -rn "LO[0-9]" slides/ deck.yaml` → only LO2/LO5/LO7 (chapter-declared) appear; no LO1/LO3/LO4/LO6/LO8/LO9 phantom references.
- `grep -rn "премьер\|premier\|2023" slides/s20*` → 0 hits.
- `grep -rn "откажется компилир\|refuse compile" slides/s17*` → 0 hits.
- s33 visible body PNG re-inspected: layer 3 = «ИИ на границе сети» (canonical).

No regressions. No new orphan slide references, no new cross-lecture leaks, no new numbers drift.

# Self-checks (v2)

- [x] **All 4 v1 issues closed** (1/1 P0 + 2/2 P1 + 1/1 P2)
- [x] **No new drift** introduced by revision
- [x] **Numbers re-sample 10/10 match** (extended from 5 to 10 samples)
- [x] **Pedagogical inversion preserved** on s17 (compile ≠ run safely — key §3.4 lesson)
- [x] **Cascade-edit closure** on s20 (chapter v3 wording «индустриальными наградами» now in slide)
- [x] **Phantom LO grep 0 hits** across all slides
- [x] **s33 rendered visible body** uses canonical RU «ИИ на границе сети» (D4 specific surface resolved)
- [x] **Frontmatter LO declaration** `[LO2, LO5, LO7]` matches all speaker notes (no LO8 orphan)
- [x] **Chapter source-of-truth principle preserved** — no chapter edits required; all fixes applied to slides side per book-first methodology

# Verdict justification

**APPROVE-CLEAN.** All 4 v1 issues (1 P0 + 2 P1 + 1 P2) closed cleanly with chapter-aligned wording on both rendered visible body AND speaker notes. Numbers fidelity preserved 10/10. No new drift introduced. Pedagogical message of §3.4 (the most important fix, P0 D1) восстановлена exactly as chapter intends. s20 cascade-edit gap closed without overclaim. Phantom LO removed. Glossary surface on s33 visible body now canonical RU.

**Promotion v1 REVISE → v2 APPROVE-CLEAN justified by:** (a) all flagged P0 closed with verified rendered evidence (PNG inspected, not just .md text), (b) speaker notes language now mirrors chapter §-level wording (which is the strongest possible cross-artifact alignment), (c) no quality regression in numbers / coverage / structure, (d) chapter source-of-truth preserved without edits.

**Recommendation:** slides v2 can proceed to Phase 9 (speech production). Speech-writer should source from chapter v3 + slides v2 (NOT v1) to inherit corrected wording.

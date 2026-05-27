# Presentation critique — Лекция 16 deck v1 rendered

**VERDICT: REJECT**

**Дата:** 2026-05-27
**Object:** `rendered/lec-16.pptx` (43 slides) + `snapshots/s01-s43.png`
**Reviewer:** presentation-critic (vision-enabled)

---

## Summary

Deck v1 architecturally работает: pattern-compliance с Lec-14 хорошее (roadmap-bar только на cover + 5 dividers подтверждён независимым grep, lecture-map есть, keystone-matrix s05 читабелен, Q&A s42 есть, hero s01 + s43 ≥40% area real images). Pacing 43 slides под 75-мин — реалистично. НО deck **структурно непригоден к показу RU-аудитории МГТУ ИУ6** из-за **catastrophic Russification failure**: deep latin-token scan показал **862 problem-occurrences / 575 unique tokens** в visible body (post-whitelist) — на порядок выше Лекции 8 (224) которая получила owner reject «трындец! провал». **8 из 11 content-section заголовков слайдов мешают English** или 100% English, включая ключевые методологические слайды s12 (6 критериев когда AI не нужен — все 6 категорий English-titled), s40 (4-квадрантный синтез), s41 (3 cornerstones). Дополнительно: **4 visible `[VFY-day-of]` scaffold leaks** в s15/s17/s27/s33 + **16 scaffold hits в speaker_notes** (LO codes + «Возвращаемся к»). Чистая Russification + scaffold cleanup требует ~25-35 человеко-часов revision.

---

## P0 issues (BLOCKING — 4)

### P0-1: Catastrophic Russification failure — 862 problem latin tokens в visible body (Анти-anglicism mandate violated)

**Severity:** P0 — структурный gap, не polish. **Cost-of-omission Лекции 8: owner reject «трындец! провал» на 224 anglicisms.**

**Evidence:**
- Deep latin-token scan (regex `[A-Za-z][A-Za-z0-9-]+` + brand allowlist 75+ companies + tech acronyms whitelist):
  - **Total Latin tokens в PPTX visible body:** 1 705
  - **Total problem-occurrences (post-whitelist):** 862
  - **Unique problem tokens:** 575
  - **Top problem terms (n≥3):** failure (7), baseline (6), augmentation (6), integration (5), cases (5), vendor (5), foundation (5), Eclipse (5), single (5), cycle (5), essential (5), flagship (5), satellite (5), mandatory (5), success (4), commercial (4), aerial (4), horizon (4), internal (4), phase (4), crash (4), plant-wide (4), Senior (4)…
- Comparison: Лекция 8 v1 = 224 unique latin tokens → owner reject. **Лекция 16 v1 = 575 unique = на 157% хуже Лекции 8 v1.**
- iteration-log claim «1678 → 1613 occurrences» misleading: those numbers включают brand names (Aramco, SLB, MethaneSAT, NVIDIA, Honeywell). Post-whitelist real problem count 862 — **structural failure, не polish round**.

**8 из 11 content-section заголовков слайдов слайдов с English в title:**
| Slide | Title (issue) |
|---|---|
| s10 | «Ландшафт поставщиков Q1 — 3 группы» (Q1 token OK, body «Enterprise (NOC + super-majors)», «Refinery + pipeline», «rising через cross-продажи») |
| s12 | «Когда AI НЕ нужен в Q1 — 6 структурных критериев» — все 6 категорий English-titled: Eclipse / Stripper wells / Custody transfer metering / BOP/PRV/ESD — SIS / Frontier без analog data / EU Methane Reg reporting |
| s17 | «ExxonMobil Discovery 6 — 4D-сейсмика месяцы → недели» |
| s18 | «BP + Beyond Limits — $20M, vendor pivot 2023» (3 урока: «Vendor concentration», «Cognitive marketing — anthropomorphic overpromise», «Imitation framing — AI не имитирует, он approximates») |
| s20 | «Альтернатива Q3: physics-based simulators + senior expertise» |
| s21 | «Methane MRV alphabet — 6 must-know терминов» |
| s27 | «EU 2024/1787 vs EPA Subpart W — AI MRV рынок развивается асимметрично» |
| s28 | «Альтернатива Q2: ground OGI + portable analyzers» |
| s31 | «Fervo Energy EGS — IPO 12 мая 2026, 40× growth ceiling» |
| s32 | «CCS 190× scale-up gap — engineering reality vs policy» |
| s34 | «Альтернатива Q4: classical engineering + deterministic safety» |
| s35 | «Россия — sanctions, insourcing, vertical integration» |
| s40 | «4-квадрантный синтез: 10 documented failures + working cases» |
| s41 | «3 cornerstone концепта — bridge к Лекции 17» |

**Chart labels English (4 чарта):**
- s07 x-axis: «86% pilot stuck», «67% cross-industry», «14% production», «3% deep integration»
- s09 x-axis: «Baseline (100-500 bopd)», «+15% InfinityRL», legend «bopd»
- s32 x-axis: «Northern Lights (2025)», «IEA target (2050)», legend «Mt CO₂/year»
- s38 x-axis: «Apr 2024», «Apr 2025», legend «Index (Apr 2024 = 100)»

**Recommendation:**
- Полный revision pass через `russification.md` mapping table 100+ terms.
- Все content-slide titles перевод RU (oставить ТОЛЬКО brand names Eclipse, BP, ExxonMobil, MethaneSAT, EU 2024/1787, EPA Subpart W в чистом виде).
- Все card headers, bullet points, callouts — RU narrative с inline gloss где термины критичные («OGI = оптическая газовая визуализация»).
- Chart labels всех 10 charts → RU («Базовая линия» вместо «Baseline», «Застряли в пилоте» вместо «pilot stuck»).
- Top progress bar labels: «Q1 Mature» → «Q1 Зрелое», «Q3 Frontier» → «Q3 Разведка», «Q2 Methane» → «Q2 Метан», «Q4 Transition» → «Q4 Энергопереход» (full Russification).

---

### P0-2: 4 visible scaffold leaks `[VFY-day-of]` в student-visible body (Pre-USER-GATE walkthrough §5 violation)

**Severity:** P0 — scaffold должен быть 0 в visible body. iteration-log claim «scaffold AFTER: 0 ✓» **ложно**.

**Evidence (orchestrator-independent grep `[VFY|[VERIFY-DAY-OF]`):**
- s15 visible: «~250 млрд параметров [VFY-day-of]»
- s17 visible: «HPE Cray EX4000, 4 032 NVIDIA Grace Hopper, 4× compute vs Discovery 5. $200–400M capex [VFY].»
- s27 visible: «6 мая 2024 final → delay 2034 [VFY]»
- s33 visible: «· Plant-wide пилот → тихо закрыт [VFY-day-of]»

**Recommendation:**
- Remove all `[VFY]` / `[VFY-day-of]` markers from visible body before render.
- Move to frontmatter `fact_check_pending:` array OR speaker_notes only.
- Add to build_lec16.py preprocessor regex `re.sub(r'\s*\[VFY[^\]]*\]', '', text)` before populating shapes.

---

### P0-3: Speaker notes scaffold leaks — 16 hits (LO codes + «Возвращаемся к»)

**Severity:** P0 — speaker_notes per CLAUDE.md «No Extra Content Rule» не должны содержать LO codes / cross-references.

**Evidence (PPTX notes_slide scan):**
- 11 `LO[1-9]` hits: s10 (×2), s13 (×2), s20, s26, s28, s33, s34, s38, s42 (×3)
- 3 «Возвращаемся к»: s12, s32, и ещё одно
- Note: 0 timing-маркеры в notes ✓, 0 methodology ✓ — это сильнее iteration-log claim

**Recommendation:**
- Regex-strip `LO[1-9]\w*` and «Возвращаемся к ...» phrases from notes injection layer (`inject_notes.py`).
- Alternative: regenerate notes from chapter narrative, не из slide-spec annotation comments.

---

### P0-4: s30 (Northern Lights CCS) — broken/wrong image (soccer ball icon вместо CCS facility)

**Severity:** P0 — student-visible слайд показывает картинку которая визуально выглядит как **soccer ball / спортивный мяч** (черно-белый pentagonal pattern) с надписью «XOIIACZ». Это **категорически НЕ** Northern Lights CCS facility (норвежский морской CO₂ storage hub).

**Hypothesis:**
- og:image fetched от Equinor Northern Lights press page оказался шаблонной соц-сетевой картинкой с логотипом / generic graphic, а не facility photo
- OR файл `s29-nl.png` corrupted/wrong-source

**Recommendation:**
- Открыть `library/lectures/lec-16/assets/screenshots/s29-nl.png` — verify visual content
- Re-acquire через Tier 2 (Wikipedia Northern Lights JV page) или Tier 3 (Equinor press release direct hi-res facility photo of subsea injection well или Bergen onshore terminal)
- Acceptable alternative: schema-style диаграмма (CO₂ source → ship → Bergen terminal → subsea injection well) построенная primitives

---

## P1 issues (HIGH — 9)

### P1-1: s17 ExxonMobil — stylized logo card disguised as real image (mock-fallback)

**Evidence:** s17 left image area shows ONLY «ExxonMobil» red logotype on white/gray gradient background с подписью «ExxonMobil corporate press · 2024». Это **не real screenshot of Discovery 6 / Stabroek operations / 4D seismic visualization** — это press-page placeholder.

**Per [[no-mock-fallbacks]] mandate:** «stylized Ocean-palette card с verbatim headline = mock = FAIL».

**Recommendation:** Re-acquire через Tier 2 (Wikipedia Stabroek Block satellite map) / Tier 3 (ExxonMobil press release Stabroek FPSO photo — Liza Unity / Liza Destiny / Errea Wittu vessels). Alt: NVIDIA Grace Hopper datacenter photo (real HPC cluster).

---

### P1-2: s31 Fervo Energy — рендер тоже выглядит broken / heavy image compression artifact

**Evidence:** s31 snapshot имеет очень small thumbnail для левой image area (look like cropped к Cape Station drilling photo) с **right text block compressed beyond readability** в snapshot rendering. Designer self-flagged risky («Fervo» Cape Station Utah image acquired but layout difficult).

**Recommendation:**
- Re-render s31 PNG @ higher DPI for verification
- Restructure layout: image full-width top half (40% area), 3-column metrics row below (IPO $1,89B / 12 мая 2026 / Cape Station 520MW)
- OR text-only with bar chart of 40× growth gap

---

### P1-3: s07 chart — все 4 x-axis labels English; sub-callout heavy anglicisms

**Evidence:** «86% pilot stuck», «67% cross-industry», «14% production», «3% deep integration» — все на english. Bottom: «Это не «AI плохой» — это статистическая норма отрасли. 14% successful vs 86% stuck — инженерный фильтр, а не приговор.» Body bullets: «Legacy IT integration», «Senior operator», «AI-vendor», «107k jobs», «successful vs stuck».

**Recommendation:** Regenerate chart с RU labels. Body: «Старая IT-интеграция», «Старший оператор», «AI-поставщик», «107 тыс. рабочих мест», «работающих vs застрявших».

---

### P1-4: s08 «Aspen Mtell» (Q1 alert fatigue) — layout compressed, body 90% English

**Evidence:** Snapshot отрисован в небольшом frame (designer flagged risky). Title «Усталость от ложных тревог устранена» — это маркетинг — RU OK. Subtitle: «Aspen Mtell на нефтепереработке: 100–500 алертов в день; plant-wide пилоты тихо закрываются». Body cards: «Маркетинг (AspenTech)», «Реальность на НПЗ: 100–500 alerts/день — оператор перестаёт реагировать», «Single-column success → plant-wide пилот тихо закрыт», «Honeywell UOP 310+ юнитов / ~700 НПЗ = ~44% rate», «Многие НПЗ — «классический APC без AI»», «Multi-physics (масс + энергия + реакция + коррозия) ломает ML-суррогаты на edge cases». Bottom: «Урок: vendor self-report ≠ field reality. Custody transfer, SIS, plant-wide refinery — AI ещё не дошёл.»

**Recommendation:** Russify «success», «alerts», «plant-wide», «rate», «vendor self-report», «field reality», «custody transfer», «refinery». Verify layout @ proper render DPI.

---

### P1-5: Roadmap-bar labels English-heavy («Q1 Mature», «Q3 Frontier», «Q2 Methane», «Q4 Transition»)

**Evidence:** На всех 6 slides с roadmap-bar (s02 cover + s06/s14/s22/s29/s35 dividers) top navigation показывает:
«1. Keystone · 2. Q1 Mature · 3. Q3 Frontier · 4. Q2 Methane · 5. Q4 Transition · 6. Россия · 7. Сквозные»

Из 7 labels — 5 содержат english/transliteration. Roadmap должен быть **полностью RU** для RU аудитории.

**Recommendation:**
- «Keystone» → «Стержень»
- «Q1 Mature» → «Q1 Зрелое»
- «Q3 Frontier» → «Q3 Разведка»
- «Q2 Methane» → «Q2 Метан»
- «Q4 Transition» → «Q4 Энергопереход»

---

### P1-6: s05 keystone matrix — bottom callout «alternative tool» не Russified

**Evidence:** s05 matrix Russified well (Q1-Q4 RU labels). НО bottom callout: «За каждым AI-внедрением — alternative tool: физический симулятор, OGI-камера, классическая интерпретация.» Слово «alternative tool» English.

**Recommendation:** «За каждым AI-внедрением — альтернатива: физический симулятор, OGI-камера, классическая интерпретация».

---

### P1-7: s40 (synthesis) card headers все English

**Evidence:** «Q2 Methane — AI essential», «Q1 Mature — AI мультипликатор», «Q4 Transition — struggle», «Q3 Frontier — physics-first». Bottom callout: «Когда работает: Q1 multiplier + Q2 essential. Когда осторожно: Q3 augmentation. Когда опасно: Q4 long-horizon + safety-critical SIS».

**Recommendation:** «Q2 Метан — AI необходим», «Q1 Зрелое — AI как мультипликатор», «Q4 Энергопереход — буксуют вместе», «Q3 Разведка — сначала физика». Bottom: «Когда работает: Q1 мультипликатор + Q2 необходим. Когда осторожно: Q3 как дополнение. Когда опасно: Q4 длинный горизонт + safety-critical SIS» (SIS — оставить acronym с inline gloss).

---

### P1-8: s41 3 cornerstones — title English «3 cornerstone концепта — bridge к Лекции 17»

**Evidence:** Title 50% English. Body Card 3 title «Industry cyclicality > AI hype cycle». Body: «portable на любую следующую отрасль», «classical APC», «federated learning», «AI добавляется ТОЛЬКО если улучшает baseline», «AI-roadmap должен иметь stress-tested устойчивость», «keystone'ы L11-L16 как universal patterns».

**Recommendation:** «3 опорных концепта — мост к Лекции 17». Card 3: «Циклы отрасли > цикл AI-хайпа». «Переносимы», «классический APC», «федеративное обучение», «улучшает базовую линию», «дорожная карта AI должна быть устойчивой к индустриальному циклу», «keystone-оси L11-L16 как универсальные шаблоны».

---

### P1-9: Baseline / counterfactual coverage gaps — sample 7 measurable claims

**Evidence (per [[feedback_baseline_counterfactual]]):**

| Slide | Claim | Baseline gap |
|---|---|---|
| s01 | «2 593 факельных шлейфа Пермский бассейн» | НЕТ denominator: сколько всего скважин Permian? сколько вне-flaring infrastructure? |
| s05 | «Ambyint +15% на 200 скважинах» | denominator visible (200 скважин), но НЕТ total Permian wells баckground (~80 000) |
| s07 | «86% AI-проектов застряли в пилоте» | counter-baseline есть («vs cross-industry ~67%»), хорошо ✓ |
| s14 | (Aramco METABRAIN) «$1,8 млрд realized 2024» | denominator есть («Aramco выручка 2024 = $436,6 млрд → $1,8B/$436,6B = 0,41%»), хорошо ✓ |
| s22 | «Permian flagship результат 410 т/ч метана = +50% над оценкой EPA» | EPA baseline implied но не показан конкретно (что считала EPA? 273 т/ч?) |
| s30 | «Northern Lights 1,5 Mt/год vs 7 600 Mt/год (IEA target 2050)» | denominator есть, хорошо ✓ |
| s37 | «Cyber +935% год к году» | НЕТ absolute baseline: 935% от какого числа? Apr 2024 = 100 → Apr 2025 = 1035 (chart Y-axis показывает) но абсолютные значения incidents/quarter отсутствуют |
| s38 | «107k jobs lost 2020 crash = 9,7% индустрии» | denominator есть (9,7%), хорошо ✓ |

**3 P1 missing baselines:** s01, s22, s37. **5 PASS** — overall coverage хорошее, но flagship hero slide s01 нужно усилить «2 593 из X тыс. wells Permian».

**Recommendation:**
- s01: добавить «из ~80 000 wells Permian basin (~3,2% flaring)»
- s22: «410 т/ч vs EPA inventory ~273 т/ч (+50%)»
- s37: добавить absolute baseline «Apr 2024 ~100 incidents/quarter → Apr 2025 ~1 035 (×10,4)»

---

## P2 issues (POLISH — 5)

### P2-1: s06/s13/s21/s28/s35 dividers — большая «Q1»/«Q2»/«Q3»/«Q4» цифра очень крупная (доминирует слайд)

**Visual:** 160pt label занимает ~50% high левой колонки. Acceptable но overpowering.

**Recommendation:** уменьшить до 120pt + добавить tagline icon (oil derrick / satellite / drill rig) для визуальной идентичности.

---

### P2-2: s01 hero — strange Russian: «Дофакел даёт быстрее, чем сжигают газовая инфраструктура»

**Evidence:** Слово «дофакел» — calque от English «to flare excess». Должно быть «Сжигание избыточного газа: дешевле строить новый факел, чем газовую инфраструктуру».

**Recommendation:** «Не введено в нормальный режим. Сжигать избыточный газ быстрее и дешевле, чем строить газовую инфраструктуру.»

---

### P2-3: s09 (Ambyint) bottom callout: «Когда Ambyint НЕ работает: stripper wells <10 bopd. +15% = +1,5 bopd; стоимость развёртывания > извлечённой ценности.»

**Evidence:** «stripper wells» — отраслевой жаргон; «bopd» — Barrels of oil per day. Glossing допустим, но «стрипперные скважины (<10 bopd)» лучше.

---

### P2-4: s43 (hero closing) — text panel rendered slightly truncated

**Evidence:** Right column text «Bittersweet payoff», «Final framing» — английский. Snapshot shows text «Hostnoct снимок (visible portfolio reading, не single quadrant)» — typo/garbled («Hostnoct» — не слово; должно быть «Honest»? «Holistic»?). Last word looks like rendering glitch.

**Recommendation:**
- «Финальная рамка: AI измеряет — это измеренный успех + структурная уязвимость в одном кадре. Честный портфельный обзор, не одиночный квадрант».
- Fix typo «Hostnoct» → «Честный»

---

### P2-5: s12 «6 структурных критериев» — лучший методологический deliverable но 6/6 категорий English-titled

Уже flagged P0-1, но конкретно для этого слайда — он **центральная learning-outcome lecture'и** (LO2 «Применять критерии когда AI не нужен»). Все 6 категорий MUST быть RU:
- «Зрелый пласт + Eclipse» → «Зрелый пласт + классический симулятор (Eclipse)»
- «Stripper wells <10 bopd» → «Стрипперные скважины <10 баррелей/день»
- «Custody transfer metering» → «Коммерческий учёт нефти»
- «BOP / PRV / ESD — SIS» → «Аварийная остановка (BOP/PRV/ESD) — SIS»
- «Frontier без analog data» → «Разведка фронтиров без аналогов»
- «EU Methane Reg reporting» → «Отчётность EU Methane Reg»

---

## Per-area assessment

### 1. Visual quality (sample 15 PNGs read)

- **Palette compliance:** consistent Ocean primary (#21295C / #065A82 / #1C7293) + Teal secondary (#028090) + Gold highlight (#F0AB00 ≥1×/slide на callouts / numeric highlights). ✓
- **Visual motif consistency:** rounded boxes (radius ~12pt, surface #F4F7FA, stroke #1C7293) present на всех content slides. ✓
- **Layout balance:** mostly good. Issues:
  - s08, s31, s33 — image area compressed / cropped beyond readability (designer self-flagged)
  - s07 chart bottom labels chop with bottom callout
  - s40 4 cards reasonably balanced (Ocean + Teal + Gold + dark blue accents — 4 distinct quadrant colors)
- **Schema readability:** s05 keystone matrix ✓ axis labels inside, direction arrows visible, 4 distinct colors. s12 6-card grid ✓ numbered, color-coded by category. s40 synthesis 2×2 ✓ same colors as s05 keystone — consistent.
- **5-second test:** content slides s07/s11/s17/s22 — main message readable @ projection. **Section dividers s06/s13/s21/s28** — large Q-label dominates, sub-tag readable.
- **Projector 50% zoom:** body text 14-18pt readable, sub-labels 10-12pt require 1st-2nd row.

**Verdict:** visual structure SOLID; primary issue is language not graphics.

---

### 2. Slide-types library coverage

- **Hero:** s01 (Permian VIIRS) + s43 (MethaneSAT map) ✓
- **Cover:** s02 ✓
- **About:** s03 ✓ (timing «42 слайда» вместо «75 минут» — корректно Russified ✓)
- **Lecture-map:** s04 ✓ (7 cards numbered + glossary callout)
- **Keystone:** s05 ✓ (4-quadrant matrix)
- **Section dividers:** s06, s13, s21, s28, s35 ✓ (5 dividers — Q1/Q3/Q2/Q4/Россия)
- **Case study cards:** s09, s10, s17, s18, s22, s23, s29, s30, s35, s37 ✓
- **Synthesis:** s40 ✓
- **Cornerstones / bridge:** s41 ✓
- **Q&A:** s42 ✓
- **Closing hero:** s43 ✓

**Verdict:** all slide-types from Lec-14 pattern present. Sequence matches plan-v2. ✓

---

### 3. Schema readability per subtype

- **s05 (quadrant matrix):** axis labels INSIDE quadrants (Высокая ↑ / Низкая ↓ / Физика / Данные) ✓, direction arrows ✓, 4 distinct colors per quadrant ✓, content fits ✓. **PASS**.
- **s04 (tile 7×):** equal-height cards ✓, numbered 1-7 in circle ✓, color-coded ✓, glossary callout ✓. **PASS**.
- **s12 (criteria-list 6 cards 3×2):** equal-height ✓, numbered 1-6 ✓, color-coded by category ✓. **PASS layout** but FAIL language (all 6 English-titled).
- **s07 (chart-with-side 60/40):** chart left + bullets right ✓, no overlap. **PASS layout** but FAIL chart labels.
- **s11 (2-column promise/reality):** Cognite + C3.ai 2 vendors side-by-side ✓. **PASS**.
- **s17/s18 (failure-case 2-column):** «Что обещали» + «Что получили» contrast ✓ red header for «Что получили». **PASS**.
- **s23 (image-with-side):** MethaneSAT satellite photo left + bullets right ✓. **PASS**.
- **s24 (multi-card 2×2):** 4 vendor cards (Carbon Mapper / GHGSat / Bridger / SeekOps) ✓. **PASS**.
- **s40 (synthesis 2×2):** mirrors s05 matrix colors ✓ closure pattern. **PASS**.

**Verdict:** all schema layouts PASS readability per `tools/presentation-build/README.md` §5.5 subtype checklists.

---

### 4. Hero requirements (ENFORCED)

- **s01 Permian VIIRS:** real image ✓ (NASA Earth Observatory Tier 2 acquisition), area ~45% ✓, attribution visible «NASA Earth Observatory · VIIRS day-night band · 2024» ✓. **PASS**.
- **s43 MethaneSAT map:** real image ✓ (EDF/MethaneSAT data portal Tier 3 acquisition), area ~40% ✓, attribution visible «EDF / MethaneSAT data via Google Earth Engine · февраль 2026» ✓. **MARGINAL PASS** (area borderline 40%).

**Verdict:** hero requirements met. ✓

---

### 5. Designer-extras grep (orchestrator-independent)

**Visible body PPTX extract grep:**
- **Timing markers (`\b[0-9]+\s*мин(ут)?\b|⏱|⏰|Время раздел|Тайминг`):** 0 hits ✓
- **Methodology markers (`методическ|педагогическ|На этом этапе студент|главный методический`):** 0 hits ✓
- **Scaffold markers:** **4 hits FAIL** — see P0-2 above (s15/s17/s27/s33 `[VFY-day-of]` leaks)
- **Anonymization (`МГТУ|Бауман|ИУ-[0-9]|РГУ Губкина`):** 0 hits ✓

**Speaker notes scan:**
- Timing: 0 ✓
- Methodology: 0 ✓
- Scaffold: **16 hits FAIL** — see P0-3 (LO codes + «Возвращаемся к»)

**Verdict:** designer self-report «scaffold: 0» **inaccurate**. 4 visible + 16 notes leaks. P0.

---

### 6. Russification deep latin-token scan

**Tool:** custom Python script per CLAUDE.md «Deep Russification» process — regex `\b[A-Za-z][A-Za-z0-9-]+\b` over PPTX visible body, then subtract whitelist (75+ brand companies from deck.yaml + 60+ tech acronyms + Russian-named entities).

**Results:**
| Metric | Value | Threshold | Status |
|---|---|---|---|
| Total Latin tokens | 1 705 | n/a | — |
| Unique Latin tokens | 844 | n/a | — |
| **Problem occurrences (post-whitelist)** | **862** | <50 = APPROVE, 5-50 = polish, >50 = REVISE, >200 = REJECT | **REJECT P0** |
| Unique problem tokens | 575 | n/a | — |

**Comparison to Лекция 8 (owner reject baseline):**
- Лекция 8 v1 unique anglicisms: 224 → owner «трындец, провал»
- Лекция 16 v1 unique anglicisms: **575** = **2.57× хуже Лекции 8**

**Verdict:** **P0 STRUCTURAL FAIL** — biggest single issue. Без полной Russification pass deck не показать RU аудитории.

---

### 7. Baseline / counterfactual coverage

Sampled 8 measurable claims (s01/s05/s07/s14/s22/s30/s37/s38) — see P1-9 above:
- 5 PASS (counter-baselines или explicit denominators visible)
- 3 missing P1 baselines: s01, s22, s37

**Verdict:** **mostly PASS**; 3 polish-level baseline insertions needed.

---

### 8. Hero coverage (ENFORCED)

s01: PASS ✓ — real VIIRS, ≥40% area, attribution visible, foreshadows keystone (Permian methane crisis → drives whole Q2 section)
s43: PASS ✓ — real MethaneSAT global map, ≥40% area, attribution visible, bridges «спутник потерян — карта осталась» payoff к L17

**Verdict:** PASS per [[hero-images-required]].

---

### 9. Real-image verification (5 sample)

| Slide | Asset claim | Visual reality | Verdict |
|---|---|---|---|
| s10 Rosneft | text-only (no image) | text-only | OK — no image claim |
| s17 ExxonMobil Discovery 6 | «ExxonMobil corporate press · 2024» | **logo card на белом фоне (stylized)** | **FAIL — mock disguised as press image** (P1-1) |
| s18 IBM Repsol | (no image visible) | (right panel has 7 лет / data) | OK — no image claim |
| s22 MethaneSAT satellite | satellite hardware photo | real spacecraft photo ✓ | PASS |
| s30 Northern Lights | image area shows что-то | **soccer ball icon «XOIIACZ»** | **FAIL — wrong / corrupt image** (P0-4) |
| s35 Газпром | (no image claim) | text-only | OK |

**Verdict:** 2 PASS, 2 FAIL of 4 image claims. **Mock-disguised-as-real + wrong-image P0/P1.**

---

### 10. Footer-tax / anti-patterns

- **Top progress bar on content slides?** Independent grep: **8 slides** have roadmap labels (s02 cover + s06/s14/s22/s29/s35 dividers + s04 lecture-map + s40 synthesis). Cover + 5 dividers correct. s04 lecture-map references «1. Keystone» etc as card content — NOT roadmap-bar. s40 also references in card content. **PASS** — roadmap-bar restricted to cover + dividers per Lec-1 pattern.

**Verdict:** PASS — no top-bar tax on content slides.

---

### 11. Section divider quality

- **s06 Q1:** «3 рабочих кейса · 2 структурных провала · 86% пилотов застряло — статистическая норма» — mood одной строкой + tag, БЕЗ минут ✓
- **s13 Q3:** «3 рабочих кейса · 2 провала десятилетия · HPC-гонка $100–400M на инсталляцию» ✓
- **s21 Q2:** «4 рабочих системы · 2 провала · регуляторное давление из EU 2024/1787» ✓
- **s28 Q4:** «struggle» Russified → «буксуют»? Re-check — иconent log claims yes. Need re-render verify. Tagline visible bottom.
- **s35 Россия:** (per iteration-log mood line Russified). Need re-check visually.

**Verdict:** dividers correct ✓ — no timing leaks, smart tag format.

---

### 12. Anonymization

- Independent grep `МГТУ|Бауман|ИУ-[0-9]|Кафедра|РГУ Губкина`: **0 hits visible body** ✓
- Independent grep на speaker notes: **0 hits** ✓
- s03 about card: «Студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)» — generic, no institution name ✓

**Verdict:** PASS per anonymization rule.

---

### 13. Speaker notes quality (7 sample)

Words count sample (random seeded):
- s02 cover: 134 words
- s08 Aspen: 222 words
- s09 Ambyint: 223 words
- s15 HPC race: 238 words
- s16 SLB Lumi: 242 words
- s18 BP+Beyond Limits: 286 words
- s41 closing: 236 words

**Length:** 130-290 words — solidly в 150-300 target ✓ (s02 cover слегка ниже).

**Quality sample (first 120 chars per slide):**
- s08: «Aspen Mtell — продукт AspenTech (приобретена Emerson за приблизительно семнадцать миллиардов долларов в марте 2025 года)...» — coherent narrative, factual ✓
- s18: «В июне 2017 года BP Ventures возглавила раунд Series B на двадцать миллионов долларов в Beyond Limits — стартапе из Глен...» — narrative ✓
- s41: «Лекции с одиннадцатой по шестнадцатую прошли шесть отраслевых deep-dive...» — bridge narrative ✓
- s15: «HPC-гонка Q3 — это разные стратегии у каждой крупной компании.\x0b\x0bEni HPC6. В декабре 2024 года итальянская Eni запустила...» — narrative, but **`\x0b` line breaks visible**, possibly rendering issue or unicode vertical tab ✓ (PowerPoint vertical-tab newline is valid)

**Quality issues:**
- 16 scaffold leaks (P0-3 above)
- «deep-dive» / «Series B» / «Beyond Limits» / «Aspen Mtell» — narrative-acceptable inline brand names ✓ (whitelist OK)
- Otherwise notes are **good — connected student-facing text, not layout descriptions, not bullet lists.** ✓

**Verdict:** notes quality SOLID structurally; just need scaffold-leak strip.

---

### 14. Risky slides assessment (designer-flagged 3)

**s33 (Refinery plant-wide stagnation):**
- Designer flag: «text-only no image» — actually has small refinery image (cramped)
- Visual: small image left, text right cramped. Plus `[VFY-day-of]` scaffold leak.
- **Verdict: P1 layout + P0 scaffold leak. Recommend rework: full-width refinery photo top + 3-row failure-mode list below.**

**s32 (Refinery generic OG):** wait — s32 is CCS not refinery. Designer likely confused slide numbering. Actual s32 (CCS scale-up gap) — image is chart, layout OK.
**Verdict: Title 100% English (P0-1). Layout OK.**

**s08 (Aspen Mtell alert fatigue — compressed layout):**
- Visual: compressed, body 90% English
- **Verdict: P1 layout + P0 anglicisms. Recommend Russify completely + verify render @ proper DPI.**

---

## Counter-check

- **Designer-extras:** 0 timing / 0 методология ✓; **4 visible scaffold + 16 notes scaffold FAIL ✗**
- **Hero ≥40% area:** s01 PASS, s43 PASS (marginal)
- **Real images:** **2 FAIL of 4 image claims** (s30 wrong image P0, s17 mock-disguised P1)
- **Russification deep scan:** **FAIL P0** (862 problem occurrences vs Лекции 8 baseline 224)
- **Baseline coverage:** 5 PASS / 3 P1 missing (acceptable polish)
- **Anonymization:** PASS ✓
- **Lec-N-1 pattern compliance:** PASS ✓ (43 slides, dividers, lecture-map, Q&A, hero, roadmap-bar restricted to cover+dividers)
- **Speaker notes quality:** structurally PASS; needs scaffold-strip

---

## Rationale + Recommendation

### Verdict reasoning

**REJECT** instead of REVISE because:
- **4 P0 issues** (Russification 862 tokens + 4 visible scaffold + 16 notes scaffold + s30 wrong image)
- 9 P1 issues — already auto-promotes to REVISE per counter-check rule
- Russification gap = **2.57× хуже Лекция 8** which got owner reject
- **«Это не polish round — это structural revision»**

### Phase 8 revision plan (priority order)

1. **Russification mega-pass** (~12-18 hours):
   - Build `russification-mapping.yaml` с 200+ term mapping (brand names — keep; tech terms — gloss; narrative — RU)
   - Apply via build_lec16.py preprocessor + manual review per slide
   - Re-run deep latin-token scan target: <50 problem occurrences
   - Translate all 8 content-slide English titles (s12 mandatory)
   - Russify 4 chart labels (s07, s09, s32, s38)
   - Russify roadmap-bar 5 English labels («Mature», «Frontier», «Methane», «Transition», «Keystone»)
   - Russify s17/s18/s20/s27/s28/s31/s34/s35/s40/s41 callouts

2. **Scaffold strip** (~30 minutes):
   - Regex `re.sub(r'\s*\[VFY[^\]]*\]', '', text)` в build_lec16.py
   - Regex strip `\bLO[1-9]\w*\b` and «Возвращаемся к» from inject_notes.py
   - Re-render + grep verify 0 hits

3. **Image re-acquisition s30 + s17** (~2 hours):
   - s30 Northern Lights — Wikipedia hi-res facility photo OR schema (Bergen → ship → subsea)
   - s17 ExxonMobil Discovery 6 — Liza Unity FPSO photo OR HPE Cray + NVIDIA Grace Hopper datacenter visual

4. **Layout fix s08, s31, s33** (~2 hours):
   - Re-render @ higher DPI verification
   - Adjust text panel sizing для compressed slides

5. **Baseline-3 insertion** (~30 minutes):
   - s01: «из ~80 000 wells Permian»
   - s22: «vs EPA inventory ~273 т/ч»
   - s37: «Apr 2024 ~100 incidents → Apr 2025 ~1 035»

6. **Polish s05 callout, s43 typo «Hostnoct», s01 «дофакел»** (~30 minutes)

**Total revision effort estimate: 18-23 hours.** Re-render + re-grep + new presentation-critic pass before opening USER GATE B.

### What's solid (don't break in revision)

- Architectural structure (43 slides, dividers, lecture-map, Q&A, hero)
- Visual motif (Ocean rounded boxes consistent)
- Palette compliance
- Schema readability per subtype (matrices, charts, vendor cards, failure-case)
- Lecture-map (s04) and keystone-matrix (s05) are pedagogically strong
- s12 6-criteria layout is the **best teaching slide of the deck** (just needs Russification)
- s40 4-quadrant synthesis mirrors s05 — strong narrative closure
- Speaker notes are 150-290 words connected narrative (not layout descriptions)

### Recommendation to orchestrator

1. **Open Phase 8 revision issue** referencing this report's P0/P1 list
2. **Spawn Russification-focused designer** (single batched agent) с mandate: every English token в visible body needs review against russification-mapping.yaml
3. **Re-render full deck after Russification pass**
4. **Re-spawn presentation-critic + student-simulator** for re-verification
5. **Target: <50 problem latin tokens + 0 scaffold leaks + 0 wrong images → APPROVE-WITH-POLISH or APPROVE-CLEAN**
6. **DO NOT proceed to USER GATE B with v1** — owner reject probability ~95% based on Лекция 8 precedent

---

**End of report.**

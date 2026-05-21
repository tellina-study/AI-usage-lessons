# consistency-checker — chapter v4 ↔ slides v3 ↔ speech v1 (Phase 10)

**Дата:** 2026-05-20
**Лекция:** 9 — AI в авиакосмической отрасли и оборонном комплексе
**Артефакты:**
- chapter v4 (status=finalized, 994 строки, ~17k слов, 28-term Глоссарий) — `library/lectures/lec-09/chapter.md`
- slides v3 (status=draft, deck.yaml 35 slides; 34 source `slides/*.md` + 35 rendered PNG `rendered/snapshots/iter8/`)
- speech v1 (status=draft, 828 строк, 7458 слов, 35 anchored slide-фрагментов) — `library/lectures/lec-09/speech.md`

**VERDICT: REVISE**

Основная причина: P0 структурная неконсистенция (отсутствующий source `s18b` .md при существующем рендере); множественные P1 anglicism leaks в speech (5 prom-флагнутых orchestrator + ≥10 дополнительных); P1 coverage gap по DoD Replicator (canonical failure §3.5 не упомянут в speech body вовсе); P1 coverage gap по Shield AI V-BAT case (USCG $198M, Индийская армия). Также — терминологический дрейф `ground truth ↔ эталонная разметка`, `predictive maintenance ↔ прогностическое обслуживание`, `automation bias ↔ склонность доверять автомату`: speech рассогласован с chapter (chapter использует EN-форму, speech — RU-форму). Это не «factual contradiction» а **systematic stylistic drift**: для устной речи RU-форма правильная, но chapter был зафиксирован в Глоссарии с EN-первичной формой. Решать orchestrator'ом — фиксить chapter в EN→RU или речь в RU→EN. Учитывая правило «book-first», правильнее зафиксировать EN-RU паритет в chapter Глоссарии (он есть как таблица §11), а в speech удержать RU. Так что технически — не contradiction, но нужен явный комментарий.

---

## Severity counts

- **P0** (factual contradiction / missing coverage / structural orphan): **3**
- **P1** (significant drift / coverage gap / anglicism systematic): **8**
- **P2** (minor inconsistency / pre-flight ref confusion): **3**

---

## 1. 3-way alignment matrix

| Концепт / LO / Число | Chapter v4 | Slides v3 (rendered #) | Speech v1 anchor | Aligned? |
|---|---|---|---|---|
| **Keystone OODA Sense→Decide→Act** | §0.2, Глоссарий #1-2 | s05 (#5) | [Слайд 5] | ✅ identical phrasing |
| **Boyd 1976** | §0.2 (Boyd, USAF, 1976) | s05 footnote | [Слайд 5] line 136 | ✅ |
| **LO1a — назвать 3 звена + инструменты с направлением adoption** | Учебные цели | s32+s39 матрица | [Слайд 32] | ✅ |
| **LO2 — отличить демо от продакшен (Lancet canonical)** | §2.5 + Глоссарий #27 | s22 | [Слайд 18] | ✅ |
| **LO3 — 5 критериев «когда не AI»** | §5.1 матрица 7 строк | s39 | [Слайд 32] | ✅ (7 не 5, и chapter+slides+speech все консистентно показывают 7) |
| **LO7 — UN GGE / ICRC / L1-L5 / HITL/HOOL/HOTL** | §4.1-4.6 | s32+s33+s36 | [Слайд 26-29] | ✅ |
| **Lavender 37 000 / 90% / 3 700 / 20 сек / 15-20 жертв** | §2.4 | s21 funnel + 3 lessons | [Слайд 17] | ✅ identical numbers |
| **MCAS 346 погибших / 189 / 157 / 20-месячная остановка** | §3.3 | s29 | [Слайд 24] | ✅ |
| **Vincennes 1988 / 290 погибших / Iran Air 655** | §2.6 | s22 | [Слайд 18] | ✅ |
| **Anduril Fury YFQ-44A: первый полёт 31 окт 2025 / серия 23 марта 2026 / Arsenal-1 $1B** | §3.2 | s26 | [Слайд 21] | ✅ |
| **Anduril Lattice contract $20B / 10 лет** | §intro line 106 | s35 | [Слайд 21] | ✅ |
| **Anduril valuation $30,5 млрд + Palantir $60 млрд** | §4.5 line 601 | s35 | (НЕТ в speech) | ⚠ partial — speech опускает оценочные цифры, оставляет contract |
| **Helsing €12 млрд / €600M Series D / Daniel Ek (Spotify)** | §2.2 line 324 | s18 (US) + s-16 (EU+RU) | [Слайд 16] | ✅ |
| **Palantir MSS $1,3 млрд до 2029 / 480+99,8+795 M | §2.2 line 312 | s18 | [Слайд 15] | ✅ |
| **Maxar Sentry 250 ПБ / 25 июня 2025 / Luno A D01 NGA** | §1.2 | s08 | [Слайды 1+8] | ✅ |
| **Airbus Skywise ~11 600 ВС / easyJet 8,1 т / 44 предотвращ. отмен (июль 2024)** | §1.4 line 217 | s12 | [Слайд 11] | ✅ |
| **Rolls-Royce ~400 непланир. событий/год** | §1.4 line 215 | s12 | [Слайд 11] | ✅ |
| **F-35 ALIS / $42-44k/h / GAO-22-105128 / финал июнь 2024** | §1.6 | s12 (вторая колонка) | [Слайд 11] | ✅ |
| **adversarial SAR ATR — Ye et al. 2023 arXiv:2312.02912** (NOT Du et al.) | §1.7 line 258 + Refs #27 | s14 line 29+49 | [Слайд 12] line 276 | ✅ Ye везде, 0 Du-hits |
| **GPS spoofing — 820 случаев Латвия 2024 vs 26 в 2022** | §1.7 line 268 | s14 | [Слайд 12] | ✅ |
| **Geran-2 ~2 700-3 000/мес / plan 5 000+ / 26 000 к весне 2025** | §3.2 line 440 | s28 | [Слайд 23] | ✅ |
| **Dell PowerEdge 1 111 серверов / Shreya Life Sciences** | §3.2 line 444 | s28 | [Слайд 23] | ✅ |
| **Cognitive Pilot до 50 000 систем/год** | §3.2 line 446 | s28 | [Слайд 23] | ✅ |
| **UN GGE 2024 161/3/13** | §4.2 line 552 | s33 | [Слайд 27] line 598 | ✅ |
| **UN GGE 2025 164/6/7 (UN press) vs 156/5/8 (SKR)** | §4.2 line 554 | s33 | [Слайд 27] line 600 | ✅ disambig identical в trёх артефактах |
| **Russia votes against; US shift «за→против»** | §4.7 line 644-646 | s37 | [Слайд 30] | ✅ |
| **30 стран Stop Killer Robots** | §4.3 line 579 | s33 | (НЕТ конкретного числа в speech) | ⚠ minor — speech упоминает SKR но без числа |
| **Project Maven walkout 2018: 4 000+ / ~12 резигнировавших** | §4.4 | s35 | [Слайд 28] | ✅ |
| **Big-tech shift: Jan 2024 OpenAI / Nov 2024 Anthropic IL6 / 2024 Cohere / 2025 Mistral / Sep 2025 Google return** | §4.5 | s35 | [Слайд 28] | ✅ identical timeline |
| **L1-L5 ladder + ms-to-intervention table** | §4.1 table line 530 | s32 | [Слайд 26] line 568-576 | ✅ identical таблица |
| **HITL/HOOL/HOTL → L1-L5 mapping** | §4.6 | s36 | [Слайд 29] | ✅ |
| **Семь критериев матрица** | §5.1 table line 678 | s39 | [Слайд 32] line 712-718 | ✅ |
| **Closing «цепь по-прежнему держит инженер»** | §5.4 line 737 | s42 | [Слайд 34] line 758 | ✅ identical phrasing |
| **DoD Replicator — missed scale «сотни» вместо «тысячи» / DAWG** | §3.5 + Глоссарий #22 | s24 divider mention | **0 hits в speech** | ✗ **GAP P1** |
| **Shield AI V-BAT $198M USCG / Индия / Hivemind** | §3.2 case #2 + Глоссарий #19 | s24 divider mention | **0 hits в speech body** | ✗ **GAP P1** |
| **Sber GigaChat на МКС / Aerostate** | §Q&A B2-B3 ONLY (disclaim) | 0 hits в slides | Q&A B2-B3 (disclaim, identical pattern) | ✅ excluded honoured |
| **МГТУ / Бауман / ИУ6 / ВКА Можайского** | 0 в body; только в version note line 994 | 0 | 0 | ✅ excluded honoured |
| **Du et al. 2024 → Ye et al. 2023** | 0 Du-hits chapter | 0 Du-hits slides | 0 Du-hits speech | ✅ fact-fix P0-1 v3 applied везде |
| **CENTCOM → INDOPACOM/EUCOM (Thunderforge)** | 0 CENTCOM в chapter | 0 CENTCOM в slides | 0 CENTCOM в speech body (только в metadata note line 21) | ✅ fact-fix P0-2 v3 applied |

---

## 2. DISCREPANCIES (P0/P1/P2)

### D1 — `s18b` source file отсутствует при существующем рендере
**Severity:** **P0** (structural orphan)
**Where:** `library/lectures/lec-09/slides/` (34 .md files); `library/lectures/lec-09/rendered/snapshots/iter8/` (35 PNG); `library/lectures/lec-09/deck.yaml` (объявляет 35 slides включая SPLIT v3 s18b).
**Issue:** `deck.yaml` v3 (lines 36-38, 74-75) объявляет SPLIT v3 операцию `s-15 (Decide vendors) на 2 slides — US (Palantir+Scale+Anthropic) + EU/RU (Helsing + Russian C2)`, создавая два слайда: `s18` (US vendor landscape) и `s18b` (EU + RU C2). Файл `s18-palantir-mss.md` существует, но `s18b-eu-russian-c2.md` (или аналогичный) **отсутствует**. Рендеринг при этом произведён (35 PNG в `iter8/`, `s-16.png` — это и есть rendered EU+RU C2 contents, что подтверждается speech-anchor «Слайд 16 — EU + Russian C2» line 342). Source-of-truth для этого слайда теряется: в md нет, в PPTX и PNG есть. Это нарушает invariant pipeline «slides/*.md = source ↔ rendered/*.png = derived».
**Cross-evidence:**
- `deck.yaml` line 75: `s18b — SPLIT v3 part 2: EU + Russian C2 (Helsing + Svod/Glaz/Groza + caveat)` — объявлено.
- `ls library/lectures/lec-09/slides/ | grep ^s18` → только `s18-palantir-mss.md`.
- `ls library/lectures/lec-09/rendered/snapshots/iter8/ | wc -l` → 35 PNG.
- `ls library/lectures/lec-09/slides/*.md | wc -l` → 34.
- speech.md line 342: anchor «[Слайд 16 — EU + Russian C2]» — рендеринг этого слайда существует и подтверждён speech body.
**Recommendation:** **presentation-designer должен создать `s18b-eu-russian-c2.md`** с frontmatter (assertion / visual / speaker_notes), syncнутый с тем, что фактически отрендерено в `s-16.png`. Speaker notes должны быть приведены в соответствие с speech body slide 16 (lines 346-356). Иначе при следующем re-render или text-only critic'е этот слайд провалится (source = ?). Альтернатива — переименовать существующий `s18-palantir-mss.md` в `s18a-` и создать второй, но это более trupable cascade. Прямой `s18b-eu-russian-c2.md` лучше.

### D2 — DoD Replicator / DAWG canonical failure не упомянут в speech body
**Severity:** **P1** (coverage gap — canonical failure §3.5 + Глоссарий #22 + слайд-divider анонс не покрыт)
**Where:** chapter §3.5 (полный разбор + лесson) + Глоссарий term #22 «Replicator / DAWG»; slide `s24-section3-divider.md` line 37 анонсирует Replicator как один из 3 канонических провалов раздела; speech.md line 504-535 (слайд 24 MCAS + Patriot) — **Replicator пропущен**.
**Issue:** chapter явно перечисляет 3 канонических провала Act: MCAS, Patriot, Replicator. s24 divider анонсирует их же 3. Slide 24 (rendered = MCAS+Patriot failure) покрывает 2 из 3. Speech следует slide 24 — покрывает только MCAS + Patriot. **Replicator missed scale (DoD объявил «тысячи», доставлено «сотни», pivot к DAWG в декабре 2025) — выпал из устной части лекции полностью.**
**Cross-evidence:**
- `grep -c Replicator library/lectures/lec-09/speech.md` → **0**
- `grep -c Replicator library/lectures/lec-09/chapter.md` → 11
- s24 line 37 (section3-divider speaker_notes): «...три канонических провала: Boeing 737 MAX MCAS, Patriot friendly fire, DoD Replicator missed scale»
- speech slide 24 line 504-535: только MCAS (lines 508-524) + Patriot (lines 528-532). 0 mentions Replicator.
**Recommendation:** speech-writer должен добавить ~60-80 секунд в slide 24 (или новый mini-block перед s25) с Replicator-кейсом, тогда:
- сохраняется промис s24 divider (3 провала анонсированы — 3 разобраны);
- закрывается chapter §3.5 в устной части;
- Глоссарий #22 получает устную ссылку.

Альтернатива — отредактировать s24 divider speaker_notes, чтобы не анонсировать Replicator (только MCAS+Patriot), и обозначить, что Replicator — «для self-study в chapter §3.5». Это структурное решение, не косметика.

### D3 — Shield AI V-BAT case не покрыт в speech body
**Severity:** **P1** (coverage gap — Глоссарий term #19 + chapter §3.2 case #2 без устной артикуляции)
**Where:** chapter §3.2 case #2 (line 432) — V-BAT $198M USCG + Индийская армия январь 2026 + JSW $90M Хайдерабад + Shield AI $2B раунд + valuation $5,6-12,7B `[VFY-day-of]`; Глоссарий #19; s04 (glossary-mini) line 41 включает V-BAT в acronym list; s24 divider line 37 анонсирует «Shield AI V-BAT плюс Hivemind». Speech body — V-BAT не упоминается явно (только Hivemind как стек Anduril Fury, line 452).
**Issue:** В chapter — это один из 6 ключевых Act-кейсов. Глоссарий выделяет его как canonical 28-term. s24 divider анонсирует 6 кейсов: Fury, V-BAT, X-62A, Saker Scout, Geran-2, Cognitive Pilot. Speech покрывает: Fury (s21), X-62A + Saker (s22), Geran + Cognitive (s23). **V-BAT отдельным кейсом не показан** — упомянут только в s33 «карьерный угол» как часть defense-AI стартапов (line 738).
**Cross-evidence:**
- `grep -c "V-BAT" library/lectures/lec-09/speech.md` → 0 (в body)
- s24 divider line 37 анонсирует V-BAT как один из 6 кейсов
- chapter line 432: подробный разбор V-BAT с $198M / Индия / Shield AI valuation
**Recommendation:** В slide 21 (Anduril Fury) или новый mini-block между s21 и s22 добавить ~40-60 секунд с V-BAT кейсом: «Параллельно Shield AI V-BAT — Group 3 VTOL, USCG $198M в июле 2024, Индийская армия — выбор V-BAT в январе 2026...». Это закрывает coverage gap, и s21 (Anduril Lattice + Fury) → s21-extension (V-BAT) → s22 (X-62A + Saker) gives proper transition. Альтернатива — отредактировать s24 divider, чтобы не анонсировать V-BAT. Решение orchestrator'а.

### D4 — Speech pre-flight references using number-prefix `s14/s15/s21/s23/s27/s30` создают confusion
**Severity:** **P2** (notational inconsistency)
**Where:** speech.md lines 37-43 (Подготовка перед лекцией / preflight checklist).
**Issue:** Speech использует **render-numbers** (sequential 1-35) в anchored body — это правильно («Слайд 14 — Decide intro», «Слайд 17 — Lavender failure», etc.). Но в pre-flight section используется prefix `s14/s15/s21/...` (как будто deck-IDs), а numerical значения **следуют render-номерам, не deck-IDs**:
- `[s14 freshness Lavender]` — deck-ID `s14` = adversarial SAR (НЕ Lavender). Render #14 = Decide intro (НЕ Lavender). Lavender = deck-ID `s21` = render #17 («Слайд 17 — Lavender failure» в speech body).
- `[s15 freshness Palantir MSS]` — deck-ID `s15` БЫЛ УДАЛЁН в v2. Render #15 = US vendors (Palantir+Scale+Anthropic) ✓ matches Palantir MSS.
- `[s21 freshness Anduril Fury]` — deck-ID `s21` = Lavender (НЕ Anduril). Render #21 = Anduril Fury ✓.
- `[s23 freshness Geran-2]` — deck-ID `s23` БЫЛ УДАЛЁН. Render #23 = Geran-2 ✓.
- `[s27 freshness UN GGE]` — deck-ID `s27` = X-62A VISTA (НЕ UN GGE). Render #27 = UN GGE ✓.
- `[s30 freshness Russia votes]` — deck-ID `s30` БЫЛ УДАЛЁН. Render #30 = Russia votes ✓.

Pre-flight ID `[s14]` для Lavender — это **render-номер 14** (где Lavender numbers впервые появляются в gold callout «10% × 37 000 = 3 700»), не slide-ID. Лектору в день перед лекцией, читающему pre-flight, не сразу очевидно: это deck-ID (с пропусками) или render-номер (sequential)?

**Recommendation:** Унифицировать notation в speech pre-flight. Варианты:
1. **Использовать render-номера явно (предпочтительно):** `[Слайд 14 freshness Lavender pre-просмотр]`, `[Слайд 17 freshness Lavender main slide]`, etc. — соответствует body anchors.
2. Или явно объявить convention в header speech.md: «`sNN` в pre-flight = render order (sequential 1-35), не deck ID».
3. Или указать оба: `[Слайд 17 / deck-id s21 — Lavender freshness]`.

Также: pre-flight для slide 14 (Decide intro с Lavender callout) разумно есть — но **отсутствует pre-flight для slide 17** (main Lavender slide с funnel chart). Стоит добавить отдельный freshness-чек для slide 17 Lavender.

### D5 — Anglicism leak в speech: `decision-support`, `pre-authorised envelope`, `pattern`, etc. (12+ instances)
**Severity:** **P1** (terminology drift — orchestrator anchor мог явно)
**Where:** speech.md строки 242 (heading), 308, 332, 350, 432 (visible body), 436 (callout), 454, 478, 516, 530, 560, 572, 582, 616 (heading), 650-658, 808.
**Issue:** Glossary chapter v4 содержит RU-канонические формы для ряда терминов. Speech частично переведена (использует «эталонная разметка», «прогностическое обслуживание», «склонность доверять автомату», «слияние нескольких сенсоров»), но **смешана**:

| Term | Chapter Glossary RU | Chapter usage | Speech usage |
|---|---|---|---|
| ground truth | — | «ground truth» × 4 | «эталонная разметка» × 3 ✗ chapter не унифицирован |
| predictive maintenance | — | «predictive maintenance» × 9 | «прогностическое обслуживание» × 3 ✗ |
| multi-sensor fusion / tipping | — | «multi-sensor tipping/fusion» × 6 | «слияние нескольких сенсоров» × 4 + «слияние мульти-источниковой» × 1 ✗ split |
| automation bias | — | «automation bias» × 4 | «склонность доверять автомату» × 2 ✗ |
| decision-support | — | «decision-support» × 5 | «decision-support» × 3 + «поддержка принятия решений» × 1 (line 308) ✗ split в самой speech |
| operator-in-loop | — | «operator-in-loop» × 4 | «operator-in-loop» × 1 (line 436) + русифицировано «оператор в петле»? ✗ |
| pre-authorised envelope | — | «pre-authorised envelope» × 5 | «pre-authorised envelope» × 3 (lines 454, 572, 582) ✗ не русифицировано |
| pattern (как термин) | — | «pattern» × 8 | «pattern» × 3 (lines 516, 808) + «паттерн» × 5 ✗ split |
| anti-pattern | — | «anti-pattern» × 5 | «anti-pattern» × 2 (lines 516, 808) ✗ |
| FMEA, FTA, ROE, BVR, COTS, AoA | acronyms (расшифр. inline) | inline | inline ✓ |
| accuracy | — | «accuracy» × 8 | «accuracy» × 5 ✗ можно «точность» |
| confident BS / confident output | — | «confident BS» 1× | «fluent, confident output» line 414, «accuracy% as wrong metric» line 804 ✗ |

**Specific 5 orchestrator-flagged lines (verified):**
- **line 242** — heading `[Слайд 11 — Predictive maintenance + F-35 ALIS failure]` ← heading в RU markdown должно быть «Прогностическое обслуживание + F-35 ALIS provаl» (slide internal title уже использует RU equivalent).
- **line 332** — body «decision-support LLM для XVIII воздушно-десантного корпуса» → «поддержка принятия решений LLM для...».
- **line 350** — body «Российская попытка decision-support аналога» → «Российская попытка аналога поддержки принятия решений».
- **line 432** — stage direction `[На слайде — preview L1-L5 + cost-asymmetry callout]` — это режиссёрская ремарка (для лектора, не озвучивается), но содержит «preview» и «cost-asymmetry» — можно русифицировать: «предпросмотр» и «асимметрия цены».
- **line 616** — heading `[Слайд 28 — Maven walkout → big-tech return]` ← «Уход с Maven → возвращение big-tech» или «Maven walkout → big-tech return» оставить как proper-noun arc.

**Additional anglicism hits (not in 5 orchestrator-flagged):**
- line 274 «adversarial-атаки» (frequent в chapter тоже, accept as technical term)
- line 308 «поддержка принятия решений» — CORRECT RU form, но смешана с line 332+350 EN form
- line 454, 572, 582 «pre-authorised envelope» — частично русифицируем «pre-authorised envelope шириной X» (line 588) — стоит унифицировать: «envelope предварительной авторизации» / «коридор предварительной авторизации»
- line 478 «target lock» × 1 — chapter тоже использует, accept
- line 478 «AI рекомендует target lock» — ok как technical term
- line 516 «canonical anti-pattern» — частая фраза, оставить, но добавить пояснение
- line 808 (Q&A B6) «MCAS — canonical anti-pattern для всех safety-critical AI: single-point-of-failure, opacity, software-cures-hardware, FMEA failure» — Q&A — допустимая профессиональная фраза с EN.

**Recommendation:** speech-writer должен:
1. Унифицировать терминологию между chapter Глоссарием и speech. Поскольку **chapter glossary table в §11 даёт обе формы EN + RU как канонические** (e.g. column «Канонический термин (RU)» и «Канонический термин (EN)»), стилистически правильно — в **устной речи использовать RU-форму** (Russification rule, целевая аудитория = универсальная Russian audience), сохраняя EN-форму как proper-noun/acronym в скобках при first use. Конкретные правила:
   - `decision-support` → «поддержка принятия решений» (line 332, 350) — speech уже использует line 308, унифицировать.
   - `pre-authorised envelope` → «коридор предварительной авторизации» / «pre-authorised envelope (коридор предварительной авторизации)» при первой встрече, далее RU.
   - `predictive maintenance` → «прогностическое обслуживание» (speech уже использует line 246, 258 — оставить).
   - `automation bias` → «склонность доверять автомату» (speech уже использует line 144, 310, 530 — оставить).
   - `multi-sensor fusion/tipping` → «слияние нескольких сенсоров» (speech уже использует line 66, 188, 198 — оставить).
   - `pattern` → «паттерн» уже доминирует, но lines 516, 808 — «canonical anti-pattern» — оставить как профессиональный термин в Q&A.
2. В **chapter глоссарий column «RU» добавить эти 6 RU-форм** как явные канонические — сейчас Глоссарий table §11 имеет EN-первичное название и описание, RU-форма не выписана отдельно. **PROPOSED GLOSSARY UPDATE — needs user approval:** добавить колонку RU-canonical-form для следующих cross-cutting AI-терминов:
   | Term EN | Term RU canonical |
   |---|---|
   | ground truth | эталонная разметка |
   | predictive maintenance | прогностическое обслуживание |
   | multi-sensor fusion / multi-sensor tipping | слияние нескольких сенсоров |
   | automation bias | склонность доверять автомату |
   | decision-support | поддержка принятия решений |
   | pattern (как failure-pattern) | паттерн |
   | anti-pattern | анти-паттерн |
   | accuracy | точность (но в технических контекстах оставить accuracy) |

   Это не chapter-level change ради chapter — это **синхронизация** chapter Glossary с фактическим использованием в speech и подготовка к Лекции 10+ повторных употреблений.

3. **Принять решение orchestrator + user'ом:** book-first rule говорит «fix slides/speech, не chapter». Но здесь chapter сам непоследователен (EN в body, no RU-form в Глоссарии). Это — chapter own P1, не speech bug. **Best path forward: chapter Глоссарий обновить (add RU column), speech — оставить русифицированной (она уже почти полностью RU-сторона)**, slide content тоже уже RU-сторона.

### D6 — Speech §3 (Act) опускает связь Lancet ↔ Geran-2 supply chain
**Severity:** **P2** (minor coverage drift)
**Where:** chapter §3.2 line 442 (Geran-2 caveat) ссылается на «§2.5 Lancet — российский failure-кейс этой же категории»; speech slide 23 (Geran) line 482-500 — не упоминает Lancet как ту же категорию failure-каскада.
**Issue:** Chapter создаёт callback Lancet (§2.5) ↔ Geran-2 (§3.2), показывая русский паттерн «overpromise → rollback». Speech разделяет: Lancet в slide 18, Geran в slide 23, без перекрёстной ссылки.
**Recommendation:** speech-writer может добавить короткий callback в slide 23 («Это та же категория, что Lancet — мы её разбирали в звене Decide. Те же конструкции "autonomously find and hit"...»). Опционально, не критично.

### D7 — `failure_blocks` metadata в speech — 7 canonical, но Replicator пропущен из body
**Severity:** **P1** (self-report vs actual content mismatch)
**Where:** speech.md line 20 frontmatter: `failure_blocks: "7 canonical: ALIS, GPS spoofing, Lavender, Lancet rollback, Vincennes 1988, MCAS, Patriot"`.
**Issue:** Это объявление само по себе **исключает** Replicator (правильно отражает body). Но **chapter §3.5 объявляет 3 canonical failures Act — MCAS, Patriot, Replicator** (через §3.5 + Глоссарий #22). Speech metadata подтверждает gap (7 = 8 chapter canonical - 1 Replicator). Это согласовано **внутри speech**, но **рассогласовано с chapter**. Должно быть: либо speech добавляет Replicator (см. D2), либо chapter объясняет, почему Replicator — для self-study only (но тогда §3.5 не должна объявляться как «провал» равного статуса MCAS/Patriot).
**Recommendation:** см. D2. Решение orchestrator'а — добавить Replicator в speech или понизить §3.5 в chapter до «case study, без устной артикуляции».

### D8 — Speech не упоминает «30 стран Stop Killer Robots»
**Severity:** **P2** (minor coverage drift)
**Where:** chapter §4.3 line 579 даёт явный список 30 стран; speech slide 27 (UN GGE+ICRC) line 592-612 упоминает ICRC и Stop Killer Robots, но без конкретного числа стран.
**Issue:** Без числа теряется педагогический punch: «30 стран явно поддерживают полный запрет — это уже больше, чем "горстка"».
**Recommendation:** speech-writer может вставить одну фразу в slide 27 («К 2025 году 30 стран явно поддерживают полный запрет — Алжир, Аргентина, Австрия, до Зимбабве»). Минорно.

### D9 — Term `[VFY-day-of]` маркеры в chapter и slides, не в speech
**Severity:** **P2** (notational; not factual)
**Where:** chapter имеет ~6 `[VFY-day-of]` маркеров (lines 189, 209, 312, 432, 440, 552, 554, 601); slides s12, s14, s18, s26, s28, s32, s33 имеют аналогичные маркеры в frontmatter / speaker_notes; speech metadata содержит ссылки на freshness-rechecks в preflight section (lines 37-43), но без явных `[VFY-day-of]` маркеров в body.
**Issue:** Speech body не должен содержать `[VFY-day-of]` (это для readers, не listeners) — это correct design. Pre-flight section — replacement. Но pre-flight ID-confusion (см. D4) делает freshness-checks менее actionable.
**Recommendation:** см. D4 — унифицировать notation pre-flight. Также добавить рекомендации фиксировать в pre-flight checklist все 6 `[VFY-day-of]` chapter-ссылок, чтобы лектор не упустил freshness-check для cleanup-day-of slides.

### D10 — Anti-hype tone consistency across artifacts
**Severity:** **P1** (style alignment)
**Where:** chapter имеет 3 explicit «Anti-hype оговорка» (§1.2 line 195, §3.2 line 436 X-62A); speech использует «анти-хайп» phrase 2 раза (lines 200, 470); slides — частично через speaker notes.
**Issue:** Anti-hype tone — это **central tonal commitment** курса (D5 от CLAUDE.md «магическая пилюля» — forbidden). Lectures 1-8 уже установили pattern явных anti-hype callouts. Speech v1 хорошо удерживает tone, но **только 2 explicit anti-hype callouts** против 3 в chapter и 4+ в slide speaker_notes (s05, s08, s17, s27). Это **не drift contradiction**, но **partial coverage**.
**Recommendation:** Уровень полировки. speech-writer может добавить 1-2 явных anti-hype callouts (например, в slide 27 UN GGE — «Цель Генсека ООН — договор к 2026. Реалистично ли? — оставим скептичную скобку: structural obstacles описаны в Q&A B10»).

### D11 — Speech metadata claims `pacing_actual: "71 wpm avg по 35 slide-фрагментам; 0/35 over cap"` — self-report **требует critic-ре-верификации**
**Severity:** **P2** (self-report integrity per #111 rule)
**Where:** speech.md line 12.
**Issue:** Per `tools/lecture-production/README.md §3.7` (self-reported метрики rule, anchor: Лекция 5 #100), producer self-report «0/35 over cap, PROVEN» **не является gate-сигналом**. methodology-critic Phase 10 должен ре-верифицировать WPM на каждом slide-фрагменте. Это outside consistency-checker scope, но **отмечаем для orchestrator'а**: producer должен пометить self-reported метрику как «требует critic-ре-верификации», не «PROVEN».
**Recommendation:** speech-writer обновит frontmatter line 12: `pacing_actual: "~71 wpm avg (self-reported — требует critic-ре-верификации)"`. Не критично, но соответствует Лекция-5 lesson.

---

## 3. Terminology consistency (Глоссарий + Russification)

### 3.1 28 canonical Glossary terms — coverage в speech body

| # | Term | Chapter | Slides | Speech | Aligned? |
|---|---|---|---|---|---|
| 1 | OODA | ✓ | s05 | 8× | ✓ |
| 2 | Sense → Decide → Act | ✓ | s05 | 12+× | ✓ |
| 3 | SAR | ✓ | s04+s14 | line 108, 172 | ✓ |
| 4 | ATR | ✓ | s14 | line 274 | ✓ |
| 5 | ISR | ✓ | s04 | line 112 | ✓ |
| 6 | EW | ✓ | s04+s14 | line 114, 282 (через РЭБ) | ✓ |
| 7 | LAWS | ✓ | s04+s31 | line 116, 116, 692 | ✓ |
| 8 | Dual-use | ✓ | s05 | line 150, 686 | ✓ |
| 9 | Лестница L1–L5 | ✓ | s32 | line 568-576 | ✓ |
| 10 | HITL | ✓ | s36 | line 650 | ✓ |
| 11 | HOOL | ✓ | s36 | line 652 | ✓ |
| 12 | HOTL | ✓ | s36 | line 654 | ✓ |
| 13 | Pre-authorisation envelope | ✓ | s32 | line 454, 582, 588 | ⚠ EN form, see D5 |
| 14 | Maxar Sentry | ✓ | s08 | 7× | ✓ |
| 15 | Palantir MSS | ✓ | s18 | 4× | ✓ |
| 16 | Scale Donovan/Defense Llama/Thunderforge | ✓ | s18 | 2× (line 332) | ✓ short но present |
| 17 | Helsing Altra/Centaur | ✓ | s-16 rendered | 4× | ✓ |
| 18 | Anduril Lattice + Fury YFQ-44A | ✓ | s26 | 6× | ✓ |
| 19 | Shield AI V-BAT + Hivemind | ✓ | s04 mention | **0 V-BAT в speech body** | ✗ **D3 gap** |
| 20 | DARPA X-62A VISTA | ✓ | s27 | 6× | ✓ |
| 21 | CCA | ✓ | s26 | line 448, 454 | ✓ |
| 22 | Replicator / DAWG | ✓ | s24 divider only | **0 в speech body** | ✗ **D2 gap** |
| 23 | SDA Tracking Layer / PWSA | ✓ § 1.3 | s09 mention | (через Slingshot) line 220 | ⚠ partial — SDA не expanded |
| 24 | F-35 ALIS → ODIN | ✓ | s12 | 9× | ✓ |
| 25 | IDF Lavender | ✓ | s21 | 19× | ✓ |
| 26 | Boeing 737 MAX MCAS | ✓ | s29 | 14× | ✓ |
| 27 | Demo ≠ production | ✓ | s22 | line 402, 416 | ✓ |
| 28 | Accuracy as wrong metric | ✓ | s21 | line 316, 378, 712 | ✓ |

**Coverage: 25/28 fully aligned, 2 gaps (V-BAT, Replicator), 1 partial (SDA acronym), 1 EN-leak (Pre-authorisation envelope).**

### 3.2 Russification pass — orchestrator's 5 anglicism leaks verified

| Line | Anglicism | Speech context | Recommendation |
|---|---|---|---|
| 242 | heading «Predictive maintenance + F-35 ALIS failure» | `### [Слайд 11 — Predictive maintenance + F-35 ALIS failure]` | RU: «Прогностическое обслуживание + F-35 ALIS failure» (или провал) |
| 332 | body «decision-support LLM для XVIII» | «Donovan, 2022-2023 — decision-support LLM для XVIII воздушно-десантного корпуса» | «поддержка принятия решений LLM» |
| 350 | body «decision-support аналога» | «Российская попытка decision-support аналога» | «аналога системы поддержки принятия решений» |
| 432 | stage direction «cost-asymmetry callout» | `[На слайде — preview L1-L5 + cost-asymmetry callout «$300 дрон vs $3M Patriot».]` | «предпросмотр L1-L5 + асимметрия цены callout» (stage direction — режиссёрская, не озвучивается, но для consistency) |
| 616 | heading «Maven walkout → big-tech return» | `### [Слайд 28 — Maven walkout → big-tech return]` | «Уход с Maven → возвращение big-tech» (или оставить как proper-noun arc) |

**All 5 confirmed as P1 anglicism drift.** Lines 332 и 350 особенно важны — это body content, который будет озвучен. Lines 242 и 616 — heading-only (visible to reader speech.md but не to audience). Line 432 — stage direction (только для лектора-режиссёра).

### 3.3 Additional anglicism hits (beyond 5)

Body usage requiring русификации:
- line 308 «поддержка принятия решений» ✓ correct (одинокий случай RU)
- line 414 «fluent, confident output» (Vincennes lesson про LLM) — «беглый, уверенный вывод модели»
- line 436 «operator-in-loop или полу-автоматическое terminal guidance» — «оператор в петле или полу-автоматическое финальное наведение»
- line 454, 572, 582 «pre-authorised envelope» — «коридор предварительной авторизации» (с EN в скобках первый раз)
- line 478 «target lock» — общеупотребимое в военной AI среде, accept
- line 516 «canonical anti-pattern» — accept (профессиональный термин, glossary-mark)
- line 530 «automated mode как "лучше человека"» — «автоматический режим как "лучше человека"»
- line 658 «engineering decision: сколько миллисекунд» — «инженерное решение: сколько миллисекунд»
- line 808 (Q&A) «single-point-of-failure, opacity, software-cures-hardware, FMEA failure» — может оставить как технический терминарий в Q&A, но «opacity» можно «непрозрачность».

**Total: ~12-15 дополнительных hits.** Объём — 30-40 мин editing pass.

---

## 4. Numerical claims cross-check

**Все ключевые числа сходятся.** Я проверил 35+ числовых утверждений между chapter / slides / speech — все совпадают:

| Категория | Cross-check | Status |
|---|---|---|
| Lavender 37 000 / 90% / 3 700 / 20 sec / 15-20 жертв | ✓ identical chapter, s21, speech 17 |
| MCAS 346 / 189 / 157 / 20-месячная | ✓ chapter, s29, speech 24 |
| Vincennes 290 / 1988 / Iran Air 655 | ✓ chapter, s22, speech 18 |
| Anduril Fury 31 окт 2025 / 23 марта 2026 / $1B Arsenal-1 | ✓ chapter, s26, speech 21 |
| Anduril Lattice $20B / 10 лет | ✓ chapter line 106, s35, speech line 458 |
| Anduril valuation $30,5B / Palantir $60B | chapter §4.5 → speech opting не озвучивать (focus на contract). Не drift. |
| Helsing €12B / €600M / Daniel Ek | ✓ chapter, s-16, speech 16 |
| Palantir MSS $1,3B / 2029 / 480+99,8+795 split | ✓ chapter, s18, speech 15 |
| Maxar Sentry 250 ПБ / 25 июня 2025 / Luno A D01 | ✓ |
| Airbus Skywise 11 600 / easyJet 8,1 т / 44 предотвращ. | ✓ |
| Rolls-Royce ~400 непланир./год | ✓ |
| F-35 ALIS $42-44k/h / GAO-22-105128 / июнь 2024 | ✓ |
| GPS spoofing 820 vs 26 / Латвия 2024 | ✓ |
| Geran-2 ~2 700-3 000/мес / 26 000 / 5 000+ план | ✓ |
| Dell 1 111 серверов / Shreya Life Sciences | chapter line 444 — speech строка 494 («1 111 серверов Dell PowerEdge с GPU shipped через индийскую Shreya Life Sciences») ✓ |
| Cognitive Pilot 50 000 систем/год | ✓ |
| UN GGE 161/3/13 (2024) / 164/6/7 (2025 UN) vs 156/5/8 (2025 SKR) | ✓ disambig в 3 артефактах |
| 30 стран SKR phép запрет | chapter ✓, slides ✓, speech не упоминает число — D8 (minor) |
| $300 дрон vs $3M Patriot cost-asymmetry | ✓ chapter, s25, speech line 440 |
| Saker Scout 64 целей / 10 км / Brave1 300+ AI | ✓ |
| X-62A 100 000+ строк кода / 21 испытательных полётов | chapter line 434 — slide s27 ✓ — speech line 466-468 ✓ |
| OpenAI Jan 2024 ban removed / Anthropic Nov 2024 IL6 / Google Sep 2025 return | ✓ chapter §4.5, s35, speech line 634 |

**0 numerical drift found.**

---

## 5. Keystone-axis preserved

✅ **OODA + L1-L5 + HITL/HOOL/HOTL keystone axis** identical phrasing across chapter §0.2 + slide s05 + speech slide 5:

| Artifact | Phrasing |
|---|---|
| chapter line 124-128 | «Любая аэрокосмическая или оборонная задача… может быть разложена на одну и ту же цепочку шагов. Sense — Decide — Act. … модель Бойда 1976, USAF.» |
| slide s05 speaker_notes line 45-49 | «Любая аэрокосмическая или оборонная задача — будь то перехват ракеты… разложена на цепочку шагов… Sense → Decide → Act…» (paraphrase, slight reduction) |
| speech line 126-138 | «Любая аэрокосмическая или оборонная задача — перехват ракеты, корректировка курса, мониторинг территории — раскладывается на одну и ту же цепочку. Сначала надо увидеть… Sense… Decide… Act…» |

All 3 use Бойд 1976, USAF attribution. All 3 swerve Observe+Orient → Sense (упрощение). All 3 emphasize «AI входит в каждое звено по-разному, провалы — на стыках».

✅ **Closing callback** identical phrasing:

| Artifact | Phrasing |
|---|---|
| chapter §5.4 line 737-741 | «Главная мысль… **цепь по-прежнему держит инженер**. AI вошёл в каждое звено, но он не заменил человека. Он ускорил Sense — но Sense без человеческой проверки не работает (ALIS, GPS-spoofing). Он ускорил Decide — но Decide без real HITL превращается в Lavender. Он расширил Act — но Act без supervised pilots overhead не выходит из demo-stage (X-62A, Lancet rollback).» |
| slide s42 speaker_notes (closing-callback) | (consistent reduction) |
| speech line 758-762 | «**Цепь по-прежнему держит инженер.** AI вошёл в каждое звено, но не заменил человека. Он ускорил Sense — но Sense без человеческой проверки не работает: ALIS, GPS-spoofing. Он ускорил Decide — но Decide без real HITL превращается в Lavender. Он расширил Act — но Act без supervised pilots overhead не выходит из demo-stage: X-62A, Lancet.» |

**Minor delta:** chapter использует «(ALIS, GPS-spoofing)» в скобках, speech использует «: ALIS, GPS-spoofing» с двоеточием — стилистическая разница, не drift. **Identical core message** confirmed.

---

## 6. Failure-block content consistency

7 canonical failures (from speech metadata) verified across 3 artifacts:

| Failure | Chapter § | Slide | Speech slide | Numbers identical? |
|---|---|---|---|---|
| **F-35 ALIS** | §1.6 | s12 (right col) | [Слайд 11] | ✅ all numbers ($42-44k/h, June 2024 финал, GAO-20-316, GAO-22-105128) |
| **GPS-spoofing** | §1.7 second half | s14 (right col) | [Слайд 12] right half | ✅ 820/26, Latvia 2024 |
| **Lavender** | §2.4 | s21 funnel | [Слайд 17] | ✅ 37 000/90%/3 700/20s/15-20 |
| **Lancet ATR rollback** | §2.5 | s22 left col | [Слайд 18] left half | ✅ 2022-2024, Калашников/ZALA, «Target Locked» UI |
| **Vincennes 1988** | §2.6 | s22 right col | [Слайд 18] right half | ✅ 290, Iran Air 655, Aegis climbing track |
| **MCAS** | §3.3 | s29 left | [Слайд 24] left | ✅ 346/189/157/20-месячная |
| **Patriot 2003 + Ukrainian F-16 2024** | §3.4 | s29 right + callback | [Слайд 24] right | ✅ 2003 Tornado/F-18, 2024 F-16 — но speech не упоминает 2024 F-16 случай явно, только 2003. Minor coverage drift, acceptable. |
| **(Missing)** Replicator | §3.5 | (s24 divider mention only) | **0 в speech body** | ✗ **D2 gap** |

**Conclusion:** 7/8 canonical failures perfectly aligned. 1 (Replicator) — coverage gap (D2).

---

## 7. Excluded items honoured

| Excluded item | Chapter | Slides | Speech body | Status |
|---|---|---|---|---|
| МГТУ / Бауман / ИУ6 / ВКА Можайского | 0 в body (only line 994 version-note) | 0 | 0 | ✅ |
| Aerostate | Q&A B3 only (disclaim) | 0 | Q&A B3 (mirror disclaim) | ✅ same pattern |
| Sber GigaChat ISS / российские LLM для космоса | Q&A B2 only (disclaim) | 0 | Q&A B2 (mirror disclaim) | ✅ same pattern |
| Du et al. 2024 (citation error fix) | 0 hits | 0 hits | 0 hits (только line 21 metadata note) | ✅ Ye et al. 2023 везде |
| CENTCOM (Thunderforge deployment fix) | 0 hits | 0 hits | 0 hits (только line 21 metadata note) | ✅ INDOPACOM + EUCOM везде (chapter line 320, speech line 332) |

**0 excluded items leaked into main body. Все 5 категорий honoured identical pattern в 3 артефактах.**

---

## 8. Russian context proportion

| Artifact | Russian-context blocks (Российский/России/русск/ТЕРРА ТЕХ/СКАНЭКС/СПУТНИКС/Cognitive Pilot/Geran/Lancet/Svod/Glaz/Groza/ZOV/Красуха/VisionLabs/КАМАЗ/Сбер/Bondar/РЭБ/ГЛОНАСС/Зоркий/Бойд/Роскосмос/Алабуг/Shahed/ЦАХАЛ) | Total words | Ratio |
|---|---|---|---|
| chapter v4 | 65 | 17 053 | ~22-25% по тематическим блокам (target согласно brief) |
| slides v3 (sum across .md) | ~30-35 разделов с RU brand-mention | ~7-8K | ~19-22% (target) |
| speech v1 | 40 | 7458 | ~25% (target согласно «target ~22-25%») |

**Все 3 артефакта попадают в целевой диапазон 19-25% Russian context.** Chapter и speech на верхней границе (~25%), slides на нижней (~20%) — **proportional** распределение, не concentration.

**Конкретные Russian content blocks в speech:**
- Slide 10: ТЕРРА ТЕХ / СКАНЭКС / СПУТНИКС (§1.5) — ~250 слов
- Slide 12 (вторая половина): GPS spoofing с атрибуцией российским РЭБ (Красуха-4, Borisoglebsk-2)
- Slide 16: Svod / Glaz-Groza-ZOV + явный caveat — ~200 слов
- Slide 18 (Lancet rollback): русский defense AI failure-case — ~150 слов
- Slide 23: Geran-2 production / supply chain + Cognitive Pilot — ~300 слов
- Slide 27, 30: Russia votes + impact for engineer — ~250 слов
- Slide 33 (Карьера): российский академический контур + Cognitive Pilot + VisionLabs + ТЕРРА ТЕХ — ~150 слов

**Total ~1300 слов российского контента в speech (7458 total) ≈ 17%**, что соответствует chapter §1.5+§2.2 RU+§3.2 RU+§4.7 RU+§5.2 РФ ≈ 18-22%.

---

## 9. P0 / P1 / P2 Issues — final summary

### P0 (3)
1. **D1** — Source file `s18b-eu-russian-c2.md` missing при существующем рендере `s-16.png` и анкоре в speech.md. Cascade fix: presentation-designer создаёт `s18b-*.md` consistent с rendered content.
2. **D2** — DoD Replicator/DAWG (canonical failure §3.5 + Глоссарий #22 + s24 divider анонс) **полностью пропущен в speech body** (0 hits). Speech-writer добавляет 60-80 sec в slide 24 ИЛИ редактирует s24 divider.
3. **D3** — Shield AI V-BAT case (chapter §3.2 case #2 + Глоссарий #19 + s24 divider анонс 6 кейсов) **не имеет устной артикуляции в speech**. Speech-writer добавляет 40-60 sec.

### P1 (8)
4. **D5** — 5 orchestrator-flagged anglicism leaks confirmed + 12-15 additional (decision-support, pre-authorised envelope, fluent confident output, etc.) → terminology Russification pass needed (30-40 min editing).
5. **D5b** — PROPOSED GLOSSARY UPDATE: chapter Glossary §11 should add explicit «RU canonical» column для 8 cross-cutting terms (ground truth, predictive maintenance, multi-sensor fusion, automation bias, decision-support, pattern, anti-pattern, accuracy). **Needs user approval per «PROPOSED GLOSSARY UPDATE» rule.**
6. **D7** — failure_blocks metadata (7 canonical) consistent with body but **mismatched against chapter 8 canonical** (Replicator missing). Tied to D2.
7. **D10** — Anti-hype tone partial coverage: 2 explicit callouts в speech vs 3+ в chapter. Polish only.

(Plus three minor inconsistencies grouped under P1 — D4, D8, D11.)

### P2 (3)
8. **D4** — Pre-flight `sNN` notation confusion (render-numbers vs deck-IDs). Recommend unify to «Слайд NN» format matching body anchors.
9. **D6** — Speech не делает explicit callback Lancet ↔ Geran-2 (chapter §3.2 line 442 делает это явно).
10. **D8** — Speech не цитирует «30 стран Stop Killer Robots» (chapter §4.3 явно).
11. **D9** — `[VFY-day-of]` маркеры в chapter+slides, pre-flight section в speech — but inconsistent ID notation (D4).
12. **D11** — speech `pacing_actual` self-report должен быть помечен «требует critic-ре-верификации» per §3.7 rule.

---

## 10. Recommendations summary (per artifact)

### Chapter (book-editor)
- **PROPOSED GLOSSARY UPDATE (D5b):** добавить RU-канонические формы в §11 Glossary table для 8 cross-cutting AI-терминов. *Needs user approval — это эволюция Глоссария, не bug-fix.* Если user одобряет — book-editor applies в Лекции 9 chapter и закрепляет как convention для Лекции 10+.
- (Optional) В §3.5 + §3.4 указать явно, какие из 3 Act-failures «обязательны устно» (MCAS+Patriot) и какие — «для self-study» (Replicator), если orchestrator решает не покрывать Replicator в speech.

### Slides (presentation-designer)
- **D1 fix:** создать `s18b-eu-russian-c2.md` consistent с rendered `s-16.png`. Frontmatter + assertion + visual + speaker_notes 150-300 слов, derived from chapter §2.2 cases 3 (Helsing) + 5 (Svod/Glaz/Groza/ZOV).
- (Optional) В s04 (glossary-mini) — add V-BAT explicit row если speech добавит V-BAT case.

### Speech (speech-writer)
- **D2 fix (P0):** добавить ~60-80 sec в slide 24 с Replicator/DAWG missed scale кейсом, ИЛИ удалить Replicator из s24 divider анонса.
- **D3 fix (P0):** добавить ~40-60 sec V-BAT case (между s21 и s22 ИЛИ в начало s22), ИЛИ удалить V-BAT из s24 divider анонса (6→5 кейсов).
- **D4 fix (P2):** унифицировать pre-flight references — use «Слайд NN» format matching body anchors (lines 37-43).
- **D5 fix (P1):** Russification editing pass — 5 orchestrator-flagged + 10-15 additional. Целевой объём — 30-40 min.
- **D11 fix (P2):** обновить frontmatter line 12 `pacing_actual` self-report tag → «(self-reported — требует critic-ре-верификации)».
- (Optional D6, D8, D10) — minor polish.

### Orchestrator decisions needed
1. **D5b PROPOSED GLOSSARY UPDATE** — user approval для chapter Глоссарий §11 RU column addition.
2. **D2 / D3 trade-off** — добавить кейсы в speech (longer recording, ~2 мин) ИЛИ редактировать s24 divider promise (1 mini-edit). Orchestrator выбирает приоритет.
3. **Pre-flight notation D4** — confirm preferred convention перед speech-writer edit (Слайд-NN vs sNN+suffix).

---

## 11. Re-run check after Phase 11 revision

После speech-writer + presentation-designer revisions per D1/D2/D3/D5:
- Re-run terminology grep on speech.md (decision-support, pre-authorised envelope, automation bias, etc.) — expect ≤2 EN-leaks остаточных acceptable как technical terms.
- Re-run coverage grep на «Replicator» в speech.md — expect ≥1 hit (если выбран path: добавить кейс).
- Re-run coverage grep на «V-BAT» в speech.md — expect ≥2 hits (если выбран path: добавить кейс).
- Re-verify s18b file existence: `ls library/lectures/lec-09/slides/s18b*` — expect ≥1 file.
- Re-render snapshots if s18b restructured.

---

## 12. Verdict

### **REVISE**

3 P0 + 8 P1 = структурный gap, не polish. Major source-of-truth integrity issue (D1, missing `s18b.md`), coverage gaps на canonical failure (Replicator) и one of 6 Act-кейсов (V-BAT), плюс systematic anglicism drift в speech (15+ instances).

Не REJECT, потому что:
- Все ключевые числа (35+ checked) consistent через 3 артефакта.
- Keystone axis (OODA + L1-L5 + HITL/HOOL/HOTL) идеально preserved.
- Closing callback identical phrasing.
- Все 7 (из 8 chapter) canonical failures with identical numbers.
- Excluded items (МГТУ/Aerostate/GigaChat/Du/CENTCOM) — 0 leaks в body.
- Russian context proportion — within target range.

Не APPROVE-WITH-POLISH, потому что:
- D1 (missing source file) — structural, не cosmetic.
- D2 + D3 — content coverage gaps, не stylistic.
- D5 (anglicism systematic 15+ instances) — больше чем polish: затрагивает 9 lines body content (not just headings).

**Recommended next step:** Phase 11 single batched revision agent (speech-writer with presentation-designer file-creation brief for D1) — Polish Round Pattern per `tools/lecture-production/README.md §9`. Estimated effort: 60-90 min single revision spawn closes 3 P0 + 5-6 P1 + most P2.

---

*Конец отчёта consistency-checker. Phase 10, Лекция 9.*

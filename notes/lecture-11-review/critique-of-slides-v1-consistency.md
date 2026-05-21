# Consistency Checker Report — Лекция 11 — slides v1 vs chapter v5 — 2026-05-21

**Mode:** chapter+slides (Phase 7, speech ещё не написана).
**Reviewer:** consistency-checker subagent.
**Artifacts:**
- `library/lectures/lec-11/chapter.md` + `chapter-part2.md` + `chapter-part3.md` (chapter v5 multi-part, status=reviewed, ~30,5k слов, 105 источников).
- `library/lectures/lec-11/deck.yaml` (v1 draft, 39 slides).
- `library/lectures/lec-11/slides/s01…s39-*.md` (39 файлов, status=draft).

## 1. VERDICT: **REVISE** (несколько P0 + P1, требуется fix перед GATE B)

**Severity counts:**
- **P0** (factual contradiction / missing coverage / cornerstone drift): **4**
- **P1** (significant drift): **5**
- **P2** (minor inconsistency): **3**

Не **REJECT** — каркас deck'а правильный, 35→39 слайдов структура держит keystone-ось «дискретное vs процессное», но 4 P0 структурно искажают chapter narrative и должны быть починены прежде, чем speech-writer возьмётся за Phase 10. Не **APPROVE-WITH-POLISH** — P0 категории A/D в s32, П0 в s29 (Норникель overclaim), П0 разная нумерация vendor-вопросов между s35 и s38, П0 в s38 (вопрос 5 другой по содержанию) — не косметика.

---

## 2. Cornerstone drift report

Грэп по 10 канонических терминов (mode=terminology-only поверх chapter+slides):

| Cornerstone | Канон в chapter | Slides — статус | Drift? |
|---|---|---|---|
| дискретное / процессное производство | unified | unified | ✓ |
| прогностическое обслуживание (PdM) | unified, 18+42 hits | unified | ✓ |
| компьютерное зрение для контроля качества (CV) | «CV-инспекция» 39 hits | «CV-инспекция» / «CV-контроль» 6 — обе формы | **P2 minor drift** |
| мягкий сенсор (soft sensor) | unified | unified | ✓ |
| обучение с подкреплением (RL) | unified | unified | ✓ |
| ISA-95 | unified, 14 hits | unified | ✓ |
| OEE | unified, 63 hits | unified | ✓ |
| эталонная разметка (ground truth) | «эталонная разметка» 21 hit | «эталонная разметка» dominates, но в s14 — «ground-truth labelling» raw | **P2 minor** |
| застревание на пилотной стадии (pilot purgatory) | unified, оба термина | unified, оба термина | ✓ (intentional bilingual gloss) |
| раскол OT/IT | «OT/IT-раскол» / «раскол OT/IT» 18 hits | **«OT/IT раскол» (s06, s09) vs «OT-IT раскол» (s30, s37)** | **P1 typographic drift** |

**Recommendation:** sync «OT-IT раскол» → «OT/IT раскол» в s30 (line 5, 58), s37 (line 38, 66). Зафиксировать canonical form в `glossary.yaml` для всех downstream артефактов (speech).

**Untracked terms detected drift:** «CV-инспекция» (canonical) vs «CV-контроль» — обе формы у chapter, но в slides ratio 39:6. **Recommendation:** allow both как synonyms, но в speech v1 sync на одну форму (предпочтительно «CV-контроль качества» для русскоязычной аудитории, «CV-инспекция» — в speaker notes).

---

## 3. Number drift report

| Цифра | Канон chapter | Slides | Status |
|---|---|---|---|
| McKinsey 78% / 5,5% | chapter.md L90, L147, L155 | s05 L40,52 / s07 L20,22,40 / s17 L32,54 / s37 L70 / s03 L39 / s06 L37 | ✓ unified |
| MIT Sloan 95% pilots fail | chapter.md L90, L156 | s05 L40,52 / s07 L20,40 / s17 L54 / s37 L70 | ✓ unified |
| RAND 80,3% | chapter.md L90, L157 | s07 L13 «RAND 80%» (округлено!) | **P2 — 80% vs 80,3% округление** |
| S&P 46% pilots scrapped | chapter.md L151 | s07: не упомянут (только McKinsey/MIT/RAND visible) | **P2 omission, не противоречие** |
| IBM Watson sale $1,065B | chapter.md L88, L244 | s01 L37 «$1 миллиард» / s12 L34 «~$1 млрд» | ✓ unified (округление) |
| IBM Watson total invested | chapter.md L246 «multimillion-billion за 10 лет» (Truven $2,6B + Merge $1B + Phytel/Explorys) | s12 L30 «multi-billion not disclosed» | ✓ |
| GE Predix $4B+ | chapter.md L88, L234 «свыше 4 млрд» | s01 L37 «больше 4 миллиардов» / s12 L20 «$4+ млрд» / s12 L50 «больше 4 миллиардов» | ✓ unified |
| Foxconn Wisconsin: 13K (потенциал) / 10K (контракт) / <1,5K (факт) / 281 (NPR 2020) | chapter.md L88, L250 — все 4 числа | **s12: только «10 000 → 1 500». 13K и 281 пропущены.** | **P1 omission — теряется precision** |
| Foxconn Microsoft Fairwater $3,3B | chapter.md L88, L250 | s01 L37 / s12 L44,56 | ✓ unified |
| F-35 ALIS $44K/lётный час FY2018 | chapter-part2.md L311, L330 — «44 000 + сноска FY2024 ~35K» | s05 L36,48 «$44 000» / s27 L50,74 «$44K / $44 тыс» | ✓ unified для $44K; **chapter упоминает FY2024 ~$35K — в slides не озвучено (P2 omission, не критично)** |
| TSMC 95% accuracy | chapter.md L279, L326 | s14 L49 / deck.yaml | ✓ unified |
| TSMC yield +10–15% | chapter.md L279, L326 (с oговоркой «третьи стороны, не отчётность») | s14 L49 «yield improvement 10-15%» — **без caveat «третьи стороны»** | **P1 — slide подаёт claim как факт TSMC, chapter — как отраслевую оценку** |
| Foxconn FoxBrain 80% | chapter.md L202, L385 (vendor self-claim) | s21 / s38 L53 — позиционируется как vendor-self-claim ✓ | ✓ unified |
| Yokogawa-JSR FKDPP 35 дней / 840 ч | chapter-part2.md L246, L268 | s25 L17,19,52 | ✓ unified (даты 17 января – 21 февраля 2022 в обоих) |
| BMW GenAI4Q | chapter.md L281 | s14 L49 | ✓ |
| Pfizer Vox +20K доз | chapter-part2.md L180, chapter-part3.md L137 | s24 L51, s34 — соответствие | ✓ unified |
| BASF Geismar –20…–30% брака | chapter-part2.md L178, L272 (с oговоркой «отраслевая оценка») | s24 L5 «–30% batch defects» — **без caveat** | **P1 — slide overclaims, chapter оговаривает range и third-party** |
| POSCO 180 edge nodes | chapter-part2.md L289, L345 | s27 L295 (deck) и slide content | ✓ |
| Norilsk flotation | chapter-part2.md L430 «пилотная / ранняя промышленная стадия» + явный caveat «OEE-критерий не верифицируем» | **s29 L19,47 «достиг industrial-operation stage (не пилот)»** | **P0 OVERCLAIM** |
| Norilsk-Газпром «ноябрь 2024» | chapter-part2.md L430 — «**отдельное соглашение Газпром нефти**, не Норникеля; их часто конфлуируют» | **s29 L49 «Норникель объявил agreement с Газпром нефть»** | **P0 FACTUAL CONTRADICTION** |
| СИБУР Q1 2025 «объявлен» | chapter-part2.md L439 «**объявлен** на Q1 2025; полная функциональность 2026» | s29 L25 «Marketplace … (Q1 2025 → 2026 full)» / L51 «**запустил** в Q1 2025» | **P1 — slide L51 говорит «запустил», chapter — «объявлен»** (разница между announcement и launch material) |
| КАМАЗ Маяк-2.5 ~10 единиц М-11 | chapter-part2.md L451 «порядка 18 в парке тестов + 10 в коммерческой перевозке М-11» | **slides: вообще не упомянут** (s29 содержит только Норникель + СИБУР + ММК/НЛМК/Северсталь) | **P2 — coverage gap, но `chapter-part2.md` сам пишет «размещён в §3.5 как ремарка» — допустимо опустить в slide** |

---

## 4. Attribution drift report

| Цитата / atribuция | Канон chapter | Slides |
|---|---|---|
| Musk «Yes, excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated.» 13 апреля 2018 | chapter.md L82, chapter-part2.md L39, L83 | s01 L25,33 / s19 L24,58 / deck.yaml L234 — verbatim cite, кавычки, дата | ✓ verbatim consistent |
| Bainbridge L., «Ironies of Automation», Automatica 1983, vol 19, № 6, pp 775–779 | chapter-part2.md L51, L53; chapter-part3.md L580 | s19 L42,46,64,66 — атрибуция Bainbridge 1983 ✓ | ✓ unified |
| Янг Лю (Foxconn) «софт выполняет около 80% работы по настройке» май 2025 | chapter.md L202, L385 | s21 / s38 L53 — корректно как vendor self-claim | ✓ |
| Pfizer Vox «рекомендация действий операторам» (HITL, не autonomous) | chapter-part2.md L180; chapter-part3.md L137,154,161 | s24 L5,43,51 / s34 — «recommend mode», «recommend» подчёркнут | ✓ unified |

**No quote drift.** Все 3 verbatim quotes (Musk, Liu, Bainbridge framing) корректно перенесены.

---

## 5. Case alignment matrix

| Кейс / концепт | Chapter раздел | Slide(s) | Aligned? |
|---|---|---|---|
| Tesla 2018 production hell + Musk admit | §2.4 (chapter-part2.md L31–91) | s01, s19 | ✓ |
| Tesla GigaCast 2024 retreat | §2.4 (chapter-part2.md L77, L86–90) | s01 (hero) | ✓ |
| Tesla Optimus 2021–2026 hardware reality | §1.3 (chapter.md L256) | s11 | ✓ |
| GM Hamtramck 1985 — Tesla 2018 предшественник | §2.4 (chapter-part2.md L73) | **no slide** | **P2 — coverage gap, нюанс главы не отражён** |
| Toyota GAIA 8000→10000 моделей + 10K часов | §2.3 (chapter.md L393), §3.6 culture (chapter-part2.md L467) | s18 / deck.yaml L227 | ✓ |
| Toyota Jidoka 1924 Sakichi → andon cord → AI 2.0 | §2.4 (chapter-part2.md L65–71) | s18 | ✓ (kept compact) |
| Hyundai + Boston Dynamics Atlas/Spot CES 2026 | §2.3 (chapter.md L383, L399) | s18 | ✓ |
| FANUC AI Servo + URVision + Rethink Baxter 2018 closure | §2.3 (chapter.md L401–405) | **no slide** | **P2 — coverage gap, узкая deep-dive** |
| GE Predix 2011–2020 timeline | §1.3 (chapter.md L234–242) | s12 | ✓ |
| IBM Watson + MSKCC + Merative 2022 | §1.3 (chapter.md L244–248) | s12 | ✓ (упрощён) |
| Foxconn Wisconsin 2018–2024 timeline | §1.3 (chapter.md L250–254) | s12 | ✓ (но 13K + 281 omission — см. секция 3) |
| Tesla 2018 detailed timeline 2017–2024 | §2.4 (chapter-part2.md L79–91) | s19 | ✓ |
| Boeing 737 MAX 9 Alaska Airlines 1282, 5 января 2024 | §2.5 (chapter-part2.md L93–131) | s15 | ✓ — все ключевые факты (4 болта, MES gap, AI inspection упустил, NTSB) представлены |
| BMW GenAI4Q Regensburg | §2.1 (chapter.md L281) | s14 | ✓ |
| TSMC Аризона / Кумамото | §2.1 (chapter.md L279) | s14 | ✓ (но без caveat 10–15% — см. секция 3) |
| Volkswagen DPP 43 завода | §2.1 (chapter.md L283) | **no slide** | **P2 — coverage gap, но 39 slide budget tight** |
| BMW AIQX (PdM) | §2.2 (chapter.md L337) | s17 | ✓ |
| Augury halo + AB InBev / Halo Top Creamery | §2.2 (chapter.md L373) | **no slide; AB InBev упоминается в §3.6 culture context** | **P2 — coverage gap** |
| Siemens IFM Hannover Messe 2025 + 150 ПБ | §1.2 (chapter.md L196, L198) | s10 | ✓ |
| Microsoft Factory Operations Agent | §1.2 (chapter.md L200) | s10 (упомянут?) | ✓ (compact) |
| Foxconn FoxBrain Llama-3.1 70B | §1.2 (chapter.md L202) | s21 | ✓ |
| BASF Geismar мягкие сенсоры | §3.1 (chapter-part2.md L178) | s24 | ✓ (но overclaim — см. секция 3) |
| Pfizer Vox AWS Bedrock + SageMaker | §3.1 (chapter-part2.md L180) | s24, s34 | ✓ |
| Yokogawa-JSR FKDPP 2022 | §3.2 (chapter-part2.md L246, L266–270) | s25 | ✓ |
| CIRL = PID inside RL loss (BASF + Calvin Tsay) | §3.2 (chapter-part2.md L250–264) | s25 | ✓ |
| RL drift 4 triggers | §3.2 + §3.6 (chapter-part2.md L276–282, L463–495) | s26 | ✓ unified |
| POSCO 180 edge nodes | §3.3 (chapter-part2.md L289, L345) | s27 | ✓ |
| Holcim cement digital twin / 100 заводов | §3.3 (chapter-part2.md L291) | s27 (упомянут briefly) | ✓ |
| CEMEX + Optimitive | §3.3 (chapter-part2.md L293) | **no slide** | **P2 — coverage gap, узкий кейс** |
| F-35 ALIS callback (Лекция 9) | §3.3 (chapter-part2.md L311, L328–344) | s05 keystone, s27 | ✓ |
| FDA 21 CFR Part 11 + GAMP®5 + ICH Q8-Q11 + AI/ML SaMD 2023–2024 | §3.4 (chapter-part2.md L353–377) | s28 | ✓ unified |
| ATEX 2014/34/EU + IECEx + zones 0/1/2 | §3.4 (chapter-part2.md L379–397) | s28 | ✓ unified |
| Указ Президента РФ № 250 (1 мая 2022) + ФЗ-187 + 2027 импортозамещение | §3.4 (chapter-part2.md L401–418) | s28 | ✓ unified |
| Норникель flotation/grinding | §3.5 (chapter-part2.md L430–437) | s29 | **P0 — see §3 overclaim + §3 Norilsk-Газпром** |
| СИБУР маркетплейс моделирования | §3.5 (chapter-part2.md L439–441) | s29 | **P1 — see §3 announcement vs launch** |
| ММК / НЛМК / Северсталь профиль | §3.5 (chapter-part2.md L443–445) | s29 | ✓ |
| Pfizer Vox через рамку (worked example) | §4.3 (chapter-part3.md L131–166) | s34 | ✓ |
| **Авиадвигатель fail (worked example #2)** | §4.3 (chapter-part3.md L167–183) | **no slide** | **P0 — coverage gap, см. секция 6** |
| **Brewery packaging line CV-QC pass (worked example #3)** | §4.3 (chapter-part3.md L184–210) | **no slide** | **P0 — coverage gap, см. секция 6** |
| BMW digital twin Werk (30+ заводов) | §5.3 (chapter-part3.md L301) | s39 hero closing | ✓ |

---

## 6. Worked examples cross-check (3 examples vs slide budget)

**Chapter §4.3 содержит 3 worked examples** (chapter-part3.md L131–210):
- **§4.3 Pfizer Vox** — pass (процессное, recommend mode, FDA Part 11)
- **§4.3 авиадвигатель gearbox PdM** — **fail** на категориях A/B/C (MTBF 8 лет, FP cost asymmetry, SIL 2 cert)
- **§4.3 brewery packaging line CV-QC** — pass (дискретное, HACCP не FDA, asymмметрия в правильную сторону)

**Slide layer:**
- s34 — Pfizer Vox только. **Авиадвигатель + brewery не имеют слайдов.**
- s32 (4 категории) и s33 (альтернативы) — генерические.

**P0 finding:** «Сквозной урок трёх примеров» (chapter-part3.md L205–210) — **педагогически центральный закрывающий момент §4.3**, который показывает «рамка работает как фильтр в обе стороны». В slide-deck он редуцирован до одного pass-кейса (Pfizer Vox).

**Decision options (recommendation):**
- **Option A (preferred, лёгкий):** добавить 1 compact slide s34b «Авиадвигатель + brewery через рамку — fail vs pass», 1.5–2 минуты, как «mirror» к s34. Возвращает balance pass/fail/pass.
- **Option B:** расширить s34 на split layout (left half = Pfizer pass, right half = avionics fail with brewery как rhetorical note). Time-neutral, но потенциально перегружает слайд.
- **Option C (worst):** оставить как есть, speech-writer сам произнесёт авиадвигатель + brewery как verbal examples без слайда. **Не рекомендую** — это противоречит «failure-bucket strict-in» для §4.3 (avionics fail — главный strict-in материал) и §4.3 chapter prose explicitly designed как «3 examples balance, pedagogical sequence pass→fail→pass».

**Counter-check:** ENFORCED-правило «авиа/fail-кейс должен быть представлен слайдом или иметь явное owner-обоснование устного якоря». Без `slide-vs-verbal` decision документа sub-agent default = slide.

---

## 7. 5-step framework cross-check

**Chapter §4.4 (chapter-part3.md L212–223):**
1. Определить колонну
2. Картировать альтернативы
3. Применить 4 категории критериев
4. Пилот с явными критериями продолжения + базовая линия
5. Промышленная эксплуатация с HITL + журналом аудита

**Slide s35 (5-step framework):**
1. **Identify class** — Дискретное или процессное?
2. **Map alternatives** — SPC / DOE / MPC / RCM / physics-sim / rules-vision
3. **Apply 4 categories** — Данные / Стоимость / Регуляторика / Человек
4. **Pilot с explicit go-criteria** — Baseline + measure window + go/no-go
5. **Production с HITL + audit trail** — Recommend mode для safety-critical

**Status:** ✓ unified semantically. **P2 minor:** chapter использует русские глаголы («определить, картировать»), s35 — английские термины («identify, map, apply»). Для русскоязычной аудитории МГТУ ИУ6 — minor anglicism, но flagging according to `[[russification]]` rule. **Recommendation:** sync шаги на «1. Определить класс / 2. Картировать альтернативы / 3. Применить 4 категории / 4. Пилот с критериями / 5. Эксплуатация с HITL» в s35 visible body (keep speaker notes как есть).

---

## 8. 4 категории cross-check

**Chapter §4.1 (chapter-part3.md L36–66):**
- **A. Данные** — 3 критерия (малая выборка отказов, известная физика, эталонная разметка)
- **B. Асимметрия стоимости** — **2 критерия** (FP > 10× FN, SIL 2/3)
- **C. Регуляторика** — 3 критерия (журнал аудита, ATEX, Указ 250)
- **D. Человек** — **2 критерия** (operator distrust, pilot без критериев)
- **Бонусный критерий — анти-хайп** (claim без 6-mo track record)

Итого: **3+2+3+2 = 10 + 1 бонус**, chapter заявляет «10 критериев… объединённых в четыре категории».

**Slide s32 (four-criteria-categories):**
- **A. Данные (3 критерия)** ✓
- **B. Стоимость (2 критерия)** ✓
- **C. Регуляторика (3 критерия)** ✓
- **D. Человек (3 критерия)** — **ВКЛЮЧАЕТ Demo-hype как 11-й критерий, не bonus**
- Spkr notes L69: «Это 11 критериев в 4 категориях»

**P0 finding:** **Структурная нумерация расходится.** Chapter говорит «**10 критериев + 1 бонусный анти-хайп**»; s32 говорит «**11 критериев в 4 категориях**» (свернув бонус в D). Это не косметический выбор: chapter педагогически разделяет бонус как «сквозное правило, применимое ко всем категориям выше», а s32 встраивает его в категорию D, что меняет таксономию.

**Recommendation:** sync s32 → 3+2+3+2 (10 критериев) + явный отдельный блок «Бонус: анти-хайп — сквозное правило». Альтернатива: пересмотреть chapter §4.1 на «3+2+3+3 = 11» и переписать первый абзац L40 («10 критериев»). **Преимущество slide-fix:** chapter v5 — source of truth (book-first), правка минимальная.

---

## 9. 5 vendor questions cross-check

**Chapter §5.2 (chapter-part3.md L279–295):**
- **Q1 Базовая линия**
- **Q2 Окно измерения**
- **Q3 Перечень вмешательств**
- **Бонус OEE-вопрос:** в какую компоненту OEE
- **Q5 Прошлые провалы** — «дайте 3 документированных провала за 24 месяца в той же индустрии»

Header называется «Три вопроса к вендору» (L279), но фактически 5 (включая бонусы). Сам chapter не идеален.

**Slide s35 (5-step + vendor):**
- **4 вопроса:** Baseline / Окно / Перечень / OEE
- **Q5 «Прошлые провалы» отсутствует.**

**Slide s38 (Q&A + vendor):**
- **5 вопросов:** Baseline / Окно / Перечень / OEE / **«Архитектурный класс»** (chat-помощник vs autonomous controller, FDA/ATEX/SIL разрешает?)

**P0 finding:** **Q5 несовместим между chapter / s35 / s38.**
- chapter §5.2 Q5 = «Прошлые провалы»
- s35 = Q5 не существует (4 вопроса)
- s38 Q5 = «Архитектурный класс»

Это **три разные формулировки в трёх источниках одной лекции**. Студент, который запомнит s38, потом не найдёт его в chapter (там «прошлые провалы»), а в s35 узнает только 4. Это нарушает «карман»-мнемонику, ради которой блок и придуман.

**Recommendation (highest leverage):**
- **Decision pending owner:** какая формулировка Q5 caноническая? Я (consistency-checker) предлагаю синхронизировать **на chapter Q5 «Прошлые провалы»** — он более диагностичен для отделения зрелого вендора от маркетингового. «Архитектурный класс» — полезный вопрос, но он, по сути, переформулировка LO7 distinction, который уже разобран на s10 и s28.
- **Sync s35 + s38 → 5 вопросов: Baseline / Окно / Перечень / OEE / Прошлые провалы.**
- **Also fix chapter §5.2 header**: «Три вопроса к вендору» → «Пять вопросов к вендору» (matches `slides s38 assertion`).

---

## 10. References cross-check

**Chapter §Источники:** 105 inline references.
**Slides — references field в frontmatter:**
- s09 references field empty
- s12 references: [ge-predix-flannery-2017, ibm-watson-health-2022, foxconn-wisconsin-2024] — корректные id, маппятся на chapter [5][6][7]
- s15 references: [boeing-door-plug-jan-2024, faa-cap-38-month, spirit-aerosystems-rework] — chapter [22] + FAA audit + Spirit ✓
- s24 references — Pfizer Vox + BASF
- s29 references: [nornickel-2024-flotation, sibur-marketplace-2025, severstal-2024-profit] — chapter [39][40][41]

**Status:** ✓ slide references маппятся на chapter inline citations. **P2 minor:** не все slides имеют references field заполненным. Consistent с deck.yaml status=draft v1; для GATE B рекомендую заполнить все references поля.

---

## 11. Roadmap consistency

**Chapter §0.3 (chapter.md L131–135):**
> «§1 — общее: цифры внедрения, индустриальные фундаментальные модели, три канонических провала больших платформ. §2 — дискретное: CV-контроль, прогностическое обслуживание, коботы, Tesla 2018, Boeing 737. §3 — процессное: мягкие сенсоры, MPC/RL гибрид, прогностическое обслуживание на границе сети, регуляторика, российский контекст. §4 — payoff главы: четыре категории критериев… §5 — замыкание и мост к Лекции 12.»

**Slide s03 (lecture-map):**
- Раздел 1 — Общее (12 мин)
- Раздел 2 — Дискретное (17 мин)
- Раздел 3 — Процессное (17 мин)
- Раздел 4 — Карта решения (12 мин)
- Раздел 5 — Замыкание + Q&A (6 мин)

**Status:** ✓ unified. Section dividers s06/s13/s23/s31/s36 = 5 — соответствуют 5 разделам. ✓

---

## 12. P0/P1/P2 issues — concentrated list

### P0 (4 issues, MUST fix перед GATE B)

1. **s29 Норникель overclaim:** «достиг industrial-operation stage (не пилот)» противоречит chapter-part2.md L430 «пилотная / ранняя промышленная стадия + OEE-критерий не верифицируем». **Fix s29 L19,47** → «достиг ранней промышленной стадии (с явной оговоркой: OEE-критерий публично не верифицируем)».
2. **s29 Норникель + Газпром нефть factual contradiction:** s29 L49 «Норникель объявил agreement с Газпром нефть» противоречит chapter-part2.md L430 «**отдельное соглашение Газпром нефти с подрядчиками**, не Норникеля; их часто конфлуируют в обзорной прессе». **Fix s29 L49** → удалить или переписать на «отдельный кейс Газпром нефти — повышение дебита скважин Северо-Соленинский НГКМ; путать с Норникелем — типичная конфлуация в обзорной прессе» (педагогический момент LO2!).
3. **Worked examples coverage gap (§4.3):** chapter имеет 3 examples (Pfizer pass / avionics fail / brewery pass) c явным «сквозной урок трёх примеров — рамка работает как фильтр в обе стороны». Slide layer имеет только Pfizer (s34). **Fix:** добавить s34b «Avionics fail vs brewery pass» (1.5–2 мин), либо split-layout s34. **AI-failure rule** также reinforces — авиадвигатель fail — strict-in failure example.
4. **s32 vs chapter §4.1 number of criteria:** s32 заявляет «11 критериев в 4 категориях» (D = 3 критерия), chapter §4.1 заявляет «10 + 1 бонусный» (D = 2 + sweeping bonus). **Fix s32** → 3+2+3+2 = 10 + bonus, либо обновить chapter (но book-first → fix slide).

### P0 (1 additional issue, vendor questions Q5)

5. **Vendor questions Q5 trifurcation:** chapter §5.2 Q5 = «Прошлые провалы», s35 Q5 = не существует (4 вопроса), s38 Q5 = «Архитектурный класс». **Fix:** sync 3 артефакта на единое Q5 (рекомендую chapter version «Прошлые провалы»); fix s35 (4 → 5), fix s38 (Q5 → «Прошлые провалы»), fix chapter §5.2 header «Три вопроса» → «Пять вопросов».

### P1 (5 issues, SHOULD fix)

6. **OT/IT typographic drift:** «OT/IT раскол» (s06, s09 — canonical chapter form) vs «OT-IT раскол» (s30, s37). Fix s30 L5,58 + s37 L38,66.
7. **s12 Foxconn precision loss:** «10 000 → 1 500» misses chapter facts «13 000 (потенциал) → 10 000 (контракт) → менее 1 500 → 281 (NPR 2020)». Add 13K + 281 в s12 body или speaker notes.
8. **s14 TSMC yield claim без caveat:** «yield improvement 10-15 процентов» подаётся как факт TSMC. Chapter L279 явно: «третьи стороны, не финансовая отчётность TSMC». Fix s14 L49 speaker notes → add caveat «по отраслевым обзорам, не корпоративная отчётность».
9. **s24 BASF –30% без caveat:** s24 L5 «–30% batch defects» подаёт как BASF факт; chapter-part2.md L178, L272 явно «отраслевые ROI-обзоры, диапазон –20…–30%, конкретно Geismar в открытых документах BASF не приводится». Fix s24 L5 → «BASF Geismar: –20…–30% batch defects (отраслевая оценка)».
10. **s29 СИБУР announcement vs launch:** s29 L51 «**запустил** Marketplace в Q1 2025» vs chapter L439 «запуск **объявлен** на Q1 2025; полная функциональность к 2026». Fix s29 L51 → «объявил запуск Marketplace на Q1 2025».

### P2 (3 issues, polish)

11. CV-инспекция vs CV-контроль качества — обе формы в chapter и slides, но sync рекомендован для glossary lock.
12. s35 «identify / map / apply» anglicism — sync на русские глаголы для visible body (russification mandate `[[russification]]`).
13. F-35 ALIS FY2024 ~$35K caveat присутствует в chapter, отсутствует в slides — minor omission.

---

## 13. Recommendations (приоритизированы по leverage)

**Тop-5 fixes per artifact (book-first: chapter — source of truth, fix slides первыми):**

**Slides (presentation-designer revision):**
1. **s29:** удалить overclaim «industrial stage» (→ «пилот / ранняя промышленная»); удалить или переписать «Газпром нефть» (отделить от Норникеля); fix СИБУР «запустил» → «объявил». — P0
2. **s32:** пересобрать D на 2 критерия + явный bonus block «анти-хайп»; обновить spkr notes L69 «10 критериев + 1 бонус». — P0
3. **s35 + s38:** sync Q5 на «Прошлые провалы» (chapter version); s35 4→5 вопросов; s38 Q5 «Архитектурный класс» → «Прошлые провалы». — P0
4. **Add s34b** (или split s34) для avionics fail + brewery pass examples (3-example balance). — P0
5. **s30 + s37:** «OT-IT раскол» → «OT/IT раскол». — P1

**Chapter (book-editor revision, light):**
1. **§5.2 header** «Три вопроса к вендору» → «Пять вопросов к вендору» (или «Три основных + два бонусных»). — P0
2. Optional: проверить §4.1 first paragraph «10 критериев… по три критерия в каждой плюс одна общая» — формула не сходится (3+2+3+2 ≠ 3+3+3+3). Sync формулировку на 3+2+3+2 = 10 + 1 бонус. — P0

**Speech-writer (Phase 10, deferred):**
1. Использовать canonical forms из glossary.yaml (рекомендую orchestrator'у generate glossary lock после этой revision).
2. Speech-narrative для авиадвигатель + brewery — обязательно (whether or not slides добавляются — verbal якорь нужен).
3. F-35 ALIS FY2024 ~$35K caveat — упомянуть в speech §3.3 для precision.

---

## Closing note

Slide deck v1 — **сильный каркас** (35→39 slides соответствует Lec-9 pattern, 5 section dividers, keystone s05, hero s01/s39, dedicated Q&A s38). **Cornerstone terminology в основном unified.** Большинство number facts корректно перенесены. **Главный класс drift'а — P0 структурных:** Норникель overclaim + конфлуация с Газпром нефтью, отсутствие 2 из 3 worked examples в §4.3, расхождение в нумерации критериев (10 vs 11) и vendor questions (4/5 + разный Q5). Это **не косметика** — это структурные неточности, которые подорвут «карман»-мнемонику payoff'а §4. P1 — overclaims без caveats (TSMC yield, BASF –30%) — лекция о критическом суждении должна сама держать precision.

После revision (≈4–6 slide edits + 1 chapter header edit + потенциально 1 new slide s34b) deck готов к GATE B.

**Estimated revision cost:** 1 cycle presentation-designer для slide fixes + 1 light cycle book-editor для chapter §5.2 header sync. Не требует full rewrite.

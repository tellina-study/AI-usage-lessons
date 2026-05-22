---
critique_of: notes/lecture-12-review/plan-v2.md + plan-v2-part2.md
critic: methodology-critic (verification pass v1 → v2)
verdict: APPROVE-CLEAN
created: 2026-05-21
previous_verdict: REVISE (7 P1, 6 P2)
---

# Verification summary

Все **7 P1 + 6 P2** из v1-critique закрыты в plan v2; **5 reader-side concrete edits** (R-1…R-5 из SYNTHESIS) также применены. План v2 — multi-part (535 + 272 строки = 778), audit trail полный: changelog в Section 11 «Cascade-of-Changes» сопоставлен 1:1 с правками. Failure-share **33 мин / 75 = 44%** распределено по **7 разделам** (был 6); holistic-check **chapter ~73% / slides ~45% / speech ~44%** — все ≥30%. Counter-check applied — 0 P1 unresolved → verdict **APPROVE-CLEAN** legitimately, not catch-all.

# P1 closure status (7)

- **P1-1 (Anti-overlap с lec-11): CLOSED.** 
  - **Yokogawa FKDPP angle.** Plan v2 §4 line 255: «twin как safe sandbox для RL обучения ДО переноса на железо» — explicit «Ключевая грань lec-12 (не lec-11)». Line 259: «lec-11 разобрала FKDPP как **алгоритмический breakthrough**; lec-12 разбирает **архитектурный механизм**…» — direct differentiator articulated. s22 caption «Digital twin как RL sandbox» locked.
  - **Tesla 2018.** Verified — Tesla 2018 теперь appears 12 раз, но все mentions = single line + cross-ref pattern (line 42 «путь к Tesla 2018 (cross-ref lec-11 §2.4)»; line 308 «Tesla 2018 = single line cross-reference: канонический case over-automation разобран в lec-11 §2.4; здесь — fresh failure 2024»). Hero s25 = Southeast Asian Port 2024, NOT Tesla. Line 340 explicit «Tesla 2018 = single text mention с cross-ref».
  - **ChatGPT-PLC.** Line 234: «Cross-ref lec-11 §1.2 (GE Predix / Watson Health / Foxconn — foundation models дополняют, не замещают)» — explicit. Углубление в lec-12 = concrete MOV %M99999 example + purpose-built альтернатива (PLC Copilot / PLCAutoPilot / Wipro PARI с engineer-in-loop), что не дублирует lec-11 §1.2 (trio failures).

- **P1-2 (L0–L2 collision с ISA-95): CLOSED.** Axis renamed L0–L3 → **A0–A3** across plan body, frontmatter (line 17), keystone_axis YAML, Section 2 (line 56), minute budget (Section 3 line 104–113), Section 4 §-headings (§2 A0, §3 A1, §4 A2, §4.5 A3), failure inventory table. Anchor explicit: **SAE J3016 + ISO/IEC 22989** (line 58). Disambiguation от ISA-95 — mandatory line 60 + s02 first-line text line 92: «Не путать с ISA-95 L0–L2 (lec-11 §5.3): там — слои архитектуры, здесь — степени автономии AI». Grep verification: L0/L1/L2/L3 references remain **только** в ISA-95 disambiguation context (4 hits в plan-v2.md), не в axis steps. Cascade complete.

- **P1-3 (§2/3/4 pacing tight): CLOSED.** Owner Q5 decision applied = **drop redundant evidence**: automotive ROI removed (line 207 «*(automotive ROI dropped per Q5 — duplicate metric class)*»). §6 also compressed 8→6 мин для §4.5 budget. §2/§3/§4 minute budget остаётся 10/10/10, но cognitive density снижена убранным duplicate metric. Net: cognitive load в §2 уменьшен на 1 evidence point (cement + chemical остаются — sufficient), §3/§4 не меняли (там evidence не дублируется).

- **P1-4 (Locked numbers list incomplete): CLOSED.** 4 missing locked numbers добавлены в Section 11 (plan-v2-part2.md):
  - **$155,04 миллиарда AI manufacturing market 2030** — line 167 (added v2).
  - **$17,15 миллиарда OPC UA + MQTT industrial AI 2026** — line 168 (added v2).
  - **PdM программа: $200K–$600K → $1,2M–$3,5M → 18–36 месяцев** — line 181 (added v2).
  - **Tesla 2018: ~10% от 5K Model 3/week target к концу месяца** — line 174 (added v2).
  - Convention: «Lock numbers convention (FINAL — fact-checker верифицирует)» — line 165.

- **P1-5 (Twin taxonomy Kritzinger 2018): CLOSED.** Kritzinger taxonomy mini-table добавлена в plan-v2.md §1 (lines 161–166) с 3 уровнями (Digital Model / Digital Shadow / Digital Twin) + Live-data-flow column + control-action-back column + 2026 пример. Источник цитирован (Kritzinger W. et al. 2018 IFAC-PapersOnLine 51(11):1016–1022, line 167). s06 plan: «Kritzinger 3-уровневая mini-table + 4-слойная архитектура справа» (line 181).

- **P1-6 (РФ context: ГОСТ + Норникель): CLOSED.** §7 Section 4 plan-v2.md обновлён:
  - **ГОСТ Р 57700.37-2021 «Цифровые двойники изделий. Общие положения»** — line 397, mandatory mention с carry-forward инструкцией book-editor цитировать определение в chapter §1 (lines 397 + 163).
  - **Норникель flotation + измельчение AI** — line 400, carry-forward от lec-11 §3.5 с явным «синергия с Yokogawa FKDPP §4 — оба process-control».
  - s35 hero options: КАМАЗ или Норникель (line 418).

- **P1-7 (L3 humanoid fragmentation): CLOSED — Hybrid (Q3 owner decision).** 
  - **§4.5 dedicated 2 мин** добавлен (plan-v2.md lines 281–302) — Toyota Digit + BMW Leipzig + 3 блокера (regulatory + cost + complexity). Budget compensation: §6 8→6 мин подтверждена (s34 dropped per line 386 «(s34 edge AI cabinet photo из v1 — dropped per Q3/Q5 для §4.5 budget.)»).
  - s23a new slide (plan-v2-part2.md line 51) — split: Toyota Digit photo + 3 блокера card.
  - **Disclaimer на s02 keystone (line 79):** «A3 в 2026 — единицы кейсов в production; основная масса A0–A2. Это асимметрия, не недостаток шкалы». 
  - Holistic: Section 1 Big Idea «Четвёртая мысль» (lines 48) даёт антропологический контекст (BMW Leipzig + Toyota Digit 7+ единиц) — связь к keystone Section 2 явная.

# P2 closure status (6)

- **P2-1 (Hero s07 — 6-tier): CLOSED.** Plan-v2.md Section 6 lines 509–515 — 6-tier acquisition fully расписан: T1 press.siemens.com → T2 news.siemens.com → T3 Wikimedia Commons → T4 YouTube CES 2026 keynote thumb → T5 Wayback Machine → T6 Google Images filtered. Attribution: «Image: Siemens AG / Press release, CES 2026» (line 517).

- **P2-2 (s05 vector diagram «4 layers required»): CLOSED.** Plan-v2.md line 180: «s05 (что НЕ цифровой двойник): **vector diagram «4 layers required»** — слои physical / sensors / model / AI-consumers с пометкой «без любого из них = не twin» (методически чище, чем composite split-screen)». Section 11 designer carry-forward (plan-v2-part2.md line 196) явно: «s05 — vector diagram «4 layers required» (NOT composite split-screen) per P2-2».

- **P2-3 (Russification 4 missing patterns): CLOSED.** Section 8 (plan-v2-part2.md) Russification table расширена (lines 104–107):
  - **cascade → каскад срабатываний** (NEW v2)
  - **expectation gap → разрыв ожиданий** (NEW v2)
  - **data layer audit → аудит слоя данных** (NEW v2)
  - **worked example → проработанный пример** (NEW v2)
  - Carry-forward для Phase 9 speech-writer (line 204): «Russification mandate + 4 new patterns».

- **P2-4 (Bridge s39 lock): CLOSED.** Bridge phrasing locked: «**AI в логистике, цепях поставок и транспорте**» (plan-v2.md frontmatter line 21 hero_s39_plan, line 439 §8 bridge, line 529 Section 6, plan-v2-part2.md line 118 Section 9 explicit «locked canonical phrasing covers oба framing»).

- **P2-5 (s02 keystone vector diagram, NOT 5-col table): CLOSED.** Plan-v2.md line 146 media plan §0: «s02 (keystone): диаграмма шкалы — 4 ступени, 1 пример на ступень, подпись "Цифровой двойник — мост между A1 и A2". **Vector diagram** (НЕ 5-col table). Первая строка: ISA-95 disambiguation. Disclaimer A3-asymmetry». Section 11 designer carry-forward (plan-v2-part2.md line 195): «s02 keystone — vector diagram of ladder (NOT 5-col table) per P2-5».

- **P2-6 (Q&A backup в Section 11): CLOSED.** Carry-forward для Phase 2 book-editor (plan-v2-part2.md line 162): «**Q&A backup (Q7 decision):** 12–14 ожидаемых студенческих вопросов с 200–300-словесными ответами (целевой объём ~3–4k слов к 30k target). Pattern carry-forward от lec-11». Phase 9 speech-writer carry-forward (line 207): «Q&A backup secondary source — speech-writer финализирует Q&A list совместно с book-editor (12–14 questions, lec-11 эталон)». Total target ~30k chapter + ~3-4k Q&A = consistent с chapter depth baseline.

# Reader-side additions verification

Все 5 reader-side P1 (R-1…R-5 из SYNTHESIS) применены.

- **R-1 (Inline gloss 9 jargon terms): CLOSED.** Verified в plan-v2.md:
  - **TSN** — «Time-Sensitive Networking, IEEE 802.1 — детерминированная доставка Ethernet-пакетов…» (line 369)
  - **FKDPP** — «Factorial Kernel Dynamic Policy Programming, NAIST 2018, off-policy RL с факториальной ядровой декомпозицией; премия премьер-министра Японии 2023» (line 258)
  - **GAMP 5** — «Good Automated Manufacturing Practice v5, основной gold-standard для валидации программных систем в фарма-производстве» (line 321)
  - **ATEX Zone 0** — «взрывоопасная среда категории 0 — постоянное присутствие… vs Zone 1 — периодическое; Zone 2 — редкое; IEC 60079» (line 322)
  - **scan-based execution** — «PLC выполняет программу циклами фиксированной длительности 1–10 мс, не event-driven» (line 234)
  - **Lighthouse Network** — «программа World Economic Forum + McKinsey, отбирающая заводы-образцы с full AI-transformation» (line 376)
  - **SHAP / LIME** — «SHapley Additive exPlanations / Local Interpretable Model-agnostic Explanations — методы post-hoc оценки вклада признаков» (line 321)
  - **MTBF** — «Mean Time Between Failures, средняя наработка на отказ» (line 216)
  - **RCM** — «Reliability-Centered Maintenance — методология Nowlan-Heap 1978, разработанная для авиации» (line 222)

- **R-2 (1-фраза-якорь для 4 альтернатив): CLOSED.** Verified:
  - **MPC** — «модельное предиктивное управление с явной оптимизацией на горизонте; гарантии устойчивости через теорию Ляпунова» (line 276)
  - **formal verification** — «математическое доказательство свойств кода: TLA+ / SPIN / Coq / SCADE для safety-critical» (line 277)
  - **RCM** — «методология Nowlan-Heap 1978 из авиации» (line 222 + reuse line 467)
  - **IEC 61508 SIL 2/3** — «вероятностные категории отказоустойчивости: SIL 2 = 10⁻⁶..10⁻⁷, SIL 3 = 10⁻⁷..10⁻⁸ на час» (line 271)

- **R-3 (§7 career section — descriptions day-to-day): CLOSED.** Plan-v2.md §7 расширен с 4 названий до **4 ролей с 4-column table** (lines 406–411): «что делает день за днём / ключевые навыки / где учиться». 4 роли — AI/ML engineer (industrial), Digital twin engineer, MES integration specialist, Edge AI engineer. Generic «профильные технические магистратуры» (no named institutions). + bonus KIIcontext (line 413).

- **R-4 (Section 1 «вторая мысль» сжата): CLOSED.** Plan-v2.md line 44: «**Вторая мысль (сжатая, forward-pointer на §5):** на каждой ступени есть *задачи, для которых AI не подходит* — раздел §5 даёт 10 формальных критериев». Одна строка + forward pointer — partial duplication с §5 устранена.

- **R-5 (3 concrete failure examples): CLOSED.** 
  - **ChatGPT MOV %M99999** в Siemens S7-1500 (line 234, M-область до M65535) — concrete addressing.
  - **RL sim-to-real concrete** (T=300°C sim vs T=315°C real + surface fouling 10% excursion) — line 261.
  - **Data-layer audit 5-вопросный checklist** — lines 191–195 (5 questions: historical data ≥1 year / sampling rate / labeling provenance / sensor drift / governance owner).

# New issues (если v2 ввела что-то new)

Нет новых P0/P1 issues. Minor observations (non-blocking, informational):

- **Plan-v2.md line 535 navigation footer содержит «вы здесь»** — это plan body, не slides body. CLAUDE.md «No timing/methodology in slides» ENFORCED только для visible body slides; plan-сам — мета-документ, навигационный маркер acceptable. Информационно.
- **Lec-11 cross-references расширены** (line 265 plan-v2-part2.md upstream impact): §2.4, §3.5, §5.3, §1.2, §3.2. Это полный 5-point cross-ref pattern — улучшение over v1.
- **Section 9 «Bridge to Лекция 13»** добавлен явный отдельный раздел (plan-v2-part2.md lines 116–125) — strengthens curriculum continuity.

# Failure-share recalc

- **Plan v1:** 33 мин / 75 = 44% (claimed) — independent recalc 41–44% strict-in.
- **Plan v2:** **33 мин / 75 = 44%** strict-in (net 0 для bucket math: §4.5 +1 мин bucket; §6 -1 мин bucket — sum unchanged).
- **Distribution:** §1 (4 мин — 75% fail + Southeast Asian Port + 11%/14% gap + Kritzinger «Model/Shadow не twin» negative def), §2 (4 — FP cascade, vision limits, metrology), §3 (4 — ChatGPT MOV, purpose-built alt), §4 (4 — sim-to-real concrete, hazardous, MPC alt), **§4.5 (1 — A3 blockers — NEW в v2)**, §5 (15 — Southeast Asian Port intro + 10 критериев + матрица альтернатив + worked example фарма+FDA + 5 вопросов вендору), §6 (1 — 11%/14% gap). **7 разделов с bucket content**, holistic (не сконцентрировано). 
- **Per-artifact distribution** (Section 5 plan-v2-part2.md lines 481–483): **chapter 73%** (~22k из 30k); **slides 45%** (15/33); **speech 44%** (~2.2k из 5k). All ≥30%.

# Anti-overlap re-check

- **Yokogawa angle: CLEAN.** Line 255 «Ключевая грань lec-12 (не lec-11): twin как safe sandbox для RL обучения ДО переноса на железо». Line 259 «lec-11 — алгоритмический breakthrough; lec-12 — архитектурный механизм… как digital twin служит safe sandbox». s22 «Digital twin как RL sandbox» — central new angle. Strict differentiation от lec-11 §3.2. ✓
- **Tesla 2018 weight: SINGLE LINE + CROSS-REF.** Не narrative-heavy. Hero §5 = Southeast Asian Port 2024 (s25 reassigned). Tesla 2018 в plan-v2 = (1) media-образ mention в Big Idea (line 40, single-line context), (2) cross-ref line 42, (3) keystone illustration line 67 (single phrase), (4) §5 explicit «Tesla 2018 = single text mention с cross-ref» line 308 + 340. **0 cases of narrative duplication of lec-11 §2.4 (paradox of automation, Bainbridge 1983, GM Hamtramck etc.)**. ✓
- **ChatGPT-PLC cross-ref: PRESENT.** Line 234 explicit «Cross-ref lec-11 §1.2 (GE Predix / Watson Health / Foxconn — foundation models дополняют, не замещают)». В lec-12 углубление = MOV %M99999 concrete + PLC Copilot purpose-built — direct new angle. ✓

# Self-checks

- [x] **Deep latin-token scan:** anglicisms outside brand allowlist — **0 critical hits**. Verified: 4 missing Russification patterns добавлены (cascade, expectation gap, data layer audit, worked example). Brand-only tokens dominate. Plan-internal acceptable (meta-tokens hero/Tier/plan OK; tech-acronyms TSN/FKDPP/GAMP с inline gloss OK; brand-allowlist names OK).
- [x] **0 named institutions:** verified grep `МГТУ|Бауман|bauman|ИУ|ВКА|vka|МАИ|СПбГУ` = **0 hits** в plan-v2.md + plan-v2-part2.md. ✓
- [x] **Hero 6-tier all:** s01 (line 497) ✓, s07 (lines 509–515) ✓, s39 (line 525) ✓ — все 6-tier explicit.
- [x] **A0-A3 rename complete:** Frontmatter ✓ (line 17), Section 2 ✓ (line 56), Section 3 minute budget ✓ (lines 104–113), Section 4 per-section detail ✓ (§2 A0 line 201, §3 A1 line 226, §4 A2 line 253, §4.5 A3 line 281), Failure inventory ✓ (Section 5 references «A0/A1/A2/A3» throughout). **0 «лестница L0–L3»** в axis-step context остался; L0–L2 references remain **только** в ISA-95 disambiguation (4 hits — все в context «не путать с ISA-95»). ✓
- [x] **L4+ Chapter Depth Baseline:** target 30 000 слов записан в frontmatter (line 19), carry-forward для book-editor explicit (line 157). Q&A backup ~3-4k слов over 30k (line 162). ✓
- [x] **Keystone-axis structural check:** ось предъявлена в Section 2 (lines 53–96) **ДО** первого погружения в A0 (§2 начинается line 201). s02 — dedicated keystone slide с 4 ступенями + disclaimer ISA-95 + disclaimer A3-asymmetry. ✓
- [x] **Cross-reference research-dump:** все 18 numbers из research-dump §10 + 4 new locked numbers — attributed inline. Lock-list в Section 11 (lines 165–186). ✓
- [x] **No designer-extras в plan body:** 0 hits в plan-v2 body для `[VERIFY-DAY-OF]` / «Лектору» / «Вы здесь» в slide body / timing markers в slide body / `LO[1-9]` codes visible — все LO-codes в frontmatter only. (Navigation footer plan-v2.md line 535 «вы здесь» = navigation, не slide body — acceptable.) ✓
- [x] **Curriculum continuity:** lec-03 (архитектуры AI), lec-07 (HITL/FDA), lec-11 (discrete/process taxonomy) listed как prerequisites; lec-13 forward bridge locked в Section 9. ✓

# Verdict justification

**APPROVE-CLEAN** legitimate. Counter-check applied: **0 P1 unresolved** (all 7 closed with concrete evidence), **0 P2 unresolved** (all 6 closed), **5 reader-side P1 closed**. Failure-share independently re-verified = 44%, holistic distribution across 7 разделов + 3 артефактов (chapter 73% / slides 45% / speech 44%). Anti-overlap с lec-11 clean (3 vendor cases differentiated с explicit angle). 0 named institutions verified. A0-A3 axis rename cascade complete. Plan v2 готов к Phase 2 (chapter draft, ≥30k слов).

**Готовность к Phase 2:** Section 11 carry-forward instructions для book-editor + designer + speech-writer полные; cascade-of-changes documented; lec-11 cross-refs explicit (5 points). Phase gate можно открывать.

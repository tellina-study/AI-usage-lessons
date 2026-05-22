---
critique_of: library/lectures/lec-12/{deck.yaml, slides/*.md, rendered/lec-12.pptx, snapshots/*.png} (39 slides v1)
critic: presentation-critic
verdict: REVISE
created: 2026-05-22
---

# Summary

VERDICT: **REVISE**

Counter-check (mandatory): 1 P0 + 14 P1 → REVISE (≥5 P1 hits the bright-line; structural anglicism failure + structural designer-extras leak both at GATE-blocking level per memory rules [[russification]] and [[feedback_no_timing_no_methodology_in_slides]]).

Headline issues:

1. **P0 — Russification depth fail.** Deep latin-token scan on rendered PPTX visible body: **282 unique latin tokens / 424 occurrences** вне brand allowlist. Designer self-reported ~140 residual; actual count is roughly 2× that. Per CLAUDE.md anti-pattern table «pattern-narrow grep как verification» + memory rule [[russification]], owner reject pattern from lec-08 («это просто трындец! провал»). Body has whole English content phrases (e.g. «sort cost растёт», «throughput loss», «оператор начинает override», «AI/ML engineer industrial», «Digital twin engineer», «MES integration specialist», «Edge AI engineer», «PLC deploy», «Safety check», «test cases», «only если все passed», «Hardwired PLC», «hard constraints (PV, MV, output)», «Excursion», «Surface fouling», «missing real-life информация», «FDA-required», «Verdict», «AI accuracy ±0,5% < required tolerance ±0,1%», «agentic AI for manufacturing», «pitch», «refund, pivot, continued integration», «pilot fails», «General references», «exit-стратегии», «sub-сегменте», «vendor question framework», «densest failure bucket», «full AI-трансформацией», «EBIT vs peers», «HITL final authority», «GPU micro-servers», «Pub/sub broker для тысяч устройств; lightweight»). This is structural, not polish.

2. **P0-adjacent → P1 «Timing markers on visible body».** 13 hits на «N минут» / «N мин». Section dividers s05/s11/s15/s19/s24/s26/s32/s36 ВСЕ показывают «Раздел N · M слайд(а/ов) · K минут» на видимой области. Cover s01+s02 показывают «75 минут + Q&A». Per memory rule [[feedback_no_timing_no_methodology_in_slides]] и CLAUDE.md anti-pattern table «Methodist comments на слайдах» — user правит в КАЖДОЙ лекции, ENFORCED. Также s26 имеет «densest failure bucket» — это методический LO-маркер на visible body.

3. **P1 — Hero structural shortfall.** s01 + s39 = 39% area (designer self-reported), measured against ≥40% threshold per [[hero-images-required]]. Slight, но это «cost of omission lec-08» memo pattern. Кроме того s39 hero — общая Toyota фабрика, НЕ связан visually с Toyota Digit (которая в speech упомянута как bridge); студент не видит «Digit на RAV4 line» visually — это и есть emotional payoff. Caption «Toyota Motor Manufacturing · Burnaston Derby» проходит attribution, но содержательно НЕ hero к Lec-13 keystone.

4. **P1 — Schema readability fails (5 schema slides).** s07 4-layer (Siemens HQ photo dwarfs все layer-cards, font ≤10pt на projector — fail 50% zoom), s12 right callout (текст слишком плотный + anglicism saturation), s20 Yokogawa (image dominates, text каскад мелкий), s25 A3 cases (3 структурных блокера слишком тесно справа), s27 Port intro (port photo доминирует, text микро-расположен с FRONT label «ПРОВАЛ»). Эти 5 не пройдут Schema Readability Checklist §5.5.

5. **P1 — Designer-extras leak.** Visible body содержит:
   - `5 слайдов · 10 минут` style на ВСЕХ section dividers (designer-added timing UI).
   - `densest failure bucket` на s26 (LO bucket marker — методическая фраза).
   - `Раздел 4.5 · 1 слайд · 2 минуты` — это методический pacing UI, не student-visible content.

# P0 issues (blocking)

## P0-1 — Russification deep-scan FAIL: 282 unique latin tokens / 424 occurrences в visible body

**Severity:** P0 (structural gap, not polish — memory rule [[russification]], cost-of-omission lec-08 = «провал» от owner)

**Issue:** Designer self-reported residual ~140 anglicisms post-iter-3. Independent deep-scan на rendered PPTX visible text shows **282 unique / 424 occurrences** (brand allowlist applied). Critical content phrases в visible body — не technical mode names (which are whitelist) but full English phrases:

| Slide | Anglicism leak (visible body) |
|---|---|
| s12 | «sort cost растёт», «throughput loss», «оператор начинает override» |
| s14 | «patterns в шуме», «laser scanner, CMM», «Geometric Dimensioning & Tolerancing», «Statistical Process Control», «Reliability-Centered Maintenance» |
| s17 | «purpose-built», «generic LLM на низком уровне (PLC) — провал», «Что выдаёт ChatGPT (промпт «оптимизируй»)», «Что не так», «Generic LLM не знает циклическое исполнение, не знает legal addresses конкретной модели» |
| s18 | «Safety check», «test cases», «PLC deploy», «только если все passed», «safety-протоколы перед deployment», «inженер с правом veto» |
| s22 | «Surface fouling», «Excursion на 10% от штатного режима за 60 дней», «missing real-life информация» |
| s23 | «edge cases по definition», «Hardwired PLC», «hard constraints (PV, MV, output)», «output несовместим с IEC 61508 SIL 2/3», «Недетерминированный output» |
| s26 | «densest failure bucket» (methodological LO marker) |
| s28 | «Defect detection нестабильного процесса», «Tight tolerances ±0,001 мм», «Generic PLC code generation», «FDA 21 CFR Part 11, GAMP 5», «Explainable AI», «ATEX Zone 0», «data audit fails» |
| s29 | «Verdict», «FDA-required ±0,1%», «AI accuracy ±0,5% < required tolerance ±0,1% — НЕСОВМЕСТИМО», «advisory tool на этапе process design», «statistical batch sampling для release», «validated USP / GMP» |
| s30 | «pitch «agentic AI for manufacturing»», «expectation gap», «twins без ROI» |
| s31 | «refund, pivot, continued integration», «pilot fails», «exit-стратегии», «sub-сегменте (process / discrete / regulated)», «General references», «failure-кейсов», «vendor продаёт hype», «vendor question framework» |
| s33 | «HITL final authority», «GPU micro-servers», «sampling rate ≥10× полоса управления», «inference <10 мс» |
| s34 | «Pub/sub broker для тысяч устройств; lightweight», «реалистичен для IIoT с ограниченным каналом», «Open Platform Communications · Unified Architecture», «гарантированная задержка доставки Ethernet-пакетов» |
| s35 | «full AI-трансформацией», «EBIT vs peers» |
| s38 | «AI/ML engineer (industrial)», «Digital twin engineer», «MES integration specialist», «Edge AI engineer», «День за днём», «Дизайнит и тренирует модели», «vision QC, PdM, alarm», «edge runtime · мониторит drift», «Python + PyTorch · MLOps · OPC UA basics», «workflow рекомендация → апрув → исполнение», «Opcenter/FactoryTalk/SAP MII», «Деплоит inference на edge (Jetson, Modicon edge)», «оптимизирует latency», «C++/Rust · встроенный Linux», «ONNX/TensorRT · планирование в реальном времени», «КИИ-cybersecurity», «Coursera/edX курсы NVIDIA Omniverse, Siemens Industrial AI» |

**Recommendation:** sed pass на slide source files + rebuild. Target — `unique - whitelist = ∅` для narrative body (PPTX). Acceptable Latin: brand names (Siemens, NVIDIA, Toyota, BMW, Yokogawa, FKDPP, JSR, Composer, Omniverse, ThingWorx, AVEVA, Xcelerator, Lighthouse, Gartner, McKinsey, Deloitte, Foxmere, Wikimedia), tech acronyms с inline gloss (PLC, MES, SCADA, OPC UA, MQTT, TSN, RL, MPC, FDA, IEC, ATEX, SIL, GAMP, ROI, MTBF, RCM, SPC, GD&T, ISO, IIoT, HITL, LLM, AI, ML, GPU, CAD, ERP, PoC, EBIT), official term abbreviations (CFR, USP, GMP). Translate phrases: «throughput loss» → «потеря пропускной способности», «override» → «перекрытие», «test cases» → «тестовые случаи», «Hardwired PLC» → «проводной PLC», «hard constraints» → «жёсткие ограничения», «Surface fouling» → «поверхностные отложения», «Excursion» → «отклонение», «Verdict» → «Вердикт», «advisory tool» → «инструмент рекомендации», «pitch» → «коммерческое предложение», «refund, pivot, continued integration» → «возврат денег, разворот, продолжение интеграции», «pilot fails» → «провал пилота», «vendor question framework» → «шаблон вопросов вендору», «full AI-трансформация» → «полная AI-трансформация», «Digital twin engineer» → «инженер цифрового двойника», «MES integration specialist» → «специалист по интеграции MES», «Edge AI engineer» → «инженер ИИ на границе сети», «edge runtime» → «среда исполнения на границе», «drift» → «дрейф», «basics» → «основы», «workflow» → «рабочий процесс», «inference» → «инференс» (или «работа модели»), «latency» → «задержка», «throughput» → «пропускная способность».

# P1 issues (high-priority)

## P1-1 — Designer-extras: timing markers visible on body (13 hits)

**Severity:** P1 (memory rule [[feedback_no_timing_no_methodology_in_slides]], ENFORCED — user правит в КАЖДОЙ лекции)

**Issue:** Visible body содержит timing markers:
- s01 + s02: «75 минут + Q&A» (cover)
- s05 «Раздел 1 · 5 слайдов · 10 минут»
- s11 «Раздел 2 · 3 слайда · 10 минут»
- s15 «Раздел 3 · 3 слайда · 10 минут»
- s19 «Раздел 4 · 4 слайда · 10 минут»
- s24 «Раздел 4.5 · 1 слайд · 2 минуты»
- s26 «Раздел 5 · 5 слайдов · 15 минут — densest failure bucket»
- s32 «Раздел 6 · 3 слайда · 6 минут»
- s36 «Раздел 7 · 2 слайда · 5 минут»

**Recommendation:** Удалить ВСЕ timing markers + «N слайдов» pacing markers + «densest failure bucket» с visible body. Cover s02 — оставить только «Модуль 2» без «· 75 минут + Q&A»; либо «Курс «Применение AI в инженерии» · 2026» footer. Section dividers — только number + title + RU subtitle topic line. Pacing budget — в speech.md, не в slides.

## P1-2 — s26 «densest failure bucket» LO methodology marker visible

**Severity:** P1 (designer-extras leak, English методический термин)

**Issue:** s26 divider subtitle: «Раздел 5 · 5 слайдов · 15 минут — densest failure bucket». «Densest failure bucket» — это методический marker из failure-bucket измерения (AI-Failure & Judgment Content Rule, strict-in measurement). Student не должен видеть.

**Recommendation:** Удалить.

## P1-3 — Hero s01 + s39 = 39% area (vs ≥40% target)

**Severity:** P1 (memory rule [[hero-images-required]])

**Issue:** Designer iteration-log: «Hero area: approximately 6.5×6.0 inches = 39 кв.дюйм = 39.0% of 100 кв.дюйм canvas». Это -1pp shortfall. Acceptance criteria требует ≥40%.

**Visual evidence:** Hannover Messe robot hand visible left, но composition вокруг текст-heavy.

**Recommendation:** Expand s01 + s39 hero к full-bleed left half (≥45% width × full height = ≈45%) или full-bleed background + text overlay. Cost: 2 builds × 39 slides ≈ 1 min.

## P1-4 — s39 hero NOT bridge к Lec-13

**Severity:** P1 (memory rule [[hero-images-required]] — s39 «должен bridge к Lec-N+1 OR emotional payoff»)

**Issue:** s39 hero = «Toyota Motor Manufacturing · Burnaston Derby» — общая фабрика Toyota. Speech s39 + assertion: «Toyota Digit на RAV4 line — первая ступень supply chain. Лекция 13 расширит до глобальной цепочки». Student visually видит generic фабрику, НЕ humanoid Digit, НЕ supply chain. Emotional payoff weak.

**Recommendation:** Replace на Agility Robotics Digit photo (Tier 1 og:image agility.com newsroom; Tier 2 commons.wikimedia.org Digit или Cassie images), либо composite split: left = current factory frame, right = Digit humanoid photo + bridge caption «Toyota Digit на RAV4 — первая ступень supply chain → Лекция 13». Если 6/6 tier failure — document in iteration-log.

## P1-5 — s07 4-layer schema layered FAIL Readability Checklist

**Severity:** P1 (schema_layered subtype, §5.5 Schema Readability Acceptance Gate)

**Issue:** Per visible PNG: Siemens HQ photo занимает левую 60% слайда; 4 layer-cards справа крошечные (font ≤10pt projector 50% zoom test — fail). Bottom-aligned compliance unclear из-за text small.

**Visual evidence:** На полном snapshot layer-cards имеют overlay-style design с тонкими text-полосами; «1. Физический актив», «2. Слой датчиков», «3. Слой модели», «4. AI-потребители» — каждый меньше 30% slide width, text вырезанный.

**Recommendation:**
- Уменьшить Siemens HQ photo до 30% (right column, top); rest = 4-layer stack с full-width cards.
- Bottom-aligned layers (общая нижняя граница).
- Каждый layer header ≥14pt, body description ≥12pt.
- Caption «Siemens Digital Twin Composer — пример платформы 2026» вне photo (под).

## P1-6 — s12 right callout overload + anglicism saturation

**Severity:** P1 (Schema Readability + Russification combined)

**Issue:** s12 right callout «100 годных деталей отвергнуто за смену 1% × 10 000» + 5 буллетов: «→ ручная переборка», «→ sort cost растёт», «→ throughput loss», «→ оператор начинает override», «→ доверие к AI рушится». 3 из 5 — full English phrases.

**Recommendation:**
- Перевод буллетов на RU: «→ ручная переборка», «→ растут затраты на сортировку», «→ падает пропускная способность», «→ оператор начинает обходить систему», «→ доверие к AI рушится».
- 5 bullets — на грани капасити карточки; уменьшить до 4 (combine #2+#3 → «→ растут затраты + падает пропускная»).

## P1-7 — s17 «Generic LLM не знает scan-based execution, не знает legal addresses» — English content

**Severity:** P1 (Russification)

**Issue:** Right card «ChatGPT generic · ПРОВАЛ»: «Generic LLM не знает циклическое исполнение, не знает legal addresses конкретной модели». «Legal addresses» — English phrase в RU sentence.

**Recommendation:** «допустимые адреса памяти конкретной модели».

## P1-8 — s18 «Safety check / test cases / PLC deploy / only если все passed» — half-English process pipeline

**Severity:** P1 (Russification + Schema Pipeline subtype unified language requirement §5.5 schema_pipeline)

**Issue:** Pipeline boxes: «AI · Инженер · Симулятор · Safety check · PLC deploy». 5-step process — 2 RU, 1 latin (Симулятор Latin in look), 2 English. Internal content также mixed: «IEC 61131-3 + test cases», «только если все passed». Pre-existing anti-pattern #17 «Mixed RU/EN sub-labels in schema».

**Recommendation:**
- Pipeline RU only: «AI · Инженер · Симулятор · Проверка безопасности · Загрузка в PLC».
- Bodies: «IEC 61131-3 + тестовые случаи», «только если все проверки пройдены».
- Fix #3 буллет внизу: «есть safety-протоколы перед deployment» → «есть протоколы безопасности перед загрузкой».
- «veto на каждое предложение AI» → «право вето на каждое предложение AI» (veto OK как established legal term, но если без gloss → перевод).

## P1-9 — s22 chart callout «Surface fouling / Excursion / missing real-life» — heavy anglicism

**Severity:** P1 (Russification)

**Issue:** Right callout «ЧТО RL НЕ ВИДИТ»: «Surface fouling — отложения на стенках колонны со временем», «Excursion на 10% от штатного режима за 60 дней», «Симуляция дешевле и быстрее, но missing real-life информация».

**Recommendation:**
- «Surface fouling» → «Поверхностные отложения» (header), keep English term inline gloss first use.
- «Excursion» → «Отклонение» (header).
- «missing real-life информация» → «отсутствует информация о реальной эксплуатации».

## P1-10 — s23 «edge cases / output / Hardwired PLC / hard constraints» mixed

**Severity:** P1 (Russification)

**Issue:** Left card «Критичный по безопасности контур»: «Недетерминированный output несовместим с IEC 61508 SIL 2/3», «Не покрывает edge cases по definition». Right card: «Учитывает hard constraints (PV, MV, output)».

**Recommendation:**
- «output» → «выход» (или «решение»).
- «edge cases» → «краевые случаи».
- «по definition» → «по построению».
- «Hardwired PLC» → «проводной PLC».
- «hard constraints» → «жёсткие ограничения».
- «PV, MV, output» — keep inline gloss «PV — process variable, MV — manipulated variable» если первое упоминание.

## P1-11 — s28 10-criteria matrix — half cells full English

**Severity:** P1 (Russification + schema_matrix §5.5)

**Issue:** Cell content:
- «4. Defect detection нестабильного процесса» (header English)
- «5. Tight tolerances ±0,001 мм» (header English)
- «6. Generic PLC code generation» (header English)
- «9. Стоимость AI > стоимость ошибки человека» (clear)
- «10. Отсутствие clear применение (data audit fails)» (mixed)
- Right column: «Explainable AI (SHAP / LIME)», «ATEX-сертифицированные датчики», «Purpose-built tool с инженер в петле ИЛИ инженер + симулятор», «Не внедрять, направить бюджет на обучение оператора», «Аудит слоя данных (5 вопросов) + remediation ДО любого пилота»

**Recommendation:**
- «Defect detection нестабильного процесса» → «Обнаружение дефектов в нестабильном процессе»
- «Tight tolerances» → «Жёсткие допуски»
- «Generic PLC code generation» → «Универсальная генерация кода PLC»
- «Отсутствие clear применение» → «Отсутствие чёткого сценария»
- «Purpose-built tool» → «Специализированный инструмент»
- «remediation ДО» → «исправление ДО»

## P1-12 — s29 worked example — English «Verdict» + «AI accuracy ±0,5% < required tolerance ±0,1%»

**Severity:** P1 (Russification)

**Issue:** 5-row table:
- Row 5 «Verdict» (English header). Row 4 «Разрыв»: «AI accuracy ±0,5% < required tolerance ±0,1% — НЕСОВМЕСТИМО».
- Footer «АЛЬТЕРНАТИВА: AI как advisory tool на этапе process design (±0,5% полезна) + человек в петле QA + statistical batch sampling для release (validated USP / GMP)».

**Recommendation:**
- «Verdict» → «Вердикт».
- «AI accuracy ±0,5% < required tolerance ±0,1%» → «AI точность ±0,5% < требуемая точность ±0,1%».
- «advisory tool на этапе process design» → «инструмент рекомендации на этапе проектирования процесса».
- «человек в петле QA» → «человек в петле контроля качества (QA)».
- «statistical batch sampling для release» → «статистическая выборка партий для выпуска».
- «validated USP / GMP» — keep USP/GMP (regulatory terms), «validated» → «валидированные».

## P1-13 — s31 vendor questions — 5/5 содержит English phrases

**Severity:** P1 (Russification)

**Issue:** All 5 sub-bullets имеют English:
1. «Без failure-кейсов вендор продаёт hype»
2. «Если вендор путается — он не понимает архитектурный класс продукта» (clean RU ✓)
3. «Без аудита — Southeast Asian Port lesson повторится»
4. «Покажите задокументированные провалы за последние 24 месяца в той же индустрии» — header OK; sub «Контракт без exit-стратегии — деньги в одну сторону»
5. «Можете показать референс-клиент в нашем sub-сегменте (process / discrete / regulated)?» + «General references — недостаточно; нужна точная индустриальная аналогия»
- Footer: «Шаблон vendor question framework — для любого AI-пилота на производстве»

**Recommendation:**
- «failure-кейсов» → «случаев провалов».
- «hype» → «хайп» (русифицировано).
- «Southeast Asian Port lesson повторится» → «урок Southeast Asian Port повторится» (или «...порта в Юго-Восточной Азии»).
- «exit-стратегии» → «стратегии выхода».
- «refund, pivot, continued integration» → «возврат, разворот, продолжение интеграции».
- «sub-сегменте (process / discrete / regulated)» → «под-сегменте (процессный / дискретный / регулируемый)».
- «General references» → «Общие референсы».
- «vendor question framework» → «шаблон вопросов вендору».

## P1-14 — s38 career bridge — total English saturation

**Severity:** P1 (Russification, ENFORCED — критическая для российской аудитории МГТУ ИУ6)

**Issue:** 4-card career layout. Card headers: «AI/ML engineer (industrial)», «Digital twin engineer», «MES integration specialist», «Edge AI engineer» — все English. Body для каждого начинается с «День за днём» (RU phrase OK), но дальше «Ключевые навыки: Python + PyTorch · MLOps · OPC UA · ...» — список full English. «Деплоит inference на edge (Jetson, Modicon edge); оптимизирует latency», «C++/Rust · встроенный Linux · ONNX/TensorRT · планирование в реальном времени · КИИ-cybersecurity».

**Recommendation:**
- Headers: «Инженер AI/ML (промышленный)», «Инженер цифрового двойника», «Специалист интеграции MES», «Инженер ИИ на границе сети» (edge → «на границе сети»).
- «vision QC, PdM, alarm» (acceptable как technical abbrev list) — оставить.
- «edge runtime» → «среда исполнения на границе».
- «drift» → «дрейф модели».
- «Деплоит inference» → «Разворачивает инференс».
- «оптимизирует latency» → «оптимизирует задержку».
- «cybersecurity» → «кибербезопасность».
- «Coursera/edX курсы» → «курсы Coursera/edX» (keep platform names).

# P2 issues (polish)

## P2-1 — s09 «Southeast Asian Port» photo composition cramped

**Issue:** Container port photo + текст-карточка справа — текст слишком плотный, line spacing < 1.2.

**Recommendation:** Increase right text-block padding + reduce content к 4 bullets max.

## P2-2 — s13 chart axis labels Y-axis truncate

**Issue:** Horizontal bar chart labels: «Затраты на обслуживание», «Незапланированные простои», «Срок службы оборудования», «Аварии». Render PNG показывает labels чётко, but font ≤10pt visible.

**Recommendation:** Tightly OK but could bump axis font to 13pt для projector readability.

## P2-3 — s16 chart x-axis sub-labels «-15м, -10м, -5м, 0, +5м, +10м»

**Issue:** Axis labels font ~9pt, нечитаемо при projector 50%.

**Recommendation:** Font ≥12pt minimum, перевести «м» → «мин» (явно).

## P2-4 — s30 chart bottom labels clipped

**Issue:** «Agentic AI отменены к 2027», «GenAI PoC прекращены в 2025», «Twin без ROI (общая винодель...)» — последний обрезан.

**Recommendation:** Increase chart container height + axis label fontSize:11; rotate labels на 25° если не помещаются.

## P2-5 — Section dividers — same template all 8 looks repetitive

**Issue:** s05/s11/s15/s19/s24/s26/s32/s36 — все имеют identical layout: big number + title + subtitle + pacing line. После убирания timing markers — proper Lec-N-1 compliance, but slight visual monotony.

**Recommendation:** OK — Lec-11 pattern carries forward correctly; не fix.

## P2-6 — s25 «3 структурных блокера A3» right column too narrow

**Issue:** Layout BMW/Toyota photo + 3 blocker-cards справа. Bullets текст обрезается visually.

**Recommendation:** Reduce photo до 40% width; expand cards.

## P2-7 — s27 hero §5 «ПРОВАЛ» trial chip too prominent

**Issue:** Red-orange «ПРОВАЛ» tag occupies top-right; tag styling looks decorative.

**Recommendation:** OK semantically (this is the failure case anchor for §5), keep.

# Per-slide issues table

| Slide | Issue | Severity |
|---|---|---|
| s01 | Hero 39% area vs ≥40% | P1 |
| s01 | «75 минут + Q&A» timing visible | P1 |
| s02 | «75 минут + Q&A» timing visible на cover | P1 |
| s05 | «5 слайдов · 10 минут» pacing visible | P1 |
| s07 | Schema_layered fail: photo dominates, layers tiny | P1 |
| s09 | Text-card cramped composition (P2) | P2 |
| s11 | «3 слайда · 10 минут» pacing visible | P1 |
| s12 | «throughput loss / sort cost / override» English bullets | P1 |
| s13 | Chart axis font ≤10pt (P2) | P2 |
| s15 | «3 слайда · 10 минут» pacing | P1 |
| s16 | Chart axis labels font ≤9pt (P2) | P2 |
| s17 | «Generic LLM не знает legal addresses» mixed RU/EN | P1 |
| s18 | Pipeline «Safety check / PLC deploy / passed» half-English | P1 |
| s19 | «4 слайда · 10 минут» pacing | P1 |
| s22 | «Surface fouling / Excursion / missing real-life» heavy English | P1 |
| s23 | «edge cases / output / Hardwired PLC / hard constraints» mixed | P1 |
| s24 | «1 слайд · 2 минуты» pacing | P1 |
| s25 | Right column 3 blockers too narrow (P2) | P2 |
| s26 | «densest failure bucket» LO methodology marker visible | P1 |
| s26 | «5 слайдов · 15 минут» pacing | P1 |
| s28 | Half matrix cells English headers | P1 |
| s29 | «Verdict / AI accuracy < required tolerance» English | P1 |
| s30 | Chart bottom labels clipped (P2) | P2 |
| s31 | 5/5 vendor questions содержат English phrases | P1 |
| s32 | «3 слайда · 6 минут» pacing | P1 |
| s33 | «HITL final authority / GPU micro-servers / inference» English | P1 |
| s34 | «Pub/sub broker / lightweight / Open Platform Communications» English | P1 |
| s35 | «full AI-трансформацией / EBIT vs peers» English | P1 |
| s36 | «2 слайда · 5 минут» pacing | P1 |
| s38 | Total English saturation career bridge | P1 |
| s39 | Hero 39% area; not visually bridge к Lec-13 (Toyota Digit absent) | P1 |
| (all) | 282 unique latin tokens / 424 occurrences | **P0** |

# Visual sweep (per snapshot)

**s01 hero:** «Hannover Messe robotic hand» visible слева ~6.5×6.0 in = 39% area; real image (CC-BY-SA); attribution «Hannover Messe 2016 · робот-манипулятор · Wikimedia · CC-BY-SA» visible bottom-left. Strong composition, good gold ladder + central anchor. **Verdict: 39% — under 40% threshold; otherwise PASS.**

**s39 hero:** Toyota factory exterior photo ~6.5×6.0 in = 39% area; real image (CC-BY-SA); attribution visible. **NOT bridge к Lec-13 visually** — student видит generic фабрику, не Digit humanoid. Toyota Digit нет на photo. **Verdict: 39% + content mismatch.**

**Schema slides assessment (12 schema slides):**
- s04 keystone autonomy ladder (assertion_visual): **PASS** — 4 cards layout works, gold A3 highlight, RU labels.
- s06 Kritzinger (assertion_visual schema): **PASS** — 3-card taxonomy clean, ГОСТ footer; «Digital Model / Shadow / Twin» — OK как inline gloss первые упоминания.
- s07 4-layer architecture (schema_layered): **FAIL** — Siemens HQ photo dominates 60%, layer-cards crowded на 40% rest.
- s10 audit 5-question (assertion_visual): **PASS** — clean numbered list, content RU OK, except «governance owner», «retention», «Drift датчиков», «Sampling rate» — partial English.
- s14 vision/PdM limits (comparison schema): **PASS structure** but body Russification — «patterns в шуме», «laser scanner, CMM», «Geometric Dimensioning», «Reliability-Centered Maintenance», «Statistical Process Control» (technical full-name listings — OK как gloss первого упоминания, но не каждый раз).
- s18 engineer-in-loop (schema_pipeline): **FAIL** mixed RU/EN sub-labels (anti-pattern #17), 5-step process mixed languages.
- s23 RL limits + MPC (comparison): **PASS structure** + Russification body.
- s28 10-criteria matrix (schema_matrix): **PASS fill rate** (10/10 = 100%) **FAIL** Russification.
- s29 worked example (assertion_visual table): **PASS** structure, **FAIL** English headers ‹Verdict, FDA-required, AI accuracy < required tolerance›.
- s31 5-question framework (assertion_visual numbered list): **PASS** structure + Russification fail per P1-13.
- s33 7-layer architecture (schema_layered): **PASS bottom-aligned**, **FAIL** Russification body «HITL final authority», «GPU micro-servers», «Time-Sensitive Networking», «sampling rate». Body sub-labels mixed.
- s34 OPC UA + MQTT + TSN (comparison 3-card): **PASS** layout, **FAIL** body Russification «Pub/sub broker», «lightweight», «Open Platform Communications · Unified Architecture».
- s38 career bridge (comparison 4-card): **STRUCTURAL FAIL** — full English headers + body.

# Russification scan

**Deep latin-token unique outside brand allowlist:** 282 unique / 424 occurrences (extended allowlist including Siemens, NVIDIA, Toyota, BMW, Yokogawa, FKDPP, MES, PLC, OPC, UA, MQTT, TSN, IEC, IIoT, PdM, RL, MPC, Kritzinger, Lighthouse, FDA, GAMP, ATEX, Composer, Omniverse, ThingWorx, AVEVA, Xcelerator, Jetson, ONNX, TensorRT, Linux, PyTorch, MLOps, КАМАЗ, ГОСТ, Росатом, Норникель etc.).

**Target:** unique - whitelist = ∅ in narrative body. **Actual: 282 unique.** ~141× the threshold.

**Critical patterns (top sed targets):**
- 13× `twin` (lower-case → translate or capitalize как branded «Twin»)
- 7× `Vision` (когда не «Vision QC» branded — переводи на «зрение/видение»)
- 5× `edge` (когда не Edge AI — переводи на «на границе»)
- 4× `Asian Port` (Southeast Asian Port case name — OK как case identifier)
- 4× `inference` (→ «инференс» или «работа модели»)
- 4× `humanoid` (→ «человекоподобный»)
- 3× `taxonomy` (→ «таксономия»)
- 3× `Network` (когда не Lighthouse Network — переводи)
- 3× `cases` (→ «случаи»)
- 3× `sampling rate` (→ «частота дискретизации»; keep inline gloss один раз)
- 2× `purpose-built` (→ «специализированный»)
- 2× `vendor` (→ «вендор» русифицировано)
- 2× `deployment` (→ «развёртывание»)
- 2× `fouling` (→ «отложения»)
- 2× `pilot` (→ «пилот» русифицировано OK как established RU loan)
- 2× `output` (→ «выход» / «выходной сигнал»)
- 2× `accuracy` (→ «точность»)
- 2× `Hardwired` (→ «проводной» / «жёстко проводной»)
- 2× `lightweight` (→ «легковесный»)
- 1× `densest failure bucket` (методический LO marker — DELETE)
- 1× `Verdict` (→ «Вердикт»)
- 1× `Defect detection` (→ «Обнаружение дефектов»)
- 1× `process redesign` (→ «перепроектирование процесса»)
- 1× `worked example` (→ «проработанный пример»)
- 1× `legal addresses` (→ «допустимые адреса памяти»)
- 1× `governance owner` (→ «ответственный за данные»)
- 1× `Drift` (→ «дрейф»)
- 1× `Pattern` (→ «Паттерн» русифицировано)
- 1× `EBIT vs peers` (→ «EBIT vs средние по индустрии»)
- 1× `vendor question framework` (→ «шаблон вопросов вендору»)
- 1× `keystone` (→ «несущая ось»; OK как title term если first-use)
- 1× `full AI-трансформацией` (→ «полной AI-трансформацией» лишний «full»)

**Estimated sed/translation effort:** 1 hour for tool-assisted replace + rebuild + re-render.

# Strengths

- **Lec-N-1 pattern compliance:** lecture-map s03 + section dividers s05/11/15/19/24/26/32/36 + glossary-like keystone s04 ✓.
- **Roadmap-bar discipline:** только на cover s02 + section dividers (правильно, не на каждом content slide).
- **Hero acquisition Tier 2 Wikimedia:** 21 real images via Commons API — proper documented in iteration-log.md per 6-tier rule [[no-mock-fallbacks]].
- **Chart QuickChart usage:** 7 charts, mostly clean (после iter 2 fixes of «undefined» legends).
- **Schema_matrix s28 fill rate 100%:** 10/10 cells filled — no skeleton anti-pattern #12.
- **Designer-extras (other than timing): «Лектору» / «Вы здесь» / LO codes / `[VERIFY-DAY-OF]` / lec-NN cross-refs / § cross-refs — все 0 hits.** Iter 3 cleanup successful.
- **Cover s02:** clean composition «12» decorative + lecture title + central question — well done.
- **Keystone s04 autonomy ladder A0→A3:** strong visual, gold A3 highlight, ISA-95 disclaimer working.
- **Speaker notes derive from chapter:** sample s06/s17/s28/s33/s38 — 169-219 words connected text, не layout descriptions, не cues. Acceptable несмотря на residual technical terminology.
- **Failure bucket coverage:** s09 + s14 + s17 (PLC fail) + s22 (sim-real gap) + s23 + s27 + s28 + s29 + s30 + s31 + s33 (HITL) — strict-in failure/judgment slides clearly visible ≥30% target met.

# Specific recommendations (top 7)

1. **(P0) Apply full Russification sed pass на slide source files +rebuild.** Target unique - whitelist = ∅ в narrative body. ~1h effort. Mandatory before GATE B.

2. **(P1) Strip all timing markers from visible body** на cover s01+s02 + 8 section dividers. «75 минут + Q&A» / «5 слайдов · 10 минут» / «densest failure bucket» — все DELETE. ~10min.

3. **(P1) Expand hero s01 + s39 to ≥40% area.** Either full-bleed left half or full-bleed background. ~20min.

4. **(P1) Re-acquire s39 hero к Toyota Digit humanoid** — Agility Robotics Digit photo или composite split с current factory + Digit overlay. Per [[hero-images-required]] s39 «bridge к Lec-N+1». ~30min.

5. **(P1) Rebuild s07 4-layer schema:** uменьшить Siemens HQ photo до 30%, bottom-align 4 layers full-width, font ≥14pt layer headers + ≥12pt body. ~20min.

6. **(P1) Rebuild s38 career bridge:** full Russification card headers + body. «AI/ML engineer (industrial)» → «Инженер AI/ML (промышленный)» и так далее. Critical career-bridge slide для МГТУ ИУ6 RU аудитории. ~15min.

7. **(P1) Fix s18 pipeline mixed RU/EN sub-labels:** unified RU only. ~5min.

# Self-checks

- [x] **All 39 snapshots inspected via Claude vision:** s-01 to s-39 — все прочитаны через Read PNG. ✓
- [x] **Deep latin-token scan:** unique count 282 / 424 occurrences (extended brand allowlist applied). **TARGET 0 — FAIL P0.**
- [x] **Schema Readability:** 13 schema slides checked. 8 pass structure, 5 fail (s07 layered, s18 pipeline, s28 matrix Russification, s29 worked example Russification, s38 career bridge Russification). 8/13 pass = 62%.
- [x] **Designer-extras grep (all 13 patterns):** «Лектору» 0, «Вы здесь» 0, `[VERIFY-DAY-OF]` 0, `[FACT-CHECK]` 0, LO[1-9] 0, §X.Y 0, → sNN 0, (sNN) 0, точк* возврата 0, «—в главе» 0, «в материалах лекции» 0, lec-NN 0. **HOWEVER: timing «N минут» 13 hits + «densest failure bucket» 1 hit = P1.**
- [x] **Hero ≥40%:** s01 39% (-1pp), s39 39% (-1pp + content mismatch к Lec-13). **FAIL.**
- [x] **Lec-N-1 pattern:** lecture-map s03 ✓, section dividers (8) ✓, dedicated Q&A merged with hero s39 + s38 career bridge — acceptable per deck.yaml comment. Roadmap-bar только на dividers + cover ✓. **PASS structure.**

# Decision rationale (4-level verdict)

- P0 count: **1** (Russification depth fail, structural gap).
- P1 count: **14** (timing markers ×9 dividers/cover + densest failure bucket + hero 39% + s39 hero mismatch + 5 schema slides + 8 русификация slides duplicated в Russification P1).
- P2 count: **7** (cosmetic).

**Bright-line rule:** ≥5 P1 → REVISE. Hit at 14. Verdict: **REVISE** (mandatory revise pass + re-render + critic re-run before GATE B).

**Block on GATE B until:**
- Deep latin scan unique - whitelist = ∅ (или <10 isolated technical exceptions с documented inline gloss).
- 0 timing markers in visible body.
- s01 + s39 hero ≥40% area.
- s39 hero shows Toyota Digit или bridge visual к Lec-13.
- 5 schema slides (s07, s18, s28, s29, s38) re-rendered с Russification.

After fixes — re-spawn presentation-critic for one verification pass on changed slides + deep scan re-run.

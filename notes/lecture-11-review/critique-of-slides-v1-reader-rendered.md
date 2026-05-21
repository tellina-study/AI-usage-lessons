VERDICT: APPROVE-CLEAN

# Reader (Rendered) Report — Лекция 11 — 2026-05-21

**Mode:** rendered (PNG + speaker notes, через 2 недели после лекции).
**Перспектива:** студент 3 курса ИУ6 МГТУ, готовится к РК, лектора нет, есть только snapshots + notes. Лекция была 2 недели назад, многое в голове размылось.
**Inputs:** 39 PNG snapshots + 39 speaker notes (md). Chapter использовался только для cross-check, не предполагается что у студента есть chapter в кармане.

---

## 1. Self-Containedness Verdict (summary first)

**Self-contained: 34/39 = 87%.** Это выше production-threshold 85% и существенно лучше Лек-1 v3 (28/34 = 82%). Notes — действительно readable connected текст 200-400 слов на content slides; почти везде хорошо повторяют main concept слайда + дают backstory. Cornerstones (двухколонная схема, OT/IT, OEE-callback, мягкий сенсор, эталонная разметка, 4 категории, 5-step framework) проходят retention test через 2 недели — могу свободно восстановить из снапшотов + notes.

**Минусы:** 5 слайдов с частичной self-containedness (s08 «VFY-day-of» leak + один technical slide где notes есть, но требуют почти chapter-level density для нового читателя), 1 hero-replay с тесной типографикой (s39), и потенциал anglicism-pollution в notes (см. §6).

---

## 2. Per-Slide Self-Contained Status (39 слайдов)

| Slide | Self-contained | Notes-quality | Visual-quality | Note |
|---|---|---|---|---|
| s01 hero Tesla giga-press | да | excellent | hero photo + цитата + central question | Главная мысль ясна без лектора. |
| s02 cover + LO | да | good | LO структурированы | LO явно перечислены. |
| s03 lecture-map | да | good | 5 секций × длительности | Roadmap читается. |
| s04 glossary | да | excellent | 6 terms × 2 columns | OEE / soft sensor / ISA-95 определены. |
| s05 keystone | **да — strong** | excellent | две колонны + universal-пояс | Cornerstone восстанавливается через 2 нед. |
| s06 §1 divider | да | good | section break | Стандартный. |
| s07 adoption gap | да | excellent | donut + bars + 4 источника | 78% / 5,5% запоминается. |
| s08 market estimates | **частично** | good | bars + caveat | **«[VFY-day-of]» visible в footnote** — designer-extras leak. Content OK, но scaffold-токен на PNG (P1). |
| s09 OT/IT раскол | **да — strong** | excellent | две колонны OT vs IT + bottom yellow callback | Cornerstone восстанавливается. |
| s10 foundation models | да | excellent | 3 reasons | «augmentation не controller» с тремя причинами — ясно. |
| s11 Tesla Optimus demo | да | excellent | demo vs production split | Anti-pattern «демо ≠ production» ясен. |
| s12 hype-collapse trio | да | excellent | 3 cards × 4B+ | GE / IBM / Foxconn WI с уроками — restorable. |
| s13 §2 divider | да | good | section break | ok |
| s14 CV-инспекция | да | excellent | 3 cases grid | BMW / TSMC / Boeing — кейсы запоминаются + эталонная разметка раскрыта в notes. |
| s15 Boeing 737 door-plug | да — strong | excellent | photo + анти-кейс с разбором | «CV — последняя линия защиты» формула — запоминается. |
| s16 label cost | да | excellent | asymmetric chart | Cornerstone (стоимость разметки) ясен из bullets + notes. |
| s17 PdM + OEE callback | **да — strong** | excellent | vendor vs reality split + OEE formula | Формула «–25% downtime ≠ +25% OEE» — запоминается, OEE-вопрос явно сформулирован. |
| s18 коботы + Jidoka | да | excellent | 3 cases + Toyota quote | augment-vs-replace ясен. |
| s19 Tesla 2018 deep-dive | да — strong | excellent | timeline + цитата + Bainbridge | Canonical case проходит retention test. |
| s20 CV limits + alternatives | да | excellent | limits + alternatives 2-col | Структурированный свет / X-ray / rules — альтернативы прозрачны. |
| s21 Foxconn 80% claim | да — strong | excellent | claim + 3 вопроса | Vendor-questions для кармана сформулированы. |
| s22 discrete failure matrix | да | excellent | 2×2 matrix | 4 типа провалов retainable. |
| s23 §3 divider | да | good | section break | ok |
| s24 soft sensors BASF + Pfizer | да — strong | excellent | 2 case grids + soft-sensor definition | Pfizer Vox introduced; forward-link к §4 ясен. |
| s25 MPC/RL/CIRL | **частично** | dense но хорошее | CIRL diagram + 3 panels | Technical depth высокая; через 2 нед могу пересказать main point («RL расширяет PID, не замещает») но детали FKDPP теряются. Для self-study OK. |
| s26 RL distribution drift | да | excellent | 4 mechanisms | Все четыре механизма drift читаемые. |
| s27 edge AI + детерминизм | да — strong | excellent | latency bars + POSCO/Holcim | Cornerstone «latency = determinism» формула. |
| s28 regulatory blockers | да | excellent | 3 regs grid | FDA / ATEX / Указ 250 — все три карты ясны. |
| s29 Russian context | да | excellent | 3 cases + caveat | Анти-pattern в reporting объяснён. |
| s30 process failure matrix | да | excellent | 2×2 matrix | Симметричен s22. |
| s31 §4 divider | да | good | section break + «payoff лекции» pointer | ok |
| s32 4 categories | да — strong | excellent | 2×2 grid с критериями + alternatives | Central payoff slide. 11 критериев в 4 категориях читаемо. |
| s33 alternatives matrix | да | excellent | 6×5 table + hybrids | SPC/DOE/MPC/RCM/physics-sim/rules-vision — каждый со своей нишей. |
| s34 Pfizer Vox worked example | да — strong | excellent | 5-column flow + lesson | Framework применён ретроспективно — ясно. |
| s35 5-step framework | да — strong | excellent | 5 cards + 4 questions panel | Карманный инструмент сформулирован. |
| s36 §5 divider | да | good | section break | ok |
| s37 recap + failure-callback | да — strong | excellent | recap two-col + bottom formula | «Завтра вендор обещает –70%...» формула чёткая. |
| s38 Q&A vendor questions | да | excellent | 5 questions + 3 student Q&A | Все 5 вопросов восстанавливаются. |
| s39 closing hero BMW | **частично** | text-dense | hero + bridge text | Hero есть, но **типографика мелкая в PNG**, надо squint. Content sufficient для bridge. |

**Итог:** 34 strong-self-contained, 3 partial (s08 / s25 / s39), 2 standard-self-contained без выпадений.

---

## 3. Cornerstones Recall Test (через 2 недели)

| Cornerstone | Slide | Recall | Comment |
|---|---|---|---|
| Дискретное vs процессное | s05 | да — strong | Keystone слайд + recap s37; формула «две модели, AI входит в обе по-разному» проходит. |
| Прогностическое обслуживание (PdM) + OEE | s17 | да — strong | Формула «–25% downtime ≠ +25% OEE» — pocket recall. |
| Мягкий сенсор | s04 + s24 | да — strong | Определение в glossary + два case-кейса в s24. Soft sensor как input substitute для лабораторной пробы — ясно. |
| Застревание на пилотной стадии | s07 + s37 | да — strong | 95% не доходят / 78% adopt / 5,5% high performers — повторено многократно. |
| OEE | s04 + s17 + s35 | да — strong | Definition + callback + 4-й вопрос к вендору. |
| Эталонная разметка | s14 + s16 | да — strong | Class imbalance + стоимость explicitly раскрыты. |
| OT/IT раскол | s09 | да — strong | Two-column slide + LLM 100-500 ms vs PLC 1-10 ms — pocket formula. |

**Все 7 cornerstones pass retention test через 2 недели.**

---

## 4. Worked Examples + Framework Recall Test

**Pfizer Vox через 5-step framework (s34):** да, могу восстановить ретроспективное application. Step 1 process → Step 2 SPC/DOE/MPC inadequate → Step 3 FDA Part 11 forces recommend-mode → Step 4 baseline + ROI go-criterion → Step 5 HITL audit trail. Strong example.

**Brewery / metallurgy / другие process cases:** в slides v1 нет отдельного brewery-кейса; есть POSCO (hot-rolled steel) на s27 + Holcim (cement kiln) + CEMEX в notes — все три passing examples. Если task brief предполагает «brewery pass» — это либо chapter-only кейс, либо не вошёл в deck. **Этот мисматч с заданием reader-rendered (brewery / avionics) надо обсудить с оркестратором.** В slides v1 «brewery pass» отсутствует, «avionics fail» = F-35 ALIS callback на s27 (lec-09 reference) и Boeing 737 на s15.

**5 шагов framework recall:** 1 identify class → 2 map alternatives → 3 apply 4 categories → 4 pilot с go-criteria → 5 production с HITL + audit trail. Все 5 запоминаются из s35 PNG (5 cards с заголовками).

**4 категории recall:** Данные / Стоимость / Регуляторика / Человек. Из s32 — все 4 категории видны grid'ом. 11 sub-критериев — частично retainable, но из notes можно восстановить.

**5 vendor questions recall:** s38 explicit: (1) baseline до AI / (2) окно измерения / (3) перечень вмешательств / (4) OEE-канал / (5) архитектурный класс. Формула «на стикер на монитор» в notes — pedagogical anchor.

---

## 5. Structural Blockers (notes-fix vs structural cut)

**Из 5 partial-self-contained slides:**

- **s08 market estimates** — **notes-fix (cosmetic)**: ребренд / удалить «[VFY-day-of]» token из visible footnote. Это designer-extras leak, P1. Content valid, надо чистить PNG.
- **s25 MPC/RL/CIRL** — **notes-already-fix**: notes уже dense и хорошие. Slide сам — самый technical в deck. Альтернативы: либо разбить на 2 slides (s25a Yokogawa + s25b CIRL), либо оставить как есть с пометкой «advanced — для self-study consult chapter §3.2». Я бы оставил, не cut. Студент через 2 нед, читая notes, получит главную мысль (RL расширяет PID, не замещает).
- **s39 closing hero** — **typography-fix**: текст на PNG мелкий, надо увеличить «Сшивка инструментов в production-fabric» + сократить bullet list. Hero photo нормальный (BMW Group plant), bridge к Лек-12 явный. Это **layout polish, не structural cut**.

**Нет slides под structural cut.** Все 39 contribute к narrative arc.

---

## 6. Deep Latin-Token Scan на 5 random sampled speaker notes

**Sampled:** s01 / s09 / s17 / s28 / s35.

**Whitelist (acceptable):** Tesla, Foxconn, BMW, BASF, Pfizer, FDA, ATEX, GAMP, OEE, MES, SCADA, PLC, MPC, RL, CIRL, PID, FKDPP, GE, IBM, Predix, AWS, Bedrock, SageMaker, mRNA, ISA-95, SIL, ISO, NVIDIA, Holcim, POSCO, Optimitive, JSR, Yokogawa, Hyundai, Boston Dynamics, Atlas, Spot, GAIA, Toyota, Bainbridge, FZ-152, FAA, IMD, RAND, McKinsey, Deloitte, Gartner, MIT Sloan, CBS, Wired, R&D, ML, AI, KPI, ROI, EBIT, QC, OEM, PoC, KII (КИИ), HMGMA, AIQX, FKDPP, ODIN, ALIS, Computex.

**Findings:**

- **s01:** «production hell» (industry term, acceptable), no leaks beyond brand names.
- **s09:** «eventually-consistent», «strong consistency», «structural divide» — все три это technical terms, для которых нет русского эквивалента в OT/IT-контексте. Acceptable, но один inline gloss («eventually-consistent — модель «возможно, переспросим через секунду»») в notes есть — good. **0 narrative anglicisms.**
- **s17:** «baseline», «window measurement», «best case», «average» — все встречаются в RU narrative. «Baseline» технически industry term для vendor-claims context; gloss («на какой объём работы вы сравниваете») присутствует. **0 narrative anglicisms beyond accepted.**
- **s28:** «traceable changes», «validated systems», «audit trail», «final decision-maker», «HITL», «recommend mode», «autonomous batch release» — это всё FDA / GAMP официальная терминология, для которой русские переводы не используются в индустрии. Acceptable. **0 leaks.**
- **s35:** «pocket framework», «hybrid patterns», «PINN», «edge ML coprocessor» — acceptable technical terms. «Identify class», «map alternatives», «apply categories», «pilot with go-criteria», «production with HITL» — это framework step-names — acceptable как technical labels. **0 narrative anglicisms.**

**Verdict deep latin scan:** notes clean. Single P1 leak — на PNG s08 «[VFY-day-of]» — scaffold-token, надо удалить, не anglicism.

**Vocabulary check:** все ключевые termы (vector DB не используется, RAG не используется в этой лекции; soft sensor / edge / PdM / OEE / MPC / RL / CIRL / SPC / DOE / RCM / FDA Part 11 / ATEX / Указ 250) имеют inline gloss либо в s04 glossary, либо при первом упоминании на content-slide. **0 unmarked-vocabulary issues.**

---

## 7. Recommendations for Phase 8

**P1 (must-fix перед GATE B):**

1. **s08:** удалить «[VFY-day-of]» из visible footnote — это designer-extras leak (memory rule «No Extra Content Rule»). Frontmatter-only.
2. **s39 hero:** увеличить шрифт title + bullets, либо сократить bullet list (сейчас текст squint-fine). Hero photo сам ok.

**P2 (polish — после GATE B):**

3. **s25 MPC/RL/CIRL** — рассмотреть split на 2 slides ИЛИ оставить с пометкой «advanced — для self-study consult chapter §3.2 для FKDPP detail».
4. **s24 PNG looks crowded** — text-dense. Consider squeezing soft-sensor definition. Optional.
5. **s35 5-step framework** — отлично подаётся, но «Pilot + go-criteria» card очень dense. Optional polish: переместить «baseline + measure window + go/no-go threshold ДО старта» в bottom callout, освободить card.

**P3 (low priority):**

6. Speaker notes на s10 / s17 / s28 — самые длинные (400+ слов), close к upper bound 300-слов-norm. Студент-read OK, но trim 10% для tighter recall не помешает.
7. Bridge между s05 (keystone) и s06 (§1 divider) — в s06 notes явно сказать, что s05 цель достигнута. Сейчас читается чистым повтором.

**Vocabulary maintenance:** keep current — все термы glossed inline. No additions needed.

---

## Сводка

- **Self-contained slides:** 34/39 = **87%** (выше production threshold 85% + лучше Лек-1 v3 82%).
- **Slides under partial-self-contained:** 3 (s08 designer-leak / s25 technical density / s39 typography).
- **Slides needing structural cut:** 0.
- **P0 issues:** 0.
- **P1 issues:** 2 (s08 scaffold leak; s39 typography).
- **P2 polish:** 3-4.
- **Cornerstones retention:** 7/7 pass через 2 недели.
- **Worked example retention:** Pfizer Vox через 5 шагов — pass; brewery / avionics в slides v1 = absent / mapped to F-35+Boeing (см. §4 mismatch note для оркестратора).
- **5-step framework recall:** pass.
- **4 категории recall:** pass.
- **5 vendor questions recall:** pass.
- **Deep latin scan на 5 sampled notes:** 0 narrative anglicisms. Single P1 на PNG s08 = scaffold leak, не anglicism.
- **Vocabulary check:** 0 unmarked terms. Glossary s04 + inline gloss cover everything.

**Verdict (mode=rendered, threshold-based):** 34/39 = 87% ≥ 30/39 и ≥ 85% threshold → **APPROVE-CLEAN** с 2 P1 fixes перед GATE B (s08 token leak + s39 typography). Deck v1 — production-ready для self-study с минимальным polish.

**Top-3 правки speaker notes:** none required structurally; notes already strong. Polish — trim 10% длины на s10 / s17 / s28 для tighter retention.

**Top-3 правки на PNG:** (1) s08 убрать «[VFY-day-of]» из visible footnote; (2) s39 увеличить typography hero text; (3) s24 sigh «Pfizer Vox» card text density.

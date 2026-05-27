# Methodology critique — speech v1 Лекция 16 «AI в нефтегазе»

**Verdict:** REVISE

**Дата:** 2026-05-27
**Object:** `library/lectures/lec-16/speech.md` (7 795 слов, 972 строки, 42 sections + Q&A + preflight, 78.5 мин schedule)
**Counter-check:** ≥5 P1 issues → REVISE (не APPROVE-WITH-POLISH).

## Summary

Speech v1 — методически серьёзный, риторически уравновешенный draft с **сильным выполнением 5 из 12 структурных зон**: keystone-консистентность (79 references, no Q4 drift «Энергопереход»→«Новые опоры» applied cleanly), AI-Failure / judgment share **strict-in 34.4% / loose-strict-in 56.7%** (выше threshold ≥30%), anonymization clean (0 МГТУ / ИУ / Бауман / РГУ Губкина — only false positives на «Сургутнефтегаз»), baseline coverage strong (15 из 17 sampled measurable claims с inline denominators), anti-pattern grep clean (0 hits «магическая пилюля» / «УГАДАЙ» / «инженер ИУ6» / «методически» / «На этом этапе» / «Лектору»).

Однако **6 P1 issues** требуют фикса перед Phase 11 финализацией:

1. **WPM hard rule violation на 25 из 42 sections (60%)** — speech-writer DoD требует ≤95 WPM per fragment; **25 sections превышают, 12 >110 WPM, 5 >130 WPM** (s17/s18/s23/s33/s20). s33 «177 WPM» абсолютный rekord — невозможно произнести naturally за 1 минуту. Это **single DoD metric fail → REVISE**.
2. **Word budget overshoot 18% над target** — 7 795 vs 5 500-6 500 target (frontmatter `length_words_target`). Корреляция с пунктом 1: излишние слова сжимают into минутный slot.
3. **Total schedule 78.5 min vs 75 min budget** — overshoot 4.7%. С учётом, что 10 min Q&A явно зарезервирован, активный время **68.5 min vs 65 min plan v2** = 5.4% over. Не катастрофа, но без Q&A buffer compression.
4. **Preflight checklist (10 items) внутри speech.md** — это **planning artifact**, не часть финального speech. Per CLAUDE.md "No Extra Content Rule" — preflight items должны быть в `iteration-log.md` / `notes/`, не в speech.md visible body. Также 1 anti-pattern hit «революция» (хоть и в `Watson выиграл Jeopardy 2011`-контексте — false positive).
5. **Russification depth — 717 unmatched Latin tokens над brand allowlist** — после whitelist 927→717 unique (1948→большая часть occurrences). Top tokens: `data` (19), `model` (11), `gap` (10), `plant-wide` (9), `oil` (8), `slide` (8), `augmentation` (7), `Digital Field` (7), `vs` (7), `ground` (7), `cost` (7), `working` (5), `cases` (5), `divider` (5), `Industry` (5), `training` (5), `Safety` (5), `aerial` (5), `scale-up` (5), `risk` (5), `crash` (5), `Industry` / `industry` mix, `stagnation` (4), `injection` (4), `regulatory` / `Regulatory` (4 / 4), `compute` (3), `workable` (3), `cornerstone` (4), `keystone-` (3), `gas` (3), `value` (6), `loss` (4), `mandatory` (4). Это **deep latin scan failure** — narrative anglicism creep, не brand mentions.
6. **Q&A starter prompts (s42) — 3 заданы, но WPM 36 (356 words / 10 min)** — слишком много speech text для 10 min где expected student talk; либо trim prompts, либо явно label «backup if no questions».

P2 (3 issues): inline preflight (item 4 above ≥ P1 actually); 14 questions (рит. — sample), некоторые grammar-loose, не natural; transition markers «давайте» (только 2 — мало, чувствуется монологичность).

**Counter-check 4-level scale:** 6 P1 issues ≥ 5 + 1 DoD hard-rule fail (WPM) → **REVISE**, не APPROVE-WITH-POLISH.

## Per-area assessment (12 zones)

### Зона 1 · Conversational vs academic style — PARTIAL

**Strengths:**
- 14 questions (риторические + content-prompting), good distribution (s06 «почему именно в Q1», s17 «Что вы делаете с этим», s18 «какие specialized training data?»).
- 24 [пауза] + 30 [акцент] + 7 [медленнее] + 2 [смотрит в зал] stage directions — sufficient pacing layer.
- 36 [переход к sNN] markers — каждый section имеет explicit transition.
- 11 transition markers («вернёмся», «давайте», «поехали») — present но not abundant.
- 30 «мы / нас / наш» (inclusive) + 10 «вы / вам» (direct) — соотношение inclusive-heavy, что comfortable для academic delivery.

**Weaknesses:**
- Только 2 «давайте» — это базовый conversational discourse marker для русской лекторской речи. Sample sections (s06, s14) читаются как academic essay, not lecturer's voice. Compare с Lec-12/13/14 patterns где «давайте» применялся 8-12 раз.
- Некоторые transitions list-driven: s09 «Шесть имён, три группы», s11 «Два имени», s24 «Четыре игрока» — академический рубрицированный стиль. Conversational alternative: «А вот ещё один игрок...» / «Третий пример — самый интересный».
- s14, s23 — самые conversational fragments. s38 хороший emotional payoff (Deepwater Horizon). Но между ними длинные «list-of-facts» секции (s24, s27, s33, s36).

**Recommendation:** добавить 5-6 «давайте» / «обратите внимание» / «представьте на минуту» в s09 / s11 / s24 / s27 / s33.

### Зона 2 · Pacing realism — FAIL (P1)

**Per-section WPM (excl. bracketed stage directions):**

| Section | Min | Words | WPM | Status |
|---|---|---|---|---|
| s01 | 2.0 | 123 | 62 | OK |
| s02 | 1.0 | 108 | 108 | ⚠️ over |
| s03 | 1.0 | 147 | 147 | ⚠️ HIGH |
| s04 | 3.0 | 308 | 103 | ⚠️ over |
| s05 | 0.5 | 31 | 62 | OK |
| s06 | 2.0 | 216 | 108 | ⚠️ over |
| s07 | 2.0 | 218 | 109 | ⚠️ over |
| s08 | 2.0 | 192 | 96 | ⚠️ near |
| s09 | 2.0 | 149 | 74 | OK |
| s10 | 2.0 | 127 | 64 | OK |
| s11 | 1.0 | 106 | 106 | ⚠️ over |
| s12 | 1.0 | 141 | 141 | ⚠️ HIGH |
| s13 | 0.5 | 34 | 68 | OK |
| s14 | 3.0 | 194 | 65 | OK |
| s15 | 2.0 | 149 | 74 | OK |
| s16 | 2.0 | 148 | 74 | OK |
| s17 | 2.0 | 245 | 122 | ⚠️ HIGH |
| s18 | 2.0 | 270 | 135 | ⚠️ HIGH |
| s19 | 2.0 | 226 | 113 | ⚠️ HIGH |
| s20 | 1.0 | 141 | 141 | ⚠️ HIGH |
| s21 | 0.5 | 30 | 60 | OK |
| s22 | 2.0 | 146 | 73 | OK |
| s23 | 2.0 | 259 | 130 | ⚠️ HIGH |
| s24 | 2.0 | 175 | 88 | near |
| s25 | 2.0 | 204 | 102 | ⚠️ over |
| s26 | 2.0 | 180 | 90 | near |
| s27 | 2.0 | 187 | 94 | borderline |
| s28 | 0.5 | 44 | 88 | near |
| s29 | 2.0 | 219 | 110 | ⚠️ over |
| s30 | 2.0 | 236 | 118 | ⚠️ HIGH |
| s31 | 2.0 | 214 | 107 | ⚠️ over |
| s32 | 2.0 | 203 | 102 | ⚠️ over |
| s33 | 1.0 | 177 | **177** | 🛑 EXTREME |
| s34 | 1.0 | 120 | 120 | ⚠️ HIGH |
| s35 | 2.0 | 224 | 112 | ⚠️ HIGH |
| s36 | 2.0 | 190 | 95 | borderline |
| s37 | 2.0 | 203 | 102 | ⚠️ over |
| s38 | 2.0 | 237 | 118 | ⚠️ HIGH |
| s39 | 1.5 | 181 | 121 | ⚠️ HIGH |
| s40 | 1.0 | 117 | 117 | ⚠️ HIGH |
| s41 | 1.0 | 121 | 121 | ⚠️ HIGH |
| s42 | 10.0 | 356 | 36 | OK (Q&A) |

**Counts:**
- 25 sections > 95 WPM (60% sections fail brief cap)
- 12 sections > 110 WPM
- **5 sections > 130 WPM:** s17 (135), s18 (135), s23 (130), s33 (**177**), s20 (141)
- s33 «1 min / 177 WPM» — невозможно произнести naturally; либо bump до 1.5 min, либо cut 60 слов.

**Schedule math:**
- Sum of section budgets: 2+1+1+3+0.5+2+2+2+2+2+1+1+0.5+3+2+2+2+2+2+1+0.5+2+2+2+2+2+2+0.5+2+2+2+2+1+1+2+2+2+2+1.5+1+1+10 = **78.5 min**.
- Active (excl. s42 Q&A) = 68.5 min.
- Plan v2 budget = 65 active + 10 Q&A = 75 total.
- **Overshoot: +3.5 min total (+4.7%), +3.5 min active (+5.4%).**

**Recommendation:** **trim 800-1000 слов из speech**, focal on s17/s18/s23/s33 (5 highest WPM). Target ≤95 WPM per fragment + 75 min total.

### Зона 3 · AI-Failure & Judgment share — PASS

**Strict-in measurement (полностью in-bucket sections только):**
- Strict-in (failure case + lesson / hard limit / "AI not needed" criterion / alternative-as-baseline): **15 sections, 27.0 min = 34.4%**
- Partial (caveat-as-judgment, anti-hype, scale-gap noted): 10 sections, 20.5 min = 26.1%
- Out (working case description, divider, recap, Q&A): 17 sections, 31 min = 39.5%

**Strict-in sections:** s06 (86% pilot stuck), s07 (Aspen alert fatigue), s11 (Cognite/C3.ai shrinkage), s12 (6 criteria когда AI не нужен), s17 (BP+Beyond Limits), s18 (IBM+Repsol Watson), s19 (Eclipse/INTERSECT alternative), s23 (MethaneSAT loss), s25 (фактор 4 conflict), s27 (OGI+Picarro alternative), s31 (CCS 190× gap + hallucination), s32 (refinery plant-wide stagnation), s33 (SIS+APC alternative), s37 (cyber +935%), s38 (2020 crash + Deepwater Horizon).

**Distribution holistic:** Q1=4, Q3=3, Q2=3, Q4=3, cross-cutting=2 — **NO single-cluster concentration**.

Plan v2 self-estimate 39% подтверждается independent measurement 34.4% strict-in. Threshold ≥30% holistic — **PASS with +4.4pp safety margin**.

Frontmatter `strict_in_failures_self_estimate: "~39% активного времени"` — близко к моей 34.4% strict-in / 56.7% looser-bucket reading.

### Зона 4 · Keystone axis consistency — PASS

- 79 keystone references (matrix / квадрант / Q1-Q4) across speech.
- s04 keystone slide content вводит ось дидактически clean: «доступность данных» + «определённость процессов» с конкретными примерами (Permian vs Angola; Eclipse vs methane fusion).
- Возврат к keystone в s14 (Q3 frame), s22 (Q2), s29 (Q4), s39 (synthesis 4×4), s41 (cornerstone closing).
- s40 + s41 unified closing message: «10 разобранных провалов → 3 переносимых cornerstone оси» — соответствует s41 slide single_message.
- Каждая section имеет attribution к keystone quadrant; нет "orphan" cases.

**Pass.**

### Зона 5 · Q4 «Новые опоры» terminology — PASS

- «Энергопереход» в speech: **0 hits**.
- «Новые опоры»: 3 hits (s04 + s28 + s39).
- «новые опоры» (lowercase): 2 hits (consistency check).
- s28 divider содержит явно «**Q4 divider — новые опоры (CCS + EGS)**».
- s04 keystone: «**Q4 — слева снизу. Новые опоры — улавливание углерода и улучшенные геотермальные системы.**».

Cascade from chapter+slides clean — terminology fully aligned.

**Pass.**

### Зона 6 · Cornerstone closing alignment — PASS

- s40 speech: «**3 cornerstone концепта для Лекции 17**» с тремя explicit названиями matching s40 slide content.
- s41 speech: «**10 разобранных провалов → 3 переносимых cornerstone оси**» — exact match с s41 slide `assertion`.
- Hero MethaneSAT карта context («февраль 2026 EDF + Google опубликовали первую глобальную карту») matches s41 slide visual description.
- Bridge к Лекции 17 объяснён («systematization» / «переносимые на любую отрасль»).

**Pass.**

### Зона 7 · Baseline / counterfactual coverage — PASS (sample 17/17 with 2 weak)

| Claim | Baseline / counterfactual? | Status |
|---|---|---|
| $1.8B Aramco AI value | / $436.6B revenue = 0.41% | ✓ |
| 88M MethaneSAT | / 15.5 month lifetime = $5.7M/mo realized vs $1.5M planned | ✓ |
| 107k jobs / 9.7% industry | / total US O&G ~1.1M | ✓ |
| 5.9% Bashneft +1 Mt | / 17 Mt baseline | ✓ |
| 0.02% Northern Lights | / 7.6 Gt IEA target | ✓ |
| 190× scale-up gap | / 40 Mt current to 7.6 Gt | ✓ |
| 0.2% Fervo | / 200+ GW IEA target; 40× ceiling | ✓ |
| +15% Ambyint | / per-well historical mean baseline | ✓ |
| +935% cyber | Zscaler year-over-year RELATIVE; absolute не disclosed (acknowledged) | ✓ |
| 4× MethaneSAT vs EPA | with Stanford 2× counter-baseline | ✓ |
| Honeywell UOP 310 units | / ~14% мировой нефтепереработки | ✓ |
| 1700+ Cognitive Pilot installs | **? no denominator** — claim что 720k tonnes на 160k ha = 0.6% Russian output, но 1700+ units не нормализовано | ⚠ partial |
| $4.4M Colonial ransom | + $200M+ recovery context | ✓ |
| $60B Deepwater | / 20% годовой выручки BP | ✓ |
| 4.9M barrels Deepwater | total US Q3 production не дан, но baseline industrial scale clear | ✓ |
| s14 4× compute Discovery 6 | 4× compute throughput ≠ 4× реальной ценности explicit anti-hype callout | ✓ |
| 6 Mt aerial Stanford | / EPA 4 Mt = 1.5× factor | ✓ |

**Weak claim:** Cognitive Pilot 1700+ deployments без denominator total combine count в РФ (chapter §6 says ~130k combines в РФ → ~1.3% penetration). Speech could borrow that math.

**Recommendation:** add 1 sentence к s36: «1700 из ~130 тысяч комбайнов в РФ — около 1,3%».

### Зона 8 · Russification deep scan — FAIL (P1)

**Counts:**
- Unique latin tokens: 927
- After brand/acronym whitelist (175+ entries): 717 unmatched non-brand tokens (1948 → большая часть occurrences остаются)

**Top 30 unmatched (narrative anglicism creep, не brand names):**
```
data (19), model (11), gap (10), plant-wide (9), oil (8), slide (8),
augmentation (7), Digital (7), vs (7), ground (7), cost (7), value (6),
foundation (6), https (6), working (5), cases (5), divider (5),
Industry (5), training (5), Safety (5), primary (5), aerial (5),
scale (5), scale-up (5), risk (5), Geo (5), crash (5), www (5),
loss (4), mission (4), source (4), mandatory (4), pilots (4),
capture (4), clean (4), injection (4), cornerstone (4), Working (4),
Failures (4), Regulatory / regulatory (4 + 4), operational (4),
exploration (4), stagnation (4), Level (4)
```

**Categorization:**
- **Tech jargon ≠ brand** (must Russify): `data`, `model`, `gap`, `working cases`, `divider`, `training`, `mandatory`, `primary`, `cost`, `value`, `working`, `cases`, `risk`, `clean`, `source`, `loss`, `mission`, `primary`, `aerial`, `injection`, `capture`, `working pilots`, `Failures`, `Regulatory`, `operational`, `exploration`, `stagnation`, `Level`, `pilots`, `cornerstone` (last is keyword, but Russify к «опорный концепт»).
- **Compound English** (specifically violates Russification): `plant-wide` (9 hits!), `scale-up` (5), `Digital Field` (7), `Cognitive Geo` (5), `working cases`, `clean energy`, `single point of failure`, `out-of-distribution`, `flat OT/IT network`, `safety case`.
- **Genuinely should stay as-is:** brand names (Aramco, Honeywell, Exxon, Газпром нефть OK Cyrillic, Roxar, Yokogawa, ExxonMobil); acronyms (HPC, OGI, LDAR, MRV, OGMP, SIL, SIS, BOP, CCS, EGS, NGO, NOC, JV, IPO, ARR, ROI, R&D, CapEx, KPI); product names (METABRAIN, InfinityRL, Discovery 6, HPC6, Tanager-1, Cognitive Geologist, Lumi, Mtell, Eclipse, INTERSECT, OpenFOAM, Picarro, FLIR, Beyond Limits, etc.).

**Sample fix mapping:**
- `plant-wide` → «общезаводской» / «общеустановочный» (chapter уже applied!)
- `scale-up gap` → «разрыв масштабирования»
- `working cases` → «рабочие случаи»  
- `divider` → «раздел» / «разделитель»
- `training data` → «обучающие данные»
- `clean energy` → «чистая энергия»
- `single point of failure` → «единая точка отказа»
- `out-of-distribution` → «вне распределения»
- `single-modality` → «одномодальный»

**Counter-check:** narrow pattern grep на 5 patterns показал бы near-0 hits; deep scan показывает structural anglicism load. Per CLAUDE.md «pattern-narrow grep НЕ достаточен» — это narrow gap.

**Estimate severity:** ~30-40 высокочастотных tech jargon tokens (data, model, gap, cost, value, working, training, primary, etc. × 4-19 occurrences each) — это **moderate** anglicism creep, не катастрофа уровня Lec-8 (919 в speech). Но **fail deep latin scan check** в CLAUDE.md §Russification.

**Recommendation:** **single revision pass** с broad RU-replace lookup table; estimate 1-1.5h. **P1.**

### Зона 9 · Anonymization — PASS

- МГТУ: 0
- Бауман: 0
- ИУ-N: 0
- Кафедра: 0
- РГУ Губкина: 0 (2 «ргу» hits — false positives внутри «Сургутнефтегаз»)
- «инженер ИУ6» / «студент Бауманки»: 0

Universal RU-audience tone preserved. **Pass.**

### Зона 10 · Rhetorical quality — APPROVE-WITH-POLISH

**Sample 5 transitions между sections:**
- s04→s05: «**Запомним эту матрицу.** К ней мы будем возвращаться каждые 8-10 минут. [переход к s05]» — strong (anchor + intentional rhythm).
- s07→s08: «Что мы с вами выносим. ... запомните эту формулировку — мы вернёмся к ней в самом конце, когда будем говорить про Deepwater Horizon. [переход к s08]» — **excellent** (foreshadow!).
- s12→s13: «Это **диагностический инструмент** на первой работе. ... Кейс попадает в один из шести — **отказать AI**, назвать альтернативу. [переход к s13]» — strong (закрывает раздел с tool, передаёт следующему).
- s24→s25: «Когда вендор продаёт «AI MRV solution» — спросите: **какие модальности он покрывает?** Single-modality «AI MRV» — **маркетинговая фраза**. [переход к s25]» — strong (urgent imperative).
- s38→s39: «**Alert fatigue REAL.** «Zero false positives» — маркетинг. **Safety culture сильнее technology sophistication.** [переход к s39]» — strong (callback to s07!).

**Sample 5 риторических вопросов:**
- s06: «**Почему именно в Q1**, где у нас всё хорошо — данных много, физика известна, опытные операторы — почему именно здесь 86% пилотов проваливаются?» — **engaging, не forced**.
- s17: «Что вы делаете с этим. Не "никогда не покупайте у вендора". А **читайте риск концентрации**.» — direct, useful.
- s18: «Когда кто-то приходит с "foundation model для нефтегаза" — спросите: какие specialized training data? какая architecture? какие бизнес-результаты в pilot?» — **excellent** (actionable script).
- s19: «Когда AI в frontier exploration буксует — что используют вместо?» — content-prompting, leads к answer.
- s31: «Критический вопрос: где будет облако через 50, 100, 500 лет?» — vivid, deep-time framing.

**Sample 5 аналогии:**
- s04: «Полпроцента. Не "AI спасает нефтянку". Полпроцента на огромной, уже оптимизированной операции.» — vivid contrast.
- s07: «**Тот же IBM, та же эпоха, та же "cognitive computing" упаковка. Два manifestations одной структурной ошибки** IBM в подходе к vertical AI.» — strong (parallel).
- s08: «Но мы с вами держим масштаб. 200 скважин — **малый флот** на фоне рынка. ExxonMobil после слияния с Pioneer объединил **16 миллиардов баррелей**.» — explicit scale framing.
- s23: «**MethaneSAT работал отлично 15,5 месяцев. Не "технология провалилась" — "спутник в космосе имеет конечную надёжность".**» — emotional + technical.
- s38: «**Junior operator с simple system лучше senior с complex AI.** Complex AI требует **более** sophisticated training.» — counter-intuitive twist.

**Strengths:** transitions consistently strong, не «следующий слайд — X». Foreshadow patterns (s07→s38, Aspen→Deepwater) excellent. Closing s41 emotional payoff («Спутник потерян, но карта осталась») clean.

**Weaknesses:** только 2 «давайте» (см. зона 1); could be 5-6 для естественности.

### Зона 11 · Q&A buffer (s42) — PARTIAL

**s42 contents:**
- 3 starter prompts present: «Можно ли применить foundation model к новому frontier basin?», «Если 86% застряли — почему инвестируют?», «Что мешает AI заменить BOP?».
- 356 words / 10 min = 36 WPM — adequate (expects student talk).
- Backup ссылка к chapter §8: **отсутствует** в s42 speech body. Plan v2 §6 mentioned «Q&A backup chapter §8» — НЕ передан в speech.
- Preflight item #10 («Принести printed copy chapter §8 Q&A backup (12 вопросов)») — **в preflight, не в Q&A speech**. OK as preflight, но не visible cue for лектор during delivery.

**Recommendation:** добавить 1 строку в s42: «*Дополнительные вопросы — см. chapter.md §8 (12 questions backup)*».

### Зона 12 · Consistency с chapter — PASS

Sample 5 claims cross-check:
- **1.8B Aramco**: chapter-part5 «Aramco самостоятельно отчитывается $1,8B realized 2024 на ~$3,5B годового R&D — то есть ~51% возврата R&D за один год»; speech s14: «1,8 миллиарда realized = **51% R&D-бюджета за один год**». ✓ exact match.
- **MethaneSAT loss 15.5 mo**: chapter-part4 «MethaneSAT loss июнь 2025 (~15,5 месяцев из 5+ лет)»; speech s23: «**15,5 месяцев** после запуска. **26%** от пятилетней проектной миссии». ✓ exact.
- **107k jobs / 9.7%**: chapter-part4 «107 000 рабочих мест ... ~9,7% индустрии за 6 месяцев»; speech s38: «107 тысяч рабочих мест в US O&G за 6 месяцев — 9,7% индустрии». ✓ exact.
- **Ambyint +15% / 200 wells**: chapter §1.2 / speech s08: identical numbers, identical baseline (per-well historical mean).
- **Fervo IPO 12 May 2026 / $1.89B / $7.7B**: chapter-part5 references match speech s30 exactly.

**Pass.** No claim drift between speech v1 and chapter v2.1.

## P0 issues (BLOCKING)

**None.** Все ENFORCED-правила курса в speech v1 acknowledged: strict-in failures ≥30% holistic distribution; keystone предъявлен и поддержан 79× references; anonymization clean; baseline coverage strong; anti-pattern grep clean; chapter cross-consistency exact.

## P1 issues (HIGH — fix before Phase 11 cascade)

### P1-1. **WPM hard rule violation (DoD metric fail) — 25/42 sections > 95 WPM, s33 = 177 WPM**

**Severity:** DoD metric fail → REVISE.

**Evidence:** см. таблицу зона 2. 5 sections > 130 WPM (s17 122, s18 135, s23 130, s33 **177**, s20 141). s33 «SIS + APC + 3 criteria когда AI не нужен в Q4» сжат в 1 minute на 177 слов — невозможно произнести naturally.

**Recommendation:** trim 800-1000 слов общесреднее, focal redistribution:
- s33 — bump до 1.5 min ИЛИ cut 60 слов (3 criteria сжать в 2-3 строки).
- s17 / s18 / s23 — cut по 50-80 слов из каждой (preserve lesson structure, trim context paragraphs).
- s20 (alphabet 141 WPM 1 min) — bump до 1.5 min ИЛИ оставить только 4 термина (MRV, OGI, LDAR, SIS) + speak others по контексту.
- s12 (141 WPM 1 min) — bump до 1.5 min ИЛИ cut 30 слов (preserve 6 criteria, trim explanations).
- s39 (121 WPM 1.5 min) — synthesis recap трудно cut; bump до 2 min либо trim 4 quadrant recap до 2 строк/quadrant.

### P1-2. **Word budget overshoot 18% — 7 795 vs 5 500-6 500 target**

**Severity:** P1.

**Evidence:** frontmatter `length_words_target: 5500-6500`; actual 7 795 (preflight 10 items excluded, ~250 words → 7 545 net narrative).

**Recommendation:** cumulative с P1-1: trim 1000-1500 words к ~6 300. Target each section's WPM ≤95.

### P1-3. **Total schedule 78.5 min vs 75 min — 5% overshoot, eats Q&A buffer**

**Severity:** P1.

**Evidence:** Schedule sum = 78.5 min. Plan v2 budget = 65 active + 10 Q&A = 75. Active overshoot = 3.5 min — eats into Q&A.

**Recommendation:** cascade с P1-1 — trim 800-1000 words. Either:
- Trim 3.5 min from active (preferred — preserve full Q&A).
- ИЛИ acknowledge as "75-80 min show" в frontmatter (less preferred).

### P1-4. **Preflight checklist (10 items, ~250 words) внутри speech.md**

**Severity:** P1 (Designer-extras / No Extra Content rule).

**Evidence:** Lines 961-972: «Подготовка перед лекцией — preflight checklist».

CLAUDE.md «No Extra Content Rule»: speech body — то, что лектор произносит. Preflight = `iteration-log.md` / `notes/lecture-16-review/preflight.md`.

**Recommendation:** MOVE preflight checklist в `iteration-log.md` ИЛИ `notes/lecture-16-review/2026-05-27-phase10-speech/preflight.md`. Speech.md ends на s42 Q&A.

### P1-5. **Russification deep scan — 717 unmatched Latin tokens, narrative anglicism creep**

**Severity:** P1.

**Evidence:** см. зона 8. Top tokens: `data`, `model`, `gap`, `plant-wide`, `working cases`, `divider`, `cost`, `training`, `risk`, `source`, `value`, etc. Frequency 4-19 each.

**Recommendation:** single broad RU-replace pass. Sample mapping:
- `data` (19) → «данные» (контекстуально «информация / выборка»)
- `model` (11) → «модель» (Cyrillic, already RU loan word — OK)
- `gap` (10) → «разрыв» / «провал»
- `plant-wide` (9) → «общезаводской»
- `working cases` (5+4=9) → «рабочие случаи»
- `oil` (8) → «нефть» (в большинстве occurrences keep brand context)
- `slide` (8) → «слайд» (RU OK already)
- `augmentation` (7) → «дополнение» / «надстройка»
- `Digital Field` (7) → «Цифровое месторождение» (chapter uses RU)
- `divider` (5) → «раздел» / «разделитель»
- `training` (5) → «обучение»
- `cost` (7) → «затраты» / «стоимость»
- `cornerstone` (4) → «опорный концепт» / «несущая ось»
- `source` (4) → «источник»
- `risk` (5) → «риск» (Cyrillic OK)
- `value` (6) → «стоимость» / «ценность»

Estimate: ~30-40 high-frequency tokens × replace ≈ 1-1.5h targeted edit.

### P1-6. **Q&A backup chapter §8 reference missing in s42**

**Severity:** P1 (small but consequence: lecturer без printed backup может drift).

**Evidence:** s42 speech body lines 943-957: 3 starter prompts present, но нет «backup chapter §8» line. Plan v2 §6 mentioned. Preflight item #10 (Принести printed copy chapter §8 — 12 questions backup) — backup есть, но visible cue в speech отсутствует.

**Recommendation:** добавить в s42 строку: «*Для расширенного Q&A — см. chapter.md §8 (12 backup questions)*» before «Какие у вас вопросы?».

## P2 issues (minor)

### P2-1. **Только 2 «давайте» transition markers**

Conversational discourse marker «давайте» применён 2× (vs Lec-12/13/14 patterns 8-12×). Speech reads slightly monologic. Sample sections s09 / s11 / s24 / s27 / s33 could benefit.

**Recommendation:** добавить 4-5 «давайте» / «обратите внимание» / «представьте на минуту» equally distributed.

### P2-2. **«революция» 1 hit** — Watson Jeopardy context

s18: «Параллельный сюжет — **Watson Health**. Объявлен как **революция в онкологии**.»

Контекст — IBM marketing claim, не speech promotional voice. Это **false-positive грубо** но technically anti-pattern hit. Можно перефразировать: «**Объявлен как прорыв в онкологии**» / «**Объявлен как прорыв десятилетия**».

### P2-3. **1700+ Cognitive Pilot deployments без denominator**

s36: «1700+ установок в 2024.» Chapter §6 has «~130k комбайнов в РФ» → ~1.3% penetration. Speech could borrow this baseline.

**Recommendation:** «1700+ установок (около 1,3% от ~130 тысяч комбайнов в РФ)».

## Counter-check

| Metric | Target | Actual | Status |
|---|---|---|---|
| Word count | 5 500–6 500 | 7 795 (or 7 545 net w/o preflight) | ⚠️ FAIL +18% |
| Schedule | 75 min | 78.5 min | ⚠️ FAIL +4.7% |
| WPM ≤ 95 per fragment (DoD hard rule) | 0 fragments > 95 | **25 of 42 > 95**; **5 > 130**; **s33 = 177** | 🛑 FAIL |
| Failure-share strict-in | ≥ 30% | 34.4% strict + 26.1% partial | ✓ PASS |
| Failure-share holistic | distributed across artifact | Q1=4, Q3=3, Q2=3, Q4=3, cross=2 | ✓ PASS |
| Keystone consistency | references throughout | 79 references; no «Энергопереход» drift | ✓ PASS |
| Russification | deep scan unique - whitelist ≈ 0 | 717 unmatched (anglicism creep ~30-40 high-freq tokens) | ⚠️ FAIL P1 |
| Anonymization | 0 МГТУ/Бауман/ИУ | 0 | ✓ PASS |
| Anti-pattern grep | 0 hits «магическая пилюля»/«УГАДАЙ»/«методически» | 0; «революция» 1 hit (false-pos context) | ✓ PASS (with P2) |
| Chapter cross-consistency | claims traceable | 5/5 sampled claims match exactly | ✓ PASS |
| Baseline coverage | each measurable claim has base | 15/17 sampled with base; 2 partial (Cognitive Pilot, ground OGI factor) | ✓ PASS |
| Q&A buffer | 3 starter + chapter §8 backup ref | 3 starter prompts ✓; chapter §8 backup ref missing | ⚠️ minor |

**Verdict:** **REVISE** — 6 P1 issues + 1 DoD hard-rule fail (WPM).

## Топ-5 правок (приоритизированных для Phase 11)

1. **WPM compliance pass** (P1-1, P1-2, P1-3) — single cascading fix: trim 800-1000 слов с focal на s17 / s18 / s23 / s33 / s20 / s12 / s39. Target ≤95 WPM per section. Cascade-fixes schedule overshoot, word budget overshoot, WPM hard rule fail.
2. **Russification deep pass** (P1-5) — broad RU-replace 30-40 high-frequency tech tokens (data, model, gap, plant-wide, working cases, cost, training, divider, etc.).
3. **Preflight checklist relocation** (P1-4) — move 10 items из speech.md в `iteration-log.md` или dedicated `preflight.md`.
4. **s42 Q&A backup reference** (P1-6) — добавить 1 строку «*Для расширенного Q&A — см. chapter.md §8 (12 backup questions)*».
5. **P2 polish:** + 4-5 «давайте» distributed; «революция» → «прорыв» в s18; добавить «1,3% от ~130k комбайнов» в s36.

## Rationale + Recommendation для Phase 11

**REVISE because:**
- DoD hard rule (WPM ≤95 per fragment) — 25/42 = 60% sections fail; s33 = 177 WPM is structurally impossible to deliver naturally. Без fix лектор будет либо rushed либо overflow per section ⇒ overall schedule drift.
- Word budget +18% над target — это **structural overshoot**, не polish; corresponds к WPM violation directly.
- Russification deep scan reveals narrative anglicism creep (30-40 high-freq tech tokens) — **deep scan fail per CLAUDE.md §Russification rule**.

**NOT REJECT because:**
- Methodologically sound: keystone consistent, failure-share strict-in 34.4% ≥30% threshold, baseline coverage strong, anti-pattern grep clean, anonymization clean, chapter cross-consistency exact.
- Rhetorical quality strong: transitions and rhetorical questions natural; emotional payoff Deepwater Horizon → MethaneSAT bittersweet closing well-crafted.
- All fixes are mechanical (trim words, RU-replace lookup, move preflight) — no structural redesign needed.

**Phase 11 plan recommendation:**
- **Single batched revision pass** (speech-writer agent, brief = "trim 800-1000 words + deep RU-replace + preflight move + s42 Q&A line + 4 P2 polish"). NOT separate agents per fix.
- Estimate: 2-3h revision + 30 min orchestrator post-revision verification.
- Re-run WPM check + deep latin scan + word count после revision.
- Phase 11 GATE C — verify revision artifacts before sync to main repo.

**Cost-of-omission if not fixed:**
- Lecturer experiences time-overflow during delivery; sacrifices either Q&A или ключевые failure cases.
- Russian-speaking МГТУ ИУ6 audience reports anglicism-heavy academic feel (Lec-08 precedent: 919 latin tokens deep scan → owner reject «трындец»).
- Without preflight relocation — speech.md is hybrid document (not stage-ready).

**Green-light criterion for Phase 11 → GATE C:**
- 0 sections >100 WPM (95 WPM target with ~5 WPM tolerance).
- Word count 5 500-6 500 net narrative.
- Deep latin scan unique-after-whitelist ≤ ~150 (vs current 717).
- Preflight relocated; s42 has backup chapter §8 reference.

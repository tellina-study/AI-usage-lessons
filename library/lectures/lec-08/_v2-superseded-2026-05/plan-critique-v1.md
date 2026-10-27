# Methodology Critic Report — Lec-08 Plan v1 — 2026-05-20

**VERDICT: APPROVE-WITH-POLISH**

(Counter-check: 4 P1 issues — under the «≥5 → REVISE» threshold. Plan is structurally sound, no P0, no DoD-blocking gap; can move к USER GATE 0 с list of polish items.)

## Severity counts
- **P0:** 0 (методически непригодных gaps нет)
- **P1:** 4 (заметно вредят, нужно адресовать до Phase 2)
- **P2:** 7 (polish)

---

## По 10 ENFORCED-проверкам

### 1. Keystone-axis check (ENFORCED — Лекция 4 lesson) — **PASS**

**Цитата (plan §2, lines 26-35):**
> «AI добавил → изменил → сломал» — три времени единой оси.
> **Keystone-слайд:** s05 (после s01 ice-breaker / s02 cover / s03 central question / s04 lecture-map) в Разделе 0.
> - Заголовок: «AI добавил → изменил → сломал» (про саму ось, не про устройство курса).
> - Первая строка: «Три времени одного процесса — каждое поколение creative-инструментов проходит их за месяцы».

Ось предъявлена ОТДЕЛЬНЫМ слайдом s05 в Разделе 0 ДО первого погружения (Раздел 1 начинается с s06 divider). Заголовок про саму ось, не recap / не защита подхода. Каждый последующий раздел = мотивированный спуск по оси (line 33). Anti-pattern (ловушка Лекции 4) явно отвергнут (line 35). **Чисто.**

**Минор-полировка (P2):** в plan §3 (line 39) написано «для s04 lecture-map + s05 keystone» — central question relates to обоим. Разделение функций: s04 lecture-map = карта/roadmap; s05 keystone = ось трёх времён. Эти 2 слайда могут читаться как дублирующиеся. **Рекомендация:** в Phase 2 chapter / Phase 5 deck явно разграничить: s04 = «вот 6 разделов» (горизонталь карты), s05 = «вот ось 3 времён, по которой раздели на 6» (вертикаль метафоры).

---

### 2. Failure/judgment ≥30% strict-in (ENFORCED, L4-L17 без waiver) — **PASS с caveat**

**Plan §6 claims (lines 164-191):**
- Time: 36/75 = 48% strict-in
- Slides: 18/39 = 46%
- Words: ~5600/10500 = 53%

**Выборочная проверка по Разделу 3 (lines 121-137):** s20-s31 = 12 кейс-слайдов. Каждый описан с конкретным механизмом + выученным уроком («Урок: …» suffix есть у s25, s26, s27, s28, s29, s30, s31 — 7 из 12). Это явно in-bucket по правилу. Раздел 4 (s32-s35) — 4 слайда чек-листа критериев = strict-in. Раздел 5 (s36-s37) — 2 слайда actionable «когда отказаться» = strict-in.

**Caveat (P2):** plan честно отделяет mini-failure-blocks в Разделах 1-2 (s07, s09, s14, s17) от strict-in count (line 170: «считаем как out при подсчёте %»). Это правильное соблюдение strict-in правила (решение #78).

**Minor gap (P2):** s20, s22 (Getty UK loss), s24 (RIAA Suno/Udio) — описание содержит детальный legal mechanism, но **не каждый имеет явное «Урок: …» строку**. Например, s20 описывает taxonomy исков, но не явный урок для инженера. **Рекомендация:** в plan v2 / chapter v1 добавить explicit «Урок:» в каждый из 12 кейс-слайдов Раздела 3 (chapter — детальный урок 2-3 предложения, слайд — 1 фраза в Ocean rounded box).

**Не сконцентрировано в одном артефакте: ✓** (claim 46-53% разброс по 3 артефактам, plan правильно мониторит).

---

### 3. §-named speech-narrative требует слайд (ENFORCED — Лекция 4 lesson) — **PARTIAL / P2**

**Цитата (plan §9 line 244):**
> Lec-3 архитектуры (агент, RAG, API) — Лекция 8 на видимый слой не вытаскивает архитектуру, но в speech упомянуть Sora 2 / Veo 3.1 как API endpoints.

Это потенциальное §-named speech-narrative («Sora 2 / Veo 3.1 как API endpoints») БЕЗ соответствующего слайда. **Не нарушение strict-rule** — это устный bridge к Лекции 3, не §-named часть narrative.

**P2 рекомендация:** в plan v2 явно отметить «owner-обоснование устного якоря (без слайда)» для этого cross-reference, чтобы Phase-5 проверка пропускала корректно. Также проверить — нет ли других неявных §-named narrative bridges (например, в Лекцию 1 framing line 243 — «Lec-1 framing где AI работает / где нет» — также устный mostly).

---

### 4. Tools-per-taxonomy-level (ENFORCED, L4+) — **PASS с caveats P1**

**Plan §4 (lines 47-79):** Все 4 ветки таксономии (кино/видео, музыка/звук, изображения/дизайн, текст/журналистика) имеют:
- **Mode (capability)** — text-to-video, voice cloning, text-to-image, и т.д. (mode ≠ brand) ✓
- **Brands 2026 (named)** — Sora 2, Veo 3.1, Kling 3.0, Suno, ElevenLabs, Midjourney v7/v8, Imagen 4, Flux 2 ✓
- **Adoption-направление словами** — «production use» / «hype demo» / «disputed» / «под давлением исков» ✓
- **Anti-hype** — каждая ветка имеет явный anti-hype блок ✓
- **`[VFY-day-of]`** на volatile facts — есть пометки на версии и benchmark numbers ✓

**P1 issue #1 — таксономия в plan vs central concept оси.** В plan §4 = 4 области (по типу контента), но keystone-ось — 3 времени (добавил/изменил/сломал). Это **две разные таксономии** — концептуальная ось и предметная таксономия. Студенту может быть непонятно: они ортогональны? Cross-product (4×3 = 12 cells)? **Plan не объясняет связь.** Конкретно: Раздел 1 (ДОБАВИЛ) ходит ПО 4 областям, Раздел 2 (ИЗМЕНИЛ) тоже, Раздел 3 (СЛОМАЛ) тоже. То есть основная axis структуры лекции = времена, а 4-областная таксономия — sub-classifier внутри каждого времени. Это работает, но **plan не делает это явно**. **Рекомендация:** добавить мини-параграф в §4 ИЛИ §2: «Эти 4 области — не разделы лекции (разделы = времена оси). 4 области — это способ читать таксономию внутри каждого времени». Без этого студент может запутаться: где «4 области» подаются как раздел и где они «горизонтально проходят» через 3 времени?

**P1 issue #2 — Инфраструктурный слой отделен, но не получает явного слайда.** Plan §4 line 79 правильно отделяет «платформенный слой» (Adobe Firefly Foundry, Hugging Face Spaces) от «уровень-инструмент». Но в slide breakdown (Раздел 1) **нет слайда об инфраструктурном слое**. Платформы упоминаются мельком на s11 (Adobe enterprise logos). **Рекомендация:** либо добавить отдельный mini-слайд про платформы в Разделе 1 (после s11), либо явно отказаться от платформенного слоя как раздела на видимом слое (justified — это L4 lecture не infrastructure lecture).

---

### 5. Lec-N-1 pattern compliance — **PASS с caveats**

**Lec-07 inventory (deck.yaml):** ice-breaker (s01) + cover (s02) + poll (s03/s04 reveal-pair) + central question (s05) + section dividers (s05b/s08a/s13a/s19a/s24a — 5 штук) + Q&A (s29) + closing payoff (s27/s28). Total 29 контентных + 5 dividers = 34.

**Lec-08 plan inventory (plan §5):** s01 ice-breaker live demo ✓, s02 cover ✓, s03 central question (но как отдельный слайд — отличается от Lec-7 где central question = s05 после poll-reveal), s04 lecture-map ✓ (НОВЫЙ pattern — Lec-1 had s02a lecture-map; Lec-7 НЕ имел отдельного lecture-map slide, использовал s05 central question с 4-point roadmap), s05 keystone ✓ (Lec-7 не имел отдельного keystone), s06/s13/s19/s32/s36 dividers (5 штук) ✓, s38 Q&A ✓, s39 closing ✓.

**Несоответствия:**

**P2 — отсутствие poll-reveal pair (как Lec-7 s03/s04).** Lec-7 имел сильный engagement device: «сначала ваша оценка, потом — данные» (reveal-pair). Lec-8 plan не имеет этого pattern, заменяя на live demo s01 (audio/image generation). **Рекомендация:** это допустимо (live demo — тоже engagement), но рассмотреть добавление reveal-pair где-то в Разделе 1-2 (например, «сколько % marketing video AI-generated в 2026?» → reveal 75%). Plan §5.s18 (4-card metric strip) можно превратить в reveal-pair.

**P2 — Lec-8 имеет 6 dividers vs Lec-7 = 5.** Plan имеет Разделы 0/1/2/3/4/5/6 + Q&A = 6 dividers (s06, s13, s19, s32, s36 — но это только 5 dividers для 5 контент-разделов; Раздел 0 = открытие без divider, Раздел 6 = Q&A с s38). Pattern matches Lec-7 (5 dividers для 5 разделов). ✓

**Top progress bar:** plan §5 line 96 говорит «6-card progress bar» на s06 divider. Lec-7 имел `section_divider_with_progress` (with progress bar на dividers только). Plan не упоминает явно «progress bar только на dividers + cover, не на content slides» (anti-pattern Lec-2). **P2 рекомендация:** в Phase 5 deck-design явно prescribe: top progress bar только на dividers + cover, НЕ на каждом content slide.

---

### 6. Hook engagement (ENFORCED — anti-pattern «outdated empirical test») — **PASS**

**Цитата (plan s01, lines 89-92):**
> Live: открыть https://suno.com/create в браузере, попросить аудиторию накидать 1 промпт (тема + жанр + язык) → сгенерировать трек на месте → проиграть 30 сек.

**2026-evergreen check:**
- НЕ использует strawberry-test / 9.11 > 9.9 / counting-r-in-strawberry ✓
- НЕ outdated empirical test ✓
- Эмоционально engaging: «вы только что сгенерировали то, что 3 года назад стоило $500 и неделю» — cost-asymmetry hook ✓
- «Висит на экране» worthy: live URL в браузере ✓
- Connected to assertion: «AI генерирует production-уровень artefact за секунды без специальных навыков» = direct foreshadow keystone «добавил» ✓

Hook сильнее, чем strawberry-class hook — это **interactive cost-reveal** с physical artefact (сгенерированный трек).

**Minor — Open question #1 (lines 254):** plan правильно flag-нул «звуковая аппаратура в аудитории — есть/нет» как owner-input. ✓

**P2 — fallback strategy:** «Firefly (image) если sound не работает» — это хорошо, но **fallback меняет ситуативно hook narrative**. Image-generation hook ≠ audio-generation hook (cost story немного другая для image: $50-200 freelance vs $0.04 image). **Рекомендация:** plan v2 явно прописать **обе версии hook narrative** (audio-version и image-version), чтобы speech-writer не импровизировал на месте.

---

### 7. Missing-fundamentals check — **GAP / P1**

**Аудитория (line 5):** студенты-инженеры 3 курса МГТУ ИУ6 (универсальная, не дизайнеры / не творцы).

**Plan не имеет fundamentals slide,** который объясняет **как работают** генеративные модели для медиа:
- Diffusion (Stable Diffusion, Midjourney, Flux, DALL-E, Imagen, Firefly) — как работает diffusion process: noise → reverse → image
- Latent video transformer (Sora 2, Veo, Runway) — latent space, temporal consistency
- Neural audio synthesis (Suno, Udio, ElevenLabs) — autoregressive vs diffusion для audio
- Voice cloning (ElevenLabs) — fine-tuning из 1 мин аудио

**Plan §5 Раздел 1 (lines 98-108)** показывает capabilities — что модели делают. **Не объясняет как они работают.** Это критично для inженер-аудитории: они должны понимать, почему diffusion vs transformer (concept) даёт разные ограничения (длина, consistency, cost). 

**P1 issue #3 — Add fundamentals slide.** В Разделе 0 (после s05 keystone) или начале Раздела 1 (между s06 divider и s07 Sora 2). Может быть:
- **Вариант А (рекомендую):** новый s05a «Как работают генеративные модели медиа — 3 семейства» (1.5 мин). Diffusion (image/video из noise) | Latent transformer (long sequences in latent space) | Neural audio synthesis (waveform/spectrogram autoregressive). 1 строка на каждое семейство. Это **не deep dive**, это mental model для оставшейся лекции — почему Sora 2 имеет 25-сек предел? потому что latent transformer ↔ cost scales. Почему Firefly «commercially safe»? potому что training corpus.
- **Вариант Б:** spread fundamentals on s07/s08/s09 как mini-intro блок к каждой capability.

**Без fundamentals slide студент-инженер уносит: «AI делает X, Y, Z; провалы — A, B, C» — но не понимает архитектурную причину границ.** Это противоречит LO2 («оценить применимость» — для этого нужно понимать почему inherent limits, не только знать что они есть). **Mandatory fix перед Phase 2.**

---

### 8. Concept-evidence-implication structure — **PASS с caveats**

**Проверка по выбранным слайдам:**

- **s07 (line 103):** Concept = «Text-to-video поколение 2026»; Evidence = Sora 2 (25 сек, 1080p, $0.10/sec), Kling 3.0 (#1 ELO 1243, 4K, 60 fps); Implication = «25 сек ≠ фильм; cinematic pipeline собирается из коротких блоков». ✓
- **s14 (line 115):** Concept = «Cost-collapse»; Evidence = таблица 100×-10,000× из research C.1; Implication = «дешевле ≠ бесплатно — Firefly $400M revenue». ✓
- **s17 (line 118):** Concept = «Под удар: −17% jobs»; Evidence = Upwork data, Getty+Shutterstock merger $3.7B, Shutterstock licensing pivot $104M→$250M; Implication = «consolidation = удар по нижнему звену авторов». ✓
- **s21 (line 127):** Concept = «NYT v OpenAI training+output»; Evidence = 20M ChatGPT logs, SJ deadline 2 апр 2026; Implication — **не явно сформулирован**. Что выученный урок? Что инженер должен делать с этим знанием? **P2 fix.**

**P2 issue:** s20, s22 (Getty), s23 (Andersen), s24 (RIAA) — те же legal cases — концепты ясны, evidence ясно, но «выученный урок для инженера» иногда implicit. Plan нужно более explicit формат `Урок: 1 фраза для инженера` для каждого s20-s31. Это уже flagged в check #2.

**Не hello-everything-bag** ✓ — каждый слайд имеет thesis (assertion), evidence anchor, и (для большинства) implication.

---

### 9. Pacing math — **GAP / P1 (P1 если не fix)**

**Plan §5 заявляет (line 84):** 75 мин = 6 разделов + Q&A.

**Time breakdown по plan:**
- Раздел 0 (открытие): 8 мин = s01 (3) + s02 (0.1) + s03 (2) + s04 (1.5) + s05 (1.4) = **8.0 мин** ✓
- Раздел 1 (ДОБАВИЛ): 12 мин = s06 (0.5) + s07 (2) + s08 (2) + s09 (2) + s10 (1.5) + s11 (2) + s12 (2) = **12.0 мин** ✓
- Раздел 2 (ИЗМЕНИЛ): 12 мин = s13 (0.5) + s14 (3) + s15 (2.5) + s16 (2.5) + s17 (2) + s18 (1.5) = **12.0 мин** ✓
- Раздел 3 (СЛОМАЛ): 24 мин = s19 (0.5) + s20 (1.5) + s21 (2) + s22 (2) + s23 (2) + s24 (2) + s25 (2) + s26 (2.5) + s27 (2) + s28 (2) + s29 (2) + s30 (1.5) + s31 (1.5) = **23.5 мин** ✓ (≈24)
- Раздел 4 (не нужен): 8 мин = s32 (0.3) + s33 (2.5) + s34 (2) + s35 (2.7) = **7.5 мин** ⚠ (0.5 мин разрыв)
- Раздел 5 (что делать): 4 мин = s36 (0.5) + s37 (3.5) = **4.0 мин** ✓
- Q&A: 3 мин = s38 (2.5) + s39 (0.5) = **3.0 мин** ✓

**Sum: 8 + 12 + 12 + 23.5 + 7.5 + 4 + 3 = 70.0 мин**, не 75. **Разрыв = 5 мин = 6.7% buffer.**

Plan §10 line 263 (open questions #4): «39 слайдов … оставляем или ужимаем до ~33». **Plan имеет 39 слайдов, не 33.** Median content slide ~1.9 мин/слайд (70 мин / ~36 контент-слайдов). Это **близко к нижней границе** (rec: 2-4 мин на средний слайд).

**P1 issue #4 — Pacing buffer недостаточен.**
- Plan заявляет «75 мин 8'+12'+12'+24'+8'+4' = 68'». Это **не математика plan**: реальная sum = 70 мин (не 68). У plan несоответствие между сумма-расчётом (line 96 «1.4 мин» для s05 — нестандартное дробное значение, выглядит как «затыкаем дырку до 8 мин Раздела 0») и реальной длительностью лекции 75 мин.
- 5 мин buffer = 6.7%, ниже рекомендованных 7-10% для Q&A overruns.
- **Если 39 слайдов на 70 мин = ~1.8 мин/слайд в среднем**, что на нижней границе (некоторые слайды — 1.5/2 мин = очень быстрый темп). **Раздел 3 (24 мин на 13 слайдов = 1.85 мин/слайд)** — это «жалкий темп» для emotionally-loaded failure-cases. Студент не сможет переварить 1 case за 1.5-2 мин для глубокого кейса вроде s27 Korea schoolgirl.

**Рекомендация:** **Принять open question #4 — ужать до ~33 слайдов** (Lec-7 size). Консолидация:
- s23+s24 (Andersen + RIAA) → 1 слайд «Art + Music — 2 class actions, общая taxonomy» (3 мин).
- s28+s29 (slop + fake authors) → 1 слайд «Brand-trust failures: slop + fakes» (3 мин).
- s11+s12 (workflow + summary Раздел 1) → 1 слайд (2.5 мин).

Это вернёт лекцию к ~32-34 слайдам, 2.2 мин/слайд average, 75 мин с 7-10% buffer.

**Alternative:** не consolidate, но удалить s12 (cross-cutting summary timeline) + s18 (adoption metrics summary) — эти summary слайды — методически слабее cases. -2 слайда, +5 мин buffer ⇒ 75 мин hit.

---

### 10. Open questions quality — **PASS**

5 open questions plan §10:

1. **Ice-breaker live demo (s01) — Suno vs Firefly** — genuinely require owner-input (зависит от audio infrastructure в аудитории, не от orchestrator decision). ✓ **Genuine.**
2. **Korea schoolgirl deepfake (s27) — sensitivity check** — это **excellent flag**: chapter может содержать sensitive contents, но slide визуал нужен owner-call. ✓ **Genuine.**
3. **Российские кейсы (Yandex Шедеврум, Sber Kandinsky, VK Music)** — research dossier не покрывает; owner-decision на охват. ✓ **Genuine and important** — Lec-7 имел российский context (mosmed.ai s12); Lec-5 имел Сбер. Если Лекция 8 не имеет российского аналога — это диссонанс с pattern course (Sber Kandinsky действительно был бы релевантен).
4. **Slide count (39 vs ~33)** — owner pacing trade-off. ✓ **Genuine.** (См. check #9 — я рекомендую ужать.)
5. **Sora 2 standalone discontinuation** — это **факт-decision**, не owner-decision. Это **должно быть проверено через `[VFY-day-of]`** в любом случае. **P2 polish:** превратить в «Если Sora 2 standalone discontinued подтверждается на дату лекции — упомянуть как урок (даже OpenAI отказался)». Не нужно owner-decision на «упоминать ли», нужен fact-check.

**Не micromanagement** ✓ — все 4 первых вопроса требуют semantic input от course owner. Только #5 — fact-check, не decision.

---

## Cross-cutting issues

### Glossary lock (P2)
**Plan §8 line 219-237** — 15 терминов flagged для lock после Phase 3. Хорошо. Но **glossary lock сейчас preliminary** — это правильно (chapter ещё не написан). После Phase 2 chapter — финальный glossary lock с cascade-of-changes для slides + speech.

### Cross-references (P2)
**Plan §9 line 246** — Lec-7 4-actor responsibility framework parallels для Лекции 8 (ScarJo / Andersen / Arup / Sony). Plan правильно решает «упомянуть тонкую параллель, не делать explicit framework» (line 246). ✓

**Minor:** Lec-5 «AI-failure кейсы (финансы)» parallel = legal-risk frame. Это хорошо, но **plan не упоминает** Sber AI scoring (Lec-5) как параллель для media moderation / brand-trust. **P2.**

### Term consistency (P2)
Plan §8 термины: **«Slop»** (line 229) — определяется как «низкокачественный AI-generated content, заполняющий platforms». Это **slang**, не canonical academic term (Bender, Marcus используют — но это recent neologism, 2024+). **Plan не flag это как insider/colloquial.** Рекомендую: в chapter явно отметить «"Slop" — colloquial term, used by Bender/Marcus 2024+; academic synonym = "low-quality synthetic content"». **P2.**

### Vendor freshness check (P2)
- Sora 2 «$0.10/сек 720p» — `[VFY-day-of]` flagged ✓
- Kling 3.0 «#1 ELO 1243» — `[VFY-day-of]` flagged ✓
- Genie 3 «29 янв 2026 релиз» — stable historical fact ✓
- ARC-AGI / benchmark scores — N/A для этой лекции (но if added — должны быть `[VFY-day-of]`)

Всё volatile корректно flagged. ✓

### Plan tone (P2)
Plan generally respectful — пишет «студент сможет» (LO formulations), не «вы научитесь решать всё». Без «магической пилюли» framing. ✓

---

## Топ-4 must-fix items (приоритизировано)

### P1 #1 — Add fundamentals slide для генеративных моделей медиа (см. check #7)
**Action:** plan v2 §5 Раздел 1 — добавить s05a «Как работают 3 семейства генеративных моделей медиа» (1.5 мин) до s06 divider, ИЛИ split between s07/s09/s10.
**Why:** студент-инженер должен понимать архитектурную причину границ (Sora 2 25-sec, Firefly «commercially safe»), не только знать что они есть.
**Cost of not fixing:** LO2 («оценить применимость») не достижим — студент уносит набор фактов, не mental model.

### P1 #2 — Resolve пейсинг discrepancy 70 vs 75 мин + decide slide count (см. check #9)
**Action:** plan v2 §5 — либо consolidate до ~33 слайдов (рекомендую), либо удалить s12 + s18 summary слайды; вернуть pacing к 75 мин с 7-10% buffer.
**Why:** 6.7% buffer слишком мал для 75-минутной лекции с emotionally-loaded failure-cases (Раздел 3); Раздел 3 на 1.85 мин/слайд — невозможно глубоко обсудить кейс вроде s27 Korea schoolgirl.
**Cost of not fixing:** лекция overruns или каждый кейс читается поверхностно (отравляет failure/judgment ≥30% strict-in claim).

### P1 #3 — Сделать explicit relationship «3 времени × 4 области» (см. check #4)
**Action:** plan v2 §2 или §4 — добавить мини-параграф: «Эти 4 области — не разделы лекции (разделы = времена оси). 4 области = sub-classifier внутри каждого времени; смотреть как cross-product».
**Why:** студент должен видеть, что 4 области и 3 времени — ортогональные taxonomies, не дублирующиеся.
**Cost of not fixing:** mental model студента смешан, разрушает keystone-ось.

### P1 #4 — Add infrastructure slide ИЛИ явно отказаться (см. check #4)
**Action:** plan v2 — либо добавить мини-слайд Раздела 1 о платформах (Adobe Firefly Foundry, HuggingFace Spaces), либо обосновать в §4 line 79 почему платформенный слой не получает слайда («L4 lecture про tools, не infrastructure»).
**Why:** plan правильно отделяет платформенный слой концептуально, но visible-layer molchit об этом — gap между concept и slide breakdown.
**Cost of not fixing:** студент может смешать Adobe Firefly (платформа) с Sora 2 (модель/инструмент).

---

## P2 (polish, не блокирующее)

1. **s04 lecture-map + s05 keystone — явно разграничить функции** (check #1).
2. **Add explicit «Урок: 1 фраза для инженера»** к каждому из 12 кейс-слайдов Раздела 3 (s20-s31, check #2).
3. **Fallback hook narrative для image-version** (check #6 Suno vs Firefly).
4. **s21 NYT — implication explicit** (check #8) + аналогично s22, s23, s24.
5. **Russian context decision** — Open Q #3, если включаем (Yandex Шедеврум / Sber Kandinsky / VK Music) — где: отдельный слайд в Разделе 1 или footnote.
6. **«Slop» term flag как colloquial** в glossary (cross-cutting).
7. **Lec-5 parallel mention** для AI-failure structural frame (cross-cutting).
8. **Open Q #5 (Sora 2 standalone) — переписать как fact-check, не decision** (check #10).
9. **Top progress bar — only on dividers + cover** — явно prescribe в plan v2 (check #5).
10. **Speech-narrative §-named «Sora 2 / Veo 3.1 как API endpoints» — явный owner-anchor flag** (check #3).
11. **Adoption-направление словами** на видимом слое — plan §4 имеет слова, но volatile-доли (40%, 75%, 86%, 87%) в Разделе 2 plan §5 (s18) — добавить `[VFY-day-of]` или прийти к «word-only» вариантам типа «большинство маркетологов» (P2 fix к Phase 2 chapter).

---

## Summary (< 300 слов)

Plan v1 структурно сильный: keystone-ось «добавил → изменил → сломал» предъявлена отдельным s05 слайдом в Разделе 0 ДО первого погружения (Лекция 4 lesson обработан правильно). Failure-share ≥30% strict-in заявлен в 3 артефактах (46-53%), не сконцентрирован в одном. Tools-per-taxonomy на каждом из 4 уровней (кино/музыка/изображения/текст) включает named brands + adoption-направление + anti-hype + `[VFY-day-of]`. Ice-breaker (Suno live demo) — 2026-evergreen, не strawberry-class.

**4 P1 issues** требуют адресации до Phase 2 chapter draft:
1. **Missing fundamentals slide** — студент-инженер не получает mental model «как работают 3 семейства генеративных моделей» (diffusion / latent transformer / neural audio). LO2 «оценить применимость» недостижим без этого.
2. **Pacing math 70 vs 75 мин** + 39 слайдов = 1.85 мин/слайд average в Разделе 3 = слишком плотный темп для emotionally-loaded кейсов. Consolidate до ~33 слайдов (s23+s24, s28+s29, s11+s12).
3. **Relationship «3 времени × 4 области»** не явный — student может смешать ось и таксономию.
4. **Infrastructure layer** — концептуально отделён, но не получает явного слайда (или явного отказа).

Плюс 7 P2 polish items (явный «Урок:» в кейсах, glossary lock для «slop», fallback hook для image-version, Russian context decision и т.д.).

**Verdict: APPROVE-WITH-POLISH** — план готов идти на USER GATE 0 при условии, что 4 P1 включены в обсуждение с owner-ом. Это не REVISE-grade gaps (структурно лекция сильна, методически работает); это polish, который улучшит LO2 achievability и темп Раздела 3. P0 нет.

---

**End of critique v1.**

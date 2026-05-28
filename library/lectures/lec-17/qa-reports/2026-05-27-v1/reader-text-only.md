# Reader Simulator (text-only) Report — Lec-17 Chapter v1

**Date:** 2026-05-27
**Mode:** text-only (chapter only, no slides, no speaker notes)
**Reader profile:** студент 3-го курса инженерных специальностей, прошёл L1-L16, готовится к экзамену
**Verdict:** **APPROVE-WITH-POLISH**

---

## Summary

Capstone глава **в целом работает для self-study**: keystone-axis (2D-плоскость) представлен ясно, 7 критериев отчётливо различимы, лестница L0→L5 хорошо структурирована, 12 провалов запоминаются. Word count = 30 001, что точно попадает в target. Тон **студенто-ориентирован** (обращается «вы», использует аналогии — компас/карта, дифференциальная диагностика, FMEA, Feynman technique).

**Главные проблемы:** (1) **Часть 1 затянута** — Раздел 0 содержит много meta-рефлексии и repetitions, которые могут утомить уже на старте; (2) **Часть 2 §1.1 имеет inconsistent slide-anchors** ([for-slide-s08] повторяется 3 раза подряд); (3) **Часть 3 §3.x перегружена компактностью** — 16 отраслей за ~3500 слов, каждая получает 100-150 слов, что недостаточно для recall; (4) **excessive англицизмы** в Части 4 (`career trajectory`, `mentorship`, `threat / opportunity`, `vendor lock-in`, `groupthink`, `slip`, `commit`) — для МГТУ ИУ6 RU-аудитории это полировки; (5) **Cornerstone glossary разрастается** от обещанных 18 терминов до 47 — без warning студенту, что половина — добавочное.

После polish-round по этим 5 P1 issues — chapter готов служить self-study ресурсом.

---

## Compliance checks

- **Self-contained for self-study:** **pass** — студент, помнящий L1-L16 только в общих чертах, понимает capstone. Cross-references к лекциям краткие («см. L13»), не блокирующие.
- **Keystone-axis clarity:** **pass** — 2D-плоскость представлена в §0.3 с полными определениями обеих осей, 4 квадрантами, и тремя кросс-кейсами (медицина, CrowdStrike, UPS ORION) показывающими независимость осей. Конкретно вижу: «Применимость ИИ × Лестница автономии».
- **7 criteria distinguishability:** **pass** — каждый критерий разворачивается отдельным §, имеет (а) определение, (б) канонический success-case, (в) канонический failure-case, (г) подкритерий. Критерии не сливаются.
- **L0→L5 ladder clarity:** **pass с caveat** — 6 ступеней distinguishable, каждая имеет «что делает / кто решает / criteria подъёма / антипаттерны / примеры из курса». **Caveat:** маппинг локальных шкал курса в §2.7 — самое слабое место Части 2 (см. P1 #4).
- **12 failures memorability:** **partially-pass** — провалы 1-6 запоминаются хорошо (open-world, reliability compounding, vendor demo, HITL boring, excessive automation, Act без канарейки). Провалы 7-12 размываются: между Galactica (#7), voice/chat (#8), training data leak (#9), vendor lock-in (#10), slopsquatting (#11), pilot purgatory (#12) — нет clear mnemonic structure. Рекомендую визуальную группировку (3 mega-pattern из §4.13 — отличная idea, но она появляется только в КОНЦЕ).
- **Cross-refs working:** **mostly-pass** — `(см. §X.Y в части N)` форма консистентна. Не нашёл broken refs. Forward-references работают (§5.5 действительно про career; §3.7 действительно про пустые квадранты).
- **Cornerstone glossary helpfulness:** **partially-pass** — glossary включает 47 терминов вместо обещанных 18 во frontmatter (см. P1 #5). Глоссарий полезен, но frontmatter mislabels.

---

## P0 issues

**Ни одного P0** — chapter functions для self-study на baseline уровне. Все обнаруженные issues — P1/P2 уровня polishing, не структурные.

---

## P1 issues

### P1-1: Часть 1 (Раздел 0) — слишком много meta-рефлексии и self-praise

**Где:** §0.1 («Hook»), §0.4 («Главный вопрос re-asked»), §0.6 («Особенности структуры»). Все три раздела по сути повторяют одну мысль: «вы научились говорить нет ИИ» / «навык дефицитный» / «карта не статична». Между §0.4 и §0.6 — 4 раза повторяется тезис «карта не вечна».

**Конкретные quote-ы:**
- §0.1 строка 134: «...вы выходите из курса как раз вовремя».
- §0.4 строка 287: «Окончание этого курса — это начало, а не окончание AI literacy».
- §0.4 строка 290: «Маршрут от 2026 года устарел бы через 2-3 года. Карта остаётся valid через 10+ лет».
- §0.6 строка 343: «Все упомянутые инструменты, модели, провалы и success-кейсы — это материал, который уже встречался».

**Проблема для reader:** через 30 минут чтения студент устал от мета-разговоров о курсе **до того, как** дошёл до собственно diagnostic content (Раздел 1 в Части 2). Раздел 0 = ~7500 слов / 25 минут чтения. Из них ~3000 слов — meta-discourse (carrer arc, чем отличается от prompt engineer, как карта будет служить через 10 лет). Это слишком рано для такого discourse — он должен быть **в Разделе 5** (там он и появляется ещё раз).

**Конкретный recommendation:**
- §0.4 строки 272-303 («Каскадирование зрелости диагностики», «Тренировка диагностического вопроса», «Аналог из медицины», «Аналог из инженерии безопасности FMEA», «Что вы реально получили в эти шестнадцать лекций») — **переместить в Раздел 5 §5.5 (career trajectory)** или **в Q&A backup** (Q1, Q3).
- §0.6 строки 335-355 — сократить с 20 параграфов до 4 (mandate: что глава делает + 1 финальный motivational paragraph).
- Целевое сокращение Части 1: с 7663 слов до ~5500 (~30%).

---

### P1-2: §1.1 — slide-anchor `[for-slide-s08]` повторяется 3 раза подряд

**Где:** chapter-part2.md, строки 71, 88, 100 — все три раза `[for-slide-s08]` для одного и того же раздела (§1.1 Критерии 1 + 2).

**Проблема:** для reader это OK (он не смотрит на anchors), но Phase 5 (speaker notes generation) сломается — slide s08 получит 3 разных «начальных» секции и не сможет правильно derive notes. Это **technical debt**, который вылезет в Phase 5.

**Recommendation:** один anchor `[for-slide-s08]` в начале §1.1 (строка 71), затем `[for-slide-s09]` либо подразделы s08a/s08b. Орчестратор / book-editor должен решить slide-mapping.

---

### P1-3: Часть 3 §3.1-§3.3 — 16 отраслей сжаты слишком плотно

**Где:** chapter-part3.md, строки 42-232 (~3500 слов на 16 отраслей).

**Проблема для reader:** каждая отрасль получает ~150-220 слов. Через 16 отраслей подряд они сливаются. Я (reader) после прочтения §3.1-§3.3 могу назвать:
- **Уверенно:** L4 SE (верхний правый), L7 медицина (верхний левый), L10 агро (bimodal), L13 логистика (3 точки — warehouse / robotaxi / black swan).
- **Слабее:** L5 финансы (mid-high?), L8 креатив (где именно?), L9 aero (где restricted top?).
- **Совсем забыл через 30 минут:** L6 CAD, L11 manufacturing, L15 наука, L16 нефтегаз — не помню квадранты без перечитывания.

**Конкретный recommendation:** 
1. **Добавить сводную таблицу** в конце §3.3 (Final batch): 16 отраслей × колонки (X-coord, Y-coord, success-case, failure-case, quadrant). Студент возвращается к одной таблице вместо 16 параграфов.
2. **Bold-выделить квадрант** в каждом параграфе отрасли (сейчас это делается inline, но смешано с длинным narrative).
3. **§3.1 starter точки — оставить как есть** (4 отрасли × 250 слов работают). §3.2 + §3.3 — компрессировать в табличную форму + 3-4 deep-dive отрасли (L10 bimodal, L13 trimodal, L16 quadrant matrix).

---

### P1-4: §2.7 Маппинг локальных шкал — концептуально перегружено

**Где:** chapter-part2.md, строки 488-528.

**Проблема:** Это **главный научный артефакт capstone** (по словам самого автора), но reader проходит через таблицу-маппинг и понимает только часть. Конкретно:
- Колонка «L13 logistics (среда)» — это **horizontal axis structuredness**, не **vertical autonomy**. Автор сам это признаёт строкой 518: «**L13 logistics 5-level structuredness** — это **horizontal**, не vertical. Описывает **тип среды**, а не уровень AI participation. ortogонально нашей единой L0-L5».
- Но если ortogонально — **почему она в таблице vertical mapping?** Это путает reader.

**Также:** L14 «Видит-Решает-Действует» — это **три функции**, не уровни, и автор это тоже признаёт строкой 519. Опять — почему в той же таблице?

**Recommendation:** Перепроектировать §2.7 в виде **двух** таблиц:
- Таблица A: «прямой mapping» (L4 SE A/B/C/D, L9 aero L1-L5, L12 A0-A3 — это все autonomy ladders).
- Таблица B: «нелинейный mapping» (L13 среда, L14 функции — это другие axes, требуют декомпозиции на autonomy ladder per axis).

Сейчас одна таблица скрывает эту разницу, и студент путается «что значит L13 L1 = capstone L1».

---

### P1-5: Cornerstone glossary раздувается до 47 терминов вместо обещанных 18

**Где:** chapter-part4.md frontmatter chapter.md строка 40 — «**Cornerstone glossary 18 терминов**». Реально в Appendix A — **47 терминов** (я считал — от AI Effect до Self-driving lab).

**Проблема:** Это **не bug — это feature**, но студент, ожидавший 18, начинает теряться к 25-му термину. Многие термины — не cornerstone, а просто **технические термины из конкретных лекций** (ATEX Zone 0 / IEC 61508 SIL 2/3, ORCA benchmark, ISA-95, PAT, SAR — эти 5 терминов появятся 1-2 раза в карьере студента, не cornerstone).

**Recommendation:** 
1. Frontmatter chapter.md обновить — `cornerstone_glossary_count: 18 cornerstone + ~30 lecture-specific = 47 total`.
2. **Разделить Appendix A на 2 раздела:**
   - **A.1 — Cornerstone (18 терминов)** — те, что повторяются 3+ раз через несколько лекций: AI Effect, Pearl's 3 levels, OODA, HITL/HOOL/HOTL, ODD, pilot purgatory, closed-loop vs open-environment, reliability compounding, distribution shift, ground-truth feedback loop, cost-of-error / blast radius, automation paradox, foundation model, RAG, MITRE ATLAS, sycophancy, hallucination, digital twin.
   - **A.2 — Lecture-specific (29 терминов)** — slopsquatting, ARC-AGI, methane MRV, ATEX Zone 0, ORCA benchmark, ISA-95, PAT, SAR, POD, SBOM, C2PA, и т.д. С пометкой «термин из L4 / L9 / L15 — пересмотри лекцию для контекста».
3. Это удешевляет cognitive load для студента, который готовится к экзамену по 18 cornerstone, а 29 lecture-specific — это reference при появлении.

---

### P1-6: Excessive англицизмы в Части 4 для МГТУ ИУ6 RU-аудитории

**Где:** chapter-part4.md, §5.5 и далее.

**Конкретные примеры** (только из §5.5):
- «Career paths» × 3 раза (строки 204, 211, 213).
- «Soft skills / hard skills» × 4 раза (строка 222).
- «Mentorship» (226, в названии раздела).
- «Trust transfer» (393).
- «Vendor lock-in» × несколько раз (везде).
- «Slip из 6-месячный пилот» (550) — «slip» здесь как глагол без перевода.
- «Threat / opportunity» × 5 раз (строки 194-200).
- «Groupthink» (65, 224).
- «Stakeholders» × 5 раз — «stakeholder management» / «non-technical stakeholders».
- «Mid-task block» / «narrow ODD» / «full automation» / «budget cap» — местами оправдано (термины), местами заменимо («блок кода» / «узкий домен эксплуатации» / «полная автоматизация» / «лимит бюджета»).

**Проблема:** для capstone курса МГТУ ИУ6 — это **не критично** (студент IT-3-курса встречает эти слова в работе), но **полировка** улучшит читаемость. Memory rule `[[russification]]` гласит «producer-agents склонны excessive англицизмам».

**Recommendation:** Phase 4 critic-pass с russification table (45+ замен из notes/decisions.md). Sample конкретных замен:
- `career path` → «карьерная траектория»
- `mentorship` → «наставничество»
- `soft skills / hard skills` → «гибкие / жёсткие навыки» (или оставить — well-established в RU)
- `threat / opportunity` → «риск / возможность»
- `groupthink` → «стадное мышление» (стандартный RU перевод)
- `stakeholder` → «заинтересованная сторона» (или оставить — RU IT vocab)
- `mid-task block` → «блок кода в середине задачи»
- `slip into purgatory` → «соскальзывание в чистилище»

Не все замены 1:1 — некоторые термины (vendor, baseline, ODD, HITL, blast radius, pilot purgatory, foundation model) являются established IT vocabulary и не требуют замены. Но `career path`, `mentorship`, `trust transfer`, `slip`, `groupthink` — однозначно RU-translate-able.

---

## P2 issues

### P2-1: Typos и stylistic awkwardness

- Часть 1, строка 79: «...способность за минуты понять, является ли решение элегантным или переусложнённым. Для AI **«AI-инженерный вкус»**...» — повтор «AI» дважды подряд.
- Часть 1, строка 116: «...жёлтком на сильно искажённую призму» — «жёлтком»? возможно меня глючит, но смотрю ещё раз — нет, в файле «через эту сильно искажённую призму». OK, ложная тревога.
- Часть 2, строка 116: «**Подробнее про distribution shift.**» — pattern repeat секцией ниже (строка 106 уже «Подробнее про distribution shift»).
- Часть 2, строка 309: «**Юридические и regulatory гран ицы**» — «гран ицы» с лишним пробелом.
- Часть 2, строка 370: «**False-positive rate приемлем.** На L2 человек **ratifies каждое** действие; если AI слишком часто ложно срабатывает, человек уста и теряет внимание.» — «уста» (надо «устаёт»).
- Часть 3, строка 392: таблица p^N имеет inconsistent precision (0.95 vs 0.90 vs 0.005) — OK для table, но запятая после 0.005 отсутствует ([12 vs 0.005]).
- Часть 4, строка 119: «**Зачем именно 12 провалов, а не 5 или 50.**» — «pаперовые исследования» в §4.9 (строка 499) — «paperовые» mix.
- Часть 4, строка 224: «Развитие через mentorship.» — «mentorship» в bold с следующим RU предложением.
- Часть 4 строка 240: «engineer **первый** проверяет границы» — «первый» как наречие? нужно «сначала».
- Часть 4 строка 251: «Шестнадцать историй» — позже в списке всего 9 (Zillow, IBM Watson, CrowdStrike, Galactica, Klarna, Plenty, Cruise, Uber Tempe = 8). «Шестнадцать историй» → «**Шестнадцать отраслей** + 8-10 канонических кейсов».
- Часть 4 строка 252: «engineering tool» — английский в финальном предложении closing thesis.

### P2-2: «Сетка self-check вопросов» работает, но не использует таблицу

В конце каждой части есть Self-check вопросы (5 в каждой) — это хорошо, но они не пронумерованы по lo-критериям и не привязаны к LO1-LO8 из frontmatter. Студент, готовясь к экзамену, не знает «какие вопросы covered LO3» (карта).

**Recommendation:** добавить tag `[LO3]` рядом с каждым вопросом self-check.

### P2-3: §0.5 Roadmap дублируется

В §0.5 строка 311-323 — roadmap 5 разделов. Это **дублирует** «Карта главы и индекс частей» (chapter.md строки 42-53). Reader получает roadmap 2 раза подряд (в frontmatter и снова в Разделе 0).

**Recommendation:** оставить TOC в §«Карта главы», убрать §0.5 (или сократить с 20 параграфов до 1 transitional абзаца к §1).

### P2-4: Mixed-case slide anchors

В chapter.md: `[for-slide-s01]`, `[for-slide-s02]`. В chapter-part2.md: `[for-slide-s06]`, `[for-slide-s07]`, `[for-slide-s08]`, `[for-slide-s09]`, `[for-slide-s10]`, `[for-slide-s11]`, `[for-slide-s12]`, `[for-slide-s13]`, `[for-slide-s14]`, `[for-slide-s15]`, `[for-slide-s16]`, `[for-slide-s17]`, `[for-slide-s18]`, `[for-slide-s19]`, `[for-slide-s20]`. **Согласно slide_map во frontmatter** — s01-s05 Раздел 0, s06-s12 Раздел 1, s13-s20 Раздел 2. Я нашёл что:
- Slide s05 anchor отсутствует — у меня anchor s05 на строке 305 (§0.5), но §0.6 идёт без anchor. **Slide s05 покрывает §0.5 или §0.6?**
- В §2.x: anchors s15-s18 повторяются неравномерно. s16 — только §2.2 (Advisory). s17 — §2.3 (Supervised) + §2.4 (Conditional) — два разных слайда на одну метку.

**Recommendation:** Phase 5 designer должен решить точное slide-mapping, но book-editor должен **гарантировать**, что каждый slide-anchor встречается строго 1 раз.

---

## «Что осталось в голове» test results (через 2 часа после прочтения, без перечитывания)

Я как reader попытался вспомнить через 2 часа после прочтения (имитация финального экзамена через несколько дней):

### Test 1 — 2D-плоскость и оси
**Result: PASS** — горизонталь = применимость ИИ (AI fit, от detministic non-AI до full AI), вертикаль = лестница автономии L0-L5. Запомнил уверенно благодаря §0.3 keystone reveal + повторению в §1 и §2.

### Test 2 — 7 критериев (хотя бы 5 из 7)
**Result: PASS** — могу назвать:
1. Закрытая петля vs открытая среда ✓
2. Достаточно training data ✓
3. Повторяемость и объём ✓
4. Цена ошибки / blast radius ✓
5. Ground truth / эталон ✓
6. Объясняемость / audit ✓ (помню Apple Card)
7. Экономика vs baseline ✓ (помню UPS ORION)

Все 7 — благодаря таблице Карточка #1 в §5.1 и структурированной подаче.

### Test 3 — L0→L5 ladder и criteria подъёма
**Result: PARTIAL-PASS** — могу:
- L0 — без автоматизации (FDA сертификация авиа) ✓
- L1 — advisory (Aidoc, Copilot autocomplete) ✓
- L2 — supervised (Stripe Radar auto-block, FKDPP) ✓
- L3 — conditional / narrow ODD (Waymo) ✓
- L4 — high / broad ODD (Symbotic, See & Spray) ✓
- L5 — full (теоретически — AlphaFold; практически — нет) ✓

**Но** criteria подъёма помню только смутно: «baseline → AI improvement» для L1→L2, «99.9% reliability + insurance + regulatory» для L3→L4. Запомнились лучше **антипаттерны** (Klarna, Uber Tempe, Cruise, CrowdStrike, LAWS) — это работает лучше.

### Test 4 — 8 из 12 канонических провалов с уроками
**Result: PASS (8 из 12)** — могу назвать:
1. Open-world prediction (Zillow / Monarch / Cruise) ✓
2. Reliability compounding (p^N) ✓
3. Vendor demo ≠ production (Devin / Epic Sepsis / Watson) ✓
4. HITL boring (Uber Tempe / F-35 ALIS) ✓
5. Excessive automation (Tesla 2018) — частично ✓
6. Act без канарейки (CrowdStrike) ✓
7. Galactica scientific hallucination ✓
8. Pilot purgatory ✓

**Не помню:**
- Voice/chat fraud (#8) — помню Air Canada chatbot, но без чёткого «класса провала».
- Training data leak (#9) — помню NYT vs OpenAI, но не как «verbatim memorization tail».
- Vendor lock-in (#10) — помню Climate FieldView и ALIS, но в моей голове это «#3 vendor demo». Слились.
- Slopsquatting (#11) — помню что это про AI hallucinated package names, но забыл имя класса провала (название слишком экзотичное).

Recall ratio: **8/12 = 67%** — попадает в target «8+».

### Test 5 — «инженер, который знает, когда НЕ применять AI»
**Result: PASS** — могу объяснить в 30 секунд: «не AI engineer (общее), не prompt engineer (узкое), а инженер с диагностическим навыком — 2D-карта, 7 критериев, лестница, 12 провалов. Дифференцирует от выпускника-генералиста на рынке труда 2026 года».

**Это запомнил уверенно** благодаря §5.5 + §5.7 closing thesis.

---

## Pacing of 4 parts (readability)

- **Часть 1 (7663 слов, 26 мин):** **engaging open, но затянутая meta-дискуссия**. Hook в §0.1 работает («умение сказать ИИ нет»). Keystone reveal в §0.3 — peak engagement. §0.4 и §0.6 — repeat + meta-overload. **Risk:** студент устаёт уже на Части 1.
- **Часть 2 (8751 слов, 30 мин):** **высокая плотность, но highest information density**. Раздел 1 (7 критериев) — каждое §1.1-§1.4 это work. Worked example §1.5 — отлично, conkretно делает абстрактное rabotающим. Раздел 2 (лестница) — структурирован, но §2.7 mapping table — confusing (P1-4). **Best section overall.**
- **Часть 3 (5833 слов, 20 мин):** **fastest read, но also fastest forgetting**. 16 отраслей × 150 слов = слишком плотно (P1-3). 12 провалов — лучше; §4.13 synthesis (3 mega-pattern) — самый ценный синтез всей главы. **Peak engagement через failures.**
- **Часть 4 (7754 слов, 26 мин):** **strong closer + glossary overload**. §5.0-§5.4 (4 карточки) — отлично, taking back home мощно. §5.5 career trajectory — мотивирующе, но англицизмы (P1-6). §5.7 closing thesis — **«знать ИИ значит знать его границы»** — крепкий thesis. Appendix A glossary 47 терминов (P1-5). Appendix B Q&A 12 вопросов — хороши, особенно Q1 (timeless map), Q11 (РФ кейсы), Q12 (books).

---

## Recommendations для Phase 4 revision

**Приоритет 1 (must-do):**
1. **Сократить Раздел 0 (Часть 1) на ~25-30%** — убрать meta-дублирование (P1-1).
2. **Перепроектировать §2.7 mapping** — две таблицы (direct vs orthogonal mappings) (P1-4).
3. **Часть 3 §3.1-§3.3** — добавить сводную таблицу 16 отраслей × квадрант + сократить inline narrative (P1-3).
4. **Cornerstone glossary** — обновить frontmatter count + разделить на cornerstone (18) и lecture-specific (29) (P1-5).

**Приоритет 2 (should-do):**
5. **Russification pass** (P1-6) — заменить ~15-20 излишних англицизмов в Части 4 на RU equivalents (career path, mentorship, threat/opportunity, slip, groupthink, trust transfer, soft/hard skills).
6. **Slide-anchors уникальность** (P1-2) — каждый `[for-slide-sNN]` встречается ровно 1 раз; Phase 5 designer не должна решать ambiguity.
7. **Typos pass** (P2-1) — «уста» → «устаёт», «гран ицы» → «границы», «pаперовые» → «paper-based», «Шестнадцать историй» → «отраслей».

**Приоритет 3 (nice-to-have):**
8. **LO-tags для self-check вопросов** (P2-2).
9. **§0.5 Roadmap** — сократить или убрать (дубль с frontmatter) (P2-3).
10. **Self-check ответы / hints** — для каждого вопроса дать reference в § (например, «см. §1.1»).

---

## Финальная оценка

**Capstone глава — рабочая для self-study.** Структура solid, концепции distinguishable, recall test 8/12 = passing target. Студент с подготовкой по L1-L16 может использовать chapter как preparation для финального экзамена + post-course reference.

**APPROVE-WITH-POLISH** — 6 P1 issues, все косметико-структурные (polish + redistribution + glossary cleanup), ни одного P0 структурного gap. После Phase 4 revision можно идти на Phase 5 (slides derivation).

**Ключевая сила chapter:** thesis «знать ИИ — значит знать его границы» — крепкий, измеримый, дифференциирующий. Студент выходит с понятной professional position, не размытым «AI literacy».

**Главная слабость chapter:** Часть 1 затянута на meta-discussion **до того, как** показала diagnostic content. Reader устаёт раньше, чем добирается до Части 2 (где content наиболее ценный).

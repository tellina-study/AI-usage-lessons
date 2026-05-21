VERDICT: APPROVE-WITH-POLISH

# Methodology Critic Report — Лекция 8 chapter v1 — 2026-05-20

## Severity counts

- **P0:** 0
- **P1:** 3
- **P2:** 8

Counter-check: 3 P1 ≤ 4 → APPROVE-WITH-POLISH is correct verdict (not REVISE).

---

## Verification of 10 ENFORCED checks

### 1. Failure / judgment share ≥30% strict-in — **PASS**

**Math re-verification (recomputed against actual file):**

| Section | Words |
|---|---|
| §3 «AI СЛОМАЛ» | **3,632** |
| §4 «AI здесь не нужен» | **934** |
| §5 «Что инженеру делать» | **628** |
| **Strict-in total** | **5,194** |
| Chapter total (incl. front-matter, sources, glossary) | **14,192** |
| **Strict-in share** | **36.6%** ✓ |

Chapter's claim 36.6% reconciles exactly. Threshold ≥30% cleared with **6.6 pp margin**.

**Sample-check 2 §3 cases for strict-in qualification:**

- **§3.2 NYT v OpenAI (256 words).** Contains documented failure (regurgitation theory, 20M logs discovery, SJ deadline 2 апр 2026) + explicit «Урок для инженера» («output similarity check обязателен», embedding/Bloom filter as concrete mitigation). **Verdict: strict-in.** ✓
- **§3.8 Korea schoolgirl deepfake (260 words).** Contains documented scale (>230 Telegram-чатов, 6,500 takedowns 4× YoY, 793 reported / 16 prosecuted = 2% enforcement) + mechanism (face-swap apps, секунды generation, Telegram distribution) + explicit lesson («safety layer до launch — NSFW detection + age verification + reporting pipeline»). **Verdict: strict-in.** ✓
- **§3.10 SI fake authors (295 words).** Provable failure (Futurism exposé, удалены articles), measurable harm (SI brand equity ~$1B, trust premium снижен), lesson is actionable («имя должно быть либо реальным человеком, либо explicitly AI-disclosed»). **Verdict: strict-in.** ✓

**Mini-failure blocks в §1-§2** (s07 «25 sec не фильм», s09 «ScarJo Sky», s11 «86% adoption ≠ success», s14 «дешевле ≠ бесплатно», s17 «consolidation как удар снизу») — корректно НЕ зачтены в strict-in. Каждый такой блок ≤2 предложений и смешан с positive capability content — это правильное применение strict-in правила «partial → как out». ✓

**Distribution across artefacts.** Chapter = 36.6%. Plan v2 declares slides = 41% strict-in, speech ≈ 47%. Все три артефакта ≥31%, разброс 36–47%. Single-cluster concentration risk = NONE. ✓

### 2. §3.x case structure (assertion-evidence-implication + Урок) — **PASS with one polish**

12 case-sections (§3.1 taxonomy + §3.2–§3.12 = 11 case-studies). Lessons count = **11** «Урок для инженера» — каждый case имеет explicit lesson line (§3.1 — taxonomy intro, корректно без lesson).

**Sample-check structure:**

| Case | Background | Mechanism | Outcome | Lesson actionability |
|---|---|---|---|---|
| §3.2 NYT (256w) | ✓ filing date, SDNY, partner Microsoft | ✓ memorization → regurgitation theory + concrete example «>90% identity» | ✓ 20M logs, SJ 2 апр 2026, trial конец 2026 | ✓ embedding similarity / Bloom filter — *concrete engineering technique* |
| §3.5 RIAA (304w) | ✓ filed 24 июня 2024, 2 параллельных иска | ✓ training+output similarity claim | ✓ Udio settled 29 окт 2025, Warner late 2025, Sony последний | ✓ «заложи licensing fees как expected cost; выбирай licensed-corpus provider» — *actionable for both vendor + deploy roles* |
| §3.8 Korea (260w) | ✓ контекст август 2024, журналисты обнаружили | ✓ source photo → face-swap → Telegram distribution, время = секунды | ✓ 6,500 takedowns / 16 prosecuted = 2% enforcement | ✓ «NSFW + age verification + reporting layer до launch — не after-patch» |
| §3.10 SI (295w) | ✓ ноя 2023, Futurism exposé, Arena Group / AdVon | ✓ purchased fake faces из marketplaces few dollars/face | ✓ articles удалены, SI Union «horror», brand equity снижен | ✓ «имя = реальный человек ИЛИ explicit AI-disclosure» |

Inженер-аудитория получает достаточный контекст в каждом случае. Background не overload'ит, mechanism всегда explicit, outcome with concrete numbers, lesson is operationalizable не «moralistic».

**Минор:** в §3.6 Thomson Reuters v Ross — «caveat: Ross — non-generative AI» хорошо выделен, но lesson «не строй product roadmap на assumption fair-use» можно конкретнее (концентрация в «expected liability в десятки млн долларов» — звучит как FUD, не как actionable measurement). **P2 — polish.**

### 3. LO coverage (LO1, LO2, LO4, LO5) — **PASS**

| LO | Coverage | Evidence |
|---|---|---|
| **LO1** (классификация 4 областей + named tools) | §0.3 cross-product матрица 3×4 + §1.1–§1.5 (видео: Sora 2 / Veo 3.1 / Kling 3.0 / Runway; §1.2 cameos / Omni Reference; §1.3 voice cloning ElevenLabs; §1.4 world models Genie 3) + §1.6 (Russian) — **named brand + capability-режим для каждого**. ✓ |
| **LO2** (оценка применимости + cost-quality-legal trade-off + mental model 3 семейств) | §0.1 fundamentals — 3 семейства technically explained + inженерные следствия каждого; §2.1 cost-collapse таблица 100×–10000× by asset-class. ✓ |
| **LO4** (landmark case анализ) | §3.2–§3.12 — 11 landmark cases с механизм + урок. ✓ |
| **LO5** (критерии «не нужен») | §4.1 — 4 критерия отказа (training-data license / output similarity / voice consent / brand-trust risk), §4.2 human-only zones, §4.3 YouTube empirical evidence, §5.1–§5.2 5-question checklist + mapping на 12 кейсов. ✓ |

Bloom-level fit для intermediate-level lecture (L8 не introductory): LO2 (Evaluate) + LO4 (Analyze) + LO5 (Evaluate/Apply) — все на correct cognitive level for L4+ industry lecture.

### 4. Keystone-axis usage — **PASS**

**§0.2 introduces ось «AI добавил → изменил → сломал»** ДО первого погружения в неё. Heading = название оси сама, не «recap Лекции 7» / «защита подхода». Первая строка («Структура этой главы построена на одной концептуальной оси…») подаёт ось как новое. ✓

**§0.3 «3 времени × 4 области»** cross-product matrix явно представлен таблицей 4×3 с примерами cells. Студент видит, что оси ортогональны, не дублируют друг друга. ✓

**Раздел 1 = «ДОБАВИЛ»**, **Раздел 2 = «ИЗМЕНИЛ»**, **Раздел 3 = «СЛОМАЛ»** — каждый раздел явно якорится на свою клетку оси. §6 Закрытие повторяет ось в trifold выводе («архитектурно / экономически / юридически»). ✓

Anti-pattern Лекции 4 «keystone всплывает в середине» — НЕТ. Anti-pattern «defensive recap вместо новой оси» — НЕТ. Anti-pattern «защита подхода вместо ось сама» — НЕТ.

### 5. Depth vs Lec-7 benchmark — **PASS**

| Metric | Lec-7 chapter | Lec-8 chapter |
|---|---|---|
| Total words | ~12,200 | 14,192 |
| Cases с 200–400 word narrative | (4 actor framework + Obermeyer + DSP-1181 + MASAI; ~300w each) | 11 cases × 256-304 words ✓ |
| Glossary | present | 18 терминов, 2-3 предложения each |
| Sources | 62 | 100+ ✓ |
| Self-check | per-section | per-section (5 blocks) ✓ |
| Cross-references | LO8-framing к L17 | L1+L3+L5+L7+L9 ✓ |

Lec-8 chapter — **deep reference + Q&A backup, не конспект** [[feedback-chapter-depth]]. Cases в §3 имеют full narrative с background / mechanism / outcome / explicit lesson — не compressed bullet-style. Объём 14k слов в верхней половине 12-14k target. ✓

### 6. Fundamentals §0.1 (P1.1 fix) — **PASS with polish**

3 семейства explained technically — diffusion forward/reverse, latent space + temporal consistency, autoregressive vs diffusion для audio. Каждое заканчивается «инженерным следствием»:

- **Diffusion → Firefly commercial-safety от corpus, не от architecture.** ✓
- **Latent video transformer → Sora 25-сек предел потому что cost linear на latent length + consistency degrades после ~25 sec.** ✓ *Это именно то, чего требовал Missing-Fundamentals check — student может предсказать, почему Sora имеет 25-sec ограничение.*
- **Neural audio synthesis → voice cloning из 1 минуты потому что fine-tuning, не from-scratch.** ✓

**P2 polish:** в §0.1 утверждение «temporal consistency degrades после ~25 секунд» — корректно как causal mechanism, но не цитируется источник (Sora System Card имеет это в общем виде; explicit 25-sec degradation — это inference). Можно добавить inline citation или hedge словами «emerging consensus from system cards». **P2 — polish, не fail.**

**P2 polish:** Stable Diffusion упомянут как «scraped-from-web» в §4.1, но в §0.1 это не введено. Связь corpus = commercial-safety vs scraped-from-web упоминается, но без явного контраста «Stable Diffusion ≠ commercial-safe» в §0.1. Студент должен сделать вывод сам. **P2 — polish.**

### 7. Russian context (§1.6) — **PASS**

Все ключевые игроки present:
- **Kandinsky 6.0 Image (28.04.2026)** ✓ + **Kandinsky 5.0 Video (18.11.2025, Apache 2.0)** ✓
- **Yandex Шедеврум (YandexART 2.7 / гибрид 3.0)** ✓
- **Sber SymFormer (Маэстро, 160k треков, Performer)** ✓
- **SaluteSpeech YourVoice + Yandex SpeechKit** ✓
- **Минцифры законопроект 18 марта 2026, в силу 1 сент 2027** ✓ — TDM-exception + маркировка + авторство у промпт-пользователя

**Урок «local convenience vs frontier»** сформулирован explicit и аргументирован: «концентрация фронтир-R&D в US/CN — **структурное** (capex, доступ к датасетам), **не идеологическое**». Эта формулировка — особенно сильная: она снимает defensive «отстали vs впереди» tone и заменяет на честный structural analysis. ✓

### 8. Cross-references quality — **PASS with one polish**

| Cross-ref | Presence | Tone |
|---|---|---|
| **Lec-1 «framing AI работает / не работает»** | §6 Заключение + introduction | Thin, как должно быть — углубление, не повторение ✓ |
| **Lec-3 архитектуры (Sora 2/Veo как API endpoints, Adobe Firefly Foundry / HuggingFace Spaces как платформенный слой)** | §0.1, §1.5, §3, §6 — 6 mentions | Тонко, без выноса архитектуры на текущий слайд (правильно, см. plan §4.7 justified rejection) ✓ |
| **Lec-5 financial-risk parallel (Сбер AI scoring → legal-risk debt в финансах vs Stable Diffusion → legal-risk debt в creative)** | §6 заключение | Параллель structural, не forced ✓ |
| **Lec-7 4-actor framework parallel** | §3.1 (artist/likeness — creator/training — victim/end-user — IP holder) + §6 заключение | Параллель тонкая, **НЕ делает explicit new framework на слайде** — правильно ✓ |

**P2 polish:** Lec-7 parallel в §3.1 («Параллель не строгая, но полезна для navigation») — формулировка хеджирована до «полезна», но student-инженер может пропустить значимость. Можно более concrete: «параллель указывает, что risk-actors в каждой индустрии — это разные leverage-points в legal framework». **P2 — polish.**

**P2 polish:** Lec-9 forward-reference в §6 («AI в авиакосмической отрасли») — упомянут, но без specific подготовки концепта. Это OK для финала главы, но можно добавить одну конкретную аналогию (например, «human-loop для high-stakes decisions, как мы видели в §4 для creative — будет fundamental для aerospace»). **P2 — polish (optional).**

### 9. Glossary §7 (18 терминов) — **PASS**

Каждое определение — 2-3 предложения, не 1-line. Sample-check:

- **#4 Diffusion model** — 3 предложения с примерами Stable Diffusion / Midjourney / DALL-E / Imagen / Firefly + cite Ho 2020 + Rombach 2022 ✓
- **#10 Slop** — **explicitly помечен «Colloquial term (Emily Bender, Gary Marcus 2024+)»** + academic synonym «low-quality synthetic content» ✓ (P2.3 fix applied)
- **#16 Fair use defence** — 3 предложения, включая 4-factor test reference + Andy Warhol v Goldsmith + Thomson Reuters v Ross ✓

Все 18 терминов используются в chapter narrative consistent с glossary definition.

### 10. Sources §8 quality — **PASS**

- **Total sources: 100+** ✓ (plan declared 80+, exceeded)
- **Volatile facts → `[VFY-day-of]`** — 14 occurrences в chapter body на specific volatile claims (Sora 2 versions / pricing, Suno SJ date, Sony litigation status, Andersen trial date, Kandinsky 6.0 benchmarks, Минцифры законопроект, YouTube data freshness, Google AI Ultra subscription, Adobe Firefly enterprise list, etc.) ✓
- **Academic papers cited:** Ho et al. 2020 (DDPM), Rombach et al. 2022 (latent diffusion), Shumailov et al. 2024 (Nature 631:755), Roediger & Karpicke 2006, Andy Warhol v Goldsmith 598 U.S. 508 (2023), Russell & Norvig (4th ed.) ✓
- **Industry sources:** Bloomberg Law, Bird & Bird, Mayer Brown, Davis Wright Tremaine, Reed Smith, Patent AI Lab, NPR, CNN, Variety, Hollywood Reporter, Marketing-Interactive, Futurum, IAB, Upwork, RIAA — diverse and authoritative ✓
- **Russian sources:** CNews, vc.ru, Habr, Sber Developers, GitHub kandinskylab, 4PDA, SHADR, Sostav — appropriate breadth ✓

---

## Anti-pattern grep (universal, ENFORCED)

| Pattern | Hits | Disposition |
|---|---|---|
| магическ\|спасёт\|революция | 1 hit | False positive — «...не строй на assumption "fair-use defence нас спасёт"» — это explicit warning AGAINST anti-pattern, не usage. ✓ |
| УГАДАЙ\|ребят\|короче | 0 | ✓ |
| рабочее определение\|прикладн\|режиме [A-Я] | 0 | ✓ Term Canonical-Validity check pass |
| инженер ИУ6\|студент Бауманки | 0 | ✓ Universal, no local binding |
| fucking sucks | 1 hit | Direct quote from Joe Russo (Avengers director) — cited reaction to Toys R Us Sora ad. Quotation marks present. Could remove or hedge. **P2.** |
| pornography / deepfake-porn | 4 hits | All in §3.8 Korea schoolgirl case + Cat.4 voice/likeness intro + sources. Topic-appropriate, sensitivity-handled (no visuals, just incident reporting). ✓ |

**Disrespectful CTA grep:** none. ✓
**Familiar tone grep:** none. ✓ Chapter использует ровный «вы»-tone throughout.

---

## P1 issues (3)

### P1.1 — Self-check для §5 missing
**Severity:** P1
**Issue:** Sections 0/1/2/3/4 имеют explicit `### Self-check (Раздел N)` blocks с 3-4 retrieval-questions. §5 «Что инженеру делать» — НЕТ self-check.
**Evidence:** `grep -c "### Self-check" chapter.md` = 5 (Раздел 0, 1, 2, 3, 4), но 6 разделов содержательных (0-5).
**Recommendation:** добавить self-check для §5 с 2-3 вопросами, проверяющими операциональность чек-листа. Примеры:
1. «Маркетолог планирует AI-generated holiday ad для legacy FMCG-бренда. Какие из 5 вопросов сразу же фейлятся? Что должен делать инженер на каждом fail?»
2. «Инженер deploys music-AI продукт для consumer. Какие 2 из 5 вопросов критичны? Какие конкретные tools / partners снижают risk?»
3. «Mapping table в §5.2 показывает 11 cases → checklist. Какой case был самый ‘ambiguous’ (multiple criteria) и почему?»

### P1.2 — «Урок для инженера» в §3.1 (taxonomy) отсутствует, но было бы методически polezno
**Severity:** P1
**Issue:** §3.1 «Авторское право — taxonomy 4 категорий исков» — это введение, после которого следует 11 case studies. Все 11 cases имеют explicit «Урок». Но сама taxonomy НЕ имеет concentrated lesson. Это создаёт inconsistency reading pattern — student ожидает урок (по pattern §3.2-§3.12), не получает.
**Evidence:** §3.1 заканчивается параграфом «Параллель не строгая, но полезна для navigation в legal-risk profile» — это бридж к Лекции 7, не урок из taxonomy.
**Recommendation:** добавить one-sentence concentrated lesson в стиле «Урок для инженера:» в конце §3.1: «4 категории — не academic классификация. Это четыре разных legal-mechanism, по каждому из которых надо проверить твой AI-workflow отдельно: пропуск любой из 4 категорий = blind spot в risk-profile.»

### P1.3 — Lec-9 forward-reference в §6 hangs without concept handoff
**Severity:** P1
**Issue:** §6 Заключение пишет «следующая лекция — AI в авиакосмической отрасли», но НЕ передаёт ни одной концептуальной нити, которая connect Лекцию 8 к Лекции 9. Это упущенная возможность handoff.
**Evidence:** §6 параграф «Что будет в Лекции 9» (lines 642): contrast statement only («creative broad-public-contact vs aerospace narrow-but-deep-stakes»), no actionable bridge.
**Recommendation:** добавить 1-2 предложения с явным concept handoff — например, «Концепт human-in-the-loop для high-stakes decisions, который мы видели в §4 как critère для creative (iconic / original direction), в Лекции 9 станет regulator-level requirement для AI в авиакосмической отрасли — это эскалация принципа от brand-trust к human-life accountability».

---

## P2 issues (8)

### P2.1 — Citation для «25-second degradation»
В §0.1 утверждение «temporal consistency degrades после ~25 секунд» — corollary из Sora System Card, но не explicit citation. Можно hedge или cite source.

### P2.2 — §0.1 не contrast'ит Stable Diffusion vs Firefly явно
Введение «scraped-from-web vs licensed corpus» происходит в §4.1, не в §0.1. Студент должен сделать вывод. Можно добавить one-line в §0.1.

### P2.3 — Lec-7 parallel formulation hedged
В §3.1 «Параллель не строгая, но полезна» — недо-actionable. Сформулировать concrete как «risk-actors = leverage-points в legal framework».

### P2.4 — Lec-9 forward-reference (см. P1.3)
P2 if P1.3 not accepted.

### P2.5 — Thomson Reuters lesson «десятки миллионов в expected liability» — FUD framing
В §3.6 lesson: «legal-risk exposure, оцениваемое в десятки миллионов долларов в expected liability». Это hyperbolic для unidentified «product roadmap». Можно скорректировать к «expected liability range depends on user base + corpus + jurisdiction — оценивай конкретно».

### P2.6 — «fucking sucks» quotation
В §3.11 цитата Joe Russo «fucking sucks» — точная цитата с attribution. Tone acceptable as direct quote, но для academic chapter можно paraphrase: «Joe Russo отзывался резко негативно: ‘fucking sucks’ (Hollywood Reporter)». Сейчас читается без adverbial dampening.

### P2.7 — §3.7 Arup mechanism mixes English/Russian неестественно
«CFO и colleagues в видеозвонке были deepfake» — стилистически smooth, но «деntрализированный finance worker» (line 432) — typo/garbled (likely meant «дезориентированный» или «doverчивый»). Single-word issue, easy fix.

### P2.8 — §5 «AI-pseudonyms» обозначен capital-A в §3.10, но lower-case в §5.2 mapping
Minor inconsistency в casing — «AI-pseudonyms» vs «AI pseudonyms» в нескольких местах.

---

## Cross-cutting strengths (worth highlighting)

1. **§0.2 keystone axis introduction** — exemplary keystone presentation. Заголовок про ось саму, первая строка про ось саму, явное rationale «почему именно эта ось» с anti-pattern callout («соблазн читать как топ инструментов»). Это benchmark для будущих L4+ industry lectures.

2. **§0.3 cross-product 3×4 матрица** — табличный визуал orthogonality двух таксономий — methodically очень сильно. Студент сразу видит, что области не дублируют времена.

3. **§1.6 Russian context — структурное vs идеологическое framing** — снимает defensive tone, заменяет на honest structural analysis. Это benchmark для будущих industry lectures.

4. **§5.2 mapping table «case → checklist criterion → engineering action»** — это **the payoff** chapter. 11 cases × 4 criteria → operational tool. Student-инженер получает actionable артефакт, не «обзор».

5. **«Урок для инженера» format на каждом case** — concise + actionable + measurement-oriented. Не «AI плохой», а «embedding similarity + Bloom filter» / «out-of-band verification» / «NSFW detection layer day-one».

---

## Sample-quote: 2 strong paragraphs

**Strong #1 — §0.1 (Latent video transformer follow-through):**
> «Sora 2 имеет 25-секундный предел не потому, что OpenAI "не доработали", а потому, что **cost scales линейно с latent length**, а **temporal consistency degrades после ~25 секунд generation horizon**. Иными словами, чтобы получить 90-секундное video через Sora 2, нужно генерировать четыре блока по ~22 секунды с дополнительным сшивающим механизмом — это не один model call, это pipeline.»

Это exemplary fundamentals: студент получает causal mechanism + numeric proxies + practical engineering consequence (pipeline of blocks vs single model call).

**Strong #2 — §1.6 Russian framing:**
> «Это сам по себе **honest takeaway**: концентрация фронтир-R&D в US/CN — **структурное** (capex, доступ к датасетам), не идеологическое.»

Honest, defensive-tone-free, technically grounded.

## Sample-quote: 2 weaker paragraphs

**Weak #1 — §3.6 Thomson Reuters Урок:**
> «Если твой product использует AI, обученный на large web corpus, имеет legal-risk exposure, оцениваемое в десятки миллионов долларов в expected liability в случае adverse ruling в любом из landmark cases.»

Это FUD framing без конкретики. Какие именно factors define exposure? Какой order of magnitude рассчитывается на конкретный product? Можно конкретизировать.

**Weak #2 — §6 Lec-9 forward-reference:**
> «Параллели и контрасты с Лекцией 7 (medical AI lives-at-individual-scale vs aerospace lives-at-systemic-scale) и с Лекцией 8 (creative AI broad-public-contact vs aerospace narrow-but-deep-stakes) сформируют framework для лекций 9–17.»

Это generic «coming attractions» line без actionable handoff. Какой именно concept из L8 будет foundational для L9? Можно одну line specific bridge.

---

## Топ-N правок (приоритизировано)

1. **(P1.1)** Добавить self-check блок к §5 — 2-3 retrieval questions про чек-лист applicability. *15 минут.*
2. **(P1.2)** Добавить one-sentence «Урок для инженера» в конце §3.1 (taxonomy) — для consistency reading pattern. *5 минут.*
3. **(P1.3)** Усилить Lec-9 handoff в §6 с одной concept-bridge sentence (human-in-the-loop escalation from brand-trust to human-life accountability). *5 минут.*
4. **(P2.5)** Скорректировать Thomson Reuters lesson — убрать «десятки миллионов» FUD-framing, дать factor-based hedging. *3 минуты.*
5. **(P2.7)** Исправить typo «деntрализированный» в §3.7 Arup. *1 минута.*
6. **(P2.6)** Опционально: hedge «fucking sucks» цитату Joe Russo с adverbial framing. *2 минуты.*
7. **(P2.1, P2.2, P2.3, P2.4, P2.8)** Optional minor polishes — citations, contrast statements, casing. *10 минут total.*

---

## Final verdict rationale

Chapter v1 — **strong draft**, clears all 10 ENFORCED checks. 3 P1 issues все локальные (one missing self-check, one missing taxonomy lesson, one weak forward-reference) — не структурные. P2 issues — pure polish (citations, hedging, typo).

**Failure/judgment ≥30% strict-in cleared с 6.6pp margin — single-cluster concentration absent (chapter / slides / speech все ≥31%).** Keystone-axis exemplary. Fundamentals §0.1 — методически образцовая. Russian context — honest, не defensive. Cross-references — thin & well-targeted (не делают explicit new frameworks где не надо).

**Counter-check verdict applied:** 3 P1 ≤ 4 → **APPROVE-WITH-POLISH**, не REVISE. Полировка завершается в ~40 минут book-editor revision; затем chapter готов для USER GATE A.

*Конец methodology-critic report.*

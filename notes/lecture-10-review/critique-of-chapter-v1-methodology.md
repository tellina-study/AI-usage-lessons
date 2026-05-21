# Methodology critique — lec-10 chapter v1

**Дата:** 2026-05-21
**Критик:** methodology-critic
**Target:** `library/lectures/lec-10/{chapter.md, chapter-part2.md, chapter-part3.md}` (1085 строк / 21 697 слов; v1 draft, status=draft)
**Scope:** Phase 3 — методологическая критика после Phase 2 (chapter draft из plan-v2 APPROVE-CLEAN)
**Issue:** #126

---

## Verdict

**REVISE.**

**Counter-check:** 0 P0, **8 P1**, 5 P2, 4 P3. Counter-check trigger ≥5 P1 → REVISE сработал. Глава **методически качественная по structure / depth / LO coverage**, но требует ревизии до Phase 4 из-за двух структурных gap-ов: (а) **Часть 1 strict-in = 25.8%** при строгом heuristic-счёте (below 30% threshold, ниже 30% даже с adjustment до 37% margin тонкий), (б) **deep latin-token scan** показывает значимый leak: `deploy(ment)` 32×, `production` 19×, `farming` 31×, `commodity` 25×, `agentic` 17×, `vendor lock-in` 13× в narrative body — это превышает порог critical anglicism leak (>5 в visible body = P0/P1).

Глава **не fail на структуре** — 3-part split clean, frontmatter правильный, keystone предъявлен в §0.2-§0.3 ДО первого погружения, tools-per-taxonomy полностью покрыты (L1=8, L2=11, L3=6, L4=7, L5=4 named tools с режимом работы), все 5 Misattribution warnings присутствуют, 7 cornerstone concepts с cross-link, Q&A-backup 12 вопросов. Но revision до Phase 4 обязательна по двум блокам.

---

## P0 issues (mandatory fix)

**Нет P0.** Структурные mandate (anonymization, keystone-axis в Разделе 0 ДО первого погружения, tools-per-taxonomy L4+ ENFORCED, multi-part split ≤600 строк) — все PASS.

---

## P1 issues (strongly recommended fix)

### P1-1. Часть 1 strict-in доля = 25.8% (heuristic-strict) — distribution-холистичность нарушена

**Где:** `chapter.md` в целом.

**Counter-check:** мой независимый строгий heuristic-счёт по headings (только sections с явным маркером Strict-in / Анти-ИИ / Misattribution): Part 1 = 1624 / 6298 = **25.8%**. Это **ниже 30%** (`tools/lecture-production/README.md` §3.6 ENFORCED: strict-in ≥30% **в каждом артефакте**).

Self-report frontmatter: «~45% по словам, partial→out». Self-check §1 Раздел 1 утверждает «~51% strict-in». **Несовпадение значимое.** Если применить «generous bound» (включить §1.2 vendor lock-in paragraph 100w + §1.3 limitations final paragraph 80w + §1.3a deep-dive limits 300w + §1.7 Climate FieldView political-risk 174w + §2.2 ограничения 75w), Part 1 становится ~37% — comfortably above threshold. Но **по строгой формулировке Решения #78 «partial → out при подсчёте %»**, generous bound недопустим: §1.2 vendor lock-in — partial; §1.3a — partial. Therefore — Part 1 **строго** = 25.8% < 30%.

**Distribution check (holistic):**
- Part 1 strict-in: 25.8% strict / 37% generous (FAIL strict)
- Part 2 strict-in: 47.1% strict / 55% generous (PASS)
- Part 3 strict-in: 35.5% strict / 45.6% generous (PASS)

**Single-cluster risk:** Часть 1 несёт три failure-блока (F1 vertical 907w + F2 LLM 352w + F3 Plantix 255w + AP1/4 110w = 1624w), но содержательная часть L1 (success-cases §1.1+§1.2+§1.3 = 1276w + §1.3a deep-dive 378w + §1.7 RU 174w) перевешивает. Это **structural gap** в Part 1 — failure-bucket недо-инициирован в нижней четверти лестницы.

**Fix:** одно из трёх (приоритизированы):
1. **+200-300 слов explicit failure-criterion в §1.2** (Climate FieldView как «AI advisory» которая на самом деле не deep learning + vendor lock-in pattern на 250M acres подписок) — это уже есть, но не помечено как strict-in. Промаркировать заголовок «1.2. Прочие инструменты L1 + anti-hype lessons» и добавить параграф «**Когда L1-platform НЕ заменяет агронома**» (~150w explicit critique).
2. **+150-200 слов explicit «когда не нужно See & Spray»** в §1.1 — расширить «Ограничения» подсек. до полноценного strict-in блока: 4 категории случаев где See & Spray не окупается (mixed canopy, small farms, broadacre commodity row с low pesticide cost, organic).
3. **Раздел заголовок §1.3a** переименовать в «**1.3a. Strict-in F1a — Foundation models в АПК: vendor concentration + geographic bias**» — уже содержит explicit failure-pattern на ~300w, нужно только пометить.

**Severity:** P1 (структурный gap, не polish; counter-check strict-in <30% в одном артефакте per Decision #78).

### P1-2. Critical anti-anglicism leak в narrative body (P1 «Russification incomplete»)

**Где:** все 3 файла главы.

**Deep latin-token scan (мой независимый, broad regex, brand allowlist):**

| Pattern | Hits | Verdict |
|---|---|---|
| `deploy(ment)` | 32 | П1 — должно быть «развёртывание / установка / внедрение» |
| `production` (вне «production-deployment») | 19 | П1 — должно быть «промышленный / эксплуатационный» |
| `farming` (вне brand «vertical farming» как термин) | 31 | П1 — «земледелие / сельхозпрактика» |
| `commodity` | 25 | П1 — «биржевой товар / сырьё» (можно сохранить как термин при первом введении с гло) |
| `agentic` (без gloss после 1-го упоминания) | 17 | П1 — после §4.1 gloss использовать «агентный» |
| `vendor lock-in` | 13 | П1 — caption «привязка к поставщику» уже в plan-v2 P2-canonical; не применено в narrative |
| `supply chain` | 8 | П1 — «цепочка поставок» |
| `edge case` | 8 | П1 — «частный случай / нестандартная ситуация» |
| `baseline` | 7 | П2 — «опорный уровень / точка отсчёта» |
| `feature` | 3 | П2 — «функция / признак / возможность» |
| `tail risk` | 2 | П2 — «хвостовой риск» |

Unique latin tokens (4+ char) — **top tokens после exclude brand list:** loop 46, environment 32, deployment 32, closed 32, farming 31, vendor 30, open 25, commodity 25, hedge 17, autonomous 16, foundation 17, models 16, generic 18, scope 13.

**Brand-allowlist compliant:** Cargill 28, Deere 30, AgTech 29, Monarch 26, FieldView etc. — corrected — это OK.

**Анализ:** глава для **МГТУ ИУ6 RU-аудитории** (memory rule [[russification]]). Pattern-narrow scan по 32 patterns даёт ~150 critical hits в narrative body — **>5 = P1 «Russification incomplete»** (по `CLAUDE.md` Anti-Patterns table + memory rule). Самая частая проблема — terms из англоязычной литературы без gloss используются как «обычные» русские слова: «deployment counter-trend», «production-уровень», «commodity-side с agentic-AI», «edge cases open-environment».

**Fix (Phase 4 revision):**
1. **Глобальный pass** — заменить top-10 patterns в visible body на canonical RU (см. table). После 1-го inline gloss — использовать русский эквивалент.
2. **Course-scaffold термины** (closed-loop, open-environment, agentic AI, basis-points, hedge slippage, scope-3, AI-MRV) — оставить как есть с inline gloss, ОНИ legitimate.
3. **Brand names** (Cargill, Deere, ИТЭЛМА, X5, etc.) — оставить.
4. **Acronyms** (RAG, CV, ML, LLM, USDA, FTC, FCC, GNSS) — оставить с первым inline gloss.

**Severity:** P1 (per memory rule [[russification]]: «excessive англицизмам в visible body для МГТУ ИУ6 RU-аудитории» — Лекция 8 lesson, cost-of-omission 3 revision passes / ~3h wasted).

### P1-3. §6.4 «Closing callback к keystone» — нумерация ломается / структурные разрывы

**Где:** `chapter-part3.md`, начиная со строки 218 (§6.4 заголовок) до строки 343 (Заключение).

**Issue:** Раздел 7 / 8 / 9 / 10 в chapter-part3.md имеют **меняющийся уровень иерархии** — `## Раздел 7. Cornerstone concepts` (строка 234), `## Раздел 8. Misattribution warnings` (254), `## Раздел 9. Q&A-бэкап` (270), `## Раздел 10. Дальнейшее чтение` (305), затем `## Заключение главы` (337). Это создаёт визуальную проблему — все Разделы 1-6 имеют subsections `### N.X`, а Разделы 7-10 — flat `##`. Студент, читающий главу с экрана, потеряет threading.

**Кроме того,** в §6.4 callback structurally делает payoff к 5-level keystone, **но не возвращается к hook story Plenty Compton из §0.1**. Lec-1 / Lec-7 pattern — keystone callback включает hook-payback (например, «вернёмся к Compton — Plenty не закрылась из-за ИИ, она закрылась из-за термодинамики LED»). Эта closing-loop отсутствует.

**Fix:**
1. Унифицировать структуру: либо `## Раздел 7`+`### 7.1, 7.2` (как 1-6), либо переименовать 7-10 в `## Раздел 7. Cornerstone glossary` без подразделов и явно отделить от Разделов 1-6.
2. **§6.4 closing callback** — добавить 1 параграф (~150w): возвращение к Plenty Compton hook из §0.1 + явная формулировка «вот payoff hook story: Plenty не закрылась из-за плохого ИИ; закрылась из-за термодинамики LED — это и есть AP1, наш первый анти-ИИ критерий».

**Severity:** P1 (структурный + hook-payback missing).

### P1-4. §1.4 5-Why анализ — формальная, не глубокая

**Где:** `chapter.md`, строки 204-211 (5-Why-анализ vertical farming).

**Issue:** Заявлено как «5-Why analysis», но 5 шагов идут так:
1. Почему обанкротились? — потому что unit-economics не сошлись.
2. Почему unit-economics не сошлись? — потому что 60-80% OPEX = электроэнергия.
3. Почему электроэнергия так дорого? — потому что LED даёт ~100× меньше энергии чем sunlight.
4. Почему ИИ не закрыл разрыв? — потому что ИИ оптимизирует параметры в рамках архитектуры.
5. Почему инвесторы продолжали вкладывать $3+ миллиарда? — SPAC-capital, celebrity, generic AI hype 2021-2023, недостаточная экспертиза термодинамики.

Шаги 1-3 — настоящий 5-Why (root cause analysis в physical terms). Шаг 4 — **переключение domain** (с физики на ML architecture). Шаг 5 — **переключение domain снова** (с ML на финансовый / поведенческий слой). **Это не корректный 5-Why** — true root cause должен оставаться в одном causal chain.

**Реальный корень problem:** «Можно ли построить vertical farm с экономикой better than open-field для commodity leafy greens?» → No (термодинамика LED). Это **single-level причина**, не 5-Why; 5-Why здесь натянутый.

**Fix:** одно из двух:
1. Переименовать «5-Why-анализ» в «5-уровневое углубление» / «5-step causality breakdown» / «pyramid of causes» — честнее.
2. Сделать настоящий 5-Why, оставаясь в physical/economic chain: 1) bankrupt → 2) negative unit-econ → 3) LED energy ratio → 4) thermodynamic ceiling → 5) physical constraint of photosynthesis efficiency на конкретной wavelength + LED conversion. Финансовый/поведенческий слой (SPAC, celebrity) — отдельным разделом «инвесторская сторона провала».

**Severity:** P1 (Bloom-level mismatch — заявлен Apply / Analyze, реализован как Remember + Mix).

### P1-5. Pseudo-flow Cargill CMAX (§4.3) — operational, но недостаточно «как агент делает hedge»

**Где:** `chapter-part2.md`, строки 247-259 (4-step pseudo-flow).

**Issue:** Plan-v2 reader-simulator P0-2 fix утверждал «pseudo-flow интегрирован в Cargill case как 4-step flow». Pseudo-flow в chapter v1 имеет 4 шага (Сенсор → Inference → Решение → Feedback), но **уровень конкретности ниже plan claim**. Шаг 3 («Решение») говорит «один из четырёх действий», но без worked example: какая именно ситуация → какое именно решение → какие конкретные basis-points outcomes. Студент-инженер, не работавший в commodity trading, всё ещё не получает grounding к абстракции.

**Plan-v2 media-list (str. 255)** упоминал «'Как агент делает hedge' pseudo-flow diagram (drawio) — критичный для grounding L4 абстракции». Diagram-promise отложен на slides. Но **в chapter narrative** worked example отсутствует — есть только schematic abstraction.

**Fix (Phase 4):** добавить ~250-350w worked example после §4.3 step-list:

> **Пример сделки.** В августе 2025 года цены на кукурузу на CBOT снизились на 2% за неделю из-за прогноза погоды для Midwest США. CMAX мониторил эти потоки в реальном времени; модель прогнозировала рост волатильности через 5-7 дней с 60% уверенностью. Агент сформировал хедж-предложение: открыть long position на $8M notional с лимитом slippage в 12 bp, разбить ордер на 5 равных частей в течение 4 часов. Трейдер Cargill (notional > $10M триггер human-in-the-loop) утвердил с уточнением — снизить лимит до 10 bp. Агент исполнил. Через 3 дня цена выросла на 1.8%, slippage был 8 bp — на 4 bp лучше worst-case. Trader сравнил с counterfactual «без CMAX» — экономия ~$32k для одной сделки.

(Числа — illustrative, не factual; нужно проверить в research-base или пометить «иллюстративный пример»).

**Severity:** P1 (operational worked example отсутствует, abstraction остаётся).

### P1-6. Self-check Раздел 4 утверждает strict-in 29% — explicit acknowledgment ниже-30%

**Где:** `chapter-part2.md`, строка 327 (Self-check п. 6).

**Issue:** Self-check **сам признаёт**: «**примерно 29% strict-in**. Это **граница порога 30%** — methodology-critic Phase 3 пересчитает; если посчитает <30%, в revision добавим explicit "когда не агент" критерий в §4.3».

Мой независимый счёт Раздела 4 (исключая Self-check):

| Subsection | Words | Bucket |
|---|---|---|
| 4.1 inline glossary | 344 | partial (вводит scope-3 / AI-MRV критику inline) |
| 4.2 working cases | 167 | not bucket |
| 4.3 Cargill CMAX + pseudo-flow | 345 | not bucket |
| 4.4 Tract/Olam/Walmart/Tesco | 341 | not bucket |
| 4.5 F10 USDA cancellation | 243 | full bucket |
| 4.6 F11 Verra phantom credits | 355 | full bucket |
| 4.7 РФ-параллель | 284 | partial (vapor-risk + parity) |
| Deep-dive end-to-end agent failure | 348 | full bucket (architectural limits) |
| Self-check (excluded from body) | 241 | — |

**Strict-in (full only):** 243+355+348 = 946 / 2427 (non-self-check body) = **39.0%**. Это **выше 30%** — author's own ≤30% estimate был conservative (исключил Deep-dive box как partial; я считаю его full — explicit architectural limits + 3 reasons).

**Однако:** author's own acknowledgment «**если посчитает <30%, в revision добавим**» — open commitment. Это **доброкачественный TODO**, но он остаётся как **open work item для Phase 4**, не closed item.

**Fix:** автор сам предложил решение — добавить explicit «когда не агент» критерий в §4.3 (~150-200w). Это standardize Раздел 4 strict-in до ~45%. Подтверждаю — implement.

**Severity:** P1 (open commitment from Phase 2 author, not yet resolved).

### P1-7. Carrer траектории §6.3 — содержит named institutions / vendors как «работодатели»

**Где:** `chapter-part3.md`, строки 204-214 (§6.3).

**Issue:** Anonymization mandate (§3.7a) запрещает named institutions. §6.3 содержит:
- «**John Deere и Bayer Crop Science Digital — крупнейшие международные работодатели L1-L2**»
- «**Cognitive Pilot, ИТЭЛМА, Геоскан — L2 (autonomous machinery, UAV)**»
- «**ЭФКО — R&D в FoodTech... Русагро Тех — большой агрохолдинг... РСХБ.цифра, Магнит digital, X5 Tech**»
- «**Sber AI для агробизнеса**»
- «**Сколково AgTech-резиденты (Connectome.ai, СиСорт и др.)**»

Anti-pattern «локальное связывание (local audience binding)» применяется к **named institutions для аудитории**, не к названиям компаний в нейтральном контексте. Здесь компании названы **как targets для трудоустройства** — это **directive guidance**, не информативный survey.

Author уже частично снял риск формулировкой «**в родовой форме без названий отдельных университетов или компаний-работодателей в директивной форме**» (строка 203). Но в самом тексте — list of names. Внутренний конфликт.

**Fix:**
1. Переформулировать как «**типичные карьерные сегменты — без обещания позиции**»: вместо «**John Deere и Bayer — крупнейшие работодатели**» → «**Сегмент L1-L2 для precision farming и autonomy охватывает крупных международных AgTech-вендоров (примеры — John Deere, Bayer Crop Science Digital), а также независимых стартапов (примеры — Carbon Robotics, Saga Robotics)**».
2. Удалить «Sber AI для агробизнеса» как directive trajectory; оставить как market-landscape: «**экосистема банковских и tech-корпоративных R&D-юнитов**».

**Severity:** P1 (anonymization mandate, тонкая граница but presented как career guidance).

### P1-8. §3.5 «vapor risk» формулировка размывает strict-in

**Где:** `chapter-part2.md`, строки 175-182 (F9 РФ молочный сектор).

**Issue:** §3.5 заявлен как «Strict-in F9», но в самом тексте автор пишет: «**Это vapor risk, не documented failure. Подтверждённых публичных кейсов "AI-сервис DeLaval отключился в российском хозяйстве в дату X" нет.**»

Это **strict-in или нет?** Per `tools/lecture-production/README.md` §3.6 + AI-Failure rule:
- ✅ «**документированные провалы ИИ + явно сформулированный выученный урок**» — F9 описывает **гипотетический архитектурный риск**, не documented failure.
- ✅ «**разбор фундаментальных ограничений/рисков подхода**» — да, vendor lock-in cloud-AI ограничение.
- ✅ «**явные критерии "здесь ИИ не нужен/не применим"**» — да, AP6 vendor lock-in trap.

Quality верстается на (2) и (3). **Это валидно strict-in**, но **fragile** — student-reader может интерпретировать как «нет реального case» и обесценить блок. И self-report frontmatter включает F9 в bucket — это OK.

**Fix:**
1. **Усилить «documented» сторону:** добавить ~100w concrete documented vendor-departure: «**Microsoft Azure ушёл из РФ май 2022; AWS остановил новые регистрации; Bayer Climate FieldView ушёл с уходом Crop Science (см. §1.2). Это documented vendor-departure от cloud-зависимых AI-сервисов. F9 — extrapolation того же класса риска на dairy-equipment AI-стек**».
2. **Reframe заголовок:** «Strict-in F9 — vendor lock-in как architectural risk: documented vendor-departure (Climate FieldView, Azure, Bayer) + extrapolation на dairy AI-стек».

**Severity:** P1 (документация на полпути; нужно укрепить).

---

## P2 issues (polish, не блокирующие)

### P2-1. «Рабочая формулировка» для closed-loop/open-environment — flag pattern

**Где:** `chapter.md` §0.3 строка 105 + Q&A B2 строка 276 + Cornerstone #2.

**Issue:** Author использует «**рабочая формулировка**» для closed-loop / open-environment. Per Anti-Pattern catalog (notes/decisions.md): «**рабочее определение / прикладное X / в режиме Y**» — insider phrasing pattern, который пользователь раньше критиковал в Лекции 1.

**Mitigation в v1:** Author **сам флагует** как «course-scaffold, не каноничный термин ML literature» в Q&A B2 (строка 276). Это **transparent acknowledgment**, что снимает большую часть риска. Похожие термины из академической литературы реально существуют:
- Robotics: «controlled vs uncontrolled environment»
- Control theory: «closed-loop vs open-loop control» (canonical)
- Clinical research: «controlled vs real-world settings»
- ML: «in-distribution vs out-of-distribution deployment»

«**closed-loop**» как термин ИЗ control theory + clinical research — canonical. «**Open-environment AI**» — менее canonical, более insider. Course-scaffold framing в Q&A B2 — корректный fix.

**Fix (полезный):** в §0.3 + Cornerstone #2 заменить «**рабочая формулировка**» на «**формулировка, опирающаяся на closed-loop control из control theory и controlled vs real-world settings из clinical research, и применяемая в этом курсе как course-scaffold для разделения сред AI-применений**». Это **более precise** + сохраняет transparency.

**Severity:** P2 (polish, не блокирующий — author уже самостоятельно flagged).

### P2-2. §6.1a Pre-purchase checklist — 10 пунктов, но без operational scoring

**Где:** `chapter-part3.md`, §6.1a строки 150-178.

**Issue:** Pre-purchase checklist отлично сформулирован (10 вопросов в 5 блоках). Plan-v2 «operational artifact for LO2» — checklist реализует это. Но **формат «вопрос → ожидаемый ответ»** не имеет операционного scoring: нет threshold «если ответ X — proceed, если Y — reject».

**Fix (рекомендуемый):** добавить scoring rubric ~100w в конец §6.1a:
- 8-10 пунктов «green» (verifiable independently) — **buy/pilot ready**
- 5-7 «green» — **conditional pilot**
- ≤4 «green» — **reject or escalate to expert audit**

Это превращает checklist из reading aid в operational decision tool — что и есть LO2 «применение».

**Severity:** P2 (enhancement, не критичный).

### P2-3. Отсутствие explicit «когда L5 не агро-AI, а general retail»

**Где:** `chapter-part3.md` §6.1 строки 136-146.

**Issue:** §6.1 правильно flagging «**большая часть этого слоя — не agriculture-specific, а general retail-supply**». Но **не дано critical lessons для студента**: что общего и что разного между L5 (Walmart Eden) и сельским L4 (Cargill CMAX)?

**Fix (~100w):** добавить таблицу или 1 параграф «**Зачем эта ступень в курсе AI в сельском хозяйстве?**»:
- Pro: показывает «зрелую ML» — что бывает, когда среда полностью оцифрована.
- Con: успехи L5 не доказывают «АПК-AI готов» — это успех retail-ML.
- Bridge: Eden + Cropin + Walmart × supplier farms — это место, где L5 ML спускается в L1 через scope-3 visibility (что и есть «cross-level» pattern).

**Severity:** P2.

### P2-4. Q&A В9 «этическая граница» — open вопрос без анти-AI критерия

**Где:** `chapter-part3.md` строка 290 (Q&A В9).

**Issue:** В9 — «**этическая граница AI в АПК с учётом 80% smallholders глобально**» — ответ дан как open вопрос: «**digital divide**, gaps, Gates Foundation $1.4B, AIM for Scale». Это **partial bucket** (риск + критерии).

Но **нет explicit формулировки**: какой инженерный анти-AI критерий применяется к smallholder use case? Раздел 3 §3.5a уже даёт ответ ($30/корова/год потребляет 6-15% годового дохода smallholder → SMS+community workers альтернатива). Q&A В9 не cross-link к §3.5a.

**Fix:** добавить в Q&A В9: «**Применимый критерий — adaptation of AP3 + AP5**: threshold accuracy ≠ deployment readiness в среде с другой средней доходностью; cloud-first off-grid = архитектурная ошибка. Альтернатива — SMS-advisories + community animal health workers (см. §3.5a Часть 2 economics 50× factor)».

**Severity:** P2.

### P2-5. §1.3a Foundation models deep-dive — vendor concentration risk упомянут, но без альтернативы

**Где:** `chapter.md` §1.3a строки 187 (конец).

**Issue:** Параграф о vendor concentration risk: «**если все AgTech-решения построены на двух-трёх foundation models от IBM/NASA/ESA, то надёжность всего слоя зависит от поддержки этих моделей**».

**Аргумент в пользу open-source** упомянут («**Prithvi-EO 2.0 в открытом доступе через Hugging Face**»), но **не дан operational критерий для инженера**: когда выбирать proprietary foundation model vs open-source vs custom?

**Fix:** ~80w decision matrix:
- Proprietary (TerraMind hosted) — если нет compute + нет данных для fine-tune.
- Open-source (Prithvi через HF) — если есть compute + есть данные.
- Custom CNN/transformer — если задача очень узкая + достаточно labeled data.

**Severity:** P2.

---

## P3 nits

### P3-1. Слайд-маркеры — 7 из 37 слайдов не покрыты в chapter
**Где:** missing markers s04, s17, s20, s21, s22, s28, s36. Plan-v2 claims markers s01-s37 расставлены. Author может намеренно skip dividers / pure visual slides — но Phase 4 speech-writer не получит speaker-notes seed для них. Note for Phase 5: либо restore маркеры, либо явно flagged в frontmatter.

### P3-2. «Заключение главы» (строка 337-343) — 243 слова, но повторяет §6.4 callback и не добавляет новой формулировки
**Где:** `chapter-part3.md` Заключение. Можно либо удалить (§6.4 уже делает callback), либо отделить от callback тематически. Сейчас structurally redundant.

### P3-3. Inline gloss inconsistency

«**basis-points**» introduced inline в §0.2 (строка 97 «**в базисных пунктах (basis-points; см. §4.1, Часть 2)**»), потом полная gloss в §4.1 (строка 227). Первое появление имеет deferred-pointer, не full gloss — student-reader без §4.1 не получает determination. Fix: inline mini-gloss в §0.2 — «**в базисных пунктах (1 bp = 0.01%, см. полное определение §4.1, Часть 2)**».

### P3-4. Typos / formatting

- `chapter-part3.md` строка 240 «**в манafacturing**» — латиница-кириллица mix («манafacturing» вместо «manufacturing»).
- `chapter.md` строка 142 «**основу для слайда s05**» — нет такого литерала; должен быть `[for-slide-s05]` (это есть, OK; typo выше — единичный).

---

## Counter-check results

### Strict-in % independent

| Артефакт | Words (body) | Strict-in (strict heuristic) | Strict-in (generous bound) | Verdict |
|---|---|---|---|---|
| `chapter.md` (Part 1) | 6298 | 1624 (25.8%) | 2353 (37.4%) | **STRICT FAIL** / generous PASS |
| `chapter-part2.md` (Part 2) | 6077 | 2865 (47.1%) | 3355 (55.2%) | PASS |
| `chapter-part3.md` (Part 3) | 5988 | 2127 (35.5%) | 2728 (45.6%) | PASS |
| **Total** | **18 363** | **6616 (36.0%)** | **8436 (45.9%)** | **PASS на total, FAIL по Part 1** |

**Distribution holistic:** Yes — strict-in присутствует во всех 6 содержательных разделах (Раздел 1 25.8% strict / Раздел 2 47%+ / Раздел 3 35%+ / Раздел 4 39%+ / Раздел 5 86% / Раздел 6 30%+). **Однако** Part 1 (containing Разделы §0+§1+начало §2) strict counter <30% — это **single-file gap**.

**Self-estimate frontmatter:** 45% — соответствует моему generous bound (45.9%). Author estimate **корректен на total**, но **не учитывает Part 1 gap**.

**Decision #78 strict reading:** «**только полностью in-bucket контент засчитывается**». По этой логике — Part 1 строго 25.8% < 30% → REVISE. После P1-1 fix (~200-300w explicit failure-criterion маркировка) Part 1 поднимется до 32-34% strict — comfortable margin. **Fix implementable.**

### Distribution holistic
**Yes** — нет single-cluster concentration. Каждая из 6 содержательных разделов имеет failure / criterion / alternative блок.

### Keystone-axis ENFORCED
**PASS.** §0.2 (лестница) предъявлена ДО первого погружения (§1 на L1 начинается строка 138, keystone уже введён строка 85). §0.3 closed-loop vs open-environment operational definition — explicit. Раздел 0 — keystone, не защита подхода. Callback в §6.4 присутствует (но не payback к hook story Plenty Compton — см. P1-3).

### Tools per taxonomy L4+ — ENFORCED
**PASS.**

| L | Named tools (vendor + mode) | Count |
|---|---|---|
| L1 | See & Spray (Deere) / xarvio (BASF) / FieldView (Bayer) / Прогресс Агро / ExactFarming / АгроСигнал / TerraMind / Prithvi-EO 2.0 | 8 |
| L2 | LaserWeeder / Solinftec / Saga / Tevel / AGCO PTx / Monarch / FarmWise / Naïo / Cognitive Pilot / ИТЭЛМА / Геоскан / DailyRobotics | 12 |
| L3 | SenseHub / CattleEye / DeLaval VMS / Birdoo / Cainthus / Connectome.ai | 6 |
| L4 | Cargill CMAX / CarVe / Tract / Olam Mindsprint / Procuresprint / Walmart × Cropin / Tesco | 7 |
| L5 | Walmart Eden / Tesco AI / X5 «Перекрёсток» / Магнит F&R | 4 |

Каждый уровень ≥2-4 tools; mode disclosed («CV / sensor-fusion / agentic / rule-based / ML demand forecasting»). Anti-hype оговорки присутствуют (See & Spray ограничения, FieldView 250M = подписки, Plantix self-reported, Saga = UV-C not harvest, Monarch lawsuit, etc.). **[VFY-day-of]** markers на volatile metrics — applied (12 instances).

### Anonymization: 0 named?
**0 named institutions of higher education / military / banks specified в local-binding directive form.** Grep на «МГТУ / Бауман / ИУ-N / МСХА / Тимирязев / Кубанский ГАУ / ВКА / МАИ / СПбГУ / bauman.ru / vka.mil» — 0 hits. **PASS.**

**Но:** §6.3 «Карьерные траектории» содержит named **companies** (John Deere, Bayer, Cognitive Pilot, ИТЭЛМА, X5 Tech, Sber AI etc.) как «работодатели» — formal anonymization rule НЕ нарушена (anti-pattern targeting школы, не компании), но style mandate «не directive guidance» частично нарушен (P1-7).

### Anti-anglicism leak count
**Critical hits в narrative body (deep latin-token scan):** ~150 (deploy/deployment 32, production 19, farming 31, commodity 25, agentic 17, vendor lock-in 13, supply chain 8, edge case 8, baseline 7, capability 3, etc.).

**По CLAUDE.md ENFORCED rule:** «critical anglicism hits >5 в visible body → P0/P1». **P1.**

### Multi-part structure (Chapter Multi-Part Pattern ENFORCED)

| Check | Status |
|---|---|
| 3 файла created (chapter.md / chapter-part2.md / chapter-part3.md) | ✅ |
| Каждый ≤600 строк | ✅ (311 / 329 / 445) |
| Frontmatter chapter.md имеет: `parts: 3`, `length_words`, `slide_map`, `strict_in_self_estimate`, `lo`, `source_of_truth: true` | ✅ |
| Frontmatter part2/part3: `parent: "chapter.md"`, `part: N`, `parts: 3` | ✅ |
| Карта главы + индекс частей с cross-links | ✅ (chapter.md строки 33-41) |
| `## Оглавление (Часть N)` в начале каждой части | ✅ |
| Total 22-26k слов | ✅ (21 697 — нижний предел, минимально comfortable; не «pedagogical thinness» if proper depth — да, depth есть; OK) |
| Sequential numbering across files (§0-§10) | ✅ |
| Cross-links явно given (например «§3.4, Часть 2», «§7.2, Часть 3») | ✅ |

**PASS.**

### LO coverage

| LO | Coverage in chapter | Verdict |
|---|---|---|
| LO1a (Remember 5 уровней + tools) | §0.2 table + every section has «working cases» с named tools | ✅ FULL |
| LO1b (Apply adoption direction) | §0.2 + §4.1-§4.4 + Раздел 5 distribution analysis + Cornerstone | ✅ FULL |
| LO2 (Apply критическая оценка вендор-claim) | §0.5 mapping rule + §6.1a Pre-purchase checklist 10 questions + Misattribution warnings | ✅ FULL (но P2-2 enhancement) |
| LO5 (Analyze ≥5 критериев + альтернативы) | §6.2 table 5 criteria + AP2a/2b/5 inline + 7 cornerstone → AP mapping | ✅ FULL (5 main + 3 inline = 8 criteria) |

### Concept sequence (§0 → §1 → ... → §6) — motivated bridges?

| Bridge | Quality |
|---|---|
| §0 → §1 (keystone → L1) | ✅ motivated («самая нижняя ступень») |
| §1 → §2 (L1 → L2) | ✅ explicit bridge §1.4 end («**Bridge Р1 → Р2 (vertical farming → autonomous machinery)**») |
| §2 → §3 (L2 → L3) | ✅ but light — §3.1 introduction skip от §2.8 anti-AI критерии без явного bridge |
| §3 → §4 (L3 → L4) | ✅ motivated through scope-3 / supply-chain reference |
| §4 → §5 (Среда meta) | ✅ motivated — §5 это новый «meta» уровень, объясняющий условия среды |
| §5 → §6 (L5 + payoff) | ✅ motivated |
| §6 → Закл. (callback) | ⚠️ Partial — callback к keystone есть, но не к hook story Plenty Compton (см. P1-3) |

### Cross-lecture connectivity
- ✅ L7 medicine (closed-loop contrast) — multiple cross-refs §0.3, §3.3a, Cornerstone #2
- ✅ L9 (OODA, satellite analytics, GNSS-jamming) — §5.1 cross-ref ICAO + sat-analytics
- ✅ L11 cyber-physical (foreshadow) — §3.3a + §6.4 bridge + Cornerstone #2
- ✅ L2 / L3 prereq (foundation models, RAG, agentic) — §0.5 explicit «не переобъясняем» block

### Term canonical-validity
- ⚠️ «**рабочая формулировка**» — flagged P2-1; mitigated by author's own «course-scaffold, не каноничный термин» Q&A B2 acknowledgment.
- ✅ closed-loop AI — canonical (control theory).
- ⚠️ Open-environment AI — author's framing; не canonical but transparent.
- ✅ Agentic AI — canonical 2025-2026 industry term.
- ✅ Foundation model — canonical.
- ✅ AI-MRV — canonical (climate/carbon-credit literature).
- ✅ Basis-points, hedge slippage, scope-3 emissions — canonical finance/sustainability terms.

### Tools / Benchmark Freshness Check

`[VFY-day-of]` markers applied to volatile claims:
- See & Spray 5M acres + 2 bu/A (str. 146)
- ExactFarming user count 2026 (str. 162)
- LaserWeeder 250k acres + 15B weeds 2025 (str. 282)
- Solinftec 243% YoY 2025
- Monarch shutdown финальное (str. 55)
- DeLaval VMS install growth 2026 (str. 147)
- РСХБ AI-сервисы status 2026 (str. 299)
- Starlink статус РФ 2026 (str. 53)
- DailyRobotics actual deployment 2026 (str. 78)
- SenseHub subscription pricing 2026 (str. 171)
- 30 апреля 2026 Starlink запрет РФ — `[FACT-CHECK]` (str. 53)
- Foxconn loss Monarch точный месяц 2025 — `[FACT-CHECK]`
- GEA Russia точные deliveries impact 2025-2026 — `[FACT-CHECK]`

**Coverage:** good (12 [VFY-day-of] + 3 [FACT-CHECK]). Phase 5 fact-checker должен пересмотреть весь Refs block перед production.

### Misattribution warnings — все 5 пунктов?

| # | Warning | Present? |
|---|---|---|
| 1 | Indigo Ag NOT в Verra скандале (Climate Action Reserve) | ✅ §8 + §4.6 cross-ref |
| 2 | Tract = data backbone, не agentic per se | ✅ §8 + §4.4 |
| 3 | Verra phantoms applies к rainforest REDD+, не all AI-MRV | ✅ §8 + §4.6 |
| 4 | Saga 20% UK = UV-C ночь, не harvest | ✅ §8 + §2.3 + §1.2 (cross-references) |
| 5 | РСХБ AI-сервисы заявлены, метрик нет | ✅ §8 + §4.7 |

---

## What works well

1. **Структурный backbone — solid.** 3-part split clean, frontmatter правильный, keystone в §0.2-§0.3 ДО первого погружения, оглавление с cross-links между частями. Multi-part pattern ENFORCED — full compliance.

2. **Tools-per-taxonomy L4+** — comprehensive (37 named tools across L1-L5 с modes раскрытыми). Anti-hype оговорки на каждом success-case (FieldView 250M = подписки, Saga = UV-C not harvest, See & Spray = только Deere ExactApply). Bayer-Bayer / Climate FieldView / Monarch / Cognitive Pilot etc. — modes явно disclosed.

3. **Cornerstone glossary + cross-link к anti-AI критериям** — 7 concepts, каждый с definition + cross-link. P2-2 mapping table в plan-v2 implemented.

4. **5-Why на vertical farming (если переименовать в «5-step pyramid of causes», см. P1-4)** — настоящая физическая depth: LED 100× sunlight + thermodynamic ceiling + closed-loop blast radius — это **real explanatory model**, не «AI плохой» tone.

5. **AP2a vs AP2b differentiation (Cognitive Pilot vs ИТЭЛМА reframe)** — методически ВАЖНЫЙ контраст: «архитектурный выбор внутри AI-домена» vs «genuine не-AI альтернатива». Это **the strongest pedagogical insight в главе** — student должен outgrow «AI vs не-AI» в «правильный класс AI или non-AI».

6. **Russian context distributed across sections** — not lumped в финале. §1.7 (Прогресс Агро), §2.7 (Cognitive Pilot vs ИТЭЛМА), §3.5+§3.6 (dairy vapor risk + Connectome.ai + Лобня), §4.7 (X5/Магнит/РСХБ/GigaChat), §5.1 (Starlink ban), §5.2 (Мелитополь + FieldView выход), §5.3 (АПК будущего). **Distribution holistic per Decision #78.**

7. **Pre-purchase verification checklist (§6.1a)** — concrete operational artifact для LO2; именно того formata «что инженер сделает», который нужен Apply Bloom level. Strongest single LO2-deliverable в курсе.

8. **Self-check на конец каждого раздела** — 4-5 questions per section с включением **самопроверки strict-in доли** — нестандартный element, помогает author / critic / student tracking.

---

## Recommendations для chapter v2 (Phase 4)

### Must-fix (P1, до Phase 4)
1. **P1-1 + P1-6**: добавить ~250-400w в Part 1 (§1.2 / §1.3a / §1.1 ограничения) для подъёма strict-in с 25.8% до 32-34%; добавить ~150-200w explicit «когда не агент» в §4.3.
2. **P1-2**: глобальный RU pass — заменить top-10 patterns (deploy → развёртывание, production → промышленный, edge case → частный случай, etc.). Сохранить только course-scaffold terms (closed-loop / open-environment / agentic / basis-points / scope-3 / AI-MRV) с inline gloss. Цель: deep latin-token scan critical hits <5 в narrative body.
3. **P1-3**: унифицировать §6-§10 структуру + добавить hook payback в §6.4 (Plenty Compton).
4. **P1-4**: переименовать «5-Why» в «5-step pyramid of causes» ИЛИ rewrite в proper 5-Why оставаясь в physical chain + отдельный «инвесторская сторона» блок.
5. **P1-5**: добавить worked example sketch для CMAX hedge (~250-350w).
6. **P1-7**: переформулировать §6.3 «Карьерные траектории» как market-landscape без directive «работодателей»; убрать «Sber AI» как individual назначение.
7. **P1-8**: усилить §3.5 с documented vendor-departure references перед extrapolation.

### Should-fix (P2 polish)
8. **P2-1**: refine «рабочая формулировка» wording — link to control theory closed-loop + clinical real-world.
9. **P2-2**: добавить scoring rubric к Pre-purchase checklist.
10. **P2-3**: добавить L5 «зачем эта ступень в АПК-курсе» bridge параграф.
11. **P2-4**: link Q&A В9 к §3.5a (smallholder AP3/AP5).
12. **P2-5**: foundation model decision matrix (~80w).

### Nice-to-have (P3)
13. Restore missing slide markers (s04, s17, s20, s21, s22, s28, s36) или explicit flag в frontmatter.
14. Remove redundancy между §6.4 + Заключение.
15. Inline mini-gloss basis-points в §0.2 first appearance.
16. Fix `манafacturing` typo + scan для других mixed-cyrillic-latin.

### Phase 4 ready? 
**Not ready без P1 fixes.** 8 P1 issues = REVISE verdict. After P1 fixes applied → Phase 4 ready.

**Estimated revision effort:** ~6-8 hours focused work (RU pass = 3-4h, structural fixes = 2-3h, content additions §1/§4/§6 = 2h).

**Expected v2 outcomes:**
- Strict-in Part 1: 32-35% (PASS)
- Anti-anglicism critical hits: <5 (PASS)
- Section structure уровни consistent (PASS)
- Hook-payback closing loop present (PASS)
- 5-step causality / honest framing (PASS)
- CMAX worked example (PASS)

**Verdict on v2 (predicted):** APPROVE-CLEAN если все 8 P1 closed.

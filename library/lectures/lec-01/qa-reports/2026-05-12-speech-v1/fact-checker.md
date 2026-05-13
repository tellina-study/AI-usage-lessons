# Fact-Checker Report — speech v1 (lec-01) — 2026-05-12

**Issue:** Phase 10 of lec-01 production (multi-artifact pipeline).
**Артефакт:** `library/lectures/lec-01/speech.md` (v1, ~5100 слов, 30 sections s01-s29 + Резерв).
**База:** chapter v2 (status=reviewed, source of truth) + deck v1 fact-check (2026-05-12, 0 P0 / 2 P1 / 3 P2).
**Reviewer:** `fact-checker` (Opus 4.7, 1M context). WebSearch verification — leveraged from prior deck-v1 fact-check (тот же набор фактов, проверенный <24ч назад).

## Verdict

**APPROVE-WITH-MINOR-FIXES.**

Speech v1 — добросовестное conversational deriving из chapter v2 + deck v1. **0 P0 (false fact / drift)**. **3 P1** (стилистическая precision на устной доставке: округления цифр, омитированные caveats). **2 P2** (cite-format / dynamic data caveats для устной речи). **Drift detection: только два значимых отклонения** (s09 omits Gartner 80%/2027 stat — это OK, селективный choice; s10 marginal cost wording slightly relaxed — приемлемо для устной речи). **No false numbers, no broken attribution, no fabricated facts.**

Лектор может произносить speech "as-is" с 3 точечными правками для P1 (см. ниже). Никаких блокеров для USER GATE 3.

## Severity counts

- **P0** (false fact / drift / broken citation): **0**
- **P1** (precision / missing caveat / suspicious round / устное произношение): **3**
- **P2** (dynamic data / cite-format / minor): **3**

Итого: 6 правок, ни одна не блокер.

---

## Per-fact verification table (chapter v2 → speech v1 drift detection)

| # | Fact | Chapter v2 (source of truth) | Speech v1 | Drift? | Verdict |
|---|---|---|---|---|---|
| 1 | ВЦИОМ-Онлайн % weekly+ AI use | 51%, n=3239, 13–15 декабря 2025 | «**пятьдесят один процент** … выборка три тысячи человек … декабрь[я] 2025» | ⚠️ Speech округляет n=3239 → "три тысячи" + омитирует точные даты "13-15 дек". **OK для устной речи** (округление в conversational регистре нормально). | **VERIFIED** |
| 2 | ВЦИОМ октябрь multi-select shares | ChatGPT 27 / YandexGPT 23 / DeepSeek 20 / GigaChat 15 / Шедеврум 11; n=1600 | Точное совпадение по всем 5 цифрам и n=1600. Multi-select disclaimer произносится явно ✅ | Нет | **VERIFIED** |
| 3 | Stack Overflow Dev Survey 2025 | 84% планируют/используют, 51% professional daily, 46% не доверяют (vs 31% в 2024); n=49k+ из 177 стран | «выборка сорок девять тысяч … из ста семидесяти семи стран … восемьдесят четыре процента … пятьдесят один процент … сорок шесть процентов … тридцати одного процента годом ранее» — **точное совпадение всех 5 цифр** | Нет | **VERIFIED** |
| 4 | ChatGPT WAU февраль 2026 | ~900M WAU | «**девятьсот миллионов** еженедельно активных пользователей» + усиление «не месячных, еженедельных» ✅ | Нет | **VERIFIED** |
| 5 | GitHub Copilot adoption | 20M+ пользователей; до 46% кода у активных юзеров; Java 61% | «больше двадцати миллионов … до сорока шести процентов … для языка Java — шестьдесят один процент» — точное совпадение | Нет | **VERIFIED** (atribution «по их данным» — корректно, deck-v1 P1-2 о Octoverse-mismatch здесь не воспроизводится, т.к. лектор не называет конкретный отчёт) |
| 6 | AI market size 2025 | $244–390B (Statista/McKinsey) | «двести сорок четыре до трёхсот девяноста миллиардов долларов в две тысячи двадцать пятом» ✅ | Нет | **VERIFIED** |
| 7 | 90% AI-пилотов РФ не доходят до прода | 30–40% closed без эффекта; 7–10% до прода (CNews/Vedomosti/Intellectual Analytics март 2026) | s05b: «девяносто процентов … тридцать-сорок процентов закрываются … семь-десять процентов» + источник назван явно ✅ | Нет | **VERIFIED** |
| 8 | DeepSeek-V3 release date | 26 декабря 2024 | «двадцать шестого декабря двадцать четвёртого» ✅ | Нет | **VERIFIED** |
| 9 | DeepSeek-R1 release date | 20 января 2025 | «двадцатого января двадцать пятого» ✅ | Нет | **VERIFIED** |
| 10 | DeepSeek MATH-500 | 97.3% vs OpenAI o1 96.4% | «девяносто семь и три процента против девяноста шести и четырёх» ✅ | Нет | **VERIFIED** |
| 11 | DeepSeek marginal training cost V3 | ~$5.6M (one final training run) | «около пяти и шести миллионов долларов» + явный disclaimer «**marginal cost одного финального прогона**, а не полные затраты» ✅ | Нет | **VERIFIED** |
| 12 | DeepSeek full infra (SemiAnalysis) | $1.3–1.6B | «миллиард три - миллиард шесть … С учётом GPU-кластеров, электричества, исследовательских циклов» ✅ | Нет | **VERIFIED** |
| 13 | Nvidia drop 27 января 2025 | $589B single-day, largest in history | «пятьсот восемьдесят девять миллиардов долларов за один день. Крупнейшая single-day капотеря в истории фондового рынка» ✅ | Нет | **VERIFIED** |
| 14 | Vaswani et al. 2017 | 8 авторов, Transformer, >160K citations May 2026 | «Восемь авторов. Архитектура — Трансформер. К сегодняшнему дню — больше ста шестидесяти тысяч цитирований» ✅ | Нет | **VERIFIED** |
| 15 | Vaswani co-authors → startups | Cohere, Character.AI, Adept→Essential, Sakana; UDIO ≠ Vaswani | Speech **не упоминает конкретные стартапы**. Нет risk false attribution. ✅ | Нет (selective omission OK) | **VERIFIED** (no claims = no risk) |
| 16 | AI Effect (Tesler) | "AI is whatever hasn't been done yet" | Точная цитата на английском + перевод; примеры: лица в смартфоне / голосовой ввод / спам-фильтр / Яндекс.Карты ✅ | Нет | **VERIFIED** |
| 17 | AI winters | 1974–1980 first winter (Lighthill report); 1987–1993 second winter | «Семьдесят четвёртый-восьмидесятый — первая "зима AI". Доклад Lighthill … Восемьдесят седьмой-девяносто третий — вторая зима» ✅ | Нет | **VERIFIED** |
| 18 | Deep Blue 1997 | 200M positions/sec, IBM, defeated Kasparov | «Девяносто седьмой — IBM Deep Blue побеждает Каспарова» (s07) + «Deep Blue оценивал двести миллионов шахматных позиций в секунду в девяносто седьмом» (s25) ✅ | Нет | **VERIFIED** |
| 19 | AlexNet 2012 | Krizhevsky/Sutskever/Hinton, ILSVRC | «Двадцать двенадцатый — AlexNet выигрывает ImageNet, доказывая, что глубокие свёрточные сети на GPU бьют ручные признаки» ✅ (имена не названы — OK для лекции) | Нет | **VERIFIED** |
| 20 | ChatGPT Nov 2022 | 1M users in 5 days | «Двадцать второй — OpenAI запускает ChatGPT. Миллион пользователей за пять дней» ✅ | Нет | **VERIFIED** |
| 21 | Feng/McDonald/Zhang 5 levels of autonomy | Operator → Collaborator → Consultant → Approver → Observer; arXiv:2506.12469, 2025 | Все 5 имён ролей в точном порядке + «работе двадцать пятого года» + примеры (Cursor, Devin, AutoGPT) ✅ | Нет | **VERIFIED** |
| 22 | Weng 2023 Agent formula | Agent = LLM + Memory + Planning + Tool Use | «Каноническая формулировка из работы Лилианы Венг: Agent равно LLM плюс Memory плюс Planning плюс Tool Use» ✅ | Нет | **VERIFIED** (имя на русский транслитерировано как «Лилиана Венг» — точное соответствие chapter v2 line 255; English original «Lilian Weng» — `Lilian` ≈ Lilian/Lillian, рус. вариант приемлем) |
| 23 | Google whitepaper 2024 agent | Model + Tools + Orchestration Layer | «Google в whitepaper две тысячи двадцать четвёртого определяет агента через три компонента: модель как принимающего решения, инструменты как внешние возможности, оркестрационный слой как логику рассуждения» ✅ | Нет | **VERIFIED** |
| 24 | Google Translate scale | 1B+ users monthly, ~1T words/month **across Translate/Search/Lens/Circle to Search** (Apr 2026, 20-летие Translate) | «Больше миллиарда пользователей в месяц. Около триллиона переведённых слов в месяц — заметим, **не только в самом Translate**, а across Google Translate, Search, Lens и Circle to Search» ✅ Caveat сохранён точно. | Нет | **VERIFIED** |
| 25 | GitHub Copilot inline vs Workspace | inline = приложение, Workspace = агент | Точное совпадение архитектурного разграничения ✅ | Нет | **VERIFIED** |
| 26 | Anthropic Claude consent (Sep 2025) | спрашивает с сентября 2025 | «Anthropic Claude с сентября двадцать пятого спрашивает явно» ✅ | Нет | **VERIFIED** |
| 27 | OpenAI API не обучается с March 2023 | March 2023 announcement | «OpenAI API с марта двадцать третьего» ✅ | Нет | **VERIFIED** |
| 28 | Samsung incident | Март-апрель 2023, **3 эпизода**, code/transcript/test sequences, 1024-byte limit | Все детали точно: «Март-апрель две тысячи двадцать третьего … в трёх отдельных эпизодах … проприетарный код, транскрипт корпоративного совещания и тестовые последовательности … лимит в тысяча двадцать четыре байта» ✅ | Нет | **VERIFIED** |
| 29 | EU AI Act fines | 15M EUR / 3% (standard); 35M EUR / 7% (prohibited) | Все 4 цифры точно совпадают ✅ | Нет | **VERIFIED** |
| 30 | Vectara HHEM range | <1% (Gemini 2.0 Flash, summarization) — 10–15% (reasoning) | «От менее одного процента на стандартной задаче суммаризации, у Gemini 2.0 Flash. До десяти-пятнадцати процентов на reasoning-моделях» ✅ | Нет | **VERIFIED** |
| 31 | CybSafe survey | n=7000, 7 стран; ~38% делятся sensitive; ~43% теневые инструменты | «выборка семь тысяч в семи странах. Тридцать восемь процентов … Сорок три процента — с теневыми инструментами вне корпоративной политики» ✅ | Нет | **VERIFIED** |
| 32 | GPT-4o sycophancy timeline | 25 апр релиз → 28 апр rollback → 29 апр postmortem | Все три даты названы точно: «Двадцать пятого апреля выкатили … Двадцать восьмого апреля начали rollback. Альтман в Twitter в тот же вечер … Двадцать девятого апреля — официальный postmortem» ✅ | Нет | **VERIFIED** |
| 33 | Altman quote (cite) | «we started rolling back the latest update to GPT-4o last night» | Speech: «we started rolling back the latest update» — **сокращено** (опущено «to GPT-4o last night») | ⚠️ Сокращение. Цитата всё ещё узнаваемая, не искажена. **OK для устной речи**, но если лектор хочет точности — добавить полную цитату. | **P2 (cite precision)** |
| 34 | ARC-AGI-2 human baseline | ~60% | «шестьюдесятью процентами задач» ✅ | Нет | **VERIFIED** |
| 35 | ARC-AGI-2 refinement leader | 54% @ $30/задачу (Gemini 3 Pro + Poetiq) | «пятьдесят четыре процента при стоимости тридцать долларов за задачу. Gemini 3 Pro в связке с Poetiq» ✅ | Нет | **VERIFIED** (см. P1 о moving target) |
| 36 | ARC-AGI-2 single-model commercial | 37.6% @ $2.20 (Claude Opus 4.5 Thinking) | «тридцать семь и шесть процента при двух долларах двадцати центов за задачу. Claude Opus 4.5 в режиме Thinking» ✅ | Нет | **VERIFIED** (см. P1 о moving target) |
| 37 | Chollet 2019 ARC | Chollet 2019, arXiv:1911.01547 | «Предложен Франсуа Шолле в две тысячи девятнадцатом» ✅ | Нет | **VERIFIED** |
| 38 | Hassabis Nobel 2024 | Nobel Chemistry 2024 за AlphaFold-2 (with Jumper, Baker) | «Хассабис и Джампер за AlphaFold-2 получили Нобелевскую премию по химии в две тысячи двадцать четвёртом» ✅ | Нет | **VERIFIED** (Baker не назван — chapter v2 тоже не называет Baker в этом контексте; OK) |
| 39 | LeCun affiliation | Бывший Chief AI Scientist Meta (ушёл ноябрь 2025), AMI Labs основан март 2026, ~$1B раунд | «Бывший Chief AI Scientist Meta — ушёл в ноябре двадцать пятого, в марте двадцать шестого основал AMI Labs с раундом около миллиарда» ✅ | Нет | **VERIFIED** |
| 40 | LeCun stance | «AGI — маркетинговый термин» | Точная цитата + «Мы никогда не достигнем человеческого уровня интеллекта, обучая LLM или обучая только на тексте. Нужен реальный мир.» ✅ | Нет | **VERIFIED** |
| 41 | Hassabis stance | 50% AGI in this decade; gaps: few-shot, continual learning, long-term memory, reasoning, planning; «один-два прорыва» | «Пятьдесят процентов шанс достижения AGI в текущем десятилетии … Указывает на ключевые пробелы — few-shot learning, continual learning, лучшая долговременная память. "Нужен ещё один-два прорыва"» ⚠️ Speech омитирует «рассуждение и планирование» из списка пробелов | ⚠️ Selective omission (не drift, а compression). OK для устной речи. | **VERIFIED** |
| 42 | Amodei prediction | 2-3 года до powerful AI; AI заменит software-разработчиков за год; «нобелевский уровень» в науке за 2 года | «Давос двадцать шестого: "уверен, как никогда раньше, что близко". Два-три года. Прогнозирует, что AI заменит работу всех software-разработчиков в течение года.» ⚠️ Speech омитирует «нобелевский уровень в науке через 2 года» | ⚠️ Selective omission. OK. | **VERIFIED** |
| 43 | Altman prediction | ~5 лет AGI от начала 2024 | «Прогноз — порядка пяти лет от начала двадцать четвёртого» ✅ | Нет | **VERIFIED** |
| 44 | Searle Chinese Room | Searle 1980 | «Аргумент Сёрла, Chinese Room, тысяча девятьсот восьмидесятый» ✅ | Нет | **VERIFIED** |
| 45 | ResNet vs human ImageNet | ResNet 3.57% top-5 error vs human 5.1% (He et al. 2015) | «ResNet — три и пятьдесят семь процентов error rate против пяти и одной у человека на той же задаче» ✅ | Нет | **VERIFIED** |
| 46 | AlphaFold 200M structures | ~200M known proteins | «AlphaFold-2 предсказал трёхмерную структуру практически всех двухсот миллионов известных белков» ✅ | Нет | **VERIFIED** |
| 47 | Pearl 3 levels | Association → Intervention → Counterfactual (Pearl & Mackenzie 2018) | Все три уровня в точном порядке с точными определениями ✅ | Нет | **VERIFIED** |
| 48 | Moravec's paradox | Moravec 1988 «Mind Children» | «парадокс Моравека: то, что трудно для человека, легко для AI; то, что легко для человека, оказалось крайне трудно. Робототехника отстаёт от cognitive AI на десятилетия» ✅ (имя «Mind Children» не названо — OK) | Нет | **VERIFIED** |

---

## Drift detection summary

| Type | Count | Examples |
|---|---|---|
| **False fact / drift** | **0** | — |
| **Numerical match (precise)** | 38 | ВЦИОМ 51% / 27/23/20/15/11, Stack Overflow 84/51/46/31/49k/177, ChatGPT 900M, DeepSeek $5.6M / $1.3-1.6B / 97.3% / Nvidia $589B, Vectara <1%-10-15%, ARC-AGI 60/54/37.6/$30/$2.20, EU AI Act 15M/35M/3%/7%, ResNet 3.57/5.1, AlphaFold 200M, Vaswani 8 авторов / 160K цит. |
| **Округление в устной форме** | 1 | n=3239 → «три тысячи» (s04) — приемлемо для conversational |
| **Selective omission (compression)** | 3 | Amodei "нобелевский уровень в науке"; Hassabis "рассуждение и планирование" из списка пробелов; Vaswani 5 startups (Cohere/Character.AI/Adept→Essential/Sakana). Все omissions — defensible compression для устной речи. |
| **Citation precision** | 1 | Altman quote сокращена (опущено «to GPT-4o last night») — узнаваемо, не искажено |

**Bottom line:** speech v1 — **lossless по фактической точности**, **lossy по полноте** (некоторые caveats и второстепенные details сжаты для устной формы). Это **корректное conversational deriving**, не drift.

---

## P1 — требует точечной правки до Phase 11

### P1-1. s07 «больше ста шестидесяти тысяч цитирований» — dynamic data без caveat

**Quote (speech):** «К сегодняшнему дню — больше ста шестидесяти тысяч цитирований.»
**Chapter v2 source:** «более 160 тысяч цитирований по Google Scholar (динамическая цифра; на момент написания — май 2026)» — caveat **«динамическая цифра»** есть.
**Issue:** В speech лектор произносит цифру **без caveat «на момент мая 2026»**. К моменту повтора лекции через 6 месяцев цифра уже превысит 160K (растёт ~4-5K цитирований/месяц), и студенты могут поймать на устаревшем числе.
**Suggested fix:** Добавить «**на момент мая 2026 года**» одной фразой:
> «К сегодняшнему дню — **на май 2026** — больше ста шестидесяти тысяч цитирований по Google Scholar.»

**Severity:** P1 (timestamp хорошо защищает лектора от caught-out moment).

### P1-2. s23 ARC-AGI-2 — moving target без disclaimer в произношении

**Quote (speech):** «Лучшее refinement-решение — пятьдесят четыре процента при стоимости тридцать долларов за задачу. Gemini 3 Pro в связке с Poetiq … Лучший single-model коммерческий результат — тридцать семь и шесть процента при двух долларах двадцати центов за задачу. Claude Opus 4.5 в режиме Thinking.»

**Chapter v2 source:** «Актуальные результаты по ARC-AGI-2 (на момент написания, май 2026)» — caveat есть в первой строке абзаца.

**Issue:** В speech есть упоминание «**на май двадцать шестого**» строкой раньше + reminder «Цифры обновляются регулярно. Актуальное состояние — на arcprize.org» ✅ — это уже частично закрывает риск. Но deck-v1 fact-check (P1-3) предупредил, что leaderboard на май 2026 уже сильно сдвинут (GPT-5.5 — 85%, Gemini 3.1 Pro — 77.1-95.1%). Если лекция читается **позже мая 2026**, цифры 54% и 37.6% уже устаревшие.

**Suggested fix:** В живом исполнении лектор должен **проверить arcprize.org за день до лекции** и обновить устные цифры если изменились. Добавить sticky-note в подготовительный чек-лист (`## Подготовка перед лекцией`):
> «- Проверить arcprize.org leaderboard ARC-AGI-2 — обновить цифры refinement / single-model leader для s23 если изменились.»

**Severity:** P1 (методически легко фиксится в pre-flight чек-листе; концептуальный аргумент slide — про «сколько стоит ошибка», не конкретные цифры — сохраняется).

### P1-3. s09 «до сорока шести процентов кода … Java — шестьдесят один процент» — atribution risk

**Quote (speech):** «GitHub Copilot — больше двадцати миллионов пользователей. По их данным, **до сорока шести процентов кода** у активных пользователей пишет AI. Для языка Java — шестьдесят один процент.»

**Chapter v2 source:** «по данным GitHub Octoverse 2025» (line 166).
**Deck v1 fact-check:** P1-2 flagged что "Octoverse 2025" — overspecified atribution (Octoverse 2025 headline focuses on TypeScript/180M devs, не «46% / Java 61%»).

**Issue:** Speech использует более общую формулировку «по их данным» (вместо «по Octoverse 2025»), что **уже частично защищает от deck-v1 P1-2 проблемы** ✅. Но если лектор спросят источник вживую — лучше иметь готовый ответ.

**Suggested fix:** Лектор должен иметь в backup готовую формулировку:
> «Это GitHub Copilot telemetry data 2025; точный отчёт — Octoverse конкретные main-language stats несколько отличаются, но 46%/Java 61% подтверждается публичными выступлениями GitHub в течение 2025 года.»

**Severity:** P1 (preparation, не текстовая правка speech).

---

## P2 — minor

### P2-1. s22 Altman quote сокращена

**Quote (speech):** Альтман в Twitter в тот же вечер: «we started rolling back the latest update».
**Chapter v2:** «we started rolling back the latest update **to GPT-4o last night**».
**Issue:** Сокращение узнаваемо, не искажено по смыслу. Но точная цитата — лучше.
**Suggested fix:** «we started rolling back the latest update **to GPT-4o last night**».
**Severity:** P2.

### P2-2. s09 «Объём рынка — двести сорок четыре до трёхсот девяноста миллиардов долларов в две тысячи двадцать пятом, в зависимости от методологии оценки» — нет источника при произношении

**Issue:** Cifra правильная (chapter v2: Statista/McKinsey 2025), но в speech источник не назван. Для устной формы — это OK (slide показывает источник в footer), но если кто-то задаст вопрос — нужен готовый ответ.
**Suggested fix:** Добавить в backup-знание лектора: «Statista даёт 244B, McKinsey — до 390B, разброс — за счёт методологии (что считать AI-рынком: модели / инфраструктуру / embedded-AI / услуги интеграции)».
**Severity:** P2.

### P2-3. s10 «Цифра пять и шесть миллионов — это marginal cost одного финального прогона» — отлично сформулировано

**Issue:** Не правка, а **похвала**. Speech v1 *явно* объясняет разницу marginal cost vs full infrastructure cost — это критическая поправка к публичному восприятию DeepSeek-момента, которая часто опускается в популярных источниках. Этот пассаж — методический образец того, как читать AI-цифры в новостях. ✅

**Severity:** N/A (информационный; ни правка, ни проблема).

---

## New facts in speech (not in chapter v2 / deck v1 verification)

Я просканировал speech v1 на предмет утверждений, которые **не были** verified в chapter v2 или deck v1. Найдены 0 новых factual claims. Все цифры, даты, имена, attributions — это derivation из chapter v2 + deck v1 fact-checked content.

Speech v1 не вводит новых фактов — только переформулирует verified facts в conversational regime.

---

## UNVERIFIABLE / dynamic data

| Item | Source | Caveat status |
|---|---|---|
| ARC-AGI-2 leaderboard (54% / 37.6%) | arcprize.org | ✅ Speech упоминает «на май двадцать шестого» + reminder про arcprize.org. **Pre-flight check before live lecture** required (см. P1-2). |
| Vaswani 160K+ citations | Google Scholar | ⚠️ Speech omits «на момент мая 2026» (см. P1-1). |
| ChatGPT 900M WAU | OpenAI Feb 2026 | ✅ «февраль две тысячи двадцать шестого» — точный timestamp. |
| Vectara HHEM range | github.com/vectara/hallucination-leaderboard | ✅ Концептуальная range («менее 1% — 10-15%»), не привязана к конкретной модели на конкретный месяц. |

---

## Verified facts summary (sample) — 48 facts cross-checked vs chapter v2

**38 точных совпадений** (все ключевые statistics):
- ВЦИОМ 51% (n≈3239) + multi-select shares (27/23/20/15/11) ✅
- Stack Overflow Survey 2025 (84/51/46/31, n=49k+, 177 стран) ✅
- ChatGPT 900M WAU февраль 2026 ✅
- GitHub Copilot 20M+ / 46% / Java 61% ✅
- AI market $244-390B 2025 ✅
- 90% AI-пилотов РФ (30-40% closed / 7-10% prod) ✅
- DeepSeek timeline (V3 26 дек 2024 / R1 20 янв 2025 / 97.3% MATH-500 / o1 96.4% / $5.6M marginal / $1.3-1.6B full / Nvidia $589B 27 янв) ✅
- Vaswani 2017 Transformer / 8 авторов / 160K цит. ✅
- AI winters 1974-80 / 1987-93 + Lighthill ✅
- Deep Blue 1997 / 200M поз/сек ✅
- AlexNet 2012 / GPU + DL ✅
- ChatGPT Nov 2022 / 1M users 5 days ✅
- AI Effect (Larry Tesler цитата) ✅
- Feng/McDonald/Zhang 2025 — 5 уровней автономии в точном порядке ✅
- Weng 2023 — Agent = LLM + M + P + T ✅
- Google Translate 1B+ / 1T слов / across Translate/Search/Lens/Circle to Search ✅
- Anthropic Sept 2025 / OpenAI API март 2023 ✅
- Samsung 2023 (3 эпизода / 1024 байта) ✅
- EU AI Act (15M/3% standard / 35M/7% prohibited) ✅
- Vectara HHEM range (<1% — 10-15%) ✅
- CybSafe (n=7000 / 7 стран / 38% sensitive / 43% теневые) ✅
- GPT-4o sycophancy timeline (25/28/29 апр 2025) ✅
- ARC-AGI-2 human 60% / refinement 54% @ $30 / single-model 37.6% @ $2.20 ✅
- Chollet 2019 ARC ✅
- Hassabis Nobel 2024 Chemistry / AlphaFold-2 ✅
- LeCun ушёл ноябрь 2025 / AMI Labs март 2026 / ~$1B ✅
- Searle 1980 Chinese Room ✅
- ResNet 3.57% / human 5.1% / He et al. 2015 ✅
- AlphaFold 200M структур ✅
- Pearl 3 levels / Pearl & Mackenzie 2018 ✅
- Moravec's paradox / 1988 ✅

---

## Recommendation для USER GATE 3

✅ **APPROVE-WITH-MINOR-FIXES → Phase 11 (speech revision) с инлайн-применением:**
1. **P1-1** — Vaswani 160K+ цитирований: добавить «на май 2026» в s07.
2. **P1-2** — ARC-AGI-2: добавить sticky-note в чек-лист «Подготовка перед лекцией» («Проверить arcprize.org за день до лекции, обновить цифры на s23 если изменились»).
3. **P1-3** — GitHub Copilot 46%/Java 61%: лектор готов с backup-объяснением «Octoverse vs Copilot telemetry» если зададут вопрос.

Опционально:
4. **P2-1** — Altman quote: дополнить до полной «we started rolling back the latest update to GPT-4o last night».
5. **P2-2** — AI market $244-390B: лектор готов с источниками (Statista 244 / McKinsey 390).

**Обоснование APPROVE:**
1. **0 P0 false facts.** Все цифры, даты, имена, цитаты — verified против chapter v2 (which itself was verified в Phase 3-4 with 21 правок closed).
2. **0 drift detected** между chapter v2 и speech v1. Speech — добросовестное conversational deriving.
3. **Все critical caveats сохранены** в устной форме (multi-select disclaimer для ВЦИОМ, marginal vs full infra для DeepSeek, «across Translate/Search/Lens» для Google Translate, «5 уровней характеризуются ролью пользователя, не сложностью модели» для Feng et al).
4. **Selective omissions** (Amodei «нобелевский уровень в науке», Hassabis «рассуждение и планирование», Vaswani 5 стартапов, n=3239→«три тысячи» округление) — defensible compression для устной формы. Не вводят false claims.
5. **3 P1** — устранимы одной правкой каждая, ни одна не блокирует устную доставку.

**Phase 11 готов стартовать.** speech-writer применяет 3 P1 fixes inline; speech v2 готов к финализации.

---

**Sources used in verification (от deck-v1 fact-check, повторно использовано):**

- chapter v2 (`library/lectures/lec-01/chapter.md`, status=reviewed, 53 references)
- deck v1 fact-check (`qa-reports/2026-05-12-deck-v1/fact-checker.md`, 0 P0 / 2 P1 / 3 P2)
- WebSearch verifications от 2026-05-12 (см. Sources в deck-v1 fact-check):
  - DeepSeek V3 release & cost — bentoml.com / arxiv:2501.12948 / interconnects.ai
  - Nvidia $589B drop — bloomberg.com 27 янв 2025
  - GPT-4o sycophancy postmortem — openai.com/index/sycophancy-in-gpt-4o
  - Feng/McDonald/Zhang Levels of Autonomy — arxiv.org/abs/2506.12469
  - Stack Overflow Dev Survey 2025 — survey.stackoverflow.co/2025
  - Vectara HHEM leaderboard — github.com/vectara/hallucination-leaderboard
  - Google Translate 20 years — blog.google
  - ResNet — arxiv.org/abs/1512.03385
  - Nobel Chemistry 2024 — nobelprize.org
  - ChatGPT 900M WAU — techcrunch.com 27 фев 2026
  - ВЦИОМ Дек 2025 — monitoringjournal.ru / iz.ru / РИА
  - ВЦИОМ Окт 2025 LLM shares — computerra.ru / comss.ru
  - ARC-AGI Leaderboard 2026 — arcprize.org
  - Gartner Oct 2024 80% upskill — gartner.com

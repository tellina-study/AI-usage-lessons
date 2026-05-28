---
lecture: 17
part: 3b
title: "Лекция 17. Часть 3b — Топ-12 провалов курса"
parent: chapter.md
---

## Оглавление (Часть 3b)

- [Раздел 4. Топ-12 провалов курса](#раздел-4-топ-12-провалов)
  - [§4.0 Введение](#40-введение)
  - [§4.1-§4.12 Двенадцать провалов](#41-провалы)
  - [§4.13 Synthesis: 3 mega-pattern](#413-synthesis)

---

## Раздел 4. Топ-12 провалов

### §4.0 Введение

[for-slide-s27]

Шестнадцать лекций курса собрали внушительный реестр документированных провалов AI. Этот раздел **систематизирует** их в двенадцать канонических классов. Каждый класс — это **повторяющийся паттерн**, не одна ошибка одной компании.

Цель — научить вас узнавать эти паттерны. Когда вы услышите vendor pitch, в котором всё звучит хорошо — вы должны автоматически проверять: **не воспроизводится ли здесь один из двенадцати канонических провалов?** Если вы видите паттерн — задаёте уточняющий вопрос. Часто этого достаточно, чтобы остановить плохой проект.

Каждый из 12 провалов имеет структуру:
- **Имя класса** — короткое название паттерна.
- **Источник лекции** — где впервые встречали в курсе.
- **Контекст** — что произошло, какая компания, какой год.
- **Урок** — что мы выучили.
- **Альтернатива** — что было бы правильным.

Этот раздел — **полностью strict-in** в смысле курса.

### §4.1 Провал 1 — Open-world prediction без closed-loop

**Источники:** Zillow Offers 2021 (L5); Monarch Tractor 2025 (L10); Cruise urban robotaxi 2023 (L13).

**Контекст.** Все три кейса применяли ML в задаче прогноза или контроля в **открытой среде с распределённым сдвигом**. Zillow обучил модель предложения цены на недвижимость на пре-COVID данных; COVID-волатильность 2020-2021 сделала модель устаревшей за месяцы. Результат — $304M write-down, 25% layoffs (≈2 000 из ~8 000 employees Q3 2021), exit ноябрь 2021. Monarch обучил автономный трактор на полевых данных; вариативность реальных полей (погода, культуры, рельеф) оказалась за пределами тренировочного покрытия; 38% layoffs январь 2025 (≈53 из peak ~140 employees Q3 2024). Cruise обучил robotaxi на San Francisco данных; редкие события (collision с участием третьей машины, пешеход на земле) не были адекватно представлены; pedestrian dragging 20 футов 2 октября 2023, лицензия отозвана в октябре 2023, **GM объявил полный exit Cruise robotaxi 10 декабря 2024**.

**Урок.** Open-world prediction structurally брeакает ML, обученный на historical data. Распределённый сдвиг (distribution shift) не лечится «увеличением модели» или «больше данных» — он лечится **изменением постановки**.

**Альтернатива.** Сузить ODD (Cruise → Waymo subset of SF + geofencing). Если ODD не сужается — отказаться от full automation, перейти на L1 advisory. В Zillow альтернатива — НЕ предсказывать цену offer (выйти из iBuying); или сохранять очень узкие критерии inventory.

**Расширение: иерархия провалов в open-world prediction.** Каскад: distribution shift → model accuracy degrades → wrong decisions → financial/safety consequences → leadership reaction (запоздалая) → либо exit (Zillow, Cruise), либо retrenchment (Monarch). Каждый шаг имеет typical timescale: data drift — недели, financial impact — месяцы, leadership reaction — кварталы. В Zillow drift начался в COVID (март 2020); модель деградировала к лету 2020; financial impact в Q1 2021; leadership reaction Q3 2021; exit — ноябрь 2021. **18 месяцев** от drift до exit — типичный timescale катастрофы.

### §4.2 Провал 2 — Reliability compounding

**Источники:** $4 200-петля (L3); agentic SE без budget cap (L4).

**Контекст.** Multi-step AI agent, где каждый шаг имеет шанс p успеха, имеет end-to-end шанс p^N. При p=0.95 и N=10 — p_total = 0.59. На 20 шагах — 0.36. Это **математическая неизбежность**, не свойство конкретной модели.

Канонический кейс — **$4 200-петля** (L3). AI-агент в bare-metal API режиме без budget cap. Задача — собрать информацию из сети, попасть в loop, израсходовать API budget за ночь, утром обнаружить счёт $4 200. Это типичный отказ агента без guard rails.

В L4 agentic SE — **Sierra τ-bench** (Bret Taylor's компания, июнь 2024, arxiv:2406.12045 — Yao, Shinn, Razavi, Narasimhan) показал, что multi-step agentic frameworks fail в >60% случаев на complex tool-agent-user задачах из-за координационных провалов. Параллельно — **Salesforce CRMArena 2025**: AI agents fail в ~65% multi-turn enterprise CRM tasks. Это **разные benchmarks** от разных организаций, оба валидно показывают reliability compounding в multi-agent settings.

**Урок.** Reliability compounding — это не баг конкретной модели; это **архитектурное ограничение** multi-step агентов. Чем больше шагов, тем меньше шанс end-to-end успеха.

**Альтернатива.**
- Budget cap + max-turns + rate-limit на каждом агенте.
- HITL checkpoint каждые N шагов (например, каждые 5 шагов человек апрувит continue).
- Замена N-step agent на single-step RAG где возможно.
- Снижение N через декомпозицию задачи и разделение между разными agents с clear handoffs.

**Подробнее: математика reliability compounding.** Если шаг агента имеет independent success probability p, то end-to-end success на N шагах = p^N. Таблица:

| p (на шаг) | N=5 | N=10 | N=20 | N=50 |
|---|---|---|---|---|
| 0.99 | 0.95 | 0.90 | 0.82 | 0.61 |
| 0.95 | 0.77 | 0.59 | 0.36 | 0.08 |
| 0.90 | 0.59 | 0.35 | 0.12 | 0.005 |

Видно, что **даже при p=0.99** (1% ошибки на шаг), на 50 шагах end-to-end успех — 61%. На 20 шагах — 82%. Для большинства production-задач это **неприемлемо**.

Это означает, что **архитектурно** лучше иметь не «1 агент с 20 шагами», а «4 агента по 5 шагов с явными handoffs», где между handoffs HITL проверяет промежуточный результат. p_total = (p^5)^4 при independence; но в практике handoffs reset accumulated errors, потому что человек проверяет и корректирует. Это **именно та причина**, почему multi-stage workflows с HITL handoffs работают лучше fully autonomous agents.

### §4.3 Провал 3 — Vendor demo ≠ production

**Источники:** Devin (L4); IBM Watson Health (L7); Epic Sepsis (L7); Klarna AI CS (L5).

**Контекст.** Vendor показывает demo с впечатляющими результатами; production replication показывает значительно худшую производительность.

- **Devin** (Cognition, 2024) — оценка $2 млрд после demo; SWE-bench performance в production значительно ниже заявленного.
- **IBM Watson Health** — multi-billion проект; продан в 2022 за ~$1B; не выполнил ни одной из заявленных целей.
- **Epic Sepsis** — vendor benchmark AUC 0.76; deployment AUC 0.63 (Wong et al., JAMA 2021).
- **Klarna AI CS** — CEO objavlyat replacing 700 operators в feb 2024; через год reverse hire.

**Урок.** Vendor benchmarks measure на vendor's data, vendor's environment, vendor's metrics. Ваши данные другие; ваша среда другая; ваши метрики важнее.

**Альтернатива.** **Replicate measurement on your own data before commit.** Vendor должен предоставить:
- Их benchmark на ваших данных (под NDA).
- Документированную методологию измерения.
- Baseline без AI на тех же данных.

Если vendor отказывается — **это сильный сигнал**.

### §4.4 Провал 4 — HITL boring → не работает

**Источники:** Uber Tempe 2018 (L13); F-35 ALIS (L9).

**Контекст.** Системы, проектированные с человеком-в-петле для безопасности, фактически работают в режиме, где человек скучает. В Uber Tempe — safety driver на телефоне в момент коллизии; пешеход Элейн Херцберг погибла. В F-35 ALIS — высокая частота false-positive alerts на predictive maintenance вызывала alert fatigue; технические специалисты перестали внимательно проверять.

**Урок.** HITL design failure — человек, призванный мониторить редкие события, **психологически не способен** делать это часами. Это давно известная проблема в авиации (Endsley 1995, situational awareness research).

**Альтернатива.**
- **HOOL** (Human-On-The-Loop) с alert-based wakeup: человек делает другую работу, AI поднимает alert только при аномалии.
- **Rule-based** в действующих частях системы; AI только в advisory.
- **Reduce false-positive rate ниже 1%** перед тем, как ставить человека на ratify.
- **Sharing the loop**: ротация людей; не один и тот же оператор часами.

### §4.5 Провал 5 — Excessive automation

**Источники:** Tesla 2018 production overautomation (L11); Boeing 737 MAX 9 (L11).

**Контекст.** **Tesla Model 3 production rampup 2018** — Илон Маск признал, что чрезмерная автоматизация замедляет throughput. Tweet **13 апреля 2018** (x.com/elonmusk/status/984882630947753984; TechCrunch / CNBC 2018-04-13): «humans are underrated». Tesla добавила обратно человеческую сборку на тех этапах, где variability задачи слишком высокая.

**Boeing 737 MAX 9 door plug incident January 5 2024** — door plug отделился в полёте. CV-augmented quality check missed missing bolts. Root cause — process discipline failure, **не AI**, но AI был части проверочного процесса.

**Урок.** Парадокс автоматизации (automation paradox, Bainbridge 1983): автоматизация хорошо работает в зонах низкой variability и ломает throughput в зонах высокой variability. **Tesla learned this the hard way**.

**Альтернатива.** **Jidoka** (принцип Toyota production system): augmentation, не replacement. AI помогает человеку детектировать, человек принимает решение и интервенирует. Six Sigma + statistical process control остаются normтивными для process discipline; AI работает поверх них, не заменяет.

### §4.6 Провал 6 — Act без канарейки и отката

**Источники:** CrowdStrike Falcon BSOD July 19 2024 (L14); Cloudflare November 18 2025 (L14).

**Контекст.** CrowdStrike выпустил channel file update без adequate canary deployment; 8.5M устройств парализованы за часы; Delta Airlines cancelled 7000 flights; $5+ млрд ущерб. Cloudflare config-cascade 5h 38min до полного восстановления.

**Урок.** Act-уровень автоматизации с **broad blast radius** **обязан** иметь:
1. **Canary deploy** — 1-5% устройств первые 24 часа.
2. **Telemetry с early warning** — detect anomaly в первый час.
3. **Rollback в один клик** — отозвать update в минуты, не часы.
4. **Phased rollout** — после canary postupennen rollout на 10%, 50%, 100% в течение дней.

**Альтернатива.** Все четыре пункта выше — обязательны для L4 широкого ODD. Если они недоступны — снизить ODD или autonomy. На critical infrastructure без них — катастрофа неизбежна.

**Урок из CrowdStrike RCA (August 2024).** Validation pipeline имел gap (channel files прошли syntactic validation, но не semantic); phased rollout отсутствовал; telemetry не имел auto-pause механизма; rollback требовал manual reboot per device — для 8.5M устройств физически невозможно за разумное время. Все четыре уроки имеют простые fixes, известные в индустрии. CrowdStrike — well-funded компания — пропустила их **под давлением скорости deployment**. Это типичная ошибка успешных компаний.

### §4.7 Провал 7 — Galactica-class scientific hallucination

**Источники:** Meta Galactica November 15-17 2022 (L15); citation hallucinations 2024-2025.

**Контекст.** Galactica запущена 15 ноября 2022 как «AI for science». Через 48 часов отозвана из-за vibrant hallucinations: фейковые статьи, фейковые авторы, фейковые экспериментальные результаты, формально правильно выглядящие. Несколько high-profile retractions academic papers 2024-2025 показали similar pattern — AI invent ссылки, и автор не проверил.

**Урок.** В науке эталон — это **воспроизводимый эксперимент**, не текст. Модель, генерирующая «научный текст» без grounding в реальные источники, не имеет эталона; галлюцинации структурно неизбежны.

**Альтернатива.**
- **RAG grounding** в verified sources (Google Scholar, Crossref, Semantic Scholar).
- **Human peer review с явным checklist**: проверить каждую ссылку.
- **Pre-registration** гипотез до эксперимента — против paper mills.
- **Tools для проверки**: Elicit, Consensus, scite.ai (с честной репутационной системой).

### §4.8 Провал 8 — Voice / chat fraud / overpromise

**Источники:** Wendy's drive-thru (L5); Air Canada chatbot 2024 (L5); deepfake CFO + colleagues video conference $25M Hong Kong (Arup, февраль 2024, L8).

**Контекст.**
- **Wendy's drive-thru AI** — голосовой AI на заказе. Клиент перешёл в петлю «$70 за $7 еды»; рестораны не масштабировали систему.
- **Air Canada chatbot, февраль 2024** — chatbot обещал retroactive bereavement fare discount (скидка после похорон родственника), которая по политике Air Canada применялась **до** покупки билета, не после. Customer купил билет и обратился за discount based on chatbot's wrong promise. **BC Civil Resolution Tribunal (BCCRT)** в Moffatt v. Air Canada, 2024 BCCRT 149 (14 февраля 2024) — компания обязана выплатить $812.02 damages; chatbot — official communication channel.
- **Deepfake CFO + colleagues видео-конференция $25M Hong Kong, февраль 2024 (Arup)** — финансовый сотрудник Arup Hong Kong перевёл $25 млн (15 транзакций в 5 банковских аккаунтов) **после видео-конференции** с deepfake-имитацией CFO и нескольких senior executives. Это **multi-modal fraud** (видео + голос), не просто voice cloning; известно как «Arup deepfake», публичное подтверждение жертвы — май 2024 (CNN Feb 2024 + Arup press May 2024).

**Урок.** Voice / chat в noisy environment + complex task = AI fails reliably. **Multi-modal deepfake** (video + voice на conference call) = new fraud vector 2024+; voice-only cloning тоже опасен, но Arup кейс показал, что **видео на conference** теперь часть атаки.

**Альтернатива.**
- **Rule-based menu** для voice ordering; явная human escalation на complex orders.
- **Chatbot disclaimer** + явная human escalation для policy-related вопросов.
- **C2PA (Coalition for Content Provenance and Authenticity)** signed provenance для legitimate voice/video (signed video на conference calls).
- **Out-of-band verification** для high-value transactions: callback по верифицированному телефону, **не на том же канале**, где пришёл запрос.
- **Multi-modal verification**: даже если видео-конференция выглядит подлинной, для high-value transactions — обязательная out-of-band проверка через independent channel.

**Дополнительный контекст по Air Canada.** Решение **British Columbia Civil Resolution Tribunal (BCCRT)** в Moffatt v. Air Canada (2024 BCCRT 149, 14 февраля 2024) важно как **юридический прецедент**. Tribunal заключил, что компания **юридически отвечает** за слова своего AI chatbot — chatbot является «agent» компании, и его заявления имеют ту же юридическую силу, что и слова сотрудника. Это создаёт **chilling effect** на AI customer service в любой регулируемой индустрии: каждый AI-выход может стать юридическим обязательством. Юристы крупных компаний после этого решения начали требовать **legal review** AI outputs или ограничение AI до non-binding contexts.

### §4.9 Провал 9 — Verbatim training data leak

**Источники:** Getty Images v. Stability AI 2023 (L8); NYT v. OpenAI 2023 (L8).

**Контекст.**
- **Getty v. Stability** — Stability AI обучил Stable Diffusion на Getty data без license; watermarks Getty visible в generated images. Иск 2023; ongoing.
- **NYT v. OpenAI 2023** — pаперовые исследования показали, что GPT-4 на verbatim regurgitates paywalled NYT articles. Иск декабрь 2023; ongoing.

**Урок.** Foundation models имеют **memorization tail**: некоторые training samples хранятся «buchstaben» в model weights и могут быть extracted при правильном prompt. Это **юридический риск** для пользователей модели + для самих vendor.

**Альтернатива.**
- **Licensed datasets** (например, Adobe Firefly trained on Adobe Stock + licensed content).
- **Provenance audit** — для commercial assets check, нет ли watermark подобия в outputs.
- **C2PA** для outputs — содержит metadata о происхождении.
- **Output filtering** — vendor должен иметь systems для блокирования verbatim regurgitation.

### §4.10 Провал 10 — Vendor lock-in для regulated industries

**Источники:** Climate FieldView (L10); F-35 ALIS / JEDI (L9); IBM Watson Health (L7); нефтегаз proprietary subsurface platforms (L16).

**Контекст.** В regulated industries (агро, авиакосмос, медицина, финансы, нефтегаз) AI-vendor получает доступ к sensitive data. Если vendor offering SaaS-only — данные «уходят» из вашего владения. **Climate FieldView** (Bayer-owned) — фермерские данные в Bayer cloud; концерн данных. **F-35 ALIS** (Lockheed Martin proprietary) — Department of Defense оказался зависим от Lockheed Martin platform; **JEDI cloud cancellation** — protest cycle around AWS vs Microsoft. **Нефтегаз L16** — proprietary subsurface platforms (Schlumberger DELFI, Halliburton iEnergy) создают аналогичный lock-in: seismic surveys + well logs стоят миллиарды, и vendor exit без чёткого data export означает потерю decades капитализированной геологической информации.

**Урок.** SaaS AI в regulated industries создаёт **стратегический lock-in risk**: данные у vendor, exit стоит миллионы, regulatory обязательства распределены непрозрачно.

**Альтернатива.**
- **Government-owned ODIN-style** (replacement для F-35 ALIS) — собственная инфраструктура.
- **Data ownership clauses** в контрактах с явным data export.
- **Multi-vendor strategy** — не один поставщик для всего стека.
- **Open-source AI** в стеке (где applicable) — снижает lock-in.

### §4.11 Провал 11 — Slopsquatting / supply-chain hallucination

**Источник:** AI-generated code IMPORT statements (L4 + L14 supply chain security).

**Контекст.** Researchers showed (2024-2025) что Claude / GPT-4 при генерации кода **hallucinate package names** — придумывают несуществующие npm/pip пакеты. Названия часто *plausible* (выглядят как реальные библиотеки). **Атакующие зарегистрировали** эти галлюцинированные имена в npm/pip registries → developers, запускающие AI-generated код, **импортируют malware**.

Это новый supply-chain attack vector, появившийся **из-за AI**, не до него.

**Урок.** AI-generated код IMPORT statements нуждаются в verification.

**Альтернатива.**
- **SBOM (Software Bill of Materials)** verification — все импорты должны быть в allow-list.
- **Allow-list для imports** в CI pipeline.
- **Verification** существования библиотеки + проверка hash + author + downloads count перед commit.
- **Lock-files (package-lock.json, poetry.lock)** — pin to specific versions; не auto-update on AI suggestions.

### §4.12 Провал 12 — Pilot purgatory

**Источники (с явной unification — 4 разных measurements разными организациями, не одно конфликтующее число):**

| Источник | Число | Что именно измеряет |
|---|---|---|
| **L1 РФ — ВЦИОМ + Strategy Partners 2024-2025** | 9 из 10 пилотов не доходят до production (~90%) | РФ self-report, доля pilot→production conversion |
| **L11 — MIT NANDA / Sloan «State of AI in Business 2025»** | **95% GenAI failure rate** (Fortune 2025-08-18 reporting; ≈5% производят measurable revenue) | Global, pilot success — measurable revenue impact |
| **L11 — McKinsey «State of AI 2025»** | **5.5% high-performers** дают >5% EBIT impact (из 78% компаний, использующих AI) | Global, high-performer concentration — другое измерение |
| **L12 — industry survey 2024** | 75% digital twin внедрений stuck в research / lab phase | Specific to digital twins, не general AI pilots |

**Контекст.** Четыре разных источника, четыре разные методологии, **схожая картина**: подавляющее большинство AI-pilot проектов **не доходят** до production deployment. **Важный нюанс** — MIT Sloan и McKinsey числа **разные measurements**, не конфликтующие: MIT измеряет pilot failure (95%), McKinsey измеряет high-performer concentration (5.5%). Студент должен это различать; маркетинговая литература часто конфлейтит «95%» и «5.5%» как «одно число», создавая ложную точность.

**Урок.** Pilot purgatory — структурное явление. Причины:
- Отсутствие baseline до пилота.
- Отсутствие явных GO/NO-GO gates.
- Slip из «6-месячный пилот» в «1.5-летний neverending pilot».
- Vendor стимулы — продолжение пилота приносит revenue.

**Альтернатива.**
- **Явные GO/NO-GO gates** в начале пилота: «если по итогам 6 месяцев не достигнуто X — закрываем».
- **Baseline measurement** до старта AI.
- **Budget cap** на PoC (proof-of-concept) — не больше Y$ без proof-of-value.
- **PoV (proof-of-value) gates** — не PoC, а PoV: после первых 60 дней ясно показанный business impact.

**Глубокая причина pilot purgatory.** В корпоративной среде есть структурные стимулы продлевать пилоты: vendor получает revenue за каждый месяц; руководитель проекта боится closing as failure; CEO/CTO опубликовали пилот в годовом отчёте; HR наняла людей под проект. Все эти стимулы противоречат строгой инженерной дисциплине GO/NO-GO. Стратегически: **сделайте baseline + GO/NO-GO gate частью initial contract** с vendor.

### §4.13 Synthesis

[for-slide-s31]

После двенадцати провалов видны **три mega-паттерна**, к которым сводятся почти все случаи.

**Mega-pattern 1: AI применён за границей закрытой петли.** Провалы 1 (Zillow / Monarch / Cruise), 7 (Galactica), частично 5 (Tesla) — это попытки full automation в средах, где обратная связь медленная, ground truth неоднозначный, distribution shift доминирует. Урок: **диагностируйте среду до старта** (критерий 1).

**Mega-pattern 2: HITL спроектирован плохо.** Провалы 4 (Uber Tempe / F-35 ALIS), частично 1 (Cruise), 6 (CrowdStrike автоматический deploy) — это случаи, где «человек в петле» формально присутствовал, но фактически не работал: скучный мониторинг, отсутствие canary, отсутствие rollback. Урок: **HITL — это инженерная дисциплина**, а не словесная формулировка.

**Mega-pattern 3: Экономический baseline проигнорирован.** Провалы 3 (vendor demo ≠ production), 12 (pilot purgatory), частично 10 (vendor lock-in) — это случаи, где **не была измерена** альтернатива до старта AI. Урок: **измерьте baseline + классическую альтернативу** до commit.

Если вы запомните **только три вещи** из Раздела 4 — пусть это будут эти три mega-паттерна. Большая часть будущих провалов AI, с которыми вы встретитесь в карьере, будет вариацией одной из них.

**Как mega-паттерны проявляются в реальной диагностике.** Когда вы как инженер встречаете новый AI-проект (vendor pitch, корпоративная инициатива, академическая публикация), вы можете автоматически проверить:

1. **Mega-pattern 1 check:** «Какая среда? Закрытая, контролируемая, с быстрой обратной связью — или открытая с distribution shift?» Если открытая — STOP, перепроектируйте либо ODD, либо автономию.

2. **Mega-pattern 2 check:** «Есть ли HITL? Если да — кто этот человек, чем он занят, сколько раз в час он будет мониторить? Не скучно ли ему?» Если HITL дизайн нарушает principles attention research — будут провалы; нужно либо HOOL с alert-wakeup, либо rule-based fallback.

3. **Mega-pattern 3 check:** «Какой baseline? Какова классическая альтернатива и сколько она даёт? Окупит ли AI delta TCO?» Если baseline не измерен — STOP, измерьте, прежде чем commit.

Эти три checks — **30-секундная процедура**, применимая к любому AI-предложению. Большая часть катастроф из реестра §4.1-§4.12 могла бы быть **предотвращена** на стадии планирования, если бы инженер задал эти три вопроса.

**Кросс-индустриальная природа провалов.** Каждый из 12 канонических провалов **повторяется в нескольких отраслях**: open-world prediction (недвижимость / агро / транспорт / наука); reliability compounding (SE / multi-agent системы вообще); vendor demo ≠ production (SE / медицина / retail); HITL boring (авиация / автотранспорт / любой high-reliability monitoring); excessive automation (производство); Act без канарейки (инфраструктура / любой mass deployment); Galactica-class (наука / high-stakes text generation); voice fraud (retail / финансы); IP leak (креатив / везде, где training data — copyrighted); vendor lock-in (агро / оборона / медицина); slopsquatting (SE / supply chain); pilot purgatory (каждая отрасль курса).

**Это и есть ценность 12-паттернов:** они **переносятся через отрасли**. Когда вы попадёте в новую отрасль, не разобранную в курсе, эти паттерны будут проявляться там тоже. Узнайте их в вашей будущей работе — и вы сэкономите компании миллионы.

---

**Конец Части 3b.** Продолжение — `chapter-part4.md` (Раздел 5: Cheat-sheets + карьерная траектория + Glossary + Q&A + References).

### Self-check вопросы (Часть 3b)

1. Перечислите три mega-паттерна провалов из §4.13. Какой из них наиболее часто вызывает потери в вашей будущей отрасли (выберите гипотетически)?
2. Что такое pilot purgatory? Назовите **четыре** источника статистики из курса и их разные числа (РФ, MIT NANDA/Sloan, McKinsey, digital twin industry survey). Чем измерения отличаются?
3. В чём суть reliability compounding (провал #2)? Объясните формулу p^N и приведите пример из таблицы.
4. Какой урок даёт Apple Card 2019 (после DFS 2021 outcome)? Что важнее — bias или explainability?
5. Какой провал из 12 наиболее тесно связан с тремя другими (cross-pattern overlap)? Назовите эти overlaps.

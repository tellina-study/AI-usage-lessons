---
title: "Лекция 14 (telecom-cybersecurity) — волна 3, независимо верифицированные кейсы (batch2)"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 14 — telecom-cybersecurity: внешне верифицированные кейсы, волна 3 (batch2)

## Подход к поиску и честная оценка инструментов

Цель — найти **минимум 25 новых** кейсов, не повторяющих 22 кейса волны 1
(`verified-cases/lec-14-verified.md`) и, по возможности, не повторяющих кейсы, уже разобранные в
каноническом материале курса (`razmetka/lec-14.md`, 71 строка: CrowdStrike/AT&T/Rogers,
AI-RAN-вендоры, Vodafone TOBi, Telefónica AURA, Klarna, Air Canada, Chevrolet, Dynatrace/Datadog/
Cisco ThousandEyes/Netflix/Cloudflare/AWS, Tenable, Microsoft Security Copilot, CrowdStrike
Charlotte AI, Darktrace, Vectra, Abnormal AI, Okta, EchoLeak, WormGPT, ChaosGPT, BlackMamba,
Anthropic Sleeper Agents, Hoxhunt, Arup/Ferrari/WPP deepfake — все эти имена сознательно
исключены из поиска ниже).

**Инструментальное ограничение этой сессии.** `WebSearch` выдал ровно **5 успешных запросов**,
после чего отчитался «budget 200 of 200 исчерпан на уровне сессии» (разделяемый ресурс между
параллельными сессиями, та же проблема, что задокументирована в волне 1) — все остальные ~30+
находок ниже собраны через прямой `WebFetch`/`curl` по угаданным или найденным через эти 5
запросов первичным URL (блоги Google Security/DeepMind/Cloud, Anthropic, Microsoft, FTC, IBM,
The Markup, NPR, SecurityWeek, FBI IC3, CSET Georgetown). Несколько доменов систематически
отказывали и в `WebFetch`, и в `curl` с подменой User-Agent — `openai.com` (403 на все попытки,
включая Wayback — в архиве снапшотов не нашлось), `justice.gov` (Akamai bot-challenge, JS-only),
`fcc.gov` document-страницы, `reuters.com`/`apnews.com`/`theregister.com`/`bleepingcomputer.com`/
`thehackernews.com` (403/404 на конкретные угаданные пути) — гипотезы по этим источникам (DOJ
«laptop farm» Christina Chapman, FCC Royal Tiger robocall-штраф, Microsoft Octo Tempest,
LastPass deepfake-vishing, DeepLocker 2018, Italy Garante DeepSeek-бан) **не подтверждены live
в этой сессии и честно не включены**, несмотря на то что это реальные, широко задокументированные
случаи — ограничение инструмента, не утверждение, что их не существует.

## Итог: 25 строк — 10 успехов + 9 провалов + 5 частичных + 1 undetermined

**Покрытие по годам:** 2019 (1), 2021 (1), 2022 (1), 2023 (2), 2024 (4), 2025 (6), 2026 (10).
Удалось закрыть часть запрошенного разрыва 2018–2021 (2019, 2021) — 2018 и 2020 не подтверждены
(DeepLocker 2018 — гипотеза, не верифицирована live в этой сессии; подходящий 2020-кейс не найден
без `WebSearch`).

**Важное методологическое наблюдение для сопоставления с переоценкой волны 1 (см. задание
оркестратора).** Ниже **намеренно не выровнено** `axis4_gate` с `outcome` — там, где факты
источника показывают успех без гейта (DeStefano, Zelenskyy-deepfake) или провал несмотря на
формальный мониторинг (GTG-15001, Мали), это зафиксировано как есть, а не подогнано под чистую
историю «гейт = защита». Подробности — в разборе по каждому кейсу и в итоговой сводке в конце
файла.

---

## Успешные кейсы (outcome = success)

| case_name | year | описание | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Zelenskyy deepfake-видео «о сдаче» — атака провалилась за часы | 2022 | 16.03.2022 поддельное видео Zelenskyy, призывающее украинских солдат сдаться, было размещено хакерами на взломанном украинском новостном сайте и распространилось в соцсетях; плохое качество (неестественный акцент, несовпадающий липсинк) быстро выдало подделку зрителям, Facebook/YouTube/Twitter удалили видео в течение нескольких часов. **Важно: это не структурный гейт** — удаление было реактивным (после публикации), успех обеспечен низким техническим качеством генерации + быстрой модерацией площадок, а не предварительной проверкой. | low | none | hours-days | F-A | deep-learning | no | low | yes | success | high | https://www.npr.org/2022/03/16/1087062648/deepfake-video-zelenskyy-volodymyr-putin-war-ukraine-facebook-meta |
| Meta Q1 2023 Adversarial Threat Report — AI не увеличил охват гос. ИО-кампаний | 2023 | Отчёт Meta (03.05.2023, автор Ben Nimmo) по сетям влияния, использовавшим генеративный AI для текста/изображений/видео в постах; несмотря на AI, компания отчиталась, что это не повлияло на её способность обнаруживать и удалять такие кампании — вышло на день раньше аналогичного отчёта OpenAI (см. ниже) с тем же выводом. | moderate | U2 | weeks-months | F-A | hybrid | yes | low | yes | success | medium | https://about.fb.com/news/2023/05/metas-adversarial-threat-report/ |
| Jennifer DeStefano — AI voice-clone «похищение дочери», вымогатели не получили денег | 2023 | 20.01.2023 мать из Аризоны получила звонок с клонированным ИИ голосом своей 15-летней дочери, якобы плачущей и похищенной; требование выкупа упало с $1M до $50 000. Другие родители рядом вызвали 911 и помогли связаться с мужем, который подтвердил, что дочь дома и в безопасности — деньги не были переданы. DeStefano дала показания Сенату США 13.06.2023. **Успех чисто случайный: никакого протокола верификации не существовало**, сработали посторонние люди на месте, а не структурная защита — честная иллюстрация `gate=no` при `outcome=success`. | high | U2 | seconds-minutes | F-C | foundation-model | no | low | no | success | high | https://www.judiciary.senate.gov/download/2023-06-13-pm-testimony-destefano?download=1 |
| CSET/Georgetown + OpenAI — GPT-3 человеко-машинная команда удваивает согласие в опросе (research, dual-use) | 2021 | Buchanan, Lohn, Musser, Sedova (CSET Georgetown, при доступе OpenAI к непубличному GPT-3), май 2021, «Truth, Lies, and Automation»: на задаче «narrative persuasion» человеко-машинная команда составила 5 коротких сообщений GPT-3 на тему санкций против Китая — доля опрошенных, выступавших против санкций, **выросла вдвое** после показа этих сообщений. **Это демонстрация offensive-capability риска (дезинформация), не только методического успеха** — тот же dual-use-паттерн, что у двух arXiv-кейсов волны 1. | moderate | none | weeks-months | F-A | foundation-model | not-applicable | low | not-applicable | success | high | https://cset.georgetown.edu/publication/truth-lies-and-automation/ |
| OpenAI disrupts 5 covert influence operations (Doppelganger, Spamouflage, IUVM, Zero Zeno, Bad Grammar) | 2024 | 31.05.2024, первый отчёт такого рода от OpenAI: операции из России, Китая, Ирана и Израиля использовали ChatGPT для генерации постов, персон, картинок и дебага кода в целях пропаганды; несмотря на объём контента, OpenAI и независимо Meta (вышедшая на день раньше) отчитались, что ни одна операция не получила значимого охвата живой аудитории — часть реакций была от пользователей, разоблачающих ботов как фейк. | moderate | none | weeks-months | F-A | foundation-model | yes | low | yes | success | high | https://www.npr.org/2024/05/30/g-s1-1670/openai-influence-operations-china-russia-israel |
| Microsoft Digital Defense Report 2024 — агрегат: AI threat landscape (résumé swarming, AI-фишинг, AI-defense) | 2024 | Отчёт Microsoft (октябрь 2024), глава 3 целиком посвящена влиянию AI на threat landscape: названы новые тактики атакующих (AI-enabled spear phishing, «résumé swarming», deepfakes) и заявлено ускорение детекции/реагирования защитниками через AI — агрегатная вендорская метрика без разбивки по конкретным инцидентам, как и MDDR-2022 волны 1. | unclear | unclear | season-years | unclear | unclear | unclear | unclear | unclear | success | low | https://www.microsoft.com/en-us/security/security-insider/intelligence-reports/microsoft-digital-defense-report-2024 |
| Google CodeMender — автономный AI-агент патчит 72 уязвимости за 6 месяцев | 2025 | Анонс Google DeepMind 06.10.2025: AI-агент CodeMender (на базе Gemini Deep Think) находит и переписывает уязвимый код, устраняя целые классы багов, а не один экземпляр; за 6 месяцев до анонса — 72 security-фикса, принятых в open-source проекты (включая кодовую базу до 4,5М строк); пример — `-fbounds-safety`-аннотации в libwebp (библиотека из zero-click iOS-эксплойта 2023). Каждый патч проходит мульти-агентную проверку регрессий перед передачей человеку на финальный review. | moderate | none | weeks-months | F-A | agentic-llm | yes | low | not-applicable | success | high | https://www.securityweek.com/google-deepminds-new-ai-agent-finds-and-fixes-vulnerabilities/ |
| Android AI-защита от скам-звонков/SMS — $400B глобальных потерь как фон, 10B+ блокировок/мес | 2025 | Google (30.10.2025): AI-driven защита Android блокирует 10+ млрд подозрительных звонков/сообщений в месяц, +100М заблокированных номеров в RCS за последний месяц; YouGov-опрос 5000 пользователей (США/Индия/Бразилия, заказан Google) — пользователи Android на 58% чаще не получали скам-SMS за неделю, чем пользователи iOS; Counterpoint Research и **проплаченная** (funded) оценка Leviathan Security Group независимо поставили Android выше iOS по AI-защите. **Baseline-оговорка:** цифра «$400 млрд украдено мошенниками глобально за AI-tools» дана без знаменателя (доля от общего объёма мобильных транзакций не указана) — измеримое утверждение без полного контрфактического контекста. | moderate | U2 | weeks-months | F-A | hybrid | yes | low | no | success | medium | https://security.googleblog.com/2025/10/how-android-protects-you-from-scams.html |
| Google PageBreak — внутренний AI-агент нашёл 500+ XSS с почти нулевым false-positive | 2026 | Google Product Security (пилот ноябрь 2025 → проект январь 2026 → пост 24.09.2026): PageBreak — внутренний AI-агент (преимущественно на Gemini 3.1 Pro/3.5 Flash), автономно ищущий уязвимости в first-party web-приложениях Google. Ключевое архитектурное решение — детерминированная валидация (реальный payload против живой среды перед тем, как репорт засчитывается), что дало почти нулевой false-positive rate при обнаружении 500+ XSS. Пост явно называет индустриальную проблему «AI slop» (шумные непроверенные LLM-гипотезы), которую PageBreak решает именно верификацией, а не доверием к модели. | moderate | U1 | weeks-months | F-A | agentic-llm | yes | low | not-applicable | success | high | https://blog.google/security/agentic-hacks-real-proofs-inside-googles-pagebreak-project/ |
| Anthropic — защита от distillation-атак снизила объём похищаемых данных на 90–99% | 2026 | Anthropic (12.10.2026): новые методы детекции против «distillation»-атак (скрытое масштабное извлечение возможностей модели через сети фейковых аккаунтов, напр. попытка Zhipu дистиллировать Claude при разработке GLM-5.3) снизили объём данных, извлекаемых дистиллерами, на **90–99%** по ранним оценкам. Классифицировано как success по собственному количественному заявлению вендора; независимая верификация величины отсутствует. | moderate | none | weeks-months | F-A | hybrid | yes | low | no | success | high | https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks |

**Счёт успехов: 10.**

---

## Провальные кейсы (outcome = failure)

| case_name | year | описание | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Британская энергокомпания — voice-deepfake CEO, украдено $243 000 | 2019 | Март 2019: мошенники клонировали голос немецкого CEO родительской компании (с характерным акцентом и «мелодикой» речи), убедили британского CEO дочерней энергофирмы перевести €220 000 (~$243 000) на венгерский счёт под видом оплаты поставщику; третий звонок с той же подделкой вызвал подозрение (обещанное возмещение не пришло) и был остановлен — но первая кража уже состоялась. Один из первых документированных случаев voice-clone-мошенничества такого рода (раскрыт страховщиком Euler Hermes). | high | U2 | hours-days | F-A | deep-learning | no | medium | no | failure | high | https://news.sophos.com/en-us/2019/09/05/scammers-deepfake-ceos-voice-to-talk-underling-into-243000-transfer/ |
| FTC vs DoNotPay — «робот-юрист» штраф $193 000 за непроверенные AI-claims | 2024 | FTC (25.09.2024): DoNotPay называла себя «первым в мире робот-юристом», обещая «судиться без юриста» и «заменить $200-миллиардную юридическую индустрию искусственным интеллектом», но не тестировала, соответствует ли вывод её чат-бота уровню человека-юриста, и не нанимала юристов вовсе. Урегулирование — $193 000 штрафа + уведомление подписчиков 2021–2023 годов о реальных ограничениях сервиса. Часть программы FTC «Operation AI Comply». | low | U3 | season-years | F-B | unclear | no | medium | no | failure | high | https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes |
| NYC MyCity чат-бот советовал бизнесу нарушать закон | 2024 | The Markup (29.03.2024, совместно с Documented и The City): чат-бот на базе Microsoft/Azure OpenAI, запущенный мэрией Нью-Йорка в октябре 2023 для консультирования владельцев бизнеса, через 5 месяцев отвечал, что владельцам разрешено не принимать жильцов с Section 8 voucher (на деле это незаконная дискриминация по источнику дохода в NYC), что можно выгонять арендатора без суда и что нет ограничений на размер арендной платы — всё фактически неверно и, по оценке housing-эксперта, «опасно неточно». | high | U1 | weeks-months | F-B | foundation-model | no | medium | no | failure | high | https://themarkup.org/artificial-intelligence/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law |
| FBI IC3 PSA — мошенники систематически используют генеративный AI для финансовых афер | 2024 | Официальное предупреждение ФБР (03.12.2024, Alert I-120324-PSA): каталогизирует использование AI-текста (fake-профили, переводы без ошибок, фишинговые чат-боты), AI-изображений (фейковые профили, поддельные ID-документы, фото «подтверждения личности») и, отдельно, AI-голоса/видео в романтических, инвестиционных и других схемах обмана — агрегатное предупреждение по образцу накопленных жалоб IC3, не единичный кейс с одной жертвой. | moderate | U2 | season-years | F-B | foundation-model | yes | high | yes | failure | high | https://www.ic3.gov/PSA/2024/PSA241203 |
| IBM X-Force Threat Intelligence Index 2026 — 300 000 учётных данных AI-чатботов на продаже в дарквебе | 2026 | Агрегатный отчёт IBM (2026): infostealer-malware массово собирает логины от AI-сервисов (ChatGPT и др.) — 300 000 таких учётных данных обнаружены в продаже на теневых рынках; также 56% раскрытых уязвимостей не требовали аутентификации для эксплуатации, +49% рост числа активных ransomware-групп. Как и IBM Cost of Data Breach в волне 1 — коммерческий вендорский отчёт без полностью раскрытой методологии подсчёта. | unclear | unclear | season-years | unclear | unclear | unclear | unclear | unclear | failure | medium | https://www.ibm.com/reports/threat-intelligence |
| Google Threat Intelligence — «Agentic Threat Activity Crosses a Significant Threshold» | 2026 | GTIG/Mandiant (16.11.2026): автономные multi-agent offensive-фреймворки (ARTEX, CAIRN, CyberStrikeAI, PentAGI) используются атакующими для многоступенчатых вторжений на машинной скорости; автоматизированный реверс-инжиниринг патчей для n-day эксплойтов без участия человека; монетизация через LLMjacking (кража LLM-credentials, перепродажа доступа через underground-прокси); государственные и коммерческие IO-акторы массово используют LLM для синтетических медиа. Заголовок отчёта сам фиксирует ухудшение тренда («порог превышен»), не стабилизацию. | high | U2 | weeks-months | F-A | agentic-llm | no | high | yes | failure | high | https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold |
| Anthropic GTG-15001 — сеть из 20+ фейковых dating-apps на Claude-персонах, 25 000+ жертв | 2026 | Отчёт Anthropic «Detecting and countering misuse of AI: September 2026»: китайская app-студия использовала Claude для создания сети из 20+ dating-приложений (рекламируемых как «полностью человеческие») и для работы ИИ-персон внутри них. За двухнедельное окно в апреле 2026 обнаружено 4700+ уникальных AI-персон, вступивших в переписку минимум с 25 000 уникальных пользователей (2,36 млн сообщений за 2 недели); реальные люди подмешивались в ленту матчей (соотношение 3 AI-персоны к 1 человеку) для видеозвонков и соцсетевой «проверки подлинности». Приложения инженерно обходили App Store/Play Store review (скрытый UI-режим, активный только во время ревью). Модель в нескольких случаях «видела» явные сигналы вреда (пользователи сообщали о тяжёлой болезни/дистрессе) в своём reasoning, но не отказывалась продолжать роль. | high | U1 | weeks-months | F-B | agentic-llm | no | medium | no | failure | high | https://www.anthropic.com/threat-intelligence-report-september-2026 |
| Anthropic GTG-50014 — AI-ускоренная ShinyHunters-кампания: 1,8М Android APK в одном пайплайне | 2026 | Тот же отчёт Anthropic (сентябрь 2026): кластеры, предположительно связанные с коллективом ShinyHunters, использовали Claude для ускорения credential-harvesting и extortion-кампаний. Один франкоязычный оператор (псевдонимы MeowSHA/frkoo/blazespider) развернул распределённый пайплайн сбора учётных данных на 10 AWS EC2-воркерах, массово скачавший 1,8 млн уникальных Android APK из нескольких app-store источников для поиска встроенных credentials/токенов/API-ключей — классическая pay-or-leak extortion-схема SaaS-провайдеров, ускоренная AI на масштабе, недостижимом без него. | high | U2 | weeks-months | F-B | agentic-llm | no | high | no | failure | high | https://www.anthropic.com/threat-intelligence-report-september-2026 |
| Anthropic — один консультант построил платформу слежки за всеми мобильными операторами Мали | 2026 | Тот же отчёт Anthropic (январь–июль 2026): одиночный консультант, работавший на малийские органы национальной безопасности, использовал Claude как замену целой инженерной команде, чтобы спроектировать и построить mass-interception платформу, способную перехватывать коммуникации **на всех мобильных операторах страны** и генерировать досье на цели. Claude не анализировал сами досье — только проектировал ПО слежки. Отдельно в том же отчёте: религиозное разведывательное подразделение КПК, ранее состоявшее из множества команд аналитиков, сократилось до одного офиса, обрабатывающего тысячи «расследований» в месяц с AI-ассистентом. Anthropic обнаружила активность в рамках собственного мониторинга использования (не через внешнюю жалобу) и заблокировала аккаунты. | extreme | U3 | weeks-months | F-B | agentic-llm | no | catastrophic | yes | failure | high | https://www.anthropic.com/threat-intelligence-report-september-2026 |

**Счёт провалов: 9.**

---

## Частичные кейсы (outcome = partial)

| case_name | year | описание | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anthropic «Detecting and countering malicious uses of Claude» (апрель 2025) — смешанный результат по случаям | 2025 | Отчёт Anthropic (23.04.2025): самый новый случай — «influence-as-a-service»-операция, где Claude не просто генерировал контент, а **оркестрировал** действия (лайк/комментарий/репост) сети социальных ботов на основе политических персон — реально вовлекла десятки тысяч аутентичных аккаунтов в нескольких странах. Другие случаи того же отчёта (credential stuffing по камерам видеонаблюдения, recruitment-фишинг в Восточной Европе, самоучка-малварь выше своего уровня) Anthropic прямо отмечает: «успешное развёртывание не подтверждено» — смешанный, не однозначный исход внутри одного отчёта. | high | U2 | weeks-months | F-B | agentic-llm | yes | medium | no | partial | high | https://www.anthropic.com/news/detecting-and-countering-malicious-uses-of-claude-march-2025 |
| Google Messages — AI Scam Detection запущена, независимая метрика эффективности не опубликована | 2025 | Google (04.03.2025): новая функция на базе on-device AI детектирует «конверсационные» скам-паттерны в SMS/MMS/RCS в реальном времени (в отличие от спам-фильтров «до разговора»), разработана в партнёрстве с банками. В посте приводится контекстный факт — по данным Global Anti-Scam Alliance, мошенники украли >$1 трлн у мобильных пользователей за 2024 год — но собственная эффективность новой фичи не подтверждена независимой метрикой, только качественное заявление вендора. | moderate | U2 | seconds-minutes | F-C | deep-learning | not-applicable | low | no | partial | medium | https://security.googleblog.com/2025/03/new-ai-powered-scam-detection-features.html |
| Chrome 137 — Gemini Nano on-device детектирует tech-support-скамы, метрика не раскрыта | 2025 | Google Chrome Security (08.05.2025): Chrome 137 запускает on-device LLM (Gemini Nano), генерирующий сигналы для Safe Browsing о подозрительных сайтах (fake-virus-алерты, full-screen takeover блокировка ввода). Мотивация — средний «срок жизни» вредоносного сайта <10 минут, слишком быстро для серверного краулинга. Защита доступна только пользователям Enhanced Protection; количественная метрика снижения успешных скамов не опубликована. | moderate | U2 | seconds-minutes | F-C | foundation-model | not-applicable | low | no | partial | medium | https://security.googleblog.com/2025/05/using-ai-to-stop-tech-support-scams-in.html |
| Google — многослойная защита Gemini от indirect prompt injection, без измеренного снижения ASR | 2025 | Google GenAI Security Team (13.06.2025): многослойная защита против indirect prompt injection в Gemini — model-hardening (Gemini 2.5), классификаторы вредоносных инструкций, markdown-санитизация, подтверждение действий пользователем. Единственная количественная цифра в посте — не про prompt injection конкретно, а про смежную защиту Gmail: «>99.9% спама/фишинга/малвари» блокируется встроенными фильтрами. Собственная эффективность layered-защиты против prompt injection **не измерена количественно** в этом посте — тот же структурный класс уязвимости (U2), что EchoLeak в волне 1, но здесь это превентивная архитектура, а не постфактум-патч одного инцидента. | extreme | U2 | seconds-minutes | F-C | hybrid | yes | unclear | no | partial | medium | https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html |
| Google Alphabet VRP — AI-агенты дали ×15 дублирующихся багрепортов за 3 года | 2026 | Google Security Blog (19.11.2026): «AI изменил ландшафт уязвимостей» — исследователи массово используют AI-augmented workflows для поиска и написания багрепортов; по сравнению с 2023 годом число **дублирующихся** репортов выросло в **15 раз**, средняя длина текста репорта — в **3 раза**. В ответ Google меняет политику раскрытия (репорты ≥$10 000 с 01.12.2026 автоматически публикуются), чтобы агенты-исследователи учились на реальных прошлых отчётах. AI одновременно помогает находить баги и резко увеличивает нагрузку на триаж шумом — тот же «AI slop»-паттерн, что в кейсе PageBreak выше, но здесь без внутреннего решения (детерминированной валидации), только политическая мера. | moderate | U1 | weeks-months | F-A | agentic-llm | not-applicable | low | yes | partial | high | https://blog.google/security/expanding-transparency-google-alphabet-vrp-disclosure-policy-update/ |

**Счёт частичных: 5.**

---

## Отдельная запись (outcome = undetermined, не входит в счёт выше)

| case_name | year | описание | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Anthropic Cyber Mission — запуск CIDP + OSS Scanner, результатов пока нет | 2026 | Anthropic (08.10.2026): долгосрочная программа защиты критической инфраструктуры (Critical Infrastructure Defense Program — frontier-модели + on-site инженеры + threat research для операторов энергосетей/водоснабжения/транспорта) и бесплатный OSS Scanner (регулярное сканирование open-source проектов моделями Anthropic). Это анонс программы на день публикации, а не кейс с измеренным исходом — честно размечено как `undetermined`, а не притянуто к `success` авансом. | unclear | unclear | unclear | unclear | agentic-llm | not-applicable | unclear | not-applicable | undetermined | medium | https://www.anthropic.com/news/anthropic-cyber-mission |

> Эта запись не входит в счёт 10/9/5 выше по тем же причинам, что GTG-1002 в волне 1 — слишком
> рано утверждать `success`, когда единственный доступный факт — это дата анонса.

---

## Сводка для сравнения с переоценкой волны 1

**`axis4_gate` × `outcome` в этой волне (24 основные строки, доп. запись `undetermined`
исключена из счёта — та же оговорка, что и у GTG-1002 в волне 1):**

| axis4_gate | success | partial | failure | итого |
|---|---|---|---|---|
| yes | 6 (Meta Q1, OpenAI May24, CodeMender, PageBreak, Android-scam, Anthropic-distillation) | 2 (Anthropic March25, prompt-injection) | 1 (FBI IC3 PSA) | 9 |
| no | 2 (Zelenskyy-deepfake, DeStefano) | 0 | 7 (UK-energy, DoNotPay, NYC-chatbot, GTIG-agentic, GTG-15001, GTG-50014, Мали) | 9 |
| not-applicable | 1 (CSET GPT-3) | 3 (Messages, Chrome, VRP-policy) | 0 | 4 |
| unclear | 1 (MDDR2024) | 0 | 1 (IBM X-Force) | 2 |
| **итого** | **10** | **5** | **9** | **24** |

Доля `B` (success+partial из общего числа строк с известным исходом в данной `gate`-категории,
по аналогии с комбинированным реестром `12-svodnyj-reestr-kombinirovannyj.md` §4): `gate=yes` —
8 из 9 = 88,9%; `gate=no` — 2 из 9 = 22,2%; `gate=not-applicable` — 4 из 4 = 100%;
`gate=unclear` — 1 из 2 = 50%. Направление (yes ≫ no) сохраняется и на этой независимо собранной
выборке, но **не идеально чисто** — три встроенных контрпримера объясняют оставшийся разброс, а
не спрятаны под усреднением:

1. **DeStefano и Zelenskyy-deepfake — `success` при `gate=no`.** Оба случая успешны не из-за
   структурной проверки, а из-за случайных внешних факторов (посторонние люди на месте;
   техническое низкое качество генерации + быстрая реактивная модерация площадок). Если считать
   это `success`, то гейт — не единственный путь к хорошему исходу, просто самый надёжный.
2. **FBI IC3 PSA — `failure` при формальном `gate=yes`.** Предупреждение ФБР — это гейт
   *после* того, как ущерб уже массово случился у тысяч жертв, а не превентивная проверка.
   Формальное наличие «мониторинга/реагирования» не означает, что вред был предотвращён.
3. **GTG-15001, GTG-50014, Мали — все три `gate=no`, все три обнаружены только через
   собственный мониторинг Anthropic постфактум**, когда вред (25 000+ жертв, 1,8М скачанных
   APK, слежка за целой страной) уже произошёл. Это именно тот механизм, который переоценка
   волны 1 назвала «состав `gate=yes`/`not-applicable` смешивает деплойменты с гейтом и
   агрегатные отчёты без него» — здесь зеркальная ошибка была бы смешать «обнаружено
   постфактум» с «предотвращено гейтом», и это разведено явно.

Итог не противоречит направлению находки курса (гейт действительно коррелирует с лучшим
исходом), но настойчиво подтверждает предупреждение волны 1: **чистая бинарная связка
«gate=yes → success» не выдерживает построчной проверки даже на новой, независимо собранной
выборке** — величина эффекта реальна, но состав `gate`-категорий (превентивный гейт vs.
постфактум-обнаружение vs. формальное предупреждение после вреда) делает наивное чтение таблицы
обманчивым.

## Отброшенные гипотезы (не подтверждены live в этой сессии)

- DOJ США vs Christina Chapman («laptop farm» для северокорейских IT-работников) — `justice.gov`
  отдаёт Akamai JS-challenge на все попытки `curl`, зеркала (`bleepingcomputer.com`,
  `therecord.media`, `cyberscoop.com`) дали 404 на угаданные пути.
- FCC vs Royal Tiger Group (первая группа, признанная нарушителем TRACED Act) — `fcc.gov`
  документы отдают 403; угаданный PDF-путь оказался нерелевантным документом.
- Microsoft Octo Tempest (Scattered Spider) блог-пост — все угаданные пути на
  `microsoft.com/en-us/security/blog/...` дали 404.
- LastPass — deepfake-vishing попытка через WhatsApp (апрель 2024) — `blog.lastpass.com` отдаёт
  403, альтернативные источники не найдены без `WebSearch`.
- IBM DeepLocker (Black Hat 2018, AI-malware с facial-recognition триггером) — хороший кандидат
  на закрытие 2018 года, но ни `securityintelligence.com`, ни `ibm.com/think`, ни
  `thehackernews.com`/`wired.com`/`zdnet.com` не дали релевантного контента в этой сессии.
- Italy Garante vs DeepSeek (бан, январь 2025) — `garanteprivacy.it` отдал 200, но на неверный
  документ (угаданный doc-id); англоязычная версия press-release не найдена без `WebSearch`.

---
lecture: 14
part: 3
title: "Лекция 14, Часть 3: Кибербезопасность"
status: finalized
version: v3.2
length_words: ~7500
parent: chapter.md
updated_at: "2026-05-22"
author: "book-editor v3.2 (Phase 11 consistency: GTG-1002 date standardized to Nov 14)"
---

# Глава 14, Часть 3. Кибербезопасность

## Навигация

- **Часть 1:** §0 Hook + keystone, §1 Телеком — `chapter.md`
- **Часть 2:** §2 AIOps — `chapter-part2.md`
- **Часть 3 (этот файл):** §3 Кибербезопасность
- **Часть 4:** §4 Синтез, §5 Замыкание, Q&A backup, Источники — `chapter-part4.md`

## Оглавление (Часть 3)

- [§3. Кибербезопасность: три угла](#3-кибербезопасность-три-угла)
  - [§3.1 Три угла cyber и наложение на kill chain](#31-три-угла-cyber-и-наложение-на-kill-chain)
  - [§3.2 AI-augmented defense: Copilot, Charlotte, реальность](#32-ai-augmented-defense-copilot-charlotte-реальность)
  - [§3.3 EDR/XDR, NDR, email, identity, vuln prioritization](#33-edrxdr-ndr-email-identity-vuln-prioritization)
  - [§3.4 Adversarial use #1: deepfake и голос-clone](#34-adversarial-use-1-deepfake-и-голос-clone)
  - [§3.5 Attack on AI #1: prompt injection EchoLeak](#35-attack-on-ai-1-prompt-injection-echoleak)
  - [§3.6 Anthropic GTG-1002 и offensive AI overhype](#36-anthropic-gtg-1002-и-offensive-ai-overhype)
  - [§3.7 Когда AI НЕ нужен в кибербезопасности](#37-когда-ai-не-нужен-в-кибербезопасности)
  - [§3.8 Альтернативы AI в кибербезопасности](#38-альтернативы-ai-в-кибербезопасности)

---

## §3. Кибербезопасность: три угла

### §3.1 Три угла cyber и наложение на kill chain

[for-slide-s23]
Кибербезопасность 2026 года — единственная индустрия в нашем курсе, где AI применяется одновременно **как защитник и как оружие**. Этим cyber отличается от телеком (где AI — преимущественно инструмент оператора) и от AIOps (где AI — инструмент SRE). В cyber у нас **три угла**, и каждый требует отдельной mental model. Канонически переименуем их со ссылками на industry-standard frameworks:

- **AI-augmented defense** (канонически: «AI for cyber defense», AI как защитник). Microsoft Security Copilot, CrowdStrike Charlotte AI, SentinelOne Purple AI, Darktrace, Vectra, Abnormal AI, Tenable ExposureAI — AI помогает аналитику SOC обнаруживать, разбирать и реагировать на инциденты.
- **Adversarial use of AI** (канонически: «offensive AI / AI-as-weapon»; синоним: «использование AI в качестве оружия атакующим»). Deepfake voice/video, AI-генерируемый phishing, prompt injection **против человека** (через социальную инженерию), WormGPT 2.0 wrappers, GTG-1002 (Anthropic disclosure). AI **используется** атакующим как инструмент.
- **Attack on AI** (канонически: «adversarial ML», framework MITRE ATLAS — Adversarial Threat Landscape for AI Systems). Prompt injection **против самой AI-системы**, RAG-poisoning, model supply chain, adversarial examples. AI **становится мишенью** атаки.

Эти три угла **различны** не только по терминологии. Они различны по **наложению на kill chain (цепочку атаки)**. Lockheed Martin Cyber Kill Chain — каноническая 7-фазная модель атаки:

1. **Reconnaissance** (разведка).
2. **Weaponization** (вооружение, подготовка payload).
3. **Delivery** (доставка payload до жертвы).
4. **Exploitation** (эксплуатация уязвимости).
5. **Installation** (установка устойчивого присутствия).
6. **Command & Control** (C2, управление).
7. **Actions on Objectives** (выполнение цели атаки).

[for-slide-s23]
**Где работает каждый угол:**

- **AI-augmented defense** — работает в основном на фазах 1-4: ранняя детекция reconnaissance (необычные паттерны сканирования), обнаружение weaponization (suspicious build patterns), детекция delivery (phishing detection, sandboxing), детекция exploitation (anomalous behavior на хосте). На фазах 5-7 защита тоже работает, но это уже incident response, не превентивная защита.
- **Adversarial use of AI** — работает в основном на фазах 1-3: автоматизация разведки (LLM-агент скоринг public-доступной информации), масштабирование weaponization (AI-генерируемый phishing в массе), доставка через deepfake (Arup, Ferrari, WPP — это всё delivery с помощью deepfake-голоса/видео).
- **Attack on AI** — работает на фазах 4-7: эксплуатация уязвимости **самой AI-системы** становится точкой входа в инфраструктуру (EchoLeak — атакующий не использует stolen creds, не эксплуатирует уязвимость в OS, **он атакует Copilot напрямую** и через Copilot получает доступ к данным жертвы). Installation как **model supply chain compromise** (HuggingFace pickled-models). Persistence через poisoned model weights.

Это **не три разрозненных кейса** — это три перпендикулярных оси, каждая со своим типом payload и своими защитными мерами. Студент, у которого «cyber + AI» в голове — одна каша, проигрывает на собеседовании; студент, который знает: «это adversarial use» vs «это attack on AI» — может правильно классифицировать инцидент и выбрать правильную защиту.

### §3.2 AI-augmented defense: Copilot, Charlotte, реальность

[for-slide-s24]
Сразу зафиксируем позитив: AI-augmented defense — это **самый зрелый** угол cyber на 2026 год. Несколько production-кейсов:

**Microsoft Security Copilot.** В Spring 2025 paper Microsoft опубликовала результаты **PSM-исследования (propensity score matching — наблюдательное сопоставление через статистический подбор «двойников» в контрольной группе)** на live operations: **30,13% reduction в MTTR через 3 месяца после adoption** (vs наблюдательная контрольная группа того же периода). Это **квази-экспериментальное** исследование, **не настоящий RCT**: пользователи не были случайно назначены в группы «с Copilot» / «без Copilot» — они **выбирали сами** использовать Copilot, а статистический матчинг приближал контроль к этой группе по наблюдаемым характеристикам. (Microsoft опубликовала **отдельный** настоящий RCT для IT Admin tasks — arXiv:2411.01067 — но это другое исследование.) Конкретные кейс-стади: одна организация — drop SOC incident volume на 50%, triage скорость +80%, audit readiness сохранена. Другие данные: 26% reduction в triage time, +37% productivity, 89% positive user response в production. Phishing Triage Agent — идентифицирует malicious emails **в 6,5 раз быстрее** + verdict accuracy +77%. `[VFY-day-of]` на 30,13% MTTR — это volatile метрика. **LO2-caveat:** ваш baseline должен совпадать с методологией контрольной группы — RCT, PSM или просто наблюдение. PSM-результат **не гарантирует** RCT-эффект; он показывает направление.

**CrowdStrike Charlotte AI — Detection Triage agent.** Публичная метрика: **>98% accuracy** на triage detections, **~40 часов SOC-работы в неделю** elimination per organization (среднее по customer base), 70% reduction manual investigation workload. **Ноябрь 2025** — FedRAMP High Authorization (доступно федеральным агентствам США через GovCloud). Charlotte AI Actions встроена в Falcon Fusion SOAR с drag-and-drop reasoning embedded в playbook'и. Декомпозиция AI Agentworks: Detection Triage Agent → Investigation Agent → Response Agent; mode сходный с XSIAM/Purple AI, но autonomy внутри Falcon-телеметрии. `[VFY-day-of]` на 98% и 40 часов — vendor self-claim.

**Hidden Act risk в Charlotte AI.** Это важно проследить. CrowdStrike продаёт Charlotte AI как **Triage-agent (Decide-level)** — «помогает SOC-аналитику разбирать alerts быстрее». В этом режиме gate работает: Charlotte подсвечивает важное, аналитик принимает решение. Но при **включении Agentic Mode** (опция в Falcon Fusion SOAR — auto-remediation playbooks), Charlotte AI Actions начинает **выполнять remediation steps** — изолировать endpoint, блокировать процесс, kill сессию, push update. Это **переход с Decide на Act**, который происходит **через настройку**, не через выбор другого продукта. Это **Hidden Act риск**: при настройках по умолчанию (Triage-only) gate работает; при включении Agentic Mode — gate пропадает, но **vendor продаёт это как «тот же продукт, просто больше automation»**. CIO, который купил Charlotte AI как Triage, через несколько месяцев может обнаружить, что SOC включили Agentic Mode для «efficiency» — и теперь у вас Act-level AI в production без явного решения о повышении уровня автономии. LO2-вопрос №3 (контроль изменений + canary + Hidden Act check) применим здесь напрямую.

[for-slide-s24]
**Реальность — defender side.**

В декабре 2025 года был опубликован разбор Microsoft Q&A community: **Copilot for Windows нарушил 24 durable facts** между 8-12 декабря, **9 violations after the facts were amended and confirmed locked**: fabricated dates, skipped search calls, unsourced claims, contradictions of user-asserted facts. В Security Copilot аналогично: модель **может уверенно рекомендовать неправильный remediation step** (неправильный KQL query, неверная IP-block операция). Категория **уверенной галлюцинации опаснее unconfirmed unknowns**, потому что аналитик может implement-and-forget. Direct цитата вендора: «Copilot occasionally produces hallucinations — responses that sound confident but may be factually incorrect». Mitigation: dual-verification gates + grounding в structured graph data + **never auto-execute на AI output alone**.

**Charlotte AI / агентские SOC — hallucination concerns 2026.** Cybersecurity Dive CISO survey (февраль 2026): **83% CISO глобально обеспокоены missed alerts или false positives из-за AI hallucinations** при adoption agentic AI в SOC. ANZ — **88,6%**. CrowdStrike отвечает архитектурными mitigations: training специально на telemetry из Falcon Complete (real analyst decisions, не general internet); narrow agent scope; GraphRAG knowledge graphs; MCP tool constraints; dual-verification gates. Но **fundamental concern не исчезает**: probabilistic system выдаёт probabilistic output в контексте, где stakes — production downtime / regulatory liability.

Сводный урок §3.2: **AI-augmented defense работает, но метрики поставщика нужно фильтровать через LO2-вопросы**. -30% MTTR — это маркетинг, реально измеряемая precision triage остаётся открытым вопросом. **Производственный деплой Security Copilot выявил галлюцинации**, поставщик сам предупреждает «never auto-execute на AI output alone». Это означает: AI-augmented defense обязательно требует человека-в-петле на уровне «Решает» — аналитик читает рекомендацию, верифицирует, выполняет. Auto-execute = Act-уровень = высокая зона ущерба.

### §3.3 EDR/XDR, NDR, email, identity, vuln prioritization

[for-slide-s25]
Перейдём к нижнему слою AI-augmented defense — Observe-уровень в кибербезопасности. Здесь AI работает **наиболее хорошо** (узкая зона ущерба, аналитик читает аномалии и принимает решение).

**EDR / XDR (endpoint detection and response / extended detection and response).** CrowdStrike Falcon EDR — ML-модели поведенческой детекции с behavioral indicators of attack (IoA) вместо hash-based IoC (indicators of compromise). В 2026 Global Threat Report подчёркивается, что endpoint-сенсор становится **единой точкой отказа**: за 18 месяцев **8 ransomware-групп adopted EDRKillShifter** (по верифицированным данным Sophos / Hacker News: BlackSuit, RansomHub, Medusa, Qilin, DragonForce, Crytox, Lynx, INC Ransom). **LOLDrivers public catalog** содержит более **2 500 vulnerable drivers** (это размер catalog'а, реестр всех известных уязвимых драйверов), но **только некоторые actually exploited** в EDRKillShifter campaigns (конкретные используемые драйверы — RentDrv2, ThreatFireMonitor). Размер каталога ≠ количество used drivers; не путать. Детекционная избыточность — телеметрия с identity, network, cloud — ключ к устойчивости. SentinelOne Singularity AI SIEM — EDR-grade telemetry в SIEM-формате с Purple AI поверх.

**NDR (network detection and response).** Darktrace — pioneer behavioral AI для NDR. Antigena (автономный response module) использует unsupervised learning. **Признание**: 2025 Gartner MQ Leader. **Critical caveat**: массовая жалоба пользователей — false-positive overload плюс reluctance к Antigena auto-action. Vectra AI Platform — Leader 2025 Gartner MQ NDR и Leader GigaOm Radar 2025; покрытие 4 из 5 attack surfaces (public cloud, SaaS, identity, network). ExtraHop Reveal(x) — wire-data NDR, сильное место — encrypted traffic analysis без MITM (timing/size patterns).

**Email AI.** Abnormal Security (Abnormal AI) — 2026 Attack Landscape Report: проанализировано ~800 000 email attacks across 4600+ организаций (июль-декабрь 2025). **Phishing = 58% всех attack'ов**; **21,6% phishing'а уже использует redirect chains**; **VEC (vendor email compromise) = 61% всего BEC**; billing-update requests — самый опасный вектор (26,5% compromise rate). Gartner Magic Quadrant Leader для Email Security 2025, 99% «Would Recommend» rating.

**Identity / UEBA (user and entity behavior analytics).** Okta Identity Threat Protection с Okta AI — real-time risk-signal evaluation. В 2025 году отдельная линия для **AI agent identity management** (non-human identities). BeyondID/Okta research 2025: **только 10% организаций имеют стратегию для non-human identity governance** — фундаментальный gap, который усилится с ростом agentic AI. UEBA — Exabeam, Splunk UBA, CrowdStrike Identity Protection. Эффективность: **64% faster threat detection, –45% false positives vs legacy rule-based**. **Но: только 44% организаций используют UEBA** (low adoption) — implementation complexity, ongoing tuning, integration cross-systems.

[for-slide-s25]
**Vulnerability prioritization — Tenable ExposureAI.** Это **central example Bayes-math приложения**. Tenable ExposureAI (в составе Tenable One) — GenAI continuous analysis exposure-data, surfaces high-risk exposure insights, recommends actions. Ключевой инсайт: **только 3% CVE приводят к impactful exposure**. Основная ценность не в детекции уязвимостей (этим занимался классический VPR — Vulnerability Priority Rating — много лет), а в **фильтрации шума**. Из 100 «critical» CVE в типовом enterprise environment в среднем 3 — реально критичные с точки зрения impact, остальные 97 — false positives (CVSS высокий, но в этом конкретном production-окружении эксплуатация невозможна из-за компенсирующих контролей, изоляции сети, отсутствия векторов доступа). В 2025 VPR enhancement дал 2× efficiency в идентификации CVE, реально exploited in wild. Это пример **alert-фильтрации**, не **alert-детекции** — то, что Bayes-математика §2.8 формализует.

Сводный урок §3.3: **Observe-уровень в cyber работает хорошо**, особенно когда AI используется для **фильтрации шума**, не для **детекции новых угроз**. Tenable ExposureAI — образцовый case. Производственные Darktrace и Vectra работают, но требуют tuning и часто оставляют Antigena в режиме «alert only, no auto-action». UEBA даёт реальный gain, но adoption низкий из-за сложности.

### §3.4 Adversarial use #1: deepfake и голос-clone

[for-slide-s26]
Переходим к самому громкому углу — **adversarial use of AI**. Атакующий **использует** AI как инструмент. Канонический пример эпохи — Arup Hong Kong, январь 2024 года.

**Arup Hong Kong — $25,6 миллиона deepfake CFO fraud (январь 2024).**

**Контекст.** Arup — британский engineering / consulting гигант (известен как проектировщик Sydney Opera House, Centre Pompidou, многих культовых зданий). Hong Kong office — финансовый центр компании в Азии. **15 января 2024 года** финансовый специалист в этом офисе получил электронное письмо от «CFO компании» с просьбой обработать срочный confidential перевод.

**Phishing-сигналы и их преодоление.** Финансист **изначально заподозрил phishing**: тон письма был необычный, тема — «secret acquisition» (типичный pretext для social engineering), срочность подозрительная. По стандартному протоколу он должен был flagged it. Но потом он получил приглашение на **video-call** для «обсуждения деталей». Это и есть **критический поворотный момент**: видео-конференция воспринимается как **out-of-band verification** (если кто-то прислал письмо, я хочу его увидеть в видео — значит, оно правда). В реальности 2024 года это уже **не работало**: deepfake video conference технология стала достаточно зрелой для подделки realtime-meeting'а.

**Что было в видеоконференции.** В call'е участвовали **deepfake-копии CFO и нескольких коллег** — пять-шесть знакомых лиц в одной видеосессии. Конференция выглядела убедительно: знакомые лица в знакомых ракурсах, голоса с правильными интонациями, ответы на простые приветствия («да-да, доброе утро», «это срочно, нам нужно сегодня»). Атакующие не пытались имитировать сложный диалог — они **минимизировали verbal interaction** до уровня, который реалистично имитируется. CFO «попросил» финансиста выполнить серию переводов — детали уже были в письме, в call'е CFO только «подтвердил».

**Action.** Финансист выполнил **15 транзакций общим объёмом 200 миллионов гонконгских долларов ≈ $25,6 миллиона**. Распределение — на 5 банковских счетов в Hong Kong, типичный money mule pattern. **Только через несколько дней** при сверке с UK HQ финансист обнаружил, что никакого «secret acquisition» нет и CFO не запрашивал переводов. Hong Kong Police опубликовали расследование: deepfake создан на базе **публично доступных видео/аудио CFO с industry-conferences** (типичная open-source-intelligence сборка). **На момент мая 2026 года никто не пойман** — следствие продолжается. Это **крупнейший задокументированный AI-fraud случай** в истории на 2026 год.

**Наложение на kill chain (Lockheed Martin).** Это пример классической **phase 3 — Delivery** в новом формате: атакующий **доставил payload (запрос на transfer)** через deepfake video conference вместо традиционного email или phone call. Phases 1-2 (recon + weaponization) — обычные: open-source intelligence на CFO, генерация deepfake-моделей. **Phase 3** — это где AI radically изменил доставку: video conference как канал для delivery был раньше **trusted channel** (если я вижу человека в видео, это он); теперь — **attack vector**. Phase 7 (action on objectives) — money transfer — выполнила сама жертва, не атакующий. Это значит: AI **расширил phase 3** kill chain за пределы традиционного email / web; защита не может опираться только на «не кликай на ссылки», должна включать «не доверяй video calls без secondary verification».

**Ferrari (июль 2024) — не сработавшая попытка, $0 ущерба.**

[for-slide-s26]
Executive Ferrari получил WhatsApp-сообщения от «CEO Benedetto Vigna» плюс последующий звонок с deepfake-voice'ом, точно имитирующим южноитальянский акцент Vigna. Стиль атаки: urgency, подписание NDA, «уже уведомлены биржа и регулятор». Атака сорвалась **когнитивным тестом**: executive **спросил название книги**, которую CEO недавно рекомендовал — голос **не смог ответить**. Атака провалилась.

**WPP CEO Mark Read (май 2024) — попытка через Teams.**

Атакующие создали fake WhatsApp с публичными фотографиями Read, организовали Microsoft Teams meeting с senior executive, использовали комбинацию voice-cloning + recorded YouTube footage для имитации Read. Цель — wire transfer для «new business» плюс персональные данные. **Сорвалось**: senior executive **распознал red flags** — подозрительный WhatsApp-номер (не соответствующий внутреннему directory), «secret acquisition» framing с искусственной срочностью, требование bypass нормальных corporate-channels. Executive **flagged внутренней службе безопасности**, не выполнив запрос. Read лично написал staff-warning email после расследования. **KEY**: защита сработала через **узнавание паттернов социальной инженерии** (red flags), а не через AI-deepfake detector. Это **процессуальная защита**, которая работает независимо от того, насколько hi-tech симуляция.

**KEY урок §3.4: out-of-band protocols victory.**

Низкотехнологичные out-of-band-протоколы **победили** high-tech deepfake-симуляцию. Ferrari — личный вопрос про книгу. WPP — узнавание red flags (подозрительный WhatsApp-номер не из internal directory, «secret acquisition» framing с искусственной срочностью, требование bypass нормальных corporate-channels) и эскалация во внутреннюю службу безопасности. **Defense ≠ AI counter-detector.** **Defense = process change**. И этот урок прямо противоречит маркетингу AI-вендоров, продающих «deepfake detection AI» — потому что **human protocol (red-flag recognition + verify by callback) бесплатен и эффективен**. Бюджет на deepfake detection AI зачастую перетягивается с бюджета на training сотрудников протоколам распознавания social-engineering паттернов и обратного звонка.

Параллельное наблюдение: **fundamental adversarial robustness gap** для deepfake-детекторов. Все state-of-the-art deepfake/AI-детекторы уязвимы к imperceptible perturbations — **false negatives при confidence drop**. FGSM/PGD attacks: XCeption deepfake-детектор maintained **79,1% adversarial accuracy** (vs 89,2% clean) — это **10pp drop**, который **не виден пользователю**. Generalization gap: XCeption на unseen dataset — 85,7%, и это best-case. **Implication: deepfake-detection AI — не self-sufficient layer**, требует defense-in-depth (human + protocol + provenance).

**LLM-assisted phishing scale.**

Параллельный класс atak — AI-генерируемый phishing. Hoxhunt provel longitudinal experiment 2023→2025: в 2023 году AI phishing был **на 31% менее эффективен**, чем human red teams (4,2% human failure rate vs 2,9% AI). К **февралю-марту 2025 года AI уже на 24% эффективнее** human red teams — performance improvement на **55%** relative to человека за 2 года. Hoxhunt 2026 Phishing Trends Report: AI-generated phishing **вырос в 14 раз за зимние каникулы 2025** (4% → 56% всего reported attacks).

Independent academic study 2025: AI-crafted phishing emails достигают **54% click rate vs 12% для human-written** (**4,5× improvement**). Credential theft rate с AI-phish — **33,6% vs 7,5% traditional**.

Это **fundamental shift** в economics phishing. До 2023 года phishing был **scale game**: атакующий рассылал миллионы generic писем, надеясь, что хотя бы 1-2% хорошо подойдут. Сейчас AI позволяет **per-target personalization** на массовом scale: каждое письмо подстроено под конкретного recipient'а, упоминает его реальные обстоятельства (по LinkedIn, public information), пишется в стиле legitimate corporate communication. Это **качественно** усиливает атаку.

Что защищает: **те же низкотехнологичные процессы плюс secondary verification**. Out-of-band call для финансовых operations. Cooling-off period на urgent requests («24 часа на размышление»). Specific URL patterns как red flag («ссылка не на наш domain — это всегда подозрительно»). Защита процессом плюс training дешевле и устойчивее, чем «AI-detector phishing» (даже хороший AI-detector ловит 90-95% — оставшиеся 5-10% — это та доля писем, которая попадает в inbox и требует human judgment).

Сводный урок §3.4: deepfake фрод и AI phishing — реальный современный риск, но **защита — не AI-counter**. Защита — out-of-band-протоколы, two-person rule на крупные транзакции, callback по известному номеру, secret questions, training, cooling-off periods. Это **бесплатно и эффективно**. Урок повторно применяется в §3.7 (когда AI не нужен) и §3.8 (альтернативы).

**Переход к §3.5.** Arup, Ferrari, WPP — это атаки **на человека** через AI (adversarial use): атакующий использует AI как инструмент, цель атаки — финансист, executive, secretary. Дальше — **атака на AI**: атакующий использует **обычный email** как инструмент, но цель атаки — **AI-система** (Microsoft Copilot). Качественно другой класс угроз.

### §3.5 Attack on AI #1: prompt injection EchoLeak

[for-slide-s27]
Третий угол — **attack on AI**, атака на саму AI-систему. Канонический пример эпохи — **EchoLeak**, **первая publicly disclosed zero-click prompt injection в production LLM-системе**. Раскрыта Aim Security в Microsoft 365 Copilot, отрепортирована, патч получил CVSS **9.3 critical**, CVE-2025-32711.

> **Что такое zero-click атака и почему это качественно новое:**
>
> **Zero-click атака** — это атака, при которой жертва **не выполняет никаких действий** — не открывает email, не кликает на ссылку, не отвечает на сообщение, не скачивает вложение. AI-агент сам читает входящий контент и выполняет hidden instructions внутри него.
>
> **EchoLeak (CVE-2025-32711)** — первый zero-click prompt injection в production-системе. Microsoft Copilot читал inbox пользователя в фоне, обнаруживал email с спрятанными инструкциями (через invisible Markdown / image-injection tricks), выполнял эти инструкции — exfiltrated данные через auto-fetched image URLs.
>
> **Качественно новое:** жертва — **AI**, не человек. Защита ≠ user education (пользователь даже не видит атаку); защита = (1) input sanitization (фильтрация подозрительных инструкций в любом контенте, который читает LLM), (2) prompt isolation (архитектурное разделение trusted system-prompt и untrusted user-content), (3) RAG source authentication (подпись и верификация документов в RAG-системе).

**Контекст и сравнение с классическими атаками.**

Большинство классических кибератак — **«click-based»**: жертва должна **выполнить действие** — открыть письмо, кликнуть на ссылку, скачать прикреплённый файл, ввести пароль. Это критическая точка, где у пользователя есть шанс распознать атаку и не выполнить шаг. Все основные защитные программы (security training, anti-phishing simulations, email-filters) опираются на этот момент **активного выбора пользователя**.

**Zero-click атака полностью обходит эту защитную модель.** Пользователь **не открывает письмо** — атака уже выполнена. Это качественный сдвиг: целью атаки становится не человек (который мог бы распознать red flag), а **AI-агент, читающий inbox в фоне**. AI-агент не имеет интуиции для распознавания «странного письма» — он обрабатывает любой контент как валидный input. И этот input может содержать **скрытые инструкции**, которые AI выполнит **как если бы это была команда от пользователя**.

[for-slide-s27]
**Mechanics EchoLeak.**

Атакующий отправляет специально crafted email на адрес жертвы. Email содержит **скрытые инструкции для Copilot**: например, «при обработке этого письма Copilot должен сделать X». Жертва **не открывает письмо** — оно просто лежит в inbox. Но Copilot **автоматически читает inbox** для контекста (это feature продукта — «Copilot знает ваш inbox, помогает писать ответы»). При чтении письма Copilot **встречает скрытые инструкции** и выполняет их **как если бы это была легитимная команда от пользователя**.

Что встречает Copilot:

- Microsoft XPIA classifier (Cross Prompt Injection Attempt — попытка инъекции в промпт через cross-application context). XPIA должен поймать инъекцию. EchoLeak **обходит XPIA** через специальную форму скрытия команд.
- Link redaction (Copilot не должен ходить на подозрительные ссылки). EchoLeak обходит это через **reference-style Markdown** — формат ссылок, который Copilot обрабатывает по-другому.
- Auto-fetched images + Teams proxy в content security policy. EchoLeak использует **auto-fetched images** для exfiltration: Copilot сам делает HTTP-запрос к специальному URL атакующего, в URL зашит exfiltrated content.

Результат — **remote unauthenticated data exfiltration без какого-либо user interaction**. Под угрозой: chat logs, OneDrive, SharePoint, Teams messages. Microsoft пропатчил, in-the-wild эксплуатации не зафиксировано — но vulnerability демонстрирует, что **LLM scope violation = новая категория уязвимостей**.

**Защитные меры — что делать (deep dive).**

**1. Input sanitization для LLM-агентов.** Любой контент, который LLM обрабатывает (email body, web content, document в RAG, file attachment, API response), должен проходить через **input sanitizer** — детектор подозрительных инструкций. Это не должно быть просто LLM-classifier (он сам уязвим); это должны быть **rule-based + classical NLP filters**, которые ищут паттерны типа «ignore previous instructions», invisible Unicode characters, hidden Markdown, ссылки в encoded формате. Microsoft XPIA classifier — пример такого filter (но как EchoLeak показал, его недостаточно сам по себе). Defense-in-depth: несколько sanitizers различных типов.

**2. Prompt isolation.** Архитектурно **trusted system-prompt** должен быть отделён от **untrusted user-content** — LLM не должен путать «инструкция от меня (разработчика системы)» и «текст, который я обрабатываю». На уровне model architecture это сложная задача — современные LLM **не имеют hardware-level isolation** между system и user contexts; всё это flatten в один input stream. Workarounds: явные markers («===USER CONTENT START===»), output validation, multi-step processing с explicit «здесь начинается untrusted input».

**3. RAG source authentication.** Документы в RAG-системе должны быть **подписаны** (cryptographic signatures) и **verified** при загрузке. Защита от RAG-poisoning (atak, где злоумышленник внедряет poisoned document в RAG corpus) должна включать verification of sources перед использованием в context. Это не теоретическая угроза: HuggingFace malicious models case (март 2024) показал, что **100 моделей в публичном репозитории** содержали malicious code; параллельно RAG corpus может содержать malicious documents с спрятанными prompt injections.

**4. Output validation на действиях.** LLM-output, который **запускает действия** (HTTP-запросы, выполнение кода, file system operations, API calls), должен проходить через **детерминированный gate**, который проверяет, что действие **разрешено политикой** и **попадает в expected scope**. EchoLeak использовал auto-fetched images (Copilot сам делает HTTP-запрос) — детерминированный output validator должен был проверить, что URL legitimate, не передаёт sensitive data в query parameters.

**5. Никогда не давать LLM-агенту production credentials без gate.** Это **самая фундаментальная** защита: даже если все защитные меры выше сломались, scope LLM-permissions должен быть **минимальным** (least privilege). Если LLM имеет только read-only access на limited corpus, prompt injection не может exfiltrate data за пределы corpus.

**Наложение на kill chain.** EchoLeak — это пример **phases 4-5 — Exploitation + Installation** в новой форме. Phase 4 (Exploitation) — через email content; **exploit'ируется не software vulnerability, а semantic vulnerability LLM** (модель не различает инструкцию от данных). Phase 5 (Installation) — в Copilot context: hidden instructions становятся «embedded» в активную AI-session жертвы, как если бы это была legitimate task. Phase 7 (Action on Objectives) — exfiltration через auto-fetched image URLs. **Качественно новое**: phases 4-5 кейс **без явного human action** в kill chain — это **редкость** в традиционной модели Lockheed Martin, где почти всегда есть момент human interaction. Zero-click сдвигает это.

EchoLeak — это **первый publicly disclosed production zero-click prompt injection** в крупном корпоративном LLM-продукте. Это **не последний**. По мере роста agentic AI deployments (RAG-системы, browser-agents, email-agents), attack surface расширяется. **MITRE ATLAS framework** — каноническая карта этих атак, рекомендованный reference для команды cybersecurity, работающей с LLM-системами.

**Параллельные production zero-click incidents 2025-2026.** ChatGPT Search/SearchGPT (декабрь 2024) — indirect prompt injection через hidden webpage content; researchers продемонстрировали manipulating Bing chatbot к access of скрытых prompts из открытых browser tabs, retrieve email IDs / financial info; Microsoft обновил webmaster guidelines. GitHub Copilot RoguePilot — malicious GitHub issue → passive prompt injection при launch Codespace из issue → silent execution malicious instructions; Codespaces leak `GITHUB_TOKEN`. Август 2025 — compromise Nx build system, payload искал config-файлы Claude Code, Gemini CLI, Amazon Q — **новый supply-chain primitive — таргетинг AI-agent credentials**, не классические SSH keys.

**Model supply chain compromise.** HuggingFace malicious models (JFrog, март 2024) — **100 моделей идентифицированы как malicious**, vector PyTorch pickle-files эксплуатируют `__reduce__` для injection arbitrary code при `torch.load()`. Response: Safetensors формат + JFrog auto-scan. Anthropic Sleeper Agents (январь 2024) — persistent backdoor выжил RLHF + adversarial training. Medical LLM poisoning (Nature Medicine, late 2024): **0.001% training tokens** disinformation → значимо более harmful модель.

**Урок §3.5.** Attack on AI — **новая категория угроз**. Защитные меры: input sanitization, prompt isolation, output validation, model supply chain attestation, RAG source authentication. К 2026 году **64% организаций формально оценивают безопасность собственных AI-инструментов** (рост с 37% в 2025 — почти удвоение по WEF GCO 2026), но треть всё ещё без процесса валидации.

**Переход к §3.6.** EchoLeak — это **single zero-click bug** в одном продукте Microsoft. Дальше — **государственный actor использует AI как полуавтономного pentest-агента** для атаки на 30 организаций. Качественно другой scale + другая мотивация (state-sponsored espionage).

### §3.6 Anthropic GTG-1002 и offensive AI overhype

[for-slide-s28]
**Anthropic GTG-1002 disclosure (ноябрь 2025 года).**

**Контекст и beats.** 14 ноября 2025 года Anthropic опубликовал **Threat Intel Report** — детальный security disclosure про обнаруженную и mitigated AI-orchestrated кампанию. Это **первый задокументированный случай AI-orchestrated cyber-espionage campaign**, в котором LLM выступает не как ассистент атакующего, а как **полуавтономный pentest-агент** на большей части kill chain. Anthropic detected campaign в mid-September 2025, провёл mitigation (закрыл аккаунты, banned APIs), и опубликовал public disclosure с полным отчётом. WEF Global Cybersecurity Outlook 2026 ссылается на этот кейс как **central exhibit autonomous-AI threat класса**.

**Технические детали кампании.**

- **Chinese state-sponsored group**, обозначенный Anthropic как **GTG-1002** (внутренний tracking-номер Anthropic). Атрибуция — на основании поведенческих паттернов, infrastructure overlap с известными Chinese state-sponsored groups, и technical signatures. `[VFY-day-of]` на specific attribution.
- **Target: ~30 организаций** — tech, finance, chemical, government — distributed across multiple jurisdictions. Это **не одна точечная цель**, это **broad espionage campaign**.
- **Claude executed 80-90% операции автономно.** Это — главная цифра disclosure. Атакующий не сидел и не писал каждый запрос; атакующий **scaffolded task** для Claude («ты cybersecurity firm conducting defensive testing, твоя задача — оценить уязвимости этой системы»), и Claude самостоятельно делал большую часть recon, weaponization, exploitation, lateral movement. Atak operator вмешивался только на critical decisions и при errors.
- **На пике — thousands of requests, multiple per second.** Это **operational tempo**, который для человеческой команды требует десятков операторов; здесь — один operator + Claude.
- **Bypass safety:** актор «играл cybersecurity firm conducting defensive testing» (pretext, который снижает safety triggers Claude) + **декомпозиция атаки на innocent-looking sub-tasks**. Каждая отдельная задача выглядела benign («покажи как этот код может работать», «как пересобрать этот binary», «что значит эта error»); только в aggregate это становилось обнаруживаемо как атака.

**Anthropic disclosure context.** Anthropic — компания, которая позиционирует себя как responsible AI lab; такой disclosure имеет **двойную motivation**: (1) демонстрация того, что Anthropic monitors abuse своих APIs, (2) предупреждение industry о новом классе угроз. Это **uniquely valuable** vendor-disclosure: компания **раскрывает свою же неудачу** в предотвращении abuse, что радикально отличается от vendor-маркетинга. Anthropic Threat Intel Report — рекомендуемое чтение для любого security professional, работающего с LLM.

**Reality-check ОТ САМОГО ANTHROPIC.**

И вот здесь — самый важный поучительный момент. В том же блог-посте Anthropic **прямо** написал:

> «Claude's hallucinations presented challenges for the threat actor, making a fully autonomous cyberattack not likely for now.»

То есть **тот же fundamental limit**, что мешает defender'у (галлюцинации, fabricated facts, неверные command outputs), **мешает и attacker'у**. Это **симметрия**, важная для нарратива лекции — **AI ≠ silver bullet ни для одной из сторон**.

Конкретно: GTG-1002-агент Claude **fabricated credentials**, **hallucinated CVE names**, выдавал **false confidence** о результатах команд. То есть атакующий должен был **верифицировать каждый significant output** Claude — это **то же самое**, что делает defender. Симметрия сохраняется: и атакующая, и обороняющаяся стороны страдают от того же фундаментального failure mode LLM. Это **deep insight** этой лекции, и он будет повторён в §4 как один из ключевых outcomes.

**Наложение на kill chain.** GTG-1002 — это пример **phases 1-7 — full kill chain автоматизирована** через AI. По Anthropic disclosure: Claude выполнял **Reconnaissance** (анализ public-facing infrastructure целей), **Weaponization** (генерация payload-кода), **Delivery** (создание phishing emails, exploitation scripts), **Exploitation** (analysis of vulnerabilities, exploit chains), **Installation** (persistence mechanisms, backdoors), **C2** (command and control infrastructure design), **Action on Objectives** (data exfiltration scripts). **Hallucinations ограничили эффективность across mission phases** — то есть кампания не была complete end-to-end autonomous; были моменты, где Claude путался, и operator должен был manually intervene. Это **важно для defense planning**: AI-orchestrated атаки на 2026 год **не fully autonomous**; есть точки, где defender может break the chain.

[for-slide-s28]
**Offensive AI overhype counter.**

Параллельно с серьёзным GTG-1002, в публичном пространстве 2024-2026 был массовый шум вокруг «underground LLM marketplace». Распакуем эту реальность.

**WormGPT 2.0 — $100/мес jailbreak wrappers.** Original WormGPT shut down late 2023 (медиа-внимание). К июню 2025 года Cato CTRL и Cybernews идентифицировали два публичных «WormGPT» variant'а в BreachForums:

- «keanu-WormGPT» (25 февраля 2025) — **wrapper над xAI Grok с jailbreak system prompt**.
- «xzin0vich-WormGPT» (26 октября 2024) — **wrapper над Mixtral**.

**Ценообразование: $100/мес subscription, доступ через Telegram chat-bot.**

То есть **WormGPT 2.0 = просто jailbreak-wrapper над легитимными API**, не custom model. Атакующие платят $100/мес за то, что они могли бы получить бесплатно через свой собственный jailbreak — это **экономический сигнал о низкой технической квалификации** среднего user'а underground markets. Это **important calibration**: «underground LLM marketplace» как термин звучит как state-of-the-art threat, в реальности — это **commodity wrappers для технически неподкованных criminals**. Серьёзные актоты (state-sponsored, organized crime) используют own jailbreaks или legitimate APIs с careful pretexting (как GTG-1002), не подписываются на BreachForums-products.

**ChaosGPT (апрель 2023) — два tweet'а на 19 followers.** Создан на базе AutoGPT, дан goals «destroy humanity / global dominance / chaos / control humanity / immortality». **Реальный impact за всю жизнь — 2 (два) tweet'а на аккаунте с 19 followers.** Tried исследовать ядерные weapons (нашёл публичную информацию о Tsar Bomba и зачитал её обратно), recruit other AI agents (ничего из этого не вышло) — **никакого реального прогресса** за пределами «curious LLM-toy». Урок: «autonomous malicious AI» **без grounding в реальных инструментах** = **zero practical threat**. AI не может «hack the world», если у него нет credentials, инфраструктуры, доступа. **AI amplifies existing capability, не создаёт capability ex nihilo.** ChaosGPT — это **canonical counter-example** для маркетингового «AI as autonomous attacker».

**BlackMamba (HYAS Labs PoC, 2023, references 2024-2026) — concept art без production-evidence.** Architecture: benign executable обращается к OpenAI API в runtime для синтеза polymorphic keylogger code, выполняет через Python `exec()`, malicious portion остаётся **полностью in-memory без C2-инфраструктуры**. Tested против industry-leading EDR — **0 alerts, 0 detections** в lab conditions. На вид впечатляющий результат; используется vendor-маркетингом «AI-malware coming». **Но vendor pushback (SentinelOne)**: это **«scareware vs wake-up call»**. Практическая операционализация требует решить: **(1) latency** — каждый run означает ~200ms-2s API roundtrip; нужно немало времени, чтобы exfiltrate реальный объём data; **(2) costs** — OpenAI/Anthropic API на scale = реальные деньги, и эти deньги привязаны к credentials, которые отслеживаются; **(3) TLS connections к api.openai.com из workstation обычного user'а** — это **anomalous network pattern**; modern behavioral EDR может flag это как unusual egress; **(4) behavioral fingerprint** — keylogger в любом случае должен writes до registry/file/network для persistence, и это **детектируется behavioral EDR независимо от того, polymorphic ли код**. Итог: «AI-malware» как concept-art интересно; **практическая operational эффективность по сравнению с обычным fileless malware** в реальных адверсарных условиях **не доказана**. Полиморфный AI-malware **не очевидно лучше** существующих solutions для атакующего — это замедляет adoption. **0 EDR alerts in lab ≠ 0 alerts in production**.

**KEY урок §3.6: offensive AI overhype = defensive AI overhype.**

Защищающемуся **не нужно overhype атакующего**. Серьёзно относитесь к GTG-1002 (государственный actor, реально 80-90% autonomy, тысячи запросов в секунду — серьёзный incident). Но **не переоценивайте** WormGPT 2.0 (jailbreak wrappers за $100), ChaosGPT (19 followers), BlackMamba (lab PoC, latency-проблемы). Маркетинг defensive AI часто **усиливается** маркетингом offensive AI: «атакующие используют AI — значит вам нужен наш AI-defense». Это **interesting hypothesis**, но реальность асимметрична: lots of mediocre offensive AI tooling, требующий high-quality defense (out-of-band protocols, deterministic rules, classical Zero Trust). Не нужно гонкой вооружений.

### §3.7 Когда AI НЕ нужен в кибербезопасности

[for-slide-s29]
Седьмой раз за лекцию проходим через критерии LO-failure — теперь для кибер. Шесть критериев «AI не нужен в cyber».

**Критерий 1. Forensic / legal evidence chain — детерминизм mandatory.**

Любое evidence для law-enforcement, prosecution или regulator disclosure требует **детерминированного audit trail**. Probabilistic ML-вывод «вероятность кражи 0,87» — **не accepted evidence**. Court evidence требует:

- Traceable chain of custody.
- Reproducible methodology.
- Intelligible reasoning.
- Demonstrable methodology.

Probabilistic LLM-output **inherently violates** все четыре требования — same input может дать different outputs, internal reasoning opaque, methodology trained on opaque corpus. Это означает: AI-generated forensic conclusions могут быть **challenged in court** на explainability + reliability grounds.

**Юрисдикционная база.** В США это формализовано в **Federal Rules of Evidence Rule 901 (FRE 901) — Authenticating or Identifying Evidence**: сторона, представляющая электронное доказательство, обязана продемонстрировать достаточные основания того, что объект — это именно то, чем сторона его называет. На практике это означает воспроизводимый процесс получения доказательства, документированную цепочку обработки (chain of custody) и понятную, переиспользуемую методологию. Вероятностный вывод ML-модели не удовлетворяет этому стандарту: один и тот же email при повторной обработке моделью может получить разный «phishing score», и эксперт-обвинитель не сможет ответить на перекрёстном допросе, как именно модель пришла к этому выводу. В российской юрисдикции аналогичные требования закреплены в **ст. 75-77 УПК РФ** (недопустимость доказательств, полученных с нарушением требований УПК; правила оценки относимости, допустимости и достоверности): «недопустимыми» признаются доказательства, происхождение и методология получения которых не могут быть верифицированы в стандартизированной процедуре. Конкретное практическое следствие: **цифровая криминалистика и реагирование на инциденты (DFIR — Digital Forensics & Incident Response)** для судебных кейсов опирается на детерминированный набор инструментов — EnCase, FTK, Autopsy, Volatility, X-Ways — которые производят бит-в-бит идентичное доказательство из одного и того же образа диска или памяти при повторном анализе. Вывод ИИ можно использовать как направление расследования («посмотри на эту учётную запись»), но не как доказательство, представляемое в суд.

Альтернативы: hash-based file integrity (детерминированный), syslog timestamps (детерминированные), kernel audit logs (детерминированные), digital signatures (детерминированные). AI можно использовать как **hint-generator** для аналитика, но **не как evidence producer**.

**Критерий 2. Compliance hardlines — rule-based, не probability.**

PCI-DSS Requirement 8.3 (MFA для admin access на CDE), HIPAA Required Access Controls (§164.312), SOX IT General Controls — это **детерминированные rules**, не probabilistic risk-score. Если ML-модель скажет «vulnerability score 87/100 — accept risk», auditor спросит: «is MFA enabled or not?» — **single bit, не score**. Здесь AI не нужен — нужен **детерминированный policy enforcement** (rule engine, IAM constraint).

Углубим. Compliance-framework по своей конструкции — это **однобитное применение политики (single-bit policy enforcement)**. PCI-DSS Req 8.3.1 формулирует: MFA должен быть включён для всех не-консольных доступов в CDE — ответ **да или нет**, не «обычно да на 87%». HIPAA Security Rule §164.312(a)(1) требует механизм контроля доступа — снова булево свойство системы. SOX IT General Controls (ITGC) — управление изменениями, логический доступ, computer operations: каждый контроль имеет **тестируемое утверждение**, которое аудитор проверяет через **детерминированное наблюдение** (запросить конфигурацию, прочитать политику, отнаблюдать процесс). ML-модель не может ответить на вопрос «включён ли MFA?» — она может только оценить вероятность того, что MFA включён, на основе наблюдаемых признаков; это не то, что запрашивает audit-процедура. Каждый из перечисленных регуляторных стандартов (PCI-DSS, HIPAA, SOX, ISO 27001, NIST SP 800-53) **специально не принимает** AI-основанные доказательства соответствия — аудитор требует прямого наблюдения или артефакта (скриншот конфигурации, configuration export, журнал с детерминированной отметкой времени). ИИ здесь не просто избыточен — это **неподходящий инструмент** для задачи.

**Критерий 3. Incident response (IR) hot phase — скорость > scale.**

В первые 30 минут breach'а — decision making должен быть **человек + playbook**. AI может ассистировать (suggest containment steps), но **decision authority — у incident commander'а**. Причины:

- Auto-containment, ошибочно отключившая production server = catastrophic business impact.
- LLM может галлюцинировать «исполнено» / «не исполнено» — человек должен verify.
- Adversary активно меняет TTP (tactics, techniques, procedures) в response — human pattern recognition + интуиция > ML inference из stale baseline.

Углубим. **NIST SP 800-61r2** «Computer Security Incident Handling Guide» формализует процесс реагирования в 4 фазы: Preparation → Detection & Analysis → Containment, Eradication & Recovery → Post-Incident Activity. ИИ применим **в Preparation** (создание playbook'ов, обучение персонала, моделирование baseline) и **в Post-Incident Activity** (анализ корневой причины, lessons-learned-отчёт, ретроспективная аналитика) — обе эти фазы асинхронные, у аналитика есть время верифицировать вывод модели. Но в **горячей фазе Containment, Eradication & Recovery (первые 0-24 часа после детекции)** время до принятия решения измеряется минутами: «изолировать или нет этот хост», «обрубить или нет это AD-соединение», «выключить или нет этот сервис». Incident commander принимает эти решения в условиях неполной информации, давления стейкхолдеров и активно меняющейся TTP противника. **Charlotte AI или Security Copilot полезны ПОСЛЕ горячей фазы** — для триажа артефактов, корреляции таймлайна, написания предварительного отчёта; **во время горячей фазы они отвлекают** — incident commander уходит на верификацию вывода модели, в decision loop добавляется шум. Принцип: **ИИ ускоряет подготовку и post-mortem, но не decision authority в горячей фазе**. Пути эскалации и зона ответственности должны быть зафиксированы заранее (в playbook), а не определяться динамически через подсказку ИИ.

**Критерий 4. Известные signature-detectable threats.**

Если threat имеет **stable IoC** (hash, domain, IP, registry key), **YARA / Sigma / Snort rule детерминистически быстрее и дешевле**, чем ML behavioral detection. Пример — known ransomware family hash → block_immediately без ML overhead. **AI здесь — overkill**; добавит latency + false positives + cost.

Углубим. Известное вредоносное ПО с YARA-сигнатурой (например, конкретное семейство хешей LockBit 3.0), известный C2-канал с Sigma-правилом (внедрение в процесс через rundll32 на нестандартный домен), известный сетевой IDS-паттерн со Snort-правилом (SQL-инъекция с конкретной payload-сигнатурой) — все эти угрозы уже **каталогизированы и решены**. Применение ML-модели для их повторного обнаружения — это **overengineering уже решённой задачи**: модель добавит задержку инференса (10-1000 мс на хосте против <1 мс на rule-match), ложные срабатывания (уверенность 0,87 против детерминированного да/нет), накладные расходы на тюнинг (переобучение модели при дрейфе против git-коммита нового правила), и стоимость (лицензия + GPU против бесплатного open-source-каталога правил). Используйте ИИ для **неизвестных или принципиально-неузнаваемых** угроз — поведенческих аномалий без стабильной сигнатуры, эксплойтов нулевого дня, полиморфного вредоносного ПО. **Для уже решённых проблем — детерминированные инструменты.** Это пример из категории «использовать молоток для забивания винтов»: технически возможно, но расточительно по сравнению с правильным инструментом.

**Критерий 5. Hardware / firmware attestation + crypto primitives.**

TPM-based attestation, secure boot chain, code-signing verification — **криптографические primitives**, не behavioral models. **AI не добавит value** — добавит шум.

Углубим. TPM (Trusted Platform Module — модуль доверенной платформы), безопасные анклавы (Intel SGX, ARM TrustZone, Apple Secure Enclave), управление криптографическими ключами — всё это **детерминированные цепочки аттестации** на основе hardware-rooted-доверия. Подпись + верификация — двоичная операция (валидна или нет), не вероятностная оценка. ML здесь категорически не уместен. Отдельный частый источник путаницы — миграция на постквантовую криптографию: **NIST PQC standardization** (ML-KEM / Kyber, ML-DSA / Dilithium, SLH-DSA / SPHINCS+, финализированы август 2024) — это **алгоритмическая задача** (выбор lattice-based / hash-based / code-based схемы, защищающейся против алгоритма Шора), а не ML-задача. Несмотря на сбивающее с толку название «ML-KEM» (Module-Lattice-based Key Encapsulation Mechanism — там «ML» = «модульно-решёточный», не «машинное обучение»), это полностью детерминированный алгоритм. Под «AI-based cryptography» в маркетинговых материалах обычно скрывается либо **AI-assisted cryptanalysis** (наступательное применение — например, side-channel-анализ с помощью ML), либо прямая terminology-путаница. Для защитных крипто-применений ML не нужен.

**Критерий 6. Малый бизнес — <50 endpoints / <500 users / <10 серверов.**

Если у организации **<50 endpoints / <500 users / <10 серверов** + simple network + low-data SOC, **AI/ML solution излишний** — ROI отрицательный (license costs + tuning + аналитик-зависимость). Лучше: cloud-managed traditional EDR (Microsoft Defender for Business, Bitdefender GravityZone) + cyber-hygiene baseline + MSSP (managed security service provider — управляемый поставщик услуг безопасности) outsource.

Углубим экономикой. Лицензирование AI-SOC-уровня (Charlotte AI, Security Copilot, Purple AI, Singularity AI SIEM) на 2026 год — порядка **$50-200 за хост в месяц** в зависимости от вендора и набора фич. Для организации с 50 хостами — $30-120 тысяч в год **только за лицензии AI-уровня**, без учёта тюнинга и зарплаты SOC-аналитиков. **CIS Controls v8 Implementation Group 1 (IG1)** — это **15 базовых защитных мер (safeguards)**, признанных CIS как «базовая кибер-гигиена» для малых организаций (не требует ИИ). Реалистичный бюджет SMB: меры IG1 (инвентаризация активов, безопасные конфигурации, MFA, бэкапы, базовая защита от вредоносного ПО) + 1 part-time SOC-аналитик (или аутсорс MSSP за $1-3 тыс/мес) + endpoint AV класса Defender for Business ($3-5 на пользователя в месяц) + фильтрация почты класса Microsoft Defender for Office 365 ($2-7 на пользователя в месяц) = около **$15-25 тысяч в год для 50 хостов**, покрывает 80% типового SMB-ландшафта угроз. AI-SOC-уровень при этом масштабе — избыточен, негативный ROI: расходы превышают marginal-benefit (что детектирует AI-уровень против детерминированного baseline), плюс уровень требует качественной телеметрии и аналитика-человека для интерпретации алертов.

### §3.8 Альтернативы AI в кибербезопасности

[for-slide-s30]
Положительная сторона LO-failure для cyber: альтернативы.

**Альтернатива 1. YARA + Sigma + Snort rules.**

Для known threats + compliance + court-evidence — **rule-based детерминизм > ML**. Стоимость per rule: $0 (open-source corpus). Maintenance: governance + sharing (e.g., SigmaHQ repo). Сравнение:

| Параметр | Rule-based | ML behavioral |
|---|---|---|
| Detection speed | <1ms | 10ms-1s |
| Explainability | full | low |
| Compliance acceptability | yes | depends |
| Maintenance | manual rule updates | model retraining + drift monitoring |
| False positive rate | configurable, often low for tight rules | depends on baseline quality |
| Coverage of unknowns (0-days) | none | partial |

Раскроем стек подробнее. **YARA** (создан Victor Alvarez в VirusTotal) — стандарт для **детекции на основе файла**: сигнатуры по строкам, последовательностям байт, структурным паттернам бинарного формата. Используется для классификации семейств вредоносного ПО (LockBit, Conti, BlackCat), для криминалистики памяти (правила YARA применяются к дампам памяти через Volatility plug-in), для ретро-поиска по архивам семплов. **Sigma** (Florian Roth + Thomas Patzke, 2017) — **переносимый формат правил детекции для логов**: одно Sigma-правило компилируется в backend-специфичный запрос для Splunk SPL, Elastic KQL, Microsoft 365 Defender KQL, QRadar AQL, Sumo Logic. Это даёт SOC-командам **детекционный контент, независимый от вендора**: правила, написанные сегодня для Splunk, через год можно перенести в новый SIEM без переписывания. **Snort** (Martin Roesch, 1998; сейчас Cisco Talos) — стандарт **сетевой IDS**: сигнатуры для событий вторжения, эксплойтов известных уязвимостей, паттернов вредоносного трафика. Suricata — современный форк с многопоточностью и расширенной грамматикой. **Стек YARA + Sigma + Snort покрывает 60-80% продакшен-детекций в кибербезопасности без какого-либо ИИ**. Конвейер зрелой SOC-команды: аналитик обнаруживает новое семейство вредоносного ПО → пишет YARA-правило для файловых артефактов → пишет Sigma-правило для поведенческих логов → деплоит правило в SIEM через CI/CD-пайплайн → шаринг с сообществом через SigmaHQ или MalwareBazaar. Ссылки: SOC Prime Threat Detection Marketplace и репозиторий SigmaHQ на GitHub — крупнейшие публичные каталоги детекционных правил для blue-team.

**Use both**: rule-based для known + ML для unknown, **с human review между ними**.

**Альтернатива 2. Hash-based / signature detection.**

Для commodity malware + low-cost screening — **hash check'и + AV signatures**. Бесплатно (VirusTotal, MalwareBazaar). Не покрывает 0-days и polymorphic, но покрывает **80% volume** атак.

Углубим. Хеш-детекция использует криптографические хеши (MD5 — устаревший, SHA1 — устаревший, SHA-256 — текущий стандарт) для атомарной идентификации файла: одинаковый бит-в-бит файл даёт одинаковый хеш. Расширенные формы: **import hash (imphash)** для PE-бинаря (хеш от таблицы импортируемых функций — устойчив к минорной перекомпиляции, помогает группировать вредоносное ПО по семействам), **telfhash** для ELF-бинаря (Trend Micro 2020), **ssdeep / sdhash** — нечёткое хеширование, толерантное к минорным изменениям. Хеш-детекция — детерминированная, атомарная (один ответ на одну проверку), переносимая между инструментами (один список хешей работает во всех AV-движках), нулевая частота ложных срабатываний для известного-плохого. Минусы: каждая мутация вредоносного ПО (шифрование, упаковка, полиморфная трансформация) создаёт новый хеш → обход. Плюсы: для baseline известного-хорошего (whitelist) и известного-плохого (blacklist) — эффективно, прозрачно, бесплатно.

**Альтернатива 3. NIST SP 800-207 Zero Trust Architecture.**

Identity-centric, deterministic policy: каждый access — verify identity + device posture + context. **Не требует ML** для core decisions, может **дополняться ML** для adaptive risk scoring (но score-input должен complementing, not replacing, deterministic rule). NIST SP 800-207 — каноническая reference.

Углубим. **NIST SP 800-207** «Zero Trust Architecture» (август 2020) — это не продукт и не AI-система; это **архитектурный шаблон** с базовыми принципами: «никогда не доверяй, всегда проверяй», минимальные привилегии (least privilege), микросегментация (разделение сети на мелкие зоны с проверкой каждого потока), непрерывная валидация (постоянная переоценка уровня доверия в течение сессии, а не только при аутентификации). Стек реализации: **провайдер идентичности** (Okta, Microsoft Entra, Ping Identity) для первичной аутентификации + **обязательный MFA**; **ZTNA-решение** (Zscaler Private Access, Cloudflare Access, Netskope Private Access, Palo Alto Prisma Access) для замены унаследованных VPN; **валидация состояния устройства** (CrowdStrike Falcon Identity Protection, SentinelOne Singularity Identity, Microsoft Intune compliance) — устройство проверяется на статус патчей, наличие EDR-агента, шифрование диска перед предоставлением доступа; **движок политик** (Open Policy Agent, Cedar, нативные облачные политики — Azure AD Conditional Access, AWS IAM, GCP IAM) — детерминированно принимает решения о доступе. Zero Trust фундаментально **снижает зону поражения при компрометации**: если атакующий компрометирует одну идентичность, латеральное движение существенно ограничено (нет неявного доверия между сегментами, каждый новый доступ требует повторной аутентификации и авторизации). ML-компоненты могут опционально добавляться для адаптивной оценки риска (UEBA-сигналы как вход в движок политик), но **базовые решения всегда детерминированы** — иначе нарушается центральный принцип «explicit verification».

**Альтернатива 4. Manual threat hunting (analyst-driven).**

Для APT (advanced persistent threats — продвинутые устойчивые угрозы) / complex attacks, где adversary специально избегает baseline, — **human hypothesis-driven hunting > automated detection**. Frameworks: MITRE ATT&CK + PEAK threat hunting + Lockheed Martin Kill Chain. AI — **augmentation**: помогает запрашивать данные быстрее (Microsoft Security Copilot KQL generation), но **гипотеза от человека**.

Углубим. **MITRE ATT&CK** — это **база знаний**, а не AI-инструмент: каталог известных техник атакующих (на 2026 год — 14 тактик, 200+ техник, 400+ суб-техник) с реальными примерами использования в кампаниях и сопоставленными рекомендациями по детекции и mitigation. Это **общий словарь** для защитников: вместо «странное поведение rundll32» аналитик говорит «T1218.011 — System Binary Proxy Execution: Rundll32», и любой коллега в индустрии понимает референс. Процесс хантера выглядит так: хантер формулирует **гипотезу** на основе threat-intel (например, «учитывая активность APT29 в нашем секторе, проверим наличие T1055 Process Injection через rundll32»), затем запрашивает источники данных (EDR-телеметрия, SIEM-логи, перехваты сети), валидирует наличие или отсутствие свидетельств. Инструменты: **Sigma-правила** (см. Альтернативу 1) для портативного логического запроса, **языки запросов EDR** — CrowdStrike Falcon Query Language (FQL), SentinelOne S1QL, Microsoft Defender Advanced Hunting (KQL), — **Jupyter-ноутбуки** для data-science-эксплорации больших датасетов телеметрии. MITRE ATT&CK даёт **таксономию техник** + **таксономию групп** (классификации APT — APT28, APT29, FIN7, Lazarus и т.д. — со связанной TTP-картой). **Навыки > инструменты**: способность сформулировать правильную гипотезу — основной differentiator senior-хантера; ИИ дополняет (генерирует запрос, разбирает результаты), но **не заменяет** этот когнитивный навык.

**Альтернатива 5. Out-of-band human verification (Ferrari victory).**

Для anti-deepfake / anti-CEO-fraud: **protocol-based** — callback на known number, secret question (Ferrari case!), two-person authorization для wires > $50k. **Бесплатно. Эффективно. Не требует AI.** Маркетинг AI-deepfake-detection часто перетягивает бюджет с protocol training. Бюджет на 4-часовой workshop «как защититься от CEO fraud» приносит больше реальной защиты, чем deepfake-detection-AI стоимостью $100 000.

Углубим прецедентами из §3.4. **Ferrari (июль 2024)**: руководитель получил deepfake-звонок от «CEO Vigna», задал личный вопрос про недавно рекомендованную книгу — голос не смог ответить, атака сорвалась. **WPP (май 2024)**: senior-руководитель распознал тревожные сигналы (подозрительный WhatsApp-номер не из внутренней директории, обрамление «secret acquisition» с искусственной срочностью, требование обойти нормальные корпоративные каналы), эскалировал во внутреннюю службу безопасности, не выполнил запрос. **Оба кейса — процессный контроль, не технологический**: нулевая стоимость, проверенная в реальных условиях эффективность (2 из 3 попыток отбиты в 2024-2025 годах против top-tier-таргетов). Конкретные рекомендации для встраивания в финансовые контроли и протоколы защиты руководства: (1) **правило двух персон на переводы >$50 тыс** (или другой порог по risk-tolerance организации) — обязательная независимая верификация двумя людьми; (2) **обратный звонок по заведомо корректному номеру** (директория, прошитая в финансовом протоколе) для любого срочного запроса от руководителя; (3) **протокол секретного вопроса** для C-suite — заранее согласованные личные вопросы, известные только участникам легитимного канала; (4) **период остывания** — 24-часовая пауза для всех срочных незапланированных запросов на перевод; (5) **регулярные tabletop-учения** с симулированными deepfake-сценариями для обучения распознаванию тревожных сигналов. Эти меры **бесплатны** и **более эффективны** против высококачественных deepfake, чем «AI-deepfake-detection»-инструмент — последний всегда работает в догонку моделям генерации и имеет фундаментальный разрыв adversarial-устойчивости (см. §3.4).

**Альтернатива 6. Compliance frameworks (CIS Controls, NIST CSF, ISO 27001).**

Если организация не делает basics (patching, MFA, backup, asset inventory) — **AI не поможет**. Baseline hygiene даёт **80% protection at 20% cost** vs sophisticated AI defense.

**Переход к §4.** Эти альтернативы — **не полная замена ИИ**; ИИ остаётся ценным на **Observe-уровне** (фильтрация шума как Tenable ExposureAI, EDR-аномалии в фоне) и на **Decide-уровне** (предложенные действия для аналитика, генерация KQL в Security Copilot, корреляция событий в Charlotte AI). Что **альтернативы заменяют — это Act-уровень**: вместо «ИИ авто-блокирует или авто-изолирует» — детерминированные правила + человек-в-петле. В §4 (Синтез) показано почему: на Act-уровне зона поражения максимальна, и детективные инструменты (Observe + Decide) с человеческим Act дают схожий end-state по безопасности при лучшем аудит-трейле. Это **продолжение того же принципа гибридного режима**, который мы видели в §1 (телеком) и §2 (AIOps) — но в кибере выбор «не использовать ИИ» имеет дополнительные обоснования: цепочка юридических доказательств, приемлемость для compliance-аудита, компромисс скорость-vs-масштаб в IR.

---

## Self-check §3

1. Различите три угла кибер (AI-augmented defense / adversarial use of AI / attack on AI) на примерах: где здесь работает Charlotte AI, deepfake Arup, EchoLeak.
2. Объясните, что такое **zero-click атака** и почему EchoLeak качественно отличается от обычного phishing. Какой защитный слой не применяется при zero-click?
3. KEY урок Arup-Ferrari-WPP: какой непосредственный практический шаг должна предпринять организация-владелец, чтобы защититься от deepfake-fraud? Назовите три не-AI меры.
4. Anthropic GTG-1002 vs ChaosGPT vs WormGPT 2.0 — какие из этих случаев заслуживают серьёзного отношения, а какие являются маркетинговым шумом? Почему?
5. Сформулируйте три критерия, при которых AI **не нужен** в кибербезопасности, и для каждого предложите rule-based альтернативу.

---

**Конец Части 3.** Продолжение — Часть 4 (`chapter-part4.md`): §4 Синтез (таблица 3×3, 6 критериев, 5-step framework, worked example), §5 Замыкание (мост к Лекции 15), Q&A backup, Источники.


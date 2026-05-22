---
lecture: 14
part: 4
title: "Лекция 14, Часть 4: Синтез, закрытие, Q&A, источники"
status: finalized
version: v3.1
length_words: ~8200
parent: chapter.md
updated_at: "2026-05-22"
author: "book-editor v3.1 (Phase 11 consistency: §4.3 март→апрель 2026)"
---

# Глава 14, Часть 4. Синтез, замыкание, Q&A backup, источники

## Навигация

- **Часть 1:** §0 Hook + keystone, §1 Телеком — `chapter.md`
- **Часть 2:** §2 AIOps — `chapter-part2.md`
- **Часть 3:** §3 Кибербезопасность — `chapter-part3.md`
- **Часть 4 (этот файл):** §4 Синтез, §5 Замыкание, Q&A backup, Источники

## Оглавление (Часть 4)

- [§4. Синтез: лестница автономии × 3 поддомена](#4-синтез-лестница-автономии--3-поддомена)
  - [§4.1 Сводная таблица 3×3](#41-сводная-таблица-33)
  - [§4.2 Ключевой инсайт: каскады на «Действует»](#42-ключевой-инсайт-каскады-на-действует)
  - [§4.3 Шесть критериев «AI не нужен» + Bayes refresh](#43-шесть-критериев-ai-не-нужен--bayes-refresh)
  - [§4.4 Пятишаговый каркас](#44-пятишаговый-каркас)
  - [§4.5 Worked example: SOAR auto-block для phishing](#45-worked-example-soar-auto-block-для-phishing)
  - [§4.6 Карьерный угол](#46-карьерный-угол)
- [§5. Замыкание: мост к Лекции 15](#5-замыкание-мост-к-лекции-15)
  - [§5.1 Recap лестницы автономии и трёх вопросов](#51-recap-лестницы-автономии-и-трёх-вопросов)
  - [§5.2 Мост к Лекции 15: Production-AI vs Discovery-AI](#52-мост-к-лекции-15-production-ai-vs-discovery-ai)
  - [§5.3 Central message](#53-central-message)
- [Q&A backup](#qa-backup)
- [Источники](#источники)

---

## §4. Синтез: лестница автономии × 3 поддомена

### §4.1 Сводная таблица 3×3

[for-slide-s31]
Перейдём к синтезу. Мы прошли три поддомена (телеком, AIOps, кибер) по нашей лестнице автономии (Видит, Решает, Действует). Зафиксируем сводную **таблицу вердиктов 3×3**. Это, возможно, самый плотный слайд всей лекции — рекомендуется read aloud медленно.

| | Телеком | AIOps | Кибербезопасность |
|---|---|---|---|
| **Видит** (низкий масштаб поражения) | **YES, ML.** rApps на RIC (Nokia AVA, Rakuten); детекция фрода (Subex); голосовая биометрия **с liveness MFA**. Альтернатива: classical 3GPP SON + Erlang. | **YES, ML.** Dynatrace Davis, Datadog Bits, Cisco ThousandEyes, Splunk Mission Control. Альтернатива: Nagios + SPC. | **YES, ML.** CrowdStrike Falcon EDR, SentinelOne, Darktrace NDR, Abnormal email, Tenable ExposureAI (фильтр, не детекция). Альтернатива: YARA + Sigma + hash signatures. |
| **Решает** (средний масштаб поражения) | **HYBRID.** Клиентский LLM **с человеком-в-петле** (TOBi, AURA) на рутину; человек — на сложных/эмоциональных/правовых (Air Canada precedent). Альтернатива: Klarna-style гибрид AI+люди. | **HYBRID.** LLM-runbooks (NeuBird, Claude SRE, incident.io) **с человеком-в-петле обязательно**. Anthropic own-postmortem апрель 2026 = vendor-disclosed limit. Альтернатива: Rundeck/Ansible runbook-as-code + LLM как «smart query layer». | **HYBRID.** Charlotte AI / Security Copilot triage **с человеком-в-петле**. Производственный деплой выявил галлюцинации — never auto-execute. Альтернатива: SIEM-rules + manual threat hunting (MITRE ATT&CK). |
| **Действует** (пиковая зона ущерба) | **NO / NEVER на critical path.** Billing engine, E911 routing, lawful interception, URLLC — детерминированные правила. xApps auto-tuning — только в специфических scoped scenarios с канарейкой и откатом. | **NO по умолчанию.** Cascade-failure история 2024-2026: CrowdStrike, Cloudflare, AWS, Azure, Replit, Cursor+PocketOS (свежий — апрель 2026). Альтернатива: SLO burn rate alerts + chaos engineering + manual approval. Auto-remediation OK только в Netflix-style scoped/repeatable scenarios. | **NO кроме narrow scope.** SOAR auto-block, EDR isolate — только с явным go/no-go gate, узким масштабом поражения, мгновенным откатом. Альтернатива: Zero Trust + manual IR + out-of-band verification. |

Каждая ячейка — короткий вердикт + альтернатива. Студент, который вышел с лекции с этой таблицей в кармане, может за 10 секунд классифицировать любое предложение поставщика: «куда вы хотите поставить AI на этой матрице?». Если ответ «верхний правый» (Действует на критическом пути) — спрашивайте три LO2-вопроса агрессивно, и зачастую правильный ответ — «нет».

### §4.2 Ключевой инсайт: каскады на «Действует»

[for-slide-s32]
Один эмпирический факт, который объединяет всю лекцию:

**Все major cascade-failures 2024-2025 годов произошли на уровне «Действует».**

Список (без повторений):

- **CrowdStrike Falcon, 19 июля 2024** — Channel File автоматически развёрнут глобально, 8,5M устройств BSOD, $5B+ ущерб.
- **Cloudflare, 18 ноября 2025** — config change automatically propagated, DNS-каскад, **5ч 38мин полное восстановление (~3ч 10мин core traffic mostly restored)**.
- **AWS DynamoDB, 20 октября 2025** — race condition между DNS Planner и DNS Enactor (детерминированная автоматизация, **не** AI-assisted), 15+ часов recovery. **Отдельный AI-инцидент: Amazon Kiro, ~декабрь 2025** — 13h disruption attributed to AI-assisted code changes per FT report; первое publicly acknowledged AI-cascade в large-scale cloud infrastructure.
- **Microsoft Azure Front Door, 29 октября 2025** — config change через broken protection mechanism, canary не сработал (signals through same broken layer), 7 часов восстановления.
- **Replit AI agent + SaaStr, июль 2025** — agent удалил production database, 1 206 executive records плюс 1 196 company records.
- **Cursor + Claude Opus 4.6 + PocketOS, апрель 2026** — agent удалил Railway volume + backups за 9 секунд. **Свежий случай, буквально месяц назад до этой лекции.**

**Не на уровне «Видит». Не на уровне «Решает». Все на уровне «Действует».**

[for-slide-s32]
Это **не теоретический вывод**, это **эмпирическое наблюдение**. Закономерность, которая повторяется снова и снова в 2024-2025 годах:

1. Автоматическая система детектирует условие или применяет изменение.
2. Автоматическая система применяет remediation **глобально / в масштабе**.
3. Remediation — неверный из-за (a) corrupted data, (b) race condition, (c) model drift, (d) hallucination, (e) configuration bug.
4. К тому моменту, как люди заметили — ущерб irreversible / требует длинного recovery.

**AIOps делает это хуже**, чем deterministic automation, потому что:

- ML decisions harder to predict → harder to test all scenarios.
- LLM agent reasoning не fully introspectable.
- «AI knows better» культура убирает скепсис.
- Auto-remediation скорости («95% faster MTTR») предполагает meaning faster damage.

**Защитный паттерн**: circuit breakers, ограничения масштаба поражения, обязательное human approval для деструктивных действий, постепенный rollout (канарейка), kill-switches. **AIOps-маркетинг систематически недооценивает эти ограничения.**

Это — **главный keystone-payoff лекции**. Студент уходит с убеждением: **на уровне «Действует» по умолчанию не нужен AI**. Точнее: на уровне «Действует» нужны **rule-based** + canary + rollback + manual approval. AI может ассистировать на «Видит» и «Решает», но **сам не должен дёргать рычаги в production без человека**.

### §4.3 Шесть критериев «AI не нужен» + Bayes refresh

[for-slide-s33]
Сводим шесть критериев «AI не нужен», которые мы выводили в каждом из трёх поддоменов. Это **slide-of-the-day** — обязательно read aloud, желательно записать. Эти шесть критериев — операционализация LO-failure: они **применимы немедленно**.

**Критерий 1. Forensic / legal audit trail.**

Если результат должен быть **доказан в суде или перед регулятором**, AI не нужен. Probabilistic вывод нарушает требования chain of custody, reproducibility, intelligible reasoning. Используйте: hash, syslog, kernel audit logs, digital signatures.

**Критерий 2. Compliance hardline.**

Если правило сводится к «MFA включён или нет», «доступ авторизован или нет», «транзакция в sanction list или нет» — это **single bit**, не probability. AI добавит галлюцинаций, не точности. Используйте: rule engine, policy enforcement points, IAM constraints. Примеры: PCI-DSS, SOX, HIPAA, FDA Part 11.

**Критерий 3. Deterministic latency.**

URLLC (1 ms), kernel hot path, lawful interception, E911 routing, real-time control systems. ML делает **probabilistic decisions** с непредсказуемой tail latency. Любая 0,3% задержка может стоить регуляторного штрафа или жизни. Используйте: static priority queues, PID/MPC, classical SS7/SIP.

**Критерий 4. Rare-event detection + Bayes math.**

Это **refresh из §2.8**. Bayes-математика: при низкой base rate (1% и ниже) даже **99,9% accuracy детектор** даёт precision TP **значительно ниже 99,9%** — false positives доминируют. Аналитик утопает в FP **не из-за плохой модели**, а из-за **base-rate fallacy**. Mitigation — **risk-based prioritization, не accuracy improvement**. Tenable ExposureAI «только 3% CVE produce impactful exposure» — это **filter, not detect**. Это правильное применение AI: фильтрация шума, не детекция новых угроз.

Cross-reference: §2.8 (Bayes math fundamentals), §2.2 (alert fatigue stats — 78% NOC burnout, 73% FP challenge #1, 71% ignore <3% alerts), §3.3 (Tenable 3% CVE matter, defender FP economics).

**Критерий 5. Hardware / crypto primitives.**

AES, RSA, ECDSA, Kyber, Dilithium — formal security proofs. TPM-based attestation, secure boot chain, code-signing verification — детерминированная криптография. AI не может «оптимизировать» это — добавит шум. Используйте: классические криптобиблиотеки (Bouncy Castle, OpenSSL, BoringSSL) + hardware HSM.

**Критерий 6. Малый scope.**

Если **<50 endpoints / <500 users / <10 серверов**, AI/ML решение **излишний**. ROI отрицательный (license costs + tuning + аналитик-зависимость). Лучше: cloud-managed классические решения (Microsoft Defender for Business, Bitdefender GravityZone, Nagios + Zabbix) + cyber-hygiene baseline + MSSP outsource.

Эти шесть критериев — **минимум**, не максимум. К ним добавляются доменные критерии (URLLC в телекоме, IR hot phase в кибере, synthetic monitoring для критически важных бизнес-транзакций в AIOps). Но шесть — это **универсальный фильтр**: если выпадает хотя бы один — AI здесь не на критическом пути.

### §4.4 Пятишаговый каркас

[for-slide-s34]
Шесть критериев — это **матрица**. Чтобы превратить её в **процедуру**, добавим пятишаговый поток: что инженер делает с любым предложением поставщика AI-системы в инфре, по порядку. Назовём это **«5-step framework для решения о включении AI в Act»**:

**Шаг 1. Identify уровень на лестнице.**

Vendor demo показывает что-то. Уточните: это Видит, Решает или Действует? Где именно граница между «AI рекомендует» и «AI выполняет»? Vendor может скрыть Act как Observe — задайте LO2 question #3 (change-control + canary + rollback).

**Шаг 2. Оцените масштаб поражения.**

Если эта система ошибётся однажды — кого/что это затронет? Один пользователь? Один кластер? Глобальный rollout? Один регион? Билинговый цикл одного месяца? Все endpoint'ы в production? **Сравните масштаб поражения с вашей готовностью к этому ущербу.**

**Шаг 3. Apply 6 criteria.**

Пройдите по шести критериям §4.3. Есть хотя бы один блок?

- Forensic audit trail нужен? — Если да, AI должен быть **assist-only**, не authoritative.
- Compliance hardline? — Не используйте AI для финального решения.
- Детерминированная задержка? — AI на критическом пути запрещён.
- Rare-event detection? — Применима Bayes-math; AI должен **фильтровать шум**, не **детектировать всё подряд**.
- Crypto primitives? — Никогда не подменяйте классику ML.
- Малый scope? — ROI отрицательный.

Если хотя бы один критерий блокирует — переходите к альтернативе или к assist-only mode.

**Шаг 4. Pilot with canary + explicit go/no-go.**

Если первые три шага прошли — **не запускайте на 100% сразу**. Pilot на 1% (отдельная подсеть, узкий отдел, ограниченный кластер). Установите **явные метрики успеха**: какой precision FP/FN нужен, какая latency приемлема, какой rollback срок. Установите **явные критерии остановки**: если что-то идёт ниже порога — stop pilot, return to baseline.

**Шаг 5. Production с HITL + audit trail + rollback.**

Если pilot успешен — **production с человеком-в-петле на действиях, deterministic audit trail на каждом решении, готовый rollback в любой момент**. Это не «полная автономия» — это **AI ассистирует, человек принимает финальное решение** на уровне «Решает»; **AI рекомендует, deterministic rule выполняет** на уровне «Действует»; **audit log всё пишет**; **rollback срабатывает не дольше 5 минут**.

Пятишаговый каркас — не теоретический. Это операционализация трёх вопросов вендору (§1.5) плюс шести критериев (§4.3) плюс лестницы автономии (§0.3). Покажем его в действии в §4.5.

### §4.5 Worked example: SOAR auto-block для phishing

[for-slide-s35]
Проработаем конкретный кейс, на котором применим пятишаговый каркас. Vendor X предлагает SOAR-инструмент с auto-block функционалом для phishing-писем. **Что мы должны спросить и проверить, прежде чем включать auto?**

**Контекст.** Vendor X — крупный SOAR-провайдер (Cortex / Tines / Torq). Их предложение: интеграция с email security, классификация подозрительных писем через ML, **автоматическая блокировка отправителя на уровне MX-records при confidence > 0.95**. Маркетинг говорит: «mean time to neutralize phishing — 12 секунд против 23 минут вручную».

Применим 5-step framework.

**Шаг 1. Identify уровень.** Это **Действует**. AI **сам блокирует** отправителя, не уведомляет аналитика. Vendor подтверждает: «mean-time-to-neutralize 12 секунд» — это **автономный** time-to-block, без человека.

**Шаг 2. Оцените масштаб поражения.** Если auto-block ложно срабатывает на легитимного отправителя:

- Один блокированный отправитель = одна потерянная коммуникация (recruiter, клиент, партнёр).
- При FP rate 0,1% и 100 000 emails/day — **100 ложных блоков в день**.
- Бизнес-импакт от одного ложного блока: пропущенный контракт (если recruiter), пропущенный платёж (если клиент), напряжённые отношения с партнёром.

Blast radius — узкий, но **повторяющийся**. 100 ложных блоков в день на протяжении недели — это **700 раздражённых внешних контактов**.

**Шаг 3. Apply 6 criteria.**

- ❌ Forensic / legal audit trail — auto-block остаётся ли trace для investigation? **Нужен audit log** на каждый блок. Если vendor не предоставляет — fail. (Допустим, vendor предоставляет SIEM-интеграцию — OK.)
- ✓ Compliance hardline — HIPAA / SOX напрямую не применяются к email-блокировке. OK.
- ✓ Детерминированная latency — для email критический latency не имеет значения. OK.
- ⚠️ **Bayes math** — какой FP rate × email volume? **0,1% × 100 000 emails/day = 100 ложных блоков в день**. Cost: 100 ложных блоков × $50/блок (средний impact на business) = **$5 000/day = $1,8M/year**. Это **выше**, чем стоимость human reviewer ($60-80k/year).
- ✓ Hardware/crypto — не применимо. OK.
- ✓ Малый scope — компания крупная, scope соответствует. OK.

**Bayes math блокирует.** При cost of FP × volume FP > cost of human reviewer — **HITL дешевле и устойчивее**.

**Шаг 4. Pilot.** Если бы мы решили pilot — какие критерии успеха? FP rate < 0,01% (10× ниже), сохранённая precision, no escalations за две недели. И **явные критерии остановки**: если FP > 0,05%, любое complaint от стороннего контакта.

**Шаг 5. Production.** Здесь — verdict. **HITL required — auto-flag, not auto-block.** SOAR может **подсвечивать** подозрительные письма (auto-flag, забросить в «карантинную» очередь). Человек-аналитик **просматривает carantine** в течение нескольких часов. **Финальное решение о блокировке — человек.**

**Vendor pushback (типичное).** «Но 23 минуты! Атакующий за 23 минуты украдёт credentials!» Контр-аргумент: средняя phishing-кампания **не атакует за 23 минуты** — она атакует на протяжении дней/недель, отправляя письма в большое количество inbox'ов. **Несколько часов человеческого review** — приемлемый trade-off против **100 ложных блоков в день** с бизнес-impact $1,8M/year. Если же кампания **target high-value** (CEO, CFO, finance), то это уже **другой класс защиты** — out-of-band protocols, two-person rule (см. §3.4 Arup/Ferrari) — которые SOAR auto-block в принципе не решает.

**Vendor counter-pushback (продвинутый).** «А что, если confidence > 0.99?» Здесь нужно вспомнить Bayes: при rare-event detection precision TP остаётся ниже expected даже при высоком nominal confidence. Confidence > 0.99 = improvement, но не панацея. Лучший mitigation: **auto-flag + human review с быстрым SLA на разбор** (15 минут — это уже defense, не «12 секунд auto-block»).

**Итоговый verdict.** SOAR — **HYBRID**, не **YES**. Auto-flag — да; auto-block — нет.

**Несколько вариаций worked example.**

Чтобы убедиться, что каркас не зависит от case-by-case деталей, проработаем коротко ещё две вариации.

**Вариация 1. EDR auto-isolate подозрительного endpoint.**

Vendor предлагает EDR (CrowdStrike Falcon, SentinelOne) с auto-isolate при detection score > 0.9. Применим 5-step:

- Шаг 1. Identify уровень: **Действует** (auto-isolate без человека).
- Шаг 2. Оцените масштаб поражения: один endpoint — production-сервер? Workstation инженера? Контроллер OT-системы? Это разный масштаб. Один production-сервер = миллионы долларов в час; один workstation = неудобство одного инженера на 30 минут.
- Шаг 3. 6 criteria: Forensic chain — изоляция оставляет ли trace? Compliance — какие requirements о continuity? Bayes math — какой FP rate? При 1% FP rate на 10 000 endpoints в день = 100 ложных изоляций.
- Шаг 4. Pilot: на каком сегменте? Только on workstations, не servers? Только в одном dept?
- Шаг 5. Production: HITL для servers; auto-isolate для workstations с быстрым auto-unisolate, если ложный.

**Вариация 2. AIOps auto-restart pod при memory leak detection.**

Vendor: AIOps platform с auto-restart при «memory leak detection score > 0.95». Применим:

- Шаг 1. Identify уровень: **Действует** (auto-restart без человека).
- Шаг 2. Оцените масштаб поражения: один pod — какой сервис? Stateless replica vs stateful master? Restart восстановим без data loss?
- Шаг 3. 6 criteria: Forensic chain — есть ли trace causes? Compliance — какие SLA? Rare-event Bayes — false positive rate?
- Шаг 4. Pilot: стартует на одном сервисе с low criticality.
- Шаг 5. Production: явные rate-limits (не более 3 restarts на сервис в час), audit log, immediate rollback при detection cascade.

В **обеих** вариациях правильный verdict — **HYBRID с blast-radius caps**, не «full auto». Это **повторяющийся паттерн**: на уровне Act правильный ответ редко «yes», обычно «hybrid с явными границами и safety mechanisms».

Этот worked example — **прямое приложение** LO-failure. Студент, который его проработал, может перенести логику на любой vendor-pitch. Это не «теория критериев», это «как применить критерии».

### §4.6 Карьерный угол

[for-slide-s36]
Где работают инженеры, для которых полезна эта лекция? Три траектории — NetEng (сетевой инженер), SRE (site reliability engineer), SOC analyst (security operations center analyst) — со структурой по **уровню готовности**, не по треку. Это важнее: на 3 курсе вы entry-level в любом из треков; через несколько лет — mid-level; через 5+ лет — senior.

**Entry-level (3 курс — 1 год опыта).** Базовые инструменты per трек, плюс foundation knowledge:

- **NetEng entry:** 3GPP TS / IETF RFCs / BGP / DNS basics; Cisco CCNA certification как baseline. Hands-on: лабораторные на eve-ng / GNS3, чтение packet captures в Wireshark. Цель: понимать как пакет идёт от телефона к серверу.
- **SRE entry:** Google SRE Book / observability basics (Prometheus + Grafana); Kubernetes basics (kubectl, deployments, services); Python / Bash. Цель: уметь развернуть простой сервис в production-like среде и наблюдать его metrics.
- **SOC entry:** MITRE ATT&CK as foundation; classical SIEM (Splunk, ELK basics); сертификация CompTIA Security+ или SANS GIAC GSEC. Цель: понимать классические attack patterns и читать SIEM-alerts.

Самопроверка: «меня привлекает low-level networking + carrier scale» (NetEng); «меня привлекает automation + observability + reliability» (SRE); «меня привлекает adversarial thinking + investigation» (SOC).

**Mid-level (2-5 лет опыта).** Specialization paths внутри каждого трека:

- **NetEng mid:** Open RAN specifics (RIC / rApps / xApps); ML basics для anomaly detection в RAN; Cisco CCNP. Может рассматривать AI-RAN / O-RAN SC development или telecom carrier roles в Tier-1 operators.
- **SRE mid:** Production observability с deep instrumentation; SLO / error budgets / burn rate methodology; chaos engineering (Netflix Chaos Monkey, Gremlin); cloud certifications (AWS / GCP / Azure). Должен уметь решать вопрос «что делать с этим AIOps-инструментом» с практическим контекстом.
- **SOC mid:** Threat hunting (MITRE ATT&CK Navigator, hypothesis-driven hunting); SANS GIAC GCIH / GMON; experience с EDR / SIEM tuning. Может работать как SOC L2 или Detection Engineer.

**Senior (5+ лет).** Architecture / strategic roles, где LO2 framework и шесть критериев применяются на decision-making уровне, не на execution:

- **NetEng senior:** Network architecture, vendor strategy (включая Hidden Act check), regulatory navigation (EU AI Act, lawful interception); может работать как Principal Network Architect или Telecom CTO advisory.
- **SRE senior:** Platform architecture, AIOps strategy (политика канареечного деплоя, ограничения масштаба поражения, дисциплина автоматизации); может работать как Principal SRE, Platform Architect, или Reliability Engineering Director.
- **SOC senior:** Security architecture, threat intel program design, AI security strategy (включая attack-on-AI как новая категория); CISSP certification; может работать как Security Architect, CISO advisory, или Threat Intel Lead.

Все три трека на любом уровне применяют общие принципы лекции: лестница автономии, LO2-вопросы вендору, шесть критериев «AI не нужен». Различие — в **доменных стеках**: NetEng глубоко знает radio + transport + routing; SRE глубоко знает observability + automation + chaos engineering; SOC analyst глубоко знает adversary tactics + forensics + threat intelligence.

Где учиться: **профильные технические университеты** (включая магистерские программы по AI / cybersecurity / network engineering); **специализированные программы** (SANS GIAC для cyber, Cisco / Juniper / Ericsson certifications для networking, Google SRE / AWS / GCP certifications для SRE); **открытое сообщество** (GitHub, MITRE ATT&CK Navigator, SigmaHQ, Awesome AI SRE, OWASP). Senior-уровень требует **публичных контрибуций** (post-mortems на собственный блог, доклады на отраслевых конференциях, open-source contributions) — это inherent part of career growth на уровне Architect / Principal.

Один общий совет: **в любой из трёх траекторий на любом уровне**, на собеседовании прозвучит вопрос «как вы относитесь к AI?». Худший ответ — «AI решает всё». Лучший ответ — структурный: «AI отлично работает на уровне Видит для observability и фильтрации шума. На уровне Решает требуется человек-в-петле. На уровне Действует — по умолчанию rule-based, AI ассистирует. Главные cascade-failures 2024-2026 — все на Act, включая свежий Cursor+PocketOS апрель 2026. Я применяю шесть критериев перед каждым включением». Это **уровень суждения**, который ищут работодатели в 2026 году.

---

## §5. Замыкание: мост к Лекции 15

### §5.1 Recap лестницы автономии и трёх вопросов

[for-slide-s37]
Зафиксируем три mental tools, которые студент уносит с лекции.

**Лестница автономии AI: Видит → Решает → Действует.** Рабочий термин этой лекции, упрощённое представление каноник Parasuraman, Sheridan & Wickens (2000) и SAE J3016. Главное: **чем выше уровень, тем сильнее масштаб поражения при ошибке**. Все major cascade-failures 2024-2026 (включая свежий Cursor+PocketOS апрель 2026) — на уровне Act. Это эмпирический закон.

**Три уточняющих вопроса вендору.** Применимы к любому AI-предложению:

1. Какой был baseline до AI?
2. Какое окно измерения и какая методология (production или demo, какие вмешательства засчитаны)?
3. Какая процедура change-control, канареечного деплоя и rollback при cascade?

**Шесть критериев «AI не нужен».** Forensic / compliance / deterministic latency / rare-event Bayes / crypto / малый scope. Применимы как фильтр перед запуском любого AI-проекта.

**Failure-callback.** Через год на стажировке начальник предложит включить auto-remediate / auto-tuning / auto-block / auto-routing. **Спросите**: на каком уровне лестницы? Какой масштаб поражения? Какой откат? Какие шесть критериев применимы? Какое окно измерения базовой точки отсчёта? Это **не противостояние** — это **дисциплина инженерного процесса**. Хорошие AIOps-команды любят эти вопросы; плохие — раздражаются.

### §5.2 Мост к Лекции 15: Production-AI vs Discovery-AI

[for-slide-s38]
Эта лекция — **последняя в Модуле 3** (AI в индустрии). В Модуле 4 курса мы переключаемся на **AI в науке и R&D** — Лекция 15 будет про AlphaFold, материаловедение, ускоренное моделирование. Это качественно другой режим работы AI, и важно **не путать failure modes**.

Сводная таблица:

| | Production-AI (Лекция 14) | Discovery-AI (Лекция 15) |
|---|---|---|
| **Цель** | Уменьшить масштаб поражения при ошибке, поддерживать инфраструктуру | Расширить пространство гипотез, ускорить научный поиск |
| **Determinism** | Critical (audit + rollback mandatory) | Optional (exploration OK) |
| **Hallucination** | Failure mode (outage / breach) | Sometimes a **feature** (новая гипотеза для проверки) |
| **Speed of validation** | Минуты-часы (production breaks) | Месяцы-годы (lab experiments) |
| **Stakes of single error** | Миллиарды долларов, тысячи рейсов | Один зря потраченный эксперимент |
| **Examples** | CrowdStrike, Cloudflare, EchoLeak, Klarna reversal | AlphaFold протеины, материаловедение, drug discovery |

**Key insight: не путайте failure modes.** AI в науке «wrong answer» → новая гипотеза для проверки в лаборатории — это **продуктивный сбой**. AI в инфре «wrong answer» → outage / breach — это **деструктивный сбой**. Разные критерии успеха, разные архитектуры, разные mental model.

[for-slide-s38]
Конкретный пример различия. **AlphaFold предсказывает структуру белка** — иногда правильно, иногда нет. Когда AlphaFold ошибается, биолог проверяет в лаборатории кристаллографически — несколько недель эксперимента, цена ошибки — несколько недель отложенного исследования. Когда **CrowdStrike Falcon делает плохое предсказание** на уровне ядра — 8,5M устройств уходят в BSOD за часы. Один и тот же тип ошибки (несоответствие предсказания реальности), радикально разный масштаб поражения. Это **фундаментальное** различие двух режимов AI.

Прямое следствие — **другой набор критериев** для discovery-AI:

- Детерминированность оптимальна (не critical) — научное исследование выдерживает probabilistic answers.
- Hallucination в контролируемой среде — может стать гипотезой; в production — outage.
- Vendor-кальибрования метрики (LO2-вопросы) применимы и здесь, но критерии измерения другие (precision vs recall в predictive science часто менее критичны, чем novelty и reproducibility результата).

Лекция 15 разберёт эти критерии подробно. Сейчас достаточно: **не переносите production-mindset в науку и наоборот**. Это два разных режима с двумя разными mental model.

### §5.3 Central message

[for-slide-s39]
Закроем лекцию одним предложением, который мы будем считать формой ответа всей дисциплины:

**Лучшая защита — инженер, который знает, где AI помогает, а где остановить его.**

Это **не анти-AI заявление**. AI на уровне «Видит» работает превосходно, фильтрует шум, обнаруживает аномалии, делает аналитика производительнее. AI на уровне «Решает» работает с человеком-в-петле — собственное признание поставщика (Anthropic Claude Code postmortem, Microsoft Copilot признание галлюцинаций) показывает, какой реальный класс ошибок есть, и production-инженер строит дисциплину проверки. AI на уровне «Действует» — **по умолчанию rule-based + канарейка + откат**; AI может ассистировать, но **сам не должен дёргать рычаги** в production.

Этому **нельзя научиться по демо-материалам поставщика**. Демо показывает, что AI работает в **идеальных условиях** на **их выборке**. Реальная инфраструктура — это плохая выборка, неидеальные условия, сложные адверсари, неожиданные каскады. Дисциплина — это **набор привычек проверки**, которые мы прошли в этой лекции:

- Применяй три LO2-вопроса к каждой маркетинговой метрике.
- Применяй шесть критериев перед запуском AI на критическом пути.
- Включай pilot с канарейкой и явным go/no-go gate.
- Никогда не делай auto-execute на AI-выводе без human verification на уровне Act.
- Помни Bayes-математику: rare events ≠ accuracy improvements.
- Помни Klarna, Air Canada, CrowdStrike, Cloudflare, EchoLeak, Arup, Replit, Cursor+PocketOS. Это **не страшилки**, это **прецеденты**, которые учат структурным урокам.

Это всё инженерные привычки. Их легко записать, легко вспомнить, легко применить. Но они — **то, что отделит** инженера, который успешно встроит AI в production, от того, кто запустит следующий CrowdStrike-инцидент.

Удачи. До встречи на Лекции 15.

---

## Q&A backup

В этом разделе собраны типичные вопросы, которые могут возникнуть у студента после прочтения главы, с подробными ответами. Эта часть не входит в основной нарратив, но служит дополнительным ресурсом для самостоятельной работы и подготовки к семинарам.

### Q1. «А если автономия уровня Действует прошла A/B-тестирование? Можно тогда?»

A/B-тестирование — **не то же самое**, что canary deployment. Это путаница, которая часто звучит в маркетинговых materials, и стоит её распутать.

**A/B-тестирование** — это сравнение двух вариантов на **разных группах пользователей** одновременно, для оценки **business metrics** (conversion rate, engagement, revenue). A/B-тест статистически валиден, когда выборка достаточна и метрики чисты. A/B-тест **не предназначен** для обнаружения catastrophic failure: он предполагает, что обе варианта **функциональны**, и измеряет **разницу в их успешности**.

**Canary deployment** — это **постепенный rollout** одного нового варианта на возрастающие проценты пользователей (1% → 10% → 50% → 100%) с **explicit fail-criteria и rollback**. Canary предназначен **именно** для обнаружения catastrophic failure до глобального rollout. Метрики, на которые смотрит canary, — это **proxy для системных проблем** (latency p99, error rate, kernel crashes, memory usage), не business metrics.

CrowdStrike Channel File 19.07.2024 **не проходил canary** — он развёртывался автоматически на 100% клиентов одновременно. Если бы CrowdStrike делал canary на 1% машин с 30-минутным observation window, было бы зарегистрировано резкое падение availability на 1% выборки, и rollout остановился бы. Cost: 1% от 8,5M = 85 000 BSOD устройств — серьёзно, но **на два порядка меньше** реального ущерба.

Поэтому: A/B-тест **не заменяет** canary. Canary **обязателен** на уровне Act. Если вендор говорит «у нас A/B-тестирование, значит, безопасно» — это **подмена понятий**, повод задавать LO2-вопрос три более настойчиво.

### Q2. «Microsoft Copilot маркетинг показывает -30% MTTR. Почему этому не верить?»

Краткий ответ: верить **частично**, с пониманием контекста.

**Что Microsoft измерил.** В Spring 2025 paper Microsoft опубликовала результаты **PSM-исследования (propensity score matching — наблюдательное сопоставление через статистический подбор «двойников» в контрольной группе)** на live operations. Это **квази-эксперимент**, **не настоящий RCT**: пользователи **выбирали сами**, использовать Copilot или нет; статистический матчинг приближал группы по наблюдаемым characteristics, но не гарантировал balance по unobservables. Сравнение: MTTR в группе аналитиков, использующих Security Copilot, vs «matched» аналитики, не использующих Copilot, за 3-месячный период. Результат — **30,13% reduction**. (Microsoft публиковал **отдельно** настоящий RCT на arXiv:2411.01067 — это другое исследование на IT Admin tasks.)

**Что это означает на практике.** Microsoft показал: в условиях наблюдательного PSM-исследования, **в среднем** Copilot ускоряет triage на 30% **в matched cohort**. Это **directionally credible** improvement, но **слабее**, чем RCT-result был бы. Если ваша SOC-команда работает в **точно таких же условиях** (тот же тип telemetry, тот же уровень подготовки аналитиков, тот же тип инцидентов), вы можете ожидать **directional** improvement; но **специфический процент 30% — не гарантия**, потому что PSM не controls для unobservable confounders.

**Что это НЕ означает.**

- Не означает, что **в вашей среде** будет 30%. У вас может быть 50%, 10%, 0%, или даже negative (Copilot замедлит из-за избытка ложных рекомендаций). Эта величина зависит от вашего baseline, состава команды, типа инцидентов.
- Не означает, что **через 6 месяцев** будет 30%. Модель обновится, ваша команда привыкнет к её ошибкам, тип угроз изменится — все эти факторы меняют MTTR.
- Не означает, что **общая security posture** улучшилась на 30%. MTTR — это **одна из метрик**, не вся картина. Если ваш false-positive rate вырос на 20%, общая нагрузка на команду могла даже вырасти.

**Что говорит сам Microsoft.** В том же документе Microsoft признаёт: «Copilot occasionally produces hallucinations — responses that sound confident but may be factually incorrect». То есть **сам вендор предупреждает**, что 30% MTTR — это **в условиях, где аналитик верифицирует каждый significant output**.

Поэтому: используйте 30% MTTR как **ориентир**, не как **гарантию**. Применяйте LO2-вопросы для понимания, переносится ли это на вашу среду. И помните: **PSM ≠ RCT**; ваш baseline должен совпадать с control group methodology — в условиях наблюдательного исследования effect size может быть переоценён из-за selection bias.

### Q3. «Что делать, когда поставщик отказывается отвечать на три LO2-вопроса?»

Это случается чаще, чем кажется. Sales engineer поставщика либо не знает ответа, либо знает, что ответ непривлекательный, либо предохраняет маркетинговый нарратив. Что делать:

**Эскалация технической линии.** Sales engineer не может ответить — попросите доступ к **техническому архитектору** или к **product manager**. У них больше опыта, и они обычно более честны, потому что их карьера зависит от долгосрочной репутации продукта.

**Структурный запрос.** Сформулируйте письменно: «Перед принятием решения о purchase, мы запрашиваем (1) baseline MTTR/MTTD/throughput **в production** перед adoption (с methodology), (2) full description of measurement window и intervention controls, (3) detailed change-control procedure включая canary deployment policy и rollback SLA». Письменный запрос увеличивает шансы на полный ответ и создаёт **artifact**, на который вы можете ссылаться.

**Альтернативные источники.** Если поставщик не предоставляет, обратитесь к customer references (особенно honest ones — у каждого продукта есть критические клиенты). Контактируйте через LinkedIn инженеров в компаниях, которые используют продукт. Обычно люди готовы поделиться **реальным** опытом.

**«No contract» политика.** В крайнем случае — **не подписывайте**. Это **не агрессивная позиция** — это **профессиональная защита бизнеса**. Контракт на $500k/год на AIOps-tool без понимания, как он раскатывается на production — это финансовая безответственность вашей роли. Если вендор не может ответить — он **не готов к production deployment**, что бы ни говорил marketing.

**Counter-pressure.** Vendor sometimes pushes back: «у нас 200 enterprise customers — почему ваши вопросы такие странные?». Стандартный ответ: «вы правы, что у нас другая среда. Именно поэтому мы хотим убедиться, что **специально в нашей среде** ваш продукт работает не как сюрприз. Ваши 200 customer'ов прошли тот же due-diligence, что мы делаем сейчас». Это reframe — не «мы недоверчивы», а «мы делаем due diligence, как любой профессиональный покупатель».

### Q4. «Bayes-математика для rare events — это не теория? В реальности тоже?»

Это часто приходящий вопрос, и ответ — категорическое «да, в реальности тоже». Пройдёмся по нескольким конкретным цифрам, которые мы видели в лекции.

**Tenable 3% CVE matter.** Это не теоретическое утверждение Tenable — это **measured реальность** в их exposure-data за несколько лет. Из 100 уязвимостей, маркированных «critical» по CVSS, в типовом enterprise-окружении только 3 действительно эксплуатируются в production или представляют real impact из-за компенсирующих контролей. Это **filter ratio**, не accuracy.

**Microsoft Defender / EDR detections.** В типовой SOC аналитик получает **тысячи events в день**. Из них **минимальный процент** — actual security incidents. 70-80% — duplicates, false positives, low-priority info. 73% organizations называют false positives главной проблемой. Это **прямая** Bayes-математика: даже при низкой FP rate, при высоком volume false positives доминируют.

**Phishing detection.** Если detector ловит 99% true phishing, но 1% legitimate emails flagged as suspicious — это означает, что в типичной 10 000/day среде вы получаете **100 ложно-подозрительных писем в день**, и каждое требует разбора. Это нагрузка, **которая может превышать** ценность поимки настоящего phishing.

**Vulnerability scanners.** Раннее VPR (Vulnerability Priority Rating) показывал, что из ~200 000 уязвимостей в типовом enterprise сразу патчить нужно ~3 000. Tenable enhancement 2025 года улучшил 2× efficiency — то есть теперь это ~1 500 из 200 000. **Всё ещё 99%** уязвимостей не требуют немедленного действия — это **measured реальность** Bayes-математики в практике.

Поэтому: Bayes-математика — это не теория. Это **structural property** rare-event detection в high-volume среде. Любая AI-system, которая работает в этой среде, **столкнётся** с этой математикой, и её **дизайн должен учитывать** это: **alert filter, не alert detect**.

### Q5. «Если deepfake +1300%, как организация защитится?»

Этот вопрос — реальная боль для финансовых директоров, governance-комитетов, HR-руководителей. Хорошая новость: **защита не требует AI**. Плохая новость: **она требует процессов и обучения**.

**Три уровня защиты.**

**Уровень 1. Out-of-band protocols.** Любая wire transfer выше $50k или любая необычная команда от executive (особенно urgency-framed) проходит **обязательное обратное подтверждение** через известный канал, не контролируемый атакующим. WPP CEO case — executive распознал red flags (suspicious WhatsApp number, «secret acquisition» framing) и flagged внутренней службе безопасности. Ferrari case — личный вопрос про книгу, на который deepfake-голос не смог ответить. Эти меры **бесплатны**, **работают**, **сорвали** обе real-world попытки.

**Уровень 2. Two-person rule.** Любая транзакция выше определённого порога (компания определяет — обычно $50k-$100k) требует **независимого одобрения двух людей**, у каждого свои credentials, ни один в отдельности не может выполнить. Это классический внутренний контроль, существующий десятилетиями для борьбы с insider fraud. Применяется идеально и к deepfake-fraud: даже если deepfake убедит финансиста, он не убедит **второго** человека, проверяющего через другой channel.

**Уровень 3. Training + protocol drills.** Регулярные **drills** (тренировки): симулированные deepfake-атаки на сотрудников, с feedback и обучением. Это **знакомит** сотрудников с реальностью угрозы, **снижает** automation bias («звонок выглядит реалистично — значит, real»), **встраивает** out-of-band-протоколы в muscle memory.

Бюджет на эти три меры — примерно стоимость одного младшего безопасника. Альтернатива — AI-deepfake-detection-vendor за $100k-$500k/год, который ловит часть deepfake (с adversarial robustness gap ~10pp false negative), но **не отменяет** необходимость protocols (потому что 10pp false negatives — это всё ещё реальные пропущенные атаки). Поэтому **сначала protocols, потом AI как complement**, не наоборот.

### Q6. «AI-augmented defense vs Attack on AI — должна ли организация выбрать одно?»

Нет, **обе**. Это **разные** угрозы, требующие **разных** защит.

**AI-augmented defense** — это **ваш собственный AI-стек**: Security Copilot, Charlotte AI, Darktrace, ваши custom ML-detector'ы. Защита от этих систем — это управление их quality, мониторинг галлюцинаций, HITL на действиях, audit trail. Это **operational discipline** вокруг AI-инструментов defense.

**Attack on AI** — это **атаки на ваш AI-стек**, превращающие его в attack surface. EchoLeak против Copilot — это атака **на Copilot напрямую**, не на ваши endpoints / network / users в классическом смысле. Атакующий не нуждается в credentials или phishing — он **манипулирует AI**, который у вас в production.

Защита от attack on AI — это **другая дисциплина**: input sanitization для LLM-агентов, prompt isolation, RAG source authentication, output validation, **никогда не давать LLM-агенту production-credentials без gate**, never auto-execute LLM output. Это MITRE ATLAS framework — каноническая карта.

Поэтому: ваша security strategy 2026 года должна **одновременно**:

1. **Использовать** AI-augmented defense (Charlotte AI, Security Copilot) — но **с дисциплиной HITL и валидации**.
2. **Защищать** ваш AI-стек как attack surface — input sanitization, RAG source verification, scope limits для agents.
3. **Готовиться** к adversarial use of AI извне — out-of-band protocols, training, social engineering awareness.

Это **триада**, не выбор «или-или». Каждая компонента закрывает свой класс угроз.

### Q7. «Лекция 15 будет про AlphaFold — там тоже масштаб поражения?»

Хороший вопрос — он именно про мост к Лекции 15. Краткий ответ: **масштаб поражения у Discovery-AI существует, но он качественно другой**.

В Production-AI (Лекция 14): масштаб поражения — это объём инфраструктуры, пользователей, данных, которые **немедленно** ломаются при ошибке. CrowdStrike: 8,5M устройств за часы. Cloudflare: глобальный internet-traffic за минуты. AWS DynamoDB: тысячи бизнесов за полчаса. **Восстановление — часы-дни**, ущерб **миллиарды долларов**.

В Discovery-AI (Лекция 15): масштаб поражения — это **затраченное время на проверку неверной гипотезы**. AlphaFold предсказывает структуру белка — иногда правильно, иногда нет. Биолог потратит **несколько недель** на кристаллографическую проверку — **зря потраченные ресурсы лаборатории**. Это **тоже** ущерб, но качественно другой:

- Recovery — недели, не часы.
- Ущерб — научное время, не finance / business / safety.
- Параллельных исследований обычно несколько — одна неверная гипотеза не останавливает программу.
- Никто не теряет связь, не пропускает 911-вызовов, не отменяет 7000 рейсов.

Поэтому **критерии запуска AI** в науке другие. Детерминированная аудитная цепочка нужна меньше (научное сообщество в любом случае проверяет результаты независимыми экспериментами). Hallucinations могут быть **продуктивны** (новая гипотеза для проверки). Скорость auto-execute не имеет того значения — наука работает на тайм-скейле недель/месяцев, не миллисекунд.

Но **некоторые** уроки переносятся. **LO2-вопросы** (baseline, methodology, validation) применимы в науке так же. AlphaFold метрика accuracy на CASP-bench — это **canonical benchmark**, но переносится ли это на **специфический белок** в вашей лаборатории? Это **тот же вопрос**, что мы задаём в кибере. **Bayes-математика** rare events тоже работает в науке: AlphaFold более accurate на distributions, похожих на training data; менее accurate на out-of-distribution proteins. Понимание этого — fundamental, не optional.

Лекция 15 раскроет эти параллели подробно. Сейчас достаточно: **AI в науке — мощный инструмент, но требует своих критериев применимости**. Перенесите inquisitive mindset из Лекции 14, но **адаптируйте** критерии под discovery-режим.

### Q8. «Drift / сдвиг распределения — почему это центральная проблема ML-моделей в продакшне?»

Это **фундаментальная** концепция, которая часто недооценивается в маркетинговых материалах. Объясним подробно.

Когда ML-модель обучается, она настраивается на **distribution** входных данных — статистическое распределение признаков. В сетевой инфраструктуре это распределение определяется множеством факторов: типы пользователей (residential vs business vs roaming), типы устройств (phones vs IoT vs M2M), сезонность (праздники vs будни), события (стадион, конференция, новости), сети-партнёры, geographically-distributed загрузки.

В production это распределение **постоянно меняется**. Появляются новые типы устройств (IoT-датчики устанавливают по 1000 в день), новые приложения (TikTok-like video apps создают новый класс traffic), новые угрозы (новый класс DDoS, новый тип spam), новый поведенческий паттерн (covid pandemic, work-from-home мобильность). Модель, обученная **в прошлом квартале**, видит **другое распределение** в текущем квартале.

Документированная статистика drift'а:

- **91% ML-моделей** в production демонстрируют существенный drift в течение полугода без активного дообучения.
- **75% businesses** в 2024 году наблюдали падение AI performance со временем без proper monitoring.
- **Модели без обновления 6+ месяцев** показывают **35% jump в error rate на new data**.
- **67% организаций**, использующих AI at scale, столкнулись минимум с одним critical issue из-за statistical misalignment, который не был замечен более месяца.

В AIOps-контексте это означает: anomaly detection начинает (а) **пропускать** новые real anomalies, потому что они «не в training distribution», (b) **flag** normal-but-new behavior как anomalous. Без active retraining схема **деградирует invisibly**.

Что делать:

- **Continuous monitoring distribution.** На каждый production input логировать статистики (среднее, стандартное отклонение, гистограммы) и сравнивать с training distribution. Метрики типа KL divergence или Population Stability Index — стандартные.
- **Streaming drift detection.** Алгоритмы типа ADWIN (Adaptive Windowing) или Page-Hinkley test обнаруживают drift в режиме реального времени.
- **Scheduled retraining.** Регулярное переобучение модели на свежих данных — раз в неделю / месяц / квартал в зависимости от чувствительности.
- **Champion-challenger A/B.** Параллельно с production-моделью запускается «challenger» на свежих данных. Если challenger consistently outperforms — заменить production.
- **Explicit fallback.** При drift-alarm — fallback на rule-based / classical baseline до окончания retraining.

Без этого пакета **AI traffic forecasting через 6 месяцев может быть хуже простого weekly-seasonal baseline**. И это — **не теоретический** риск, это **документированная** реальность в большинстве AIOps-deployments, где MLOps-команда не была организована.

### Q9. «Шесть критериев — это для cyber. А для телекома и AIOps те же шесть?»

Хороший вопрос — короткий ответ: **пять из шести универсальны, один доменно-специфичен**.

**Универсальны:**

- **Критерий 1. Forensic / legal audit trail.** Применим везде: телеком (биллинговые споры, регуляторные запросы), AIOps (compliance audit), cyber (forensic для prosecution).
- **Критерий 2. Compliance hardline.** Везде. PCI-DSS / SOX / HIPAA в финансовой инфре. CALEA / СОРМ в телекоме. FDA Part 11 в фарме. EU AI Act high-risk в любой critical инфре.
- **Критерий 4. Rare-event detection + Bayes math.** Везде. Telecom fraud, AIOps anomaly, cyber threat — все три — rare-event detection в high-volume environment.
- **Критерий 5. Hardware / crypto primitives.** Везде. Аутентификация в телекоме (AKA, EAP-AKA'), authentication в cyber (passkey, TPM), data integrity в AIOps (hash-checks).
- **Критерий 6. Малый scope.** Везде. AI-tools имеют overhead. <50 endpoints / <500 users / <10 серверов — ROI отрицательный.

**Доменно-специфичен:**

- **Критерий 3. Deterministic latency.** Конкретно для телекома и AIOps. В телекоме — URLLC, E911, lawful interception, kernel path RAN. В AIOps — kernel hot path, time-sensitive transactions, real-time control loops. В cyber — IR hot phase (но это уже другая природа: не latency, а **decision authority** в кризисе).

То есть **универсальный фильтр — пять критериев**, и **один доменный** (deterministic latency vs decision authority в hot phase) — расщепляется на два аспекта в зависимости от поддомена.

Можно ещё добавить **седьмой** критерий, который применим везде, но менее явный: **операционная зрелость команды**. Если у вас нет MLOps capabilities (data pipeline, model retraining, drift detection, monitoring, A/B testing), AI-инструмент станет stale за 6 месяцев и сломается. Это **не «AI плохой»**, это «**вы не готовы поддерживать** AI». В этом случае лучший выбор — **отказ от AI** до того, как команда подготовится.

### Q10. «Что произойдёт, если я просто проигнорирую LO2-вопросы и куплю AI-инструмент по маркетинговым обещаниям?»

Часто задаваемый вопрос, особенно от инженеров, которые работают в компаниях, где procurement-решения принимаются не на инженерном уровне. Честный ответ — три сценария.

**Сценарий 1. AI-инструмент в Observe-режиме — низкий риск.**

Если инструмент работает только на Observe (например, anomaly detection в Datadog), даже без LO2-вопросов риск умеренный. Худшее, что произойдёт: вы будете получать много false positives, аналитики раздражатся, инструмент потеряет credibility, постепенно его перестанут использовать. Это **дорого** ($200k-$500k/year wasted license), но **не catastrophic**. В первый год это будет «изучаем продукт, не работает идеально, постепенно настраиваем».

**Сценарий 2. AI-инструмент в Decide-режиме — средний риск.**

Если инструмент рекомендует решения, которые аналитики выполняют (например, AI-runbook рекомендует remediation step), без LO2-вопросов риск растёт. Аналитики могут начать выполнять hallucinated recommendations и **создавать дополнительные incidents** (выключить не тот сервис, заблокировать не того пользователя, перезапустить не тот pod). Stable production-команда обнаружит эти ошибки и постепенно научится фильтровать AI-вывод — но **6-12 месяцев операционных проблем** реальны. Cost — несколько средних incidents с восстановлением (~$500k-$2M), плюс потерянная команда (если кто-то уволится из-за фрустрации).

**Сценарий 3. AI-инструмент в Act-режиме — высокий риск.**

Если инструмент имеет production-credentials и **сам выполняет действия** (auto-remediation, auto-block, auto-isolate), без LO2-вопросов риск **значительный**. Это **класс** инцидентов CrowdStrike, Cloudflare, AWS, Replit — описанных в §2.5-§2.7. Cost: cascade-failure, многие часы-сутки восстановления, ущерб **миллионы-миллиарды долларов** в зависимости от scale. И это **не теоретический риск**, это **наблюдаемая закономерность** последних 18 месяцев.

LO2-вопросы — это **insurance policy**. Они стоят несколько встреч в начале процедуры закупки. Они **предотвращают** Сценарий 2 и Сценарий 3 практически бесплатно. Это самая выгодная инженерная гигиена, доступная вам.

Если вы инженер и обнаружили, что procurement-решение принимается без due diligence — поднимите вопрос **письменно**: «Перед тем как мы развернём это в production, я хотел бы видеть ответы на следующие вопросы: (1) baseline, (2) measurement window, (3) change-control + rollback». Если ответ — «не задавай вопросов» — это **архитектурный** flag для вашей карьеры: компания не готова к ответственному использованию AI, и **вы рискуете** репутацией, если что-то пойдёт не так. Лучший момент сменить работу — **до** того, как ваша команда подпишется под катастрофой, не после.

### Q11. «Какие учебники / курсы / сертификации развивают эти навыки?»

Краткие рекомендации по основам, сгруппированные по треку:

- **Networking / телеком:** Tanenbaum & Wetherall «Computer Networks» 5e (Pearson, 2010); 3GPP TS 23.501 + TS 33.501; O-RAN ALLIANCE specifications (`https://www.o-ran.org/specifications`); Cisco CCNA → CCNP → CCIE.
- **SRE / observability / AIOps:** Google SRE Book + Workbook (`https://sre.google/books/`); Majors et al. «Observability Engineering» (O'Reilly, 2022); Google Cloud SRE certification, Datadog / Dynatrace Trainings.
- **Cybersecurity:** Anderson «Security Engineering» 3e (Wiley, 2020 — бесплатно `https://www.cl.cam.ac.uk/~rja14/book.html`); Stamp «Information Security» 3e (Wiley, 2021); SANS GIAC (GSEC, GCIH, GMON); CompTIA Security+ → ISC2 CISSP.
- **AI / ML:** Russell & Norvig «AIMA» 4e (Pearson, 2021); Goodfellow et al. «Deep Learning» (MIT Press, 2016 — бесплатно `https://www.deeplearningbook.org/`); Burkov «Hundred-Page ML Book» (2019).
- **MLOps:** Huyen «Designing ML Systems» (O'Reilly, 2022); Treveil et al. «Introducing MLOps» (O'Reilly, 2020).

Главный совет: **читайте инцидент-постмортемы**. Cloudflare blog, AWS post-incident reports, Anthropic engineering blog, CrowdStrike PIR, GitLab incident database. Это **самый ценный источник** реального инженерного знания. По одному постмортему в неделю — за год вы будете лучше большинства практикующих инженеров.

---

## Источники

### Канонические references (упомянуты в visible body)

- **NIST AI Risk Management Framework (RMF) 1.0** (2023) + **NIST AI 600-1 «Generative AI Profile»** (июль 2024). Базовый framework для управления рисками AI-систем; foundation для LO3.
- **NIST CSF (Cybersecurity Framework) 2.0** (февраль 2024). Cybersecurity governance framework.
- **MITRE ATT&CK** + **MITRE ATLAS** (Adversarial Threat Landscape for AI Systems, 2021-). Канонические карты атак на classic infrastructure и на ML-системы.
- **EU AI Act** (Regulation (EU) 2024/1689, поэтапное вступление 2024-2026). High-risk AI в critical infrastructure; запреты + аудит обязателен.
- **ISO/IEC 42001:2023** «Information technology — Artificial intelligence — Management system» + **ISO/IEC 27001:2022** «Information security management». Основа аудита AI-систем.
- **3GPP TS 33.501** «Security architecture and procedures for 5G System». Baseline для AI-RAN security analysis.

### Speaker notes / chapter references (не на slides)

- **NIST SP 800-207** «Zero Trust Architecture» (2020).
- **NIST SP 800-61r2** «Computer Security Incident Handling Guide» (актуальная редакция). Фундаментальный референс 4-фазной модели реагирования на инциденты; используется в §3.7 при обосновании, почему ИИ неприменим в горячей фазе.
- **CIS Critical Security Controls v8** (Center for Internet Security, 2021; обновления 2024-2026). Используется в §3.7 для baseline-бюджета SMB-защиты (Implementation Group 1 = 15 базовых мер).
- **Federal Rules of Evidence Rule 901** «Authenticating or Identifying Evidence» (US Federal Rules of Evidence, актуальная редакция). Стандарт аутентификации электронных доказательств в США; используется в §3.7 для обоснования детерминизма forensic evidence chain.
- **УПК РФ, ст. 75-77** «Недопустимые доказательства; правила оценки относимости, допустимости и достоверности». Российский аналог требований к воспроизводимой методологии получения доказательств; используется в §3.7.
- **CALEA** (Communications Assistance for Law Enforcement Act, US) / Постановление Правительства РФ № 538 (СОРМ).
- **3GPP TS 33.535** + **GSMA NESAS / SCAS**.
- **CISA Joint Cybersecurity Guidance on Deploying AI Systems Securely** (апрель 2024).
- **Verizon DBIR 2025/2026** + **WEF Global Cybersecurity Outlook 2026** + **CrowdStrike Global Threat Report 2026**.
- **Bainbridge L.** «Ironies of Automation» (Automatica, 1983).
- **Anderson R.** «Security Engineering» 3rd ed. (Wiley, 2020).
- **Parasuraman R., Sheridan T.B., Wickens C.D.** «A Model for Types and Levels of Human Interaction with Automation» (IEEE Transactions on Systems, Man, and Cybernetics, Part A, vol. 30, no. 3, pp. 286-297, 2000). DOI: 10.1109/3468.844354.
- **SAE J3016** «Taxonomy and Definitions for Terms Related to On-Road Motor Vehicle Automated Driving Systems».
- **Endsley M.R.** «Toward a Theory of Situation Awareness in Dynamic Systems» (Human Factors, 1995).
- **Boyd J.R.** OODA loop (исторические лекции, рассмотренные в работах R. Coram, 2002; F. Osinga, 2007).

### Кейсы и пресс-релизы — телеком

AI-RAN / Open RAN: NVIDIA Developer Blog «AI-RAN Goes Live»; SoftBank Press 2025-10-29 «Software-only Massive MIMO on GPU»; Samsung Newsroom 2025-12 «Samsung + KT validate AI-RAN»; Rakuten Mobile/Symphony Press 2025-05-28; Nokia AVA Customer Story (KDDI); Ericsson + MasOrange 2025-03; Nokia + Orange Deep Sleep 2024-02; Google Cloud Blog «AI-powered transformation MWC 2025». Customer LLM: Vodafone SuperTOBi; Telefónica AURA Handbook; Microsoft Customer Story Telefónica. Failures / lawsuits: Klarna reversal (Fortune, FinTech Weekly, Entrepreneur); Moffatt v. Air Canada (McCarthy Tétrault TechLex, ABA Business Law Today); FCC AT&T Outage Post-mortem (Network World, The Register); CRTC Rogers Outage Report 2024 (DevOps.com). Fraud / security: CFCA Global Fraud Loss Survey 2025; Pindrop 2025 Voice Intelligence; Subex Risk Assurance. Market: MIT State of AI 2025 (Legal.io); NTT DATA GenAI failure; GSMA Mobile Economy 2026; Omdia Telecoms Trends 2026; Opensignal 5G SA Status 2026-02.

### Кейсы и пресс-релизы — AIOps

Vendor platforms: Dynatrace Davis AI customer story ADT; Datadog Bits AI SRE deeper reasoning (Help Net Security 2025-12-03); Cisco ThousandEyes + Kamstrup; Kentik AI Advisor launch (BusinessWire 2025-11-18); Juniper Mist AI Marvis; ServiceNow AI Control Tower 2026. Major outages: Cloudflare 18.11.2025 outage (Cloudflare blog); AWS DynamoDB 20.10.2025 (ThousandEyes analysis, InfoQ); Azure Front Door 29.10.2025 (Microsoft public PIR, Gremlin reliability blog); CrowdStrike 19.07.2024 (Wikipedia, CISA alerts, CrowdStrike PIR); Knight Capital 2012 (SEC filings, PRMIA case study); Facebook BGP 2021 (Engineering at Meta, Cloudflare blog). AI agent failures: Replit AI agent + SaaStr database (Fortune, AI Incident Database #1152, The Register); Cursor + Claude Opus + PocketOS (TechRadar, Tom's Hardware, Live Science); Anthropic Claude Code postmortem 2026-04-23 (Anthropic engineering blog); QCon Palcuie talk on Claude Code reliability 2026-03-19 (The Register coverage). Reports: DORA 2025 (Google Cloud blog, Faros.ai); TelOps arxiv 2412.04731 (Dec 2024); Time Series Anomaly Detection AIOps arxiv 2308.00393; AIOps for Failure Management LLM Era arxiv 2406.11213.

### Кейсы и пресс-релизы — кибербезопасность

Defender side: Microsoft Security Copilot Spring 2025 evidence; CrowdStrike Charlotte AI FedRAMP High (Nov 2025); VentureBeat «CrowdStrike AI slashes SOC workloads 40+ hours/week»; Vectra AI Platform 2025 Gartner MQ Leader; Abnormal AI 2026 Attack Landscape Report; Okta Identity Threat Protection Datasheet Oct 2025; Tenable ExposureAI launch; Google Mandiant + Sec-PaLM 2. Offensive / deepfake: Arup $25.6M deepfake January 2024 (Fortune, CNN, CoverLink case study); Ferrari deepfake foiled July 2024 (Fortune, MIT Sloan, Bloomberg); WPP CEO Mark Read attempt May 2024 (TruthScan, ComplyCube); BlackMamba PoC (HYAS, DarkReading, SentinelOne pushback); WormGPT 2.0 Grok/Mixtral wrappers (CyberNews, Cato CTRL, TechRepublic); Anthropic GTG-1002 disclosure Nov 2025 (Anthropic blog + full report PDF, The Hacker News); EchoLeak CVE-2025-32711 (The Hacker News, Checkmarx, SOC Prime, arxiv 2509.10540); GitHub Copilot RoguePilot (Orca Security, PointGuard AI); HuggingFace malicious models JFrog March 2024 (JFrog, DarkReading); ChaosGPT analysis (Vice, CCN, SafeAI Newsletter). Failures / governance: Microsoft Copilot for Windows 24 durable facts violation Dec 2025; Darktrace Antigena reluctance reviews (TrustRadius, PeerSpot, Gartner Peer Insights). Reports: Verizon DBIR 2025/2026; WEF Global Cybersecurity Outlook 2026; CrowdStrike 2026 Global Threat Report; IBM Cost of a Data Breach 2024/2025; Hoxhunt 2026 Phishing Trends Report; Hoxhunt 2025 AI phishing analysis.

### Ключевые normative / methodology references

SigmaHQ rule repository (GitHub); NIST SP 800-207 Zero Trust; MITRE ATT&CK; MITRE ATLAS; OWASP ML Top 10; OWASP LLM Top 10; Google SRE Workbook (alerting on SLOs); Lockheed Martin Cyber Kill Chain; CISA Joint Cybersecurity Guidance on Deploying AI Systems Securely (April 2024).

### Дальнейшее чтение (depth для студента-исследователя)

- Russell, S., Norvig, P. (2021). «Artificial Intelligence: A Modern Approach», 4th ed. Pearson. ISBN: 978-0-13-461099-3. (Глава 19 — машинное обучение в принятии решений; глава 27 — этика и безопасность AI.)
- Goodfellow I., Bengio Y., Courville A. (2016). «Deep Learning». MIT Press. (Главы про adversarial examples и model robustness.)
- Bishop, C.M. (2006). «Pattern Recognition and Machine Learning». Springer. (Bayes-математика false positives на уровне доказательств.)
- Sheridan T.B. (2002). «Humans and Automation: System Design and Research Issues». Wiley. (Levels of automation в производственном контексте; параллель Parasuraman & Sheridan.)
- Beyer B., Jones C., Petoff J., Murphy N.R. (eds.) (2016). «Site Reliability Engineering: How Google Runs Production Systems». O'Reilly. (Канонический reference для SRE-практик, SLO burn rate methodology.)
- Anderson R. (2020). «Security Engineering», 3rd ed. Wiley. (Главы про access control, identity, evidence chain в кибербезопасности.)
- Cybersecurity и AI Special Issue журналов IEEE Security & Privacy, ACM Computing Surveys, USENIX Security Symposium proceedings (2024-2026).
- arxiv papers по prompt injection, RAG poisoning, model supply chain — текущие 2025-2026 публикации, лучше искать через MITRE ATLAS references.

---

**Конец Главы 14.** Следующая лекция — **Лекция 15: AI в науке и R&D**, начиная с AlphaFold и протеомики.

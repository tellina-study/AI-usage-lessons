---
id: s25
type: assertion_visual
duration_min: 2
version: v2.1
assertion: "Observe-уровень в cyber: EDR/XDR, NDR, email AI, identity, vuln priority. Tenable: только 3% CVE реально эксплуатируются — это математика Байеса в продакшне."
learning_goal: "Cyber Observe tools + Tenable Bayes bridge"
media_tier: "Custom python-pptx schema + Wikimedia Tier-2 photo"
media:
  - type: real_photo
    path: assets/screenshots/s25-nsoc-dashboard.jpg
    source_url: https://commons.wikimedia.org/wiki/File:NSOC-2012.jpg
    acquisition_tier: 2
    attribution_label: "Wikimedia · NSOC 2012 · public domain"
    description: "National Security Operations Center — operations floor with display wall"
---

# Observe-уровень в cyber: пять направлений в проде

## Visible content

5 карточек:
• EDR/XDR (Endpoint + Extended): CrowdStrike Falcon, SentinelOne Purple AI, Microsoft Defender. ML на телеметрии endpoint.
• NDR (Network Detection & Response): Darktrace, Vectra (Gartner Leaders 2025). Сетевые аномалии, lateral movement.
• Email AI (Phishing + BEC): Abnormal AI (Gartner Leader email security 2025). Behaviour-based, не signature.
• Identity (Поведенческая аналитика): Okta ITP (Identity Threat Protection). UEBA — User & Entity Behaviour Analytics.
• Vuln Priority (Tenable ExposureAI): Анти-шум: «только 3% CVE реально эксплуатируются». Это математика Байеса на практике — фильтрация шума.

Внизу — gold-tint:
«Tenable "только 3% CVE" — это математика Байеса в продакшне: фильтрация шума по базовой ставке эксплуатации»

## Speaker notes

Observe-уровень в кибербезопасности — пять основных направлений, где AI работает в проде.

EDR — Endpoint Detection and Response — и его расширение XDR. CrowdStrike Falcon, SentinelOne Purple AI, Microsoft Defender. Это ML над телеметрией endpoint — процессы, сетевые соединения, файловые операции, registry changes. Идея: классические сигнатуры пропускают новые малвари, ML ловит поведенческие паттерны.

NDR — Network Detection and Response. Darktrace, Vectra. В Gartner Magic Quadrant 2025 — Leaders. NDR смотрит на сетевые потоки, ищет аномалии в трафике, lateral movement атакующего внутри корпоративной сети. Особенно полезно для post-breach detection.

Email AI. Abnormal AI — Gartner Leader 2025 в email security. Не signature-based, а behavioral. Учится «нормальной» переписке: кто кому пишет, в каком стиле, в какие часы. Аномалия — alert. Это особенно полезно для BEC — Business Email Compromise атак, где сигнатур нет.

Identity protection. Okta ITP — Identity Threat Protection. UEBA — User and Entity Behaviour Analytics — на identity-данных. Аномальные логины, escalation паттерны, обход MFA.

Vulnerability prioritization. Tenable ExposureAI — это самый интересный кейс. У организации в среднем десятки тысяч open CVE в их инфре. Аналитик не может разобраться со всеми. Tenable утверждает: только три процента CVE реально эксплуатируются в реальном мире. И ExposureAI приоритизирует именно эти.

Это и есть Bayes из s21 в продакшне. Базовая ставка эксплуатации CVE низкая. Большинство — теоретические уязвимости. ML фильтрует шум по threat intel feeds, ranking, exploitation telemetry. И вместо десяти тысяч CVE — приоритизирует триста.

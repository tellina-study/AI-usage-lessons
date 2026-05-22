---
id: s17
type: assertion_visual
duration_min: 2
version: v2.4
assertion: "Act-уровень автоматического исправления: Cisco DNA, Juniper Mist, Netflix 56% инцидентов. Это работает, и именно поэтому опасно."
learning_goal: "Act-level autonomous remediation tools (setup for s18-s20)"
media_tier: "Tier 2 — Cisco HQ + Juniper Networks HQ Wikimedia (v2.3 embedded)"
media:
  - asset: assets/screenshots/s17-cisco-hq.jpg
    source_url: https://commons.wikimedia.org/wiki/File:Cisco_Systems_Headquarters_(Building_10),_Cisco_San_Jose_Main_Campus.jpg
    acquisition_tier: 2
    attribution_label: "Cisco HQ Сан-Хосе · Wikimedia"
  - asset: assets/screenshots/s17-juniper-hq.jpg
    source_url: https://commons.wikimedia.org/wiki/File:Juniper_Networks_Headquarters_Sunnyvale.jpg
    acquisition_tier: 2
    attribution_label: "Juniper Networks HQ · Wikimedia"
---

# Act-уровень: автоматическое исправление инцидентов

## Visible content

4 карточки в сетке 2×2:
• Cisco DNA Center IBN — Intent-Based Networking. Декларативный intent → автоматический translation в network config. 4000+ enterprise deployments.
• Juniper Mist Marvis Actions — AI-driven assurance. AI собирает root cause + предлагает action; в auto-mode исполняет change.
• ServiceNow Control Tower — Auto-remediation orchestration. Workflow + LLM + change-control integration в крупных enterprise.
• Netflix auto-remediation — внутреннее, утверждение самой Netflix. Заявление: 56% инцидентов в проде исправляются автоматически. Источник: Netflix Tech Blog.

Внизу — gold-tint warning:
«Это работает. И именно поэтому опасно. Дальше — каскадные сбои 2024–2025 ровно на этом уровне. CrowdStrike, Cloudflare, AWS, Azure, Replit — все на "Действует". Без поэтапной раскатки и процедуры отката — вы следующий.»

## Speaker notes

Act-уровень — это где AI выполняет финальное действие сам. Auto-remediation, kernel updates, automated configuration changes. Четыре основных инструмента в этом классе.

Cisco DNA Center с Intent-Based Networking. Это декларативная модель сети — администратор пишет интент: «вот эта группа пользователей должна иметь доступ к этой группе сервисов с такой политикой QoS». Система автоматически транслирует интент в конкретные конфиги VLAN, ACL, QoS на устройствах. Четыре с лишним тысячи enterprise deployments по миру.

Juniper Mist Marvis Actions. Juniper строит «AI-driven assurance». Marvis собирает root cause и предлагает action. В auto-mode исполняет change самостоятельно. Это уровень «Действует» в чистом виде.

ServiceNow Control Tower — оркестратор auto-remediation на enterprise уровне. Workflow integration с change-control системами, audit trail. Часто LLM в качестве decision-aid.

Netflix auto-remediation — vendor-self-claim из их собственного Tech Blog. Утверждение: пятьдесят шесть процентов инцидентов в проде исправляются автоматически без участия человека. Это серьёзная метрика, vendor-self-claim — мы не имеем независимой валидации.

Все эти инструменты работают. И именно потому что они работают — они опасны. Следующие три слайда — это четыре крупных каскадных сбоя ровно на этом уровне. CrowdStrike, Cloudflare, AWS, Azure, Replit. Каждый — пример того, что автоматизация без canary и rollback — это вопрос времени, а не возможности.
